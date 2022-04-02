import csv
import plotly.express as px

rows = []

with open("data.csv", "r") as f:
  csvreader = csv.reader(f)
  for row in csvreader: 
    rows.append(row)

headers = rows[0]
datarows = rows[1:]
print(headers)
print(datarows[0])

x=datarows[0]
y=datarows[1]

fig = px.scatter(x=x, y=y)
fig.show()