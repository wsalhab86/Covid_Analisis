import csv
import random
import copy



Covid_Cases = []
with open ('covid_data.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        Covid_Cases.append(dict(row))
print (Covid_Cases)

new_cases = sum(int(row['new_cases']) for row in Covid_Cases)
Deaths = sum(int(row['deaths']) for row in Covid_Cases)
Recoveries = sum(int(row['recovered']) for row in Covid_Cases)

average_new_cases = new_cases / len(Covid_Cases)
print("The daily average of infected people is ",average_new_cases)

random_day = random.choice(Covid_Cases)
print("Covid records for the date : ",random_day['date'])
print("New Cases:", random_day['new_cases'])
print("Deaths:", random_day['deaths'])
print("Recoveries:", random_day['recovered'])

