# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: Matthew McCabe
# Section: 538 102
# Assignment: lab 11b
# Date: 11/14/22
import matplotlib.pyplot as plt
import numpy as np

'''
Act I
'''

m = np.array([1.00583, -0.087156, 0.087156, 1.00583]).reshape(2, 2)
v = np.array([1, 0]).reshape(2, 1)
v_list = np.array([])

for i in range(250):
    vp = np.dot(m, v)
    v = vp
    v_list = np.append(v_list, v)

plt.plot(v_list, 'b')
plt.title('Tornado')
plt.ylabel('Y Axis')
plt.xlabel('X Axis')
plt.show()

