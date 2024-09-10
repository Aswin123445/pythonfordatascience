string=input("enter the string you want to check")
vowels=['a','e','i','o','u']
count = 0
for char in string:
    if char in vowels:
       count += 1
       print(f" {char}")
print(f"count of vowels in {string} is {count}")