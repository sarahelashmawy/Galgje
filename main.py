import random
import re 

woorden = ["informatica","informatiekunde","spelletje","aardigheidje","scholier","fotografie","waardebepaling","specialiteit","verzekering","universiteit","heesterperk"]

raad = 1
kanzen = 5
gevonden = False
correct = False
amount = 0
vast = True

gekozen = []
veld = []


print("Welkom bij galgje! Het gaat erom dat je door de computer gekozen woord gaat raden. Maar pas op, je aantal levens zijn beperkt. Raad het woord voordat je levens op zijn!")

begin = input("Wil je beginnen? JA of NEE?\n")
while vast == True:
  veld.clear()
  gekozen.clear()
  woord = random.choice(woorden)
  
  #print (woord)
  lijstwoord = list(woord)
  if begin == "JA" or begin == "ja" or begin == "Ja":
    for x in range (len(lijstwoord)):
        veld.append("_")
  
  else:
    print("Bedankt voor het niet spelen ;)")
    break
    
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
    gekozen.sort() 
 
  # Alleen 1 letter invoeren
    if len(keuze) > 1:
      print("Je kan alleen 1 letter invoeren!")


  #Alleen letters, geen getallen  
    elif not re.match("^[a-z]*$", keuze):
     print("Er kunnen geen cijfers worden geraden, alleen letters. Probeer het opnieuw! ")

  #Letters in word   
    if gevonden == True:
        print(keuze + " komt voor in het woord\n")
        print("Je hebt de volgende letters gekozen:\n")
        print(gekozen)
    elif gevonden == False:
        print(keuze + " komt niet voor in het woord")
        print("Je hebt nog " + str(kanzen - raad) + " keren om het woord te raden.\n")
        print("Je hebt de volgende letters gekozen:\n")
        print(gekozen)

    if gevonden == False:
        raad += 1

    else:
        gevonden = False

    if lijstwoord == veld:
      print("Je hebt alle letters geraden! Gefeliciteerd!")
      break

    print(veld)

    print(100*"-")
  if raad > kanzen:
    print("Jammer. Je hebt het woord niet geraden.") 
    raad = 1      

  opnieuw = input("Wil je opnieuw spelen? JA of NEE?\n")

  if opnieuw == "NEE" or opnieuw == "nee" or opnieuw == "Nee":             
    print("Dankje wel voor het spelen")
    break