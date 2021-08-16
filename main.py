
morseToChar = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
                'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                'Y': '-.--', 'Z': '--..', '1': '.----',
                '2': '..---', '3': '...--', '4': '....-',
                '5': '.....', '6': '-....', '7': '--...',
                '8': '---..', '9': '----.', '0': '-----'}

morseChar = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
            'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7',
            '8', '9', '0']
morseCode = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....',
            '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.',
            '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '.----',
            '..---', '...--', '....-', '.....', '-....', '--...', '---..',
            '----.', '-----']

DotS = sprites.create(img("""
    . . . . .
    . . 3 . .
    . . . . .
"""))
Question = sprites.create(img("""
    . . . . .
    . . 3 . .
    . . . . .
"""))

input_code = ""
choise_chr_index = 0
choise_chr = ""
def choise():
    global choise_chr,input_code,choise_chr_index
    choise_chr_index = randint(0, len(morseCode)+1)
    choise_chr = morseChar[choise_chr_index]
    input_code=""
def dot():
    global input_code
    input_code = input_code + "."
def dash():
    global input_code
    input_code = input_code + "-"
def show():
    #game.splash(input_code)
    DotS.say(input_code)
    Question.say(choise_chr)

def parse():
    global morseToChar,choise_chr,choise_chr_index
    if morseCode[choise_chr_index] == input_code:
        game.splash("correct answer")
        info.change_score_by(1)
    else:
        game.splash("wrong answer "+choise_chr+": "+morseCode[choise_chr_index]+" you: "+input_code)
        info.change_life_by(-1)
    choise()
    show()
    pass
def on_button_event_left_pressed():
    dot()
    show()
    pass
controller.player1.on_button_event(ControllerButton.LEFT, ControllerButtonEvent.PRESSED, on_button_event_left_pressed)

def on_button_event_right_pressed():
    dash()
    show()
    pass
controller.player1.on_button_event(ControllerButton.RIGHT, ControllerButtonEvent.PRESSED, on_button_event_right_pressed)


def on_button_event_a_pressed():
    parse()
    pass
controller.player1.on_button_event(ControllerButton.B, ControllerButtonEvent.PRESSED, on_button_event_a_pressed)

def mode_1():

    Question.set_position(30, 30)
    info.set_score(0)
    info.set_life(3)
    choise()
    show()
    game.splash("Test Mode")


if game.ask("请选择模式","A: 测试/ B: ID"):
    mode_1()    
else:
    game.splash("ID")