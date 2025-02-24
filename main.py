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