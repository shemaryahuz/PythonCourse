ques=input("Do you hungry? (yes/no):")
if ques != "yes" and ques != "no":
    print("Please answer!")
    ques = input("Do you hungry? (yes/no):")
if ques == "yes" :
    ques = True
if ques == "no":
    ques = False
if ques:
    print("Prepare or order food!")
else:
    print("Take advantage of the time!")



