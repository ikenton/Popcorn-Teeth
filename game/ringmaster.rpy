define rm = Character("Ringmaster", color = "#ff0000")
define p = Character("Pita", color = "#edf4b3")
image ringmaster_looks_slideshow:
    "ringmaster maskless 2"
    pause 1.0
    "ringmaster maskless"
    pause 1.0
        
label global_ringmaster:
    show ringmaster door
    "I approach the trailer and notice that it’s slightly open."
    if marlonIsAlive or bonnieIsAlive or hugoIsAlive:
        "Should I enter?"
        menu:
            "Yes.":
                jump enter
            "No.":
                "I slowly back away from the open door and my immense dread fades."
                hide door
                jump global_courtyard
    else:
        label enter:
            stop channel1 
            hide door
            stop sound fadeout 1.0
            #scene ringmaster-trailer
            $ persistent.ringmasterTrailer_unlocked = True
            "I take a step on the stepping stool and open the door to a poorly lit room."
            "A man sits at his desk."
            play sound "audio/wood-creak-single-v3.mp3"
            scene ringmaster_looks_slideshow
            $ persistent.ringmasterMaskless2_unlocked = True
            $ persistent.ringmasterMaskless_unlocked = True
            play music "tension.mp3" fadein 1.5
            "!!!"
            $ persistent.ringmaster_unlocked = True
            "He reaches for his mask and slips it on."
            
            scene ringmaster-trailer
            show ringmaster
            "He stands up and fully faces me."
            if not marlonIsAlive and not bonnieIsAlive and not hugoIsAlive:
                $ persistent.outtaTeeth_unlocked = True
                jump goodEnding
            else:
                jump rmbadending

            label goodEnding:
                rm "I can smell the blood on your hands, Sweetheart."
                rm "It’s impressive that you wiped out my circus."
                rm "My failure of a son, Marlon, the charismatic Hugo, and my little perfectionista, Bonnie."
                rm "How did their teeth taste?"
                rm "I hope it was to your liking."
                "How did he know?"
                voice "voices/Pita VA Clips/Ringmaster/Pita_TastedWonderfully.wav"
                p "They tasted wonderfully~"
                "I put out my hand and scowl"
                voice "voices/Pita VA Clips/Ringmaster/Pita_NowGive.wav"
                p "Now give me my wand before I take your life! "
                rm "No, sweetheart. Now think of what we could have together."
                rm "Just the two of us."
                rm "The fantastic duo of the Striking Light Circus!"
                rm "We can even get a new crew if we wanted to, but we’ll both be the bosses, we’ll be equal partners."
                "He puts out his hand towards me."
                rm "Whaddya say?"
                menu:
                    "No.":
                        jump killing_rm
                    "Yes.":
                        jump rm_teamup
                label killing_rm:

                    p "I never wanted to be here to begin with!" #NO VOICE LINE! GO BACK AND SEARCH!!!!!!!!! PROBABLY IN voices/Pita VA Clips/Celina_Endings.wav
                    "I fly towards him at great speed with my claws ready to tear at his flesh."
                    "He catches my arm but I quickly pull away and slash at him repeatedly."
                    "With my unfathomable rage, I knock him down to the ground and pummel him senselessly."
                    "He must pay for everything he has done to me!"
                    "I tear off his mask and I grins as he begins coughing and wheezing."
                    show ringmaster dead
                    $ persistent.ringmasterDead_unlocked = True
                    voice "voices/RM VA clips/RM_DreamComeTrue.wav"
                    rm "Do you know how much of a dream come true that you are to me?"
                    voice "voices/RM VA clips/RM_EverSince.wav"
                    rm "Ever since I was a kid, I worshipped you, I kept sacrificing my teeth till I got you."
                    voice "voices/RM VA clips/RM_Will2Live.wav"
                    rm "You were my will to live,"
                    voice "voices/RM VA clips/RM_PrizedPoss.wav"
                    rm "you were my most prized possession,"
                    voice "voices/RM VA clips/RM_PerfectStar.wav"
                    rm "you were a perfect and beautiful star."
                    voice "voices/RM VA clips/RM_ManToday.wav"
                    rm "{b}You made me the man that I am today.{/b}"
                    "He places a hand on mine."
                    "I recoil and slap him."
                    voice "voices/Pita VA Clips/Ringmaster/Pita_IDC.wav"
                    p "I don’t care."
                    "I break his jaw and he goes still."
                    "I pluck a tooth from his lower jaw and chew."
                    "I gag and spit it out."
                    "He wasn’t kidding."
                    "His teeth were wooden..."
                    "I stand up and I rummage every nook and cranny of his trailer."
                    "I find my wand in one of his desk’s drawers and I grin."
                    "Holding it in my hands finally made me feel complete and content."
                    "It’s time to go home."
                    $ persistent.ringmasterShirtless_unlocked = True
                    return
            label rmbadending:
                voice "voices/RM VA clips/RM_MyMyMy.wav"
                rm "My, my, my little Princess is trying to fly away! "
                voice "voices/RM VA clips/RM_GotNerve.wav"
                rm "You got a nerve to be out of your cage."
                voice "voices/Pita VA Clips/Ringmaster/Pita_Wand.wav"
                p "I’m escaping with my wand and you’re not going to stop me!"
                "I fly towards him at great speed with my claws ready to tear at his flesh."
                stop music
                play sound "piano-keys-smashed.mp3"
                queue sound "death_screen.mp3" loop
                ""
                voice "voices/Pita VA Clips/Pita_Ack2.wav" #VOICE LINE NO WORK FIX LATER
                p "Ack-!"
                "He catches me from the throat and squeezes it. No! I’m not strong enough-"
                voice "voices/RM VA clips/Bad Ending/RM_Line3.wav"
                rm "You know I don’t want to hurt you and yet you test me?!"
                voice "voices/RM VA clips/Bad Ending/RM_Line4.wav"
                rm "You have no power and you will learn your place that you’re supposed to be my perfect star."
                voice "voices/RM VA clips/Bad Ending/RM_Line5.wav"
                
                rm "You’re mine forever, till death do us part!"
                "I seethe and scratch at arms."
                
                "He drops me onto the ground."
                voice "voices/Pita VA Clips/Ringmaster/Pita_FuckYou.wav"
                p "Fuck you! I’m not your pet!"
                "I attempt to get up, yet I feel something pin my leg on the ground. He has his large foot on my shin!"
                "I scream"
                voice "voices/Pita VA Clips/Ringmaster/Pita_LetGo.wav"
                p "{b}LET GO OF ME!{/b}"
                voice "voices/RM VA clips/Bad Ending/RM_Line6.wav"
                rm "You know that’s not an option, sweetheart."
                rm "Stay still."
                p "?!!!"
                hide ringmaster 
                show blackscreen

                #CRUNCH NOISE
                voice "voices/Pita VA Clips/Pita_Aggh.wav"
                p "AHH-AGH"
                hide blackscreen                
                show pita dead
                $ persistent.pitaDead_unlocked = True
                "I look down at my leg and notice that it’s bleeding and that one of my bones is sticking out."
                voice "voices/Pita VA Clips/Pita_No.wav"
                p "{b}NO! NO!!{/b}"
                "My body terribly shakes in horror at the sigh of my own broken leg. "
                "I can’t move it and it hurts!"
                "I try crawling away with my arms and look toward the door."
                "He laughs"
                rm "Still trying to escape me? It seems you haven’t learned your lesson. Maybe I’ve been too soft on you, my dear. "
                rm "..."
                rm "I'm doing this for your own good."
                "He places a foot on my back and on my other leg I look at him in terror."
                voice "voices/Pita VA Clips/Ringmaster/Pita_GoHome.wav"
                p "No! Please just let me go, I’m sorry! I just want to go home! I want to go-"

                #CRONCH

                "My legs..."
                "The pain is too much"

                "Since that night, I never had another opportunity to escape."
                "He chained me up every night and put me in that cage."
                "I performed and performed and performed in front of millions of crowds with only my arms and wings."
                "I never got to go home ever again."
                jump death_screen
            label rm_teamup:
                show pita push
                $ persistent.pitaPush_unlocked = True
                "I reach past his hand and grab him by the collar, dragging him in."
                voice "voices/Pita VA Clips/Ringmaster/TeamUp/Pita_Line1.wav"
                p "Fine... but we need to establish some ground rules."
                voice "voices/Pita VA Clips/Ringmaster/TeamUp/Pita_Line2.wav"
                p "First, we’re not equals. If you try anything funny, I’ll kill you."
                voice "voices/RM VA clips/RMteamup/RM_DontTrust.wav"
                rm "You don’t trust me? I’m hurt! How you wound me so, my beautiful princess…"
                "I slam him against the caravan wall and snarl."
                voice "voices/RM VA clips/RMteamup/RM_VeryWell.wav"
                rm "Very well, as you wish."
                voice "voices/Pita VA Clips/Ringmaster/TeamUp/Pita_Line3.wav"
                p "Second, tell me where my wand is. I’m not taking any other chances."
                "He points at one of his drawers"
                voice "voices/RM VA clips/RMteamup/RM_InThereSweet.wav"
                rm "In there, sweetheart, I kept it close to remind me of you at night."
                "I slam him again out of disgust, and drag him towards the drawer he pointed at. Using my other hand, I rummage around and manage to find my wand."
                voice "voices/Pita VA Clips/Ringmaster/TeamUp/Pita_Line4.wav"
                p "There you are! Now where were we… Oh yes, our terms."
                voice "voices/Pita VA Clips/Ringmaster/TeamUp/Pita_Line6.wav"

                p "Finally, I’m a fairy. I fly by my own terms, and you will never lock me down again. I’m staying out of convenience, and the minute I don’t need you or this circus, I’m gone. If you try to stop me, just remember what rule one was."
                voice "voices/Pita VA Clips/Ringmaster/TeamUp/Pita_Line7.wav"
                p "Now, are we clear?"
                voice "voices/RM VA clips/RMteamup/RM_cryst.wav"
                rm "Crystalline."
                "I loosen my grip. He tenderly grabs my hand and leans in to kiss it, but I slap him away."
                
                p "Quit it!" #NO VOICE LINE OR A MIX UP, WILL HAVE TO GO BACK THROUGH ALL THE AUDIO TO FIND IT
                "But he just cackles in glee."
                voice "voices/RM VA clips/RMteamup/RM_LookForward.wav"
                rm "Oh how I look forward to our new partnership!"
                scene blackscreen
                
                "Several weeks later…"
                voice "voices/RM VA clips/RMteamup/RM_Welcome.wav"
                rm "Welcome, one and all, to the Striking Light Circus! We have a wonderful performance for you tonight, led by the one! The only!"
                show pita rm_teamup with dissolve
                $ persistent.pitaRMTeamUp_unlocked = True
                voice "voices/RM VA clips/RMteamup/RM_PitaTheTooth.wav"
                rm "Pita the Tooth Fairy!"
                #play applause sound effects
                "A roar of cheers and applause rings through the tent."
                "I walk up the stage and give a great wave and a wide smile"
                voice "voices/Pita VA Clips/Ringmaster/TeamUp/Pita_Line8.wav"

                p "Thank you all for coming to the show! I hope you’ll enjoy this performance as I will be performing it!"
                "I spot a nice target in the crowd and I lick my lips in enthusiasm. The afterparty will be fantastic once more."
                $ persistent.ringmasterShirtless_unlocked = True
                return
            