"""To'plamdagi elementlarning ko'paytmasini hisoblash. To'plamda raqamli elementlar
 bor, ularning ko'paytmasini hisoblash."""

numSet = {1, 2, 3, 4, 5, 6, 7, 8, 1, 3, 5}
multiplication = 1

for i in numSet:
    multiplication *= i
    
print(multiplication)    