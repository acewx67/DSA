A = {
    "quantity" : 0
}
print(A.quantity)

quantity_A = input("enter the quantity of Product_A\n")
if quantity_A == "":
    quantity_A = 0
else:
    quantity_A = int(quantity_A)
gift_A = ""
if quantity_A > 0:
    gift_A = (input('do you want product_A to be gift wrapped?enter "yes" or "no"\n'))

quantity_B = input("enter the quantity of Product_B\n")
if quantity_B == "":
    quantity_B = 0
else:
    quantity_B = int(quantity_B)
gift_B = ""
if quantity_B > 0:gift_B = (input('do you want product_B to be gift wrapped?enter "yes" or "no"\n'))

quantity_C = input("enter the quantity of Product_C\n")
if quantity_C == "":
    quantity_C = 0
else:
    quantity_C = int(quantity_C)
gift_C = ""
if quantity_C>0:gift_C = (input('do you want product_C to be gift wrapped?enter "yes" or "no"\n'))

total_A, total_B, total_C = 0.0, 0.0, 0.0

if gift_A.lower() == "yes":
    total_A = (quantity_A * 20) + quantity_A
else:
    total_A = quantity_A * 20

if gift_B.lower() == "yes":
    total_B = (quantity_B * 40) + quantity_B
else:
    total_B = quantity_B * 40

if gift_C.lower() == "yes":
    total_C = (quantity_C * 50) + quantity_C
else:
    total_C = quantity_C * 50

print(total_A,total_B,total_C)

subtotal = total_A+total_B+total_C

#Discount Rules:
temp = [0,0,0,0]
if subtotal > 200:
    temp[0] = (subtotal-10)
if quantity_A > 10:
    temp[1] = subtotal - total_A
    temp[1] = temp[1] + total_A*0.95
print(temp)