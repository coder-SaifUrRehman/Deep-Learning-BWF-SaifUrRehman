import timeit

my_list = list(range(10000))

start_time = timeit.default_timer()

sum = 0
for num in my_list:
    sum += num

end_time = timeit.default_timer()

print("list sum:", sum)
print("Execution time of program:", end_time - start_time, "seconds")



