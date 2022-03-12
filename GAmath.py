
import numpy as np
import random
#Define a function
##Variables
pop = 1000 #Initial Population
iterations = 1000 #Number of iterations
elite = 2 #Number of elite solutions to keep unchanged. 

#Function to solve
def fun(x,y,z):
    func = ((x**2)/2+y**2+z**2)**2-69
    return func

#Fitness function
def fitness(x,y,z):
    ans = fun(x,y,z)
    if ans == 0:    #Found correct solution 100% correct. Return a very high fitness value
        return 1000000
    else:           #Else return a value that is increasing the lower the result of the function is. we want 0
        return abs(1/ans)

#Generate initial population
solutions = []
for s in range(pop):   #
    solutions.append((
    random.uniform(0,pop),
    random.uniform(0,pop),
    random.uniform(0,pop),"First Generation"))


for i in range(iterations):
    rankedsolutions = []
    elitesolution = []
    for s in solutions: #Get fitness of the population
        rankedsolutions.append((fitness(s[0],s[1],s[2]),s))
    rankedsolutions.sort()  #Sort the list 
    rankedsolutions.reverse()   #Reverse the list to get highest number at the top aka best solution. 
    print(f"=== Gen {i} best solutions ===")
    print(rankedsolutions[0])
    #print("=== Found from ===")
    #print(rankedsolutions[0])
    elitesolution = rankedsolutions[0:elite]            #Keep the elite solutions unchanged for next population
    a = int(pop/10)
    bestsolutions = rankedsolutions[elite:elite+a]    #Generate population which is to be used for creating the new population
                                                        #We keep 10% of the population
    elementsX = []
    elementsY = []
    elementsZ = []
    elementsScore = []
    for e in bestsolutions:
        elementsX.append(e[1][0])   
        elementsY.append(e[1][1])
        elementsZ.append(e[1][2])
        elementsScore.append(e[0])
    newGen = []
    found = []
    text = ""
    for t in elitesolution:
        text = "Elite"
        newGen.append((t[1][0],t[1][1],t[1][2],text))
    #Do not remove/change/mutate the best solution from current generation
    for i in range(pop-len(elitesolution)):
        mutate = random.randint(0,100)
        b = random.randint(0,a-1)   #Generate random number between 0 and mate pop size
        score = elementsScore[b]    #Select the score of the randomly selected individual.
        #print(score)
        if mutate > 70: #Mutate 30% of the population. 
#            if score > 10:
            if score < 500.:
                e1 = random.choice(elementsX) * random.uniform(-1.5,1.5)    #
                e2 = random.choice(elementsY) * random.uniform(-1.5,1.5)    #
                e3 = random.choice(elementsZ) * random.uniform(-1.5,1.5)    #
                text = "Solution from heavy random mutation"
            elif score > 500. and score < 1000.:
                e1 = elementsX[b] * random.uniform(-1.5,1.5)    #
                e2 = elementsY[b] * random.uniform(-1.5,1.5)    #
                e3 = elementsZ[b] * random.uniform(-1.5,1.5)    #
                text = "Solution from heavy mutation"
            else: 
                e1 = elementsX[b] * random.uniform(0.8,1.2)    #
                e2 = elementsY[b] * random.uniform(0.8,1.2)    #clear
                e3 = elementsZ[b] * random.uniform(0.8,1.2)    #
                text = "Solution from low mutation"
        else:
            e1 = random.choice(elementsX)
            e2 = random.choice(elementsY)
            e3 = random.choice(elementsZ)
            text = "Solution from random"
        newGen.append((e1,e2,e3,text))
    solutions = newGen  #Assign new population to solutions and redo tests.
    print(len(newGen)) 
print("=== best solutions ===")
print(rankedsolutions[0])
