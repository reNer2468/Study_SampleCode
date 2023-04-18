import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import math

def Output_Graph():
    buffer = BytesIO()                   #バイナリI/O(画像や音声データを取り扱う際に利用)
    plt.savefig(buffer,dpi=100, format="png")    #png形式の画像データを取り扱う
    plt.close()
    buffer.seek(0)                       #ストリーム先頭のoffset byteに変更
    img   = buffer.getvalue()            #バッファの全内容を含むbytes
    graph = base64.b64encode(img)        #画像ファイルをbase64でエンコード
    graph = graph.decode("utf-8")        #デコードして文字列から画像に変換
    buffer.close()
    return graph


def Plot_Hist(x,color,title,label_name):
    plt.hist(x,stacked=True,bins=30,color=color,label=label_name,alpha=0.3,ec="black")
    #plt.axvline(x=entire_average,lw=2,color=plt.cm.hsv(10),label="全体平均")
    #plt.axvline(x=series_average,lw=2,color=plt.cm.hsv(80),label="検索結果の平均")
    plt.title(title+"のヒストグラム")
    plt.xlabel(title)
    plt.ylabel("出現数")
    plt.legend()
    graph=Output_Graph()
    return graph
