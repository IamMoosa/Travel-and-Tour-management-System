# Tour and Travel Management System

Basic Demo Tour and Travel Management System built with python and Microsoft SQL Server Management Studio

`Note: You must have Microsoft SQL Server Management Studio installed`

# Create DataBbase

Open the 'ProjectTTMS.sql' file with ssms and execute the file.
It will create the database, Create tables and insert data in it.


# Getting Started

Clone this repo in your local machine using,

```bash
git clone https://github.com/IamMoosa/Travel-and-Tour-management-System.git
```

Run this command to install required modules,

```bash
pip install -r requirements.txt
```

#Change Server Name

In 'ProjectTTMS.py' file,
replace <Your-Server-Name-Here> with server name you are running on your local machine,

```bash
connection = pyodbc.connect('Driver={SQL Server};' 'Server=<Your-Server-Name-Here>;' 
'Database=projectTTMS;' 'Trusted_connection=yes;')
```

Enter this command to run,

```bash
python ProjectTTMS.py
```
