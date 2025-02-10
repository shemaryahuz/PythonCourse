num=683
units=num%10
hundreds=num//100
tens=(num//10)%10
result=tens-(hundreds+units)
print(result)