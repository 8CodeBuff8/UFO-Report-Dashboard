import pandas as pd
import plotly.express as px

ufo_data = pd.read_csv("data/ufo_sighting_data.csv", low_memory=False)
ufo_data['Date_time'] = pd.to_datetime(ufo_data['Date_time'], errors='coerce')


#Months
months = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}

for month in months:
    months[month] = (ufo_data["Date_time"].dt.month==month).sum()

month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
months_values = list(months.values())

months={"month":month_names, "counts":months_values}
fig = px.bar(months, x="month", y="counts")
fig.write_html("html/months.html")

month_perc = {}
sum_reports = sum(months_values)
for month, count in zip(month_names, months_values):
    month_perc[month] = (count/sum_reports)*100

print("Total Reports with date: ",sum_reports)
print("For context, 1% is equivalent to, ", 0.01*sum_reports," reports")
for month in month_perc:
    print(month, ":", "{:.2f}".format(month_perc[month]),"% of reports")

# =================================================================================
# Seasons

# =================================================================================
# Years

# =================================================================================
# Time of Day

# =================================================================================
# UFO Shape

# =================================================================================
# Length of Encounter
