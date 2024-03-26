# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Marlon", color = "#281aa3")
define p = Character("Pita", color = "#edf4b3")
define r = Character("Ringmaster", color = "#880808")
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
    if renpy.music.is_playing:
        play music "tension.mp3"
    else:
        play music "tension.mp3" fadein 3
    "I guess there’s no point in being sneaky, since as soon as I get close enough to the cages, the animals start stirring and making loud noises, banging on their bars and reaching out to grab me."

    show marlon surprised at right
    show crimson at left
    #also have lion

    $ persistent.marlonNuetral_unlocked = True
    $ persistent.marlonHappy_unlocked = True
    $ persistent.marlonSuprised_unlocked = True
    $ persistent.marlonSad_unlocked = True
    $ persistent.marlonDisapointed_unlocked = True
    $ persistent.marlonAngry_unlocked = True
    $ persistent.crimson_unlocked = True
    $ persistent.marlonChibi_unlocked = True
    m "I-Is someone there?"

    "I see Marlon, the circus’ animal trainer and performer. He’s standing in front of his trailer with a lion by his side, whip in one hand as he works with the animal."

    "His eyes land on me and immediately his expression changes, looking somewhat relieved."
    show marlon happy
    show marlon disapointed

    m "O-Oh, it’s just you, Pita..."

    show marlon surprised
    m "Wait a minute! H-How did you get out of your cage?"

    menu:
        "Don't worry about it.":
            p "Don’t worry too much about it, I just wanted to come speak with you."
            show marlon disapointed
            m "O-Oh, okay..."
        "The Ringmaster let me out.":
            p "The Ringmaster let me out of my cage so that I can come speak with you."
            show marlon disapointed
            m "O-Oh, I see..."
    
    "Out of all the other performers in the Circus, Marlon has always been the nicest to me. But even then, that isn’t saying a lot…"
    "He, like the other performers, still thinks that my suffering is worth it if it means keeping the Circus alive and functioning. As long as the Ringmaster makes money off of my pain, my existence… then the others will continue to think less of me."

    p "What are you still doing out here? Our performance ended hours ago."
    m "Oh, w-well…"
    m "The Ringmaster said my performance tonight was… lackluster. He needs it to be more engaging and more… dangerous…"

    "He looks towards his lion with a strange sadness, looking at the whip in his hand with a clenched fist before petting his lion with his other hand."
    show marlon happy
    m "Let’s head inside my trailer, my animals are being too noisy right now…"
    scene pt-marlon-trailer
    $ persistent.marlonTrailer_unlocked = True
    stop sound fadeout 1.0
    show marlon nuetral at right
    show crimson at left
    "Marlon leads me into his trailer along with his lion. The lion looks up to me and bares its teeth, growling."

    #thinking
    "{i}Hm, killing Marlon might be a problem if his lion is still here…{/i}"

    p "Does your lion have to come inside with us?"

    m "Oh, sorry about him… Crimson is very protective of me since I rescued him as a cub."

    "{i}Looks like I’ll have to find a way to get rid of his lion before I kill Marlon and eat his teeth.{/i}"

    "As I settle myself into Marlon’s trailer, I take a moment to glance around at my surroundings." 
    "His trailer is left plain with no notable decorations. There’s nothing displayed on any of the shelves, and the only thing interesting about the trailer was the animal fur rug on the floor."
    "One thing that caught my eye was a single portrait hanging on what is otherwise a barren wall. At a glance, I can’t help but feel like the man in the portrait looked really familiar."

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

            m "I was performing the same tricks I always do with my animals…"
            m "My monkey walks across the tightrope, my sea lion balances on a bouncy ball, my elephant performs with musical instruments…"
            m "But the Ringmaster said it wasn’t enough… He said my acts are getting “boring” and if I don’t improve it soon, he will…"

            "He trails off and looks up at me with a tortured expression."
            
            show marlon angry
            m "He wants me to perform with Crimson, but I can’t bring myself to hurt him."

            p "Perform with him how?"

            m "He wants him to “attack” me, and then I have to defend myself and tame him…"

            "His grip tightens on the whip in his hand."
            
            show marlon disapointed
            m "But he won’t attack me! He won’t even pounce at me or do anything dangerous… He’s just too attached to me…"
            m "And I can’t even hurt him if I wanted to…"
            
            menu:
                "What are you going to do?":
                    p "So what are you going to do? You know how the Ringmaster is, if you don’t do as he says, he’ll punish you."
                    show marlon disapointed
                    m "I… I don’t know…"
                    show marlon nuetral
                    m "If I don’t do what the Ringmaster says, he’ll probably lock me up like you and make me a sideshow freak…"
                    show marlon sad
                    m "Just like…"
                    "Marlon trails off again then glances up at the photo on the wall. He then shakes his head and turns back to me."
                    show marlon nuetral
                    m "I can’t let that happen."
                "Sounds like you’re in trouble.": #BAD
                    $ bad += 1
                    p "Well, it looks like you’re in a lot of trouble."
                    show marlon angry
                    m "Don’t you think I know that?"
                    show marlon nuetral
                    m "If I don’t figure out this act, the Ringmaster might take Crimson away from me. My only friend."
                    show marlon disapointed
                    m "I can’t lose her… I can’t lose anyone again. Not like…"
                    "Marlon trails off again then glances up at the photo on the wall. He then shakes his head and turns back to me."
                    show marlon nuetral
                    m "I can’t let that happen."
            $ choice1 = True
            jump talking
        "So you and Crimson must be quite close." if closeCrimson:
            $ closeCrimson = False
            p "I can see that you and your pet lion are quite close."
            show marlon angry
            m "Crimson is not just my pet, he’s my friend."
            show marlon nuetral
            m "But yes, he and I are very close."
            p "You mentioned that you rescued him, what did you mean?"
            show marlon happy
            m "Oh yes…"
            show marlon nuetral
            m "When I first joined the Circus, I already started training the animals that the Ringmaster kept here. Before me, the Ringmaster was the one who performed with them."
            m "I was young then, but on one of our trips, we found a lion cub that ran away from a zoo."
            show marlon disapointed
            m "The Ringmaster wanted to… dispose of it. A young lion cub is not as profitable as other animals, he said."
            show marlon nuetral
            m "But I was able to convince him to keep it, and I named him Crimson."
            show marlon disapointed
            m "The Ringmaster once said that one day, I need to perform with him, and he didn’t like our show, well…"
            m "He’ll do what he wanted to do when we first found Crimson."

            menu:
                "What’s it like being friends with a lion?":
                    p "You must feel very grateful to have a lion as a friend. What’s it like?"
                    show marlon happy
                    m "Oh, it’s really great."
                    show marlon nuetral
                    m "Lions are dangerous predators, but if you grow up with one, they treat you like part of their pride."
                    m "Crimson here sees me as one of his own, so he would never try to hurt me, ever."
                    show marlon disapointed
                    m "That’s why it’s kind of hard to perform with him like the Ringmaster wants us to…"
                    show marlon happy
                    m "Here, do you want to try and feed him? That way you can see how nice he really is."
                    "Marlon walks over to a cupboard in his trailer and opens the door, putting out a small bag of treats called “Steak Bites.”"
                    "As soon as the treats come out, Crimson lets out a purr of anticipation."
                    "Marlon takes two treats out and hands one to me."
                    m "Here, watch this."
                    show marlon nuetral
                    m "Crimson, sit."
                    #show crimson
                    "Like a dog, Crimson sits like Marlon commands."
                    m "Good, now roll over!"
                    "The large cat gets on the floor and rolls around on the animal fur rug."
                    "{i}Heh, cute{/i}"
                    show marlon happy 
                    m "See? He’s a very sweet boy."
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
                            "Crimson looked at me cautiously, but eventually he rolled over on the floor."
                        "Play dead":
                            p "Alright, play dead."
                            #show crimson 
                            "Crimson looked at me cautiously, but eventually he laid down on the ground belly up."
                        "Speak.":
                            p "Alright, speak."
                            #show crimson 
                            "Crimson looked at me cautiously, but eventually he let out a loud roar that filled the trailer."
                    show marlon happy
                    m "Good boy, Crimson! Now give him his treat."
                    "I hand over the treat to the lion who very carefully takes it from me for devouring it."
                    "{i}So the lion really likes these treats, huh? Maybe I can use that to distract him somehow so I can get Marlon alone.{/i}"
                "Maybe the lion deserves it.": 
                    #BAD
                    $ bad += 1
                    p "That’s understandable. After all, a lion can still be very dangerous."
                    show marlon angry
                    m "You don’t know anything about Crimson."
                    show marlon nuetral
                    m "Lions may be dangerous predators, but if you grow up with one like I did, they treat you like part of their pride."
                    m "Crimson here sees me as one of his own, so he would never try to hurt me, ever."
                    show marlon disapointed
                    m "As much as you would think, I can’t get him to act dangerously around me like the Ringmaster wants…"
                    show marlon nuetral
                    m "I can show you just how tame and friendly he is with some of his favorite treats."
                    "Marlon walks over to a cupboard in his trailer and opens the door, putting out a small bag of treats called “Steak Bites.”"
                    "As soon as the treats come out, Crimson lets out a purr of anticipation."
                    "Marlon takes two treats out and hands one to me."
                    m "Here, watch this."
                    show marlon nuetral
                    m "Crimson, sit."
                    #show crimson
                    "Like a dog, Crimson sits like Marlon commands."
                    m "Good, now roll over!"
                    "The large cat gets on the floor and rolls around on the animal fur rug."
                    show marlon angry
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
            m "I can’t believe you don’t remember him… Even though he spent his last few days next to your cage…"
            "All of a sudden, I remembered something. Or someone."
            "A man with red hair and green scales, who sat quietly in a cage next to mine. He rarely spoke, and when he did, his voice was hoarse and gravelly."
            "Like me, the Ringmaster treated him with little respect. He would always threaten to “put more scales on him” if he misbehaved."
            "I can recall one night, there was screaming. A lot of screaming. I remember just being annoyed, wishing the noise would stop. And it did. Dead quiet."
            "The next day, the man was in his cage, but he wasn’t moving."

            p "The Lizard Man? Huh…"
            p "He looks so… happy in that picture…"
            m "Yes, for a while, he and I were happy…"
            show marlon angry
            m "But then the Ringmaster took that away from me."
            $ time = 3
            show screen qte(3, 'lizard_wrong')
            menu:
                "His act wasn’t very good anyway.":
                    label lizard_wrong:
                        hide screen qte
                        $ bad += 1
                        p "His act wasn’t very good anyway."
                        show marlon angry
                        m "I wouldn’t expect you to sympathize. You’re the Ringmaster’s favorite little toy."
                        m "You’re just some fairy tale. A spectacle for others to look at."
                        show marlon disapointed
                        m "Meanwhile, I and the rest of the Circus work day and night on our performances with barely any recognition from the Ringmaster."
                        m "He did, too. He could bend and twist his body in impossible ways, but that was never enough for the Ringmaster or the rest of the Circus."
                        show marlon angry
                        m "Sometimes I think you deserve that fate more than he did."
                "He died screaming in his cage.":
                    hide screen qte
                    $ bad += 1
                    m "I wouldn’t expect you to sympathize. You’re the Ringmaster’s favorite little toy."
                    m "You’re just some fairy tale. A spectacle for others to look at."
                    show marlon disapointed
                    m "Meanwhile, I and the rest of the Circus work day and night on our performances with barely any recognition from the Ringmaster."
                    m "He did, too. He could bend and twist his body in impossible ways, but that was never enough for the Ringmaster or the rest of the Circus."
                    show marlon angry
                    m "Sometimes I think you deserve that fate more than he did."
                "He didn’t deserve that fate.":
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
                "Really? You and him?":
                    hide screen qte
                    $ bad += 1
                    m "I wouldn’t expect you to sympathize. You’re the Ringmaster’s favorite little toy."
                    m "You’re just some fairy tale. A spectacle for others to look at."
                    show marlon disapointed
                    m "Meanwhile, I and the rest of the Circus work day and night on our performances with barely any recognition from the Ringmaster."
                    m "He did, too. He could bend and twist his body in impossible ways, but that was never enough for the Ringmaster or the rest of the Circus."
                    show marlon angry
                    m "Sometimes I think you deserve that fate more than he did."
            jump talking
        "How close are you to the Ringmaster?" if not closeCrimson and ringmaster:
            $ ringmaster = False
            p "It sounds like you’re pretty close to the Ringmaster."
            show marlon nuetral
            m "I’ve been a part of this Circus since I was kid, and I always looked up to him."
            show marlon happy
            m "He was always so charismatic and intelligent. It was hard not to admire him, especially growing up."
            show marlon disapointed
            m "But now that I’m older… There are some things about him that I’ve grown to despise."
            m "I see how he treats other people, those who are less than him. I thought we were close, but he treats me badly, too."
            show marlon angry
            m "But you’re his favorite. He loves your act and even made you the mascot of the Circus."
            p "That’s not true. I hate him as much as you do."
            show marlon disapointed
            m "“Hate” is a strong word, but…"
            "Marlon takes another look at the portrait on the wall."
            jump talking
    label dialogTreeEndings:
        menu:
            "I’m done talking to you. It’s time to end this.":
                p "All of this talking is making me hungry. And I did spy some tasty teeth in that mouth of yours."
                show marlon surprised
                m "Huh? What do you mean…?!"
                if crimsonhere:
                    "I leap forward, trying to pry Marlon’s pretty little mouth just wide enough to yank out his teeth. But as soon as I move for him, I feel a large force jump on me."
                    "I get pushed off of Marlon, rolling across the floor of the trailer. Once I get my bearings, I realize that I’m being pinned down by Marlon’s lion."
                    p "Get off of me!"
                    "I struggle against his weight, but I’m too weak to fend off this fully grown lion."
                    show marlon angry
                    m "Argh, you were trying to kill me!"
                    show marlon disapointed
                    m "And I thought I liked you…"
                    show marlon nuetral
                    m "Crimson, it’s feeding time."
                    hide marlon nuetral
                    #play music "FEAR.mp3" noloop
                    stop music fadeout 3.0
                    show crimson bad
                    $ persistent.crimsonBad_unlocked = True
                    "The lion on top of me growls, raising its hackles to reveal large and sharp teeth. For a moment, I smile as I think about how delicious they must be…"
                    "And then, I feel the lion’s jaw wrap around my neck, piercing my throat with his fangs. The lion rips my body to shreds, piece by piece, and my vision fades to black."
                    
                    jump death_screen
                    
                    return
                else:
                    "I leap forward, quickly overtaking the smaller man beneath me."
                    show marlon surprised
                    m "P-Pita! What are you doing…?!"
                    p "I’m getting tired of hearing your little sob stories. No matter what, I can’t forgive you for just standing aside while the Ringmaster tortured me!"
                    p "You think I’m his favorite plaything? Well, you’re right. He just loves to hear me scream in pain. And you know what? I bet I’d love to hear you scream, too!"
                    "I take my hands and shove them into his mouth, forcing them between his lips as I try to pry it open."
                    m "P-Please stop, that hurts…!"
                    p "That’s right, beg. Beg for your life as I take it away, just like the Ringmaster and this damn Circus took away mine."
                    p "Oh, I wonder how he’ll react once he’s seen how I devoured his precious little boy."
                    show marlon bad
                    $ persistent.marlonBad_unlocked = True
                    stop music fadeout 3.0
                    $ marlonIsAlive = False
                    "My hands are thrust into his mouth cavity, as I dig my fingers into its roof and bottom jaw. I begin to stretch Marlon’s mouth wider and wider, and all he can do is cry and scream."
                    "Finally, with a sharp crack, I break his jaw as his mouth begins to fill with blood from his torn skin and muscles. He falls limp beneath me."
                    "I take out his teeth piece by piece, savoring each little snack as I take it into my mouth and chew. I can feel my power growing stronger."
                    hide marlon bad
                    p "Delicious."
                    jump global_courtyard
            "We should try to get out of here. Together.":
                if bad > 0:
                    p "You know how bad the Ringmaster is. We should both try to escape him and this Circus"
                    show marlon surprised
                    m "You're trying to escape...?!"
                    show marlon disapointed
                    m "I should’ve known you were trying to leave, after all this time…"
                    m "I thought I trusted you…"
                    show marlon angry
                    m "… No. I can’t let you leave. If you go, who knows what the Ringmaster will do to me, to all of us…"
                    m "You’re staying right here."
                    p "Damn it Marlon, after all you’ve been through? The torture and abuse the Ringmaster has put you through, and you still choose his side?!"
                    show marlon disapointed
                    m "You just don’t get it, Pita…"
                    show marlon angry
                    m "Crimson, get her."
                    "Before I can even react, the lion pounces on top of me."
                    #play music "FEAR.mp3"
                    stop music fadeout 3.0
                    show crimson bad
                    $ persistent.crimsonBad_unlocked = True
                    "I can feel its claws press against my body as it takes a bite out of my arm. The pain is enough to send my vision flashing white as I fall unconscious."
                    "The last thing I see is Marlon standing above me, his face warped with hurt, regret, and finally resolution."

                    jump death_screen

                    return
                else:
                    #good ending
                    p "Marlon… I have to tell you the truth."
                    show marlon nuetral
                    m "What is it?"
                    p "I’m trying to escape. You and I both know that we deserve better lives than this."
                    p "Marlon, I know you want to leave, too. We need to leave the Circus and the Ringmaster."
                    show marlon surprised
                    m "O-oh… I…"
                    "Marlon hesitates, but I interject quickly before he gets a chance to think about rejecting my offer."
                    p "Do it for him."
                    "I point to the portrait on the wall and he follows to look at it. Then, he turns to me with a look of determination."
                    show marlon nuetral
                    m "You’re right."
                    show marlon disapointed
                    m "Even if the Ringmaster is like… a father to me, it doesn’t excuse the horrible, terrible things he’s done to me and you… and Echo"
                    m "It’s what he would’ve wanted for me… to be free and happy… and I can only do that if I’m away from this place…"
                    show marlon happy
                    m "Alright, I’ll come with you."
                    "I grin knowing this makes my plans for escape so much easier"
                    "And my stomach rumbles knowing this makes my plans for revenge even sweeter."
                    p "Before we leave, I need to get my wand back from the Ringmaster. Without it, I don’t have any power."
                    show marlon nuetral
                    m "Alright, I’m sure I can sneak into the Ringmaster’s trailer to get it for you. I go there all the time anyways."
                    p "Actually, it’s more than that."
                    show marlon surprised
                    m "Huh? What is it?"
                    p "I  need {i}revenge{/i}. Revenge for what the Ringmaster has done to me, how he captured me and tortured me all for his little Circus."
                    p "And I’m sure you want it, too. For everything the Ringmaster took away from you. Your life, your childhood, your partner…"
                    p "With that wand, we can both take down the Ringmaster."
                    show marlon nuetral
                    "Marlon pauses to think, but this time he responds quickly and confidently, full of resolve."
                    m "We’ll take him down, together."
                    "We shake hands as we put our plan into motion: Marlon will escort me to the Ringmaster’s trailer, pretending as if I had been captured for escaping. Then, when the Ringmaster leasts expects it, Marlon will toss me my wand."
                    "Before we leave, Marlon takes with him the portrait of Echo on the wall and a bag of Steak Bites, with Crimson following behind us as we leave his trailer."
                    scene ringmaster-trailer
                    $ persistent.ringmasterTrailer_unlocked = True
                    #play music "tension.mp3" fadein 1.5
                    "We make it to the Ringmaster’s trailer, and putting on my best act yet, I pretend to be helplessly captured by Marlon."
                    "When we enter the trailer, the Ringmaster is there playing quietly with my wand."
                    #show ringmaster at right
                    show marlon nuetral at right
                    show ringmaster at left
                    r "Well, well, well, what do we have here…"
                    r "My little Marlon, bringing with him a new pet."
                    m "S-she was trying to escape, but luckily my animals alerted me and I was able to catch her."
                    r "Well done, my boy. You’ve proven to me that you’re still useful."
                    r "Who said you can’t teach an old dog new tricks? You’ve learned well to fetch me my prized fairy."
                    "Marlon backs away from me as the Ringmaster approaches, inching towards my wand which he left on his table."
                    r "Trying to fly away, are we, my little princess?"
                    
                    p "{i}Don’t{/i} call me that."
                    show marlon disapointed
                    r "Aw, don’t be such a sour sugarplum. Be glad it was Marlon who caught you and not the others. Lord knows that {i}child{/i} couldn’t hurt a fly."
                    show marlon nuetral
                    "He grabs my face with a gloved hand, squeezing my cheeks as he pulls me closer to him."
                    r "Oh what ever shall I do with you, pet? I can barely put you on a leash, let alone in a cage. Perhaps it’s time for more… drastic measures."
                    r "I have ways to {i}discipline{/i} my naughty pets. Isn’t that right, Marlon?"
                    "Marlon freezes just before he gets to my wand. He’s able to reel back and act like nothing happened."
                    show marlon surprised
                    m "Y-yes, sir…"
                    r "Haha, of course you would know. After all, you’ve seen me work with the {i}naughtiest{/i} of them all."
                    r "The nosey Echo, trying to seduce my precious Marlon right from under my nose. It’s a good thing he bit off more than he can chew with me."
                    r "That was the last meal he ever had before he rotted away in his cage."
                    show marlon angry 
                    m "You’re wrong about him."
                    "I see from over the Ringmaster’s shoulder, Marlon just grabbed my wand off the table. The Ringmaster turns to him with a crazed malice."
                    r "What’s this, talking back to your {i}father{/i}? I taught you better manners than that."
                    m "And you’re wrong about me, too. I’m not your little boy."
                    m "I know now that everything you’ve ever done to me was wrong. And now, it’s time to end it."
                    "Marlon throws my wand to me, and while the Ringmaster is distracted, I take off my fake bindings and catch my wand."
                    r "What the hell is this?! You rotten fairy, you’ve turned my own pet against me!"
                    p "I didn’t do anything other than wake him up to the truth."
                    p "It’s finally over for you, Ringmaster."
                    m "This is for Echo"
                    "Marlon opens the door to let Crimson in. The lion pounces on top of the Ringmaster, who can’t help but struggle underneath the weights of the animal."
                    r "GET OFF OF ME! MARLON, YOU STUPID SHIT, GET YOUR DISGUSTING CREATURE OFF OF ME!!!"
                    m "I don’t take orders from you anymore. Crimson, it’s feeding time."
                    "The lion clamps its jaws around the Ringmaster’s neck, tearing out his throat. I raise my wand, feeling my power slowly return to me as it surges from my fingertips."
                    "With my powers back, I toss away the Ringmaster’s mask to reveal his face for the first time. He’s barely able to protest as blood begins to fill his mouth and lungs."
                    r "Ghhhk– s-stop… chhhk– give that… b-back…"
                    "Fear fills his eyes as he lifts into the air from my magic."
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

                    return
            "I think I hear something going on outside." if crimsonhere and not attempted:
                $ attempted = True
                p "I think I hear something outside… Like one of your animals choking on something."
                show marlon surprised
                m "W-what?!"
                show marlon disapointed
                m "Ugh, it might be my hyena again."
                show marlon nuetral
                m "Stay right here. I’ll be right back."
                hide marlon nuetral
                "Marlon quickly leaves the trailer, leaving me and Crimson behind. He also forgets to close the trailer door, letting it swing loosely on its hinges."
                #show pita?
                "{i}This is the perfect opportunity to get rid of the lion.{/i}"
                "{i}Where are those treats again?{/i}"
                #TIMED CHOICES
                $ time = 3
                show screen qte(3, 'outOfTime')
                menu:
                    "Walk to the cabinet":
                        hide screen qte
                        "I walk over and check inside for its contents, except I don’t find what I’m looking for."
                        p "Damn it, where are they?!"
                        "As I frantically start searching for the treats, I hear Marlon shouting from outside as he walks back towards the trailer."
                        show marlon disapointed at right
                        m "Looks like it was a false alarm…"
                        "I walk away as calmly as I can to avoid any suspicions as Marlon enters the trailer."
                        show marlon nuetral
                        m "What were we talking about again?"
                        jump dialogTreeEndings
                    "Walk to the drawer":
                        hide screen qte
                        "I walk over and check inside for its contents, except I don’t find what I’m looking for."
                        p "Damn it, where are they?!"
                        "As I frantically start searching for the treats, I hear Marlon shouting from outside as he walks back towards the trailer."
                        show marlon disapointed at right
                        m "Looks like it was a false alarm…"
                        "I walk away as calmly as I can to avoid any suspicions as Marlon enters the trailer."
                        show marlon nuetral
                        m "What were we talking about again?"
                        jump dialogTreeEndings
                    "Walk to the cupboard.":
                        hide screen qte
                        "I walk over and check inside for its contents where I find dozens of other treats lining the shelves. I have to act quickly and find what I’m looking for."
                        #TIMED MENU
                        $ time = 3
                        show screen qte(3, 'outOfTime')
                        menu:
                            "Take the “Salmon Bits”":
                                hide screen qte
                                "I grab the treat and turn back around to Crimson, but I get no reaction from him. The lion barely even looks in the treat’s direction when I throw it out the open door."
                                show marlon surprised at right
                                m "Woah, what was that!"
                                "I stash away the treats and walk away as calmly as I can to avoid any suspicions as Marlon enters the trailer."
                                jump dialogTreeEndings
                            "Take the “Stoat Bones”":
                                hide screen qte
                                "I grab the treat and turn back around to Crimson, but I get no reaction from him. The lion barely even looks in the treat’s direction when I throw it out the open door."
                                show marlon surprised at right
                                m "Woah, what was that!"
                                "I stash away the treats and walk away as calmly as I can to avoid any suspicions as Marlon enters the trailer."
                                jump dialogTreeEndings
                            "Take the “Steak Bites”":
                                hide screen qte
                                $ crimsonhere = False
                                "I grab the treat and turn back to Crimson, whose eyes immediately lock onto the bag of “Steak Bites.” As I grab one treat and toss it out the open door, the lion immediately bolts out as Marlon comes back inside the trailer."
                                hide crimson
                                m "Woah, what was that!"
                                show marlon surprised at right
                                "I quickly stash the treats away and walk over to the door to close and lock it."
                                p "It looks like Crimson wanted some time outside."
                                show marlon disapointed
                                m "I guess you’re right…"
                                show marlon nuetral
                                m "What were we talking about again?"
                                jump dialogTreeEndings
                label outOfTime:
                    hide screen qte
                    "I stand there for a bit too long..."
                    show marlon disapointed at right
                    m "Looks like it was a false alarm…"
                    m "What were we talking about again?"
                    jump dialogTreeEndings

return
