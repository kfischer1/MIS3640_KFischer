import time
print(time.time())

#number of minutes
minutes = (time.time()// 60)
print('Minutes:', minutes)

#number of hours
hours = (minutes // 60)
print('Hours:', hours)

#number of days
days = (hours // 24)
print('Days:', days)

#number of years
years = (days // 365)
print('Years: ', years)






