﻿# The script of the game goes in this file.

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
            scene pt-courtyard
            menu:
                "Marlon's":
                    jump global_visitMarlon
                "Bonnie's":
                    "jump global_bonnie"
                "Hugo's":
                    "jump global_hugo"
                "The Ringmaster's":
                    "jump global_ringmaster"
            
            #scene pt-courtyard
            #jump global_visitMarlon
        "Back":
            return

    return
