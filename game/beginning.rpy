define rm = Character("Ringmaster", color = "#ff0000")
define p = Character("Pita", color = "#edf4b3")
image pullaway_slideshow:
    "ringmaster lean"
    pause 2.3
    "ringmaster pullaway"
    pause 1.0
label global_beginning:
    $ renpy.movie_cutscene("videos/pt-intro-cutscene.webm")
    $ persistent.pitaIntroDark_unlocked = True
    $ persistent.pitaIntroSpotlight_unlocked = True
    $ persistent.daysOne_unlocked = True
    $ persistent.daysTallymarks_unlocked = True
    show ringmaster lean 
    $ persistent.ringmasterLean_unlocked = True
    $ persistent.ringmasterChibi_unlocked = True
    $ persistent.ringmasterTaunt_unlocked = True
    $ persistent.ringmasterPoster_unlocked = True
    pause 1.0
    rm "..."
    rm "You did great today, Sweetheart. The crowd loved you like always."
    show ringmaster taunt
    rm "Continue to be my good girl and I’ll get you a treat at the end of this week."
    
    rm "You wouldn’t want to starve now would you?"
    "He lets out a gleeful chortle, the same one that I heard when he first caught me."
    "{i}This creep!{/i}"
    show pullaway_slideshow
    "He rubs one of his fingers against my knuckles and I immediately pull away."
    $ persistent.ringmasterPull_unlocked = True
    rm "Goodnight. See you tomorrow, Sweetheart."
    hide pullaway_slideshow
    show cage int
    $ persistent.cageInt_unlocked = True
    $ persistent.pitaInCage_unlocked = True
    #footsteps sound
    p "Finally he's gone."
    "Two hours passed as I waited until everyone left the tent."
    "Now it's time for my escape."
    "Aha! I got it. Finally!"
    show pita happy
    $ persistent.pitaHappy_unlocked = True
    $ persistent.pitaChibi_unlocked = True
    "I crawl out of the cage and crack my back. After tonight, I'm never going to perform again."
    "I look at the bone in the lock’s keyhole. I reach out and take it."
    "I immediately shove it in my mouth."
    show pita teeth
    $ persistent.pitaTeeth_unlocked = True
    "The sharp bone pierces the inside of my right cheek as I grind my teeth against it. I can taste the iron of my blood as I gulp it as if it were air. I lick my lips, not letting any ounce of blood escape my grasp."
    show pita disgusted
    $ persistent.pitaDisgust_unlocked = True
    "I am not satisfied."
    "I need more."
    "More than just a tiny bone! I need real food! A-and I want to go back home! Oh, but I can’t leave just yet, the Ringmaster must still have my wand…"
    show pita laugh
    $ persistent.pitaLaugh_unlocked = True
    "Oh, he’ll pay, they’ll all pay for what they’ve done to me!"
    "I slowly stand up on my two hooves and dust off some hay off of my dress."
    show pita disgusted
    "I need to get out of this tent, I can’t stand being in it anymore…"
    scene pt-cage-tent
    $ persistent.ptCageTent_unlocked = True
    show pita disgusted
    "I walk quietly, trying not to agitate the animals."
    "I approach the cage that has helped me dearly by providing me with that lone tooth. It was empty and had a stack of hay in it. I look at the words etched into the cage’s design and it says "
    "The Lizard Man."
    show pita sad
    $ persistent.pitaSad_unlocked = True
    "Oh, Lizard Man."
    "I’m so sorry for what happened to you…"
    "I do not wish to turn out like you…"
    "I look up and see the yellow dim light coming from outside. I approach it."
    hide pita sad
    scene pt-courtyard
    play channel1(  "audio/cricket-song.mp3") volume 0.09

    $ persistent.ptCourtyard_unlocked = True
    $ persistent.pitapita_unlocked = True
    "This must be where they sleep. I wonder which one’s The Ringmaster’s?"
    jump global_courtyard
