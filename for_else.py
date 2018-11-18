fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print("You have...")
for fruit in fruits:
    if fruit == 'tomato':
        print("A tomato is not a fruit!")
        break
    else:
        print('A', fruit)
else:
    print("A fine selection of fruits")
