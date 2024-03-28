define dragon = Character("Bryce")

image bg cave = "images/backgrounds/cave.png"
image bg cave wall = "images/backgrounds/cave_wall.png"
image bg treasure = "images/backgrounds/treasure.png"

image dragon normal = "images/characters/dragon_normal.png"
image dragon angry = "images/characters/dragon_angry.png"
image dragon flirty = "images/characters/dragon_flirty.png"
image dragon laugh = "images/characters/dragon_laugh.png"
image dragon sad = "images/characters/dragon_sad.png"
image dragon smirk = "images/characters/dragon_smirk.png"
image dragon stern = "images/characters/dragon_stern.png"
image dragon brow = "images/characters/dragon_brow.png"

label main:

    scene

    "Dizzy and unorganised, you wake up in some sort of cave. Luckily, it is not completely dark."

    scene bg cave with Dissolve(2.0)

    "From the shadows, a large figure walks up to you. When it enters the light, your heart skips a beat."

    window hide
    python:
        renpy.vibrate(0.25)
    play audio "/audio/sfx/growl.wav"
    show dragon angry with hpunch
    window show

    unknown "Raaaaaaaaaaaaaaaaa!"
    unknown "What is this? Another foolish adventurer entering my hoard without permission?"

    show dragon stern
    menu:
        unknown "You better explain yourself quickly before I turn up the heat."
        
        "It wasn't my choice to be here.":
            unknown "Well, it certainly wasn't my choice for a critter like you to show up either."
            unknown "Alas, I think it would be wise to get acquinted at once."
        
        "S-Sorry! Where is the exit?":
            show dragon sad
            unknown "There is none. Magical means brought you here, so only magical means could bring you back."

        "Die, you scaly bastard!":
            show dragon brow
            unknown "And how exactly did you plan on killing me? You are completely unarmed."
            show dragon smirk
            unknown "Meanwhile, I could easily slice your throat if I wanted to, chew on your arms and legs."
            show dragon stern
            unknown "But I'm afraid that would get messy quickly, so let's try to remain friendly for now."

    show dragon normal
    unknown "Since we're going to be stuck here for a while, I suppose I'll introduce myself."
    dragon "My name is Bryce. A dragon, as you can see. You currently find yourself inside of my hoard."
    dragon "You are not from this world, so you most likely ended up here through a portal."

    show dragon stern
    menu:
        dragon "However, I know for a fact those portals always come with a warning. Why did you proceed regardless?"

        "I thought that voice was all in my head.":
            show dragon brow
            dragon "I know magic is rare in your world, but stop and think for a moment next time it happens."
            dragon "You think your brain would be able to come up with an intricate, fake legend to scare you off?"
            show dragon laugh
            dragon "Hah, I don't think so! Only an aspriring writer like me could!"
        "I was curious where that voice came from.":
            show dragon brow
            dragon "I can understand, but maybe think for a moment when the warning involves a spooky legend."
            show dragon smirk
            dragon "Even if that legend is fake... Honestly, as an aspiring writer, I'm proud how it turned out."

    show dragon stern
    dragon "Anyways, the reason does not matter much. What matters is that we get you out of here."
    show dragon normal
    dragon "There is a magical artifact in my treasure room that could bring you back home. However..."
    dragon "That room is behind a magical door that only opens when you manage to solve a puzzle."
    show dragon sad
    dragon "Regrettably, I left the answers in the treasure room, and I haven't been able to solve them since."
    show dragon brow
    dragon "Only someone clever and dragon-hearted could figure out the solution. Care to give it a try?"
    show dragon normal
    dragon "Alright, let me show one to you. I'll try to give you a hint when you get stuck. Good luck!"

    python:
        renpy.jump(renpy.random.choice([
            "puzzle_inscriptions",
            "puzzle_trivia"
        ]))

    label main_end:
        scene bg cave
        show dragon brow
        dragon "It looks like the treasure room is opening!"
        scene bg treasure with Fade(0.5,1.0,0.5,color="#fff")
        show dragon laugh with dissolve
        dragon "Oh my goodness, it's been too long since I've been here. Take a look at all this!"
        label main_end_unlock:
            window hide
            hide dragon with dissolve
            show text "Press to unlock the locker. Make sure to open the door before the lock closes again."
            pause
            show text "Locker has been unlocked. Please close the door when finished!"
            python:
                renpy.fetch("http://192.168.1.1/open", method="post")
                renpy.pause(delay=5, hard=True)
            show text "Waiting for the lock to cool down..."
            python:
                renpy.pause(delay=5, hard=True)
            hide text
            menu:
                "Continue":
                    window show
                "Re-open locker":
                    jump main_end_unlock
            
            show dragon normal
            dragon "Thank you so much for helping me out here. I truly appreciate it!"
            "The dragon inspects the hoard, walks up to one of the crystals and picks it up."
            dragon "This is the Chronoreverie, a crystal that allows you to reverse decisions made in the past."
            dragon "I can use this to reverse your decision to ever come here, and thus send you back to the human realm."
            dragon "Though, it comes with several side effects. I will no longer be able to remember you, for example."
            show dragon sad
            menu:
                dragon "And any memories you have of me and this place will no longer seem real to you. As if it all happened in a video game."

                "Stay here":
                    show dragon normal
                    dragon "Awrrr, that's incredibly sweet of you. Alas, I think it's better for you to back."
                    show dragon sad
                    dragon "You've got family and friends up there, and adventures to be had. Down here, there isn't a lot to do."
                    show dragon laugh
                    dragon "And, besides... Maybe, that cache will pique your interest again at some point. You'd get to see me again!"
                    show dragon normal
                    dragon "I might have a different puzzle for you to solve, too. There are several other ways we could've gotten into the treasure room."

                "Insist on sending you back":
                    show dragon normal
                    dragon "Yeah, you are right. Let's get you home now. I appreciate the visit, though!"

            dragon "Before I let you go and will forget your visit, I would like to ask you something though."
            "The dragon picks up a pen and notebook and gives it to you. The cover reads \"Humans Who Visited\"."
            show dragon brow
            dragon "Would you mind writing your name in there, alongside the date and time of your visit?"
            show dragon normal
            dragon "Thank you for visiting me. Take good care of yourself!"
            "The dragon whispers something in draconic tongue to the crystal, after which is begins to glow."
            "And before long, you find yourself on the way back to the human realm."
            window hide

            play music "audio/bgm/portal.mp3"
            python:
                renpy.pause(delay=0.5, hard=True)
            scene bg portal 1 with Fade(0.5,1,0.5)
            scene bg portal 2 with Dissolve(0.50)
            scene bg portal 1 with Dissolve(0.50)
            scene bg portal 2 with Dissolve(0.40)
            scene bg portal 30 with Dissolve(0.30)
            scene bg portal 29 with Dissolve(0.30)
            scene bg portal 28 with Dissolve(0.30)
            scene bg portal 27 with Dissolve(0.30)
            scene bg portal 26 with Dissolve(0.30)
            scene bg portal 25 with Dissolve(0.30)
            scene bg portal 24 with Dissolve(0.30)
            scene bg portal 23 with Dissolve(0.30)
            scene bg portal 22 with Dissolve(0.30)
            scene bg portal 21 with Dissolve(0.30)
            scene bg portal 20 with Dissolve(0.30)
            scene bg portal 19 with Dissolve(0.30)
            scene bg portal 18 with Dissolve(0.30)
            scene bg portal 17 with Dissolve(0.30)
            scene bg portal 16 with Dissolve(0.30)
            scene bg portal 15 with Dissolve(0.30)
            scene bg portal 14 with Dissolve(0.30)
            scene bg portal 13 with Dissolve(0.30)
            scene bg portal 12 with Dissolve(0.30)
            scene bg portal 11 with Dissolve(0.30)
            scene bg portal 10 with Dissolve(0.30)
            scene bg portal 9 with Dissolve(0.30)
            scene bg portal 8 with Dissolve(0.30)
            stop music fadeout 3
            scene bg portal 7 with Dissolve(0.30)
            scene bg portal 6 with Dissolve(0.30)
            scene bg portal 5 with Dissolve(0.30)
            scene bg portal 4 with Dissolve(0.30)
            scene bg portal 3 with Dissolve(0.30)
            python:
                renpy.pause(delay=0.3, hard=True)
            scene

            pause 3

            return # this ends the game