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

"""
EXP-5


from sklearn.linear_model import LinearRegression
import pickle
import numpy as np

X = np.array([[1], [2], [3], [4], [5]])
Y = np.array([2, 4, 6, 8, 10])

model = LinearRegression()
model.fit(X, Y)

with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully")


from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    value = float(request.form["value"])
    prediction = model.predict([[value]])
    return render_template("index.html", result=f"Predicted Output: {prediction[0]}")

if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    <!DOCTYPE html>
<html>
<head>
    <title>ML Model Deployment</title>
</head>
<body>
    <h2> Linear Regression </h2>
    <form action="/predict" method="post">
        Enter value:
        <input type="text" name="value" required>
        <button type="submit"> Predict </button>
    </form>
    <h3> {{ result }} </h3>
</body>
</html>

"""
    
"""
EXP-6


from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

X, Y = load_breast_cancer(return_X_Y=True)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

# Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, Y_train)
rf_pred = rf_model.predict(X_test)
print("Random Forest Accuracy: ", accuracy_score(Y_test, rf_pred))

# Gradient Boosting
gb_model = GradientBoostingClassifier(n_estimators=100, random_state=42)
gb_model.fit(X_train, Y_train)
gb_pred = gb_model.predict(X_test)
print("Gradient Boosting Accuracy: ", accuracy_score(Y_test, gb_pred))

# Stacking
estimators = [
    ('rf', RandomForestClassifier(n_estimators=50, random_state=42)),
    ('svm', SVC(probability=True))
]
stack_model = StackingClassifier(estimators=estimators, final_estimator=LogisticRegression())
stack_model.fit(X_train, Y_train)
stack_pred = stack_model.predict(X_test)
print("Stacking Accuracy: ", accuracy_score(Y_test, stack_pred))


"""
    
    
"""

EXP-7


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
from sklearn.feature_selection import SelectKBest, f_classif

data = pd.DataFrame({
    'Age': [22, 25, 47, 52, 46],
    'Salary': [25000, 30000, 50000, 60000, 52000],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Female'],
    'Purchased': [0, 1, 1, 0, 1]
})

print("Original Data: \n", data)

# Encoding
le = LabelEncoder()
data['Gender'] = le.fit_transform(data['Gender'])
print("\n After Encoding: \n", data)

# Scaling
scaler = StandardScaler()
data[['Age', 'Salary']] = scaler.fit_transform(data[['Age', 'Salary']])
print("\n After Scaling: \n", data)

# Feature Selection
X = data[['Age', 'Salary', 'Gender']]
Y = data['Purchased']
selector = SelectKBest(score_func=f_classif, k=2)
X_new = selector.fit_transform(X, Y)
print("\n Selected Features: \n", X_new)


"""
    
    
"""
EXP-8


import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

texts = ["I love this movie", "This film is terrible", "Amazing Experience", "I enjoyed this film", "I hate this movie"]
labels = [1, 0, 1, 0, 0] # Adjusted based on common logic, source shows [1,0,1,0,1,0]

tokenizer = Tokenizer(num_words=1000)
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)

max_len = 5
X = pad_sequences(sequences, maxlen=max_len)
y = np.array(labels)

model = Sequential()
model.add(Embedding(input_dim=1000, output_dim=16, input_length=max_len))
model.add(SimpleRNN(32))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=['accuracy'])
model.summary()
model.fit(X, y, epochs=10, batch_size=2)

# Prediction
test_text = ["I really love this film"]
test_seq = tokenizer.texts_to_sequences(test_text)
test_pad = pad_sequences(test_seq, maxlen=max_len)
prediction = model.predict(test_pad)

if prediction > 0.5:
    print("Positive Review")
else:
    print("Negative Review")
    
"""
    
    
"""
EXP-9


import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

(X_train, Y_train), (X_test, Y_test) = tf.keras.datasets.mnist.load_data()
X_train = X_train / 255.0
X_test = X_test / 255.0

X_train = X_train.reshape(-1, 28, 28, 1)
X_test = X_test.reshape(-1, 28, 28, 1)

model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=['accuracy'])
model.fit(X_train, Y_train, epochs=5, batch_size=64)

test_loss, test_acc = model.evaluate(X_test, Y_test)
print(f" Test Accuracy: {test_acc}")

prediction = model.predict(X_test[:1])
print("Predicted digit:", np.argmax(prediction))


"""
    
    
"""
EXP-10


import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

data = load_iris()
X = data.data
Y = data.target
Y = to_categorical(Y, num_classes=3)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

model = Sequential()
model.add(Dense(16, input_dim=4, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(3, activation='softmax'))

model.compile(optimizer="adam", loss='categorical_crossentropy', metrics=['accuracy'])
history = model.fit(X_train, Y_train, epochs=50, batch_size=5, validation_split=0.2)

"""
