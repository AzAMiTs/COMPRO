phonebook = {"anirach":"777-1111","Mickey":"777-2222","Ronaldo":"777:3333"}

print(phonebook)

print(phonebook['Mickey'])
print(phonebook.get('Ronaldo'))


key = 'Pluto'
if key in phonebook:
    print(phonebook['Pluto'])
else:
    print(key+' not in phonebook')

phonebook["simpson"] = "777-4567"
phonebook["Pluto"] = "777-4444"
phonebook["Mickey"] = "777-2122"
print(phonebook)

del phonebook["simpson"]
print(phonebook)


