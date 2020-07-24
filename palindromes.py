"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
total = 0

for number in range(0,1000000):
    numText = str(number)
    numRev = numText[::-1]
    if numText == numRev:
        dec = bin(number)
        dec = dec[2:]
        decReverse = dec[::-1]
        if decReverse == dec:
            total += number
            
print(total)
