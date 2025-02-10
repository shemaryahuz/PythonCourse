num=int(input("Enter a 7 digits number:"))
first=num%10
second=num//10%10
third=num//100%10
fourth=num//1000%10
fifth=num//10000%10
sixth=num//100000%10
last=num//1000000
print(last,sixth,fifth,fourth,third,second,first)
print('Is the first digit equal to the last one?',first==last)
print('Is the second digit not equal to the sixth?',second!=sixth)
print('Is the third digit equal to the last one and not equal to the fifth?',third==fourth and third!=fifth)