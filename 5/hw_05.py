
import xlrd, xlwt
import pandas as pd
import sys
from pandas import Series, DataFrame
path = "D:/ts/Learn_Python/5/hw_data/"


file = Series({"App-Shipments" : "ApplianceShipments.xls",
                "Creditcard":"creditcard-dataset.txt",
                "DressSales":'DressSales.csv'
                })

# read DressSales
DressSales = pd.read_csv(path+file["DressSales"], index_col=['Dress_ID'],)
DressSales[:3]

# read Creditcard
names = ["type","money1","money2",
        "code1","code2","code3",
        "code4","money3","t"
        "t1","number","f/t","g","money4",
        "money5","+/-"]

string=[]
for i in range(1,17):
    string.append(str(i))

name = map(lambda x: 'col'+x, string)

Creditcard = pd.read_table(path+file["Creditcard"],header=None,
                            names = name,
                            sep=','
                            )
Creditcard[:3]


# pandas read xls
xls_file=pd.ExcelFile(path +file["App-Shipments"])
table=xls_file.parse('Data')
table