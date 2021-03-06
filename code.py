# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file is stored in the variable path

#Code starts here

# Data Loading 
data = pd.read_csv(path)

# Renaming the Total Variable
data.rename({"Total":"Total_Medals"},axis=1,inplace=True)

# Displaying first 10 records
print(data.head(10))

# Summer or Winter
def better(df):
    if df["Total_Summer"] == df["Total_Winter"]:
        val = "Both"
    elif df["Total_Summer"] > df["Total_Winter"]:
        val = "Summer"
    else:
        val = "Winter"

    return val

data["Better_Event"] = data.apply(better,axis=1)
better_event = data["Better_Event"].value_counts().index[0]
print(better_event)

# Top 10
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries.drop(top_countries.shape[0]-1,inplace=True)

def top_ten(df,col):
    top10 = df.nlargest(10, col)
    country_list = list(top10.Country_Name)
    return(country_list)

top_10_summer = top_ten(top_countries,"Total_Summer")
top_10_winter = top_ten(top_countries,"Total_Winter")
top_10 = top_ten(top_countries,"Total_Medals")
common = [x for x in top_10 if x in top_10_summer and x in top_10_winter]

# Plotting top 10
summer_df = data[data["Country_Name"].isin(top_10_summer)]
winter_df = data[data["Country_Name"].isin(top_10_winter)]
top_df = data[data["Country_Name"].isin(top_10)]
summer_df.plot.bar("Country_Name","Total_Summer")
winter_df.plot.bar("Country_Name","Total_Winter")
top_df.plot.bar("Country_Name","Total_Medals")

# Top Performing Countries
summer_df["Golden_Ratio"] = summer_df["Gold_Summer"]/summer_df["Total_Summer"]
summer_max_ratio = summer_df["Golden_Ratio"].max()
summer_country_gold = list(summer_df[summer_df["Golden_Ratio"] == summer_max_ratio].Country_Name)[0]
print(summer_max_ratio,summer_country_gold)

winter_df["Golden_Ratio"] = winter_df["Gold_Winter"]/winter_df["Total_Winter"]
winter_max_ratio = winter_df["Golden_Ratio"].max()
winter_country_gold = list(winter_df[winter_df["Golden_Ratio"] == winter_max_ratio].Country_Name)[0]
print(winter_max_ratio,winter_country_gold)

top_df["Golden_Ratio"] = top_df["Gold_Total"]/top_df["Total_Medals"]
top_max_ratio = top_df["Golden_Ratio"].max()
top_country_gold = list(top_df[top_df["Golden_Ratio"] == top_max_ratio].Country_Name)[0]
print(top_max_ratio,top_country_gold)

# Best in the world 
data_1 = data.drop(data.shape[0]-1)
data_1["Total_Points"] = data_1["Gold_Total"]*3 + data_1["Silver_Total"]*2 + data_1["Bronze_Total"]
most_points = data_1["Total_Points"].max()
best_country = list(data_1[data_1["Total_Points"] == most_points].Country_Name)[0]
print(most_points,best_country)

# Plotting the best
best = data[data["Country_Name"] == best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar(stacked=True)
plt.xlabel("United States")
plt.ylabel("Medals Tally")
plt.xticks(rotation=45)



