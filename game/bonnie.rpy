
define b = Character("Bonnie", color = "#9966cc")
define p = Character("Pita")
default bad = 0
#timer
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve 
    #This is the timer bar.
label global_bonnie:
    $ timer_range = 0
    $ timer_jump = 0
    
    "I take a deep breath, steeling my nerves before hurrying over to {b}her{/b} trailer."
    "The outside a faded pink, 2 large windows sat on one side, painted green and decorated with a pattern of daisies that lined the rim."
    "Stepping up to her door I turn the handle, the door clicking as I push it open. The inside is dim, lit only by the moonlight peeking through her windows, tinting the room an eerie blue hue."

    scene pt bonnie trailer
    show pita teeth
    "I look around, I’ve not been in here before, but the room just screamed her name, from the posters strewn about the wall reciting her praises, flowers now wilted sat atop her vanity, and a lump in a bed decorated with the colors pink and green."
    "I was in Bonnie’s room."
    show pita disgusted
    "..."
    "I need to stay quiet... but..."
    menu:
        "I am still rather hungry…":
            "I approach the bed, stepping carefully through the mess of fallen posters and petals. The floor is dangerously creaky."
            "Step… step… step-"
            "{i}{b}Creaaak~{/b}{/i}"
            "I stop in my tracks, the lump in the bed groans and begins getting up- I need to hide, {i}{b}now!{/i}{/b}"
            #TIMED CHOFdiICES
            $ time = 5
            $ timer_range = 5
            $ timer_jump = 'direct'
            show screen countdown
            menu:
                "Hide behind the vanity":
                    hide screen countdown
                    hide pita disgusted
                    show bonnie hidden
                    "I dash towards the vanity, hiding behind the old, rotted wood, white paint peeling off at every nook and cranny."
                    #show bonnie excited
                    b "*Yawn…*"
                    "She steps over to the vanity, sitting down on the cushioned chair."
                    #show bonnie sad
                    b "My lord, have I not been getting enough beauty sleep…?"
                    "She presses a finger to her cheek, pulling at her taut skin. Deep red circles are under her eyes."
                    #hide bonnie hidden
                    #show bonnie disgusted
                    b "Damned fairy…" 
                    "I flinch, holding my breath."
                    b "I’ve hardly any attention from the ringmaster since she’s been here… not any good attention at least…"
                    "She opens her drawer, grabbing some pink face paint. She begins repainting her cheeks, applying some cream below her eye, all done quickly, methodically. She’s been here for a long time, her routine makes that much clear."
                    #show bonnie sad
                    b "{b}Sniffle...{/b}"
                    #hide bonnie sad
                    #show pita disgusted
                    "Is she… crying…?"
                    "Now that I think about it… ever since my arrival, she’s been undermined by the ring leader, wasn’t she originally his favorite…? Is she really… to blame?"
                    #show pita sad
                    "..."
                    "No… I don’t care…"
                    #show pita laugh
                    "She’s been nothing but mean to me, she deserves this… she deserves {b}all{/b} that is coming to her…"
                    #show pita teeth
                    "I slowly reach forward, a large grin forming on my face."
                    "Suddenly, I grab her leg, and pulling her down, I manage to hit her head against the vanity,knocking her unconscious."
                    p "I am so hungry… starved, even.."
                    show bonnie dead
            # INSERT CG'S HERE
                    "{b}{i}Crunch. Crunch. Crunch.{/b}{/i}"
                    "Her teeth taste divine, heavenly after being starved for so long… more… I want more."
                    "My claws dig into the flesh, tearing at cheek and gum, a mess of red staining my hands, spilling from her defiled mouth."
                    "Bits of veins and strings of tattered flesh now decorate the crevice with which once held her teeth in place, filling my stomach, regaining my power…"
                    jump global_courtyard
                "Hide under the bed":
                    hide screen countdown
                    hide pita disgusted
                    "I scurry beneath the bed, eyeing Bonnie’s legs sliding off the side. She stands and steps over to her vanity… now’s my chance…"
                    show bonnie excited
                    "I crawl forward, inching my way over to her, she looks preoccupied, now is my chance to strike…!"
                    "I lunge at her-!!!"
                    hide bonnie excited
                #BLACK SCREEN
                    show blackscreen
                    "{b}SLAM{/b}"
                    "I am knocked back, something incredibly heavy and hard hitting me square in the face…"
                #HIDE BLACK SCREEN
                    hide blackscreen
                    show bonnie disgusted
                    "The drawer from her vanity, broken in half, held in her hands"
                    "The objects that were once inside now spilled out, decorating the floor in pink and green hair ties and makeup and other frilly things."
                    hide bonnie disgusted
                    show pita disgusted
                    "My head is spinning, a terrible, throbbing pain in my skull."
                    "Her footsteps are muffled by the ringing in my head as she walks past me to her bed, grabbing something from behind it. It was something shiny, that reflected the dim light from her vanity"
                    hide pita disgusted
                    show bonnie excited
                    "She stands above me, raising the object over her head."
                    show bonnie disgusted
                    b "I’ve had enough of you, little fairy…"
                    "She slams the object into my stomach, my body lurching forward in pain, tears streaming down my cheeks, the life spilling from my eyes in pitiful, salty tears"
                    b "{b}Quite{/b} enough…"
            #cgs 
                    show bonnie bad
                    "She stabs me again, my body convulsing. I can hear the knife being removed from me again, a disgusting slick, wet sound as my own life spills from the deep wound she created…"
                    return
                "Attempt a direct approach":
                    hide screen countdown
                    jump direct

        "No, I need to get out of here…":
            "I slowly step back, exiting the tent. It’s too risky, I need to escape…"
            jump global_courtyard
        
    label direct:
        "No… I’m done hiding. I’m taking her on here and now."
        "I stand my ground, balling my hands into tight fists as Bonnie rises from her slumber."
        hide pita
        show bonnie disgusted
        b "What- Pita?  What are you doing in here?!"
        p "..."
        "I can feel my heart racing, my mouth sticky and sweat dripping from every pore. I clench my fists, stepping towards her."
        "She slips her hand behind her bed, glaring at me."
        b "What are you getting at, little fairy… come to kill me, have you?"
        "I stumble, taking in a sharp breath, but I continue on my way towards her."
        b "Oh I see.. Lords aren’t you just…"
        "She pauses, pressing a finger to her lips in contemplation"
        b "Bothersome"
        p "Shut it, Bonnie… I’ve had enough of your incessant whining."
        show bonnie excited
        "She laughs, no.. she giggles. She’s giddy and excited, her hand hidden behind her back."
        "I pause, my eyes catching something glinting from behind her, something metal…"
        "something sharp…"
        "She seems to notice my hesitance"
        b "Getting cold feet, are we?"
        "She stands from her bed, walking in long strides towards me."
        "This is my only chance… I lunge at her, my hands reaching for her neck, with intent to push her down"
        "The hand behind her back suddenly shoots forward-"
        p ""
    return