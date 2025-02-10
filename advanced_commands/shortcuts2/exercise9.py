
height = int(input("בחר את גובה הפירמידה: "))
space = " "
keystroke = "*"
[print(space * (height - i) + (keystroke + space) * (i + 1)) for i in range(height)]


