define rm = Character("Ringmaster", color = "#F00040")
define p = Character("Pita")


label global_beginning:
    play sound  "cricket-song.mp3" fadein 1.0 volume 0.09
    show ringmaster lean
    rm "..."
    rm "You did great today, Sweetheart. The crowd loved you like always."
    rm "Continue to be my good girl and I’ll get you a treat at the end of this week."
    rm "Goodnight"
    "He rubs one of his fingers against my knuckles and immediately pull away."
    hide ringmaster lean
    show cage int
    rm "See you tomorrow."
    #footsteps sound
    p "Finally he's gone"
    "I wait until I felt everyone leave the tent. Now it's time for my escape."
    "Aha! I got it. Finally!"
    show pita happy
    
    "I crawl out of the cage and crack my back. After tonight, I'm never going to perform again."
    "I look at the bone in the lock’s keyhole. I reach out and take it."
    "I immediately shove it in my mouth."
    "The sharp bone pierces the inside of my right cheek as I grind my teeth against it. I can taste the iron of my blood as I gulp it as if it were air. I lick my lips, not letting any ounce of blood escape my grasp."
    "I am not satisfied."
    "I need more."
    "More than just a tiny bone! I need real food! A-and I want to go back home! Oh, but I can’t leave just yet, the Ringmaster must still have my wand…"
    
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
