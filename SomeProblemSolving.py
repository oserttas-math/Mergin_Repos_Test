def sum_multiples(n):
    '''This Function Sums Up Multiples of
        3 or 5 Within Range of Number n'''
    n = int(n)
    numbers = []
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            numbers.append(i)
    return np.sum(numbers)
    
