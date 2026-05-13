"""
EXP-1

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")

    def grade(self):
        if self.marks >= 80:
            print("Grade A")
        elif self.marks >= 50:
            print("Grade B")
        else:
            print("Grade C")

# Creating objects (instances)
s1 = Student("Joe", 85)
s2 = Student("John", 47)

print("Student 1:")
s1.display()
s1.grade()

"""

"""
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result: ", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Please enter valid integers.")

finally:
    print("Execution Completed.")
    
"""

"""
# 1. Writing to a file (w)
f = open("file.txt", "w")
f.write("Hello World \n")
f.write("File Handling Example")
f.close()

# 2. Reading from a file (r)
f = open("file.txt", "r")
data = f.read()
print(data)
f.close()

# 3. Appending to a file (a)
f = open("file.txt", "a")
f.write("\n New Line Added")
f.close()

"""
"""
EXP-2

import pandas as pd
import numpy as np

# Creating the dataset
data = {
    'Name': ['Joe', 'John', 'Karen', 'Sam', 'Tom'],
    'Age': [22, np.nan, 25, 24, np.nan],
    'Marks': [78, 85, np.nan, 90, 88],
    'Branch': ['CSE', 'IT', 'CSE', None, 'IT']
}

# Initializing DataFrame
df = pd.DataFrame(data)
print("Original Values:\n", df)

# Checking for missing values
print("\nMissing Values:\n", df.isnull().sum())

# Data Cleaning: Handling missing values
# Filling Age with Mean, Marks with Median, and Branch with 'Unknown'
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Marks'].fillna(df['Marks'].median(), inplace=True)
df['Branch'].fillna('Unknown', inplace=True)

# Data Transformation: Adding a 'Result' column
df['Result'] = np.where(df['Marks'] >= 40, 'Pass', 'Fail')

# Renaming 'Marks' to 'Score'
df.rename(columns={'Marks': 'Score'}, inplace=True)

# Analysis: Average Score by Branch
avg_score = df.groupby('Branch')['Score'].mean()
print("\nAverage Score by Branch:\n", avg_score)

# Filtering: Students scoring above 80
high_scorers = df[df['Score'] > 80]
print("\nStudents Scoring Above 80:\n", high_scorers)

# Statistical Summary using NumPy
print("\nMax Score: ", np.max(df['Score']))
print("Min Score: ", np.min(df['Score']))
print("Mean Score: ", np.mean(df['Score']))

# Final output
print("\nCleaned and Transformed Data:\n", df)

"""
"""
EXP-3

from sklearn.metrics import accuracy_score, confusion_matrix

# Sample data: y_true are the actual labels, y_pred are the model's guesses
y_true = [1, 0, 1, 1]
y_pred = [1, 0, 0, 1]

print("True: ", y_true)
print("Pred: ", y_pred)

# Calculating Accuracy
# Formula: (Correct Predictions) / (Total Predictions)
acc = accuracy_score(y_true, y_pred)

# Generating a Confusion Matrix
# Shows True Positives, True Negatives, False Positives, and False Negatives
cm = confusion_matrix(y_true, y_pred)

print("Accuracy: ", acc)
print("Matrix: \n", cm)

"""
"""
from sklearn.metrics import mean_squared_error, r2_score

# Sample data: y1 is Actual values, y2 is Predicted values
y1 = [2, 4, 6, 8]
y2 = [2.1, 3.9, 6.2, 7.8]

print("Actual: ", y1)
print("Pred: ", y2)

# Calculating Mean Squared Error (MSE)
# Measures the average squared difference between actual and predicted
mse = mean_squared_error(y1, y2)

# Calculating R-squared (R2) Score
# Measures how well the model fits the data (1.0 is a perfect fit)
r2 = r2_score(y1, y2)

print("MSE: ", mse)
print("R2: ", r2)

"""
"""
EXP-4

from sklearn.cluster import KMeans
import numpy as np

# Sample 2D data points
X = np.array([[1, 2], [1, 4], [10, 2], [10, 4]])

# Initializing KMeans with 2 clusters
k = KMeans(n_clusters=2)
k.fit(X)

print("Data:\n", X)
print("Labels:\n", k.labels_)
print("Centers:\n", k.cluster_centers_)

"""
"""
from sklearn.cluster import DBSCAN
import numpy as np

# Sample 2D data points
X = np.array([[1, 2], [2, 3], [10, 10], [11, 11]])

# eps: maximum distance between two samples to be considered neighbors
# min_samples: number of samples in a neighborhood for a point to be a core point
d = DBSCAN(eps=2, min_samples=2)
d.fit(X)

print("Data:\n", X)
print("Labels:\n", d.labels_)
print("Clusters:", set(d.labels_))

"""
