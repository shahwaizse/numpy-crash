import numpy as np

#one dimensional array
one_dimensional_array = np.array([1,2,3,4,5,6])
print(one_dimensional_array)

#two dimensional array
two_dimensional_array = np.array([[1,2], [3,4], [5,6]])
print(two_dimensional_array)

#sequence of integers (5-11)
sequence_of_integers = np.arange(5,12)
print(sequence_of_integers)

#random integers (between 10 & 20)
random_integers = np.random.randint(10,20,10)
print(random_integers)

#floating points (between 0 & 1)
random_floats = np.random.random(6)
print(random_floats)

#task 1 (creating linear dataset)
feature = np.arange(6,21)
print(feature)

label = (feature * 3) + 4
print(label)

#task 2 (adding noise to dataset)
noise = (np.random.random(15) * 4) - 2
print(noise)

label = label + noise
print(label)