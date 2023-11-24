define rm = Character("Ringmaster", color = "#F00040")
define p = Character("Pita")

label global_ringmaster:
    "I approach the trailer and notice that it’s slightly open."
    if marlonIsAlive or bonnieIsAlive or hugoIsAlive:
        "Should I enter?"
        menu:
            "Yes":
                jump enter
            "No":
                "I slowly back away from the open door and my immense dread fades."
                jump global_courtyard
    else:
        label enter:
            #scene pt-ringmaster-trailer
            "I take a step on the stepping stool and open the door to a poorly lit room."
            "A man sits at his desk, writing. He doesn’t bother to raise his head, but instead reaches for his mask and slips it on."
            if not marlonIsAlive and not bonnieIsAlive and not hugoIsAlive:
                jump goodEnding
            else:
                jump badending

            label goodEnding:
                rm ""
            label badending:

            