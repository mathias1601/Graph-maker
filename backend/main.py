from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import Response
import pandas as pd
import matplotlib
from violinplot import violin_plot
from bargraph import bar_graph
from boxplot import box_plot

# To disable the matplotlib GUI
matplotlib.use("Agg") 

import matplotlib.pyplot as plt
from io import BytesIO
from fastapi.middleware.cors import CORSMiddleware

items = []

app = FastAPI()

origins = [
    "http://localhost:3000", 
    "http://localhost:3001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],    
    allow_headers=["*"],    
)

# Helper-function for creating graphs which sums values of each label
def avg_graph(dataFrame, groupName, columnValue):

    summedData = dataFrame.groupby([groupName], as_index=False).mean()
    return summedData[groupName], summedData[columnValue]

# Helper-function for creating graphs which creates the average values of each label
def sum_graph(dataFrame, groupName, columnValue):

    summedData = dataFrame.groupby([groupName], as_index=False).agg({columnValue: "sum"})
    print(summedData)
    return summedData[groupName], summedData[columnValue]

@app.post("/box_plot")
def create_box_plot(groupName: str = Form(...), columnValue: str = Form(...),  title: str = Form("Title"), csvFile: UploadFile = File(...)):
    return box_plot(groupName=groupName, columnValue=columnValue, title=title, csvFile=csvFile)


@app.post("/bar_graph")
def create_bar_graph(groupName: str = Form(...), columnValue: str = Form(...),  title: str = Form("Title"), summedData: str = Form("sum"), csvFile: UploadFile = File(...)):
    return bar_graph(groupName=groupName, columnValue=columnValue, title=title, csvFile=csvFile, summedData=summedData)


@app.post("/violin_plot")
def create_violin_plot(groupName: str = Form(...), columnValue: str = Form(...),  title: str = Form("Title"), csvFile: UploadFile = File(...)):
    return violin_plot(groupName=groupName, columnValue=columnValue, title=title, csvFile=csvFile)




