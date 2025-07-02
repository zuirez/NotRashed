score = 5
height = 5.5
is_wining = True

# We can't concatinate different data types without type casting
print("Your score is : " + str(score), "Your height is : " + str(height), "You are wining : " + str(is_wining))

# To solve this problem we use f-string
print(f"Your score is : {score}, Your height is : {height}, Your are wining : {is_wining}")