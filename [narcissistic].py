def nar(given):
    b= given
    given=list(map(int,str(given[0]))) #coverting a whole integer into single integers
    result=[]
    if len(given) <= 10:
        for value in given:
            a = 1  
            for i in range(0,len(given)):
                gg = a * value  #muliplying with a(1)
                a= gg
            result.append(a)
    result= sum(result)
    last = [ ]  #converting a int to list, so we can compare with list value b
    last.append(result)
    if str(last) == str(b):
        return f' {True}, {str(b)} is narcissistic '
    else:
        return f' {False}, {b} is not narcissistic '
need_result = [7]
print(nar(need_result))