#!/usr/bin/env python
# coding: utf-8

# In[37]:


import random
from colorama import Fore, Style, init
init(autoreset=True)


# In[38]:


def load_words():
    with open('sgb-words.txt','r') as f:
        words = f.read().splitlines()
        secret = random.choice(words).lower()
        words_set = set(w.lower() for w in words if len(w)==5)
    return secret, words_set


# In[39]:


def letter_tracker(secret):
    letter_dict={}
    for letter in secret:
        if letter not in letter_dict.keys():
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1
    return letter_dict


# In[40]:


def show_output(secret,guess):
    letter_dict = letter_tracker(secret)

    output = [""]*5
    for i in range(5):
        if guess[i]==secret[i]:
            output[i] = Fore.GREEN + guess[i].upper() + Style.RESET_ALL
            letter_dict[guess[i]]-=1

    for i in range(5):
        if output[i] != "":
            continue
        if (guess[i] in secret) and (letter_dict[guess[i]]>0):
            output[i] = Fore.YELLOW + guess[i].upper() + Style.RESET_ALL
            letter_dict[guess[i]]-=1
        else:
            output[i] = Fore.LIGHTBLACK_EX + guess[i].upper() + Style.RESET_ALL

    print(" ".join(output))


# In[41]:


def main():
    secret,words_set = load_words()
    attempts = 6

    while attempts>0:
        guess = input("Enter guess: ").lower()

        if len(guess)!=5:
            print("Guess must be 5 letters")
            continue
        if guess not in words_set:
            print("Word not in list")
            continue

        if guess == secret:
            print(Fore.GREEN + "Correct Guess!!" + Style.RESET_ALL)
            return 

        show_output(secret,guess)
        attempts-=1
        print(f"Attempts Left: {attempts}")

    print("Game Over!")
    print(f"Secret Word: {secret.upper()}")


# In[ ]:


if __name__ == "__main__":
    main()

