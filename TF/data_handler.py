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
#weekday_counts.coffees.plot(kind="bar")


# 2 Weekday trends
# first, we'll set our timestamps to the dataframe's index
data.index = data.timestamp
data.drop(["timestamp"],axis=1,inplace=True)

midnight = pd.date_range(data.index[0],data.index[-1],freq="D",normalize=True)
new_index = midnight.union(data.index)
upsampled_data = data.reindex(new_index) #there are NaNs in the data
#we can fill in hte NaNs using interpolation
upsampled_data = upsampled_data.interpolate(method="time")
daily_data = upsampled_data.resample("D").asfreq()
daily_data = daily_data.drop(["contributor"],axis=1)
daily_data["weekdays"] = daily_data.index.weekday_name
#daily_data.plot()
#plt.show()
#print(daily_data.head(10))


#How many coffee is consumed by an given day.
coffees_made = daily_data.coffees.diff().shift(-1)
daily_data["coffees_made_today"] = coffees_made
coffees_by_day = daily_data.groupby("weekdays").mean()
coffees_by_day = coffees_by_day.loc[weekday_names]
#print(coffees_by_day)
#coffees_by_day.coffees_made_today.plot(kind="bar")
#plt.show()

#
people = pd.read_csv("data/department_members.csv",index_col="date",parse_dates=True)
daily_data = daily_data.join(people, how="outer").interpolate(method="nearest")

daily_data["coffees_per_person"] = \
    daily_data.coffees_made_today/daily_data.members
#daily_data.coffees_per_person.plot()
#plt.show()

# Coffee machine broken, we have to drop those days

machine_status = pd.read_csv("data/coffee_status.csv",index_col="date",parse_dates=True)

numerical_status = machine_status.status == "OK"

#print(machine_status.status.value_counts())
daily_data = daily_data.join(machine_status)

#
#daily_data.numerical_status*=100
daily_data["numerical_status"] = daily_data.status=="OK"
print(daily_data)
daily_data[['numerical_status','coffees_made_today']].plot()
plt.show()