
mission_complete = False
part1 = False
part2 = False
part3 = False



def drive():
    print("The paramedic is riding in an ambulance to save someone.")
    global part1
    part1 = True

def save_people():
    print("The paramedic is saving people.")
    global part2
    part2 = True


def return_to_base():
    print("The paramedic is returning to the base.")
    global part3
    part3 = True

drive()
save_people()
return_to_base()

if part1 and part2 and part3:
    mission_complete = True

if mission_complete:
    print("The mission was completed successfully!")

else:
    print("The mission was failed")