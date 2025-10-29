#continue -skips current iteration and move to next iteration
for num in range(10):
    if num%2==0:
        continue
    else:
        print(num)