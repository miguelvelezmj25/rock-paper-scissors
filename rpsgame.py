import sys
import random

__author__ = 'Miguel Velez'

_ROCK = 'rock'
_PAPER = 'paper'
_SCISSORS = 'scissors'

_RULES = {_SCISSORS: _PAPER, _PAPER: _ROCK, _ROCK: _SCISSORS}
_HANDS = [_ROCK, _PAPER, _SCISSORS]


# Get the computers move
def get_computer_move():
    computer_move = _HANDS[random.randint(0, 2)]
    
    print 'Computer move: ' + computer_move
    
    return computer_move
    

def determine_winner(user_move, computer_move):
    if computer_move == _RULES[user_move]:
        print 'You win!'
        
    elif user_move == _RULES[computer_move]:
        print 'You lose!'
        
    elif user_move == computer_move:
        print 'You tied'
        
    else:
        print 'What happened?'
        
    print


# Main logic of the game
def play():    
    while True:
        user_move = raw_input('Enter your move: ')
                
        if len(user_move) < 1:
            print 'You did not enter your move\n'
            
            continue
                
        if user_move in _HANDS:            
            user_move = user_move.lower()
            computer_move = get_computer_move()
            
            determine_winner(user_move, computer_move)
            
        elif user_move.lower() == 'quit':
            print 'Bye bye!'
            sys.exit(0)
            
        else:
            print 'You did not enter a valid move\n'


# Main method that welcomes the user to the game
def main():
    print '\n\n'
    print '******************************************************'
    print '*       WELCOME TO THE ROCK PAPER SCISSORS GAME      *'
    print '*                                                    *'
    print '* Type \'quit\' to quit the game                       *'
    print '* Type \'rock\', \'paper\', \'scissors\' to  play the game *'
    print '******************************************************'
    print '\n\n'
    
    # Call the main logic of the game
    play()
    
# Initialize the program
if __name__ == '__main__':
    main()
