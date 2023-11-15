# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.
image intro_slideshow:
    "intro-cg-1.png"
    pause 1.5
    "intro-cg-2.png"
    pause 1.5
    "intro-cg-3.png"
    pause 1.5
    "intro-cg-4.png"
    pause 1.5
    "intro-cg-5.png"
    pause 1.5
    "intro-cg-6.png"
    pause 1.5
    "intro-cg-7.png"
    pause 1.5
    "intro-cg-8.png"
    pause 1.5
    "intro-cg-9.png"
    pause 1.5
    "intro-cg-10.png"
    pause 1.5
label start:
    scene trigger warning
    # shift options down      
    menu:
        "Continue":
            #play intro
            #RESIZE THEM
            scene "intro_slideshow"
            
            
            #scene pt-courtyard
            #jump global_visitMarlon
        "Back":
            return

    return
