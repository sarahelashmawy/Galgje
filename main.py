import random 

woorden = ["informatica","informatiekunde","spelletje","aardigheidje","scholier","fotografie","waardebepaling","specialiteit","verzekering","universiteit","heesterperk"]

woord = random.choice(woorden)


raad = 0
kanzen = 5
gevonden = False
correct = False
amount = 0
vast = True

gekozen = []
veld = []
lijstwoord = list(woord)

print("Welkom bij galgje! Het gaat erom dat je door de computer gekozen woord gaat raden. Maar pas op, je aantal levens zijn beperkt. Raad het woord voordat je levens op zijn!")

while vast == True:

  begin = input("Wil je beginnen?\n")
  if begin == "ja":
    for x in range (len(lijstwoord)):
        veld.append("_")

    while raad <= kanzen and lijstwoord != veld:
        keuze = input("Noem een letter:\n")

    #check for letter
        for z in range (len(lijstwoord)):
            if lijstwoord[z] == keuze:
                amount += 1
                
        for i in range (len(lijstwoord)):
            
            if lijstwoord[i] == keuze:
                veld[i] = keuze
                gevonden = True
                amount -= 1
                if amount == 0:
                    break            
            else:
                gevonden = False        
            
        gekozen.append(keuze)

    #Letters in word    
        if lijstwoord == veld:
            print("Je hebt alle letters geraden!")
            break

        if gevonden == True:
            print(keuze + " komt voor in het woord\n")
            print("Je hebt de volgende letters gekozen:\n")
            print(gekozen)
        elif gevonden == False:
            print(keuze + " komt niet voor in het woord\n")
            print("Je hebt de volgende letters gekozen:\n")
            print(gekozen)

        if gevonden == False:
            raad += 1

        else:
            gevonden = False

        print(veld)

        print(100*"-")

