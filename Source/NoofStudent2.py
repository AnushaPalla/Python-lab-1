#To find the common student in two classes and to print common and non-common student from the class..

#declaring empty lists
Python = []
Web = []

print("Enter students of python class,Enter none to stop ")
while(True): #loop to append the data into python class
    temp_var = input("Enter name: ")

    if(temp_var =='none'):
        break
    else:
        Python.append(temp_var)

print("Enter students of Web class, Enter none to stop: ")
while (True): #loop to append the data into web class
    temp_var = input("Enter name: ")

    if (temp_var == 'none'):
        break
    else:
        Web.append(temp_var)

#to print the common students in both class
print("students attending both the classes: \n")
for x in Python: #loop for finding common students
    if x in Web:
        print(x)


#to print the non-common students in both class
print("students who do not attend both the courses in common: \n")
for y in Python: #loop for finding non-common students
    if y not in Web:
        print(y)
for z in Web:
    if z not in Python:
        print(z)