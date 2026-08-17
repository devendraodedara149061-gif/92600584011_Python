student = {
    "name": "Devendra",
    "age": 21,
    "marks": 80
}

print(student)

print("Name:", student["name"])
print("Keys:", student.keys())
print("Values:", student.values())


student["city"] = "Rajkot"

print("Updated dictionary:", student)


for key in student:
    print(key, ":", student[key])