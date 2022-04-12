# ---------------------------------Importing all the libraries needed-------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

# ---------------------------------Reading the data from csv files with pandas-----------------

Data = pd.read_csv("covid_19_india.csv")  # Main Data

vaccine_data = pd.read_csv("covid_vaccine_statewise.csv")

# -------------------------------- Data Pre-processing: remove,add,change---------------

Data.drop(["Sno", "Time", "ConfirmedIndianNational", "ConfirmedForeignNational"], axis=1, inplace=True)  # Removing
Data["Date"] = pd.to_datetime(Data["Date"])  # type casting
Data.rename(columns={"Cured": "Recovered"}, inplace=True)  # renaming
Data["Active"] = Data["Confirmed"] - (Data["Recovered"] + Data["Deaths"])  # adding new columns

vaccine_data.drop(
    columns=["Sessions", "18-44 Years (Doses Administered)", "Male (Doses Administered)", "Female (Doses Administered)",
             "Transgender (Doses Administered)",
             "18-44 Years (Doses Administered)", "45-60 Years (Doses Administered)", "Sputnik V (Doses Administered)",
             "AEFI",
             "60+ Years (Doses Administered)"], inplace=True)
vaccine_data.rename(columns={"Updated On": "Vaccine date"}, inplace=True)

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
d1 = vaccine_data.groupby("State").sum()["Total Individuals Vaccinated"].reset_index().sort_values(
    by="Total Individuals Vaccinated",
    ascending=False)
