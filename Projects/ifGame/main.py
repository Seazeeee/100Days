"""
Todo

- Make a logic game using if, else, and elif statements to follow a story.
- Include some ASCII Art.

"""

import random

print('''    
     _                                
    | |                                   
  __| |_   _ _ __   __ _  ___  ___  _ __  
 / _` | | | | '_ \\ / _` |/ _ \\/ _ \\| '_ \\ 
| (_| | |_| | | | | (_| |  __/ (_) | | | |
 \\__,_|\\__,_|_| |_|\\__, |\\___|\\___/|_| |_|
                    __/ |                 
                   |___/                  
      ''')

print("Welcome to the Dungeon!")



while True:
    choice = input('Please type "start": \n' )

    if choice.lower() == "start":
        print('''
                                _________________________________________________________
                /|     -_-                                             _-  |\\
                / |_-_- _                                         -_- _-   -| \\   
                |                            _-  _--                      | 
                |                            ,                            |
                |      .-'````````'.        '(`        .-'```````'-.      |
                |    .` |           `.      `)'      .` |           `.    |          
                |   /   |   ()        \\      U      /   |    ()       \\   |
                |  |    |    ;         | o   T   o |    |    ;         |  |
                |  |    |     ;        |  .  |  .  |    |    ;         |  |
                |  |    |     ;        |   . | .   |    |    ;         |  |
                |  |    |     ;        |    .|.    |    |    ;         |  |
                |  |    |____;_________|     |     |    |____;_________|  |  
                |  |   /  __ ;   -     |     !     |   /     `'() _ -  |  |
                |  |  / __  ()        -|        -  |  /  __--      -   |  |
                |  | /        __-- _   |   _- _ -  | /        __--_    |  |
                |__|/__________________|___________|/__________________|__|
                /                                             _ -        lc \\
                /   -_- _ -             _- _---                       -_-  -_ \\ 
                ''')
        
        choice = input("Please decide which path you take! Right or left? \n")

        if choice.lower() == "right":
            
            print(""" You have taken the right path...you walk in and find yourself surrounded by
                faces of rock.""")
            
            print("""
                    .-----------.         .------------.
                    :`.__________`        :`.____________`  .-----.._
                    '.'_.------._.'       `.|__.-------..'  |`-..___.'|
                    | ||__..| | |-._ __   | | |.... || |-._`--..__ |.'---.
                .::/ / |    | | |  ___  `-| | |  _  || |   | | | | | \\    `.
            _.-.`  -`.|_|    `.|.' /`.  `. '.|_\\     `|.'   | | | | || `.    `.
            '.   `.   `-   _     _  |  `.__`   _          _  `.|.' | ||`. \\     \\
            | `. __`.  _           _ `. |   |     `--   _     _    '.||  \\ `.____.
            /`. |   |  .'`---...____   `'---' _       _          _    | | `.|_..-'
            | /`|__.' |`---...___ . |  `--      ______________________`.|_| |  ` |
            | | | '|  `---...____|.'    _     |`._-_______-______-_____`. | |    |
            .| | |  | _ |  | | | | '| `-       '.|  ' ' '  '  '  '  ' ' ' || |    |  
            ' `| |  |   /  | | |'|  |      _    |'.__.-------.__.-----.__.'| | .- |\\
            |  | |' |   |  | | | |  |   `--   _ | |..|    |  |''|  -| |::| `.|_..-' |
            \\   `|_.' _ |  | |_| '. | .`-._     | |  | -  |  |  | _ | |  | `--     .'
            '.         |  | | |  | | |`.  `. _ | |  |  _ |  |  |   | |  |   _    `.
            '-. _    '._|.' |  | | |  `.__`. | |  | __ |  |  |__ | |  |  `-- _  |
                `''''.    _  `-.|.' '.  |   |  `|__| ___ `.|__| _ `.|__|        /
                    :    _    _      `.|_.-'   `-             _          _   .'
                        `-._______.::.__     `-     _      _       ___.:::.__.-'
                    """)
            print("You will now have the option to roll a dice to decide your fate. Choose wisely...")
            choice = input("A monster now stands before you...do you decide to fight (even) or hide (odds)? \n")

            if choice.lower() == "fight":
                chance = random.randint(1, 6)

                if (chance % 2) == 0:
                    print("YOU HAVE FOUGHT AND WON! Enjoy your loot.")
                    print("""
                                        _.--.
                                    _.-'_:-'||
                                _.-'_.-::::'||
                        _.-:'_.-::::::'  ||
                        .'`-.-:::::::'     ||
                        /.'`;|:::::::'      ||_
                    ||   ||::::::'     _.;._'-._
                    ||   ||:::::'  _.-!oo @.!-._'-.
                    \\'.  ||:::::.-!()oo @!()@.-'_.|
                        '.'-;|:.-'.&$@.& ()$%-'o.'\\U||
                        `>'-.!@%()@'@_%-'_.-o _.|'||
                        ||-._'-.@.-'_.-' _.-o  |'||
                        ||=[ '-._.-\\U/.-'    o |'||
                        || '-.]=|| |'|      o  |'||
                        ||      || |'|        _| ';
                        ||      || |'|    _.-'_.-'
                        |'-._   || |'|_.-'_.-'
                            '-._'-.|| |' `_.-'
                                '-.||_/.-'
                        """)
                    
                    contQuestion = input("Would you like to play again? Y/N \n")
                    
                    if contQuestion.lower() == "y":
                        pass
                    else:
                        break

                else:
                    print("You have died...Try again!")

                    contQuestion = input("Would you like to play again? Y/N \n")
                    
                    if contQuestion.lower() == "y":
                        pass
                    else:
                        break

            elif choice.lower() == "hide":
                chance = random.randint(1, 6)

                if (chance % 2) != 0:
                    print("You watched as the monster walked by! Enjoy your loot.")
                    print("""
                                        _.--.
                                    _.-'_:-'||
                                _.-'_.-::::'||
                        _.-:'_.-::::::'  ||
                        .'`-.-:::::::'     ||
                        /.'`;|:::::::'      ||_
                    ||   ||::::::'     _.;._'-._
                    ||   ||:::::'  _.-!oo @.!-._'-.
                    \\'.  ||:::::.-!()oo @!()@.-'_.|
                        '.'-;|:.-'.&$@.& ()$%-'o.'\\U||
                        `>'-.!@%()@'@_%-'_.-o _.|'||
                        ||-._'-.@.-'_.-' _.-o  |'||
                        ||=[ '-._.-\\U/.-'    o |'||
                        || '-.]=|| |'|      o  |'||
                        ||      || |'|        _| ';
                        ||      || |'|    _.-'_.-'
                        |'-._   || |'|_.-'_.-'
                            '-._'-.|| |' `_.-'
                                '-.||_/.-'
                        """)
                    
                    contQuestion = input("Would you like to play again? Y/N \n")
                    
                    if contQuestion.lower() == "y":
                        pass
                    else:
                        break

                else:
                    print("You have died...Try again!")

                    contQuestion = input("Would you like to play again? Y/N \n")
                    
                    if contQuestion.lower() == "y":
                        pass
                    else:
                        break
            else:
                print("You have selected an unknown option. Try again!")
                continue



        elif choice.lower() == "left":
            print("You have chosen the left entrance. When you walk inside you see a skeleton!")

            print("""
                                        ,--,  ,.-.
                ,                   \\,       '-,-`,'-.' | ._
                /|           \\    ,   |\\         }  )/  / `-,',
                [ '          |\\  /|   | |        /  \\|  |/`  ,`
                | |       ,.`  `,` `, | |  _,...(   (      _',
                \\  \\  __ ,-` `  ,  , `/ |,'      Y     (   \\_L\\
                \\  \\_\\,``,   ` , ,  /  |         )         _,/
                \\  '  `  ,_ _`_,-,<._.<        /         /
                ', `>.,`  `  `   ,., |_      |         /
                    \\/`  `,   `   ,`  | /__,.-`    _,   `\\
                -,-..\\  _  \\  `  /  ,  / `._) _,-\\`       \\
                \\_,,.) /\\    ` /  / ) (-,, ``    ,        |
                ,` )  | \\_\\       '-`  |  `(               \\
                /  /```(   , --, ,' \\   |`<`    ,            |
                /  /_,--`\\   <\\  V /> ,` )<_/)  | \\      _____)
        ,-, ,`   `   (_,\\ \\    |   /) / __/  /   `----`
        (-, \\           ) \\ ('_.-._)/ /,`    /
        | /  `          `/ \\\\ V   V, /`     /
    ,--\\(        ,     <_/`\\\\     ||      /
    (   ,``-     \\/|         \\-A.A-`|     /
    ,>,_ )_,..(    )\\          -,,_-`  _--`
    (_ \\|`   _,/_  /  \\_            ,--`
    \\( `   <.,../`     `-.._   _,-`
                """)
            
            print("You will now have the option to roll a dice to decide your fate. Choose wisely...")
            choice = input("A monster now stands before you...do you decide to fight (even) or run (odds)? \n")
            
            if choice.lower() == "fight":
                chance = random.randint(1, 6)

                if (chance % 2) == 0:
                    print("YOU HAVE FOUGHT AND WON! Enjoy your loot.")
                    print("""
                                        _.--.
                                    _.-'_:-'||
                                _.-'_.-::::'||
                        _.-:'_.-::::::'  ||
                        .'`-.-:::::::'     ||
                        /.'`;|:::::::'      ||_
                    ||   ||::::::'     _.;._'-._
                    ||   ||:::::'  _.-!oo @.!-._'-.
                    \\'.  ||:::::.-!()oo @!()@.-'_.|
                        '.'-;|:.-'.&$@.& ()$%-'o.'\\U||
                        `>'-.!@%()@'@_%-'_.-o _.|'||
                        ||-._'-.@.-'_.-' _.-o  |'||
                        ||=[ '-._.-\\U/.-'    o |'||
                        || '-.]=|| |'|      o  |'||
                        ||      || |'|        _| ';
                        ||      || |'|    _.-'_.-'
                        |'-._   || |'|_.-'_.-'
                            '-._'-.|| |' `_.-'
                                '-.||_/.-'
                        """)
                    contQuestion = input("Would you like to play again? Y/N \n")
                    
                    if contQuestion.lower() == "y":
                        pass
                    else:
                        break

                else:
                    print("You have died...Try again!")
                    contQuestion = input("Would you like to play again? Y/N \n")
                    
                    if contQuestion.lower() == "y":
                        pass
                    else:
                        break

            elif choice.lower() == "run":
                chance = random.randint(1, 6)

                if (chance % 2) != 0:
                    print("You ran past the slow monster!! Enjoy your loot.")
                    print("""
                                        _.--.
                                    _.-'_:-'||
                                _.-'_.-::::'||
                        _.-:'_.-::::::'  ||
                        .'`-.-:::::::'     ||
                        /.'`;|:::::::'      ||_
                    ||   ||::::::'     _.;._'-._
                    ||   ||:::::'  _.-!oo @.!-._'-.
                    \\'.  ||:::::.-!()oo @!()@.-'_.|
                        '.'-;|:.-'.&$@.& ()$%-'o.'\\U||
                        `>'-.!@%()@'@_%-'_.-o _.|'||
                        ||-._'-.@.-'_.-' _.-o  |'||
                        ||=[ '-._.-\\U/.-'    o |'||
                        || '-.]=|| |'|      o  |'||
                        ||      || |'|        _| ';
                        ||      || |'|    _.-'_.-'
                        |'-._   || |'|_.-'_.-'
                            '-._'-.|| |' `_.-'
                                '-.||_/.-'
                        """)
                    contQuestion = input("Would you like to play again? Y/N \n")
                    
                    if contQuestion.lower() == "y":
                        pass
                    else:
                        break

                else:
                    print("You have died...Try again!")
                    pass
            else:
                print("You have selected an unknown option. Try again!")
                continue
        else:
            print("You have selected an unknown option. Try again!")
            continue



    else:
        print('Retry. Please make sure you type "start"')
        continue