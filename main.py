numbers = [12, 5, 18, 7, 24, 3, 30]

over_10 = []
count = 0
total = 0
avg = 0
max_num = 0
min_num = 0
even = []
odd = []
above_avg = []

for n in numbers:
    if n > 10:
        over_10.append(n)
        count = count + 1
        total = total + n
        
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

avg = total / count
max_num = max(over_10)
min_num = min(over_10)

for n in numbers:
    if n > avg:
        above_avg.append(n)

print("\n==== NUMBER ANALYSIS REPORT ===\n")
print("Numbers over 10: ",over_10)
print("Count: ",count)
print ("Total: ",total)
print ("Average: ",avg)
print ("Max: ",max_num)
print("Min: ",min_num)
print("Even numbers: ",even)
print("Odd numbers: ",odd)
print ("Above average: ",above_avg)
