# label before_main_menu:
#     play music "audio/bgm/main_menu.opus" noloop

label splashscreen:
    if renpy.variant("web"):
        show screen confirm("Would you like to play the game in full screen (if supported)? You can change this later in the preferences menu.",  [ Hide(), Preference("display", "fullscreen") ], [ Hide(), Preference("display", "window") ])
    return