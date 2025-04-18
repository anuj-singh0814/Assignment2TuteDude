### Print sum of Integers in range of 1 to 50
### Using loop

total_sum = 0
for a in range(1, 51):
    total_sum += a

print(total_sum)

### or we can write like this without using loop
print(sum(range(1, 51)))