d1 = d1[d1["State"] != "India"]
# --------------------------------------Introduction Part-------------------------------
while True:
    print("-------------------    WELCOME TO COVID-19 ANALYTICAL AND DETAILS PREDICTION SYSTEM     -----------------\n")
    print("-----   YOU ARE INSIDE ANALYTICAL PART  ------\n")
    print("PLEASE SELECT 1 OPTION FROM GIVEN OPTIONS")
    print("   1 : Plotting top 10 states having most  cases ")
    print("   2 : Plotting India's covid-19 cases trend ")
    print("   3 : Plotting combinely top-5 states cases trend ")
    print("   4 : Vaccination comparisons Individually")
    print("   5 : Vaccinations comparisons of States ")
    inp = input(" Enter your option : ")
    if inp == "1":
        print("PLEASE SELECT 1 OPTION FROM GIVEN OPTIONS")
        print("   1 : Plotting top 10 states having most ACTIVE cases ")
        print("   2 : Plotting top 10 states having most CONFIRMED cases ")
        print("   3 : Plotting top 10 states having most DEATHS cases ")
        print("   4 : Plotting top 10 states having most RECOVERED cases ")
        inp2 = input("\n Enter your option : ")
        if inp2 == "1":
            top_10_active_states = Data.groupby("State/UnionTerritory").max()[['Active']].sort_values(by=["Active"],
                                                                                                      ascending=False).reset_index()
            print("PLEASE SELECT 1 OPTION FROM GIVEN OPTIONS")
            print("1-For normal Bar charts")
            print("2-For Interactive Bar charts")
            inp3 = input("Enter your choice : ")
            if inp3 == "1":
                plt.figure(figsize=(12, 6))
                plt.title("Top 10 states with most active cases", size=20)
                sns.barplot(x="State/UnionTerritory", y="Active", data=top_10_active_states[:10], linewidth=1,
                            edgecolor="black")
                plt.show()
            elif inp3 == "2":
                fig = px.bar(top_10_active_states[:10], x="State/UnionTerritory", y="Active",
                             color="State/UnionTerritory", title="Top 10 states with most active cases")
                fig.show()
            else:
                print("---------!!!!!WRONG INPUT ------")
        elif inp2 == "2":
            top_10_confirmed_states = Data.groupby("State/UnionTerritory").max()[['Confirmed']].sort_values(
                by=["Confirmed"], ascending=False).reset_index()
            top_10_confirmed_states.drop(
                index=top_10_confirmed_states[
                    top_10_confirmed_states["State/UnionTerritory"] == "Maharashtra***"].index,
                inplace=True)
            top_10_confirmed_states.drop(
                index=top_10_confirmed_states[top_10_confirmed_states["State/UnionTerritory"] == "Karanataka"].index,
                inplace=True)
            top_10_confirmed_states.reset_index()
            print("PLEASE SELECT 1 OPTION FROM GIVEN OPTIONS")
            print("1-For normal Bar charts")
            print("2-For Interactive Bar charts")
            inp3 = input("Enter your choice : ")
            if inp3 == "1":
                plt.figure(figsize=(12, 6))
                plt.title("Top 10 states with most Confirmed cases", size=20)
                sns.barplot(x="State/UnionTerritory", y="Confirmed", data=top_10_confirmed_states[:10], linewidth=1,
                            edgecolor="black")
                plt.show()
            elif inp3 == "2":
                fig = px.bar(top_10_confirmed_states[:10], x="State/UnionTerritory", y="Confirmed",
                             color="State/UnionTerritory", title="Top 10 states with most Confirmed cases")
                fig.show()
            else:
                print("---------!!!!!WRONG INPUT ------")
        elif inp2 == "3":
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
            inp3 = input("Enter your choice : ")
            if inp3 == "1":
                plt.figure(figsize=(12, 6))
                plt.title("Top 10 states with most Deaths cases", size=20)
                sns.barplot(x="State/UnionTerritory", y="Deaths", data=top_10_deaths_states[:10], linewidth=1,
                            edgecolor="black")
                plt.show()
            elif inp3 == "2":
                fig = px.bar(top_10_deaths_states[:10], x="State/UnionTerritory", y="Deaths",
                             color="State/UnionTerritory", title="Top 10 states with most Deaths cases")
                fig.show()
            else:
                print("---------!!!!!WRONG INPUT ------")
        elif inp2 == "4":
            top_10_recovered_states = Data.groupby("State/UnionTerritory").max()[['Recovered']].sort_values(
                by=["Recovered"], ascending=False).reset_index()
            top_10_recovered_states.drop(
                index=top_10_recovered_states[
                    top_10_recovered_states["State/UnionTerritory"] == "Maharashtra***"].index,
                inplace=True)
            top_10_recovered_states.drop(
                index=top_10_recovered_states[top_10_recovered_states["State/UnionTerritory"] == "Karanataka"].index,
                inplace=True)
            top_10_recovered_states.reset_index()
            print("PLEASE SELECT 1 OPTION FROM GIVEN OPTIONS")
            print("1-For normal Bar charts")
            print("2-For Interactive Bar charts")
            inp3 = input("Enter your choice : ")
            if inp3 == "1":
                plt.figure(figsize=(12, 6))
                plt.title("Top 10 states with most Recovered cases", size=20)
                sns.barplot(x="State/UnionTerritory", y="Recovered", data=top_10_recovered_states[:10], linewidth=1,
                            edgecolor="black")
                plt.show()
            elif inp3 == "2":
                fig = px.bar(top_10_recovered_states[:10], x="State/UnionTerritory", y="Recovered",
                             color="State/UnionTerritory", title="Top 10 states with most Recovered cases")
                fig.show()
            else:
                print("---------!!!!!WRONG INPUT ------")
        else:
            print("---------!!!!!WRONG INPUT ------")
    elif inp == "2":
        print("PLEASE SELECT 1 OPTION FROM GIVEN OPTIONS")
        print("   1 : India's trend for  ACTIVE cases ")
        print("   2 : India's trend for  RECOVERED cases ")
        print("   3 : India's trend for DEATHS cases ")
        inp2 = input("\n Enter your option : ")
        if inp2 == "1":
            print("PLEASE SELECT 1 OPTION FROM GIVEN OPTIONS")
            print("1-For normal Graphs")
            print("2-For Interactive Graphs")
            inp3 = input("Enter your choice : ")
            if inp3 == "1":
                plt.figure(figsize=(12, 6))
                plt.title("Active cases trend in India ", size=20, color="darkblue")
                plt.xlabel("Dates", fontdict={'family': 'serif', 'color': 'darkred', 'size': 15})
                plt.ylabel("Active cases", fontdict={'family': 'serif', 'color': 'darkred', 'size': 15})
                plt.plot(Per_day_data["Date"], Per_day_data["Active"], color="orange", linewidth=3, label="India")
                plt.legend(loc="upper left", title="Country", fontsize=15, shadow=True, facecolor=
                'lightyellow').get_title().set_fontsize('20')
                plt.grid()
                plt.show()
            elif inp3 == "2":
                fig = px.line(Per_day_data, x="Date", y="Active", title="Active cases trend India ")
                fig.show()
            else:
                print("---------!!!!!WRONG INPUT ------")
        elif inp2 == "2":
            print("PLEASE SELECT 1 OPTION FROM GIVEN OPTIONS")
            print("1-For normal Bar charts")
            print("2-For Interactive Bar charts")
            inp3 = input("Enter your choice : ")
            if inp3 == "1":
                plt.figure(figsize=(12, 6))
                plt.title("Recovered cases trend in India", size=20, color="darkblue")
                plt.xlabel("Dates", fontdict={'family': 'serif', 'color': 'darkred', 'size': 15})
                plt.ylabel("Recovered cases", fontdict={'family': 'serif', 'color': 'darkred', 'size': 15})
                plt.plot(Per_day_data["Date"], Per_day_data["Recovered"], color="orange", linewidth=3, label="India")
                plt.legend(loc="upper left", title="Country", fontsize=15, shadow=True, facecolor=
                'lightyellow').get_title().set_fontsize('20')
                plt.grid()
                plt.show()
            elif inp3 == "2":
                fig = px.line(Per_day_data, x="Date", y="Recovered", title="Recovered cases trend India ")
                fig.show()
            else:
                print("---------!!!!!WRONG INPUT ------")
        elif inp2 == "3":
            print("PLEASE SELECT 1 OPTION FROM GIVEN OPTIONS")
            print("1-For normal Bar charts")
            print("2-For Interactive Bar charts")
            inp3 = input("Enter your choice : ")
            if inp3 == "1":
                plt.figure(figsize=(12, 6))
                plt.title("Deaths cases trend in India ", size=20, color="darkblue")
                plt.xlabel("Dates", fontdict={'family': 'serif', 'color': 'darkred', 'size': 15})
                plt.ylabel("Deaths cases", fontdict={'family': 'serif', 'color': 'darkred', 'size': 15})
                plt.plot(Per_day_data["Date"], Per_day_data["Deaths"], color="darkorange", linewidth=3, label="India")
                plt.legend(loc="upper left", title="Country", fontsize=15, shadow=True, facecolor=
                'lightyellow').get_title().set_fontsize('20')
                plt.grid()
                plt.show()
            elif inp3 == "2":
                fig = px.line(Per_day_data, x="Date", y="Deaths", title="Deaths cases trend India ")
                fig.show()
            else:
                print("---------!!!!!WRONG INPUT ------")
        else:
            print("---------!!!!!WRONG INPUT ------")
    elif inp == "3":
        print("PLEASE SELECT 1 OPTION FROM GIVEN OPTIONS")
        print("   1 : Top-5 States trend for  ACTIVE cases ")
        print("   2 : Top-5 States  trend for  RECOVERED cases ")
        print("   3 : Top-5 States  trend for DEATHS cases ")
        inp2 = input("\n Enter your option : ")
        if inp2 == "1":
            print("PLEASE SELECT 1 OPTION FROM GIVEN OPTIONS")
            print("1-For normal Graphs")
            print("2-For Graphs")
            inp3 = input("Enter your choice : ")
            if inp3 == "1":
                kerla_data = Data[Data["State/UnionTerritory"][:] == "Kerala"]
                Maharashtra_data = Data[Data["State/UnionTerritory"][:] == "Maharashtra"]
                Karnataka_data = Data[Data["State/UnionTerritory"][:] == "Karnataka"]
                TamilNadu_data = Data[Data["State/UnionTerritory"][:] == "Tamil Nadu"]
                UttarPradesh_data = Data[Data["State/UnionTerritory"][:] == "Uttar Pradesh"]
                plt.figure(figsize=(12, 6))
                plt.title("Active cases trend of top-5 State/UnionTerritory", size=20, color="darkblue")
                plt.xlabel("Dates", fontdict={'family': 'serif', 'color': 'darkred', 'size': 15})
                plt.ylabel("Active cases ", fontdict={'family': 'serif', 'color': 'darkred', 'size': 15})
                plt.plot(kerla_data["Date"], kerla_data["Active"], label="kerla", linewidth=3)
                plt.plot(Maharashtra_data["Date"], Maharashtra_data["Active"], label="Maharashtra", linewidth=3)
                plt.plot(Karnataka_data["Date"], Karnataka_data["Active"], label="Karnataka", linewidth=3)
                plt.plot(TamilNadu_data["Date"], TamilNadu_data["Active"], label="TamilNadu", linewidth=3)
                plt.plot(UttarPradesh_data["Date"], UttarPradesh_data["Active"], label="Uttar Pradesh", linewidth=3)
                plt.legend(loc="upper left", title="State/UnionTerritory", fontsize=15, shadow=True, facecolor=
                'lightyellow').get_title().set_fontsize('20')
                plt.grid()
                plt.show()
            elif inp3 == "2":
                top_5_active = Data[
                    (Data["State/UnionTerritory"] == "Kerala") | (Data["State/UnionTerritory"] == "Maharashtra") | (
                            Data["State/UnionTerritory"] == "Karnataka") |
                    (Data["State/UnionTerritory"] == "Tamil Nadu") | (Data["State/UnionTerritory"] == "Uttar Pradesh")]
                fig = px.line(top_5_active, x="Date", y="Active", color="State/UnionTerritory",
                              title="Active cases trend of top-5 State/UnionTerritory")
                fig.show()
            else:
                print("---------!!!!!WRONG INPUT ------")
        elif inp2 == "2":
            print("PLEASE SELECT 1 OPTION FROM GIVEN OPTIONS")
            print("1-For normal Graphs")
            print("2-For Interactive Graphs")
            inp3 = input("Enter your choice : ")
            if inp3 == "1":
                kerla_data = Data[Data["State/UnionTerritory"][:] == "Kerala"]
                Maharashtra_data = Data[Data["State/UnionTerritory"][:] == "Maharashtra"]
                Karnataka_data = Data[Data["State/UnionTerritory"][:] == "Karnataka"]
                TamilNadu_data = Data[Data["State/UnionTerritory"][:] == "Tamil Nadu"]
                AndhraPradesh_data = Data[Data["State/UnionTerritory"][:] == "Andhra Pradesh"]
                plt.figure(figsize=(12, 6))
                plt.title("Recovered cases trend of top-5 State/UnionTerritory", size=20, color="darkblue")
                plt.xlabel("Dates", fontdict={'family': 'serif', 'color': 'darkred', 'size': 15})
                plt.ylabel("Recovered cases ", fontdict={'family': 'serif', 'color': 'darkred', 'size': 15})
                plt.plot(kerla_data["Date"], kerla_data["Recovered"], label="kerla", linewidth=3)
                plt.plot(Maharashtra_data["Date"], Maharashtra_data["Recovered"], label="Maharashtra", linewidth=3)
                plt.plot(Karnataka_data["Date"], Karnataka_data["Recovered"], label="Karnataka", linewidth=3)
                plt.plot(TamilNadu_data["Date"], TamilNadu_data["Recovered"], label="TamilNadu", linewidth=3)
                plt.plot(AndhraPradesh_data["Date"], AndhraPradesh_data["Recovered"], label="Andhra Pradesh",
                         linewidth=3)
                plt.legend(loc="upper left", title="State/UnionTerritory", fontsize=15, shadow=True, facecolor=
                'lightyellow').get_title().set_fontsize('20')
                plt.grid()
                plt.show()
            elif inp3 == "2":
                top_5_recovered = Data[
                    (Data["State/UnionTerritory"] == "Kerala") | (Data["State/UnionTerritory"] == "Maharashtra") | (
                            Data["State/UnionTerritory"] == "Karnataka") |
                    (Data["State/UnionTerritory"] == "Tamil Nadu") | (Data["State/UnionTerritory"] == "Andhra Pradesh")]
                fig = px.line(top_5_recovered, x="Date", y="Recovered", color="State/UnionTerritory",
                              title="Recovered cases trend of top-5 State/UnionTerritory")
                fig.show()
            else:
                print("---------!!!!!WRONG INPUT ------")
        elif inp2 == "3":
            print("PLEASE SELECT 1 OPTION FROM GIVEN OPTIONS")
            print("1-For normal Graphs")
            print("2-For Interactive Graphs")
            inp3 = input("Enter your choice : ")
            if inp3 == "1":
                Delhi_data = Data[Data["State/UnionTerritory"][:] == "Delhi"]
                Maharashtra_data = Data[Data["State/UnionTerritory"][:] == "Maharashtra"]
                Karnataka_data = Data[Data["State/UnionTerritory"][:] == "Karnataka"]
                TamilNadu_data = Data[Data["State/UnionTerritory"][:] == "Tamil Nadu"]
                UttarPradesh_data = Data[Data["State/UnionTerritory"][:] == "Uttar Pradesh"]
                plt.figure(figsize=(12, 6))
                plt.title("Deaths cases trend of top-5 State/UnionTerritory", size=20, color="darkblue")
                plt.xlabel("Dates", fontdict={'family': 'serif', 'color': 'darkred', 'size': 15})
                plt.ylabel("Deaths cases ", fontdict={'family': 'serif', 'color': 'darkred', 'size': 15})
                plt.plot(Delhi_data["Date"], Delhi_data["Deaths"], label="Delhi", linewidth=3)
                plt.plot(Maharashtra_data["Date"], Maharashtra_data["Deaths"], label="Maharashtra", linewidth=3)
                plt.plot(Karnataka_data["Date"], Karnataka_data["Deaths"], label="Karnataka", linewidth=3)
                plt.plot(TamilNadu_data["Date"], TamilNadu_data["Deaths"], label="TamilNadu", linewidth=3)
                plt.plot(UttarPradesh_data["Date"], UttarPradesh_data["Deaths"], label="Uttar Pradesh", linewidth=3)
                plt.legend(loc="upper left", title="State/UnionTerritory", fontsize=15, shadow=True, facecolor=
                'lightyellow').get_title().set_fontsize('20')
                plt.grid()
                plt.show()
            elif inp3 == "2":
                top_5_deaths = Data[
                    (Data["State/UnionTerritory"] == "Delhi") | (Data["State/UnionTerritory"] == "Maharashtra") | (
                            Data["State/UnionTerritory"] == "Karnataka") |
                    (Data["State/UnionTerritory"] == "Tamil Nadu") | (Data["State/UnionTerritory"] == "Uttar Pradesh")]
                fig = px.line(top_5_deaths, x="Date", y="Deaths", color="State/UnionTerritory",
                              title="Deaths cases trend of top-5 State/UnionTerritory")
                fig.show()
            else:
                print("---------!!!!!WRONG INPUT ------")
        else:
            print("---------!!!!!WRONG INPUT ------")
    elif inp == "4":
        print("PLEASE SELECT 1 OPTION FROM GIVEN OPTIONS")
        print("   1 : Vaccination comparisons of different age groups ")
        print("   2 : Vaccination comparisons by gender ")
        print("   3 : Vaccination comparisons Between covishield and covaxin ")
        inp2 = input("\n Enter your option : ")
        if inp2 == "1":
            age_18_44 = vaccine_data["18-44 Years(Individuals Vaccinated)"].sum()
            age_45_60 = vaccine_data["45-60 Years(Individuals Vaccinated)"].sum()
            age_60_more = vaccine_data["60+ Years(Individuals Vaccinated)"].sum()
            plt.figure(figsize=(12, 6))
            plt.title("Diiferent ages vaccination camparision", size=20, color="darkblue")
            plt.pie(x=[age_18_44, age_45_60, age_60_more], labels=["age_18_44", "age_45_60", "age_60_more"],
                    shadow=True,
                    wedgeprops={'edgecolor': 'black', 'linewidth': 1}, colors=["lightgreen", "lightblue", "orange"],
                    explode=[0.033, 0.033, 0.033], autopct="%1.1f%%")
            plt.legend(bbox_to_anchor=(1, 0.5), fontsize=15, shadow=True, facecolor='lightyellow')
            plt.show()

        elif inp2 == "2":
            male = vaccine_data["Male(Individuals Vaccinated)"].sum()
            female = vaccine_data["Female(Individuals Vaccinated)"].sum()
            plt.figure(figsize=(12, 6))
            plt.title("comarision of vaccination between male and female", size=20, color="darkblue")
            plt.pie(x=[male, female], labels=["Male", "female"], shadow=True,
                    wedgeprops={'edgecolor': 'black', 'linewidth': 1}, colors=["lightgreen", "lightblue"],
                    explode=[0, 0.06], autopct="%1.1f%%")
            plt.legend(bbox_to_anchor=(1, 0.5), fontsize=15, shadow=True, facecolor='lightyellow')
            plt.show()

        elif inp2 == "3":
            Covaxin = vaccine_data[" Covaxin (Doses Administered)"].sum()
            CoviShield = vaccine_data["CoviShield (Doses Administered)"].sum()
            plt.figure(figsize=(12, 6))
            plt.title("Vaccination comparisons Between covishield and covaxin ", size=20, color="darkblue")
            plt.pie(x=[Covaxin, CoviShield], labels=["Covaxin", "CoviShield"], shadow=True,
                    wedgeprops={'edgecolor': 'black', 'linewidth': 1}, colors=["lightgreen", "lightblue"],
                    explode=[0, 0.06], autopct="%1.1f%%")
            plt.legend(bbox_to_anchor=(1, 0.5), fontsize=15, shadow=True, facecolor='lightyellow')
            plt.show()

        else:
            print("---------!!!!!WRONG INPUT ------")
    elif inp == "5":
        print("PLEASE SELECT 1 OPTION FROM GIVEN OPTIONS")
        print("   1 : Vaccination comparisons of all States ")
        print("   2 : Vaccination comparisons of top-5 states  ")
        inp2 = input("\n Enter your option : ")
        if inp2 == "1":
            print("PLEASE SELECT 1 OPTION FROM GIVEN OPTIONS")
            print("1-For normal Pie charts")
            print("2-For Pie  charts")
            inp3 = input("Enter your choice : ")
            if inp3 == "1":
                Maharashtra = d1[d1["State"] == "Maharashtra"]["Total Individuals Vaccinated"].sum()
                Uttar_Pradesh = d1[d1["State"] == "Uttar Pradesh"]["Total Individuals Vaccinated"].sum()
                Rajasthan = d1[d1["State"] == "Rajasthan"]["Total Individuals Vaccinated"].sum()
                Gujarat = d1[d1["State"] == "Gujarat"]["Total Individuals Vaccinated"].sum()
                West_Bengal = d1[d1["State"] == "West Bengal"]["Total Individuals Vaccinated"].sum()
                other = \
                d1[(d1["State"] != "Maharashtra") & (d1["State"] != "Rajasthan") & (d1["State"] != "Uttar Pradesh")
                   & (d1["State"] != "Gujarat") & (d1["State"] != "West Bengal")][
                    "Total Individuals Vaccinated"].sum()
                plt.figure(figsize=(10, 10))
                plt.title("Comarision of vaccination among all  different states", size=20, color="darkblue")
                plt.pie(x=[Maharashtra, Uttar_Pradesh, Rajasthan, Gujarat, West_Bengal, other],
                        labels=["Maharashtra", "Uttar_Pradesh", "Rajasthan", "Gujarat", "West_Bengal", "other"]
                        , shadow=True, wedgeprops={'edgecolor': 'black', 'linewidth': 1}, explode=[0, 0, 0, 0, 0, 0.1],
                        autopct="%1.1f%%", textprops={"fontsize": 14})
                plt.legend(bbox_to_anchor=(1, 0.5), fontsize=15, shadow=True, facecolor='lightyellow')
                plt.show()
            elif inp3 == "2":
                d2 = d1[:5]
                other = \
                d1[(d1["State"] != "Maharashtra") & (d1["State"] != "Rajasthan") & (d1["State"] != "Uttar Pradesh")
                   & (d1["State"] != "Gujarat") & (d1["State"] != "West Bengal")][
                    "Total Individuals Vaccinated"].sum()
                value = {"State": "other", "Total Individuals Vaccinated": other}
                d3 = pd.DataFrame(value, index=[0])
                d2 = pd.concat([d2, d3], ignore_index=True)
                fig = px.pie(d2[:6], values="Total Individuals Vaccinated", names="State",
                             title="Comarision of vaccination among all different states")
                fig.show()
            else:
                print("---------!!!!!WRONG INPUT ------")
        elif inp2 == "2":
            print("PLEASE SELECT 1 OPTION FROM GIVEN OPTIONS")
            print("1-For normal PIE charts")
            print("2-For Interactive PIE charts")
            inp3 = input("Enter your choice : ")
            if inp3 == "1":
                Maharashtra = d1[d1["State"] == "Maharashtra"]["Total Individuals Vaccinated"].sum()
                Uttar_Pradesh = d1[d1["State"] == "Uttar Pradesh"]["Total Individuals Vaccinated"].sum()
                Rajasthan = d1[d1["State"] == "Rajasthan"]["Total Individuals Vaccinated"].sum()
                Gujarat = d1[d1["State"] == "Gujarat"]["Total Individuals Vaccinated"].sum()
                West_Bengal = d1[d1["State"] == "West Bengal"]["Total Individuals Vaccinated"].sum()
                plt.figure(figsize=(10, 10))
                plt.title("Comarision of vaccination among top-5 vaccinated statesstates", size=20, color="darkblue")
                plt.pie(x=[Maharashtra, Uttar_Pradesh, Rajasthan, Gujarat, West_Bengal],
                        labels=["Maharashtra", "Uttar_Pradesh", "Rajasthan", "Gujarat", "West_Bengal"]
                        , shadow=True, wedgeprops={'edgecolor': 'black', 'linewidth': 1}, explode=[0.1, 0, 0, 0, 0],
                        autopct="%1.1f%%", textprops={"fontsize": 14}, startangle=-20)
                plt.legend(bbox_to_anchor=(1, 0.5), fontsize=15, shadow=True, facecolor='lightyellow')
                plt.show()
            elif inp3 == "2":
                fig = px.pie(d1[:5], values="Total Individuals Vaccinated", names="State",
                             title="Comarision of vaccination among top-5 states")
                fig.show()
            else:
                print("---------!!!!!WRONG INPUT ------")

        else:
            print("---------!!!!!WRONG INPUT ------")
    else:
        print("---------!!!!!WRONG INPUT ------")
    inp4 = input("if you want to explore more type(y) : ")
    if inp4 != 'y':
        break
    os.system('cls')
