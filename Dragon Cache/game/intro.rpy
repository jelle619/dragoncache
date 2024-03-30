define unknown = Character("???")

image bg forest = "images/backgrounds/forest.webp"

image bg portal 1 = "images/backgrounds/portal_1.webp"
image bg portal 2 = "images/backgrounds/portal_2.webp"
image bg portal 3 = "images/backgrounds/portal_3.webp"
image bg portal 4 = "images/backgrounds/portal_4.webp"
image bg portal 5 = "images/backgrounds/portal_5.webp"
image bg portal 6 = "images/backgrounds/portal_6.webp"
image bg portal 7 = "images/backgrounds/portal_7.webp"
image bg portal 8 = "images/backgrounds/portal_8.webp"
image bg portal 9 = "images/backgrounds/portal_9.webp"
image bg portal 10 = "images/backgrounds/portal_10.webp"
image bg portal 11 = "images/backgrounds/portal_11.webp"
image bg portal 12 = "images/backgrounds/portal_12.webp"
image bg portal 13 = "images/backgrounds/portal_13.webp"
image bg portal 14 = "images/backgrounds/portal_14.webp"
image bg portal 15 = "images/backgrounds/portal_15.webp"
image bg portal 16 = "images/backgrounds/portal_16.webp"
image bg portal 17 = "images/backgrounds/portal_17.webp"
image bg portal 18 = "images/backgrounds/portal_18.webp"
image bg portal 19 = "images/backgrounds/portal_19.webp"
image bg portal 20 = "images/backgrounds/portal_20.webp"
image bg portal 21 = "images/backgrounds/portal_21.webp"
image bg portal 22 = "images/backgrounds/portal_22.webp"
image bg portal 23 = "images/backgrounds/portal_23.webp"
image bg portal 24 = "images/backgrounds/portal_24.webp"
image bg portal 25 = "images/backgrounds/portal_25.webp"
image bg portal 26 = "images/backgrounds/portal_26.webp"
image bg portal 27 = "images/backgrounds/portal_27.webp"
image bg portal 28 = "images/backgrounds/portal_28.webp"
image bg portal 29 = "images/backgrounds/portal_29.webp"
image bg portal 30 = "images/backgrounds/portal_30.webp"

define config.default_fullscreen = True 

label start:

    stop music fadeout 1.0

    scene

    unknown "..."
    unknown "Congratulations, brave adventurer. It appears you have found the Geocache."
    unknown "However, this is no ordinary Geocache. In fact, there's a legend surrounding it."
    unknown "You are in quite a predicament, if the legend turns out to be true."
    unknown "The legend... hmm, I think I remember it now..."

    scene bg forest

    play music "audio/bgm/suspense.opus"

    unknown "Once upon a time, two brave adventurers were overjoyed to find a Geocache. However, something was amiss."
    unknown "The cache was placed on private property, but they knew the owner had little to do with Geocaching."
    unknown "They tried to look online, but the cache they found was not displayed on any map."
    unknown "Despite all the red flags, curiosity got the better of them, and they attempted to open it."
    unknown "As they were figuring out how to get the mechanism to unlock, they heard a voice coming from inside."
    unknown "A low, rumbling and foreign voice, trying to tell them that they should stay away."
    unknown "One of the duo was stubborn and did not heed the warning. The other got frightened and distanced himself."
    unknown "The foolish adventurer continued trying to open it. Nothing seemed to work, until he heard a click."
    unknown "The door flew wide open to reveal a dark void, and the adventurer got sucked into it."
    unknown "The other ran away, looking for help. But when he got back, the cache had disappeared."
    unknown "It earned the name \"The Dragon Cache\", referring to the ominous spirit inside of it."
    unknown "For only a creature as vile as a dragon could ever do this to someone innocent."
    unknown "And over time, the story became known as \"The Legend of the Dragon Cache\"."

    stop music fadeout 1.0

    scene

    unknown "Something tells me this must be the Dragon Cache of legend."
    unknown "It would be foolish to repeat the steps of the previous adventurer."
    unknown "I think it's best to turn around now. Go home, and make yourself comfortable."
    unknown "..."
    unknown "It was certainly nice meeting you."
    unknown "..."
    unknown "Goodbye, my friend. Take care!"
    unknown "..."
    unknown "Still here? Hmmm..."
    unknown "..."
    unknown "I suppose I can't stop you. However, you are on your own now."
    unknown "Wish you the most of luck, take care."

    "You pry away at the Geocache, trying to figure out the mechanism that opens it."
    "Even though you do your best, nothing seems to work until you suddenly hear a click."
    "The door of the Geocache suddenly swings right open, and you feel a force pulling on you."
    "You try to get away, but the force is too over-powering, and you get sucked up into the Geocache."

    play music "audio/bgm/portal.opus" noloop
    python:
        renpy.pause(delay=0.5, hard=True)
    scene bg portal 1 with Dissolve(0.50)
    scene bg portal 2 with Dissolve(0.50)
    scene bg portal 1 with Dissolve(0.50)
    scene bg portal 2 with Dissolve(0.40)
    scene bg portal 3 with Dissolve(0.30)
    scene bg portal 4 with Dissolve(0.30)
    scene bg portal 5 with Dissolve(0.30)
    scene bg portal 6 with Dissolve(0.30)
    scene bg portal 7 with Dissolve(0.30)
    scene bg portal 8 with Dissolve(0.30)
    scene bg portal 9 with Dissolve(0.30)
    scene bg portal 10 with Dissolve(0.30)
    scene bg portal 11 with Dissolve(0.30)
    scene bg portal 12 with Dissolve(0.30)
    scene bg portal 13 with Dissolve(0.30)
    scene bg portal 14 with Dissolve(0.30)
    scene bg portal 15 with Dissolve(0.30)
    scene bg portal 16 with Dissolve(0.30)
    scene bg portal 17 with Dissolve(0.30)
    scene bg portal 18 with Dissolve(0.30)
    scene bg portal 19 with Dissolve(0.30)
    scene bg portal 20 with Dissolve(0.30)
    scene bg portal 21 with Dissolve(0.30)
    scene bg portal 22 with Dissolve(0.30)
    scene bg portal 23 with Dissolve(0.30)
    scene bg portal 24 with Dissolve(0.30)
    scene bg portal 25 with Dissolve(0.30)
    stop music fadeout 3
    scene bg portal 26 with Dissolve(0.30)
    scene bg portal 27 with Dissolve(0.30)
    scene bg portal 28 with Dissolve(0.30)
    scene bg portal 29 with Dissolve(0.30)
    scene bg portal 30 with Dissolve(0.30)
    python:
        renpy.pause(delay=0.3, hard=True)
    scene

    pause 3

    jump main