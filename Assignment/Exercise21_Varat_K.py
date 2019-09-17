from tkinter import *
import math

def description(x):
    if x >= 30:
        return "อ้วนไป"
    elif x >= 25:
        return "อ้วน"
    elif x >= 23:
        return "น้ำหนักเกิน"
    elif x >= 18.6:
        return "น้ำหนักปกติ เหมาะสม"
    else:
        return "ผอมเกินไป"

def leftClickButton(event):
    BMI = float(textBoxWeight.get())/math.pow(float(textBoxHeiht.get())/100,2)
    print(BMI)
    labelResult.configure(text=description(BMI))



MainWindow =Tk()
labelHeight = Label(MainWindow,text = "ส่วนสูง (cm)")
labelHeight.grid(row=0,column=0)

textBoxHeiht = Entry(MainWindow)
textBoxHeiht.grid(row=0,column=1)

labelWeight = Label(MainWindow,text = "น้ำหนัก (kg)")
labelWeight .grid(row=1,column=0)

textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)

calculateButton = Button(MainWindow,text = "คำนวณ")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2,column=0)

labelResult = Label(MainWindow,text = "ผลลัพธ์")
labelResult.grid(row=2,column=1)


MainWindow.mainloop()