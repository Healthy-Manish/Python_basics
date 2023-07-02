my_dict  = {"name": "Max","age": "27","city":"New york"}
print(my_dict)

my_dict2 = dict(name ="Marry",age=24,city="Melbourne")#dictionary by dict function
print(my_dict2)

my_dict["email"] = "manish@gmail.com"
print(my_dict)# adding key in dictionary

del my_dict["name"]#deleting key in dicitonary
print(my_dict)
my_dict.pop("age")
print(my_dict)

if"name"in my_dict:
    print(my_dict["name"])

for key in my_dict2:
    print(key)

for value in my_dict2.values():
    print(value)

for key, value in my_dict2.items():
    print(key, value)

# my_dict_cpy = my_dict2#if we apply this operator for copying then changes will be made in both instead of copied one
my_dict_cpy = my_dict2.copy()
my_dict_cpy["email"] = "xyz@gmail.com"
print(my_dict2)
print(my_dict_cpy)

  