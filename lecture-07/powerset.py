attendance_week = [
    ["alice","bob","charlie","david"],
    ["alice","charlie","david"],
    ["alice","bob","david"],
    ["alice","david","eve"],
    ["bob","charlie","david"]
]

attendance_sets = [set(day) for day in attendance_week]
print(attendance_sets)

present_every_d = set.intersection(*attendance_sets)
print("Present every day",present_every_d)

all_stu = set.union(*attendance_sets)
absent_at_least_one = all_stu - present_every_d
print("absent at least day",absent_at_least_one)

first = attendance_sets[0]
last = attendance_sets[-1]
first_butnolast = list(first - last)
print("present on first",first_butnolast)

unique_stu = len(all_stu)
print("total stu",unique_stu)
