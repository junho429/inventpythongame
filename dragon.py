import random
import time

def displayIntro():
    print('''당신은 드레곤으로 가득 한 땅에 있다. 당신의 앞에는, 두 개의 동굴이 있다.
    한 동굴에는, 친절한 드래곤이 보물을 당신과 공유할 것이다. 다른 동굴에는 욕심 많고 배고픈 
    드레곤이 있어, 보자마자 당신을 잡아먹을 것이다.
    ''')
    print()
def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('어느 동굴로 들어가시겠습니까(1또는 2중 선택하십시오)')
        cave = input()
    return cave

def checkCave(chosenCave):
    print('당신은 동굴로 들어간다...')
    time.sleep(2)
    print('여기는 어둡고 으시시하다...')
    time.sleep(2)
    print('커다란 드레곤이 당신의 앞으로 점프해 왔다! 그는 입을 열어...')
    print()
    time.sleep(2)

    friendlycave= random.randint(1,2)
    if chosenCave == str(friendlycave):
        print('보물을 주었다!')
    else:
        print('당신을 한 입에 먹어버렸다!')


playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('다시 플레이하시겠습니까(yes or no)')
    playAgain = input()