# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)


import pymysql
import matplotlib.pyplot as plt

f = open("conf.txt", "r")
strin = f.readlines()

db = pymysql.connect(host=strin[0][0:-1],user=strin[1][0:-1],password=strin[2][0:-1])
cursor = db.cursor()

cursor.execute("use ACQ")
cursor.fetchone()



cursor.execute("select Value,timeOfProbe from ACQ.historian where ID_Location = 4 AND timeOfProbe > '2023-01-01' AND timeOfProbe < '2023-01-10' ORDER BY timeOfProbe desc ")
data = cursor.fetchall()

tab = []
ox = []
i = 0
for x in range(len(data)):
    if data[x][0] < 60:
        tab.append(data[x][0]*(-0.5)+40)
        ox.append(data[x][1])
        i+=1

x = ox
y = tab

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": x,
    "Amount": y#,
    #"City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.line(df, x="Fruit", y="Amount")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)