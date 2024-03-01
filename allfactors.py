def allfactors(n):
    factors = []
    for i in range(1,n+1):
      if (n%i) == 0:
        factors.append(i)
    return factors
number = int(input("please enter a number: "))
listfactors = allfactors(number)
print(listfactors)
        