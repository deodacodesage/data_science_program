Y = ["table", "chair", "bed"]
x = input("Enter furniture: ")
while x in Y:
    print("furniture exist")
    break
else:
    Y.append(x)
    print(Y)
