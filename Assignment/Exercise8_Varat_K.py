usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "Pun" and passwordInput == "1234":
    print(" Hello Welcome")
    print("----Ari Fruit Shop----")
    print("Apple     10 THB")
    print("Banana     9 THB")
    print("Orange    15 THB")
    orderSelected = input("Order : ")
    if orderSelected == "Apple" :
        quantityInput = int(input("Quantity : "))
        result = quantityInput * 10
        print("Total :", result, "THB")
    elif orderSelected == "Banana" :
        quantityInput = int(input("Quantity : "))
        result = quantityInput * 9
        print("Total :", result, "THB")
    elif orderSelected == "Orange" :
        quantityInput = int(input("Quantity : "))
        result = quantityInput * 15
        print("Total: ", result, "THB")
else :
    print("Sorry, Invalid Username or Password")