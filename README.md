# Data Visualization of Covid analysis with CSV fill

- ***step 1: Create CSV file with data***
```touch covid_data.csv```
- ***Step 2: Import The necessary modules*** 
```import csv```
``` import copy```
``` import random ```

- ***Step 3: define your Dictionary Template
``` covid_Template```
-Step 4: open the csv file and read the data:***
```
with  open('covid_data.csv') as file:
reader  = csv.DictReader(file) 
```
- **Step 4: Calculate and print the total number of cases, deaths, and recoveries**

**Step 5: Calculate the average number of new cases per day**

***Step 6: Select a random day from the data and print the data for that day***
```
random_day  =  random.choice(Covid_Cases)
```