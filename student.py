'''
8) Create a dictionary named student with the following key-value pairs:

"name": Your Name
"age": Your Age
"major": Your Major
"hobbies": A list of your top three hobbies
Add a new key-value pair for "State": Your State of Residence

Update the "age" to your current age + 1

Write a loop to iterate over the key-value pairs in the student 
dictionary and print each pair on a new line in a well formatted way.
'''
#create dictionary
student = {"name": "Grant","age": 20,"major": "Finance and Management Information Systems","hobbies": ["Piano", "Fishing", "Hunting"]}

#Add state
student["State"] = "Your State of Residence"

#update age
student["age"] += 1

for key, item in student.items():
    print(f"{key}: {item}\n")
