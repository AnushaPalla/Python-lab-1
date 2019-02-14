# program to find the longest string and length

length = input("enter the string to be checked ")
longest = ""
longest_final = ""

# for loop to check each and every character in set
for i in range(0, len(length)):

    check = length[i]  # to check if character already exists

    if check in longest:  # if it exists then empty it
        longest = ""

    longest = longest + check  # if does not exist then add it

    if len(longest) > len(longest_final):  # check the length of current string and previous string
        longest_final = longest
print("Longest substring is:", longest_final)
print("Length of the longest substring is: ", len(longest_final))  # print the longest string and length
