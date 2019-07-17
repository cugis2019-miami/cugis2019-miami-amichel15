# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 10:02:03 2019

@author: admin
"""

#code to describe types and numbers of chocolate bars in box"
 def chocolates (M, D, W):
     print("there are", M, "milk chocolate bars,", D, "dark chocolate bars, and", W, "white chocolate bars.")
     
chocolates(5, 3, 8)

#dict data structure, 3 variables, 6 pieces of information
chocolate1 = {"milk":5}
chocolate2 = {"dark": 3}
chocolate3 = {"white":8}

#dict data structure, 1 variable, 6 pieces of information
chocolatebox =  {"milk":5, "dark":3, "white": 8}

#to call up information on data structure 
print(chocolatebox)

namegender = {"Steve":"male", "Lia":"female", "Vin": "male", "Katie":"female"}
nameage = {"Steve": 32, "Lia": 28, "Vin":45, "Katie":38}

print("the number of milk chocolates in chocolate box is", chocolatebox["milk"])

print("the number of white chocolates in chocolate box is", chocolatebox["white"])

print("Lia's age is", nameage["Lia"], "and gender is", namegender["Lia"])

import pandas

dir(pandas)

#to change chocolate box information into table 
chocolateinfo = pandas.Series(chocolatebox)   #pandas.Series converts into tabular data
print(chocolateinfo)

#lists. dict to list
chocolatedata = [chocolatebox]
print(chocolatedata)

#data frame
chocolatedf = pandas.DataFrame(chocolatedata, index = ["quantity"])  #convert to column
print(chocolatedf)

#practice dataframes from lists
studentallinfo = [["Steve", 32, "male"], ["Lia", 28, "female"]]
df = pandas.DataFrame(studentallinfo)
print(df)


df2 = pandas.DataFrame(studentallinfo, columns=["Name", "Age", "Gender"])
print(df2)

#more practice
data = [nameage,namegender] #using dict convert to list
print(data)

df3 = pandas.DataFrame(data)
print(df3)
