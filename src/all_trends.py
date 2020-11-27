import numpy as np
import pandas as pd
import plotly.express as px

data = "../data/ufo_sighting_data.csv" 
ufo_data = pd.read_csv(data, low_memory=False)
ufo_data['Date_time'] = pd.to_datetime(ufo_data['Date_time'], errors='coerce')

#World Map
fig = px.scatter_mapbox(ufo_data, lat="latitude", lon="longitude", hover_name="city", hover_data=["UFO_shape", "description"], color_discrete_sequence=["fuchsia"], zoom=3, height=900)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.write_html("../html/world_map.html")

#====================================================================================
# Map of UFO's and Nuclear Power Plants
fig = px.scatter_mapbox(ufo_data, lat="latitude", lon="longitude", hover_name="city", hover_data=["Date_time", "UFO_shape", "description"], color_discrete_sequence=["fuchsia"], zoom=3, height=900)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

nuclear_plant_data = "../data/nuclear-plants-locations.csv"
plant_data = pd.read_csv(nuclear_plant_data, low_memory=False)
fig.add_trace(px.scatter_mapbox(plant_data, lat="Latitude", lon="Longitude", hover_name="Plant", hover_data=["Plant", "NumReactor"]).data[0])
fig.write_html("../html/world_map_with_nuclear.html")






#===================================================================================

#Months
months = ufo_data["Date_time"].dt.month.value_counts().to_dict()
months_parsed={"month":months.keys(), "counts":months.values()}
fig = px.bar(months_parsed, x="month", y="counts", title="UFO Reports by Month")
fig.write_html("../html/months.html")

print("UFO Report Monthly Trends:")
print("Total Reports with date: ", sum(months.values()))
print("For context, 1% is equivalent to,", 0.01*sum(months.values()),"reports")
print("\n")
for month, count in months.items():
    print(str(int(month))+":", "{:.2f}".format(count/sum(months.values())*100),"% of reports")

print("\n")
print("==============================================================================")
print("\n")
# Seasons
summer = fall = winter = spring = 0
for key, val in months.items():
    if key in [6,7,8]:
        summer += val
    elif key in [9,10,11]:
        fall += val
    elif key in [12,1,2]:
        winter += val
    else:
        spring += val

season_perc = {"Summer":summer, "Fall":fall, "Winter":winter, "Spring":spring}
print("UFO Report Seasonal Trends:")
print("Total Reports with Month:", summer+fall+winter+spring)
print("\n")
for season, count in season_perc.items():
    print(season + ": ", "{:.2f}".format((count/sum(months.values()))*100),"%")

seasons_parsed = {"season":season_perc.keys(), "counts":season_perc.values()} 
fig = px.pie(seasons_parsed, values="counts", names="season", title="UFO Reports by Season")
fig.write_html("../html/seasons.html")


print("\n")
print("==============================================================================")
print("\n")
# Years
years = ufo_data['Date_time'].dt.year.value_counts().to_dict()
years_parsed = {"Year":years.keys(), "Counts":years.values()}
fig1 = px.bar(years_parsed, x="Year", y="Counts", title="UFO Reports by Year")
decades = ((ufo_data["Date_time"].dt.year//10)*10).value_counts().to_dict()

#Decades
decades_parsed = {"Decade":decades.keys(), "Count":decades.values()}
fig2 = px.bar(decades_parsed, x="Decade", y="Count", title="UFO Reports by Decade")
with open("../html/years.html", "a") as f:
    f.write(fig1.to_html(full_html=False))
    f.write(fig2.to_html(full_html=False))
#Print the distribution as well

print("UFO Report Yearly Trends:")
print("Total Reports with Year:", sum(decades.values()), "Reports")
print("\n")
for key, val in decades.items():
    print(int(key), "-",str(int(key+10))+": ", "{:.2f}".format(val/sum(decades.values())*100), "%")


print("\n")
print("============================================================================")
print("\n")

# Time of Day
hours = ufo_data["Date_time"].dt.hour.value_counts().to_dict()
hours_parsed = {"Hour":hours.keys(), "Count":hours.values()}
fig = px.bar(hours_parsed, x="Hour", y="Count", title="UFO Reports by hour of the day")
fig.write_html("../html/hours.html")

print("UFO Hourly Report Trends")
print("Total Reports with Time:", sum(hours.values()), "Reports")
print("\n")
for key,val in hours.items():
    print(str(key)+":", "{:.2f}".format(val/sum(hours.values())*100), "%")

print("\n")
print("============================================================================")
print("\n")

# UFO Shape
shapes = ufo_data["UFO_shape"].value_counts().to_dict()
shapes_parsed = {"Shape":shapes.keys(), "Count":shapes.values()}
fig = px.pie(shapes_parsed, values="Count", names="Shape", title="Distribution of Reported UFO Shapes")
fig.write_html("../html/shapes.html")
print("UFO Shape Trends:")
print("Total Reports with UFO Shape:", sum(shapes.values()), "Reports")
print("\n")
for key, val in shapes.items():
    print(key+":", "{:.2f}".format(val/sum(shapes.values())*100), "%")



print("\n")
print("============================================================================")
print("\n")

# =================================================================================
# Length of Encounter
ufo_data['length_of_encounter_seconds'] = pd.to_numeric(ufo_data['length_of_encounter_seconds'], errors='coerce')
lengths = (np.ceil(ufo_data["length_of_encounter_seconds"]/60)).value_counts().to_dict()
lengths_parsed = {"Length of Encounter in minutes":lengths.keys(), "Count":lengths.values()}
fig = px.pie(lengths_parsed, names="Length of Encounter in minutes", values="Count", title="Length of Encounters in minutes")
fig.write_html("../html/encounter_lengths.html")

print("UFO Length of Encounter Trends in Minutes:")
print("Total Reports with length of encounter:", sum(lengths.values()), "Reports")
print("\n")
for key,val in lengths.items():
    print(str(int(key))+" minutes:", "{:.2f}".format(val/sum(lengths.values())*100), "%")




