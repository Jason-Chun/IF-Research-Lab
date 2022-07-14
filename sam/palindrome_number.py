def pal(num):
  number_of_digits = length2(num)
  for i in range(number_of_digits//2):
    j = num//(10**i) % 10
    k = num//10**(number_of_digits-1-i) % 10

    if j != k:
      return False
  return True

def length(num):
  a = 10
  b = 1
  while True:
    if num//a != 0:
      a *= 10
      b += 1
    else:
      break
  return b

def length2(num):
  b=0
  while num>0:
    num=num//10
    b+=1
  return b


def reverse_digits(num):
  number_of_digits = length2(num)
  result = 0
  for i in range(number_of_digits):
    k = num//10**(number_of_digits-1-i) % 10
    result += k*10**i
  return result

def reverse_digits2(num):
  result = 0
  while num > 0:
    last = num % 10
    num = num // 10
    result = result * 10 + last
  return result
    
    
#1234
#result = ((4 * 10 + 3) * 10  + 2 ) * 10 + 1

var1 = 234612353457
print(reverse_digits(var1))
print(reverse_digits2(var1))
print(var1)
print("-"*50)
  
print(reverse_digits2(1234))
print(reverse_digits(1234))
print(pal(123456)) # --> False
print(pal(123321)) # --> True
print(pal(10000000001)) # --> True
#v//10%10]


# 12345
# var = 1 + 2*10 + 3 * 10**2 + 4 * 10**3 + 5 * 10**4
