define e = Character("Eileen")
default bonnieIsAlive = True
default marlonIsAlive = True
default hugoIsAlive = True
default visitedRM = False

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
                #"I enter the courtyard where the main performers live. This is where I end this" #change line is bad
                #"Where should I go now?"
                menu:
                    "The blue wooden trailer with animal cages infront of it" if marlonIsAlive :
                        #$ marlonVisit = True
                        jump global_visitMarlon
                    "The pink and green floral trailer" if bonnieIsAlive:
                        jump global_bonnie
                    "The red, blue and yellow flashy trailer" if hugoIsAlive:
                        #$ hugo = True
                        jump global_hugoVendetta
                    "The red and gold panneled trailer":
                        "jump global_ringmaster"
            
            #scene pt-courtyard
            #jump global_visitMarlon
        "Back":
            return

    return
