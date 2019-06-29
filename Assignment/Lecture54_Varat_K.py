def login():
    usernameInput = input("Username :")
    passwordInput = input("Password :")
    if usernameInput == "admin" and passwordInput == "1234":
        showMenu()
    else:
        print("Wrong Username or Password")


def showMenu():
    print("----ishop----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    menuSelect()
def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        print("Price including vat: ", vatCalculate(int(input("Price: "))), "Baht")
    elif userSelected == 2:
        print("Total Price including vat: ", priceCalculate(), "Baht")
def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result
def priceCalculate():
    price1 = int(input("First Product Price: "))
    price2 = int(input("Second Product Price: "))
    return vatCalculate(price1 + price2)


login()