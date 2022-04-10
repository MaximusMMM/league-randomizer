import random
import time

styles = ["Tank", "Lethality", "Full AP", "Attack Speed", "Support"]

def generateChamp(champFile):
    with open(champFile) as f:
        contents = f.read()
    lines = contents.splitlines()
    line_number = random.randrange(0, len(lines))
    return lines[line_number]

def generateSynergies(tftFile):
    with open(tftFile) as f:
        contents = f.read()
    lines = contents.splitlines()
    line_number = random.randrange(0, len(lines))
    return lines[line_number]

def chooseStyle():
    choice = input("Would you like for me to choose a playstyle as well? y/n: ")
    if choice == "y":
        print("\n"+random.choice(styles))
        
def champs():
    print(generateChamp("LOLChamps.txt")+"\n")

def synergies():
    print("\n"+generateSynergies("tftSynergies.txt")+"\n")

def startMenu():
    proceed = int(input("What would you like to do?\n 1. Random Champion\n 2. Random TFT Synergy\n 3. Exit\n"))
    if proceed == 1:
        chooseStyle()
        champs()
        time.sleep(1)
    elif proceed == 2:
        synergies()
        time.sleep(1)
    elif proceed == 3:
        exit()
    else:
        print("Please choose one of the given options.")

    
if __name__ == '__main__':
    while True:
        startMenu()
