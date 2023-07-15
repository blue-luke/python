As a marketeer
So that I can enjoy myself away from the daily grind
I would like to be able to play rock/paper/scissors


This was implemented with a lazy TDD approach - I jumped ahead once I realised the emergent structure

There are 9 game combinations and only 5 are accounted for (see the elif statmements). Implementing the other 4 is academic but I also don't like the elif structure. 

You can currently call result() before play_hand() has been called for each player. We need a catch function at the start of result()



Another option would be to have a dictionary of whether the hand beats the other hands. Eg, rock[scissors] == True

rock = { scissors: True, paper: False }
paper = { rock: True, scissors: False }
scissors = { paper: True, rock: False }

This would be scaleable to more than 3 hands. You could initialise the game with the number of hands and an explanation of what beats what. However, you would need a completeness/consistency checker to make sure that that information was correct. I suspect this is a complex algorithm (to scale to arbitrary values of n), which is beyond the scope of this exercise