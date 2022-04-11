# ---------------------------------Importing all the libraries needed-------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import seaborn as sns
import plotly.express as px
# ---------------------------------Reading the data from csv files with pandas-----------------

Data = pd.read_csv("covid_19_india.csv")

# -------------------------------- Data Pre-processing: remove,add,change---------------

Data.drop(["Sno", "Time", "ConfirmedIndianNational", "ConfirmedForeignNational"], axis=1, inplace=True)  # Removing
Data["Date"] = pd.to_datetime(Data["Date"])  # type casting
Data.rename(columns={"Cured": "Recovered"}, inplace=True)  # renaming
Data["Active"] = Data["Confirmed"] - (Data["Recovered"] + Data["Deaths"])  # adding new columns

# ---------------------------------Adding more required dataframes----------------------

group_by_date = Data.groupby("Date")[["Recovered", "Deaths", "Confirmed", "Active"]].sum().reset_index()
Per_day_data = group_by_date[["Date", "Active"]].copy()
Recovered = [0]
Deaths = [0]
for i in range(1, 560):
    Recovered.append(group_by_date["Recovered"][i] - group_by_date["Recovered"][i - 1])
    Deaths.append(group_by_date["Deaths"][i] - group_by_date["Deaths"][i - 1])
Per_day_data["Recovered"] = Recovered
Per_day_data["Deaths"] = Deaths
# --------------------------------------Introduction Part-------------------------------

