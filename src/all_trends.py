import numpy as np
import pandas as pd
import plotly.express as px

ufo_data = pd.read_csv("../data/ufo_sighting_data.csv", low_memory=False)
ufo_data['Date_time'] = pd.to_datetime(ufo_data['Date_time'], errors='coerce')


#Months
months = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}

for month in months:
    months[month] = (ufo_data["Date_time"].dt.month==month).sum()

month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
months_values = list(months.values())

months_parsed={"month":month_names, "counts":months_values}
fig = px.bar(months_parsed, x="month", y="counts")
fig.write_html("../html/months.html")

month_perc = {}
sum_reports = sum(months_values)
for month, count in zip(month_names, months_values):
    month_perc[month] = (count/sum_reports)*100

print("Total Reports with date: ",sum_reports)
print("For context, 1% is equivalent to, ", 0.01*sum_reports," reports")
for month in month_perc:
    print(month, ":", "{:.2f}".format(month_perc[month]),"% of reports")

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
for season, count in season_perc.items():
    print(season + ": ", "{:.2f}".format((count/sum_reports)*100),"% of reports")

seasons_parsed = {"season":season_perc.keys(), "counts":season_perc.values()} 
fig = px.bar(seasons_parsed, x="season", y="counts")
fig.write_html("../html/seasons.html")


print("\n")
print("==============================================================================")
print("\n")
# Years
years = ufo_data['Date_time'].dt.year.value_counts().to_dict()
years_parsed = {"Year":years.keys(), "Counts":years.values()}
fig1 = px.bar(years_parsed, x="Year", y="Counts")
decades = ((ufo_data["Date_time"].dt.year//10)*10).value_counts().to_dict()

#Decades
decades_parsed = {"Decade":decades.keys(), "Count":decades.values()}
fig2 = px.bar(decades_parsed, x="Decade", y="Count")
with open("../html/years.html", "a") as f:
    f.write(fig1.to_html(full_html=False))
    f.write(fig2.to_html(full_html=False))
#Print the distribution as well

print("\n")
print("============================================================================")
print("\n")

# Time of Day
hours = ufo_data["Date_time"].dt.hour.value_counts().to_dict()
hours_parsed = {"Hour":hours.keys(), "Count":hours.values()}
fig = px.bar(hours_parsed, x="Hour", y="Count")
fig.write_html("../html/hours.html")

print("\n")
print("============================================================================")
print("\n")

# UFO Shape
shapes = ufo_data["UFO_shape"].value_counts().to_dict()
shapes_parsed = {"Shape":shapes.keys(), "Count":shapes.values()}
fig = px.pie(shapes_parsed, values="Count", names="Shape", title="Distribution of Reported UFO Shapes")
fig.write_html("../html/shapes.html")




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





