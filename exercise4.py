"""To'plamni birlashtirish. Ikki yoki undan ortiq to'plamni birlashtirib, yangi 
to'plam yarating."""

num1 = {1, 2, 3, 4, 5, 6, 12, 2, 5}
num2  = {12, 23, 14, 2, 5, 6, 1, 14}

num1.update(num2)

print(num1)