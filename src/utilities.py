import pandas as pd
import pymongo 
import json



def row_to_json(row):
    
    """
    Converts a row of this dataset into a json object with a variable number of fields.
    """
    li = []
    res = "{"
    
    for key in row.keys():
        
        val = row[key]
        
        if val == "X":
            val = 'true'
            
        try:
            int(val)
            float(val)
        except:
            if val!='true':
                val = f"\"{val}\""
        
        li.append((key, val))
    
    for tup in li:
        res+=f"\"{tup[0]}\" : {tup[1]}, "
    
    res = res.strip(", ")
    res+="}"
    return res



def dataframe_to_json_array(df):
    """
    Convert a dataframe into a jsonarray.
    Each row of the df is treated as a json object.
    """
    json_objects = df.apply(lambda x : row_to_json(x), axis=1)
    json_array = "[ "
    for obj in json_objects:
        json_array+=obj+", "
    json_array = json_array.strip(", ")
    json_array+=" ]"
    return json_array


def get_n_months_between_to_months_name(name1, name2):  
    
    months = ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"]
    
    # strange case when a plant has two flowering periods
    if (name2 == "Aprsett"):
        return 4
    ## strange case when the person has inserted strange month name
    if (name1 == "Apile"):
        name1 = "Aprile"
    if (name1 == "Giungo"):
        name1 = "Giugno"
    if (name2 == "Agoso"):
        name2 = "Agosto"
    """
    Calculates the number of months between two months name
    """
    return months.index(name2) - months.index(name1) + 1




def get_score_sum(singular_species):
    
    """
    Calculates the summed-score of a plant, based on 8 relevant metrics.
    
    Source: http://csu.unipv.it/wp-content/uploads/2022/01/Tesi-Colombini.pdf
    THE 8 RELEVANT METRICS ARE:
    - Forma biologica
    - Vistosità
    - Durata del periodo di fioritura
    - Presenza sul mercato di specie simili
    - Aromaticità
    - Tipo di impollinazione
    - Allergenicità
    - Tossicità
    IMPORTANT: READ ABOUT EACH OF THE 8 METRICS.
    THE METRICS VALUES IN EACH PLANT IS WRITTEN CORRECTLY (for example, if the plant is not
    toxic its value is 1, viceversa it is 0...) SO WE DO NOT HAVE TO CONSIDER THEM DIFFERENTLY
    """
    
    #REFACTOR
    overall = float(singular_species["FORMA BIOLOGICA"])
    if (singular_species["VISTOSITA'"] == 1):
        overall += 1
    if (not pd.isna(singular_species["PRESENZA MERCATO"])):
        overall += 1
    if (singular_species["IMPOLLINAZIONE"] == 1):
        overall += 1
    if (singular_species["ALLERGENICITA’"] == 1):
        overall += 1
    if (singular_species["TOSSICITA’"] == 1):
        overall += 1
    if (singular_species["AROMATICA"] == 1):
        overall += 1
        
    """
    According to the Colombini thesis, if the "PERIODO FIORITURA" is 
    #  - 1/2 months: 1 point
    #  - 3/4 months: 2 points
    #  - more than 4 months: 3 points
    """
    periodo_fioritura = str(singular_species['PERIODO FIORITURA']).replace(".", "-")
    if (("ogni mese dell’anno" in periodo_fioritura) or ("Tutto l’anno" in periodo_fioritura)):
        overall += 3
    else:
        name1 = str(periodo_fioritura).split("-")[0].capitalize().replace(" ", "")
        name2 = str(periodo_fioritura).split("-")[1].capitalize().replace(" ", "")
        if (1 <= get_n_months_between_to_months_name(name1, name2) <= 2):
            overall += 1
        elif(3 <= get_n_months_between_to_months_name(name1, name2) <= 4):
             overall += 2
        else:
            overall += 3
    return overall


def get_ornamental_index_value(singular_species):
    
    """
    Source: http://csu.unipv.it/wp-content/uploads/2022/01/Tesi-Colombini.pdf
    Sommatoria dei punteggi compresa tra 2 e 5 inclusi: valore dell’indice 1.
    Al range 6 - 9 inclusi: valore dell’indice 2. 
    Punteggio superiore a dieci: l’indice assegnato è 3. 
    """
    
    score_sum = get_score_sum(singular_species)
    if  2 <= score_sum <= 5:
        return 1
    elif 6 <= score_sum <= 9:
        return 2
    elif score_sum >= 10:
        return 3
    
    
    
def get_setting(setting):
    df = pd.read_csv("../settings/db_config.csv")
    return df.loc[df.key==setting, "val"].values[0]

def get_connection_string():
    return f"mongodb+srv://{get_setting('username')}:{get_setting('password')}@{get_setting('cluster')}/{get_setting('database')}?retryWrites=true&w=majority"




def store_into_mongodb_istance(json_file):
    
    """
    json_file should be an actual list of json objects (non-stringified).
    
    eg:
    
    " [ {"mondo" : "world"}, {"capra" : "goat"}] "
    
    A python list of dictionaries.
    
    """
    
    conn_string = get_connection_string()
    
    client = pymongo.MongoClient(conn_string)
    
    # OVE: stands for Ornamental Value Estimation
    client.OVE.data.insert_many(json_file)
    
    
def store_locally(json_file):
    with open('../ornamental_db.json', 'w+') as dest:
        json.dump(json_file, dest)