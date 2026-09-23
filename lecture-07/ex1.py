survey_results = [
    ["Python","Javascript","C++"],
    ["Python","Javascript","C#"],
    ["Python","Java"],
    ["Python","c++","JavaScript"],
    ["Python","Javascript","C++","Java"],
]

attendance_sets = [set(par) for par in survey_results]
print(attendance_sets)