# version code ef5291f09f60+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

# Some of the GF2 problems require use of the value GF2.one so the stencil imports it.

from GF2 import one


## 1: (Problem 1) Vector Addition Practice 1
#Please express each answer as a list of numbers
p1_v = [-1, 3]
p1_u = [0, 4]
p1_v_plus_u = [i + j for i, j in zip(p1_v, p1_u)]
p1_v_minus_u = [i - j for i, j in zip(p1_v, p1_u)]
p1_three_v_minus_two_u = [3 * i - 2 * j for i, j in zip(p1_v, p1_u)]



## 2: (Problem 2) Vector Addition Practice 2
p2_u = [-1,  1, 1]
p2_v = [ 2, -1, 5]
p2_v_plus_u = [i + j for i, j in zip(p2_v, p2_u)]
p2_v_minus_u = [i - j for i, j in zip(p2_v, p2_u)]
p2_two_v_minus_u = [2 * i - j for i, j in zip(p2_v, p2_u)]
p2_v_plus_two_u = [i + (2 * j) for i, j in zip(p2_v, p2_u)]



## 3: (Problem 3) Vector Addition Practice 3
# Write your answer using GF2's one instead of the number 1
p3_vector_sum_1 = [i + j for i, j in zip([0, one, one], [one, one, one])]
p3_vector_sum_2 = [i + j + k for i, j, k in zip([0, one, one], [one, one, one], [one, one, one])]



## 4: (Problem 4) GF2 Vector Addition A
# Please express your solution as a subset of the letters {'a','b','c','d','e','f'}.
# For example, {'a','b','c'} is the subset consisting of:
#   a (1100000), b (0110000), and c (0011000).
# The answer should be an empty set, written set(), if the given vector u cannot
# be written as the sum of any subset of the vectors a, b, c, d, e, and f.

u_0010010 = {'d', 'f'}
u_0100010 = {'b', 'd'}



## 5: (Problem 5) GF2 Vector Addition B
# Use the same format as the previous problem

v_0010010 = set()
v_0100010 = set()



## 6: (Problem 6) Solving Linear Equations over GF(2)
#You should be able to solve this without using a computer.
x_gf2 = [0]



## 7: (Problem 7) Formulating Equations using Dot-Product
#Please provide each answer as a list of numbers
v1 = [2,3,-4,1]
v2 = [1,-5,2,0]
v3 = [4,1,-1,-1]



## 8: (Problem 8) Practice with Dot-Product
uv_a = sum([i*j for i, j in zip([1, 0], [5, 4321])])
uv_b = sum([i*j for i, j in zip([0, 1], [12345, 6])])
uv_c = sum([i*j for i, j in zip([-1, 3], [5, 7])])
uv_d = sum([i*j for i, j in zip([-2**0.5/2, 2**0.5/2], [2**0.5/2, -2**0.5/2])])

