#Syntax of a Dictionary:
#dictionary_name = {key1: value1, key2: value2, key3: value3}

student={"name":'shivani',"age":21,"gender":"female"}
print(student)#{'name': 'shivani', 'age': 21, 'gender': 'female'}

#2. Dictionary Operations
print(student['name'])
print(student.get('course','Not Available'))
#2.2 Adding and Updating Items
student["age"]=22
student["city"]="Palasa"
print(student)#{'name': 'shivani', 'age': 22, 'gender': 'female', 'city': 'Palasa'}
age=student.pop("age")
print(age)#22
print(student)#{'name': 'shivani', 'gender': 'female', 'city': 'Palasa'}
del student["name"]
print(student)#{'gender': 'female', 'city': 'Palasa'}
student.popitem()
print(student)#{'gender': 'female'}
student.clear()
print(student)#{}

#3. Dictionary Built-in Methods
#3.1 Dictionary Methods for Accessing Data
student.get("name","Not found")
print(student)#{}
student={"name":'shivani',"age":21,"gender":"female"}
print(student.keys())#dict_keys(['name', 'age', 'gender'])
print(student.values())#dict_values(['shivani', 21, 'female'])
print(student.items())#dict_items([('name', 'shivani'), ('age', 21), ('gender', 'female')])
#3.2 Dictionary Methods for Adding and Updating Data
student.update({"city":"Palasa"})
print(student)#{'name': 'shivani', 'age': 21, 'gender': 'female', 'city': 'Palasa'}
student.setdefault("city","unknown")
print(student)

#5. Nested Dictionaries
students={"alice":{"age":21,"course":"cs"},
          "bob":{"age":22,"coruse":"java"}}
print(students["alice"]["course"])#cs
#6. Dictionary Comprehension
squares={x:x*x for x in range(1,6)}
print(squares)#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
