""""
โจทย์ 1 : เครื่องคำนวนอย่างปลอดภัยเขียนโปรแกรมรับตัวเลข 2 จำนวนและตัวดำเนินการ 1 ตัว ได้แก่ + - * / แล้วแสดงผลลัพธ์
โปรแกรมต้องจัดการกรณีต่อไปนี้
ผู้ใช้กรอกข้อมูลที่ไม่ใช่ตัวเลข #ValueError
ผู้ใช้เลือกตัวดำเนินการอื่นนอกเหนือจาก + - * / raise Value Error
ผู้ใช้พยายามหารด้วยศูนย์ #ZeroDivisionError
โปรแกรมต้องแสดง จบการทำงาน เสมอด้วย finally
ตัวอย่างผลลัพธ์ที่คาดหวัง
ตัวเลขที 1: 10
ตัวเลขที่ 2 : 0
เครื่องหมาย (+,-,*,/): /
ไม่สามารถหารด้วยศุูนย์ได้
c
จบการทำงาน
"""
try:
    #input 3 ตัว
    number1 = float(input("ตัวเลขที่ 1: "))
    number2 = float(input("ตัวเลขที่ 2: "))
    operator = input("เครื่องหมาย(+,-,*,/): ")

    result = 0
    if operator == "+":
        result = number1 + number2
    elif operator == "-":
        result = number1 - number2
    elif operator == "*":
        result = number1 * number2
    elif operator == "/":
        result = number1 / number2
    else:
        raise ValueError("รับเฉพาะ + - * / เท่านั้น")

    print(f"{number1} {operator} {number2} = {result}")
except ValueError:
    print("ต้องเป็นตัวเลขเท่านั้น")
except ZeroDivisionError:
    print("ไม่สามารถหารด้วยศูนย์ได้")
finally:
    print("จบการทำงาน")