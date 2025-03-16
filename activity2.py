my_dict={"Name":"John",1:[2,3,4]}
my_dict={"Name":"Priya","Age":"26"}

print( my_dict['Name'])
print(my_dict.get('age'))

my_dict['Age']=27
print(my_dict)

my_dict['address']= 'Downtown'
print(my_dict)

my_dict.pop('Age')
print(my_dict)

print("address :",my_dict.get('address'))

my_dict.clear()
print(my_dict)