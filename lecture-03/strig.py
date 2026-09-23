string1 = "Mery"
string2 = "Mark"

if string1 == string2:
    print(f'"{string1}" and "{string2}" are equal ')
else:
    print(f'"{string1}" and "{string2}" are not equal ')
    
if string1 < string2:
    print(f'"{string1}" come before "{string2}" in lexicographincal oder')
elif string1 > string2:
    print(f'"{string1}" come after "{string2}" in lexicographincal oder')


if string1.lower() == string2.lower():
    print(f'"{string1}" and "{string2}" are equal when case in ignored.')
else:
    print(f'"{string1}" and "{string2}" are not equal when case in ignored.')
