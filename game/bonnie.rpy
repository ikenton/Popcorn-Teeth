
define b = Character("Bonnie", color = "#9966cc")
define p = Character("Pita", color = "#edf4b3")
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
    stop sound fadeout 1.0
    play music "tension.mp3" fadein 0.5
    scene pt bonnie trailer

    "I look around, I’ve not been in here before, but the room just screamed her name," 
    "from the posters strewn about the wall reciting her praises, flowers now wilted sat atop her vanity," 
    "and a lump in a bed decorated with the colors pink and green."
    "I was in Bonnie’s room."
    
    "..."
    "I need to stay quiet... but..."
    menu:
        "I am still rather hungry…":
            "I approach the bed, stepping carefully through the mess of fallen posters and petals. The floor is dangerously creaky."
            "Step… step… step-"
            "{i}{b}Creaaak~{/b}{/i}"
            "I stop in my tracks, the lump in the bed groans and begins getting up- I need to hide, {i}{b}now!{/i}{/b}"
            #TIMED CHOiICES
            $ time = 5
            $ timer_range = 5
            $ timer_jump = 'failed'
            show screen countdown
            menu:
                "Hide behind the vanity":
                    hide screen countdown
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
                    
                    "Is she… crying…?"
                    "Now that I think about it… ever since my arrival, she’s been undermined by the ring leader, wasn’t she originally his favorite…? Is she really… to blame?"
                    
                    "..."
                    "No… I don’t care…"
                    
                    "She’s been nothing but mean to me, she deserves this… she deserves {b}all{/b} that is coming to her…"
                    "I slowly reach forward, a large grin forming on my face."
                    "Suddenly, I grab her leg, and pulling her down, I manage to hit her head against the vanity,knocking her unconscious."
                    stop music fadeout 1.5
                    p "I am so hungry… starved, even.."
                    show bonnie dead
                    $ bonnieIsAlive = False
                    # INSERT CG'S HERE
                    "{b}{i}Crunch. Crunch. Crunch.{/b}{/i}"
                    "Her teeth taste divine, heavenly after being starved for so long… more… I want more."
                    "My claws dig into the flesh, tearing at cheek and gum, a mess of red staining my hands, spilling from her defiled mouth."
                    "Bits of veins and strings of tattered flesh now decorate the crevice with which once held her teeth in place, filling my stomach, regaining my power…"
                    jump global_courtyard
                "Hide under the bed":
                    hide screen countdown
                    "I keep my hand pressed over my mouth, biting my tongue as the shuffling goes quiet."
                    "..."
                    "After a few moments of silence, I spot Bonnie’s legs swinging overhead, and she makes her way over to her vanity, taking a seat and peering at her reflection in the mirror."
                    "I do my best to keep in the shadows, feeling fortunate that her room was so dimly lit."
                    "She opens her drawer and begins searching for something from within, this is my chance."
                    $ time = 5
                    $ timer_range = 5
                    $ timer_jump = 'sneak'
                    show screen countdown
                    menu:
                        "Sneak up to her from behind": #fail
                            label sneak:
                                hide screen countdown
                                "I step out from under the bed, remaining as low to the floor as I can..."
                                "Step."
                                "Step.."
                                "Step..."
                                "Each hoof gently sliding across the ground, now wary of the creaky floor boards"
                                #back of bonnie OR bonnie sitting at vanity png
                                "I finally reach her, and begin to stand, my hands lifting and reaching towards her neck.."
                                "Finally... I press my hands against her neck-"
                                "{b}HNGK-{/b}"
                                "Bonnie slides her chair back as hard as she can, easily knocking me onto my back as I was caught off guard."
                                "I hear something crash onto the floor as I try to get back on my feet, but it’s in vain"
                                show bonnie disgusted
                                "Bonnie kneels down and pressed her knee into my stomach, holding her vanity drawer over her head, and without a word"
                                hide bonnie disgusted
                                show blackscreen
                                
                                "{b}{i}SLAM{/i}{b}"
                                "She bashes the drawer against my face, rendering me partially unconscious"
                                
                                show bonnie disgusted
                                show blackscreen:
                                    alpha .5 
                                "Then, throwing it aside, she digs her hand into my mouth"
                                show blackscreen:
                                    alpha .2 
                                #crazed yet melancholic expression
                                show bonnie excited
                                b "{i}How does it feel...{/i}"
                                show blackscreen:
                                    alpha .1
                                
                                "She rips one of my teeth from its socket, the initial shock saves me from most of the pain, but it doesn’t take long for it to  catch up with me, and I groan in pain, my breaths shallow."
                                b "Tell me... is the pain truly unbearable..?"
                                #TODO: PUT BLACKSCREEN ONTOP OF BONNIE SPRITE
                                show blackscreen:
                                    alpha .5 
                                
                                "Another tooth is pulled, my mouth tastes like iron, and my vision begins to dim, I choke on my own fluids, unable to utter even a single sound more."
                                show blackscreen:
                                    alpha .6 
                                
                                b "Already..? That’s no fun..."
                                show blackscreen:
                                    alpha .7
                                
                                "Another tooth"
                                show blackscreen:
                                    alpha .8
                                
                                "And another"
                                show blackscreen:
                                    alpha .85 
                                "..."
                                show blackscreen:
                                    alpha .9 
                                "She continues pulling out teeth"
                                show blackscreen:
                                    alpha 1.0
                                "Until I finally expire"
                                return
                        "Attempt an escape": #succeed but can no longer enter Bonnie's trailer
                            hide screen countdown
                            "No..."
                            "This as a bad idea, and now she's awake."
                            "I need to focus on getting out of here."
                            "I pull myself across the floor, keeping low as to avoid Bonnie’s sight, and glance at Bonnie one last time before slipping through the door."
                            $ escapedBonnie = True
                            jump global_courtyard
                "Attempt a direct approach":
                    hide screen countdown
                    "No… I’m done hiding. I’m taking her on here and now."
                    "I stand my ground, balling my hands into tight fists as Bonnie rises from her slumber."
                
                    show bonnie shocked 
                    b "What- Pita?  What are you doing in here?!"
                    
                    p "..."
                    "I can feel my heart racing, my mouth sticky and sweat dripping from every pore. I clench my fists, stepping towards her."
                    "She slips her hand behind her bed, glaring at me."
                    show bonnie disgusted
                    b "What are you getting at, little fairy… come to kill me, have you?"
                    "I stumble, taking in a sharp breath, but I continue on my way towards her."
                    show bonnie excited
                    b "Oh I see.. Lords aren’t you just…"
                    "She pauses, pressing a finger to her lips in contemplation"
                    show bonnie disgusted
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
                    play music "FEAR.mp3"
                    p "Kch- ah.."
                    "She catches me on the object, my eyes falling to her hand, in it an incredibly sharp knife, implanted in my gut."
                    
                    show bonnie disgusted at center
                    b "Oh you poor thing… how clumsy of you, falling right onto such a dangerous object like that…"
                    #play music "FEAR.mp3"
                    show bonnie bad
                    "I slide off, falling onto the ground."
                    b "I’ve had enough of you, little fairy…"
                    "She slams the object into my stomach, my body lurching forward in pain, tears streaming down my cheeks, the life spilling from my eyes in pitiful, salty tears."
                    b "{b}Quite{/b} enough..."
                    "She stabs me again, my body convulsing." 
                    "I can hear the knife being tornfrom my flesh, over and over and over again, a disgusting slick, wet sound as my own life spills from the deep wound she created…"
                    return       
        "No, I need to get out of here…":
            "I slowly step back, exiting the tent. It’s too risky, I need to escape…"
            jump global_courtyard
        
    label failed:
        "I gasp and scurry beneath the bed, pressing my hands over my mouth"
        "..."
        "Maybe she didn’t... hear me..?"
        "..." 
        #insert bed creaking noise
        "Slowly, Bonnie peers under the bed, only her eyes are visible at first then, after a second upon seeing me"
        "her head lowers further, revealing a demented smile"
        p "Bon-"
        "{b}I am suddenly pulled out from under the bed-"
        show bonnie disgusted
        b "Wretched thing." 
        "I spin to face her, but it is too late."
        show blackscreen
        "{b}SLAM{/b}"
        play music "FEAR.mp3"
        "I am knocked back, something incredibly heavy and hard hitting me square in the face…"
        #HIDE BLACK SCREEN
        hide blackscreen
        show bonnie disgusted
        "The drawer from her vanity, broken in half, held in her hands"
        "The objects that were once inside now spilled out, decorating the floor in pink and green hair ties and makeup and other frilly things."
        #show bonnie disgusted
        "My head is spinning, a terrible, throbbing pain in my skull."
        "Her footsteps are muffled by the ringing in my head as she walks past me to her bed, grabbing something from behind it. It was something shiny, that reflected the dim light from her vanity"
        
        show bonnie bad
        "She stands above me, raising the object over her head."
        
        b "I’ve had enough of you, little fairy…"
        "She slams the object into my stomach, my body lurching forward in pain, tears streaming down my cheeks, the life spilling from my eyes in pitiful, salty tears"
        b "{b}Quite{/b} enough…"
        "She stabs me again, my body convulsing." 
        "I can hear the knife being torn from my flesh, over and over and over again, a disgusting slick, wet sound as my own life spills from the deep wound she created…"
        return
    return