############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
import replit
import random
import art

print(art.logo)

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def blackjack(play_blackjack, deck, cont):
  '''The main game of Blackjack. Takes user choice to play from play_blackjack = input and uses this value to keep player in game of Blackjack.'''

  cont = True

  player_hand = []
  computer_hand = []

  another_hand = ''

  blackjackp = False
  blackjackc = False


  while cont:    
      #gives computer their hand, only one card as player can only see one card of the dealers.
      for chand in range(1,2):
        computer_hand.append(random.choice(deck))
      
      #deals player their hand and prints both their hand and computer's hand
      for phand in range(1,2):
        player_hand.append(random.choice(deck))
        if player_hand == [11, 10] or [10, 11]:
          print("Your hand is Blackjack!")
          blackjackp = True
          if computer_hand == [11, 10] or [10, 11]:
            print("The dealer has Blackjack!")
            blackjackc = True
          #victory(blackjackp, blackjackc)
        print(f"Your hand is: {player_hand}")
        print(f"The dealer's hand is: {computer_hand[0]}")
      hit_or_stick(player_hand, computer_hand, deck)

def hit_or_stick(player_hand, computer_hand, deck):      
  '''gives player option to hit or stick with their dealt hand'''

  hit = True
  hit_choice = ''
  final_countp = 0


  while hit: 
    hit = input("would you like to 'hit' or 'stick'?")
    if hit_choice.lower() == 'hit':
      player_hand.append(random.choice(deck))
      for count in player_hand:
        final_countp += count
      hit_or_stick(player_hand, computer_hand)
    elif hit_choice.lower() == 'stick':
      stick(final_countp, player_hand, computer_hand, deck)
      return player_hand, computer_hand
    else:
      print("Please enter 'hit' or 'stick'.")
      hit_or_stick(player_hand, computer_hand, deck)

def stick(final_countp, player_hand, computer_hand, deck):
  
  final_countc = 0

  for chand in computer_hand:
    final_countc += chand
  if final_countc < 17:
    computer_hand.append(random.choice(deck))
    stick(final_countp, player_hand, computer_hand, deck)
  elif final_countc < final_countp:
    computer_hand.append(random.choice(deck))
    stick(final_countp, player_hand, computer_hand, deck)
  #elif final_countc > final_countp and final_countc <= 21:
    #victory(final_countp, final_countc, player_hand, computer_hand)
  #else:
    #victory(final_countp, final_countc, player_hand, computer_hand)

def another_hand():
  another_hand = input("Would you like to play another hand? 'y' or 'n': ")
            
  if another_hand.lower() == 'y':
    replit.clear()
    blackjack(play_blackjack, deck)
  elif another_hand.lower() == 'n':
    return
  else:
    print("please enter 'y' or 'n'.")
    another_hand()

def victory(final_countp, final_countc, player_hand, computer_hand, blackjackp, blackjackc):

   if final_countp > 21 and final_countc > 21:
     print("You have both gone bust, it's a draw!")
     print(f" Your score: {final_countp} Dealer's score: {final_countc}")

play_blackjack = input("Would you like to play a game of Blackjack? 'y' or 'n': ")

if play_blackjack.lower() == 'y':
  cont = True
if play_blackjack.lower() == 'n':
  cont = False

blackjack(play_blackjack, deck, cont)
