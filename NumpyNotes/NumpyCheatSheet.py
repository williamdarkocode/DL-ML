import numpy as np

# Create array manually
a = np.array([0, 2, 4, 6])

# Get dimension of array
print(a.ndim) #should print 1
#####

# Get shape of array
print(a.shape) #should print (4,) meaning 4 dimensions on 0th axis

# Get length of array
print(len(a)) #should print 4

# Create multidimesional arrays manually
b = np.array([[0, 1, 2], [3, 4, 5]])
b.ndim #should be 2, because its a matrix
b.shape #should be (2, 3) because its a 2x3 matrix
len(b) #should be 2 b/c the length of first dimension is 2

c = np.array([ [ [1,2], [3, 4], [5, 6] ] ])
print(c)
print(c.ndim) #should 3
print(c.shape) #should be (1,3,2) b/c outer most array has only 1 nested array, and first nested array has 3 nested arrays, and 3 nested arrays have 2 elements, so 1x3x2
print(len(c)) #should be 1

d = np.array([ [ [1], [2] ], [ [3], [4] ] ])
print(d) 
print(d.ndim) #should be 3, b/c its a matrix of arrays
print(d.shape) #should be (2, 2, 1)
print(len(d)) #should be 2


#Creating arrays with functions
a =  np.arange(10)
print(a) #creates array with values from 0-10, so 0-(n-1)

b = np.arange(1, 9, 2) #syntax (start, not inclusive end, step size)
print(b) #should print array([1, 3, 5, 7])

c = np.linspace(0, 1, 6) #syntax (start, end inclusive, number of elements in list)
print(c) #should print array([0., 0.2, 0.4, 0.6, 0.8, 1.])

d =  np.linspace(0, 1, 5, endpoint=False) #syntax (start, end not inclusive, numnber of elements, bool for inclusive end or not)
print(d)


#Common arrays
a = np.zeros((3, 3)) #a 3x3 matrix of zeros
print(a)

b = np.ones((2,2)) #a 2x2 matrix of ones
b = np.ones((2,3,4)) #a 2x3x4 matrix of ones. A 2x3 matrix with dim 4 arrays as entries
print(b)

c = np.eye(4) # an identity matrix with diagonal elements set to 1 and 0s everywhere else
print(c) #[[1 0 0 0]
         # [0 1 0 0]
         # [0 0 1 0]
         # [0 0 0 1]]

d = np.diag(np.array([2, 4, 6, 8])) #a diagonal matrix with diagonal entries as the elements of the inputed elements
print(d) #[[2, 0, 0, 0],
         # [0, 4, 0, 0],
         # [0, 0, 6, 0],
         # [0, 0, 0, 8]]

e = np.random.rand(4) #an array of length 4, with values as random floating points in the range [0,1]
f = np.random.randn(4) #an array of lenghth 4 with gaussian random floating point numbers
g = np.random.seed(1234)

g =  np.empty((2,2)) #a numpy array of  shape 2x2 with random values as entries
print(g)

print(g.dtype) #data type of elemennts in array. should be "float64"

#Complex data type
a = np.array([1+2j, 3+4j, 5+6*1j])
print(a[2]) #5.+6.j
a.dtype # "dtype('complex128')"

#Indexing and Slicing
a = np.arange(10) #array([0, 1, 2, 3, 4, 5, 6, 7, 8 , 9])
a[0] # 0
a[7] # 7
a[-1] # 9
a[-4] #6


a[::1] #array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
a[::-1] #reverses the array; whats really happening is the we're accessing elements starting from the back with a step count of 1

print(a[::2]) #array([0, 2, 4, 6, 8]) every other element
print(a[2::2]) #start form the second element and access every other element
print(a[-2::-2]) #a reversed array starting form the second to last, acessing every othe element in reverse
print(a[:7]) #everything up until but not including the 7th index
print(a[3:]) #everything following the 3rd index including the element at the 3rd index
print(a[1:8:1]) #syntax (start, end, step size) start at the first number, and at the sencond (not inclusive), with a step size of the 3rd number

a[:4] = 10 # assign all the values before index 4 (not inclusive) the number 10
print(a)
a[4:] = 7 #assign all elements from index 4, including the element at index 4, the value of 7
print(a)
print('\n')

b = np.diag(a) #a diagonal matrix with diagonal entries as the elements of array a
print(b)
print('\n')

print(b[:2]) #the rows before the 2nd row (not inclusive of the second row)
print(b[::2]) #print every other row
print(b[::3]) #print every fourth (row at index 3) row
print(b[3::2]) #print every other row starting from the fourth (row at index 3 and every other row after)
print('\n')

print(b[::2, ::2]) #for every other row, access every other column
print('\n')
print(b[3:6,2:7]) #get the image of the matrix fromed by the 3-5th row, and 2nd-6th column
print(b[(0,1,2,3,4,5,6,7,8,9), (0,1,2,3,4,5,6,7,8,9)]) # get the diagonals entries of the matrix
