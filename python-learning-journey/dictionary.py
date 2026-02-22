student={
    "name":"sreeshma",
    "age":25,
    "role":"Developer"
}

#to access
print(student["name"])
print(student)
#update
student["age"]=26
print(student["age"])
#add new value
student["city"]="kochi"
print(student)

#looping
for key,value in student.items():
    print(key,":",value)

