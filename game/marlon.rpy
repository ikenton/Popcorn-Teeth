# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Marlon", color = "#6380e0", voice_tag = "m")
define p = Character("Pita", color = "#edf4b3", voice_tag="p")
define rm = Character("Ringmaster", color = "#ff0000", voice_tag="rm")
default crimsonhere = True

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

label global_visitMarlon:
    $ timer_range = 0
    $ timer_jump = 0
    $ bad = 0

    #if pita has already visited
    
    
    "I think it’s time to stop by Marlon’s trailer."
    
    "I head towards Marlons’s trailer, which is hard to see since it’s surrounded by cages filled with other circus animals. Bears, tigers, horses, monkeys, and even sea lions… All trapped here, just like me."
   
    "I guess there’s no point in being sneaky, since as soon as I get close enough to the cages, the animals start stirring and making loud noises, banging on their bars and reaching out to grab me."

    show marlon surprised at right
    show crimson at left
    $ persistent.marlonNuetral_unlocked = True
    $ persistent.marlonHappy_unlocked = True
    $ persistent.marlonSuprised_unlocked = True
    $ persistent.marlonSad_unlocked = True
    $ persistent.marlonDisapointed_unlocked = True
    $ persistent.marlonAngry_unlocked = True
    $ persistent.crimson_unlocked = True
    $ persistent.marlonChibi_unlocked = True
    $ persistent.marlonPoster_unlocked = True
    if renpy.music.is_playing:
        play music "tension.mp3" volume 0.5
    else:
        play music "tension.mp3" fadein 3 volume 0.5
    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Marlon_Line1.wav"
    m "I-Is someone there?"

    "I see Marlon, the circus’ animal trainer and performer. He’s standing in front of his trailer with a lion by his side, whip in one hand as he works with the animal."

    "His eyes land on me and immediately his expression changes, looking somewhat relieved."
    show marlon happy
    show marlon disapointed
    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Marlon_Line2.wav"
    m "O-Oh, it’s just you, Pita..."

    show marlon surprised
    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Marlon_Line3.wav"
    m "Wait a minute! H-How did you get out of your cage?"

    menu:
        "Don't worry about it.":
            p "Don’t worry too much about it, I just wanted to come speak with you."
            show marlon disapointed
            voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/_Don_t_worry_about it_/Marlon_Line1.wav"
            m "O-Oh, okay..."
        "The Ringmaster let me out.":
            p "The Ringmaster let me out of my cage so that I can come speak with you."
            show marlon disapointed
            voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/_The RM let me out_/Marlon_Line1.wav"
            m "O-Oh, I see..."
    
    "Out of all the other performers in the Circus, Marlon has always been the nicest to me. But even then, that isn’t saying a lot…"
    "He, like the other performers, still thinks that my suffering is worth it if it means keeping the Circus alive and functioning. As long as the Ringmaster makes money off of my pain, my existence… then the others will continue to think less of me."

    p "What are you still doing out here? Our performance ended hours ago."
    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Marlon_Line4.wav"
    m "Oh, w-well…"
    m "The Ringmaster said my performance tonight was… lackluster. He needs it to be more engaging and more… dangerous…"

    "He looks towards his lion with a strange sadness, looking at the whip in his hand with a clenched fist before petting his lion with his other hand."
    show marlon happy
    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Marlon_Line5.wav"
    m "Let’s head inside my trailer, my animals are being too noisy right now…"
    scene pt-marlon-trailer
    stop channel1
    stop channel2
    $ persistent.marlonTrailer_unlocked = True
    stop sound fadeout 1.0
    show marlon nuetral at right
    show crimson at left
    "Marlon leads me into his trailer along with his lion. The lion looks up to me and bares its teeth, growling."

    #thinking
    "{i}Hm, killing Marlon might be a problem if his lion is still here…{/i}"

    p "Does your lion have to come inside with us?"

    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Marlon_Line1.wav"
    m "Oh, sorry about him… Crimson is very protective of me since I rescued him as a cub."

    "{i}Looks like I’ll have to find a way to get rid of his lion before I kill Marlon and eat his teeth.{/i}"

    "As I settle myself into Marlon’s trailer, I take a moment to glance around at my surroundings." 
    "His trailer is left plain with no notable decorations. There’s nothing displayed on any of the shelves, and the only thing interesting about the trailer was the animal fur rug on the floor."
    "One thing that caught my eye was a single portrait hanging on what is otherwise a barren wall. At a glance, I can’t help but feel like the man in the portrait looked really familiar."

    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Marlon_Line2.wav"
    m "So, you said you wanted to talk to me about something…?"
    
    $ performance = True
    $ closeCrimson = True
    $ ringmaster = True
    $ lizardboy = True
    $ attempted = False

    menu talking:
        
        "What happened with the performance tonight?" if performance:
            $ performance = False
            p "You mentioned something about the performance tonight. What happened exactly?"

            "Marlon looks away from me for a moment and glances back to Crimson, who reassures him with a growl."

            show marlon disapointed
            voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_What happened with the performance tonight_/Marlon_Line1.wav"
            m "I was performing the same tricks I always do with my animals…"

            voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_What happened with the performance tonight_/Marlon_Line2.wav"
            m "My monkey walks across the tightrope, my sea lion balances on a bouncy ball, my elephant performs with musical instruments…"
            voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_What happened with the performance tonight_/Marlon_Line3.wav"
            m "But the Ringmaster said it wasn’t enough… He said my acts are getting “boring” and if I don’t improve it soon, he will…"

            "He trails off and looks up at me with a tortured expression."
            
            show marlon angry
            voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_What happened with the performance tonight_/Marlon_Line4.wav"
            m "He wants me to perform with Crimson, but I can’t bring myself to hurt him."

            p "Perform with him how?"

            voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_What happened with the performance tonight_/Marlon_Line5.wav"
            m "He wants him to “attack” me, and then I have to defend myself and tame him…"

            "His grip tightens on the whip in his hand."
            
            show marlon disapointed
            voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_What happened with the performance tonight_/Marlon_Line6.wav"
            m "But he won’t attack me! He won’t even pounce at me or do anything dangerous… He’s just too attached to me…"

            voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_What happened with the performance tonight_/Marlon_Line7.wav"
            m "And I can’t even hurt him if I wanted to…"
            
            menu:
                "What are you going to do?":
                    #voice "voices/Pita VA Clips/Pita_SoWhat.wav"
                    p "So what are you going to do? You know how the Ringmaster is, if you don’t do as he says, he’ll punish you."
                    show marlon disapointed

                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_What happened with the performance tonight_/_What are you going to do_/Marlon_Line1.wav"
                    m "I… I don’t know…"
                    show marlon nuetral

                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_What happened with the performance tonight_/_What are you going to do_/Marlon_Line2.wav"
                    m "If I don’t do what the Ringmaster says, he’ll probably lock me up like you and make me a sideshow freak…"
                    
                    show marlon sad
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_What happened with the performance tonight_/_What are you going to do_/Marlon_Line3.wav"

                    m "Just like…"
                    "Marlon trails off again then glances up at the photo on the wall. He then shakes his head and turns back to me."
                    show marlon nuetral

                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_What happened with the performance tonight_/_What are you going to do_/Marlon_Line4.wav"
                    m "I can’t let that happen."
                "Sounds like you’re in trouble.": #BAD
                    $ bad += 1
                    p "Well, it looks like you’re in a lot of trouble."
                    show marlon angry
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_What happened with the performance tonight_/_Sound_s like you_re in trouble_/Marlon_Line1.wav"
                    m "Don’t you think I know that?"

                    show marlon nuetral
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_What happened with the performance tonight_/_Sound_s like you_re in trouble_/Marlon_Line2.wav"
                    m "If I don’t figure out this act, the Ringmaster might take Crimson away from me. My only friend."
                    
                    show marlon disapointed
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_What happened with the performance tonight_/_Sound_s like you_re in trouble_/Marlon_Line3.wav"
                    m "I can’t lose her… I can’t lose anyone again. Not like…"
                    "Marlon trails off again then glances up at the photo on the wall. He then shakes his head and turns back to me."
                    show marlon nuetral
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_What happened with the performance tonight_/_Sound_s like you_re in trouble_/Marlon_Line4.wav"
                    m "I can’t let that happen."
            $ choice1 = True
            jump talking
        "So you and Crimson must be quite close." if closeCrimson:
            $ closeCrimson = False
            p "I can see that you and your pet lion are quite close."
            show marlon angry
            voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_So you and Crimson must be quite close_/Marlon_Line1.wav"
            m "Crimson is not just my pet, he’s my friend."

            show marlon nuetral
            voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_So you and Crimson must be quite close_/Marlon_Line2.wav"
            m "But yes, he and I are very close."
            p "You mentioned that you rescued him, what did you mean?"

            show marlon happy
            voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_So you and Crimson must be quite close_/Marlon_Line3.wav"
            m "Oh yes…"
            show marlon nuetral
            voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_So you and Crimson must be quite close_/Marlon_Line4.wav"
            m "When I first joined the Circus, I already started training the animals that the Ringmaster kept here. Before me, the Ringmaster was the one who performed with them."
            
            voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_So you and Crimson must be quite close_/Marlon_Line5.wav"
            m "I was young then, but on one of our trips, we found a lion cub that ran away from a zoo."

            show marlon disapointed
            voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_So you and Crimson must be quite close_/Marlon_Line6.wav"
            m "The Ringmaster wanted to… dispose of it. A young lion cub is not as profitable as other animals, he said."
            
            show marlon nuetral
            voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_So you and Crimson must be quite close_/Marlon_Line7.wav"
            m "But I was able to convince him to keep it, and I named him Crimson."

            show marlon disapointed
            voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_So you and Crimson must be quite close_/Marlon_Line8.wav"
            m "The Ringmaster once said that one day, I need to perform with him, and he didn’t like our show, well…"

            voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_So you and Crimson must be quite close_/Marlon_Line9.wav"
            m "He’ll do what he wanted to do when we first found Crimson."

            menu:
                "What’s it like being friends with a lion?":
                    p "You must feel very grateful to have a lion as a friend. What’s it like?"
                    show marlon happy
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_So you and Crimson must be quite close_/Subchoices/_What_s it like being friends with a lion_/Marlon_Line1.wav"
                    m "Oh, it’s really great."

                    show marlon nuetral
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_So you and Crimson must be quite close_/Subchoices/_What_s it like being friends with a lion_/Marlon_Line2.wav"
                    m "Lions may be dangerous predators, but if you grow up with one, they treat you like part of their pride."
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_So you and Crimson must be quite close_/Subchoices/_What_s it like being friends with a lion_/Marlon_Line3.wav"
                    m "Crimson here sees me as one of his own, so he would never try to hurt me, ever."
                    show marlon disapointed
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_So you and Crimson must be quite close_/Subchoices/_What_s it like being friends with a lion_/Marlon_Line4.wav"
                    m "That’s why it’s kind of hard to perform with him like the Ringmaster wants us to…"
                    show marlon happy
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_So you and Crimson must be quite close_/Subchoices/_What_s it like being friends with a lion_/Marlon_Line5.wav"
                    m "Here, do you want to try and feed him? That way you can see how nice he really is."
                    "Marlon walks over to a cupboard in his trailer and opens the door, putting out a small bag of treats called “Steak Bites.”"
                    show crimson purr
                    $ persistent.crimsonPurr_unlocked = True
                    "As soon as the treats come out, Crimson lets out a purr of anticipation."
                    play sound "CrimsonPurr.mp3"
                    "Marlon takes two treats out and hands one to me."
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_So you and Crimson must be quite close_/Subchoices/_What_s it like being friends with a lion_/Marlon_Line6.wav"
                    m "Here, watch this."
                    show marlon nuetral
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_So you and Crimson must be quite close_/Subchoices/_What_s it like being friends with a lion_/Marlon_Line7.wav"
                    show crimson
                    m "Crimson, sit."
                    #show crimson
                    "Like a dog, Crimson sits like Marlon commands."
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_So you and Crimson must be quite close_/Subchoices/_What_s it like being friends with a lion_/Marlon_Line8.wav"
                    m "Good, now roll over!"
                    play sound "CrimsonPurr.mp3" 
                    "The large cat gets on the floor and rolls around on the animal fur rug."
                    "{i}Heh, cute{/i}"
                    show marlon happy 
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_So you and Crimson must be quite close_/Subchoices/_What_s it like being friends with a lion_/Marlon_Line9.wav"
                    m "See? He’s a very sweet boy."
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_So you and Crimson must be quite close_/Subchoices/_What_s it like being friends with a lion_/Marlon_Line10.wav"
                    m "Did you want to try?"
                    p "Uh, sure…"
                    menu:
                        "Sit":
                            p "Alright, sit."
                            #show crimson 
                            "Crimson looked at me cautiously, but eventually he sat."
                        "Roll over.":
                            p "Alright, roll over."
                            #show crimson 
                            play sound "CrimsonPurr.mp3" 
                            "Crimson looked at me cautiously, but eventually he rolled over on the floor."
                        "Play dead":
                            p "Alright, play dead."
                            #show crimson 
                            "Crimson looked at me cautiously, but eventually he laid down on the ground belly up."
                        "Speak.":
                            p "Alright, speak."
                            #show crimson 
                            play sound "CrimsonRoar.mp3"
                            "Crimson looked at me cautiously, but eventually he let out a loud roar that filled the trailer."
                    show marlon happy
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_So you and Crimson must be quite close_/Subchoices/_What_s it like being friends with a lion_/Marlon_Line11.wav"
                    m "Good boy, Crimson! Now give him his treat."
                    show crimson purr
                    "I hand over the treat to the lion who very carefully takes it from me for devouring it."
                    play sound "CrimsonPurr.mp3" 
                    show crimson
                    "{i}So the lion really likes these treats, huh? Maybe I can use that to distract him somehow so I can get Marlon alone.{/i}"
                "Maybe the lion deserves it.": 
                    #BAD
                    $ bad += 1
                    p "That’s understandable. After all, a lion can still be very dangerous."
                    show marlon angry
                    #play sound "CrimsonGrowl.mp3" #voice line will not play with growl in background for some reason will need to fix
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_So you and Crimson must be quite close_/Subchoices/_Maybe the lion deserves it._/Marlon_Line1.wav"
                    m "You don’t know anything about Crimson."
                    show marlon nuetral
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_So you and Crimson must be quite close_/Subchoices/_Maybe the lion deserves it._/Marlon_Line2.wav"
                    m "Lions may be dangerous predators, but if you grow up with one like I did, they treat you like part of their pride."
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_So you and Crimson must be quite close_/Subchoices/_Maybe the lion deserves it._/Marlon_Line3.wav"
                    m "Crimson here sees me as one of his own, so he would never try to hurt me, ever."
                    show marlon disapointed
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_So you and Crimson must be quite close_/Subchoices/_Maybe the lion deserves it._/Marlon_Line4.wav"
                    m "As much as you would think, I can’t get him to act dangerously around me like the Ringmaster wants…"
                    show marlon nuetral
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_So you and Crimson must be quite close_/Subchoices/_Maybe the lion deserves it._/Marlon_Line5.wav"
                    m "I can show you just how tame and friendly he is with some of his favorite treats."
                    "Marlon walks over to a cupboard in his trailer and opens the door, putting out a small bag of treats called “Steak Bites.”"
                    play sound "CrimsonPurr.mp3"
                    show crimson purr
                    "As soon as the treats come out, Crimson lets out a purr of anticipation."
                    "Marlon takes two treats out and hands one to me."
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_So you and Crimson must be quite close_/Subchoices/_What_s it like being friends with a lion_/Marlon_Line6.wav"
                    m "Here, watch this."
                    show crimson
                    show marlon nuetral
                    m "Crimson, sit."
                    #show crimson
                    "Like a dog, Crimson sits like Marlon commands."
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_So you and Crimson must be quite close_/Subchoices/_Maybe the lion deserves it._/Marlon_Line6.wav"
                    m "Good, now roll over!"
                    play sound "CrimsonPurr.mp3"
                    show crimson purr
                    "The large cat gets on the floor and rolls around on the animal fur rug."
                    show marlon angry
                    show crimson
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_So you and Crimson must be quite close_/Subchoices/_Maybe the lion deserves it._/Marlon_Line8.wav"
                    m "See? He’s not as dangerous as he looks."
                    "{i}So the lion really likes these treats, huh? Maybe I can use that to distract him somehow so I can get Marlon alone.{/i}"
            jump talking
        #if choice 1 is finished
        "Who’s the man in that photo?" if not performance and lizardboy:
            $ lizardboy = False
            p "I noticed that you kept looking at that photo on the wall. Who is that?"
            show marlon surprised
            "Marlon looks at me with quiet disbelief. Then, his eyes are cast to the side as he answers."
            show marlon disapointed
            voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_Who_s the man in that photo_/Marlon_Line1.wav"
            m "I can’t believe you don’t remember him… Even though he spent his last few days next to your cage…"
            "All of a sudden, I remembered something. Or someone."
            "A man with red hair and green scales, who sat quietly in a cage next to mine. He rarely spoke, and when he did, his voice was hoarse and gravelly."
            "Like me, the Ringmaster treated him with little respect. He would always threaten to “put more scales on him” if he misbehaved."
            "I can recall one night, there was screaming. A lot of screaming. I remember just being annoyed, wishing the noise would stop. And it did. Dead quiet."
            "The next day, the man was in his cage, but he wasn’t moving."

            p "The Lizard Man? Huh…"
            p "He looks so… happy in that picture…"
            voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_Who_s the man in that photo_/Marlon_Line2.wav"
            m "Yes, for a while, he and I were happy…"
            show marlon angry
            voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_Who_s the man in that photo_/Marlon_Line3.wav"
            m "But then the Ringmaster took that away from me."
            $ time = 7
            show screen qte(7, 'lizard_wrong')
            menu:
                "His act wasn’t very good anyway.":
                    label lizard_wrong:
                        hide screen qte
                        $ bad += 1
                        show marlon angry
                        voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_Who_s the man in that photo_/Bad Subchoices/Marlon_Line1.wav"
                        m "I wouldn’t expect you to sympathize. You’re the Ringmaster’s favorite little toy."
                        voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_Who_s the man in that photo_/Bad Subchoices/Marlon_Line2.wav"
                        m "You’re just some fairy tale. A spectacle for others to look at."
                        show marlon disapointed
                        voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_Who_s the man in that photo_/Bad Subchoices/Marlon_Line3.wav"
                        m "Meanwhile, I and the rest of the Circus work day and night on our performances with barely any recognition from the Ringmaster."
                        voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_Who_s the man in that photo_/Bad Subchoices/Marlon_Line4.wav"
                        m "He did, too. He could bend and twist his body in impossible ways, but that was never enough for the Ringmaster or the rest of the Circus."
                        show marlon angry
                        voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/_Who_s the man in that photo_/Bad Subchoices/Marlon_Line5.wav"
                        m "Sometimes I think you deserve that fate more than he did."
                "He died screaming in his cage.":
                    jump lizard_wrong
                "He didn’t deserve that fate.":
                    # no voice lines
                    hide screen qte
                    show marlon surprised
                    m "O-oh."
                    show marlon disapointed
                    "He looks off to the side again, avoiding eye contact as he speaks."
                    m "Y-you’re the only one who thinks that… Besides me, of course."
                    show marlon nuetral
                    m "The rest of the Circus always said he was a waste of time and space. They said no one wanted to watch him bend or twist his body in impossible ways."
                    show marlon happy
                    m "But I always thought he was talented. He was also sweet and thoughtful. He told some great jokes, too. Better than Hugo’s."
                    p "What was his name?"
                    "Marlon paused for a moment, taking one more glance to the portrait on the wall before smiling to himself."
                    m "Echo"
                    $ persistent.marlonEchoKiss_unlocked = True
                    $ persistent.echoPoster_unlocked = True
                    $ persistent.echo_unlocked = True
                    $ persistent.marlonPregante_unlocked = True
                    $ persistent.mecho_unlocked = True
                    $ persistent.maidEcho_unlocked = True
                "Really? You and him?":
                    hide screen qte
                    $ bad += 1
                    jump lizard_wrong
            jump talking
        "How close are you to the Ringmaster?" if not closeCrimson and ringmaster:
            $ ringmaster = False
            p "It sounds like you’re pretty close to the Ringmaster."
            show marlon nuetral
            voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/HowClose/Marlon_Line1.wav"
            m "I’ve been a part of this Circus since I was kid, and I always looked up to him."
            show marlon happy
            voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/HowClose/Marlon_Line2.wav"
            m "He was always so charismatic and intelligent. It was hard not to admire him, especially growing up."
            show marlon disapointed
            voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/HowClose/Marlon_Line3.wav"
            m "But now that I’m older… There are some things about him that I’ve grown to despise."
            voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/HowClose/Marlon_Line4.wav"
            m "I see how he treats other people, those who are less than him. I thought we were close, but he treats me badly, too."
            show marlon angry
            voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/HowClose/Marlon_Line5.wav"
            m "But you’re his favorite. He loves your act and even made you the mascot of the Circus."
            p "That’s not true. I hate him as much as you do."
            show marlon disapointed
            voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/HowClose/Marlon_Line6.wav"
            m "“Hate” is a strong word, but…"
            "Marlon takes another look at the portrait on the wall."
            menu:
                "Seriously, after all he’s done?": #bad choice
                    $ bad += 1
                    #voice "voices/Pita VA Clips/Pita_UrWeak.wav"
                    p "Seeing how he treats all his performers, I’m surprised you can even tolerate him. You’re just weak."
                    show marlon surprised
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/HowClose/_Seriously after all he_s done_/Marlon_Line1.wav"
                    m "W-what did you just say…?"
                    show marlon angry
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/HowClose/_Seriously after all he_s done_/Marlon_Line2.wav"
                    m "The Ringmaster may… act the way he does, but he does plenty for the Circus!"
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/HowClose/_Seriously after all he_s done_/Marlon_Line3.wav"
                    m "He provides us food and shelter… He gives us guidance when we need it the most…"
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/HowClose/_Seriously after all he_s done_/Marlon_Line4.wav"
                    m "He’s even the most talented performer in the Circus– no, in the world! You just haven’t seen it for yourself…"
                    show marlon disapointed
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/HowClose/_Seriously after all he_s done_/Marlon_Line5.wav"

                    m "Only a few lucky ones have…"
                    #voice "voices/Pita VA Clips/Pita_Brainwashed.wav"
                    p "Ugh, I can’t believe how brainwashed you are. You can’t even see how messed up he is!"
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/HowClose/_Seriously after all he_s done_/Marlon_Line6.wav"

                    show marlon angry
                    m "JUST SHUT UP!"

                    "As Marlon yells, Crimson gets up next to him and starts to growl. I have never seen him get so angry before…"

                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/HowClose/_Seriously after all he_s done_/Marlon_Line7.wav"
                    m "You don’t understand anything."

                    "Marlon stares at me with a venom behind his eyes. He heaves heavily before finally taking a deep breath to calm himself down."

                    show marlon nuetral
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/HowClose/_Seriously after all he_s done_/Marlon_Line8.wav"
                    m "Whatever, let’s just move on from this."
                    jump talking

                "The Ringmaster isn't here, you can talk about it.":
                    #voice "voices/Pita VA Clips/Pita_NotHere.wav"
                    p "Y’know, the Ringmaster isn’t here right now. And he’s not omniscient. You can talk about… whatever you need to say."
                    "Marlon takes a deep breath and looks over to Crimson for comfort. The lion nudges his hand as if to encourage him, and Marlon sighs."
                    show marlon disapointed
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/HowClose/_The Ringmaster isn_t here, you can talk about it_/Marlon_Line1.wav"
                    m "Maybe I’m just trying to convince myself everything’s fine, but…"
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/HowClose/_The Ringmaster isn_t here, you can talk about it_/Marlon_Line2.wav"
                    m "No matter how hard I try to think about hating him, I feel like I can’t."
                    show marlon nuetral
                    m "Even after all he’s done, he still gives us food and shelter… Honest advice about our performances and how we can do better…"
                    show marlon happy
                    "Marlon smiles quietly to himself."
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/HowClose/_The Ringmaster isn_t here, you can talk about it_/Marlon_Line3.wav"
                    m "You should’ve seen him when he was a performer… He was amazing. He’s the best performer in the Circus– no, the world, even."
                    
                    show marlon disapointed
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/HowClose/_The Ringmaster isn_t here, you can talk about it_/Marlon_Line4.wav"
                    m "But then I think about what he’s done to those close to me… What he did to… to Echo…" 
                    #voice "voices/Pita VA Clips/Pita_MarlonHey.wav"
                    p "Marlon, hey…"
                    "I move to place a hand on Marlon’s shoulder but he flinches, and Crimson growls in response. I slowly move my hand away but look at him with assurance."
                    #voice "voices/Pita VA Clips/Pita_Can'tBelieve.wav"
                    p "I can’t believe I’m saying this, but… You can still love the Ringmaster and hate him, too. Feelings are… complicated like that. Just don’t forget to put yourself first."

                    "Marlon looks over to the side, his brows furrowed as he mulls over his complicated feelings."
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/HowClose/_The Ringmaster isn_t here, you can talk about it_/Marlon_Line5.wav"

                    m "R-right…"
                    jump talking
    label dialogTreeEndings:
        menu:
            "I’m done talking to you. It’s time to end this.":
                #voice "voices/Pita VA Clips/Pita_TastyTeeth.wav"
                p "All of this talking is making me hungry. And I did spy some tasty teeth in that mouth of yours."
                show marlon surprised
                voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Endings/_I_m done talking to you. It_s time to end this_/Marlon_Line1.wav"
                
                m "Huh? What do you mean…?!"
                if crimsonhere:
                    "I leap forward, trying to pry Marlon’s pretty little mouth just wide enough to yank out his teeth. But as soon as I move for him, I feel a large force jump on me."
                    play sound "CrimsonRoar.mp3"
                    "I get pushed off of Marlon, rolling across the floor of the trailer. Once I get my bearings, I realize that I’m being pinned down by Marlon’s lion."
                    voice "voices/Pita VA Clips/Pita_GetOff.wav"
                    p "Get off of me!"
                    "I struggle against his weight, but I’m too weak to fend off this fully grown lion."
                    show marlon angry
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Endings/_I_m done talking to you. It_s time to end this_/Crimson present/Marlon_Line1.wav"   
                    m "Argh, you were trying to kill me!"
                    show marlon disapointed
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Endings/_I_m done talking to you. It_s time to end this_/Crimson present/Marlon_Line2.wav"   
                    m "And I thought I liked you…"
                    stop music 
                    show marlon nuetral
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Endings/_I_m done talking to you. It_s time to end this_/Crimson present/Marlon_Line3.wav"   
                    m "Crimson, it’s feeding time." #he's an icon
                    hide marlon nuetral
                    show crimson bad
                    play sound "CrimsonGrowl.mp3"
                    $ persistent.crimsonBad_unlocked = True
                    play music "FEAR.mp3"
                    "The lion on top of me growls, raising its hackles to reveal large and sharp teeth. For a moment, I smile as I think about how delicious they must be…"
                    "And then, I feel the lion’s jaw wrap around my neck, piercing my throat with his fangs. The lion rips my body to shreds, piece by piece, and my vision fades to black."
                    
                    jump death_screen
                    
                    return
                else:
                    "I leap forward, quickly overtaking the smaller man beneath me."
                    show marlon surprised
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Endings/_I_m done talking to you. It_s time to end this_/Alone/Marlon_Line1.wav"
                    m "P-Pita! What are you doing…?!"
                    #voice "voices/Pita VA Clips/Pita_GettingTired.wav"
                    p "I’m getting tired of hearing your little sob stories. No matter what, I can’t forgive you for just standing aside while the Ringmaster tortured me!"
                    #voice "voices/Pita VA Clips/Pita_PlayThing.wav"
                    p "You think I’m his favorite plaything? Well, you’re right. He just loves to hear me scream in pain. And you know what? I bet I’d love to hear you scream, too!"
                    "I take my hands and shove them into his mouth, forcing them between his lips as I try to pry it open."
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Endings/_I_m done talking to you. It_s time to end this_/Alone/Marlon_Line2.wav"   
                    m "P-Please stop, that hurts…!"
                    #voice "voices/Pita VA Clips/Pita_Beg.wav"
                    p "That’s right, beg. Beg for your life as I take it away, just like the Ringmaster and this damn Circus took away mine."
                    #voice "voices/Pita VA Clips/Pita_Wonder.wav"
                    p "Oh, I wonder how he’ll react once he’s seen how I devoured his precious little boy."
                    show marlon bad
                    $ persistent.marlonBad_unlocked = True
                    stop music fadeout 3.0
                    $ marlonIsAlive = False
                    "My hands are thrust into his mouth cavity, as I dig my fingers into its roof and bottom jaw. I begin to stretch Marlon’s mouth wider and wider, and all he can do is cry and scream."
                    "Finally, with a sharp crack, I break his jaw as his mouth begins to fill with blood from his torn skin and muscles. He falls limp beneath me."
                    "I take out his teeth piece by piece, savoring each little snack as I take it into my mouth and chew. I can feel my power growing stronger."
                    hide marlon bad
                    voice "voices/Pita VA Clips/Pita_Delicious.wav"
                    p "Delicious."
                    jump global_courtyard
            "We should try to get out of here. Together.":
                if bad > 0:
                    #voice "voices/Pita VA Clips/Pita_YouKnowHowBad.wav"
                    p "You know how bad the Ringmaster is. We should both try to escape him and this Circus"
                    show marlon surprised
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Endings/_We should try to get out of here. Together_/Marlon no like Pita/Marlon_Line1.wav"
                    m "You're trying to escape...?!"
                    show marlon disapointed
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Endings/_We should try to get out of here. Together_/Marlon no like Pita/Marlon_Line2.wav"
                    m "I should’ve known you were trying to leave, after all this time…"
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Endings/_We should try to get out of here. Together_/Marlon no like Pita/Marlon_Line3.wav"
                    m "I thought I trusted you…"
                    show marlon angry
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Endings/_We should try to get out of here. Together_/Marlon no like Pita/Marlon_Line4.wav"
                    m "… No. I can’t let you leave. If you go, who knows what the Ringmaster will do to me, to all of us… You’re staying right here."
                    #voice "voices/Pita VA Clips/PIta_DammitMarlon.wav"
                    p "Damn it Marlon, after all you’ve been through? The torture and abuse the Ringmaster has put you through, and you still choose his side?!"
                    show marlon disapointed
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Endings/_We should try to get out of here. Together_/Marlon no like Pita/Marlon_Line5.wav"
                    m "You just don’t get it, Pita…"
                    show marlon angry
                    stop music
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Endings/_We should try to get out of here. Together_/Marlon no like Pita/Marlon_Line6.wav"
                    m "Crimson, get her."
                    play sound "CrimsonRoar.mp3"
                    "Before I can even react, the lion pounces on top of me."
                    #play music "FEAR.mp3"
                    stop music fadeout 3.0
                    show crimson bad
                    $ persistent.crimsonBad_unlocked = True
                    play sound "CrimsonGrowl.mp3"
                    "I can feel its claws press against my body as it takes a bite out of my arm. The pain is enough to send my vision flashing white as I fall unconscious."
                    "The last thing I see is Marlon standing above me, his face warped with hurt, regret, and finally resolution."

                    jump death_screen

                    return
                else:
                    #good ending
                    #voice "voices/Pita VA Clips/Pita_TellTruth.wav"
                    p "Marlon… I have to tell you the truth."
                    show marlon nuetral
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Endings/_We should try to get out of here. Together_/Marlon fw Pita/Marlon_Line1.wav"
                    m "What is it?"
                    #voice "voices/Pita VA Clips/Pita_Trying.wav"
                    p "I’m trying to escape. You and I both know that we deserve better lives than this."
                    #voice "voices/Pita VA Clips/Pita_WantToLeaveToo.wav"
                    p "Marlon, I know you want to leave, too. We need to leave the Circus and the Ringmaster."
                    show marlon surprised
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Endings/_We should try to get out of here. Together_/Marlon fw Pita/Marlon_Line2.wav"
                    m "O-oh… I…"
                    "Marlon hesitates, but I interject quickly before he gets a chance to think about rejecting my offer."
                    #voice "voices/Pita VA Clips/Pita_ForHim.wav"
                    p "Do it for him."
                    "I point to the portrait on the wall and he follows to look at it. Then, he turns to me with a look of determination."
                    show marlon nuetral
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Endings/_We should try to get out of here. Together_/Marlon fw Pita/Marlon_Line3.wav"
                    m "You’re right."
                    show marlon disapointed
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Endings/_We should try to get out of here. Together_/Marlon fw Pita/Marlon_Line4.wav"
                    m "Even if the Ringmaster is like… a father to me, it doesn’t excuse the horrible, terrible things he’s done to me and you… and Echo"
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Endings/_We should try to get out of here. Together_/Marlon fw Pita/Marlon_Line5.wav"
                    m "It’s what he would’ve wanted for me… to be free and happy… and I can only do that if I’m away from this place…"
                    show marlon happy
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Endings/_We should try to get out of here. Together_/Marlon fw Pita/Marlon_Line6.wav"
                    m "Alright, I’ll come with you."
                    "I grin knowing this makes my plans for escape so much easier"
                    "And my stomach rumbles knowing this makes my plans for revenge even sweeter."
                    voice "voices/Pita VA Clips/Pita_BeforeLeave.wav"
                    #p "Before we leave, I need to get my wand back from the Ringmaster. Without it, I don’t have any power."
                    show marlon nuetral
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Endings/_We should try to get out of here. Together_/Marlon fw Pita/Marlon_Line7.wav"
                    m "Alright, I’m sure I can sneak into the Ringmaster’s trailer to get it for you. I go there all the time anyways."
                    #voice "voices/Pita VA Clips/Pita_Actually.wav"
                    p "Actually, it’s more than that."
                    show marlon surprised
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Endings/_We should try to get out of here. Together_/Marlon fw Pita/Marlon_Line8.wav"
                    m "Huh? What is it?"
                    #voice "voices/Pita VA Clips/Pita_Revenge.wav"
                    p "I  need {i}revenge{/i}. Revenge for what the Ringmaster has done to me, how he captured me and tortured me all for his little Circus."
                    #voice "voices/Pita VA Clips/Pita_ImSure.wav"
                    p "And I’m sure you want it, too. For everything the Ringmaster took away from you. Your life, your childhood, your partner…"
                    #voice "voices/Pita VA Clips/Pita_WithWand.wav"
                    p "With that wand, we can both take down the Ringmaster."
                    show marlon nuetral
                    "Marlon pauses to think, but this time he responds quickly and confidently, full of resolve."
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Endings/_We should try to get out of here. Together_/Marlon fw Pita/Marlon_Line9.wav"
                    m "We’ll take him down, together."
                    "We shake hands as we put our plan into motion: Marlon will escort me to the Ringmaster’s trailer, pretending as if I had been captured for escaping. Then, when the Ringmaster leasts expects it, Marlon will toss me my wand."
                    "Before we leave, Marlon takes with him the portrait of Echo on the wall and a bag of Steak Bites, with Crimson following behind us as we leave his trailer."
                    scene ringmaster-trailer
                    $ persistent.ringmasterTrailer_unlocked = True
                    "We make it to the Ringmaster’s trailer, and putting on my best act yet, I pretend to be helplessly captured by Marlon."
                    "When we enter the trailer, the Ringmaster is there playing quietly with my wand."
                    #show ringmaster at right
                    show marlon nuetral at right
                    show ringmaster at left
                    voice "voices/RM VA clips/Marlon Ending/RM_Line1.wav"
                    rm "Well, well, well, what do we have here…"
                    voice "voices/RM VA clips/Marlon Ending/RM_Line2.wav"
                    rm "My little Marlon, bringing with him a new pet."
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Endings/_We should try to get out of here. Together_/Marlon fw Pita/Inside RM_s Trailer/Marlon_Line1.wav"
                    m "S-she was trying to escape, but luckily my animals alerted me and I was able to catch her."
                    voice "voices/RM VA clips/Marlon Ending/RM_Line3.wav"
                    rm "Well done, my boy. You’ve proven to me that you’re still useful."
                    voice "voices/RM VA clips/Marlon Ending/RM_Line4.wav"
                    rm "Who said you can’t teach an old dog new tricks? You’ve learned well to fetch me my prized fairy."
                    "Marlon backs away from me as the Ringmaster approaches, inching towards my wand which he left on his table."
                    voice "voices/RM VA clips/Marlon Ending/RM_Line5.wav"
                    rm "Trying to fly away, are we, my little princess?"
                    #voice "voices/Pita VA Clips/Pita_DontCall.wav"
                    p "{i}Don’t{/i} call me that."
                    show marlon disapointed
                    voice "voices/RM VA clips/Marlon Ending/RM_line6.wav"
                    rm "Aw, don’t be such a sour sugarplum. Be glad it was Marlon who caught you and not the others. Lord knows that {i}child{/i} couldn’t hurt a fly."
                    show marlon nuetral
                    "He grabs my face with a gloved hand, squeezing my cheeks as he pulls me closer to him."
                    voice "voices/RM VA clips/Marlon Ending/RM_Line7.wav"
                    rm "Oh what ever shall I do with you, pet? I can barely put you on a leash, let alone in a cage. Perhaps it’s time for more… drastic measures."
                    voice "voices/RM VA clips/Marlon Ending/RM_Line8.wav"
                    rm "I have ways to {i}discipline{/i} my naughty pets. Isn’t that right, Marlon?"
                    "Marlon freezes just before he gets to my wand. He’s able to reel back and act like nothing happened."
                    show marlon surprised
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Endings/_We should try to get out of here. Together_/Marlon fw Pita/Inside RM_s Trailer/Marlon_Line2.wav"
                    m "Y-yes, sir…"
                    voice "voices/RM VA clips/Marlon Ending/RM_Line9.wav"
                    rm "Haha, of course you would know. After all, you’ve seen me work with the {i}naughtiest{/i} of them all."
                    voice "voices/RM VA clips/Marlon Ending/RM_Line10.wav"
                    rm "The nosey Echo, trying to seduce my precious Marlon right from under my nose. It’s a good thing he bit off more than he can chew with me."
                    voice "voices/RM VA clips/Marlon Ending/RM_Line11.wav"
                    rm "That was the last meal he ever had before he rotted away in his cage."
                    show marlon angry 
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Endings/_We should try to get out of here. Together_/Marlon fw Pita/Inside RM_s Trailer/Marlon_Line3.wav"
                    m "You’re wrong about him."
                    "I see from over the Ringmaster’s shoulder, Marlon just grabbed my wand off the table. The Ringmaster turns to him with a crazed malice."
                    voice "voices/RM VA clips/Marlon Ending/RM_Line12.wav"
                    rm "What’s this, talking back to your {i}father{/i}? I taught you better manners than that."
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Endings/_We should try to get out of here. Together_/Marlon fw Pita/Inside RM_s Trailer/Marlon_Line4.wav"
                    m "And you’re wrong about me, too. I’m not your little boy."
                    #no voice line
                    m "I know now that everything you’ve ever done to me was wrong. And now, it’s time to end it."
                    "Marlon throws my wand to me, and while the Ringmaster is distracted, I take off my fake bindings and catch my wand."
                    voice "voices/RM VA clips/Marlon Ending/RM_Line13.wav"
                    rm "What the hell is this?! You rotten fairy, you’ve turned my own pet against me!"
                    #voice "voices/Pita VA Clips/Pita_WakeHimUp.wav"
                    p "I didn’t do anything other than wake him up to the truth."
                    #voice "voices/Pita VA Clips/Pita_FinallyOver.wav"
                    p "It’s finally over for you, Ringmaster."
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Endings/_We should try to get out of here. Together_/Marlon fw Pita/Inside RM_s Trailer/Marlon_Line5.wav"
                    m "This is for Echo."
                    play sound "CrimsonRoar.mp3"
                    "Marlon opens the door to let Crimson in. The lion pounces on top of the Ringmaster, who can’t help but struggle underneath the weights of the animal."
                    voice "voices/RM VA clips/Marlon Ending/RM_Line14.wav"
                    rm "GET OFF OF ME! MARLON, YOU STUPID SHIT, GET YOUR DISGUSTING CREATURE OFF OF ME!!!"
                    stop music
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Endings/_We should try to get out of here. Together_/Marlon fw Pita/Inside RM_s Trailer/Marlon_Line6.wav"
                    m "I don’t take orders from you anymore. Crimson, it’s feeding time."
                    play sound "CrimsonGrowl.mp3"
                    "The lion clamps its jaws around the Ringmaster’s neck, tearing out his throat. I raise my wand, feeling my power slowly return to me as it surges from my fingertips."
                    "With my powers back, I toss away the Ringmaster’s mask to reveal his face for the first time. He’s barely able to protest as blood begins to fill his mouth and lungs."
                    voice "voices/RM VA clips/Marlon Ending/RM_Line15.wav"
                    rm "Ghhhk– s-stop… chhhk– give that… b-back…"
                    "Fear fills his eyes as he lifts into the air from my magic."
                    #voice "voices/Pita VA Clips/Pita_BeenThinking.wav"
                    p "I’ve been thinking about this feast since the moment I got here. And that look on your face is only going to make this much sweeter."
                    "With my magic, I crack apart his jaw like a peanut shell, and almost instantly his body falls limp. Marlon winces and turns away from the scene."
                    hide ringmaster 
                    show marlon good
                    $ persistent.marlonGood_unlocked = True
                    "As the Ringmaster’s body falls to the ground, I instantly rush over to his head, plucking out his teeth and gorging it down."
                    "When I chewed, I realized something was wrong and spat it out!"
                    "Disgusting! It's wood!"
                    "I wonder what part of his body isn't wood?"
                    "I dig my fingers into his chest and pierce his flesh. I reach in until I found what I wanted."
                    "One of his ribs."
                    "I tear it away from his body and begin gorging on it."
                    "Oh, I never realized how hungry I was until now."
                    "And it’s sweet. {i}Oh so sweet{/i}."
                    $ persistent.ringmasterShirtless_unlocked = True
                    return
            "I think I hear something going on outside." if crimsonhere and not attempted:
                $ attempted = True
                #voice "voices/Pita VA Clips/Pita_Hears.wav"
                p "I think I hear something outside… Like one of your animals choking on something."
                show marlon surprised
                voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Endings/_I think I hear something going on outside_/Marlon_Line1.wav"
                m "W-what?!"
                show marlon disapointed
                voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Endings/_I think I hear something going on outside_/Marlon_Line2.wav"
                m "Ugh, it might be my hyena again."
                show marlon nuetral
                voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Endings/_I think I hear something going on outside_/Marlon_Line3.wav"
                m "Stay right here. I’ll be right back."
                hide marlon nuetral
                "Marlon quickly leaves the trailer, leaving me and Crimson behind. He also forgets to close the trailer door, letting it swing loosely on its hinges."
                #show pita?
                "{i}This is the perfect opportunity to get rid of the lion.{/i}"
                "{i}Where are those treats again?{/i}"
                #TIMED CHOICES
                $ time = 5
                show screen qte(5, 'outOfTime')
                menu:
                    "Walk to the cabinet":
                        hide screen qte
                        "I walk over and check inside for its contents, except I don’t find what I’m looking for."
                        #voice "voices/Pita VA Clips/Pita_WhereAreThey.wav"
                        p "Damn it, where are they?!"
                        "As I frantically start searching for the treats, I hear Marlon shouting from outside as he walks back towards the trailer."
                        show marlon disapointed at right
                        voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Endings/_I think I hear something going on outside_/Wrong Choices/Marlon_Line1.wav"
                        m "Looks like it was a false alarm…"
                        "I walk away as calmly as I can to avoid any suspicions as Marlon enters the trailer."
                        show marlon nuetral
                        voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Endings/_I think I hear something going on outside_/Wrong Choices/Marlon_Line2.wav"
                        m "What were we talking about again?"
                        jump dialogTreeEndings
                    "Walk to the drawer":
                        hide screen qte
                        "I walk over and check inside for its contents, except I don’t find what I’m looking for."
                        #voice "voices/Pita VA Clips/Pita_WhereAreThey.wav"
                        p "Damn it, where are they?!"
                        "As I frantically start searching for the treats, I hear Marlon shouting from outside as he walks back towards the trailer."
                        show marlon disapointed at right
                        voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Endings/_I think I hear something going on outside_/Wrong Choices/Marlon_Line1.wav"
                        m "Looks like it was a false alarm…"
                        "I walk away as calmly as I can to avoid any suspicions as Marlon enters the trailer."
                        show marlon nuetral
                        voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Endings/_I think I hear something going on outside_/Wrong Choices/Marlon_Line2.wav"
                        m "What were we talking about again?"
                        jump dialogTreeEndings
                    "Walk to the cupboard.":
                        hide screen qte
                        "I walk over and check inside for its contents where I find dozens of other treats lining the shelves. I have to act quickly and find what I’m looking for."
                        #TIMED MENU
                        $ time = 5
                        show screen qte(5, 'outOfTime')
                        menu:
                            "Take the “Salmon Bits”":
                                hide screen qte
                                "I grab the treat and turn back around to Crimson, but I get no reaction from him. The lion barely even looks in the treat’s direction when I throw it out the open door."
                                show marlon surprised at right
                                voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Endings/_I think I hear something going on outside_/Wrong Choices/Marlon_Line3.wav"
                                m "Woah, what was that!"
                                "I stash away the treats and walk away as calmly as I can to avoid any suspicions as Marlon enters the trailer."
                                jump dialogTreeEndings
                            "Take the “Stoat Bones”":
                                hide screen qte
                                "I grab the treat and turn back around to Crimson, but I get no reaction from him. The lion barely even looks in the treat’s direction when I throw it out the open door."
                                show marlon surprised at right
                                voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Endings/_I think I hear something going on outside_/Wrong Choices/Marlon_Line3.wav"
                                m "Woah, what was that!"
                                "I stash away the treats and walk away as calmly as I can to avoid any suspicions as Marlon enters the trailer."
                                jump dialogTreeEndings
                            "Take the “Steak Bites”":
                                hide screen qte
                                $ crimsonhere = False
                                play sound "CrimsonPurr.mp3" 
                                show crimson surprised
                                $ persistent.crimsonSurprised_unlocked = True
                                "I grab the treat and turn back to Crimson, whose eyes immediately lock onto the bag of “Steak Bites.” As I grab one treat and toss it out the open door, the lion immediately bolts out as Marlon comes back inside the trailer."
                                hide crimson with moveoutleft
                                show marlon surprised at center
                                voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Endings/_I think I hear something going on outside_/Wrong Choices/Marlon_Line4.wav"
                                m "Woah, Crimson!"
                                "I quickly stash the treats away and walk over to the door to close and lock it."
                                #voice "voices/Pita VA Clips/Pita_ItLooksLike.wav"
                                p "It looks like Crimson wanted some time outside."
                                show marlon disapointed
                                voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Endings/_I think I hear something going on outside_/Wrong Choices/Marlon_Line5.wav"
                                m "I guess you’re right…"
                                show marlon nuetral
                                voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Endings/_I think I hear something going on outside_/Wrong Choices/Marlon_Line2.wav"
                                m "What were we talking about again?"
                                jump dialogTreeEndings
                label outOfTime:
                    hide screen qte
                    "I stand there for a bit too long..."
                    show marlon disapointed at right
                    m "Looks like it was a false alarm…"
                    voice "voices/Marlon_VA_clips/Front_of_Marlon_s_Trailer/Inside Trailer/Endings/_I think I hear something going on outside_/Wrong Choices/Marlon_Line2.wav"
                    m "What were we talking about again?"
                    jump dialogTreeEndings

return
