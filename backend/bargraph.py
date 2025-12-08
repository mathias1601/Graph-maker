from io import BytesIO
from fastapi import File, Response
from matplotlib import pyplot as plt
import pandas as pd

def bar_graph(groupName: str, columnValue: str,  title: str, csvFile: File, summedData: str = "sum"):

    # Read csv file
    df = pd.read_csv(csvFile.file)

    labels, values = [], []

    match summedData:
        case "sum":
            labels, values = sum_graph(df, groupName, columnValue)
        case "avg":
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