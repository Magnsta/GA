
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
"Solutions","Hate","Untitled","History"]

word = random.choice(words)

"""
pop - Initilize population 
iterations - Number of iterations. If no solution is found, repeat from 0
elite - Number of solution to keep untouched
mutateVariable - Decides how often a mutation occurs. 
Changing the values affect the running time. 

"""
pop = 1000              
iterations = 100        
elite = 5

"""Awardeds are given by the following order.
Wrong length on word: -10 points

Correct position and letter: 4 points
Wrong position but correct letter: 1 point
Neighbour position and correct letter: 1.5 point
Wrong position and wrong letter: -2 points. 
"""
def textfun(text):
    score = 0.0
    if text[0] == word:
        return 90000
    if len(text[0]) == len(word): 
        for i in range(len(text[0])):
            if text[0][i] == word[i]:
                score += 4
            elif i != len(text[0])-1:
                if text[0][i+1] == word[i]:
                    score +=1.5
            elif text[0][i-1] == word[i]:
                score +=1.5
            elif text[0][i] in word:
                score += 1
            else:
                score -=2
    else:
        score -=10
    return score

"""
Fitness function. 
Take value from textfun() and multiply by 10. 
Higher value --> Higher performing word. 
If the word is matching set a artificial high value
"""
def textFitness(text):
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
for s in range(pop):
    wordSize = random.randint(2,15) 
    individials = ""
    for i in range(wordSize):
        individials += random.choice(string.ascii_letters)
    population.append(((individials),"First generation"))

"""
Continue searching for word until found. 
When found loop is broken and code terminated. 
"""
notFound = True
msg = ""
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
        #print(f"=== Gen {i} best solutions ===")
        #print(rankedPopulation[0])
        msg = (f"=== Gen {i}")                          #Used only for presenting which geenration solution was found

        """
        Keep the elitesolutions unchanged. 
        Generate the new population based on the top 10 percent individuals
        Add the new generation in list newGen. 
        """      
        top10Percent = int(pop/10)
        bestsolutions = rankedPopulation[0:top10Percent]  
        
        """
        matingPool - List of population without the fitness score. Used for mating.
        newPopulation - After generating new individual, append to newPopulation. 
        """
        matingPool = []
        newPopulation = [] 
        idx = 0
        for e in bestsolutions:
            if idx <= 4:
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
        for i in range(pop-elite):
            mutate = random.randint(0,100)
            Individual = matingPool[random.randint(0,len(matingPool)-1)]    #Select a random element of the besYt performing individual.
            newIndividual = ""
            for j in range(len(Individual)):
                mutate = random.randint(0,100)
                if mutate > 80: 
                    newIndividual += random.choice(matingPool[random.randint(0,len(matingPool)-1)])
                    texts = "Heavy local mutation"
                elif mutate < 5:
                    newIndividual += random.choice(string.ascii_letters)
                    texts = "Heavy random mutation"
                else:
                    newIndividual += Individual[j] 
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

"""Print the final word and generations used to find this word"""
print("\n")
print(f"=== Correct word found in {msg} ===")
print(rankedPopulation[0])
