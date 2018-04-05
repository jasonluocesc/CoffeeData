import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("data/coffees.csv")

data.coffees = pd.to_numeric(data.coffees,errors="coerce")
#data.coffees = data.coffees.astype(int)
plt.interactive(False)
data.dropna(inplace=True)
data.timestamp = pd.to_datetime(data.timestamp)
#data.plot(x='timestamp',style='.-')
#plt.show()
#print(data.head())
#print(data.iloc[:5])
#print(data[data.timestamp<"2013-01-13"].tail())

# Who contribute most to the dataset?
data.contributor.value_counts()
#data.plot(kind="bar")
#plt.show()

# On which weekdays were contributions made
weekdays = data.timestamp.dt.weekday
data = data.assign(weekdays = weekdays)
weekday_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weekday_dict = {key:weekday_names[key] for key in range(7)}

def day_of_week(idx):
    return weekday_dict[idx]

data.weekdays = data.weekdays.apply(day_of_week)

weekday_counts = data.groupby("weekdays").count()
weekday_counts = weekday_counts.loc[weekday_names] #organize the weekday data order
weekday_counts.coffees.plot(kind="bar")
plt.show()

# 2 Weekday trends
# first, we'll set our timestamps to the dataframe's index