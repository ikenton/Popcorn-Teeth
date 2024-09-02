
define b = Character("Bonnie", color = "#9966cc", voice_tag="b")
define p = Character("Pita", color = "#edf4b3", voice_tag="p")
#timer
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script


$ time = 0

screen qte(rangeD, missed_event):
    on "hide" action SetVariable("g_time", 0)
    hbox:
        xalign 0.5
        yalign 0.1
        timer 0.1 repeat True action If(time > 0, true = SetVariable("time", time - 0.1), false = [Hide("qte"),Jump(missed_event)]) 
        bar:
            value AnimatedValue(value=time, range=rangeD, delay= 0.5)
            xmaximum 300

image redflash:
    "images/redscreen.png"
    alpha 0.0
    linear 1.0 alpha 0.30
    linear 0.5 alpha 0.0
    #linear 0.0 alpha 0.30
    
    repeat
label global_bonnie:
    $ timer_range = 0
    $ timer_jump = 0
    "I take a deep breath, steeling my nerves before hurrying over to the trailer."
    "The outside a faded pink, two large windows sat on one side, painted green and decorated with a pattern of tulips that lined the rim."
    "Stepping up to the door I turn the handle, the door clicking as I push it open. The inside is dim, lit only by the moonlight peeking through the windows, tinting the room an eerie blue hue."
    stop sound fadeout 1.0

    scene pt bonnie trailer
    stop channel1
    $ persistent.bonnieTrailer_unlocked = True
    if visitedBon:
        "I find myself back in Bonnie's trailer again."
        "I'm still rather hungry..."
        jump hungry
    else:
        $ visitedBon = True
        "I look around, I’ve not been in here before, but the room just screamed her name," 
        "from the posters strewn about the wall reciting her praises, flowers now wilted sat atop her vanity," 
        "and a lump in a bed decorated with the colors pink and green."
        "I was in Bonnie’s room."
        
        "..."
        "I need to stay quiet... but..."

        menu:
            "I am still rather hungry…":
                $ persistent.bonnieExcited_unlocked = True
                $ persistent.bonnieSad_unlocked = True
                $ persistent.bonnieDisgust_unlocked = True
                $ persistent.bonnieShocked_unlocked = True
                $ persistent.bonnieChibi_unlocked = True
                label hungry:
                    "I approach the bed, stepping carefully through the mess of fallen posters and petals. The floor is dangerously creaky."
                    "Step… step… step-"
                    play sound "wood-creak-single-v2.mp3"
                    "{i}{b}Creaaak~{/b}{/i}"
                    "I stop in my tracks, the lump in the bed groans and begins getting up- I need to hide, {i}{b}now!{/i}{/b}"
                    #TIMED CHOiICES
                    $ time = 5
                    show screen qte(5, 'failed')
                    menu:
                        "Hide behind the vanity":
                            hide screen qte
                            play music "audio/tension.mp3" fadein 1.0 volume 0.3
                            "I dash towards the vanity, hiding behind the old, rotted wood, white paint peeling off at every nook and cranny."
                            #show bonnie excited
                            voice "voices/Bonnie_Lines/Bonnie_Line1.wav"
                            b "*Yawn…*"
                            show bonnie hidden
                            $ persistent.bonnieHidden_unlocked = True
                            "She steps over to the vanity, sitting down on the cushioned chair."
                            #show bonnie sad
                            voice "voices/Bonnie_Lines/Bonnie_Line2.wav"
                            b "My lord, have I not been getting enough beauty sleep…?"
                            "She presses a finger to her cheek, pulling at her taut skin. Deep red circles are under her eyes."
                            voice "voices/Bonnie_Lines/Bonnie_Line3.wav"
                            b "Damned fairy…" 
                            "I flinch, holding my breath."
                            voice "voices/Bonnie_Lines/Bonnie_Line4.wav"
                            b "I’ve hardly any attention from the ringmaster since she’s been here… not any good attention at least…"
                            "She opens her drawer, grabbing some pink face paint. She begins repainting her cheeks, applying some cream below her eye, all done quickly, methodically. She’s been here for a long time, her routine makes that much clear."
                            #show bonnie sad
                            voice "voices/Bonnie_Lines/Bonnie_Line4.5_Sniffle.wav"

                            b "{b}Sniffle...{/b}"
                            #hide bonnie sad
                            
                            "Is she… crying…?"
                            "Now that I think about it… ever since my arrival, she’s been undermined by the Ringmaster, wasn’t she originally his favorite…? Is she really… to blame?"
                            
                            "..."
                            "No… I don’t care…"
                            
                            "She’s been nothing but mean to me, she deserves this… she deserves {b}all{/b} that is coming to her…"
                            "I slowly reach forward, a large grin forming on my face."
                            "Suddenly, I grab her leg, and pulling her down, I manage to hit her head against the vanity, knocking her unconscious."
                            stop music fadeout 5.0
                            #voice "voices/Pita VA Clips/Bonnie/Pita_Starved3.wav"
                            p "I am so hungry… starved, even.."
                            voice "voices/Bonnie_Lines/Bonnie_Line4.5_Choking.wav"
                            show bonnie dead
                            $ persistent.bonnieDead_unlocked = True
                            $ bonnieIsAlive = False
                            # INSERT CG'S HERE
                            "{b}{i}Crunch. Crunch. Crunch.{/b}{/i}"
                            "Her teeth taste divine, heavenly after being starved for so long… more… I want more."
                            "My claws dig into the flesh, tearing at cheek and gum, a mess of red staining my hands, spilling from her defiled mouth."
                            "Bits of veins and strings of tattered flesh now decorate the crevice with which once held her teeth in place, filling my stomach, regaining my power…"
                            voice "game/voices/Pita VA Clips/Pita_Delicious.wav"
                            p "Delicious."
                            jump global_courtyard
                        "Hide under the bed":
                            hide screen qte
                            show full underbed
                            "I keep my hand pressed over my mouth, biting my tongue as the shuffling goes quiet."
                            "..."
                            "After a few moments of silence, I spot Bonnie’s legs swinging overhead, and she makes her way over to her vanity, taking a seat and peering at her reflection in the mirror."
                            "I do my best to keep in the shadows, feeling fortunate that her room was so dimly lit."
                            "She opens her drawer and begins searching for something from within, this is my chance."
                            $ time = 3
                            show screen qte(3, 'sneak')
                            menu:
                                "Sneak up to her from behind": #fail
                                    label sneak:
                                        play music "audio/tension.mp3" fadein 1.0 volume 0.3
                                        hide screen qte
                                        hide full underbed
                                        "I step out from under the bed, remaining as low to the floor as I can..."
                                        "Step."
                                        "Step.."
                                        "Step..."
                                        "Each hoof gently sliding across the ground, now wary of the creaky floor boards."
                                        #back of bonnie OR bonnie sitting at vanity png
                                        "I finally reach her, and begin to stand, my hands lifting and reaching towards her neck.."
                                        "Finally... I press my hands against her neck-"
                                        "{b}HNGK-{/b}"
                                        "Bonnie slides her chair back as hard as she can, easily knocking me onto my back as I was caught off guard."
                                        "I hear something crash onto the floor as I try to get back on my feet, but it’s in vain."
                                        show bonnie disgusted
                                        "Bonnie kneels down and pressed her knee into my stomach, holding her vanity drawer over her head, and without a word."
                                        hide bonnie disgusted
                                        show blackscreen
                                        stop music 
                                        play sound "audio/piano-keys-smashed.mp3"
                                        "{b}{i}SLAM{/i}{b}"
                                        "She bashes the drawer against my face, rendering me partially unconscious."
                                        hide blackscreen with Dissolve(0.5)
                                        show bonnie disgusted 
                                        "Then, throwing it aside, she digs her hand into my mouth."
                                        
                                        
                                        #crazed yet melancholic expression
                                        show bonnie excited behind blackscreen
                                        voice "voices/Bonnie_Lines/Bonnie_Line8.wav"

                                        b "{i}How does it feel...{/i}"
                                        
                                        #show flashing_red_effect
                                        "She rips one of my teeth from its socket, the initial shock saves me from most of the pain, but it doesn’t take long for it to  catch up with me, and I groan in pain, my breaths shallow."
                                        voice "voices/Bonnie_Lines/Bonnie_Line9.wav"
                                        b "Tell me... is the pain truly unbearable...?"
                                        #TODO: PUT BLACKSCREEN ONTOP OF BONNIE SPRITE
                                                                    
                                        "Another tooth is pulled, my mouth tastes like iron, and my vision begins to dim, I choke on my own fluids, unable to utter even a single sound more."
                                        
                                        voice "voices/Bonnie_Lines/Bonnie_Line10.wav"
                                        b "Already...? That’s no fun..."
                                        
                                        
                                        "Another tooth."
                                    
                                        
                                        "And another."
                                        
                                        "..."
                                        
                                        "She continues pulling out teeth..."
                                        
                                        "Until I finally expire."

                                        jump death_screen

                                        return
                                "Attempt an escape": #succeed but can no longer enter Bonnie's trailer
                                
                                    hide screen qte
                                    "No..."
                                    "This as a bad idea, and now she's awake."
                                    "I need to focus on getting out of here."
                                    hide full underbed
                                    "I pull myself across the floor, keeping low as to avoid Bonnie’s sight, and glance at Bonnie one last time before slipping through the door."
                                    $ escapedBonnie = True
                                    jump global_courtyard
                        "Attempt a direct approach":
                            hide screen qte
                            play music "audio/tension.mp3" fadein 1.0 volume 0.3
                            "No… I’m done hiding. I’m taking her on here and now."
                            "I stand my ground, balling my hands into tight fists as Bonnie rises from her slumber."
                        
                            show bonnie shocked 
                            voice "voices/Bonnie_Lines/Bonnie_Line11.wav"

                            b "What- Pita?  What are you doing in here?!"
                            
                            p "..."
                            "I can feel my heart racing, my mouth sticky and sweat dripping from every pore. I clench my fists, stepping towards her."
                            show bonnie disgusted
                            "She slips her hand behind her bed, glaring at me."

                            voice "voices/Bonnie_Lines/Bonnie_Line12.wav"
                            b "What are you getting at, little fairy… come to kill me, have you?"
                            "I stumble, taking in a sharp breath, but I continue on my way towards her."
                            show bonnie excited

                            voice "voices/Bonnie_Lines/Bonnie_Line13.wav"

                            b "Oh I see.. Lords aren’t you just…"
                            "She pauses, pressing a finger to her lips in contemplation."
                            show bonnie disgusted
                            voice "voices/Bonnie_Lines/Bonnie_Line14.wav"

                            b "Bothersome."
                            #voice "voices/Pita VA Clips/Bonnie/Pita_ShutIt3.wav"
                            p "Shut it, Bonnie… I’ve had enough of your incessant whining."
                            show bonnie excited
                            voice "voices/Bonnie_Lines/Bonnie_Line14.5_Giggle.wav"

                            "She laughs, no.. she giggles. She’s giddy and excited, her hand hidden behind her back."
                            "I pause, my eyes catching something glinting from behind her, something metal…"
                            "Something sharp…"
                            "She seems to notice my hesitance."
                            voice "voices/Bonnie_Lines/Bonnie_Line15.wav"
                            b "Getting cold feet, are we?"
                            "She stands from her bed, walking in long strides towards me."
                            "This is my only chance… I lunge at her, my hands reaching for her neck, with intent to push her down."
                            "The hand behind her back suddenly shoots forward-"
                            play music "FEAR.mp3"
                            show bonnie bad at center
                            $ persistent.bonnie_unlocked = True                    
                            show redflash
                            voice "voices/Pita VA Clips/Bonnie/Pita_Stabbed2.wav"
                            p "Kch- ah.."
                            "She catches me on the object, my eyes falling to her hand, in it an incredibly sharp knife, implanted in my gut."
                            voice "voices/Bonnie_Lines/Bonnie_Line16.wav"
                            b "Oh you poor thing… how clumsy of you, falling right onto such a dangerous object like that…"
                            "I slide off, falling onto the ground."
                            voice "voices/Bonnie_Lines/Bonnie_Line17.wav"
                            b "I’ve had enough of you, little fairy…"
                            "She slams the object into my stomach, my body lurching forward in pain, tears streaming down my cheeks, the life spilling from my eyes in pitiful, salty tears."
                            voice "voices/Bonnie_Lines/Bonnie_Line18.wav"
                            b "{b}Quite{/b} enough..."
                            "She stabs me again, my body convulsing." 
                            "I can hear the knife being torn from my flesh, over and over and over again, a disgusting slick, wet sound as my own life spills from the deep wound she created…"
                            
                            jump death_screen

                            return       
            "No, I need to get out of here…":
                "I slowly step back, exiting the tent. It’s too risky, I need to escape…"
                jump global_courtyard
        
    label failed:
        play sound "wood-creak-single-v3.mp3"
        "I gasp and scurry beneath the bed, pressing my hands over my mouth"
        show underbed
        show bonnie peak at offscreenleft
        show bed
        $ persistent.bonniePeak_unlocked = True
        $ persistent.underBed_unlocked = True
        "..."
        stop sound
        "Maybe she didn’t... hear me..?"
        play sound "audio/door-creek.mp3" 
        show bonnie peak at Move((0.0, -0.8), (0.0, 0.0), 5.0, xanchor = 0, yanchor = 0)
        show bed
        "..." 
        #insert bed creaking noise & peak animation
        p "Bon-"
        stop sound
        play music "audio/tension.mp3" volume 0.3
        "{b}I am suddenly pulled out from under the bed-"
        #show bonnie disgusted
        voice "voices/Bonnie_Lines/Bonnie_Line5.wav"
        b "Wretched thing." 
        "I spin to face her, but it is too late."
        hide bed
        hide underbed
        show blackscreen
        stop music
        play sound "audio/piano-keys-smashed.mp3"
        "{b}SLAM{/b}"
        "I am knocked back, something incredibly heavy and hard hitting me square in the face…"
        #HIDE BLACK SCREEN
        hide blackscreen
        stop sound
        
        show bonnie disgusted at center

        "The drawer from her vanity, broken in half, held in her hands"
        "The objects that were once inside now spilled out, decorating the floor in pink and green hair ties and makeup and other frilly things."
        #show bonnie disgusted
        "My head is spinning, a terrible, throbbing pain in my skull."
        "Her footsteps are muffled by the ringing in my head as she walks past me to her bed, grabbing something from behind it. It was something shiny, that reflected the dim light from her vanity"
        
        play music "audio/FEAR.mp3"
        show bonnie bad
        show redflash
        $ persistent.bonnieBad_unlocked = True
        "She stands above me, raising the object over her head."
        voice "voices/Bonnie_Lines/Bonnie_Line6.wav"
        
        b "I’ve had enough of you, little fairy…"
        "She slams the object into my stomach, my body lurching forward in pain, tears streaming down my cheeks, the life spilling from my eyes in pitiful, salty tears."
        voice "voices/Bonnie_Lines/Bonnie_Line7.wav"
        b "{b}Quite{/b} enough…"
        "She stabs me again, my body convulsing." 
        "I can hear the knife being torn from my flesh, over and over and over again, a disgusting slick, wet sound as my own life spills from the deep wound she created…"

        jump death_screen

        return
    return
