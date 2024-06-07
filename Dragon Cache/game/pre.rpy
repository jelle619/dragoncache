# label before_main_menu:
#     play music "audio/bgm/main_menu.opus" noloop

label splashscreen:
    call screen languageselect

    if renpy.variant("web"):
        call screen confirm(_("Would you like to play the game in fullscreen (if supported)? You can change this later in the preferences menu."),  [ Hide(), Preference("display", "fullscreen"), Return()], [ Hide(), Preference("display", "window"), Return()])
    return

screen languageselect:

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _("Choose a language. / Kies een taal."):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("English") action [Hide(), Language(None), Return()]
                textbutton _("Nederlands") action [Hide(), Language("nederlands"), Return()]

    ## Right-click and escape answer "no".
    ## key "game_menu" action [Hide(), Language(None), Return()]