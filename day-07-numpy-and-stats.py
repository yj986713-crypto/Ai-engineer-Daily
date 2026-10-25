import numpy as np
import pandas as pd

# data - marks of students
marks = np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91])
hours = np.array([5, 7, 4, 8, 6, 3, 9, 5, 6, 7])

# basic info
print("Marks:", marks)
print("Total students:", len(marks))

# mean median calculation
mean_val = np.mean(marks)
median_val = np.median(marks)

print("Mean marks:", mean_val)
print("Median marks:", median_val)

# std deviation - to check how marks are spread
std_val = np.std(marks)
print("Std Dev:", std_val)

# correlation check
# checking if hours and marks are related
corr = np.corrcoef(hours, marks)[0,1]
print("Correlation:", corr)

# filtering top students
top = marks[marks > 85]
print("Students with more than 85:", top)

# making simple dataframe for report
df = pd.DataFrame({'Hours': hours, 'Marks': marks})
print(df.head())
print(df.describe())
