let morseToChar = {
    "A" : ".-",
    "B" : "-...",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "..-.",
    "G" : "--.",
    "H" : "....",
    "I" : "..",
    "J" : ".---",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "--..",
    "1" : ".----",
    "2" : "..---",
    "3" : "...--",
    "4" : "....-",
    "5" : ".....",
    "6" : "-....",
    "7" : "--...",
    "8" : "---..",
    "9" : "----.",
    "0" : "-----",
}

let morseChar = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
let morseCode = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", "-----"]
let DotS = sprites.create(img`
    . . . . .
    . . 3 . .
    . . . . .
`)
let Question = sprites.create(img`
    . . . . .
    . . 3 . .
    . . . . .
`)
let input_code = ""
let choise_chr_index = 0
let choise_chr = ""
function choise() {
    
    choise_chr_index = randint(0, morseCode.length + 1)
    choise_chr = morseChar[choise_chr_index]
    input_code = ""
}

function dot() {
    
    input_code = input_code + "."
}

function dash() {
    
    input_code = input_code + "-"
}

function show() {
    // game.splash(input_code)
    DotS.say(input_code)
    Question.say(choise_chr)
}

function parse() {
    
    if (morseCode[choise_chr_index] == input_code) {
        game.splash("correct answer")
        info.changeScoreBy(1)
    } else {
        game.splash("wrong answer " + choise_chr + ": " + morseCode[choise_chr_index] + " you: " + input_code)
        info.changeLifeBy(-1)
    }
    
    choise()
    show()
    
}

controller.player1.onButtonEvent(ControllerButton.Left, ControllerButtonEvent.Pressed, function on_button_event_left_pressed() {
    dot()
    show()
    
})
controller.player1.onButtonEvent(ControllerButton.Right, ControllerButtonEvent.Pressed, function on_button_event_right_pressed() {
    dash()
    show()
    
})
controller.player1.onButtonEvent(ControllerButton.B, ControllerButtonEvent.Pressed, function on_button_event_a_pressed() {
    parse()
    
})
function mode_1() {
    Question.setPosition(30, 30)
    info.setScore(0)
    info.setLife(3)
    choise()
    show()
    game.splash("Test Mode")
}

if (game.ask("请选择模式", "A: 测试/ B: ID")) {
    mode_1()
} else {
    game.splash("ID")
}

