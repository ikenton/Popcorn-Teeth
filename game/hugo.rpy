define h = Character("Hugo", color = "#FFFF00")
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


label global_hugoVendetta:
    $ timer_range = 0
    $ timer_jump = 0
    play music "tension.mp3" fadein 3.0
    "I look over and quietly approach the red and flashy trailer with many posters from past shows on it. I don’t seem to be on any of them."
    "I can see smoke coming from behind the trailer and humming. I cock my head with curiosity."
    "Who could it be?"
    menu:
        "Leave":
            jump global_courtyard
        "Take a peek":
            "I place my dainty hand on the trailer and slowly poke my head out."
            "Oh I know who it is."
            show hugo back
            "I can see the back of that mean clown, humming and smoking."
            "Ugh, I hate Hugo… he’d press his cigarette butts onto my skin till I could smell my own skin and he’d bad mouth me backstage. I get that he never wanted me here, but I also never wanted to be here!"
            "Oh!"
            "I look beside him and I spot a rusty foldable table next to him that has a toolbox and a half eaten sandwich on top of it. hmm…"
            "!!!"
            show hugo angry
            "Hugo drops his cigarette and stomps on it."
            "Crap!"
            #timer
            $ time = 5
            $ timer_range = 5
            $ timer_jump = 'badending'
            show screen countdown
            menu:
                "Hide!":
                    hide screen countdown
                    hide hugo angry
                    show pita underneath
                    "I quickly hide underneath the trailer and I pull my white dress with me so it isn’t poking out, getting it dirty in the process. I place my hand on my mouth as I watch Hugo walk to his trailer and go up the creaky steps. I can hear keys jingle."
                    
                    #timed
                    
                    $ time = 5
                    $ timer_range = 5
                    $ timer_jump = 'wait'
                    show screen countdown
                    menu:
                        "Go Now":
                            hide screen countdown
                            hide pita underneath
                            scene pt-hugo-trailer
                            stop sound fadeout 1.0
                            "I crawl out of the trailer and I stand up, hunching as I approach behind Hugo. I go up one of the steps and it creaks."
                            "!!!"
                            show hugo back 
                            "Hugo‘s head snaps in my direction."
                            show hugo surprised
                            h "What the?! What are you doing here?!"
                            p "Hugo?!-"
                            jump badending
                        "Wait":
                            hide screen countdown
                            label wait:
                                "I lay there under the trailer. I could hear Hugo walking inside the trailer."
                                "I remember seeing the toolbox behind the trailer. Maybe there’s something in there that I can use. I crawl out from under the trailer and I stand up. I don't bother dusting off my dress and I quietly go behind the trailer."
                                hide pita underneath
                                "I open the toolbox and go through it. I find a rusty hammer, or is that blood on it? I hold it in my hand and it feels oddly heavy."
                                "I didn’t realize I’ve become this weak…"
                                "*Sighs*"
                                "I’ll regain all my strength soon. C’mon, I got this, Pita!"
                                "I look around and find an open window. I smile and climb my way into the trailer quietly. I can hear gentle snoring coming from the bedroom area of the trailer."
                                "I hold the hammer with both hands and slowly approach the source of the noise."
                                scene pt-hugo-trailer
                                stop sound fadeout 1.0
                                "I poke my head in and view a resting Hugo with his arms behind his head and his legs crossed. It seems that he’s napping…"
                                "Perfect"
                                show hugo hammer
                                $ hugoIsAlive = False
                                "I raise the hammer above my head and strike it down onto Hugo’s face repeatedly."
                                p "Hehe—-HEHEHEH!"
                                stop music fadeout 2.0
                                "The adrenaline and euphoria embody my very soul to the brim as I hear his bones crack and flesh squelch every time I bring down the hammer."
                                "I drop the hammer to the ground and begin picking at the teeth and other skull fragments from the disfigured face. I popped them into my mouth like how humans eat chips and chew with saliva and blood dripping from my jaw."
                                hide hugo hammer
                                p "Mmm"
                                "I finish and wipe my mouth."
                                "I’ve made quite a mess."
                                "I wipe the blood off myself with Hugo’s blankets and I bend down to look for the hammer."
                                "I look under the bed and see the hammer’s head separated from the handle."
                                p "Crap"
                                "I stand back up straight and look at the trailer’s door. I need more."
                                "I leave the trailer and head back to the courtyard."
                                jump global_courtyard
                "Throw a pebble":
                    hide screen countdown
                    "I look down and grab a pebble off the ground. This should get 'em distracted!"
                    show hugo angry
                    h "Who’s there?!"
                    "He approaches the sound where the pebble was."
                    "Perfect! This is my chance. I approach Hugo quickly and quietly from behind. I bump into him in an attempt to knock him over but he barely budged! "
                    show hugo surprised
                    "Hugo turns around and looks down at me."
                    h "What the?! What are you doing here?!"
                    p "Hugo?!-"
                    jump badending
        "Wait and listen":
            "I dare not to take any chance of making myself known yet…I wait and listen for a while. After a moment,the humming stops and I can hear footsteps approaching!"
            #timed
            $ time = 5
            $ timer_range = 5
            $ timer_jump = 'prebadending'
            show screen countdown
            menu:
                "Hide!":
                    hide screen countdown
                    show pita underneath
                    "I quickly hide underneath the trailer and I pull my white dress with me so it isn’t poking out, getting it dirty in the process. I place my hand on my mouth as I watch Hugo walk to his trailer and go up the creaky steps. I can hear keys jingle."
                    $ time = 5
                    $ timer_range = 5
                    $ timer_jump = 'wait2'
                    show screen countdown
                    menu: #timed
                        "Go Now":
                            hide screen countdown
                            hide pita underneath
                            "I crawl out of the trailer and I stand up, hunching as I approach behind Hugo. I go up one of the steps."
                            "Creeeak"
                            "!!!"
                            "Hugo suddenly turns around"
                            show hugo surprised
                            h "What the?! What are you doing here?!"
                            p "Hugo?!-"
                            jump badending
                        "Wait":
                            hide screen countdown
                            label wait2:
                                "I lay there under the trailer. I could hear Hugo walking inside the trailer."
                                "Oh! I look up and notice a trapdoor, I can see a square outline of the light coming from inside the trailer. I grin and I wait for some minutes until I can barely hear any movement coming from inside the trailer."
                                "I slightly push up the trapdoor and it opens."
                                scene pt-hugo-trailer
                                stop sound fadeout 1.0
                                hide pita underneath
                                "I grin and I enter the trailer though the trapdoor as quietly as I can."
                                "I scan my surroundings and see Hugo in bed, facing the wall. lowering my head, I quietly approach him. Eventually, I  get close enough to him and I look around for a weapon. I grab the base of a lamp with both of my hands."
                                
                                "Hugo turns his body towards me and jumps."
                                show hugo surprised
                                h "Are you trying to kill me?"
                                menu:
                                    "Yes":
                                        "I immediately strike down the lamp onto Hugo’s head."
                                        "He catches it in  midair. I gasp and let go of the lamp. I grit my teeth."
                                        "Desperate, I strike at his face with my fingernails, drawing some blood. He recoils and screams. He wipes his face and notices the blood on his fingertips. He then looks at me with a sinister grin."
                                        h "Look what we have here. The fairy’s giving me an opportunity of a lifetime!"
                                        "He swings the lamp towards me-"
                                        show blackscreen
                                        "..."
                                        "I was met with a sudden darkness and warmth that felt like freedom."

                                    "No":
                                        "Hugo sits up on the bed and stares at me."
                                        show hugo upset 
                                        h "Then explain why you have a lamp in your hands little fairy and why you’re out of your cage."
                                        "I hesitantly lower the lamp that’s in my hands."
                                        "Awkward…"
                                        p "Uhh, I was simply inspecting it"
                                        h "Ha! You’re a bad liar! You had an opportunity and you flopped. I wonder how the Ringmaster favored such an idiot over me. It pisses me off"
                                        "He gets off the bed and towers over me. "
                                        show hugo smile
                                        h "The circus will be mine again!"
                                        "I drop the lamp."
                                        jump badending
    label badending:
        play music "FEAR.mp3"
        show hugo bad
        "I felt my neck be grasped and my body be lifted! I gasp and hyperventilate, clawing at the hand around my neck."
        h "I’m so happy that you gave me a reason to kill you."
        p "ghh- hk!"
        "{i}Stop it! Stop it!{/i}"
        "Is what I tried to say. His grip tightened, restricting my speech. My legs shake and I flail my hand, trying to claw at his face, but my hand slowly becomes limp. I was met with a sudden darkness and warmth that felt like freedom."
        show blackscreen
        return

    label prebadending:
        show hugo surprised
        h "What the?! What are you doing here?!"
        p "Hugo?!-"
        jump badending

    