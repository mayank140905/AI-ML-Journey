# basic print statement
print("hello world")  

# square fxn
def square(num):
    return num * num
print(square(5))  # Output: 25

# even fxn
def is_even(num):
    return num % 2 == 0
print(is_even(4)) # Output: True

# square of a list of numbers
nums = [1, 2, 3, 4, 5]
for i in nums:
    print(square(i)) # Output: 1, 4, 9, 16, 25

# creating a dictionary and accessing its values
student = {
    "name": "Alice",
    "age": 20
}
print(student["name"]) # Output: Alice
print(student.get("age")) # Output: 20

# count vowels in a string
def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Hello, World!"))  # Output: 3



# calculate average marks of a student without using sum() function
student = {
    "name": "Mayank",
    "marks": [80, 90, 70, 85]
}

def average_marks(student):
    marks = student.get("marks", [])
    if not marks:
        return 0
    total = 0
    for i in marks:
        total += i
    return total / len(marks)

print(average_marks(student))  # Output: 81.25