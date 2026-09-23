animals = ['cat','dog','rabbit','hamster','dog','parrot','dog']
first_dog_ind = animals.index('dog')
print(f"first dog :{first_dog_ind}")

second_dog_ind = animals.index('dog',first_dog_ind+1)
print(f"second dog :{second_dog_ind}")


third_dog_ind = animals.index('dog',second_dog_ind+1)
print(f"third dog :{third_dog_ind}")
