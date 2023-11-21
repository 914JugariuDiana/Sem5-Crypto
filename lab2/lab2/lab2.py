from math import perm
import random


def encrypt():
    print("Insert the message you want to encrypt:")
    text = input().replace(' ', '')
    if (len(text) < 3):
        print("text to short")
        return

    #choose a permutation size, randomly
    permutationLength = random.randrange(3, len(text))
    
    permutation = [i for i in range(0, permutationLength)]
    #go from 0 to permutation length - 1 and interchange the current value with the value from a random position, to create a permutation
    for i in range (0, permutationLength - 1):
        generated = random.randrange(0, permutationLength)
        aux = permutation[i]
        permutation[i] = permutation[generated]
        permutation[generated] = aux 

    #add x to the end to have complete permutations
    while (len(text) % permutationLength != 0):
        text += 'x'

    repetitions = 0
    newText = ''
    #create a new message, following the permutation
    while (repetitions < len(text) / permutationLength):
        for i in range(0, permutationLength):
            newText += text[permutation[i] + repetitions * permutationLength]
        repetitions += 1

    print("this is the permutation: ", permutation)
    print("this is the encrypted message: ", newText)
    print("this is the original message: ", text)

if __name__ == "__main__":
    while (True):
        print("Do you want to encrypt a messsage?\nYes(y)\nNo(n)")
        answer = input()

        if (answer == 'y'):
            encrypt()
        else:
            break
