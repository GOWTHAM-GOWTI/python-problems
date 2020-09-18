def middlename(name):
    if len(name) % 2 == 0:
        ret = len(name)/2 
        return name[int(ret-1)] + name[int(ret)]
    elif len(name) % 2 ==1:
        return name[int(len(name)/2 )]


list = 'gowtham'
print(middlename(list)) 


# BEST FROM CODEWARS
#        |
#def get_middle(s):
# return s[(len(s)-1)/2:len(s)/2+1]