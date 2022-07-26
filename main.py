#! /usr/bin/python3 -i
art = r"""
                       ,---.
                       /    |
                      /     |
                     /      |
                    /       |
               ___,'        |
             <  -'          :        ┌ You shall not
              `-.__..--'``-,_\_      │      PASS!
                 |o/ ` :,.)_`>       │
                 :/ `     ||/)      ─┘
                 (_.).__,-` |\
                 /( `.``   `| :
                 \'`-.)  `  ; ;
                 | `       /-<
                 |     `  /   `.
 ,-_-..____     /|  `    :__..-'\
/,'-.__\\  ``-./ :`      ;       \
`\ `\  `\\  \ :  (   `  /  ,   `. \
  \` \   \\   |  | `   :  :     .\ \
   \ `\_  ))  :  ;     |  |      ): :
  (`-.-'\ ||  |\ \   ` ;  ;       | |
   \-_   `;;._   ( `  /  /_       | |
    `-.-.// ,'`-._\__/_,'         ; |
"""
while True:
    try:
        print(art)
        exec(input(">>> "))
    except KeyboardInterrupt:
        print()
    except EOFError:
        print()
        break
    except Exception as e:
        print(e)
