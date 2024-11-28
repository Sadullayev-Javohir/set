"""To'plamdagi eng katta va eng kichik elementni topish. To'plamdagi maksimal va
 minimal qiymatlarni aniqlang."""

numSet = {1, 2, 3, 4, 5, 6, 7, 8, 9}

maxNum = 0
minNum = 9

for i in numSet:
    if maxNum < i:
        maxNum = i
    if minNum > i:
        minNum = i

print(f"Katta: {maxNum}\t Kichik {minNum}")