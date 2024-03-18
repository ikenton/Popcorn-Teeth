init python:
    gallery = Gallery()
    
    gallery.button("pitaHappy")
    gallery.image("pita happy")
    gallery.condition("persistent.pitaHappy_unlocked")

    gallery.button("pitaLaugh")
    gallery.image("pita laugh")
    gallery.condition("persistent.pitaLaugh_unlocked")

    gallery.button("pitaTeeth")
    gallery.image("pita teeth")
    gallery.condition("persistent.pitaTeeth_unlocked")

    gallery.button("pitaSad")
    gallery.image("pita sad")
    gallery.condition("persistent.pitaSad_unlocked")

    gallery.button("pitaDisgust")
    gallery.image("pita disgusted")
    gallery.condition("persistent.pitaDisgust_unlocked")

    gallery.button("bonnieExcited")
    gallery.image("bonnie excited")
    gallery.condition("persistent.bonnieExcited_unlocked")

    gallery.button("bonnieShocked")
    gallery.image("bonnie shocked")
    gallery.condition("persistent.bonnieShocked_unlocked")

    gallery.button("bonnieSad")
    gallery.image("bonnie sad")
    gallery.condition("persistent.bonnieSad_unlocked")

    gallery.button("bonnieDisgust")
    gallery.image("bonnie disgusted")
    gallery.condition("persistent.bonnieDisgust_unlocked")

    gallery.button("hugoNuetral")
    gallery.image("hugo nuetral")
    gallery.condition("persistent.hugoNuetral_unlocked")

    gallery.button("hugoSmile")
    gallery.image("hugo smile")
    gallery.condition("persistent.hugoSmile_unlocked")

    gallery.button("hugoSmoking")
    gallery.image("hugo smoking")
    gallery.condition("persistent.hugoSmoking_unlocked")

    gallery.button("hugoSuprised")
    gallery.image("hugo surprised")
    gallery.condition("persistent.hugoSuprised_unlocked")

    gallery.button("hugoUpset")
    gallery.image("hugo upset")
    gallery.condition("persistent.hugoUpset_unlocked")

    gallery.button("hugoAngry")
    gallery.image("hugo angry")
    gallery.condition("persistent.hugoAngry_unlocked")

    gallery.button("hugoBack")
    gallery.image("hugo back")
    gallery.condition("persistent.hugoBack_unlocked")

    gallery.button("marlonNuetral")
    gallery.image("marlon nuetral")
    gallery.condition("persistent.marlonNuetral_unlocked")

    gallery.button("marlonHappy")
    gallery.image("marlon happy")
    gallery.condition("persistent.marlonHappy_unlocked")

    gallery.button("marlonSuprised")
    gallery.image("marlon surprised")
    gallery.condition("persistent.marlonSuprised_unlocked")

    gallery.button("marlonSad")
    gallery.image("marlon sad")
    gallery.condition("persistent.marlonSad_unlocked")

    gallery.button("marlonDisapointed")
    gallery.image("marlon disapointed")
    gallery.condition("persistent.marlonDisapointed_unlocked")

    gallery.button("marlonAngry")
    gallery.image("marlon angry")
    gallery.condition("persistent.marlonAngry_unlocked")

    gallery.button("crimson")
    gallery.image("crimson")
    gallery.condition("persistent.crimson_unlocked")

    gallery.button("ringmaster")
    gallery.image("ringmaster")
    gallery.condition("persistent.ringmaster_unlocked")

    gallery.button("ringmasterLean")
    gallery.image("ringmaster lean")
    gallery.condition("persistent.ringmasterLean_unlocked")

    gallery.button("ringmasterPull")
    gallery.image("ringmaster pullaway")
    gallery.condition("persistent.ringmasterPull_unlocked")

    gallery.button("cageInt")
    gallery.image("cage int")
    gallery.condition("persistent.cageInt_unlocked")

    gallery.button("ptCageTent")
    gallery.image("pt-cage-tent")
    gallery.condition("persistent.ptCageTent_unlocked")

    gallery.button("ptCourtyard")
    gallery.image("pt-courtyard")
    gallery.condition("persistent.ptCourtyard_unlocked")

    gallery.button("bonnieBad")
    gallery.image("bonnie bad")
    gallery.condition("persistent.bonnieBad_unlocked")

    gallery.button("bonnieTrailer")
    gallery.image("pt bonnie trailer")
    gallery.condition("persistent.bonnieTrailer_unlocked")

    gallery.button("bonnieDead")
    gallery.image("bonnie dead")
    gallery.condition("persistent.bonnieDead_unlocked")

    gallery.button("bonnieHidden")
    gallery.image("bonnie hidden")
    gallery.condition("persistent.bonnieHidden_unlocked")

    gallery.button("bonniePeak")
    gallery.image("bonnie peak")
    gallery.condition("persistent.bonniePeak_unlocked")

    gallery.button("underBed")
    gallery.image("underbed")
    gallery.condition("persistent.underBed_unlocked")

    gallery.button("hugoTrailer")
    gallery.image("pt-hugo-trailer")
    gallery.condition("persistent.hugoTrailer_unlocked")
    
    gallery.button("hugoBad")
    gallery.image("hugo bad")
    gallery.condition("persistent.hugoBad_unlocked")

    gallery.button("underTrailer")
    gallery.image("pita underneath")
    gallery.condition("persistent.underTrailer_unlocked")

    gallery.button("hugoHammer")
    gallery.image("hugo hammer")
    gallery.condition("persistent.hugoHammer_unlocked")

    gallery.button("marlonTrailer")
    gallery.image("pt-marlon-trailer")
    gallery.condition("persistent.marlonTrailer_unlocked")

    gallery.button("crimsonBad")
    gallery.image("crimson bad")
    gallery.condition("persistent.crimsonBad_unlocked")

    gallery.button("marlonBad")
    gallery.image("marlon bad")
    gallery.condition("persistent.marlonBad_unlocked")

    gallery.button("marlonGood")
    gallery.image("marlon good")
    gallery.condition("persistent.marlonGood_unlocked")

    gallery.button("ringmasterTrailer")
    gallery.image("ringmaster-trailer")
    gallery.condition("persistent.ringmasterTrailer_unlocked")

    gallery.button("pitaDead")
    gallery.image("pita dead")
    gallery.condition("persistent.pitaDead_unlocked")

    gallery.button("ringmasterDead")
    gallery.image("ringmaster dead")
    gallery.condition("persistent.ringmasterDead_unlocked")

    gallery.button("hugoChad")
    gallery.image("chad hugo")
    gallery.condition("persistent.hugoChad_unlocked")

    gallery.button("hugoPoster")
    gallery.image("hugo poster")
    gallery.condition("persistent.hugoPoster_unlocked")

