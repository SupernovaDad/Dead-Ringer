define n = Character("Nigel")
define d = Character("Digby")
define y = Character("[name]")
define z = Character("???")
define N = Character(what_italic=True)
define slowdissolve = Dissolve(1.0)

label start:

    python:
        name = renpy.input("What's your name?")

        name = name.strip()

    scene intro_1
    with slowdissolve
    N "You find yourself watching your favorite MeTube musicians late at night."
    N "You only discovered this new genre of music recently, but it quickly became one of your favorites to listen to."
    N "You're also surprisingly invested in their silly, one off characters that they play despite them not having much substance."
    N "You feel like you could watch these videos for hours, there's still so much you have yet to see."
    N "You yawn as you stretch your back, a loud pop resonates throughout the room."
    N "You look at the time and realize just how late it is."

    scene intro_2
    with slowdissolve
    N "You get up from your computer and head to bed, more exhausted than you realized."

    scene intro_3
    with slowdissolve

    scene intro_4
    with slowdissolve
    N "A bright red light emits from your monitor."
    N "Your computer starts to hum as hands begin reach through the LCD display."

scene black
show bg park table:
    xzoom .60 yzoom .60 xalign 0.5
with slowdissolve
N "It was a beautiful day, you decide to get out of the house to take advantage of the gorgeous weather."
N "You find yourself walking in the park as you see someone playing Battleship™ by themselves."
N "They appear to be losing."
N "You approach the stranger as you realize that they're too engrossed in their task to even notice you."

menu:
    "Say Hi":
        jump choice1_yes

    "Tap them on the shoulder":
        jump choice1_no

label choice1_yes:

    $ menu_flag = True

    y "...Hello?"

    N "The stranger jumps as they knock over a peg."

    jump choice1_done

label choice1_no:

    $ menu_flag = False

    N "You tap the stranger on the shoulder. The stranger jumps and lets out a yelp."

    jump choice1_done

label choice1_done:

z "Oh, my apologies, I didn't see you there"

menu:
    "Tell them it's okay":
        jump choice2_yes1

    "Ask them where the other player is":
        jump choice2_no1

label choice2_yes1:

    $ menu_flag = True

    y "Don't worry, it's alright."
    y "What are you doing if you don't mind me asking?"
    z "I'm honing my craft."
    z "You see, I'm a bit of a board game enthusiast."
    y "Wouldn't it be better if you played with someone else, to give yourself a bit of a challenge?"
    z "I've tried."
    z "But none of my friends really want to go against me anymore."

jump choice2_done

label choice2_no1:

    $ menu_flag = False

    y "Who are you playing against?"
    z "I'm playing against myself."
    z "I'm trying to hone my skills."

jump choice2_done

label choice2_done:

    z "Excuse me, where are my manners?"
    z "My name's The Chairman."
    n "But you can just call me Nigel."
    n "And you are?..."
    y "The name's [name]"
    y "Would it be okay if I joined you?"
    n "Does using all 7 tiles in Scrabble™ give you a 50 point bonus?"
    N "..."
    N "Huh?"
    n "Yes."
    n "The answer's yes."
    N "You sit down at the bench and look down at the board, pieces scattered from a game unfinished."
    N "You assemble your fleet and get to work."
    N ". . ."
    N "A few minutes pass and you slowly begin to realize that you're losing horribly."
    N "A smug grin spreads against Nigel's face."
    N "At this point, there's a strong likelyhood that any hit will result in you losing."
    N "Nigel swiftly lands on your last peg as they laugh triumphantly and fold their arms."
    N "Nigel reaches out their hand, as if extending their hand to friendship."
    n "Well played."
    n "You really had me there."
    N "You know they're just trying to butter you up but they're being nice so you accept their compliment."
    n "Say..."
    n "Would you like to accompany me to my place?"
    n "You see, I've been looking for someone to test my wits and well..."
    n "You're the only person in a long time to offer to play with me."
    N "You're unsure if you should go with them."
    N "I mean, you only just met them."

    menu:
        "Agree to go with them":
            jump choice3_yes2

        "Ask what's in it for you":
            jump choice3_no2
        
        "Refuse their offer":
            jump choice1picked

