define e = Character("Eileen")
default bonnieIsAlive = True
default marlonIsAlive = True
default hugoIsAlive = True
default visitedRM = False
default escapedBonnie = False

screen warning():
    
    vbox:
        at transform:
            ypos 800
            xalign 0.5
            
        textbutton "Continue":
            action Jump("global_beginning")
            style "choice_button"

        textbutton "Back":
            action Jump("global_back")
            style "choice_button"
            
# The game starts here.
label start:  
    stop music fadeout 2.0
    scene trigger warning
    call screen warning
    # shift options down  
    label global_courtyard:
        stop music
        play sound  "audio/cricket-song.mp3" volume 0.09
        scene pt-courtyard
        menu:
            "The blue wooden trailer with animal cages infront of it" if marlonIsAlive :
                
                jump global_visitMarlon
            "The pink and green floral trailer" if bonnieIsAlive and not escapedBonnie:
        
                jump global_bonnie
            "The flashy red, blue and yellow trailer" if hugoIsAlive:
                
                jump global_hugoVendetta
            "The red and gold panneled trailer":
                jump global_ringmaster
    #scene pt-courtyard
    #jump global_visitMarlon
    label global_back:
        return

label death_screen:
    play music "audio/death_screen.mp3" fadein 1.0
    show blackscreen
    with Fade(1.0, 4.0, 0.5)
