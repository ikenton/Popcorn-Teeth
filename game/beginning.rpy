define h = Character("Hugo", color = "#FFFF00")
define p = Character("Pita")


label global_beginning:
    
    scene pt-cage-tent
    show pita happy
    "Oh, he’ll pay, they’ll all pay for what they’ve done to me!"
    "I slowly stand up on my two hooves and dust off some hay off of my dress."
    show pita disgusted
    "I need to get out of this tent, I can’t stand being in it anymore…"
    "I walk quietly, trying not to agitate the animals."
    "I approach the cage that has helped me dearly by providing me with that lone tooth. It was empty and had a stack of hay in it. I look at the words etched into the cage’s design and it says "
    "The Lizard Man."
    show pita sad
    "Oh, Lizard Man."
    "I’m so sorry for what happened to you…"
    "I do not wish to turn out like you…"
    "I look up and see the yellow dim light coming from outside. I approach it."
    hide pita sad
    scene pt-courtyard
    "This must be where they sleep. I wonder which one’s The Ringmaster’s?"
    jump global_courtyard