label choice3_yes2:

    $ menu_flag = True

    scene bg city
    with slowdissolve

    N "You decide to go with them, they usher you in their direction as you both make it back to their place."
    N "The sun begins to set as you make it to an apartment complex."
    N "You make your way up the elevator as you make it to apartment number 302."

jump choice3_done

label choice3_no2:

    $ menu_flag = False

    y "What's in it for me if I do go with you?"
    n "I can get you free tickets to a tournement I'm going to be competing in."
    y "Deal."

    scene bg city

    N "You decide to go with them, they usher you in their direction as you both make it back to their place."
    N "The sun begins to set as you make it to an apartment complex."
    N "You make your way up the elevator as you make it to apartment number 302."

jump choice3_done

label choice1picked:
   
    $ choice1picked = True

    hide bg park table

    N "Really?"
    N "You're just gonna leave now?"
    N "You're not even going to play the game?"
    N "Fine."
    N "Leave then."
    N "Upon leaving, you decide to take a brisk walk in the middle of the street."
    N "You don't hear the bus barrling towards you because you have your {size=+10}stupid{/size} little headphones in."
    N "The bus hits you and you die."
    N "Immediately."
    N "And thus ends the tale of Insert Name Here" 
    return

label choice3_done:

    scene black

    n "Welcome to my They Cave!"
    n "Be wary of the boards, I'd hate to lose weeks of progress."
    N "Scattered around are several games of Monopoly™, seemingly in different stages of progression, all meticulously arranged."
    N "It looks as if they're part of one larger game."
    n "5th-Dimensional Monopoly™, it's all the rage these days!"
    n "At least, within the confines of this room that is."
    N "Your eyes scan the room for the game board."
    N "You quickly spot it already set up at a table sitting in the corner."
    n "Come— Sit, sit."
    N "They gesture towards a small stool adjacent to the table."
    N "As you sit down you feel your surroundings begin to shift."
    N "Papers flutter, game pieces begin to scatter, the ground rumbles beneath your feet."
    n "Oh, don't worry about that, this just happens sometimes."
    N "They crack their neck and look you dead in the eye."
    n "I told you, I haven't had anyone to challenge in a while."
    n "You should go first."
    n "Please, I insist."

    menu:
        "YOU WIN!!!!":
            jump choice4_yes3

        "YOU LOSE!!!!":
            jump choice4_no3

label choice4_yes3:

    $ menu_flag = True

    y "Oh, it looks like I won!"
    N "Nigel begins to visibly shake, clearly mad at something."
    N "They dig their fingernails into the table, leaving a carved trail."
    n "{size=+10}HOW DID YOU-{/size}"
    N "They quickly stand up, clenching their fists."
    N "You stand up in response to their sudden shift in demeanor."
    N "An aura of pure vitriol radiates off of them."
    N "You feel the room start to spin. Their hate fills your lungs."
    N "You stumble as you lose your footing."
    N "But, just as quickly as you felt their anger, it dissapears."
    N "Fading away as they regained their composure."
    n "I'm so sorry, I don't know what overcame me." 
    n "I just havent lost that bad in quite a while or, well, ever."
    N "Nigel stops to think for a moment"
    n "Well, there is ONE board game I am quite the expert at."
    N "They pull an unlabled, dusty board game off the shelf."
    n "It takes a lot of nerve to come here and challenge me."
    n "So, lets see how much nerve you've got when I SCRABOPOLY™ YOU."


    jump choice4_done 

    label choice4_no3:
    $ menu_flag = False

    n "Hah! Looks like I win again!"
    n "That makes it... What? 37 times in a row?"
    n "Not like I'm counting or anything."
    y "You sure do live up to your title, huh."
    n "Yes, yes. Care for a refreshment?"
    n "You must be parched by now."
    N "You nod."
    N "After a few minutes, Nigel returns with two glasses of lemonade."
    n "Here you are."
    N "They hand you an ice cold glass, you grab it and take a sip."
    n "You know, I'm really glad that you decided to hang out with me today."
    n "Not many people come over anymore if I'm going to be frank."
    

label choice4_done:

return