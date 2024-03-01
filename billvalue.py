y = int(input("subtotal"))
x = input("how was your service, please enter bad,okay,good, or great")
if (x) == "bad":
    print(y)
elif (x) == "okay":
    print(int(y) + y*0.15)
elif (x) == "good":
    print(int(y) + y*0.2)
else:
    print(int(y) + y*0.25)