print("-------------------    WELCOME TO COVID-19 ANALYTICAL AND DETAILS PREDICTION SYSTEM     -----------------\n")
print("-----   YOU ARE INSIDE ANALYTICAL PART  ------\n")
print("PLEASE SELECT 1 OPTION FROM GIVEN OPTIONS")
print("   1 : Plotting top 10 states having most  cases ")
print("   2 : Plotting India's covid-19 cases trend ")
print("   3 : Plotting combinely top-5 states cases trend ")
print("   4 : Vaccination comparisions ")
print("   5 : Vaccinations comparisions ")
inp = int(input(" Enter your option : "))
if inp == 1:
    print("PLEASE SELECT 1 OPTION FROM GIVEN OPTIONS")
    print("   1 : Plotting top 10 states having most ACTIVE cases ")
    print("   2 : Plotting top 10 states having most CONFIRMED cases ")
    print("   3 : Plotting top 10 states having most DEATHS cases ")
    print("   4 : Plotting top 10 states having most RECOVERED cases ")
    inp2 = int(input("\n Enter your option : "))
    if inp2 == 1:
        top_10_active_states = Data.groupby("State/UnionTerritory").max()[['Active']].sort_values(by=["Active"],
                                                                                                  ascending=False).reset_index()
        print("PLEASE SELECT 1 OPTION FROM GIVEN OPTIONS")
        print("1-For normal Bar charts")
        print("2-For Interactive Bar charts")
        inp3 = int(input("Enter your choice : "))
        if inp3 == 1:
            plt.figure(figsize=(12, 6))
            plt.title("Top 10 states with most active cases", size=20)
            sns.barplot(x="State/UnionTerritory", y="Active", data=top_10_active_states[:10], linewidth=1,
                        edgecolor="black")
            plt.show()
        elif inp3 == 2:
            fig = px.bar(top_10_active_states[:10], x="State/UnionTerritory", y="Active", color="State/UnionTerritory")
            fig.show()
        else:
            print("---------!!!!!WRONG INPUT ------")
    elif inp2 == 2:
        top_10_confirmed_states = Data.groupby("State/UnionTerritory").max()[['Confirmed']].sort_values(
            by=["Confirmed"], ascending=False).reset_index()
        top_10_confirmed_states.drop(
            index=top_10_confirmed_states[top_10_confirmed_states["State/UnionTerritory"] == "Maharashtra***"].index,
            inplace=True)
        top_10_confirmed_states.drop(
            index=top_10_confirmed_states[top_10_confirmed_states["State/UnionTerritory"] == "Karanataka"].index,
            inplace=True)
        top_10_confirmed_states.reset_index()
        print("PLEASE SELECT 1 OPTION FROM GIVEN OPTIONS")
        print("1-For normal Bar charts")
        print("2-For Interactive Bar charts")
        inp3 = int(input("Enter your choice : "))
        if inp3 == 1:
            plt.figure(figsize=(12, 6))
            plt.title("Top 10 states with most Confirmed cases", size=20)
            sns.barplot(x="State/UnionTerritory", y="Confirmed", data=top_10_confirmed_states[:10], linewidth=1,
                        edgecolor="black")
            plt.show()
        elif inp3 == 2:
            fig = px.bar(top_10_confirmed_states[:10], x="State/UnionTerritory", y="Confirmed",
                         color="State/UnionTerritory")
            fig.show()
        else:
            print("---------!!!!!WRONG INPUT ------")

    elif inp2 == 3:
        top_10_deaths_states = Data.groupby("State/UnionTerritory").max()[['Deaths']].sort_values(by=["Deaths"],
                                                                                                  ascending=False).reset_index()
        top_10_deaths_states.drop(
            index=top_10_deaths_states[top_10_deaths_states["State/UnionTerritory"] == "Maharashtra***"].index,
            inplace=True)
        top_10_deaths_states.drop(
            index=top_10_deaths_states[top_10_deaths_states["State/UnionTerritory"] == "Karanataka"].index,
            inplace=True)
        top_10_deaths_states.reset_index()
        print("PLEASE SELECT 1 OPTION FROM GIVEN OPTIONS")
        print("1-For normal Bar charts")
        print("2-For Interactive Bar charts")
        inp3 = int(input("Enter your choice : "))
        if inp3 == 1:
            plt.figure(figsize=(12, 6))
            plt.title("Top 10 states with most Deaths cases", size=20)
            sns.barplot(x="State/UnionTerritory", y="Deaths", data=top_10_deaths_states[:10], linewidth=1,
                        edgecolor="black")
            plt.show()
        elif inp3 == 2:
            fig = px.bar(top_10_deaths_states[:10], x="State/UnionTerritory", y="Deaths", color="State/UnionTerritory")
            fig.show()
        else:
            print("---------!!!!!WRONG INPUT ------")
    elif inp2 == 4:
        top_10_recovered_states = Data.groupby("State/UnionTerritory").max()[['Recovered']].sort_values(
            by=["Recovered"], ascending=False).reset_index()
        top_10_recovered_states.drop(
            index=top_10_recovered_states[top_10_recovered_states["State/UnionTerritory"] == "Maharashtra***"].index,
            inplace=True)
        top_10_recovered_states.drop(
            index=top_10_recovered_states[top_10_recovered_states["State/UnionTerritory"] == "Karanataka"].index,
            inplace=True)
        top_10_recovered_states.reset_index()
        print("PLEASE SELECT 1 OPTION FROM GIVEN OPTIONS")
        print("1-For normal Bar charts")
        print("2-For Interactive Bar charts")
        inp3 = int(input("Enter your choice : "))
        if inp3 == 1:
            plt.figure(figsize=(12, 6))
            plt.title("Top 10 states with most Recovered cases", size=20)
            sns.barplot(x="State/UnionTerritory", y="Recovered", data=top_10_recovered_states[:10], linewidth=1,
                        edgecolor="black")
            plt.show()
        elif inp3 == 2:
            fig = px.bar(top_10_recovered_states[:10], x="State/UnionTerritory", y="Recovered",
                         color="State/UnionTerritory")
            fig.show()
        else:
            print("---------!!!!!WRONG INPUT ------")
    else:
        print("---------!!!!!WRONG INPUT ------")
