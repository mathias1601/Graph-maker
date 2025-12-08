from io import BytesIO
from fastapi import File, Response
from matplotlib import pyplot as plt
import pandas as pd

# Helper-function for creating a list of values for each group
def get_group_arrays(dataFrame, groupName, columnValue):

    summedData = dataFrame.groupby([groupName], as_index=False).agg(list)
    return summedData[groupName], summedData[columnValue]

def box_plot(groupName: str, columnValue: str, csvFile: File, title: str = "Title"):

    # Read csv file
    df = pd.read_csv(csvFile.file)

    labels, values = get_group_arrays(df, groupName, columnValue)
    values = list(values)
    print(values)

    # Convert to string in case of extra tick markers
    labels = [str(label) for label in labels]

    # Generate plot
    fig, ax = plt.subplots()
    ax.boxplot(values, labels=labels)
    ax.set_title(title)
    ax.set_xlabel(groupName)
    ax.set_ylabel(columnValue)

    # Save the plot into an in-memory buffer
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    plt.close(fig)
    buffer.seek(0)

    return Response(content=buffer.getvalue(), media_type="image/png")