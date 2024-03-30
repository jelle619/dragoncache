image bg puzzle trivia = "images/backgrounds/puzzle_trivia.webp"

label puzzle_trivia:
    scene bg puzzle trivia
    play music "audio/bgm/puzzle.opus"

    dragon "This puzzle is... oh no. This doesn't even make any sense..."
    dragon "It is a trivia quiz about dragons in human media, culture and mythology."
    dragon "I know nothing about those crazy tales your kind comes up with. I won't be able to give you any hints."
    dragon "Luckily, it seems you're allowed to make mistakes. You only need to answer 10 questions correctly."
    dragon "Alright, let's get started. Wish you the most of luck."

    $ score = 0 # variable that tracks the trivia score.

    menu:
        "In which mythology are dragons most commonly found?"
        "Greek mythology":
            $ score += 0
        "Norse mythology":
            $ score += 0
        "Egyptian mythology":
            $ score += 0
        "Chinese mythology":
            $ score += 1
    menu:
        "Which author is known for his series 'A Song of Ice and Fire', which features dragons?"
        "J.R.R. Tolkien":
            $ score += 0
        "George R.R. Martin":
            $ score += 1
        "J.K. Rowling":
            $ score += 0
        "C.S. Lewis":
            $ score += 0
    menu:
        "In the movie 'How to Train Your Dragon', what is the name of the protagonist's dragon?"
        "Toothless":
            $ score += 1
        "Smaug":
            $ score += 0
        "Draco":
            $ score += 0
        "Mushu":
            $ score += 0
    menu:
        "In the film 'Pete's Dragon', what is the name of the friendly dragon?"
        "Elliot":
            $ score += 1
        "Spike":
            $ score += 0
        "Norbert":
            $ score += 0
        "Pete":
            $ score += 0
    menu:
        "Which animated movie features a dragon named Mushu?"
        "Mulan":
            $ score += 1
        "Frozen":
            $ score += 0
        "Moana":
            $ score += 0
        "Tangled":
            $ score += 0
    menu:
        "In the Harry Potter series, what kind of breed is the dragon that Harry faces in the Triwizard Tournament?"
        "Chinese Fireball":
            $ score += 0
        "Swedish Short-Snout":
            $ score += 0
        "Hungarian Horntail":
            $ score += 1
        "Ukrainian Ironbelly":
            $ score += 0
    menu:
        "What is the name of the dragon in the book 'The Hobbit' by J.R.R. Tolkien?"
        "Smaug":
            $ score += 1
        "Drogon":
            $ score += 0
        "Falkor":
            $ score += 0
        "Toothless":
            $ score += 0
    menu:
        "Which video game series features a protagonist who has an inherent connection to dragons?"
        "The Elder Scrolls":
            $ score += 1
        "Final Fantasy":
            $ score += 0
        "Assassin's Creed":
            $ score += 0
        "Grand Theft Auto":
            $ score += 0
    menu:
        "In the animated film 'Shrek', what is the name of the dragon that falls in love with Donkey?"
        "Puff":
            $ score += 0
        "Smokey":
            $ score += 0
        "Fiona":
            $ score += 0
        "Dragon":
            $ score += 1
    menu:
        "What is the name of the dragon in the Disney movie 'Sleeping Beauty'?"
        "Maleficent":
            $ score += 1
        "Draco":
            $ score += 0
        "Mushu":
            $ score += 0
        "Figment":
            $ score += 0
    menu:
        "Which dragon is often described as having multiple heads in Greek mythology?"
        "Hydra":
            $ score += 1
        "Chimera":
            $ score += 0
        "Wyvern":
            $ score += 0
        "Leviathan":
            $ score += 0
    menu:
        "Which of these dragons does not appear in the TV show 'Game of Thrones'?"
        "Drogon":
            $ score += 0
        "Viserion":
            $ score += 0
        "Rhaegal":
            $ score += 0
        "Argyrth":
            $ score += 1
    menu:
        "In the animated film 'How to Train Your Dragon', what type of dragon is the protagonist's companion?"
        "Night Fury":
            $ score += 1
        "Deathgripper":
            $ score += 0
        "Skrill":
            $ score += 0
        "Monstrous Nightmare":
            $ score += 0
    
    if score >= 10:
        dragon "You made it!"
        
    else:
        dragon "Unfortunately, you've made too many mistakes. You got [score] out of 13 questions correctly."
        dragon "If only you had an electronic device with you... You could have maybe asked a friend, or searched online."
        dragon "Your kind's twisted dragon tales are confusing for sure. However, we have to give this another try..."
        jump puzzle_trivia
    
    stop music fadeout 1.0
    jump main_end