transform gallery_transform_full:
    zoom 0.35

transform gallery_transform_expression:
    zoom 0.45

transform gallery_transform_large:
    xsize 340
    ysize 324

transform gallery_transform_crop1:
    crop(800, 10, 340, 324)

transform gallery_transform_crop2:
    xsize 555
    ysize 420

    xcenter 10

transform gallery_transform_locked:
    xsize 260
    ysize 420
    # crop (0, 0, 960, 540)

screen gallery_characters:
    tag menu

    use game_menu(_("Character Gallery"), scroll="viewport"):
        vbox:
            hbox:
                anchor(-0.9, 0.25) 
                spacing 50
                textbutton "Characters" action ShowMenu("gallery_characters")
                textbutton "CGs" action ShowMenu("gallery_cgs")
                textbutton "More" action ShowMenu("gallery_other")
        hbox:
            xalign 0.5
            yalign 0.5
            spacing 30

            grid 3 2:
                add gallery.make_button(name="pitaHappy", unlocked=At("images/pita happy.png", gallery_transform_expression), locked=At("images/blackscreen.png", gallery_transform_locked))
                add gallery.make_button(name="pitaSad", unlocked=At("images/pita sad.png", gallery_transform_expression), locked=At("images/blackscreen.png", gallery_transform_locked))
                add gallery.make_button(name="pitaDisgust", unlocked=At("images/pita disgusted.png", gallery_transform_expression), locked=At("images/blackscreen.png", gallery_transform_locked))
                add gallery.make_button(name="pitaLaugh", unlocked=At("images/pita laugh.png", gallery_transform_expression), locked=At("images/blackscreen.png", gallery_transform_locked))
                add gallery.make_button(name="pitaTeeth", unlocked=At("images/pita teeth.png", gallery_transform_expression), locked=At("images/blackscreen.png", gallery_transform_locked))
                spacing 15

        hbox:
            xalign 0.5
            yalign 0.5
            spacing 30
            grid 4 1:
                add gallery.make_button(name="bonnieExcited", unlocked=At("images/bonnie excited.png", gallery_transform_expression), locked=At("images/blackscreen.png", gallery_transform_locked))
                add gallery.make_button(name="bonnieSad", unlocked=At("images/bonnie sad.png", gallery_transform_expression), locked=At("images/blackscreen.png", gallery_transform_locked))
                add gallery.make_button(name="bonnieDisgust", unlocked=At("images/bonnie disgusted.png", gallery_transform_expression), locked=At("images/blackscreen.png", gallery_transform_locked))
                add gallery.make_button(name="bonnieShocked", unlocked=At("images/bonnie shocked.png", gallery_transform_expression), locked=At("images/blackscreen.png", gallery_transform_locked))
                spacing 15

        hbox:
            xalign 0.5
            yalign 0.5
            spacing 30
            grid 4 2:
                add gallery.make_button(name="hugoNuetral", unlocked=At("images/hugo nuetral.png", gallery_transform_large), locked=At("images/blackscreen.png", gallery_transform_locked))
                add gallery.make_button(name="hugoSmile", unlocked=At("images/hugo smile.png",  gallery_transform_large), locked=At("images/blackscreen.png", gallery_transform_locked))
                add gallery.make_button(name="hugoSmoking", unlocked=At("images/hugo smoking.png",  gallery_transform_large), locked=At("images/blackscreen.png", gallery_transform_locked))
                add gallery.make_button(name="hugoSuprised", unlocked=At("images/hugo surprised.png",  gallery_transform_large), locked=At("images/blackscreen.png", gallery_transform_locked))
                add gallery.make_button(name="hugoUpset", unlocked=At("images/hugo upset.png",  gallery_transform_large), locked=At("images/blackscreen.png", gallery_transform_locked))
                add gallery.make_button(name="hugoAngry", unlocked=At("images/hugo angry.png",  gallery_transform_large), locked=At("images/blackscreen.png", gallery_transform_locked))
                add gallery.make_button(name="hugoBack", unlocked=At("images/hugo back.png", gallery_transform_crop1), locked=At("images/blackscreen.png", gallery_transform_locked))
                spacing 15

        hbox:
            xalign 0.5
            yalign 0.5
            spacing 30
            grid 2 3:
                add gallery.make_button(name="marlonNuetral", unlocked=At("images/marlon nuetral.png", gallery_transform_expression), locked=At("images/blackscreen.png", gallery_transform_locked))
                add gallery.make_button(name="marlonHappy", unlocked=At("images/marlon happy.png", gallery_transform_expression), locked=At("images/blackscreen.png", gallery_transform_locked))
                add gallery.make_button(name="marlonSuprised", unlocked=At("images/marlon surprised.png", gallery_transform_expression), locked=At("images/blackscreen.png", gallery_transform_locked))
                add gallery.make_button(name="marlonSad", unlocked=At("images/marlon sad.png", gallery_transform_expression), locked=At("images/blackscreen.png", gallery_transform_locked))
                add gallery.make_button(name="marlonDisapointed", unlocked=At("images/marlon disapointed.png", gallery_transform_expression), locked=At("images/blackscreen.png", gallery_transform_locked))
                add gallery.make_button(name="marlonAngry", unlocked=At("images/marlon angry.png", gallery_transform_expression), locked=At("images/blackscreen.png", gallery_transform_locked))
                
                spacing 15

        hbox:
            xalign 0.5
            yalign 0.5
            spacing 30
            grid 2 1:
                add gallery.make_button(name="crimson", unlocked=At("images/crimson.png", gallery_transform_expression), locked=At("images/blackscreen.png", gallery_transform_locked))
                add gallery.make_button(name="ringmaster", unlocked=At("images/ringmaster.png", gallery_transform_expression), locked=At("images/blackscreen.png", gallery_transform_locked))