elif inp == 2:
    print("PLEASE SELECT 1 OPTION FROM GIVEN OPTIONS")
    print("   1 : India's trend for  ACTIVE cases ")
    print("   2 : India's trend for  RECOVERED cases ")
    print("   3 : India's trend for DEATHS cases ")
    inp2 = int(input("\n Enter your option : "))
    if inp2 == 1:
        print("PLEASE SELECT 1 OPTION FROM GIVEN OPTIONS")
        print("1-For normal Graphs")
        print("2-For Interactive Graphs")
        inp3 = int(input("Enter your choice : "))
        if inp3 == 1:
            plt.figure(figsize=(12, 6))
            plt.title("Active cases trend", size=20, color="darkblue")
            plt.xlabel("Dates", fontdict={'family': 'serif', 'color': 'darkred', 'size': 15})
            plt.ylabel("Active cases", fontdict={'family': 'serif', 'color': 'darkred', 'size': 15})
            plt.plot(Per_day_data["Date"], Per_day_data["Active"], color="orange", linewidth=3, label="India")
            plt.legend(loc="upper left", title="Country", fontsize=15, shadow=True, facecolor=
            'lightyellow').get_title().set_fontsize('20')
            plt.grid()
            plt.show()
        elif inp3 == 2:
            fig = px.line(Per_day_data, x="Date", y="Active")
            fig.show()
        else:
            print("---------!!!!!WRONG INPUT ------")
    elif inp2 == 2:
        print("PLEASE SELECT 1 OPTION FROM GIVEN OPTIONS")
        print("1-For normal Bar charts")
        print("2-For Interactive Bar charts")
        inp3 = int(input("Enter your choice : "))
        if inp3 == 1:
            plt.figure(figsize=(12, 6))
            plt.title("Recovered cases trend", size=20, color="darkblue")
            plt.xlabel("Dates", fontdict={'family': 'serif', 'color': 'darkred', 'size': 15})
            plt.ylabel("Recovered cases", fontdict={'family': 'serif', 'color': 'darkred', 'size': 15})
            plt.plot(Per_day_data["Date"], Per_day_data["Recovered"], color="orange", linewidth=3, label="India")
            plt.legend(loc="upper left", title="Country", fontsize=15, shadow=True, facecolor=
            'lightyellow').get_title().set_fontsize('20')
            plt.grid()
            plt.show()
        elif inp3 == 2:
            fig = px.line(Per_day_data, x="Date", y="Recovered")
            fig.show()
        else:
            print("---------!!!!!WRONG INPUT ------")
    elif inp2 == 3:
        print("PLEASE SELECT 1 OPTION FROM GIVEN OPTIONS")
        print("1-For normal Bar charts")
        print("2-For Interactive Bar charts")
        inp3 = int(input("Enter your choice : "))
        if inp3 == 1:
            plt.figure(figsize=(12, 6))
            plt.title("Deaths cases trend", size=20, color="darkblue")
            plt.xlabel("Dates", fontdict={'family': 'serif', 'color': 'darkred', 'size': 15})
            plt.ylabel("Deaths cases", fontdict={'family': 'serif', 'color': 'darkred', 'size': 15})
            plt.plot(Per_day_data["Date"], Per_day_data["Deaths"], color="darkorange", linewidth=3, label="India")
            plt.legend(loc="upper left", title="Country", fontsize=15, shadow=True, facecolor=
            'lightyellow').get_title().set_fontsize('20')
            plt.grid()
            plt.show()
        elif inp3 == 2:
            fig = px.line(Per_day_data, x="Date", y="Deaths")
            fig.show()
        else:
            print("---------!!!!!WRONG INPUT ------")
    else:
        print("---------!!!!!WRONG INPUT ------")
