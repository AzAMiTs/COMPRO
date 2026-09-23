stu = {"name":"alice","age":25,"grade":"A"}

stu["age"] = 26
stu["major"] = "Computer Science"
print(stu)


del stu["grade"]
print(stu)


removed_major = stu.pop('major')
print(removed_major)
print(stu)