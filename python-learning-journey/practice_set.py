employee=("sreeshma",25,"Developer")
name,age,role=employee
print(employee)

sample_set={1,2,3,4,3,2}
print(sample_set)
unique_set=list(set(sample_set))

print(unique_set)

emp={
    "name":"Thadhu",
    "age":25,
    "skill":['office','autoCAD'],
    "experience":{
        "role":"civil engineer",
        "year":2
    }
}

print(emp)
print(emp["experience"]["year"])
print(emp["skill"][1])