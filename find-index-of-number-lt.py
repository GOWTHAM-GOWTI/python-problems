#find the index of given int in list if the given value not in the list then display index where it would be.
class Solution():
    def ret(self, list1,num):
        if num in list1:
            return list1.index(num)
        elif num not in list1:
            for val in list1:
                if num < val:
                    index1= list1.index(val)
                    list1.insert(index1,num)
                    return list1.index(num)
            list1.append(num)
            return list1.index(num)
list1=[1,2,4,5]
num=32
sortd= sorted(list1)
sol=Solution()
sol=sol.ret(list1,num)
print(sol)