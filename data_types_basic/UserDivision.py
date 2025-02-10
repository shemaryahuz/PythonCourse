num=int(input("enter a two digits number:"))
units=num%10
tens=num//10
dividing=units+tens
print("Is the number divisible by the sum of its digits?:",(num%dividing==0))



