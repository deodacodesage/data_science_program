listy = ["table", "chair", "bed"]
response = ""
while response != "end":
    response = input("Enter item: ")
    if response in listy:
         print("furniture exist", listy)
    else:
         listy.append(response)
         print(listy)