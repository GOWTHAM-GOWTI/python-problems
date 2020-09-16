def filter_list(l):
    #return [value for value in l if isinstance(value, len(4))] -->my try
    retvalue = []
    for val in l:
        if len(val)==4:
            retvalue.append(val)
    return retvalue

list=['goti','gow','gowtham','jack']
print(filter_list(list))

# BEST  FROM CODEWARS
#return [value for value in l if len(value)==4]