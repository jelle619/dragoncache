image bg cave wall = "images/backgrounds/cave_wall.webp"

label puzzle_inscriptions:
    scene bg cave wall
    play music "audio/bgm/puzzle.opus"

    $ inscription = _("even the flame of a dragon must begin as a spark")
    show text "{size=+30}{font=clawrite.ttf}[inscription]"

    dragon "These inscriptions are written in an acient dragon language. I wonder what they mean..."
    dragon "See, I actually grew up with the modern dragon language, so I have no idea what this says."
    dragon "At the very least, I do know that every symbol corresponds to one letter."
    dragon "Punctuation marks are omitted, and capital letters look identical to small letters."
    dragon "I bet figuring out what it says is the key towards getting access to the treasure room."
    dragon "Good luck! Let me know if you need a hint or want me to explain it again."

    label puzzle_inscriptions_text:
        window hide
        pause
        window show

    menu:
        dragon "Do you think you have figured it out?"
        "I know what the inscription means.":
            dragon "If you truly do, you really must be a genius. What do they say?"
            python:
                guess = renpy.input("What do the inscriptions say?", length=64)
                guess = guess.strip().lower().replace('!', '').replace('?', '').replace('.', '').replace('-', ' ')
            dragon "Alright, that looks promising! Let me give it a try."
            if guess == inscription: 
                dragon "Amazing, I think that's it! A pathway to the treasure room should open any moment now..."
            else:
                dragon "Hmmm... I'm sorry to say, but that doesn't appear to be it."
                dragon "Maybe I just misheard you, but taking another look at it wouldn't hurt either."
                jump puzzle_inscriptions_text
        "I need a hint.":
            dragon "It might look impossible, but it might be easier than you'd think at first glance."
            $ hint = renpy.random.choice([
                "Taking some notes might be of great help. Note down the symbols you have already deciphered.",
                "Look at words consisting of one, two, or three letters. I don't think many such words exist.",
                "Are there any symbols that appear often? In English, the most common letters are E, T, A, O, and N.",
                "Think of context. Dragons probably wrote this. What would dragons write about?",
                "Are there any words that commonly appear at the start of a sentence?",
                "Come to think of it, I do know for a fact that \"{font=clawrite.ttf}dragon{/font}\" stands for dragon!",
                "Funny how some symbols look like letters in the human tongue, though there are some false friends in there."
                ])
            dragon "[hint]"
            jump puzzle_inscriptions_text
    
    hide text
    stop music fadeout 1.0
    jump main_end
