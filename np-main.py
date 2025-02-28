import numpy as np
a = [2 , 3 , 4]
b = [3 , 5 , 6]

print(f"a type:  {type(a)},b array:{type(b)}")

print(np.add(a , b))


A = np.array([2,3,6,4])
print(A[0])
print(f"type A :{type(A)}")

B = np.ones(5)
C = np.zeros(3)
D = np.empty(3)

print(f"b : {B} , C: {C} , D: {D}")

T= np.arange(4)
print(T)

G = np.arange(2 , 9 , 2)
print(G)

S = np.linspace(0 , 10 , num=5)
print(S)

#N-dimensional array
m = np.array([
  [0, 1 , 2 , 3],
  [4 , 5 , 6 ,7],
 ])

print(m.ndim)
print(m.size)
print(m.shape)

F = np.array([
    [
        [0 , 1 , 2 , 3 ],
        [4 , 5 , 6 , 7],
        [8 , 9 , 10 , 11 ]
    ],
    [
        [0 , 1 ,2, 3 ],
        [4, 5 , 6 ,7],
        [8 , 9 , 10 , 11]
    ]
])

print(F.ndim)
print(F.size)
print(F.shape)


#4

A1 = [1, 5 , 2 , 7]
print(np.prod(A1))

print(np.power([2 , 3.5],3))

print(np.sin(np.linspace(-np.pi/2,np.pi/2 , 100)))

print(np.sqrt(4))
print(np.emath.sqrt(-4))

print(np.log(1))
print(np.emath.log(-2))

A2 = np.arange(12)
print(A2)

B1 = A2.reshape(3 , 4)
C1 = B1.reshape(-1)
# C2 = B1.raven()
print(C1)
# print(C2)

D1 = B1.flatten()
print(D1)

#6

A3 = np.arange(3,9)
print(A3)
print("A3[0]:",A3[0])
print("A3[1]:",A3[1])
print("A3[2:]",A3[2:])
print("A3[-3:]:",A3[-3:])
print("A3[2:4]:",A3[2:4])

#in list python
# lst = [[2 , 4 , 5 , 6],[3 , 5 , 6 , 8]]
# print(lst[0][1])

A4 = np.arange(12).reshape(3 , 4)
print(A4)

print("A4[0]:",A4[0])
print("A4[0,1]:",A4[0,1])
print("A4[0,1:]:",A4[0,1:])
print("A4[0,:]:",A4[0,:])
print("A4[2,1:3]:",A4[2,1:3])
print("A4[0]:",A4[0])

A5= np.arange(12).reshape(3,4)
print(A5[A5<5])
Three_up = (A5 >= 3)
print(A5[Three_up])
print(Three_up)

print(A5[(A5>2)&(A5<11)])
print(A5[(A5<2)|(A5 % 3 == 0)])


#array operation - 
A6 = np.array([1,3,2,7])
A7 = np.array([4 , 1 , 1 ,3])
print(A6 + A7)
print(np.add(A6,A7))
print(A6 * A7)
print(np.multiply(A6 , A7))
print(A6 ** A7)
print(np.power(A6 , A7))

x1 = np.array([[1,2],[3,4]])
y1 = np.array([[3,1],[4,7]])
print(x1 @ y1)
print(np.matmul(x1 , y1))

#Broadcasting
A8 = np.array([1 , 2 , 3])
A9 = 2
print(A8 * A9)

# A10 = np.array([1 , 2 , 3],[4 , 5 , 6])
A11 = np.array([1 , 2 , 3])
# C4 = A10 + A11
# print(C4)

#(m , n) op (1 , n)=> (m , n)
#(m , n) op (1 , n)=> (m , n)
#(m , 1) op (1 , n)=> (m , n)
#(1 , n) op (1 , n)=> (1 , n)

A12 = np.array([[0],[10],[20],[30]])
A13 = np.array([0 , 1 , 2])
print(A12 + A13)


A14 = np.array([1 , 2 , 3 , 4 , 5])
mean = A14.mean()
std = A14.std()

normalized_A = (mean)/std
print(normalized_A)


#====================
arr = np.array([1 , 2 , 3 , 4 , 5,6])

arr_2d = np.array([[1 , 2 , 3 ], [4 , 5 , 6]])
zeros = np.zeros((3 , 3))

ones = np.ones((2, 4))

identity_matrix = np.eye(3)

range_arr = np.arange(0 , 10 , 2)
linspace_arr = np.linspace(0 , 1 , 5)
random_arr = np.random.rand(3 , 3)

arr.shape
print(arr.shape)
print(arr.ndim)
print(arr.size)
print(arr.dtype)


arr1 = np.array([11 , 12 , 13])
arr2 = np.array([21 , 22 , 23])
arr3 = np.array([31 , 32 , 33])
arr4 = np.array([41 , 42 , 43])

reshaped_arr = arr.reshape(2,3)
print(reshaped_arr)
transposed_arr = arr.T
flattened_arr = arr.flatten()
concatenated = np.concatenate((arr1 , arr2), axis=0)
print(concatenated)
stacked = np.vstack((arr3 ,arr4))
print(stacked)

element = arr[1:2]

sliced_arr = arr[1:4]
sliced_arr = arr_2d[0:2 , 1:3]
filtered_arr = arr[arr>3]

result2 = arr1 + arr2

result3 = arr1 * arr2

result = np.dot(arr1 , arr2)

total = np.sum(arr1)

mean = np.mean(arr1)

std_dev = np.std(arr1)
sqrt_arr = np.sqrt(arr1)
exp_arr = np.exp(arr1)
print(f"std : {std_dev} , sqrt :  {sqrt_arr} , exp : {exp_arr}")

# det = np.linalg.det(arr1)


# inv = np.linalg.inv(arr_2d)
# eigenvalues, eigenvectors = np.linalg.eig(arr_2d)
# solution = np.linalg.solve(A , b)

min_val = np.min(arr1)
max_val = np.max(arr1)

median = np.median(arr1)
percentile = np.percentile(arr_2d , 50)
print(percentile)
print(np.ndim(arr_2d))