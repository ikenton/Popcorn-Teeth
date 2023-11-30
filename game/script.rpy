define e = Character("Eileen")
default bonnieIsAlive = True
default marlonIsAlive = True
default hugoIsAlive = True
default visitedRM = False

# The game starts here.
label start:  
    stop music fadeout 2.0
    scene trigger warning
    # shift options down  
    menu:
        "Continue":
            
            jump global_beginning
            label global_courtyard:
                stop music
                play sound  "cricket-song.mp3" volume 0.09
                scene pt-courtyard
                menu:
                    "The blue wooden trailer with animal cages infront of it" if marlonIsAlive :
                        
                        jump global_visitMarlon
                    "The pink and green floral trailer" if bonnieIsAlive:
                        jump global_bonnie
                    "The flashy red, blue and yellow trailer" if hugoIsAlive:
                       
                        jump global_hugoVendetta
                    "The red and gold panneled trailer":
                        jump global_ringmaster
            
            #scene pt-courtyard
            #jump global_visitMarlon
        "Back":
            return

    return
