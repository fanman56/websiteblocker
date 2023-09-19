from logic import Website
import os
from rich.prompt import Prompt
from rich.console import Console

command_ = ""
console_ = Console()
console_.print("""[cyan]
                                    !7.                          7G5.                               
                                   ^@#.                          !5J.   ~7                          
      ..    ...    ..    .:^^:     J@Y :^^.            .^^^.     ..  .:^@B::.    .:^^:              
     ~&P   ~&&Y   ?@J  ^5BG5P#B~   G@G555B#J         !GBP5PGP:  :&B. ?P#@B55:  ^5BP5P#G~            
     :@#. .&PBB  ^@G  !@#^   5@P  :@&!.  .#@!       .&@7    :   ?@P   .#@^    7@B^   P@5            
      B@: G# P& .#&: :&@J!?YP#5:  7@P     G@7        ~PBBGY!    P@7   ~@B    :&@?!?YG#5:            
      P@^J@^ Y@:5@!  ~@@J?7!:     P@7    !@#.           :~P@P  .&@:   J@Y    ~@&J?7~:               
      ?@P@?  ?@P@J   .G@Y:::~J:  .&@!::^Y@B^       .J7^::^5@P  !@G    P@J:~: .B@J:::!J:             
      ^PPJ   ^PPJ     .7PGPP5?:  .J5PPPPY!         .75PPPPY!   7P!    ^5GPP!  .?PGPP5?:                        
                                                                                                    
                                 ~J~                 ~J^                                            
                   !#BPPPPPJ:    G@!                .#@^                                            
                   5@Y...:?@#.  :@&.     .~~~^.     ~@B :~!^.      ^~!~:     :. :~~.                
                  .#@~   .J@P   7@P    ~G#PY5B#?    J@G5PY5&#~  .J#G5YP&P.  !@P5BG5.                
                  ~@@PPPG&B!    P@7   ?@B:   .B@7   B@G^  .#@! .B@?   ^@@^  Y@&7.                   
                  J@P:^^^!B&7  .&@:  ^@@:     G@?  :@&.:?YGP~  J@B7?YPBP!   #@!                     
                  B@!     P@5  !@G   !@#     ~@#:  ?@P ^#@7    P@G7!~:     ^@#                      
                 ^@@7!!7?G@P:  J@P^  .G@Y~^~Y@B^   G@7  :B@7   !&&7^^~J?   J@5                      
                 ^YYYYYYJ7^    :YP5:   !Y5P5Y~     JY.   :YY:   :?5PP5J~   7Y^ [/]""")
# main loop for checking and connecting the user with the logic
while command_.lower() != "exit":
    x = Prompt.ask("[bold][red on cyan]@WEB_Blocker-V0.1 [/][cyan]>>>  ")
    command_, *website = [i for i in x.split() if x != ""]
    # check
    if command_.lower() == "block":
        web = Website(website)
        web.block()

    elif command_.lower() == "unblock":
        web = Website(website)
        web.unblock()

    elif command_.lower() == "list":
        web = Website("")
        web.readlist()

    elif command_ == "clear":
        os.system('cls')
    elif command_.lower() == "help":
        console_.print(
            "[yellow]USE BLOCK TO BLOCK SITE  FOR E.G:  Block youtube.com\nTHE SAME GOES TO UNBLOKEING .\nCLEAR TO CLEAN THE TERMINAL \nIF YOU WANT TO SEE BLOCKED SITES TYPE > LIST \n YOU CAN CLOSE THE THE SW BY TYPING EXIT EASY AS THAT ![/]")
    elif command_ == "exit":
        break
    else:
        console_.print(
            "[yellow]Enter correct command or use help to see diffrent options ![/]")
