# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 23:22:48 2023

@author: iyino
"""
# Use numpy function to count the number of students who scored above 90.
# Use numpy function to calculate the percentage of students who scored above 90.
# Use numpy function to calculate the percentage of students who scored below 75.
# Use numpy function to extract all the grades above 90 and put them in a new array called "high_performers".
# Create a new array called "passing_grades" that contains all the grades above 75.
# Print the result of all the above steps.
# Note:

# to calculate percentage use numpy.mean(grades > 90) * 100
# to extract the grades above 90 use grades[grades > 90]
# to extract the grades above 75 use grades[grades > 75]
# You can use other numpy functions as well to 
#analyze the data as you want. The above steps are just examples of what can be done.

import numpy as np
grades = np.array([85, 90, 88, 92, 95, 80, 75, 98, 89, 83]) 
print(grades)

mean = np.mean(grades)
median = np.median(grades)
std = np.std(grades)
print(mean)
print(median)
print(std)

maximum = np.max(grades)
minimum = np.min(grades)
print(maximum)
print(minimum)

ascending = np.sort(grades)#function for ascending
print(ascending)

highest = np.argmax(grades)#higest index
print(highest)

no_student_high = np.count_nonzero(grades > 90)
print(no_student_high)

percentage1 = np.mean(grades > 90)* 100
percentage2 = np.mean(grades < 75)* 100
print(percentage1)
print(percentage2)

high_performer =grades[grades > 90]
print(high_performer)

passing_grades = grades[grades > 75]
print(passing_grades)








