"""def ShortLong(a, b):
    return a+b+a if len(a)<len(b) else b+a+b

def elevator(left, right, call):
    return "left" if abs(call - left) < abs(call - right) else "right"
#
import math
def logs(x, a, b):
    result = math.log(a * b, x)
    return result



def monkey_count(n):
    return [i for i in range(1,n+1)]        



#[1, 2, 3, 4, 5, 6], 2 --> [2, 4, 6]   
a=[1, 2, 3, 4, 5, 6]
b=2
l=[]
for i in a:
    if i==b:
        for j in range(i-1,len(a),b):
            l.append(a[j])
print(l)  


def divisible_by(numbers, divisor):
    result = []
    for number in numbers:
        if number % divisor == 0:
            result.append(number)
    return result
print(divisible_by([1, 2, 3, 4, 5, 6], 2))




def between(a,b):
    return list(range(a,b+1))




def format_money(amount):
    return '${:.2f}'.format(amount)




def ice_brick_volume(radius, bottle_length, rim_length):
    return (bottle_length - rim_length) * 2 * radius ** 2        




def stringy(size):
    s=""
    for i in range(size):
        if i%2==0:
            s+="1"
        else:
            s+="0"
    return s        
   


def lowercase_count(strng):
    c=0
    for i in strng:
        if i.islower():
            c+=1
    return c     
"""
"""

def draw_stairs(n):
    stairs = ""
    for i in range(n):
        stairs += " " * i + "I\n"
    return stairs.rstrip()
print(draw_stairs(5))
"""

"""
q=""
print(len(q))
for i in range(5):
    q+="\t"
print(len(q))    """




"""l1 = []
result=[]
for i in lists:
    for j in i.values():
        l1.append(j)

for i in l1:
    for j in lists:
        for key,value in j.items():
            if l1.count(i)==2 and value==i:
                result.append(key)
result1=set(result)
print(sorted(list(result1)))   """ 




# mavzu: lists,dict,set larga doir masala (EASY😂)
def Dict_Values_Dublicate_Print_Sort_Keys(n):
    l1 = []
    result=[]
    for i in n:
        for j in i.values():
            l1.append(j)
    for i in l1:
        for j in lists:
            for key,value in j.items():
                if l1.count(i)==2 and value==i:
                    result.append(key)
    result1=set(result)
    return sorted(result1)
lists=[{"ali":20},{"toms":55},{"john":20},{"sardor":11},{"bobir":55}]
print(Dict_Values_Dublicate_Print_Sort_Keys(lists))


                








