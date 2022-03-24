import plotly.express as px
import numpy as np 
import csv

def getDataSource(dp):
    marks = []
    days = []
    with open(dp) as d:
        df = csv.DictReader(d)
        for i in df:
            marks.append(float(i["Marks In Percentage"]))
            days.append(float(i["Days Present"]))
    return {"x":marks, "y":days}

def findCorrelation(ds):
    c = np.corrcoef(ds["x"],ds["y"])
    print(c[0,1])
def setup():
    gds = getDataSource("Project\Student Marks vs Days Present.csv")
    findCorrelation(gds)    
setup()
