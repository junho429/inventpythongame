import random

guessesTaken = 0

print("음.. 네 이름은 뭐지?")
MyName = input()

number = random.randint(1,20)
print(MyName + '라... 그럼 게임을 시작하지. 내가 1부터 20까지의 숫자를 생각해 놨다')

for guessesTaken in range(6):
    print('한번 맞춰 봐라.')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('니가 생각한 것보다 큰 숫자다.')
    if guess > number:
        print('니가 생각한 것보다 적은 숫자다')
    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('잘 했다, ' + MyName + "!" + guessesTaken + "번만에 정답을 말했군!")

if guess != number:
    number = str(number)
    print('틀렸군. 내가 생각한 숫자는 ' + number + '였다.')