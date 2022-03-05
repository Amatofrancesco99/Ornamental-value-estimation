# Ornamental Value Estimation
![](https://komarev.com/ghpvc/?username=OVE&label=Views&style=plastic&color=brightgreen)

![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Microsoft Excel](https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)

[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)

## 💐 Brief Description
This project is related to a No-SQL database, whose data are referred to *autoctone botanic species*. 

The final goal is creating a function that performs the estimation of the ornamental value, given the specific characteristics of a single species.

(The ornamental value is a figure of merit that can be used in order to decide if a specific species can be planted in a specific area.
The higher the ornamental value, the best the result)

You can find an in-depth study of this topic at [this link](http://csu.unipv.it/wp-content/uploads/2022/01/Tesi-Colombini.pdf).

## 🖥 Download
[Link to the whole **`.json` database** file](https://drive.google.com/uc?export=download&id=1qbFqC_eSVcBgorBP0HvW2fprnrDihGQP).

## 🎥 Presentation
[Link to the **`.pdf` presentation**](https://github.com/Amatofrancesco99/Ornamental-value-estimation/blob/main/presentation/presentation.pdf) of the project.

## ℹ️ Other
<details>
<summary><b>Setting up the local environment</b></summary>
### 1) Clone This Repo
...and navigate to its root directory.

  
### 2) Create a Python Virtual Environment 
...calling it '.my_env' 

(For gitignore-related reasons).

```
$ python3 -m venv .my_env
```

(You'll be prompted to install the 'venv' module if you don't have it yet).

  
### 3) Activate the Virtual Environment

```
$ source .my_env/bin/activate
```

If this command doesn't work try with:

```
$ . .my_env/bin/activate
```
  
In Windows 10 try with :
```
.\.my_env\Scripts\activate.bat
```

(You should notice that the console starts displaying the virtual environment's name before your username and the dollar-sign).
  
### 4) Install this App's Dependencies 
In the virtual environment you just created run:
  
```
(.my_env)$ pip install -r requirements.min.txt
```

If instead you want to install the very same versions of the libraries that we used run:
  
```
(.my_env)$ pip install -r requirements.txt
```
</details>

<details>
<summary><b>Run the app on `localhost`</b></summary>  
### 1) Run `jupyter` Notebook
  
```
(.my_env)$ jupyter notebook
```

### 2) Open `main.ipynb` and Enjoy 🤠
</details>

<details>
<summary><b>Setup the database credentials</b></summary>
The file `settings/db_config.csv` should contain the configuration settings needed to connect to the MongoDB instance.

The file format should be as follows:

```
key,val
username,<your-username-here>
password,<your-password-here>
database,<your-database-name-here>
cluster,<your-cluster-address-here>
```
</details>

<details>
<summary><b>Enable the dark theme on `jupyter` notebook</b></summary>
To switch to the dark `jupyter` notebook theme run: 

```
(.my_env)$ pip install jupyterthemes
(.my_env)$ jt -t chesterish
```

![image](https://user-images.githubusercontent.com/80333091/149359355-6f027794-931e-45ef-95d0-4857dd9bd477.png)
</details>
