def ShortLong(a, b):
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