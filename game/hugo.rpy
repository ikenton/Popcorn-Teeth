define h = Character("Hugo", color = "#862424")
define p = Character("Pita", color = "#edf4b3")
define rm = Character("Ringmaster", color = "#ff0000")

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
image chest death_slideshow:
    #hugo pants holding chest
    "chest darkness" with Dissolve(0.2)
    pause 0.5
    #key sound
    "hugo open" with Dissolve(0.5)
    pause 0.5
    "hugo grab" 
    pause 1.0
    "hugo bad" 
    pause 2.0
    "blackscreen" with Dissolve(1.0)

image hugo smile_action:
    "hugo surprised"
    pause 4.0
    "hugo smile"

label global_hugoVendetta:
    $ timer_range = 0
    $ timer_jump = 0
    scene hugo-trailerdoor
    if visitedHugo:
        "I quietly approach the colorful and flashy trailer again."
        "I can see smoke coming from behind the trailer and humming."
        "Who could it be?"
    else: 
        "I look over and quietly approach the colorful and flashy trailer with many posters from past shows on it. I don’t seem to be on any of them."
        "I can see smoke coming from behind the trailer and humming. I cock my head with curiosity."
        "Who could it be?"
    $ visitedHugo = True

    menu:
        "Leave":
            jump global_courtyard
        "Take a peek":
            $ persistent.hugoNuetral_unlocked = True
            $ persistent.hugoSmile_unlocked = True
            $ persistent.hugoSmoking_unlocked = True
            $ persistent.hugoSuprised_unlocked = True
            $ persistent.hugoUpset_unlocked = True
            $ persistent.hugoAngry_unlocked = True
            $ persistent.hugoBack_unlocked = True
            $ persistent.hugoChibi_unlocked = True
            "I place my dainty hand on the trailer and slowly poke my head out."
            "Oh I know who it is."
            play music "tension.mp3" fadein 1.0 volume 0.5
            show hugo back
            $ persistent.hugoChad_unlocked = True
            $ persistent.hugoPoster_unlocked = True
            "I can see the back of that mean clown, humming and smoking."
            "Ugh, I hate Hugo… he’d press his cigarette butts onto my skin till I could smell my own skin and he’d bad mouth me backstage. I get that he never wanted me here, but I also never wanted to be here!"
            "Oh!"
            "I look beside him and I spot a rusty foldable table next to him that has a toolbox and a half eaten sandwich on top of it. hmm…"
            "!!!"
            "Hugo drops his cigarette and stomps on it."
            "Crap!"
            #timer
            $ time = 5
            show screen qte(5, 'badending')
            menu:
                "Hide!":
                    hide screen qte
                    hide hugo
                    show pita underneath
                    play sound "audio/footsteps-dirt-gravel.mp3"
                    "I quickly hide underneath the trailer and I pull my white dress with me so it isn’t poking out, getting it dirty in the process." 
                    "I place my hand on my mouth as I watch Hugo walk to his trailer and go up the creaky steps. I can hear keys jingle."
                    
                    #timed
                    
                    $ time = 5
                    show screen qte(5,'wait')
                    menu:
                        "Go Now":
                            hide screen qte
                            hide pita underneath
                            
                            stop sound fadeout 1.0
                            play sound "wood-creak-single-v2.mp3" fadein 0.5
                            "I crawl out of the trailer and I stand up, hunching as I approach behind Hugo. I go up one of the steps and it creaks."
                            stop sound 
                            "!!!"
                            stop sound
                            show hugo surprised
                            "Hugo‘s head snaps in my direction."
                            voice "voices/HUGO LINES/Hugo_CommonBadEnding1.wav"
                            h "What the?! What are you doing here?!"
                            voice "voices/Pita VA Clips/Hugo/Pita_Hugo2.wav"
                            p "Hugo?!-"
                            play music "FEAR.mp3"

                            jump badending
                        "Wait":
                            hide screen qte
                            label wait:
                                "I lay there under the trailer. I could hear Hugo walking inside the trailer."
                                "I remember seeing the toolbox behind the trailer. Maybe there’s something in there that I can use. I crawl out from under the trailer and I stand up. I don't bother dusting off my dress and I quietly go behind the trailer."
                                hide pita underneath
                                hide hugo
                                show  toolbox
                                "I open the toolbox and go through it. I find a rusty hammer, or is that blood on it? I hold it in my hand and it feels oddly heavy."
                                "I didn’t realize I’ve become this weak…"
                                "*Sighs*"
                                "I’ll regain all my strength soon. C’mon, I got this, Pita!"
                                "I look around and find an open window. I smile and climb my way into the trailer quietly. I can hear gentle snoring coming from the bedroom area of the trailer."
                                "I hold the hammer with both hands and slowly approach the source of the noise."
                                
                                scene pt-hugo-trailer
                                $ persistent.hugoTrailer_unlocked = True
                                hide hugo
                                stop channel1
                                $ persistent.hugoTrailer_unlocked = True
                                stop sound fadeout 1.0
                                "I poke my head in and view a resting Hugo with his arms behind his head and his legs crossed. It seems that he’s napping…"
                                "Perfect"
                                show hugo hammer
                                $ persistent.hugoHammer_unlocked = True
                                $ hugoIsAlive = False
                                "I raise the hammer above my head and strike it down onto Hugo’s face repeatedly."
                                #voice "voices/Pita VA Clips/Pita_Laugh2.wav"
                                p "Hehe—-HEHEHEH!"
                                stop music fadeout 5.0
                                "The adrenaline and euphoria embody my very soul to the brim as I hear his bones crack and flesh squelch every time I bring down the hammer."
                                "I drop the hammer to the ground and begin picking at the teeth and other skull fragments from the disfigured face. I popped them into my mouth like how humans eat chips and chew with saliva and blood dripping from my jaw."
                                hide hugo hammer
                                #voice "voices/Pita VA Clips/Hugo/Pita_Mmm1.wav"
                                p "Mmm"
                                "I finish and wipe my mouth."
                                "I’ve made quite a mess."
                                "I wipe the blood off myself with Hugo’s blankets and I bend down to look for the hammer."
                                "I look under the bed and see the hammer’s head separated from the handle."
                                #voice "voices/Pita VA Clips/Hugo/Pita_Crap1.wav"
                                p "Crap"
                                "I stand back up straight and look at the trailer’s door. I need more."
                                "I leave the trailer and head back to the courtyard."
                                jump global_courtyard
                "Throw a pebble":
                    hide screen qte
                    "I look down and grab a pebble off the ground. This should get 'em distracted!"
                    voice "voices/HUGO LINES/Hugo_Line1.wav"
                    h "Who’s there?!"
                    show hugo pebble
                    $ persistent.hugoPebble_unlocked = True
                    "He approaches the sound where the pebble was."
                    "Perfect! This is my chance. I approach Hugo quickly and quietly from behind. I bump into him in an attempt to knock him over but he barely budged! "
                    scene toolbox
                    $ persistent.toolbox_unlocked = True
                    show hugo surprised
                    "Hugo turns around and looks down at me."
                    voice "voices/HUGO LINES/Hugo_CommonBadEnding1.wav"
                    h "What the?! What are you doing here?!"
                    voice "voices/Pita VA Clips/Hugo/Pita_Hugo2.wav"
                    p "Hugo?!-"
                    play music "FEAR.mp3"

                    jump badending
        "Wait and listen":
            $ persistent.hugoNuetral_unlocked = True
            $ persistent.hugoSmile_unlocked = True
            $ persistent.hugoSmoking_unlocked = True
            $ persistent.hugoSuprised_unlocked = True
            $ persistent.hugoUpset_unlocked = True
            $ persistent.hugoAngry_unlocked = True
            $ persistent.hugoBack_unlocked = True
            play channel2 ("audio/footsteps-dirt-gravel.mp3")
            "I dare not to take any chance of making myself known yet…I wait and listen for a while. After a moment,the humming stops and I can hear footsteps approaching!"
            #timed
            $ time = 2
            show screen qte(2, 'prebadending')
            menu:
                "Hide!":
                    hide screen qte
                    show pita underneath
                    $ persistent.underTrailer_unlocked = True
                    "I quickly hide underneath the trailer and I pull my white dress with me so it isn’t poking out, getting it dirty in the process. I place my hand on my mouth as I watch Hugo walk to his trailer and go up the creaky steps. I can hear keys jingle."
                    stop channel2 fadeout 1.0
                    $ time = 5
                    show screen qte(5, 'wait2')
                    menu: #timed
                        "Go Now":
                            hide screen qte
                            hide pita underneath
                            "I crawl out of the trailer and I stand up, hunching as I approach behind Hugo. I go up one of the steps."
                            #play creak sound
                            play sound "wood-creak-single-v3.mp3"
                            "Creeeak"
                            "!!!"
                            play music "tension.mp3" fadein 3.0 volume 0.5
                            "Hugo suddenly turns around"
                            show hugo surprised
                            voice "voices/HUGO LINES/Hugo_CommonBadEnding1.wav"
                            h "What the?! What are you doing here?!"
                            voice "voices/Pita VA Clips/Hugo/Pita_Hugo2.wav"
                            p "Hugo?!-"

                            jump badending
                        "Wait":
                            hide screen qte
                            label wait2:
                                play sound "wood-creak-single-v2.mp3" fadein 0.5

                                "I lay there under the trailer. I could hear Hugo walking inside the trailer."
                                stop channel2 fadeout 1.0
                                "Oh! I look up and notice a trapdoor, I can see a square outline of the light coming from inside the trailer. I grin and I wait for some minutes until I can barely hear any movement coming from inside the trailer."
                                "I slightly push up the trapdoor and it opens."
                                scene pt-hugo-trailer
                                stop channel1
                                $ persistent.hugoTrailer_unlocked = True
                                hide pita underneath
                                "I grin and I enter the trailer though the trapdoor as quietly as I can."
                                show hugo asleep
                                play music "tension.mp3" volume 0.5
                                "I scan my surroundings and see Hugo in bed, facing the wall. lowering my head, I quietly approach him. Eventually, I  get close enough to him and I look around for a weapon. I grab the base of a lamp with both of my hands."
                                show hugo awake
                                "Hugo turns his body towards me and jumps."
                                show hugo surprised
                                voice "voices/HUGO LINES/Hugo_Line2.wav"
                                h "Are you trying to kill me?"
                                menu:
                                    "Yes":
                                        "I immediately strike down the lamp onto Hugo’s head."
                                        "He catches it in  midair. I gasp and let go of the lamp. I grit my teeth."
                                        show hugo smile_action
                                        "Desperate, I strike at his face with my fingernails, drawing some blood. He recoils and screams. He wipes his face and notices the blood on his fingertips. He then looks at me with a sinister grin."
                                        voice "voices/HUGO LINES/Hugo_Line3.wav"
                                        h "Look what we have here. The fairy’s giving me an opportunity of a lifetime!"
                                        "He swings the lamp towards me-"                                       
                                        show blackscreen
                                        stop music fadeout 0.5
                                        "..." #add ringing sound
                                        "Everything went dark for a moment as I got struck by the lamp."

                                    "No":
                                        "Hugo sits up on the bed and stares at me."
                                        show hugo upset 
                                        voice "voices/HUGO LINES/Hugo_Line4.wav"
                                        h "Then explain why you have a lamp in your hands little fairy and why you’re out of your cage."
                                        "I hesitantly lower the lamp that’s in my hands."
                                        "Awkward…"
                                        p "Uhh, I was simply inspecting it."
                                        show hugo smile
                                        voice "voices/HUGO LINES/Hugo_Line5.wav"
                                        h "Ha! You’re a bad liar! You had an opportunity and you flopped. I wonder how the Ringmaster favored such an idiot over me. It pisses me off."
                                        play music "FEAR.mp3"
                                        show hugo bad
                                        "He gets off the bed and towers over me. "
                                        
                                        voice "voices/HUGO LINES/Hugo_Line6.wav"
                                        h "Well it seems you've given me an opportunity of a lifetime, Pita. The circus will be mine again!"
                                         
                                        "Hugo struck me and I was met with darkness…"
                                        stop music fadeout 0.3
                                        play sound "audio/ear-ringing.mp3" fadein 0.3 volume 0.20 loop
                                        show blackscreen with Dissolve(1.0)
                                        jump hugopt2
    label badending:
        hide blackscreen
        stop channel1
        play music "FEAR.mp3"
        show hugo bad
        $ persistent.hugoBad_unlocked = True
        "I felt my neck be grasped and my body be lifted! I gasp and hyperventilate, clawing at the hand around my neck."
        voice "voices/HUGO LINES/Hugo_CommonBadEnding2.wav"
        h "I’m so happy that you gave me a reason to kill you."
        p "ghh- hk!"
        "{i}Stop it! Stop it!{/i}"
        "Is what I tried to say. His grip tightened, restricting my speech. My legs shake and I flail my hand, trying to claw at his face, but my hand slowly becomes limp. I was met with a sudden darkness and warmth that felt like freedom."
    
        jump death_screen

        return

    label prebadending:
        stop channel2 fadeout 1.0
        show hugo surprised
        voice "voices/HUGO LINES/Hugo_CommonBadEnding1.wav"
        h "What the?! What are you doing here?!"
        voice "voices/Pita VA Clips/Hugo/Pita_Hugo2.wav"
        p "Hugo?!-"
        play music "FEAR.mp3"
        jump badending

    label hugopt2: #keeping separate for organization
        hide hugo

        "..."
        "...."
        "....."
        stop sound fadeout 1.0
        scene blackscreen
        show chest hugo-trailer with Dissolve(1.0)
        "Where am I?"
        "The area I’m in is cramped and smells like strong wood."
        "I try moving, but I can only move the thing I’m inside of."
        "!!!"
        "I move more in panic and try to get a good look through the keyhole."
        "All I can see is the inside of Hugo’s trailer that is slightly lit from the morning glow."
        menu:
            "Panic!":
                "I scream loudly, hoping someone will find me and help me."
                "!!!"
                play sound "audio/door-creek.mp3"
                "Bed creaking can be heard nearby."
                "Crap-!"
                stop sound
                voice "voices/HUGO LINES/Hugo_Line7.wav"
                h "Are you serious? I thought I killed you, little fairy!"
                show chest eye
                voice "voices/HUGO LINES/Hugo_Line8.wav"
                h "I guess I need to finish the job~."
                show chest death_slideshow
                
                voice "voices/HUGO LINES/Hugo_Line9.wav"
                h "Die."
                #play neck crack sound
                
                "..."
                "Oh Lizard Man,"
                "I’m sorry I didn’t keep my promise…"
                jump death_screen

            "Keep Calm.":
                "I decided to stay quiet and think about how I’m going to get out of here."
                "Darn, if only I had my wand, I could shrink myself!"
                play sound "audio/door-creek.mp3"
                "!!!"
                "Hugo’s here! I can’t see him, I must be right next to his bed."
                # yawn sound
                stop sound
                voice "voices/HUGO LINES/Hugo_Line10.wav"
                h "Let’s get this over with."
                "I can feel myself and the chest I’m in being lifted off the ground."
                show chest carried
                "Where is he taking me?"
                #footsteps on wood floor + door opening and closing sound"
                
                play sound "audio/footsteps-dirt-gravel.mp3"
                "The sun is much brighter here. Is that-"
                stop sound
                show chest ringmaster
                voice "voices/HUGO LINES/Hugo_Line11.wav"
                h "Joseph!-I mean sir- What are you doing out so early?"
                voice "voices/RM VA clips/Hugo/ive_been_looking_for_pita.wav"
                rm "I’ve been looking for Pita! I checked her cage and she wasn’t there. The circus will be in shambles if we don’t find her now!"
                "He’s looking for me?!"
                "Maybe I should try something. I don’t know what Hugo plans on doing with me!"
                $ time = 5
                show screen qte(5, 'doNothing')
                menu:
                    "Plea for help!":
                        hide screen qte
                        #voice "voices/Pita VA Clips/Hugo/Pita_HelpMe.wav"
                        p "Help me! Ringmaster! Please, I’m in here!"
                        "I didn’t want to do this but I felt like I didn’t have much of a choice…"

                        voice "voices/HUGO LINES/HUGO VS RM/HugoRM_Line1.wav"
                        rm "Pita?! You lied to me and you have her in that chest?! Let her go, this instant, Hugo!"
                        "!!!"
                        show chest dropped
                        "I can feel the chest I’m inside of being dropped!"
                        #play thud then bangning sounds play sound ["thud", "bang"]
                        "I scream and I bang at the chest from the inside."

                        p "Let me out, dammit!"

                        voice "voices/HUGO LINES/HUGO VS RM/HugoRM_Line2.wav"
                        rm "How dare you treat her that way…"

                        voice "voices/HUGO LINES/HUGO VS RM/HugoRM_Line3.wav"
                        h "Do you even want to know why I have her in the chest? She was trying to kill me!"
                        
                        voice "voices/HUGO LINES/HUGO VS RM/HugoRM_Line4.wav"
                        h "She’s a danger to us, Joseph!"
                        
                        voice "voices/HUGO LINES/HUGO VS RM/HugoRM_Line5.wav"
                        rm "Such a poor excuse! Pita trying to kill you? She can’t even harm a fly in her state…"
                        
                        voice "voices/HUGO LINES/HUGO VS RM/HugoRM_Line6.wav"
                        rm "Well, I should’ve known you’d be like this with her too. I’m quite disappointed."
                        "..."
                        "There’s a moment of silence between the two."
                        voice "voices/HUGO LINES/HUGO VS RM/HugoRM_Line7.wav"
                        h "You’re the problem."
                        
                        voice "voices/HUGO LINES/HUGO VS RM/HugoRM_Line8.wav"
                        h "After everything we’ve done together, you choose her over your own people."
                        
                        voice "voices/HUGO LINES/HUGO VS RM/HugoRM_Line9.wav"
                        h "You won’t even give me a chance to explain."
                        
                        voice "voices/HUGO LINES/HUGO VS RM/HugoRM_Line10.wav"
                        h "That makes me think you treated him the same way! All of that for a damn mythical creature!"
                        
                        voice "voices/HUGO LINES/HUGO VS RM/HugoRM_Line11.wav"
                        rm "Now, now, don’t be an idiot, and make the same mistake, Hugo."
                        
                        voice "voices/HUGO LINES/HUGO VS RM/HugoRM_Line12.wav"
                        h "I’m not scared of you, old man!"

                        voice "voices/HUGO LINES/HUGO VS RM/HugoRM_BattleCry.wav"

                        show chest carried
                        voice "voices/HUGO LINES/HUGO VS RM/HugoRM_ShockGasp.wav"
                        rm "!!!"
                        #fighting sounds
                        voice "voices/HUGO LINES/HUGO VS RM/HugoRM_Line13.wav"
                        rm "You should’ve never crossed me, Hugo."
                        voice "voices/HUGO LINES/HUGO VS RM/HugoRM_Line14.wav"
                        rm "Say hello to Echo for me, would you?"
                        voice "voices/HUGO LINES/HUGO VS RM/HugoRM_Line15.wav"
                        
                        rm "I’m sure he’ll describe to you how I tortured him every night in his cage whilst his ignorant brother was in his trailer moping about a “mythical creature.”"
                        voice "voices/HUGO LINES/HUGO VS RM/HugoRM_Line16.wav"
                        h "Why?"
                        voice "voices/HUGO LINES/HUGO VS RM/HugoRM_Line17.wav"
                        h "WHY?!"
                        voice "voices/HUGO LINES/HUGO VS RM/HugoRM_Stabbed.wav"

                        # flesh being sliced sound then thud
                        #footsteps approaching
                        $ hugoIsAlive = False
                        "..."
                        hide chest with Dissolve(1.0)
                        
                        show ringmaster crackedmask #temp until rm cg is done
                        $ persistent.ringmasterCrackedMask_unlocked = True
                        "I gasp. His mask is broken…And he’s bloody. Did he… Kill Hugo?"
                        voice "voices/RM VA clips/Hugo/RM_HelloSweet.wav"
                        rm "Hello, sweetheart."
                        voice "voices/RM VA clips/Hugo/RM_Apologize.wav"
                        rm "I apologize for the wait."
                        voice "voices/RM VA clips/Hugo/RM_RuOK.wav"
                        rm "Are you okay?"
                        menu:
                            "No, my body aches.":
                                voice "voices/RM VA clips/Hugo/RM_PoorThing.wav"
                                rm "Ah, you poor thing. I’m sorry about that."
                                jump resume
                            "Ringmaster, he did terrible things!":
                                voice "voices/RM VA clips/Hugo/RM_DontWorryAbout.wav"
                                rm "Ah, don’t worry about him anymore. He’s just another idiot six feet under now."
                                jump resume
                            "Yeah, I’m fine.":
                                voice "voices/RM VA clips/Hugo/RM_Wonderful.wav"
                                rm "Ah, that’s wonderful. I’m glad he didn’t hurt you as bad as I thought."
                                jump resume
                            "Screw you!":
                                rm "Ah, well that’s no way to treat your savior." #NO VOICE LINE FOR
                                jump resume
                            "I’m fine… But,how did you do it?":
                                voice "voices/RM VA clips/Hugo/RM_BuiltInSword.wav"
                                rm "Remember the cane that I sometimes carry around? It has a built-in sword."
                                jump resume
                        label resume:
                            voice "voices/RM VA clips/Hugo/RM_AfterWhats.wav"
                            rm "After what’s happened, I promise I’ll protect you. Who knows who else would treat you just like how Hugo did." 
                            voice "voices/RM VA clips/Hugo/RM_HugoIsGone.wav"
                            rm "Hugo is gone, but I won’t have his death go to waste."
                            play music "tension.mp3" fadein 0.3 volume 0.5
                            show ringmaster hugohead
                            $ persistent.ringmasterHugoHead_unlocked = True
                            "He holds up Hugo's decapitated head" #TEMPORARY LINE UNTIL CG IS DONE
                            "!!!"
                            "Oh my…"
                            "I can’t breathe."
                            show ringmaster hugoteeth
                            $ persistent.ringmasterHugoTeeth_unlocked = True
                            voice "voices/RM VA clips/Hugo/RM_LookAt.wav"
                            rm "Look at all of those teeth! Aren’t they just delicious looking?"
                            "He places a finger on the decapitated head’s upper lip and he lifts it, revealing the upper teeth and gums better."
                            voice "voices/RM VA clips/Hugo/RM_WellYellow.wav"
                            rm "Well, they’re a little yellow from smoking but they’re surely edible."
                            #voice "voices/Pita VA Clips/Hugo/Pita_TheyAre.wav"
                            p "They are…"
                            "I reach towards the teeth but he smacks my hand away!"
                            voice "voices/RM VA clips/Hugo/RM_nuhuh.wav"
                            rm "Nah-ah-ahh~."
                            voice "voices/RM VA clips/Hugo/RM_CantHave.wav"
                            rm "You cannot have any of this yet."
                            show ringmaster crackedmask
                            "He lowers the head."
                            voice "voices/RM VA clips/Hugo/RM_INeedTo.wav"
                            rm "I need to move you and clean up some things first. You’re going to be staying with me from now on."
                            # play chest closing sound
                            hide ringmaster
                            show chest darkness
                            stop music fadeout 1.0
                            show blackscreen with Dissolve(1.0)
                            "I felt the chest I’m inside of being lifted and moved somewhere else."
                            "..."
                            "I’m in a new area now."
                            "“I’ll be back” is what he said to me before I was met with silence."
                            "..."
                            "...."
                            "How long has it been?"
                            "What is he doing?"
                            "What is he going to do with me?"
                            "Is it really better to be in his hands than it was to be in Hugo’s?"
                            "..."
                            "Eventually, he came back."
                            "I thought he was going to harm me when he opened the chest, but he just ended up putting me back in my cage."
                            "My cage is in his trailer now…"
                            scene cage-trailer with Dissolve(1.0)
                            show ringmaster
                            voice "voices/RM VA clips/Hugo/RM_Treat.wav"
                            rm "Here’s your treat. To be honest, I feel awful for letting you get hurt like that. Take it as an apology gift."
                            "He hands me over Hugo’s severed head."
                            "I stare at the head for a moment."
                            "I did hate the man and I feel a little bad for what happened to him, but I cannot refuse a meal in my condition."
                            "I take the head and begin plucking and eating Hugo’s teeth like how humans would with grapes."                         
                            "Delicious and a little smoky."
                            "..."
                            "I can feel his gaze on me as I eat."
                            #voice "voices/Pita VA Clips/Hugo/Pita_Rude2Stare.wav"
                            p "It's rude to stare."
                            "He stares at me for a brief moment longer."
                            "..."
                            "He turns away from me and he walks towards his desk."
                            hide ringmaster
                            voice "voices/RM VA clips/Hugo/RM_IKnow.wav"
                            rm "I know what you did. What you tried to do."
                            "He stares at the posters on his wall, having his back towards me."
                            if not marlonIsAlive or  not bonnieIsAlive:
                                voice "voices/RM VA clips/Hugo/RM_HugoWasRight.wav"
                                rm "You escaped your cage and ate their teeth. Hugo was right."
                                "He must’ve checked the trailers…"
                            else:
                                voice "voices/RM VA clips/Hugo/RM_YouEscaped2.wav"
                                rm "You escaped your cage. Were you that impatient that you couldn’t wait by the end of this week for your treat?"
                                voice "voices/RM VA clips/Hugo/RM_EvilIntent.wav"
                                rm "I know you wouldn’t go to his trailer without evil intent."
                                voice "voices/RM VA clips/Hugo/RM_ItsClear.wav"
                                rm "It’s clear you both hated each other."
                            "Crunch, crunch, crunch."
                            "I feel a surge of energy from the teeth I have eaten."
                            "I pluck the last tooth from Hugo’s mouth and carefully begin picking at the lock carefully like how I did with the other tooth I had in my possession earlier."
                            "I need to act fast!"
                            voice "voices/RM VA clips/Hugo/RM_WhateverDoesntMat.wav"
                            rm "Well, whatever you did doesn’t really matter to me. What really matters to me is if you’re willing to work with me."
                            "It is unlocked."
                            voice "voices/RM VA clips/Hugo/RM_PerfectStar.wav"
                            rm "All you need to do is listen and be my perfect star."
                            "He lightly caresses the poster that he has of me on his wall."
                            show ringmaster
                            "He turns around and approaches my cage whilst putting out his hand."
                            voice "voices/RM VA clips/Hugo/RM_whaddyaSay.wav"
                            rm "Whaddya say?"
                            if not marlonIsAlive and not bonnieIsAlive and not hugoIsAlive:
                                menu: 
                                    "No.":
                                        
                                        "I swing open the cage and I step out of it as I scowl at him."
                                        scene ringmaster-trailer
                                        show ringmaster
                                        voice "voices/RM VA clips/Hugo/RM_HOW.wav"
                                        rm "How?-"
                                        #voice "voices/Pita VA Clips/Hugo/Pita_NeverWorkW.wav"
                                        p "I’ll never work with you!"
                                        jump killing_rm
                                        
                                    "Yes.":
                                        "I swing open the cage and I step out of it while grinning at him."
                                        scene ringmaster-trailer
                                        show ringmaster
                                        voice "voices/RM VA clips/Hugo/RM_Gasp.wav"
                                        "He gasps" #Temp line
                                        jump rm_teamup
                            else:
                                "My hands are shaking…"
                                "I don’t feel strong enough to go up against him." 
                                "I don’t want to be stabbed next!"
                                "I lower my head... and hesitantly take his hand..."
                                stop music fadeout 0.3
                                #voice "voices/Pita VA Clips/Hugo/Pita_FineObey.wav"
                                p "Fine, I’ll obey."
                                "..."
                                voice "voices/RM VA clips/Hugo/RM_GoodGirl.wav"
                                rm "That’s my good girl…"
                                show blackscreen
                                with Fade(1.0, 4.0, 0.5)
                    "Do Nothing":
                        label doNothing:
                            hide screen qte
                            voice "voices/HUGO LINES/Hugo_Line12.wav"
                            h "She’s most likely gone by now if she escaped last night, and well c’mon you didn’t mean that. We were doing just fine before she showed up and ruined everything. We don’t need her."
                            voice "voices/RM VA clips/Hugo/dontbedaft.wav"
                            rm "Wow, don’t be so daft…Without my Pita, we are nothing. You’re nothing!"
                            voice "voices/RM VA clips/Hugo/jealous.wav"
                            rm "Get it through your thick skull that she is the star now. You should know better than to be jealous."
                            voice "voices/HUGO LINES/Hugo_Line13.wav"
                            h "Tch!"
                            voice "voices/RM VA clips/Hugo/whylug.wav"
                            rm "Hm, now,-why are you still lugging around that chest? Put it down and come help me."
                            voice "voices/HUGO LINES/Hugo_Line14.wav"
                            h "Yes, Sir"
                            "!!!"
                            "I felt myself being lowered."
                            stop sound fadeout 1.0
                            show chest carried
                            "Ah finally, they’re all gone!"
                            "I must find a way out of this chest."
                            "I scratch at the keyhole and bang at the wood."
                            "No! No!"
                            "I try pushing up the chest’s top by force."
                            "Nothing."
                            play sound "audio/footsteps-dirt-gravel.mp3" fadein 1.0 
                            show chest darkness
                            "!!!"
                            "No!"
                            stop sound
                            voice "voices/HUGO LINES/Hugo_Line7.wav"
                            h "Aw, trying to get out? Well, that’s too bad."
                            "I can feel the chest I’m inside of being lifted again."
                            show chest carried
                            play sound "audio/footsteps-dirt-gravel.mp3" loop
                            "He’s been walking for a bit."
                            "Where is he taking me?"
                            #voice "voices/Pita VA Clips/Hugo/PIta_WhatAreUGoing.wav"
                            p "What are you going to do with me?!"
                            # play heartbeat sounds
                            "My heart pounds rapidly in my chest."
                            voice "voices/HUGO LINES/Hugo_Line16.wav"
                            h "I’m going to do what I should have done a long time ago."
                            "!!!"
                            stop sound
                            "I can feel the chest I’m inside of being dropped!"
                            #play thud sound
                            show chest dropped
                            "I groaned as the impact made my body ache."
                            "I peek out of the keyhole, in search of my whereabouts, but all I could see was dirt."
                            voice "voices/HUGO LINES/Hugo_Line17.wav"
                            h "Thanks again for easily giving me the chance of avenging my brother and myself, little fairy. All you did was ruin everything... Goodbye."
                            "I can hear something being thrown at the chest I’m in. It smells like dirt."
                            show chest dirt
                            "My vision eventually goes dark and I can’t breathe as much anymore."
                            show chest darkness with Dissolve(1.0)
                            "I thrash at the chest from the inside."
                            "I need to get out!"
                            "I need to get out!"
                            "I need…to get…"
                            "Out…"
                            jump death_screen