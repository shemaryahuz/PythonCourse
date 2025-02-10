
coffee_ready = False
part1 = False
part2 = False
part3 = False
part4 = False

def boil_water():
    print("Boiling water.")
    global part1
    part1 = True

def brew_coffee():
    print("Making coffee.")
    global part2
    part2 = True

def add_sugar():
    print("Adding sugar.")
    global part3
    part3 = True

def serve_coffee():
    print("Serving the coffee.")
    global part4
    part4 = True

boil_water()
brew_coffee()
add_sugar()
serve_coffee()

if part1 and part2 and part3 and part4:
    coffee_ready = True

if coffee_ready:
    print("The coffee is ready!")
else:
    print("Something went wrong with the coffee.")

