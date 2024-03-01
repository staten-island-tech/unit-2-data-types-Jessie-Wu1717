def gcf(x,y):
    great = []
    for i in range(1,min(x,y)+1) :
        if x%i == 0 and y%i == 0:
          great.append(i)
    return max(great)
a = int(input("enter first number"))
b = int(input("enter second number"))
g = gcf(a,b)
print(g)
