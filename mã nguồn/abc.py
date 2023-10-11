import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow.compat.v1 as tf
from numpy import array
import csv

tf.disable_v2_behavior()

""" file1 = 'Student_Performance.csv'
data_set1 = []
with open(file1, mode='r', encoding = 'utf-8-sig') as file:
    reader = csv.reader(file)
    for row in reader:
        data_set1.append(row)
in_data1 = np.array(data_set1)
print(in_data1)
print(in_data1[:][0]) """

df = pd.read_csv('Student_Performance.csv')
in_data = array(df.iloc[:,:])
hours_studies = in_data[:, 0]
performance_index = in_data[:, 5]
print(hours_studies)

# Plot of Training Data
plt.scatter(hours_studies, performance_index)
plt.xlabel('hours_studies')
plt.ylabel('performance_index')
plt.title("Training Data")
plt.show()

X = tf.placeholder("float")
Y = tf.placeholder("float")

n = len(hours_studies)
print(n)
# khởi tạo biến w và b
W = tf.Variable(np.random.randn(), name = "W")
b = tf.Variable(np.random.randn(), name = "b")
# thiết lập tốc độ học
learning_rate = 0.1
# số vòng lặp
training_epochs = 10000
# Hàm tuyến tính
y_pred = tf.add(tf.multiply(X, W), b)
 
# Mean Squared Error Cost Function
cost = tf.reduce_sum(tf.pow(y_pred-Y, 2)) / (2 * n)
 
# Tối ưu bằng Gradient Descent 
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)
 
# Thiết lập Global Variables 
init = tf.global_variables_initializer()
# Starting the Tensorflow Session
with tf.Session() as sess:
     
    # Initializing the Variables
    sess.run(init)
     
    # Iterating through all the epochs
    for epoch in range(training_epochs):
         
        # Feeding each data point into the optimizer using Feed Dictionary
        for (_x, _y) in zip(hours_studies, performance_index):
            sess.run(optimizer, feed_dict = {X : _x, Y : _y})
         
        # Displaying the result after every 50 epochs
        if (epoch + 1) % 50 == 0:
            # Calculating the cost a every epoch
            c = sess.run(cost, feed_dict = {X : hours_studies, Y : performance_index})
            print("Epoch", (epoch + 1), ": cost =", c, "W =", sess.run(W), "b =", sess.run(b))
     
    # Storing necessary values to be used outside the Session
    training_cost = sess.run(cost, feed_dict ={X : hours_studies, Y : performance_index})
    weight = sess.run(W)
    bias = sess.run(b)
# Calculating the predictions
predictions = weight * hours_studies + bias
print("Training cost =", training_cost, "Weight =", weight, "bias =", bias, '\n')
# Plotting the Results
plt.plot(hours_studies, performance_index, 'ro', label ='Original data')
plt.plot(performance_index, predictions, label ='Fitted line')
plt.title('Linear Regression Result')
plt.legend()
plt.show()
