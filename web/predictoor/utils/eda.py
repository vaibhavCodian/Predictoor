import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64
# Adjusting the size of matplotlib
import matplotlib as mpl
mpl.rc('figure', figsize=(20, 40))
mpl.__version__

# # Adjusting the style of matplotlib
# plt.style.use(['fast', 'seaborn-muted'])
# plt.tight_layout()
# ____________________________

def html_table(df, size):
    html = df.head(size).to_html()
    return html

def html_desc(df):
    desc = df.describe(percentiles=[.2, .35])
    html = desc.to_html()
    return html

def nullAnal(df):
    data = df.columns[df.isnull().any()]
    df_ = pd.DataFrame(df[data].isnull().sum()).T
    return df_.to_html()


def correlation(df):
    corr = df.corr()
    c = corr.style.background_gradient(cmap='Blues_r')
    cData = c.render()
    return cData

# for plots
def p_scatter(x, y):
    # print("x :"+ x)
    # print("x :"+ y)
    plt.clf()
    plt.style.use('seaborn-whitegrid')
    plt.scatter(x, y)
    plt.xlabel(x.name)
    plt.ylabel(y.name)
    # Saving Scatter_/
    figfile = BytesIO()
    plt.savefig(figfile, format='png', bbox_inches='tight', transparent=True)
    figfile.seek(0)  # rewind to beginning of file
    figdata_scatter = figfile.getvalue()  # extract string (stream of bytes)
    figdata_scatter = base64.b64encode(figdata_scatter)
    return figdata_scatter
    
def p_bar(x, y):
    plt.clf()
    plt.style.use("_classic_test");
    plt.bar(x, y)
    plt.xlabel(x.name)
    plt.ylabel(y.name)
    # Saving Scatter_/
    figfile = BytesIO()
    plt.savefig(figfile, format='png', bbox_inches='tight', transparent=True)
    figfile.seek(0)  # rewind to beginning of file
    figdata_bar = figfile.getvalue()  # extract string (stream of bytes)
    figdata_bar = base64.b64encode(figdata_bar)
    return figdata_bar

def p_pie(x, y):
    plt.clf()
    plt.style.use("seaborn-whitegrid")
    sums = y.groupby(x).sum()
    plt.pie(x=sums, labels=sums.index)
    plt.xlabel(x.name)
    plt.ylabel(y.name)
    plt.tight_layout()
    # Saving Pie_/
    figfile = BytesIO()
    plt.savefig(figfile, format='png', bbox_inches='tight', transparent=True)
    figfile.seek(0)  # rewind to beginning of file
    figdata_bar = figfile.getvalue()  # extract string (stream of bytes)
    figdata_bar = base64.b64encode(figdata_bar)
    return figdata_bar

def p_hist(x, bin):
    plt.clf()
    plt.style.use('seaborn-whitegrid')
    plt.hist(x, bins=bin)
    plt.xlabel(x.name)
    # Saving Scatter_/
    figfile = BytesIO()
    plt.savefig(figfile, format='png', bbox_inches='tight', transparent=True)
    figfile.seek(0)  # rewind to beginning of file
    figdata_hist = figfile.getvalue()  # extract string (stream of bytes)
    figdata_hist = base64.b64encode(figdata_hist)
    return figdata_hist


