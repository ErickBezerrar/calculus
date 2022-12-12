#Given function
def f(x):
   return 3*x**2
 #Implementing Simpson's 1/3 rule
def simpson(x0,xn,n):
   # step size
   h= (xn-x0)/n
   
   # finding sum
   S=f(x0)+f(xn)
   for i in range(1,n):
      k = x0 + i*h
      if i%2 == 0:
         S = S + 2 * f(k)
      else:
         S = S+4  * f(k)
   #Finding value
   S = S * h/3
   return S
   
a = float(input("Lower limit: "))   
b = float(input("Upper limit: "))   
n = int(input("number of sub intervals: "))    
result = simpson(a , b, n)   
print("Value is: %0.6f" % (result))
