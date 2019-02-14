#Converting list of tuples into Dictionary with keys and values and convert into sorted order.

input = [('John', ('Physics', 80)), ('Daniel', ('Science', 90)), ('John', ('Science', 95)), ('Mark',('Maths', 100)),
         ('Daniel', ('History', 75)), ('Mark', ('Social', 95))]

#empty dictionary is created
final_dictionary = {}

#Iterate for each and every item in the list
for item in input:
    result_tuple = item
    if result_tuple[0] in final_dictionary.keys():
        final_dictionary[result_tuple[0]].append(result_tuple[1]) #if exists then add current value to key
    else:
        final_dictionary[result_tuple[0]] = [result_tuple[1]] #if not then add new key and valur pair to dictionary.

#print the output of dictionary in sorted order
for key, value in final_dictionary.items():
    print(key, sorted(value))



