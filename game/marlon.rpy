# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Marlon", color = "#281aa3")
define p = Character("Pita")

# The game starts here.

label global_visitMarlon:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    

    #if pita has already visited
    "I decided to stop by Marlon's trailer again."
    scene pt-marlon-trailer
    
    show marlon surprised

    m "O-Oh it's just you again..."

    show marlon disapointed

    m "Was there something else you needed?"
    
    #if first time visiting marlon

    "I think it’s time to stop by Marlon’s trailer."
    

    "I head towards Marlons’s trailer, which is hard to see since it’s surrounded by cages filled with other circus animals. Bears, tigers, horses, monkeys, and even sea lions… All trapped here, just like me."

    "I guess there’s no point in being sneaky, since as soon as I get close enough to the cages, the animals start stirring and making loud noises, banging on their bars and reaching out to grab me."

    show marlon surprised
    #also have lion

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
    show marlon nuetral
    #show crimson
    "Marlon leads me into his trailer along with his lion. The lion looks up to me and bares its teeth, growling."

    #thinking
    "{i}Hm, killing Marlon might be a problem if his lion is still here…{/i}"

    p "Does your lion have to come inside with us?"

    m "Oh, sorry about him… Crimson is very protective of me since I rescued him as a cub."

    "{i}Looks like I’ll have to find a way to get rid of his lion before I kill Marlon and eat his teeth.{/i}"

    "As I settle myself into Marlon’s trailer, I take a moment to glance around at my surroundings. His trailer is left plain with no notable decorations. There’s nothing displayed on any of the shelves, and the only thing interesting about the trailer was the animal fur rug on the floor."
    "One thing that caught my eye was a single portrait hanging on what is otherwise a barren wall. At a glance, I can’t help but feel like the man in the portrait looked really familiar."

    m "So, you said you wanted to talk to me about something…?"

    menu:
        "What happened with the performance tonight?":

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
                    p "Well, it looks like you’re in a lot of trouble."
                    show marlon angry
                    m "Don’t you think I know that?"
                    show marlon nuetral
                    m "If I don’t figure out this act, the Ringmaster might take Nala away from me. My only friend."
                    show marlon disapointed
                    m "I can’t lose her… I can’t lose anyone again. Not like…"
                    "Marlon trails off again then glances up at the photo on the wall. He then shakes his head and turns back to me."
                    show marlon nuetral
                    m "I can’t let that happen."
        "So you and Crimson must be quite close.":
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
                    show marlon nuetral
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
                            p "Alright, speaka."
                            #show crimson 
                            "Crimson looked at me cautiously, but eventually he let out a loud roar that filled the trailer."
                    show marlon happy
                    m "Good boy, Crimson! Now give him his treat."
                    "I hand over the treat to the lion who very carefully takes it from me for devouring it."
                    "{i}So the lion really likes these treats, huh? Maybe I can use that to distract him somehow so I can get Marlon alone.{/i}"
                "Maybe the lion deserves it.": 
                    #BAD
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
        #if choice 1 is finished
        #"Who’s the man in that photo?":

   
   
   
    return
