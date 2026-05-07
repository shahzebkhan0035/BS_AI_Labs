#!/usr/bin/env python
# coding: utf-8

# # Task 1 — Creating Arrays

# In[1]:


import numpy as np

# 1. Create a 1D NumPy array containing values from 1 to 10
array1 = np.arange(1, 11)

# 2. Create a 2D array of size 3×3
array2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# 3. Create an array of zeros of size 4×4
zeros_array = np.zeros((4, 4))

# 4. Create an array of ones of size 2×5
ones_array = np.ones((2, 5))

# 5. Display all arrays
print("1D Array:")
print(array1)

print("\n2D Array (3x3):")
print(array2)

print("\nZeros Array (4x4):")
print(zeros_array)

print("\nOnes Array (2x5):")
print(ones_array)


# # Task 2 — Array Properties

# In[3]:


import numpy as np

# Create a 2D array
array = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# 1. Find shape of the array
print("Shape of array:", array.shape)

# 2. Find total number of elements
print("Total elements:", array.size)

# 3. Find data type of elements
print("Data type:", array.dtype)

# 4. Find number of dimensions
print("Number of dimensions:", array.ndim)


# 5. Why shape is important:
#Shape is important because:
#AI models expect data in a specific format.
#Images, text, and datasets are stored as multidimensional arrays.
#Incorrect shapes can cause training or prediction errors.
#Neural networks use shapes to process inputs and outputs correctly.''


# # Task 3 — Indexing

# In[4]:


import numpy as np

# 1. Create an array
arr = np.array([10, 20, 30, 40, 50, 60])

# 2. Access elements

# First element
print("First element:", arr[0])

# Last element
print("Last element:", arr[-1])

# Third element
print("Third element:", arr[2])

# 3. Print all values greater than 30
print("Values greater than 30:", arr[arr > 30])


# # Task 4 — Slicing

# In[5]:


import numpy as np

# Create array
arr = np.array([10, 20, 30, 40, 50, 60])

# 1. Extract elements from index 1 to 4
print("Elements from index 1 to 4:", arr[1:5])

# 2. Reverse the array using slicing
print("Reversed array:", arr[::-1])

# 3. Extract alternate elements
print("Alternate elements:", arr[::2])

# 4. Create a 3×3 matrix
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Print first row
print("First row:", matrix[0])

# Print second column
print("Second column:", matrix[:, 1])

# Print last two rows
print("Last two rows:")
print(matrix[1:])


# # Task 5 — Vectorization

# In[6]:


import numpy as np

# 1. Create an array
arr = np.array([1, 2, 3, 4, 5])

# 2. Multiply all elements by 5 without using loops
print("Multiply by 5:", arr * 5)

# 3. Add 10 to all elements
print("Add 10:", arr + 10)

# 4. Square all elements
print("Squared elements:", arr ** 2)

# 5. Why vectorization is important in AI:
# Vectorization allows operations on entire arrays without loops.
# It makes computations much faster and more efficient.
# AI and Machine Learning work with large datasets,
# so fast mathematical operations are very important.
# NumPy uses optimized low-level implementations,
# which improve performance in AI models and neural networks.


# # Task 6 — Broadcasting

# In[7]:


import numpy as np

# 1. Create a 2D array of size 2×3
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# 2. Add value 10 to all elements using broadcasting
print("After adding 10:")
print(arr + 10)

# 3. Multiply entire array by 2
print("After multiplying by 2:")
print(arr * 2)

# 4. How broadcasting helps in Machine Learning:
# Broadcasting allows NumPy to perform operations
# on arrays of different shapes automatically.
# It removes the need for loops and makes calculations faster.
# In Machine Learning, broadcasting is useful for:
# - Normalizing datasets
# - Updating weights in neural networks
# - Performing matrix operations efficiently
# This improves speed and performance when working with large data.


# # Task 7 — Matrix Addition and Subtraction

# In[8]:


import numpy as np

# 1. Create two matrices of size 2×2
matrix1 = np.array([
    [1, 2],
    [3, 4]
])

matrix2 = np.array([
    [5, 6],
    [7, 8]
])

# 2. Perform addition
addition = matrix1 + matrix2

# Perform subtraction
subtraction = matrix1 - matrix2

# 3. Display results
print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

print("\nAddition:")
print(addition)

print("\nSubtraction:")
print(subtraction)


# # Task 8 — Matrix Multiplication

# In[9]:


import numpy as np

# 1. Create two matrices
matrix1 = np.array([
    [1, 2],
    [3, 4]
])

matrix2 = np.array([
    [5, 6],
    [7, 8]
])

# 2. Perform matrix multiplication using np.dot()
multiplication = np.dot(matrix1, matrix2)

# 3. Find transpose of matrix
transpose = matrix1.T

# Display results
print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

print("\nMatrix Multiplication:")
print(multiplication)

print("\nTranspose of Matrix 1:")
print(transpose)

# 4. Relation of matrix multiplication with neural networks:
# Neural networks use matrix multiplication to process data.
# Inputs, weights, and outputs are represented as matrices.
# During forward propagation, inputs are multiplied by weights
# to calculate predictions.
# Matrix multiplication makes computations faster and efficient,
# especially for large AI and deep learning models.


