x = input("enter the students list for python.Enter none to halt entering")
python_count = 0
python_students = []
while(x!="none"):
    python_students.append(x)
    python_count = python_count+1
    x = input("enter next student details in python class")
print('students in python class',python_students)
y = input("enter the students list for web development .Enter none to halt entering")
web_count = 0
web_students = []
while(y!="none"):
    web_students.append(y)
    web_count = web_count+1

    y = input("enter next student details in python class")
print('Students in web class',web_students)
set1 = set(python_students)
set2 = set(web_students)
common = set1.intersection(set2)
union = set1.union(set2)

notCommon = union - common

print("In Common- {0}".format(common))
print("Not in Common- {0}".format(notCommon))


