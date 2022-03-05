import json
import pandas as pd
import pymongo


def get_n_months_between_to_months_name(name1, name2):  
    months = ['Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno', 'Luglio', 'Agosto', 'Settembre', 'Ottobre', 'Novembre', 'Dicembre']
    
    # Strange case when a plant has two flowering periods
    if (name2 == 'Aprsett'):
        return 6

    # Strange case where we find strange month names
    if (name1 == 'Apile'):
        name1 = 'Aprile'
    if (name1 == 'Giungo'):
        name1 = 'Giugno'
    if (name2 == 'Agoso'):
        name2 = 'Agosto'

    # Calculates the number of months between two months names
    return months.index(name2) - months.index(name1) + 1


def get_score_sum(singular_species):
    """
    Calculates the score sum for a plant, based on 8 relevant metrics.

    The 8 relevant metrics are:
        - Forma biologica
        - Vistosità
        - Durata del periodo di fioritura
        - Presenza sul mercato di specie simili
        - Aromaticità
        - Tipo di impollinazione
        - Allergenicità
        - Tossicità

    Important: read about each of the 8 metrics.

    The metrics values in each plant are written correctly (for example, if the plant is not
    toxic the value is 1, viceversa it is 0) so we do not have to consider them differently.

    Source: http://csu.unipv.it/wp-content/uploads/2022/01/Tesi-Colombini.pdf
    """

    overall = float(singular_species['FORMA BIOLOGICA'])
    if (not pd.isna(singular_species['PRESENZA MERCATO'])):
        overall += 1
    for metric in ['VISTOSITA\'', 'IMPOLLINAZIONE', 'ALLERGENICITA’', 'TOSSICITA’', 'AROMATICA']:
        if (singular_species[metric] == 1):
            overall += 1

    # According to the Colombini thesis, if 'PERIODO FIORITURA' is 
    #     - 1/2 months: 1 point
    #     - 3/4 months: 2 points
    #     - more than 4 months: 3 points

    periodo_fioritura = str(singular_species['PERIODO FIORITURA']).replace('.', '-')
    if (('ogni mese dell’anno' in periodo_fioritura) or ('Tutto l’anno' in periodo_fioritura)):
        overall += 3
    else:
        name1 = str(periodo_fioritura).split('-')[0].capitalize().replace(' ', '')
        name2 = str(periodo_fioritura).split('-')[1].capitalize().replace(' ', '')
        if 1 <= get_n_months_between_to_months_name(name1, name2) <= 2:
            overall += 1
        elif 3 <= get_n_months_between_to_months_name(name1, name2) <= 4:
             overall += 2
        else:
            overall += 3
    return overall


def get_ornamental_index_value(singular_species):
    """
    Sommatoria dei punteggi compresa tra 2 e 5 inclusi: valore dell'indice 1.
    Al range 6 - 9 inclusi: valore dell'indice 2.
    Punteggio superiore a 10: l'indice assegnato è 3.
    
    Source: http://csu.unipv.it/wp-content/uploads/2022/01/Tesi-Colombini.pdf
    """

    score_sum = get_score_sum(singular_species)
    if 2 <= score_sum <= 5:
        return 1
    elif 6 <= score_sum <= 9:
        return 2
    elif score_sum >= 10:
        return 3
    else:
        return None


def get_setting(setting):
    df = pd.read_csv('../settings/db_config.csv')
    return df.loc[df.key==setting, 'val'].values[0]


def get_connection_string():
    return f"mongodb+srv://{get_setting('username')}:{get_setting('password')}@{get_setting('cluster')}/{get_setting('database')}?retryWrites=true&w=majority"


def store_into_mongodb_istance(json_object):
    """
    Argument json_object should be a (non-serialized) list of json objects, e.g.:

    " [ {"mondo" : "world"}, {"capra" : "goat"}] "

    That is, A Python list of dictionaries.
    """

    client = pymongo.MongoClient(get_connection_string())

    # Clear any data that is already there
    client.OVE.data.delete_many({})

    # Insert the new object
    client.OVE.data.insert_many(json_object)


def store_locally(json_object):
    with open('../ornamental_db.json', 'w+') as output_file:
        json.dump(json_object, output_file, indent=4)
