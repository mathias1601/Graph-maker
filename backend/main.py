from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import Response
import pandas as pd
import matplotlib

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
    return summedData[groupName], summedData[columnValue]

@app.post("/plot")
def create_basic_plot(groupName: str = Form(...), columnValue: str = Form(...),  title: str = Form("Title"), csvFile: UploadFile = File(...)):

    # Read csv file
    df = pd.read_csv(csvFile.file)
    
    labels, values = avg_graph(df, groupName, columnValue)

    # Convert to string in case of extra tick markers
    labels = [str(label) for label in labels]

    # Generate plot
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_title(title)
    ax.set_xlabel(groupName)
    ax.set_ylabel(columnValue)

    # Save the plot into an in-memory buffer
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    plt.close(fig)
    buffer.seek(0)

    return Response(content=buffer.getvalue(), media_type="image/png")




