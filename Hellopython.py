def information():
    print("""l - for moving left
r - for moving right
Any other letter for quitting""")
    
def move(færa, staða):
    if (staða == Vinsri_endi and færsla == "l") or (staða == Hægri_endi and færsla =="r"):
        return staða
    if færa == "r":
        staða += 1
    elif færa == "l":
        staða -= 1
    return staða

Vinsri_endi = 1
Hægri_endi = 10
staðsetning = int(input("Input a position between 1 and 10: "))
færsla = "r"

while færsla == "l" or færsla == "r":
    information()
    færsla = input("Input your choice: ")
    staðsetning = move(færsla, staðsetning)
    print("New position is:", staðsetning)