# # Task 9 — Random Arrays

# In[10]:


import numpy as np

# 1. Generate a random integer array of size 4×4 between 1 and 100
int_array = np.random.randint(1, 101, (4, 4))

# 2. Generate random decimal values
decimal_array = np.random.rand(4, 4)

# 3. Find maximum, minimum, and average values
print("Random Integer Array:")
print(int_array)

print("\nRandom Decimal Array:")
print(decimal_array)

print("\nMaximum value:", np.max(int_array))

print("Minimum value:", np.min(int_array))

print("Average value:", np.mean(int_array))

# 4. Why random numbers are important in AI:
# Random numbers are used in AI and Machine Learning for:
# - Initializing neural network weights
# - Splitting training and testing data
# - Random sampling of data
# - Data augmentation
# - Simulation and optimization algorithms
# Randomness helps models learn better and avoid overfitting.


# # Task 10 — Student Marks Analysis

# In[11]:


# Marks of 10 students
marks = [78, 92, 45, 66, 81, 39, 55, 88, 73, 49]

# 1. Display marks
print("Marks of students:", marks)

# 2. Calculations
average = sum(marks) / len(marks)
highest = max(marks)
lowest = min(marks)

print("\nAverage marks:", average)
print("Highest marks:", highest)
print("Lowest marks:", lowest)

# 3. Count students scoring above 80
above_80 = sum(1 for mark in marks if mark > 80)
print("\nStudents scoring above 80:", above_80)

# 4. Students who failed (below 50)
failed_students = [mark for mark in marks if mark < 50]
print("Students who failed (below 50):", failed_students)


# # Task 11 — Image Pixel Simulation

# In[12]:


import numpy as np

# 1. Create a random 5×5 array representing image pixels
# Each value represents pixel intensity (0 = black, 255 = white)
image = np.random.randint(0, 256, (5, 5))

# Display the image (pixel matrix)
print("Image (5x5 pixels):\n", image)

# 2. Find brightest pixel (maximum value in array)
brightest_pixel = np.max(image)

# 2. Find darkest pixel (minimum value in array)
darkest_pixel = np.min(image)

# 2. Find shape of image (rows, columns)
shape = image.shape

# Display results
print("\nBrightest pixel value:", brightest_pixel)
print("Darkest pixel value:", darkest_pixel)
print("Image shape:", shape)

# 3. Explanation:
# AI reads images as arrays (matrices) of numbers.
# In grayscale images:
# - Each pixel is a single number (0 to 255)
# - 0 = black, 255 = white
#
# In colored images:
# - Each pixel has 3 values [R, G, B]
# - Example: [255, 0, 0] = red color
#
# AI models (like CNNs) process these arrays to detect:
# - edges
# - shapes
# - objects
#
# This is how computer vision systems see images.


# # Task 12 — Data Normalization

# In[13]:


import numpy as np

# 1. Create an array of numerical data
data = np.array([10, 20, 30, 40, 50])

print("Original data:", data)

# 2. Normalize the dataset using Min-Max Normalization formula:
# normalized_x = (x - min) / (max - min)

min_val = np.min(data)
max_val = np.max(data)

normalized_data = (data - min_val) / (max_val - min_val)

# 3. Print normalized values
print("Normalized data:", normalized_data)

# 4. Explanation:
# Normalization scales all values between 0 and 1.
# This helps AI models because:
# - All features are on the same scale
# - Prevents large values from dominating small ones
# - Improves training speed and accuracy
# - Helps gradient descent converge faster
#
# Without normalization, models may become biased toward larger numbers,
# leading to poor performance.


# # Task 13 — Mini AI Dataset Task

# In[14]:


import numpy as np

# 1. Create a small AI dataset (as normal Python list first)
# Columns: Age, Salary, Purchased (0 = No, 1 = Yes)

data_list = [
    [22, 25000, 0],
    [25, 30000, 1],
    [30, 45000, 1],
    [35, 50000, 0],
    [40, 60000, 1]
]

print("Original Dataset (List):")
print(data_list)

# Convert dataset into NumPy array
data = np.array(data_list)

# 2. Separate input features and output labels
# Input features: Age and Salary
X = data[:, :2]

# Output labels: Purchased (0 or 1)
y = data[:, 2]

print("\nInput Features (X):\n", X)
print("\nOutput Labels (y):\n", y)

# 3. Find average salary
average_salary = np.mean(data[:, 1])
print("\nAverage Salary:", average_salary)

# 4. Find highest age
highest_age = np.max(data[:, 0])
print("Highest Age:", highest_age)

# 5. Display dataset shape
print("Dataset Shape:", data.shape)

# Explanation:
# We first created the dataset as a normal Python list.
# Then we converted it into a NumPy array for efficient numerical operations.
#
# AI uses this structured data to learn relationships between:
# - Age
# - Salary
# - Purchase decision (0/1)
#
# This helps models predict whether a new customer will buy a product.


# In[ ]:




