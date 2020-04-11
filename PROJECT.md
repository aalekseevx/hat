# Description

First of all, join to this [website](https://hat.alekseev.tk)

Have 2 options: create new room or join some existing room due to its universal name. Then one of online members choose the number of words, its difficulty, 
difficulty dispersion and time for round. After that, press "Start" to begin. The game happens in a circular mode. Assume that we have N players. 
In first round player 1 explains words to player 2, in second round player 2 explains words to player 3, ..., in  N-th round player N explains words to player 1. 
Of course, we assume that all players have audio connection. The game ends when the word list ends.
When player X tries to guess the word, which is explained by player Y there are 3 possible cases:

- player X guesses the word. Then player Y explain him another word, if start word list is not empty, both of X and Y obtain 1 point.
- player X gives wrong answer. Then player Y explain him another word, if start word list is not empty, X obtain -1 point.
- player X gives up. Then round ends instantly, until the end time.

In the end of the game final scoreboard appears. Here you can find all imnformation about final points, guesses, explanations and mistakes. 

