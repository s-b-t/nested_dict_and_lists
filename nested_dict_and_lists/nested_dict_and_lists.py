#1 Update values in dictionaries and lists:

#1 Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
#2 Change the last_name of the first student from 'Jordan' to 'Bryant'
#3 In the sports_directory, change 'Messi' to 'Andres'
#4 Change the value 20 in z to 30

x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1
x[1][0] = 15
print(x)

#2
students[0]['last_name'] = 'Bryant'
print(students[0])

#3
sports_directory['soccer'[0]] = 'Andres'
print(sports_directory['soccer'])

#4
z[0]['y'] = 30
print(z)


#2 Iterate Through a List of Dictionaries

# Create a function iterateDictionary(some_list) that, 
# given a list of dictionaries, the function loops through each dictionary 
# in the list and prints each key and the associated value. 
# For example, given the following list:

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterate_dictionary(some_list):
    for each_dict in some_list:
        str = ''
        for each_key in each_dict:
            str = str + each_key + ' - ' + each_dict[each_key] + ', '
        print(str)
iterate_dictionary(students)


#3 Get Values From a List of Dictionaries:

# Create a function iterateDictionary2(key_name, some_list) that, 
# given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. 
# For example, iterateDictionary2('first_name', students) should output:

def iterate_dictionary2(key_name, some_list):
    for each_dict in some_list:
        if key_name in each_dict:
            print(each_dict[key_name])
iterate_dictionary2('first_name', students)
iterate_dictionary2('last_name', students)


#4 Iterate Through a Dictionary with List Values:

# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key
# along with the size of its list, and then prints the associated values within each key's lists.

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(some_dict):
    for each_key in some_dict:
        print(f'{len(some_dict[each_key])} {each_key.upper()}')
        for each_item in some_dict[each_key]:
            print(each_item)

print_info(dojo)


