import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import math

def Output_Graph():
    buffer = BytesIO()
    plt.savefig(buffer,dpi=100, format="png")
    plt.close()
    buffer.seek(0)
    img   = buffer.getvalue()
    graph = base64.b64encode(img)
    graph = graph.decode("utf-8")
    buffer.close()
    return graph


def Plot_Hist(x,color,title,label_name):
    plt.hist(x,stacked=True,bins=30,color=color,label=label_name,alpha=0.3,ec="black")
    plt.title(title)
    plt.xlabel(title)
    plt.ylabel("occurrence")
    plt.legend()
    graph=Output_Graph()
    return graph
