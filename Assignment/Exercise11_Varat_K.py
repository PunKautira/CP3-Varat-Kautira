number = int(input())
for x in range(number):
        print(" "*(number-(x+1)), "*"*(x*2+1) )




number = int(input())
for x in range(number):
    text = ""
    for y in range(2*x+1):
        text += "*"
    print(" "*(number-(x+1)), text)


number = int(input())

[print(" "*(number-(x+1)), "*"*(x*2+1) ) for x in range(number)]