elif inp == 3:
    print("PLEASE SELECT 1 OPTION FROM GIVEN OPTIONS")
    print("   1 : India's trend for  ACTIVE cases ")
    print("   2 : India's trend for  RECOVERED cases ")
    print("   3 : India's trend for DEATHS cases ")
    inp2 = int(input("\n Enter your option : "))
    if inp2 == 1:
        print("PLEASE SELECT 1 OPTION FROM GIVEN OPTIONS")
        print("1-For normal Bar charts")
        print("2-For Interactive Bar charts")
        inp3 = int(input("Enter your choice : "))
        if inp3 == 1:
            pass
        elif inp3 == 2:
            pass
        else:
            print("---------!!!!!WRONG INPUT ------")
    elif inp2 == 2:
        print("PLEASE SELECT 1 OPTION FROM GIVEN OPTIONS")
        print("1-For normal Bar charts")
        print("2-For Interactive Bar charts")
        inp3 = int(input("Enter your choice : "))
        if inp3 == 1:
            pass
        elif inp3 == 2:
            pass
        else:
            print("---------!!!!!WRONG INPUT ------")
    elif inp2 == 3:
        print("PLEASE SELECT 1 OPTION FROM GIVEN OPTIONS")
        print("1-For normal Bar charts")
        print("2-For Interactive Bar charts")
        inp3 = int(input("Enter your choice : "))
        if inp3 == 1:
            pass
        elif inp3 == 2:
            pass
        else:
            print("---------!!!!!WRONG INPUT ------")
    else:
        print("---------!!!!!WRONG INPUT ------")
elif inp == 4:
    print("PLEASE SELECT 1 OPTION FROM GIVEN OPTIONS")
    print("   1 : India's trend for  ACTIVE cases ")
    print("   2 : India's trend for  RECOVERED cases ")
    print("   3 : India's trend for DEATHS cases ")
    inp2 = int(input("\n Enter your option : "))
    if inp2 == 1:
        print("PLEASE SELECT 1 OPTION FROM GIVEN OPTIONS")
        print("1-For normal Bar charts")
        print("2-For Interactive Bar charts")
        inp3 = int(input("Enter your choice : "))
        if inp3 == 1:
            pass
        elif inp3 == 2:
            pass
        else:
            print("---------!!!!!WRONG INPUT ------")
    elif inp2 == 2:
        print("PLEASE SELECT 1 OPTION FROM GIVEN OPTIONS")
        print("1-For normal Bar charts")
        print("2-For Interactive Bar charts")
        inp3 = int(input("Enter your choice : "))
        if inp3 == 1:
            pass
        elif inp3 == 2:
            pass
        else:
            print("---------!!!!!WRONG INPUT ------")
    elif inp2 == 3:
        print("PLEASE SELECT 1 OPTION FROM GIVEN OPTIONS")
        print("1-For normal Bar charts")
        print("2-For Interactive Bar charts")
        inp3 = int(input("Enter your choice : "))
        if inp3 == 1:
            pass
        elif inp3 == 2:
            pass
        else:
            print("---------!!!!!WRONG INPUT ------")
    else:
        print("---------!!!!!WRONG INPUT ------")
elif inp == 5:
    print("PLEASE SELECT 1 OPTION FROM GIVEN OPTIONS")
    print("   1 : India's trend for  ACTIVE cases ")
    print("   2 : India's trend for  RECOVERED cases ")
    print("   3 : India's trend for DEATHS cases ")
    inp2 = int(input("\n Enter your option : "))
    if inp2 == 1:
        print("PLEASE SELECT 1 OPTION FROM GIVEN OPTIONS")
        print("1-For normal Bar charts")
        print("2-For Interactive Bar charts")
        inp3 = int(input("Enter your choice : "))
        if inp3 == 1:
            pass
        elif inp3 == 2:
            pass
        else:
            print("---------!!!!!WRONG INPUT ------")
    elif inp2 == 2:
        print("PLEASE SELECT 1 OPTION FROM GIVEN OPTIONS")
        print("1-For normal Bar charts")
        print("2-For Interactive Bar charts")
        inp3 = int(input("Enter your choice : "))
        if inp3 == 1:
            pass
        elif inp3 == 2:
            pass
        else:
            print("---------!!!!!WRONG INPUT ------")
    elif inp2 == 3:
        print("PLEASE SELECT 1 OPTION FROM GIVEN OPTIONS")
        print("1-For normal Bar charts")
        print("2-For Interactive Bar charts")
        inp3 = int(input("Enter your choice : "))
        if inp3 == 1:
            pass
        elif inp3 == 2:
            pass
        else:
            print("---------!!!!!WRONG INPUT ------")
    else:
        print("---------!!!!!WRONG INPUT ------")
else:
    print("---------!!!!!WRONG INPUT ------")
