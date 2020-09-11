def liked(names):
    retval =''
    
    if len(names) == 0:
        retval = "No one likes this"
    elif len(names) == 1:
        retval = retval +'"'+names[0] +' liked' + '"'
    elif len(names) ==2 :
        retval=retval +'"'+ list[0]+ ' and ' + list[1] + ' likes this'+'"'
    elif len(names) == 3:
        for name in range(0, len(names)-1):
            retval = retval + names[name] + ', '
        retval = retval[:-2]
        retval=retval +'"'+retval + ' and ' + list[2] + ' likesss this' + '"'
        #list is a keyword to get a value in a names list
    else:
        for name in range(0, 2):
            retval= retval + names[name] + ','
            retval = retval[:5]
        retval=retval + '"' + retval + " and " + str(len(list)-2)+ " others likes" +'"'
    
    return retval
list =['ab']
liked=liked(list)
print(liked)