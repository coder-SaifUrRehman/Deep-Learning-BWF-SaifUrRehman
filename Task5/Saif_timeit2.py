import timeit  

print('x' * 6)  
print('x' + 'x' + 'x' + 'x'+'x'+'x')  

print(timeit.timeit("y = 'x' * 6", number=10))  
print(timeit.timeit("xy = 'x' + 'x' + 'x' + 'x'+'x','x'", number = 10))  
