# -*- coding: utf-8 -*-
"""OsnoviPython.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VXYXIYWM7uRaSuumlbnDPaiE1V_JGsE8
"""

True + 4

text = 'hello'

print(text[4:100])

def square(x):
  return x**2

numbers = [1, 2, 3, 4]
something = list(map(lambda x: square(x), numbers))
print(something[3])

#file = open("out.txt", "w")
for i in range(5):
  print(str(i))
#file.close()

print("\n 8008135 \n")

#file = open("out.txt", "w")
for i in range(5, 10):
  file.write(str(i))
#file.close()

def almost_double_factorial(n):
  res = 1
  for i in range(n+1):
    if i%2 == 1:
      res *= i
  return res

almost_double_factorial(5)

items = [('one', 'two'), ('three', 'four'), ('five', 'six'), ('string', 'a')]
#dir(items)
sorted_items = sorted(items, key=lambda x: x[1][-1])
sorted_items

x = [1, 2, 3, 4, 5]

x[::-2] = [-1, -3, -5]

print(x)

#Напишите слайс вместо ###, чтобы на экран вывелось:

#[-5, 2, -3, 4, -1]

A = [5, 1, 4, 5, 14] 
#B = cumsum_and_erase(A, erase=10)
#assert B == [5, 6, 15, 29], "Something is wrong! Please try again"

def cumsum_and_erase(A, erase):
    C = []
    for i in range(1, len(A)+1):
      sum = 0
      for j in range(i):
        sum+=A[j]
      if(sum!=erase): C.append(sum)
    #C.remove(erase)
    return C
B = cumsum_and_erase(A, 10)
B

def process(sentences):
    result=[]
    for sentence in sentences:
        st=""
        for word in sentence.split():
            if word.isalpha():
                st+=word+" "
        s1=st[0:-1]  
        result.append(s1)     
    return result

class Neuron:

      def __init__(self, w, f = lambda x : x):
        self.w = w
        self.f = f
        self.x = list()
      
      def forward(self, x):
        self.x = x
        sum = 0
        for i in range(len(x)):
          sum+=self.w[i]*x[i]
        return self.f(sum)
    
      def backlog(self):
        #if(self.f != Null):
        #  return self.x
        #else:
        #  return None
        return self.x