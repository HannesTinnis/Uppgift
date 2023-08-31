#1

"""
Det
Här 
Är
Modul
2
"""

#2

print ("addition:",5+10) #addition
print ("subtraktion:",5-10) #subtraktion
print ("multiplikation:",5*10) #multiplikation
print ("division:",5/10) #division
print ("potenser:",5 ** 10)#potenser

#3
name=input ("what is your name? ")
age = input ("how old are you? ")
color=input("what is your favorit color? ")
print ("you are " + age , "your name is " + name,"and your favorit color is " + color, ) #välkomstprogrammet 

#4
multiplikation1=int(input ("Multiply "))    #multiplikations räknare 
multiplikation2=int(input ("With "))
print (multiplikation1 * multiplikation2)

#5
multiplikation3=int(input ("your Weight ")) #Bmi kalkylator 
multiplikation4=int(input ("your Height "))
multiplikation4=multiplikation4/100
print ("din bmi är ", multiplikation3 / (multiplikation4 ** 2))

#6

år =int(input ("Hur gammal är du? ")) 
år = år * 52                                #Ålder i veckor 
print ("du är ungefär", år, "veckor gammal ")

#7

print("Dethär är ett program för att omvandla viktinheter kg till lbs eller lbs till kg")
unit=input ("vilken enhet vill du omvandla från? ")
if unit== "kg":
    kg=int(input("Skriv in din vikt i kg ")) #Enhets omvandlare i vikt (kg till lbs och lbs till kg)
    kg= kg * 2.2
    print(" din vikt är", kg,"i lbs")

if unit== "lbs":
    lbs=int(input("skriv in din vikt i lbs "))
    lbs= lbs / 2.2
    print("din vikt är", lbs,"i kg")




