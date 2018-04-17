import random
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']


words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

failedNumber = 0
correctLetter = []
wrongLetter = []

'''기본적인 게임 화면을 출력합니다.'''
def displayScreen(word):
    print(HANGMAN_PICS[failedNumber])
    print('Missed letters:')
    for letter in word:
        if letter in correctLetter:
            print(letter,end = ' ')
        else:
            print('_', end = " ")
    print()
    
'''words에서 단어를 렌덤하게 선택합니다'''
def selectword():
    return words[random.randint(0,len(words))]

'''사용자의 입력을 받아 올바른 입력인지 검증합니다.'''
def userInput():
    print("Guess a letter:")
    userinput = input()
    return userinput

print("H A N G M A N")
word = selectword()
print("debug: 선택된 단어: " + word)

while True:
    displayScreen(word)
    guessedLetter = userInput()
    #단어 안에 guessesLetter가 있는지 확인 후 처리합니다.
    if guessedLetter in word:
        correctLetter.append(guessedLetter)
    else:
        wrongLetter.append(guessedLetter)
        failedNumber += 1
    


input()
