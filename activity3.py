def test(lst):
    result={}
    for item in lst:
        result[item[0]]=item[1:]
        return result
    
students=[[1, 'Adhya' ,'V'],[2,'Bhoomi','V'],[3,'harsh','VI'],[5,'Kartik','VI']]

print("Orignal list of lists:")
print(students)
print("Converted lists to a dictionary:")
print(test(students))   