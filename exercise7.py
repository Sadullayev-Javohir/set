"""Ikki to'plamning farqini (difference) hisoblash. Ikkita to'plam berilgan,
ularning farqini toping (ya'ni, birinchi to'plamda bor, lekin ikkinchi to'plamda
yo'q)."""

num1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
num2 = {1, 2, 4, 6, 13, 64, 12, 15}

difference = num1.difference(num2)

print(difference)