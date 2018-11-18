hobbies = []

for i in range(3):
    hobby = input("What is your %s Hobby\n" % (i + 1))
    hobbies.append(hobby)

for hobby in hobbies:
    print(hobby)
