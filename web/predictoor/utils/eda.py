import pandas as pd
def html_table(df, size):
    html = df.head(size).to_html(classes = 'female')
    return html

def html_desc(df, size):
    html = df.df.describe(percentiles=[.2, .25])
    return html

