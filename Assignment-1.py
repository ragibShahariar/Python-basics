"""Assignment"""
"""Ragib Shahariar"""
"""Developed in Jetbrains IDE"""
"""10/9/24"""

# 1. Dictionary

def manage_courses():
    # 1. Create a dictionary with the initial courses
    courses = {
       "CSE101": {"name": "Introduction to Programming", "credits": 3, "instructor": "Dr. Alice"},
       "CSE102": {"name": "Data Structures", "credits": 4, "instructor": "Dr. Bob"},
       "CSE103": {"name": "Database Systems", "credits": 3, "instructor": "Dr. Carol"}
    }

    # 2. Update the instructor's name for CSE102
    courses["CSE102"]["instructor"] = "Dr. Bob Jr."

    # 3. Add a new course
    courses["CSE104"] = {"name": "Algorithms", "credits": 4, "instructor": "Dr. Dave"}

    # 4. Remove the course CSE101
    del courses["CSE101"]

    # 5. Loop through the dictionary and print the course code along with its details
    for code, details in courses.items():
        print(f"Course Code: {code}")
        for key, value in details.items():
            print(f"  {key.capitalize()}: {value}")
        print()  # Empty line for better readability

# Call the function to execute the operations
manage_courses()

# 2. String

# Given sentence
sentence = "Learning Python is fun and rewarding."

# a. Extract substring using negative slicing
substring = sentence[-26:-14]
print("Extracted substring:", substring)

# b. Modify the original string
modified_sentence = sentence.replace("rewarding", "exciting")
print("Modified sentence:", modified_sentence)

# c. Insert phrase at correct position
insert_phrase = " Keep practicing!"
last_space_index = modified_sentence.rfind(" ")
final_sentence = modified_sentence[:last_space_index] + insert_phrase + modified_sentence[last_space_index:]
print("Sentence with inserted phrase:", final_sentence)

# d. Capitalize first letter of each word
capitalized_sentence = final_sentence.title()
print("Capitalized sentence:", capitalized_sentence)

# 3. List

# Initial list of customers
customers = ["Alice", "Bob", "Charlie", "David", "Eve"]

# a. Access the third customer
print("Third customer:", customers[2])

# b. Change the name of the second customer
customers[1] = "Ben"

# c. Add a new customer
customers.append("Frank")

# d. Remove the customer "David"
customers.remove("David")

# e. Sort the customer names alphabetically
customers.sort()

print("Final customer list:", customers)

# 4. Control flow

grades = [85, 78, 92, 45, 33, 67, 88, 41]

# a. Categorize grades
print("Grade Categories:")
for grade in grades:
    if grade > 80:
        category = "A"
    elif 60 <= grade <= 80:
        category = "B"
    elif 40 <= grade < 60:
        category = "C"
    else:
        category = "F"
    print(f"Score: {grade} - Grade: {category}")

# b. Boost grades function
def boost_grades(grade):
    return grade * 1.05

# Apply boost to grades using map()
boosted_grades = list(map(boost_grades, grades))
print("\nBoosted Grades:")
print(boosted_grades)

# c. Find boosted grades above 90 using lambda
above_90 = list(filter(lambda x: x > 90, boosted_grades))
print("\nBoosted Grades Above 90:")
print(above_90)

# 5. Tuple & Set

# Initial data
books = (
    ("To Kill a Mockingbird", "Harper Lee", 1960),
    ("1984", "George Orwell", 1949),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925)
)
tags = {"classic", "dystopian", "novel", "literature"}

# a. Access the second book's author
print("Second book's author:", books[1][1])

# b. Add a new book record
new_book = ("Brave New World", "Aldous Huxley", 1932)
books = books + (new_book,)

# c. Unpack the third book's details
title, author, year = books[2]
print(f"Third book: {title} by {author}, published in {year}")

# d. Loop through books and print titles
print("Book titles:")
for book in books:
    print(book[0])

# e. Add a new tag and print updated set
tags.add("sci-fi")
print("Updated tags:", tags)

# f. Remove a tag and print updated set
tags.remove("novel")
print("Tags after removal:", tags)