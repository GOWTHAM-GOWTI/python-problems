def filter_list(l):
    retvalue = [ ]
    list1 = [ num for num in range(123)]
    for value in l:
        if value in list1:
            retvalue.append(value)
    return retvalue

list=[1,4,122,'123',0,'asc','a']
print(filter_list(list))

# BEST METHOD FROM CODEWARS
#def filter_list(l):
#  return [i for i in l if not isinstance(i, str)]


retvalue = []
    for val in l:
        if len(val)==4:
            retvalue.append(val)
    return retvalue