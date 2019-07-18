# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 10:20:14 2019

@author: admin
"""

#day 4 data visualization
import plotly
import pandas 

studentlist = [["Steve", 32, "male"], ["Lia",28, "female"], ["Vin", 45, "male"], ["Kate", 38, "female"]]
print(studentlist)

studentlistdf = pandas.DataFrame(studentlist, columns = ["Name", "Age", "Gender"]
print(studentlistdf)

#graph our data
dir(plotly)
from plotly.offline import plot
import plotly.graph_objs as go

agename = go.Bar(x=studentlistdf["Name"], y=studentlistdf["Age"])

plot([agename])

#project, women in occupations
import pandas as pd
from plotly.offline import plot
import plotly.graph_objs as go

#we read the data into a dataset or data frame called df
df = pd.read_excel("GISdata.xlsx", sheet_name = "womenOccupation")

#we use the bar graph option out of the graph_objs function from the plotly library
womenoccupation= go.Bar(x=df["occupation"], y=df["women"], 
                        marker = {"color": df["women"], "colorscale": "Jet"})

#we call the plot function from the plotly.offline library
plot([womenoccupation])

#OR we use the figure option out of the graph_objs function from the plotly library
fig = go.Figure(data=[womenoccupation])
plot(fig)

#we use the Layout option of the graph_objs function from the plotly library
titles = go.Layout(title = "Percentage of Women Employed by Occupation",
                    xaxis=go.layout.XAxis(title = go.layout.xaxis.Title(text="Occupation",)),

                    yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text="Percentage",))                                                
                                                                      
                                                                      
                 )                                                  

#we use figure option of the graph_opts function from the plotly library
fig = go.Figure(data=[womenoccupation], layout = titles)

#we call the plot function from the plotly.offline library
plot(fig)

