# Wordle (Python CLI)

This project is a **command-line version of the popular Wordle game**, built entirely in Python.  
The goal is to guess a randomly chosen 5-letter word within 6 attempts.  
After each guess, the game provides feedback:  
- 🟩 Green → correct letter in the correct spot  
- 🟨 Yellow → correct letter but wrong spot  
- ⬜ Gray → letter not in the word  

The project helped me practice important programming concepts such as **file handling, randomization, dictionaries, loops, and conditional logic**.  

## How it works?

### Step 1:-

- Loading in the words from the txt file.
- Choosing only 5 lettered words converting all chosen into lower case.
- Choosing a random word. (word to be guessed)
- Returning the random word and a set of all words. (to maintain uniqueness)
- This helps in creating the word base and selecting the **secret** word

  ### Step 2:-

  - Creating and returning a **letter tracking** dictionary.
  - This helps in tracking the count of every letter in the **secret word**.
  - This is important as it *prevents* marking **extra yellows** when the guess has more copies of the letter than the secret word has.

  ### Step 3:-

  - This is the **core logic** of the game.
  - Here we first mark the letters - of the guess - which are in their **correct position** using green with respect to the secret word.
  - Upon marking those letters, we reduce their count too from the letter tracker.
  - Once this is completed, we move on to checking which letters exist in the secret word and are in the **incorrect position** and which letters **do not exist** at all.
  - We follow the same process as we did for green marking.
  - We then output the final feedback for the user to understand how accurate their guess is.
 
    ### Step 4:-

    - Here, we invoke all the above functions that we defined to run them in the correct order.
    - We also perform procedures like, checking whether guess is 5-lettered, checking whether guess is in the word base or not.
    - If user guesses right, they win the game.
    - If user is unable to guess the right word withing the 6 attempts, then they lose the game and can see the secret word.










