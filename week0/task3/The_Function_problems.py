# version code d345910f07ae
coursera = 1
# Please fill out this stencil and submit using the provided submission script.





## 1: (Problem 1) Tuple Sum
def tuple_sum(A, B):
    '''
    Input:
      -A: a list of tuples
      -B: a list of tuples
    Output:
      -list of pairs (x,y) in which the first element of the
      ith pair is the sum of the first element of the ith pair in
      A and the first element of the ith pair in B
    Examples:
    #>>> tuple_sum([(1,2), (10,20)],[(3,4), (30,40)])
    [(4, 6), (40, 60)]
    '''
    # [ zip()]
    result = []
    for i, v in enumerate(A):
        tmp = []
        for ind, val in enumerate(v):
            tmp.append(A[i][ind] + B[i][ind])
        result.append(tuple(tmp))
    return result


## 2: (Problem 2) Inverse Dictionary
def inv_dict(d):
    '''
    Input:
      -d: dictionary representing an invertible function f
    Output:
      -dictionary representing the inverse of f, the returned dictionary's
       keys are the values of d and its values are the keys of d
    Examples:
    #>>> inv_dict({'goodbye':  'au revoir', 'thank you': 'merci'})
    {'merci':'thank you', 'au revoir':'goodbye'}]
    '''
    return dict(zip(d.values(), d.keys()))



## 3: (Problem 3) Nested Comprehension
def row(p, n):
    '''
    Input:
      -p: a number
      -n: a number
    Output:
      - n-element list such that element i is p+i
    Examples:
    #>>> row(10,4)
    [10, 11, 12, 13]
    '''
    return [i for i in range(p, p + n)]

comprehension_with_row = row(15, 20)

comprehension_without_row = [i for i in range(15, 15 + 20)]



## 4: (Problem 4) Probability Exercise 1
Pr_f_is_even = 5
Pr_f_is_odd  = 5



## 5: (Problem 5) Probability Exercise 2
Pr_g_is_1    = 5
Pr_g_is_0or2 = 5

if __name__ == '__main__':
    print(tuple_sum([(1,2), (10,20)],[(3,4), (30,40)]))
    print(row(10,4))