# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.
label start:
    scene trigger warning
    # shift options down  
    menu:
        "Continue":
            #play intro
            #RESIZE THEM
            jump global_beginning
            label global_courtyard:
                scene pt-courtyard
                
                menu:
                    "The blue wooden trailer with animal cages infront of it" :
                        #$ marlonVisit = True
                        jump global_visitMarlon
                    "The pink and green floral trailer":
                        jump global_bonnie
                    "The red and gold panneled trailer":
                        "jump global_ringmaster"
            
            #scene pt-courtyard
            #jump global_visitMarlon
        "Back":
            return

    return
