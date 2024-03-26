define rm = Character("Ringmaster", color = "#F00040")
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
            "Yes":
                jump enter
            "No":
                "I slowly back away from the open door and my immense dread fades."
                hide door
                jump global_courtyard
    else:
        label enter:
            hide door
            stop sound fadeout 1.0
            play music "tension.mp3"
            #scene ringmaster-trailer
            $ persistent.ringmasterTrailer_unlocked = True
            "I take a step on the stepping stool and open the door to a poorly lit room."
            scene ringmaster_looks_slideshow
            $ persistent.ringmaster_unlocked = True
            "A man sits at his desk, writing. He doesn’t bother to raise his head, but instead reaches for his mask and slips it on."
            scene ringmaster-trailer
            show ringmaster
            if not marlonIsAlive and not bonnieIsAlive and not hugoIsAlive:
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
                p "They tasted wonderfully~"
                "I put out my hand and scowl"
                p "Now give me my wand before I take your life! "
                rm "No, sweetheart. Now think of what we could have together."
                rm "Just the two of us."
                rm "The fantastic duo of the Striking Light Circus!"
                rm "We can even get a new crew if we wanted to, but we’ll both be the bosses, we’ll be equal partners."
                "He puts out his hand towards me."
                rm "Whaddya say?"
                p "No."
                p "I never wanted to be here to begin with!"
                "I fly towards him at great speed with my claws ready to tear at his flesh."
                "He catches my arm but I quickly pull away and slash at him repeatedly."
                "With my unfathomable rage, I knock him down to the ground and pummel him senselessly."
                "He must pay for everything he has done to me!"
                show ringmaster dead
                $ persistent.ringmasterDead_unlocked = True
                "I tear off his mask and I grins as he begins coughing and wheezing."
                rm "Do you know how much of a dream come true that you are to me?"
                rm "Ever since I was a kid, I worshiped you, I kept sacrificing my teeth till I got you."
                rm "You were my will to live,"
                rm "you were my most prized possession,"
                rm "you were a perfect and beautiful star."
                rm "{b}You made me the man that I am today.{/b}"
                "He places a hand on mine."
                "I recoil and slap him."
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
                return
            label rmbadending:
                rm "My, my, my little Princess is trying to fly away! "
                rm "You got a nerve to be out of your cage."
                p "I’m escaping with my wand and you’re not going to stop me!"
                "I fly towards him at great speed with my claws ready to tear at his flesh."
                p "Ack-!"
                "He catches me from the throat and squeezes it. No! I’m not strong enough-"
                rm "You know I don’t want to hurt you and yet you test me?!"
                rm "You have no power and you will learn your place that you’re supposed to be my perfect star."
                rm "You’re mine forever, till death do us part!"
                "I seethe and scratch at arms."
                
                "He drops me onto the ground. "
                p "Fuck you! I’m not your pet!"
                "I attempt to get up, yet I feel something pin my leg on the ground. He has his large foot on my shin!"
                "I scream"
                p "{b}LET GO OF ME!{/b}"
                rm "You know that’s not an option, sweetheart."
                rm "Stay still."
                p "?!!!"
                hide ringmaster
                #play music "FEAR.mp3"
                show blackscreen

                #CRUNCH NOISE

                p "AHH-AGH"
                hide blackscreen                
                show pita dead
                $ persistent.pitaDead_unlocked = True
                "I look down at my leg and notice that it’s bleeding and that one of my bones is sticking out."
                p "{b}NO! NO!!{/b}"
                "My body terribly shakes in horror at the sigh of my own broken leg. "
                "I can’t move it and it hurts!"
                "I try crawling away with my arms and look toward the door."
                "He laughs"
                rm "Still trying to escape me? It seems you haven’t learned your lesson. Maybe I’ve been too soft on you, my dear. "
                rm "..."
                rm "I'm doing this for your own good."
                "He places a foot on my back and on my other leg I look at him in terror."
                p "No! Please just let me go, I’m sorry! I just want to go home! I want to go-"

                #CRONCH

                "My legs..."
                "The pain is too much"

                "Since that night, I never had another opportunity to escape."
                "He chained me up every night and put me in that cage."
                "I performed and performed and performed in front of millions of crowds with only my arms and wings."
                "I never got to go home ever again."
                return


            