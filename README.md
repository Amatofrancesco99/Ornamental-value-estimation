# Ornamental value estimation
![](https://komarev.com/ghpvc/?username=OVE&label=Views&style=plastic&color=brightgreen)

![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Microsoft Excel](https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)

[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)

## 💐 Brief description
This project is related to a No-SQL database, whose data are referred to *autoctone botanic species*. 
<br>
The final goal is creating a function that performs the estimation of the ornamental value, given the specific characteristics of a single species.
<br>
(The ornamental value is a figure of merit that can be used in order to decide if a specific species can be planted in a specific area.
The higher the ornamental value, the best the result)
<br><br>
You can find an in-depth study of this topic, at this **[link](http://csu.unipv.it/wp-content/uploads/2022/01/Tesi-Colombini.pdf)**.


## 🖥 Download
If you want to download the whole ```.json``` file, click here:
<a href="https://drive.google.com/uc?export=download&id=1qbFqC_eSVcBgorBP0HvW2fprnrDihGQP" ><strong>DOWNLOAD</strong></a>

## 🎥 Presentation
For the pdf presentation of the project, this is the <a href="https://github.com/Amatofrancesco99/Ornamental-value-estimation/blob/main/presentation/presentation.pdf">link</a>


## ℹ️ Other


<details>
  <summary><b><strong>SETTING UP THE LOCAL ENVIRONMENT</strong></b></summary>

### 1) Clone this repo
...and navigate to its root directory.

  
### 2) Create a python virtual environment 
...calling it '.my_env' 

(For gitignore-related reasons).

```
$ python3 -m venv .my_env
```

(You'll be prompted to install the 'venv' module if you don't have it yet).

  
### 3) Activate the virtual environment:

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

  
### 4) Install this app's dependencies 
... on the virtual environment you just created:
  
```
(.my_env)$ pip install -r requirements.min.txt
```

Or:
  
```
(.my_env)$ pip install -r requirements.txt
```
If you want to install the exact tested versions of the libraries.
  
</details>



<details>
  <summary><b><strong>RUN THE APP ON LOCALHOST (JUPYTER NOTEBOOK)</strong></b></summary>

### 1) Install jupyter notebook on your own device (if you don't have it yet)
  
```
(.my_env)$ pip install notebook
```
(But it should already be included in the requirements as 'jupyter').
  
### 2) Run jupyter notebook (if you already downloaded it)
  
```
(.my_env)$ jupyter notebook
```

### 3) Open the ```main.ipynb``` file
  
### 4) Enjoy 🤠
  
</details>



<details>

<summary><b><strong> CREDENTIALS FOR THE DB </strong></b></summary>

Please remember to create the file settings/db_config.csv and fill it up as such:

```
key,val
username,<yourusernamehere>
password,<yourpasswordhere>
database,<yourdbsnamehere>
cluster,<yourclusterhere>
```
  
</details>

  

<details>
  <summary><b><strong>ENABLE DARK THEME ON JUPYTER NOTEBOOK </strong></b></summary>

![image](https://user-images.githubusercontent.com/80333091/149359355-6f027794-931e-45ef-95d0-4857dd9bd477.png)
     
```
pip install jupyterthemes
jt -t chesterish
```
     
</details>
