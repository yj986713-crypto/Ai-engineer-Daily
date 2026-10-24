import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dataset for distribution analysis
marks = [85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 77, 84, 86, 93, 79]

# Plot 1: Histogram - To check marks distribution
# Used in AI to find data bias and outliers
plt.figure()
plt.hist(marks, bins=5, color='#9b59b6', edgecolor='black')
plt.title('Day 6 - Marks Distribution (Histogram)')
plt.xlabel('Marks Range')
plt.ylabel('Number of Students')
plt.savefig('day-06-histogram.png')
plt.show()

# Plot 2: Box Plot - To find outliers
plt.figure()
sns.boxplot(data=marks, color='#e74c3c')
plt.title('Day 6 - Outlier Detection using Box Plot')
plt.savefig('day-06-boxplot.png')
plt.show()