screen gallery_cgs:
    tag menu

    use game_menu(_("CG Gallery"), scroll="viewport"):
        vbox:
            hbox:
                anchor(-0.9, 0.25) 
                spacing 50
                textbutton "Characters" action ShowMenu("gallery_characters")
                textbutton "CGs" action ShowMenu("gallery_cgs")
                textbutton "More" action ShowMenu("gallery_other")
        hbox:
            xalign 0.5
            yalign 0.5
            spacing 30
            grid 2 11:
                add gallery.make_button(name="ringmasterLean", unlocked=At("images/ringmaster lean.png", gallery_transform_full), locked=At("images/blackscreen.png", gallery_transform_full))
                add gallery.make_button(name="ringmasterPull", unlocked=At("images/ringmaster pullaway.png", gallery_transform_full), locked=At("images/blackscreen.png", gallery_transform_full))
                add gallery.make_button(name="cageInt", unlocked=At("images/cage int.png", gallery_transform_full), locked=At("images/blackscreen.png", gallery_transform_full))
                add gallery.make_button(name="ptCageTent", unlocked=At("images/pt-cage-tent.png", gallery_transform_full), locked=At("images/blackscreen.png", gallery_transform_full))
                add gallery.make_button(name="ptCourtyard", unlocked=At("images/pt-courtyard.png", gallery_transform_full), locked=At("images/blackscreen.png", gallery_transform_full))

                add gallery.make_button(name="bonnieTrailer", unlocked=At("images/pt bonnie trailer.png", gallery_transform_full), locked=At("images/blackscreen.png", gallery_transform_full))
                add gallery.make_button(name="bonniePeak", unlocked=At("images/bonnie peak.png", gallery_transform_full), locked=At("images/blackscreen.png", gallery_transform_full))
                add gallery.make_button(name="underBed", unlocked=At("images/underbed.png", gallery_transform_full), locked=At("images/blackscreen.png", gallery_transform_full))
                add gallery.make_button(name="bonnieBad", unlocked=At("images/bonnie bad.png", gallery_transform_full), locked=At("images/blackscreen.png", gallery_transform_full))
                add gallery.make_button(name="bonnieHidden", unlocked=At("images/bonnie hidden.png", gallery_transform_full), locked=At("images/blackscreen.png", gallery_transform_full))
                add gallery.make_button(name="bonnieDead", unlocked=At("images/bonnie dead.png", gallery_transform_full), locked=At("images/blackscreen.png", gallery_transform_full))

                add gallery.make_button(name="hugoTrailer", unlocked=At("images/pt-hugo-trailer.png", gallery_transform_full), locked=At("images/blackscreen.png", gallery_transform_full))
                add gallery.make_button(name="hugoBad", unlocked=At("images/hugo bad.png", gallery_transform_full), locked=At("images/blackscreen.png", gallery_transform_full))
                add gallery.make_button(name="underTrailer", unlocked=At("images/pita underneath.png", gallery_transform_full), locked=At("images/blackscreen.png", gallery_transform_full))
                add gallery.make_button(name="hugoHammer", unlocked=At("images/hugo hammer.png", gallery_transform_full), locked=At("images/blackscreen.png", gallery_transform_full))

                add gallery.make_button(name="marlonTrailer", unlocked=At("images/pt-marlon-trailer.png", gallery_transform_full), locked=At("images/blackscreen.png", gallery_transform_full))
                add gallery.make_button(name="crimsonBad", unlocked=At("images/crimson bad.png", gallery_transform_full), locked=At("images/blackscreen.png", gallery_transform_full))
                add gallery.make_button(name="marlonBad", unlocked=At("images/marlon bad.png", gallery_transform_full), locked=At("images/blackscreen.png", gallery_transform_full))
                add gallery.make_button(name="marlonGood", unlocked=At("images/marlon good.png", gallery_transform_full), locked=At("images/blackscreen.png", gallery_transform_full))

                add gallery.make_button(name="ringmasterTrailer", unlocked=At("images/ringmaster-trailer.png", gallery_transform_full), locked=At("images/blackscreen.png", gallery_transform_full))
                add gallery.make_button(name="pitaDead", unlocked=At("images/pita dead.png", gallery_transform_full), locked=At("images/blackscreen.png", gallery_transform_full))
                add gallery.make_button(name="ringmasterDead", unlocked=At("images/ringmaster dead.png", gallery_transform_full), locked=At("images/blackscreen.png", gallery_transform_full))


screen gallery_other:
    tag menu

    use game_menu(_("More Art"), scroll="viewport"):
        vbox:
            hbox:
                anchor(-0.9, 0.25) 
                spacing 50
                textbutton "Characters" action ShowMenu("gallery_characters")
                textbutton "CGs" action ShowMenu("gallery_cgs")
                textbutton "More" action ShowMenu("gallery_other")

        hbox:
            xalign 0.5
            yalign 0.5
            spacing 30
            grid 2 1:
                add gallery.make_button(name="hugoChad", unlocked=At("images/chad hugo.png",  gallery_transform_expression), locked=At("images/blackscreen.png", gallery_transform_locked))
                add gallery.make_button(name="hugoPoster", unlocked=im.Scale("images/hugoposter.png", 360, 415.9), locked=At("images/blackscreen.png", gallery_transform_locked))