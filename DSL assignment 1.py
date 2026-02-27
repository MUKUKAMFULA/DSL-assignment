# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 08:58:25 2026
First line plot shows the GDP growth observations against the years which 
starts from 2019-2024 to show how GDP growth has been affected by COVID-19
CSV file used to read the data is based on public information and the data 
was cleaned to get the desired results.

Second pie chart shows the share of the total population each age group from
25 and older has in United Kingdom. CSV file used to read the data is
based on public information and the data was cleaned to get the desired 
results.

Third bar graph shows the meat production in tonnes of every region in the 
world. CSV file used to read the data is based on public information
and the data was cleaned to get the desired results. 




@author: Mukuka Noward Mfula
"""
#importing the packages that are going to be used
import pandas as pd
import matplotlib.pyplot as plt
#defining the function for the line plots
#####################################################################
def line_plot(lenght,countries,filename,name_country):
    """
    Creates the line graph. legnth is used for the length of the line.
    countries is used for the labels. filename is the name of the file.
    It is important to note that this is only for one given country at
    a time.
    """
    plt.figure()
    #first argument on the x axis produces the plot  
    #second argument on  the y axis produces the length
    plt.plot(lenght,countries)
    plt.title(f"Growth observation; {name_country}")
    plt.xlabel("YEARS")
    plt.ylabel("percent")
    plt.savefig(filename)
    plt.show()
    return
#the progam that is used to call the function
#reading data from United States of America csv file into df_USA
df_USA = pd.read_csv("United States of America.csv")
#creating the arguments for the function
USA = df_USA["Year"]
countries = df_USA["GDP growth observations in percent"]
name_country = "USA"
#reading data from United Kingdom  csv file into df_UK
df_UK = pd.read_csv("United kingdom.csv")
#creating the arguments for the function
UK = df_UK["Year"]
countries_2 = df_UK["GDP growth observations"]
name_country2 = "United Kingdom"
#reading data from Germany csv file into df_Germany
df_Germany=pd.read_csv("Germany.csv")
#creating the arguments for the function
Germany = df_Germany["Year"]
countries_3 = df_Germany["GDP growth observations"]
name_country3 = "Germany"
#reading data from Japan csv file into df_Japan
df_Japan=pd.read_csv("Japan.csv")
#creating the arguments for the function
Japan = df_Japan["Year"]
countries_4 = df_Japan["GDP growth observations"]
name_country4 = "Japan"
#reading data from France csv file into df_France
df_France=pd.read_csv("France.csv")
#creating the arguments for the function
France = df_France["Year"]
countries_5 = df_France["GDP growth observations"]
name_country5 = "France"
#reading data from China csv file into df_China
df_China=pd.read_csv("China.csv")
#creating the arguments for the function
China = df_China["Year"]
countries_6 = df_China["GDP growth observations"]
name_country = "China"
#reading data Canada csv file into df_Canada
df_Canada=pd.read_csv("Canada.csv")
#creating the arguments for the function
Canada = df_Canada["Year"]
countries_7 = df_Canada["GDP growth observations"]
name_country7 = "Canada"
#creating a plot  for all the countries on one graph
plt.figure()
#creating the line for USA at alpha=0.7 for transperancy
plt.plot(df_USA["Year"],df_USA["GDP growth observations in percent"],
         label = "USA",alpha=0.7)
#creating the line for UK at alpha=0.7 for transperancy
plt.plot(df_UK["Year"],df_UK["GDP growth observations"],
         label = "UK",alpha=0.7)
#creating the line for Germmany at alpha=0.7 for transperancy
plt.plot(df_Germany["Year"],df_Germany["GDP growth observations"],
         label = "Germany",alpha=0.7)
#creating the line for Japan at alpha=0.7 for transperancy
plt.plot(df_Japan["Year"],df_Japan["GDP growth observations"],
         label = "Japan",alpha=0.7)
#creating the line for France at alpha=0.7 for transperancy
plt.plot(df_France["Year"],df_France["GDP growth observations"],
         label = "France",alpha=0.7)
#creating the line for China at alpha=0.7 for transperancy
plt.plot(df_China["Year"],df_China["GDP growth observations"],
         label = "China",alpha=0.7)
#creating the line for USA at alpha=0.7 for transperancy
plt.plot(df_Canada["Year"],df_Canada["GDP growth observations"],
         label = "Canada",alpha=0.7)
#label shwoing the yearfor x axis 
plt.xlabel("Year")
#label showing growth observation in percentage for the y label
plt.ylabel("Growth observation in percentage")
#legend to be used as a guide for people viewing the graph
plt.legend()
#####################################################################
"""
Pie chart for age distribution of the United Kingdom adult population 
older than 25 years.

"""

df_population = pd.read_csv("Age Distribution in United Kingdom (2023).csv")
plt.figure()
plt.pie(df_population["Variable observation value"], 
        labels=df_population["Variable properties name"],normalize=True)
plt.title("Population in the United Kindgom by Age")
plt.show()


#####################################################################
def plot_bar(production,continents,filename):
    colours = ["red","blue","green","yellow","orange","purple"]
    labels = ["Africa","Asia", "Europe","North America","Ocenia", 
              "South America"]
    plt.figure(figsize=(10,6))
    plt.bar(continents,production,color=colours,label=labels)
    plt.xlabel("Continents")
    plt.ylabel("production in tonnes 100,000,000")
    plt.title("Global Meat Production in 2023 by continents")
    plt.legend()
    plt.savefig(filename)
    plt.show()
    
    return
#the progam that is used to call the function
#reading data global-meat-production.csv in df_meatproduction
df_meatproduction = pd.read_csv("global-meat-production.csv")
#the variables in the function
meat_prod2023 = df_meatproduction["All meat - Production (tonnes)"]
continents = df_meatproduction["Entity"]
#calling the function
plot_bar(meat_prod2023, continents, "meat.png")
