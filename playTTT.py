from random import shuffle, randint
import time
from subprocess import call
import os


def updateBoard(ba, space, mark):
  if space == '1':
    ba[0][0] = mark
  if space == '2':
    ba[0][1] = mark
  if space == '3':
    ba[0][2] = mark
  if space == '4':
    ba[1][0] = mark
  if space == '5':
    ba[1][1] = mark
  if space == '6':
    ba[1][2] = mark
  if space == '7':
    ba[2][0] = mark
  if space == '8':
    ba[2][1] = mark
  if space == '9':
    ba[2][2] = mark


def displayBoard(ba):
  print()
  print(f' {ba[0][0]} | {ba[0][1]} | {ba[0][2]} ')
  print('-----------')
  print(f' {ba[1][0]} | {ba[1][1]} | {ba[1][2]} ')
  print('-----------')
  print(f' {ba[2][0]} | {ba[2][1]} | {ba[2][2]} ')


def introducePlayer():
  print('Welcome to Tic-Tac-Toe!')
  print('On your turn, enter the space you\'d like to mark.')
  print('Three in a row wins.')


def getPlayerMark():
  playerMark = ''
  while playerMark != 'X' and playerMark != 'O':
    playerMark = input('Do you want to play as X or O? ').upper()
    if playerMark != 'X' and playerMark != 'O':
      print("Error. Please enter 'X' or 'O' to continue.")
  if playerMark == 'X':
    return ('X', 'O')
  return ('O', 'X')


def checkWinner(space, playerMark):
  if space == playerMark:
    return 'win'
  return 'lose'


def checkEnd(ba, playerMark, availableSpots):
  if ba[0][0] == ba[0][1] == ba[0][2]:
    return checkWinner(ba[0][0], playerMark)
  if ba[1][0] == ba[1][1] == ba[1][2]:
    return checkWinner(ba[1][0], playerMark)
  if ba[2][0] == ba[2][1] == ba[2][2]:
    return checkWinner(ba[2][0], playerMark)
  if ba[0][0] == ba[1][0] == ba[2][0]:
    return checkWinner(ba[0][0], playerMark)
  if ba[0][1] == ba[1][1] == ba[2][1]:
    return checkWinner(ba[0][1], playerMark)
  if ba[0][2] == ba[1][2] == ba[2][2]:
    return checkWinner(ba[0][2], playerMark)
  if ba[0][0] == ba[1][1] == ba[2][2]:
    return checkWinner(ba[0][0], playerMark)
  if ba[0][2] == ba[1][1] == ba[2][0]:
    return checkWinner(ba[0][2], playerMark)
  if len(availableSpots) == 0:
    return 'draw'
  return ''


def askPlayAgain():
  playAgain = ''

  while playAgain not in ['Y', 'N']:
    playAgain = input("Would you like to play again (Y/N)? ").upper()
  if playAgain not in ['Y', 'N']:
    print("Error. Try again.")

  return playAgain == 'Y'


def playttt():
  ba = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
  availableSpots = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
  continuePlaying = True
  turn = 0
  print()
  playerMark, computerMark = getPlayerMark()

  while continuePlaying:
    call('clear' if os.name == 'posix' else 'cls')
    print(f'You are playing as {playerMark}')

    space = '0'
    displayBoard(ba)
    print()

    if turn % 2 == 0:
      while space not in availableSpots:
        space = input('Your turn. Enter number to play a spot. ')
        if space not in availableSpots:
          print('Invalid entry. Try again.')
      updateBoard(ba, space, playerMark)
    else:
      print("Computer's turn! Thinking", end=' ')
      for i in range(10):
        print('.', end='')
        time.sleep(0.2)
      print()
      shuffle(availableSpots)
      space = str(availableSpots[randint(0, len(availableSpots) - 1)])
      updateBoard(ba, space, computerMark)

    availableSpots.remove(space)

    endState = checkEnd(ba, playerMark, availableSpots)
    if endState == 'win':
      call('clear' if os.name == 'posix' else 'cls')
      print(f'You are playing as {playerMark}')
      displayBoard(ba)
      return 'win'
    elif endState == 'lose':
      call('clear' if os.name == 'posix' else 'cls')
      print(f'You are playing as {playerMark}')
      displayBoard(ba)
      return 'lose'
    elif endState == 'draw':
      call('clear' if os.name == 'posix' else 'cls')
      print(f'You are playing as {playerMark}')
      displayBoard(ba)
      return 'draw'

    turn += 1


def main():

  playAgain = True

  introducePlayer()

  while playAgain:
    outcome = playttt()
    print()

    if outcome == 'win':
      print('Congrats! You win!')
    elif outcome == 'lose':
      print('You lose! Better luck next time.')
    else:
      print('Draw! See ya next time!')

    playAgain = askPlayAgain()


main()
