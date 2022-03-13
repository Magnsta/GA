
"""
(C) 2022: Magnus Stava <magnsta@stud.ntnu.no>
First introduction to GA. Developed simple GA that guesses
a word.  
"""
import numpy as np
import random
import string

"""
Customizable variables.
Words is a list of words, word randomly pick one of these. 
Add any word as preferred
"""
words = ["Variables","Nice","Initial","Population",
"Wrong","Length","Solver","Following",
"Okey","Correct","Width","Function",
"Love","Generator","Words","Python",
"Solutions","Hate","Untitled","History"
,"Interdisciplinary","Inconsequential",
"Hypothetically","Incomprehensibilities"
,"SOurhsKD","TeHSdnsoRUSjdS","pneumonoultramicroscopicsilicovolcanoconiosis"]

word = random.choice(words)
#word = "The Python installers for the Windows platform usually include the entire"

"""
pop - Initilize population 
iterations - Number of iterations. If no solution is found, repeat from 0
elite - Number of solution to keep untouched
globalMutation - Decides how often a mutation occurs. Number between 0 and 100.  
Changing the values affect the running time. 
"""
pop = 200           
iterations = 100        
elite = 5
mutationRate = 2  #

"""If true, generate new population Asexually, if false use random crossover selection"""
Asexual = False

def textfun(text):
    """Points are given by the following rules.
    Wrong length on word: -10 points

    Correct position and letter: 4 points
    Wrong position but correct letter: 1 point
    Neighbour position and correct letter: 1.5 point
    Wrong position and wrong letter: -2 points. 
    """
    score = 0.0
    if text[0] == word:
        return 90000
    if len(text[0]) == len(word): 
        for i in range(len(text[0])):
            if text[0][i] == word[i]:
                score += 4
            elif i != len(text[0])-1:
                if text[0][i+1] == word[i]:
                    score +=1.75
            elif text[0][i-1] == word[i]:
                score +=1.75
            elif text[0][i] in word:
                score += 1
            else:
                score -=2
    else:
        score -=10
    return score

def textFitness(text):
    """
    Fitness function. 
    Take value from textfun() and multiply by 10. 
    Higher value --> Higher performing word. 
    If the word is matching set a artificial high value
    """
    ans = textfun(text)
    if ans == 900000:       
        return 900000
    else:
        return ans*10.      

"""
Generate initial population with 
individuals containing a random combination of letters. 
For simplicity limit words between 2 and 15 in length.

solutions - List containing the initial population
wordSize - Decides size of individuals
individuals - Combination of letters, all individuals makes up the population. 
"""
population = []
wordSize = len(word)
for s in range(pop):
    individials = ""
    for i in range(wordSize):
        individials += random.choice(string.printable)
    population.append(((individials),"First generation"))

"""
Continue searching for word until found. 
When found loop is broken and code terminated. 
"""
notFound = True
msg = ""
rounds = -1
mut = 0
bestScore = []
while notFound:
    
    for i in range(iterations):
        rankedPopulation = []
        for s in population: 
            fitnessscore = textFitness(s)
            rankedPopulation.append((fitnessscore,s))
        """
        After grabbing fitness value, sort the list and reverse
        to get highest fitness value on the top
        """
        rankedPopulation.sort()  
        rankedPopulation.reverse()   
        """
        Uncomment to get the best current solution for each iteration
        """
        print(f"=== Gen {i} best solutions ===")
        print(rankedPopulation[0])
        iter = i
        msg = (f"Generation {i} ===")                          #Used only for presenting which geenration solution was found

        """
        Keep the elitesolutions unchanged. 
        Generate the new population based on the top 10 percent individuals
        Add the new generation in list newGen. 
        """      
        top25Percent = int(pop*0.25)
        bestsolutions = rankedPopulation[0:top25Percent]  
        
        """
        matingPool - List of population without the fitness score. Used for mating.
        newPopulation - After generating new individual, append to newPopulation. 
        """
        matingPool = []
        newPopulation = [] 
        idx = 0
        for e in bestsolutions:
            if idx <= elite:
                text = "Elite"
                newPopulation.append((e[1][0],text))                
            matingPool.append(e[1][0])
            idx += 1
        """
        Variable description: 
        
        mutate          - random number between 0 and 100, decides if mutation occurs or not
        individual      - Individual from mating pool
        newIndividual   - Generated child from individual
        """
        plussminus = [-1,1]
        if Asexual:
            for i in range(pop-elite):
                IndividualA = matingPool[random.randint(0,len(matingPool)-1)]    #Select a random element from the mating pool. Using Asexual mating    
                newIndividual = ""
                for j in range(len(IndividualA)):
                    mutate = random.randint(0,100)
                    if mutate < mutationRate:
                        newIndividual += random.choice(string.printable)
                        texts = "Heavy random mutation"
                    elif mutate >51:
                        newIndividual += IndividualA[j] 
                        texts = "Not mutation"                   
                    else:
                        newIndividual += IndividualA[j] 
                        texts = "Not mutation"                   
                newPopulation.append((newIndividual,texts))
        else:
            for i in range(pop-elite):
                IndividualA = matingPool[random.randint(0,len(matingPool)-1)]    #Select a random parent from the mating pool. Using Asexual mating
                IndividualB = matingPool[random.randint(0,len(matingPool)-1)]    #Select another random parent from the mating pool. 
                newIndividual = ""
                for j in range(len(IndividualA)):
                    mutate = random.randint(0,100)
                    if mutate < mutationRate:
                        newIndividual += random.choice(string.printable)
                        texts = "Heavy random mutation"
                    elif mutate >51:
                        newIndividual += IndividualB[j] 
                        texts = "Not mutation"                   
                    else:
                        newIndividual += IndividualA[j] 
                        texts = "Not mutation"                   
                newPopulation.append((newIndividual,texts))

        """Assign the new population to the solutions list"""
        population = newPopulation  
        """
        If solution is found terminate
        """
        if(rankedPopulation[0][0]==900000):
            notFound = False
            break
    bestScore.append(rankedPopulation[0][0])
    if rounds >= -1:
        scores = (rankedPopulation[0][0])/10
        maxScore = len(rankedPopulation[0][1][0])*4
        accuracy = (scores/(maxScore))*100
        print("\nIteration %s"%(rounds+1))
        print("Looking for: "+word)
        print("Current best solution:")
        print(rankedPopulation[0])
        print("Accuracy %s"%accuracy+"%")
    if mut > 2:                                         #If no improvements for 2 iterations, decrease mutation rate. 
        if bestScore[rounds] == bestScore[rounds-2]:
            print("\nDecrease mutation rate to:")
            mutationRate -= 1
            print("%s"%mutationRate+"%")
            mut = 0
            if mutationRate < 1:
                mutationRate = 1
    rounds +=1
    mut += 1

"""Print the final word and generations used to find this word"""

accuracy = 100
totGen = iter+(rounds)*iterations
print("\nComplete")
print("Looking for: "+word)
print("Found      : %s"%rankedPopulation[0][1][0])
print("Generation : %s"%totGen)
print("Accuracy %s"%accuracy+"%")