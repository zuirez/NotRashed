marks = [91, 95, 88, 86, 82, 99, 80, 87, 96]

# Finding max value using max function
print(f"Max value is : {max(marks)}")

# Finding max value using for loop

max = 0

for m in marks:
    if m>max:
        max=m
print(max)