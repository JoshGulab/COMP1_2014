



# Skeleton Program code for the AQA COMP1 Summer 2014 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA Programmer Team
# developed in the Python 3.2 programming environment
# version 2 edited 06/03/2014

######test change#############

import random
import datetime
date = datetime.datetime.now()

NO_OF_RECENT_SCORES = 3

class TCard():
  def __init__(self):
    self.Suit = 0
    self.Rank = 0

class TRecentScore():
  def __init__(self):
    self.Name = ''
    self.Score = 0
    self.date = ''

Deck = [None]
RecentScores = [None]
Choice = ''
AceHighOrLow = False

def GetRank(RankNo):
  Rank = ''
  if RankNo == 1 or RankNo == 14:
    Rank = 'Ace'
  elif RankNo == 2:
    Rank = 'Two'
  elif RankNo == 3:
    Rank = 'Three'
  elif RankNo == 4:
    Rank = 'Four'
  elif RankNo == 5:
    Rank = 'Five'
  elif RankNo == 6:
    Rank = 'Six'
  elif RankNo == 7:
    Rank = 'Seven'
  elif RankNo == 8:
    Rank = 'Eight'
  elif RankNo == 9:
    Rank = 'Nine'
  elif RankNo == 10:
    Rank = 'Ten'
  elif RankNo == 11:
    Rank = 'Jack'
  elif RankNo == 12:
    Rank = 'Queen'
  elif RankNo == 13:
    Rank = 'King'
  return Rank

def GetSuit(SuitNo):
  Suit = ''
  if SuitNo == 1:
    Suit = 'Clubs'
  elif SuitNo == 2:
    Suit = 'Diamonds'
  elif SuitNo == 3:
    Suit = 'Hearts'
  elif SuitNo == 4:
    Suit = 'Spades'
  return Suit

def DisplayMenu():
  print()
  print('MAIN MENU')
  print()
  print('1. Play game (with shuffle)')
  print('2. Play game (without shuffle)')
  print('3. Display recent scores')
  print('4. Reset recent scores')
  print('5. Options')
  print()
  print('Select an option from the menu (or enter q to quit): ', end='')

def GetMenuChoice():
  Choice = input()
  print()
  if Choice in ["Q","Quit","q","quit"]:
    Choice = "q"
  return Choice

def LoadDeck(Deck):
  global AceHighOrLow
  CurrentFile = open('deck.txt', 'r')
  Count = 1
  while True:
    LineFromFile = CurrentFile.readline()
    if not LineFromFile:
      CurrentFile.close()
      break
    Deck[Count].Suit = int(LineFromFile)
    LineFromFile = CurrentFile.readline()
    Deck[Count].Rank = int(LineFromFile)
    if AceHighOrLow == True and Deck[Count].Rank == 1:
      Deck[Count].Rank = 14
    Count = Count + 1

  
 
def ShuffleDeck(Deck):
  SwapSpace = TCard()
  NoOfSwaps = 1000
  for NoOfSwapsMadeSoFar in range(1, NoOfSwaps + 1):
    Position1 = random.randint(1, 52)
    Position2 = random.randint(1, 52)
    SwapSpace.Rank = Deck[Position1].Rank
    SwapSpace.Suit = Deck[Position1].Suit
    Deck[Position1].Rank = Deck[Position2].Rank
    Deck[Position1].Suit = Deck[Position2].Suit
    Deck[Position2].Rank = SwapSpace.Rank
    Deck[Position2].Suit = SwapSpace.Suit

def DisplayCard(ThisCard):
  print()
  print('Card is the', GetRank(ThisCard.Rank), 'of', GetSuit(ThisCard.Suit))
  print()

def DisplayOptions():
  print("OPTIONS MENU")
  print()
  print("1. Set Ace to be HIGH or LOW")
  print()
  print()

def GetOptionChoice():
  validChoice = False
  while not validChoice:
    OptionChoice = input("Select a option from the menu (or 'q' to quit): ")
    if OptionChoice in ['1','q']:
      return OptionChoice
      validChoice = True
    else:
      print("That was not a avalid choice")
      

def SetOptions(OptionChoice):
  if OptionChoice == '1':
    SetAceHighOrLow()
  else:
    pass

def SetAceHighOrLow():
  global AceHighOrLow
  AceHighOrLow = input("Do you want Ace to be (h)igh or (l)ow: ")
  if AceHighOrLow in ['high', 'HIGH', 'H', 'h']:
    AceHighOrLow = True
  elif AceHighOrLow in ['low', 'LOW', 'l', 'L']:
    AceHighOrLow = False
  else:
    pass


    
    
def GetCard(ThisCard, Deck, NoOfCardsTurnedOver):
  ThisCard.Rank = Deck[1].Rank
  ThisCard.Suit = Deck[1].Suit
  for Count in range(1, 52 - NoOfCardsTurnedOver):
    Deck[Count].Rank = Deck[Count + 1].Rank
    Deck[Count].Suit = Deck[Count + 1].Suit
  Deck[52 - NoOfCardsTurnedOver].Suit = 0
  Deck[52 - NoOfCardsTurnedOver].Rank = 0

def IsNextCardHigher(LastCard, NextCard):
  Higher = False
  if NextCard.Rank > LastCard.Rank:
    Higher = True
  return Higher

def GetPlayerName():
  print()
  PlayerName = input('Please enter your name: ')
  if len(PlayerName) >10:
    print("Your name can only be 10 characters long.")
    GetPlayerName()
  print()
  return PlayerName



def GetChoiceFromUser():
  Choice = input('Do you think the next card will be higher than the last card (enter y or n)? ')
  if Choice in ["yes","Y","Yes","y"]:
    Choice = "y"
  elif Choice in ["no","No","N","n"]:
    Choice = "n"
  return Choice


def DisplayEndOfGameMessage(Score):
  print()
  print('GAME OVER!')
  print('Your score was', Score)
  if Score == 51:
    print('WOW! You completed a perfect game.')
  print()

def DisplayCorrectGuessMessage(Score):
  print()
  print('Well done! You guessed correctly.')
  print('Your score is now ', Score, '.', sep='')
  print()

def ResetRecentScores(RecentScores):
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores[Count].Name = ''
    RecentScores[Count].Score = 0
    RecentScores[Count].date = ''

def DisplayRecentScores(RecentScores):
  print()
  print('Recent Scores: ')
  print()
  print("{0:<10}{1:<10}{2:<10}".format("Name", "Score", "Date"))
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    print("{0:<10}{1:<10}{2:<10}".format(RecentScores[Count].Name, RecentScores[Count].Score, RecentScores[Count].date))
    
  print()
  print('Press the Enter key to return to the main menu')
  input()
  print()

def UpdateRecentScores(RecentScores, Score, date):
  valid = False
  while not valid:
    PlayerName = GetPlayerName()
    if PlayerName == "":
      print("You must enter something for your name!")
      valid = False
    else:
      FoundSpace = False
      Count = 1
      while (not FoundSpace) and (Count <= NO_OF_RECENT_SCORES):
        if RecentScores[Count].Name == '':
          FoundSpace = True
        else:
          Count = Count + 1
    if not FoundSpace:
      for Count in range(1, NO_OF_RECENT_SCORES):
          RecentScores[Count].Name = RecentScores[Count + 1].Name
          RecentScores[Count].Score = RecentScores[Count + 1].Score
          RecentScores[Count].date = RecentScores[Count + 1].date
          
      Count = NO_OF_RECENT_SCORES
    RecentScores[Count].Name = PlayerName
    RecentScores[Count].Score = Score
    RecentScores[Count].date = ("{0}/{1}/{2}".format(date.day, date.month, date.year))

    
    valid = True

def PlayGame(Deck, RecentScores):
  LastCard = TCard()
  NextCard = TCard()
  GameOver = False
  GetCard(LastCard, Deck, 0)
  DisplayCard(LastCard)
  NoOfCardsTurnedOver = 1
  while (NoOfCardsTurnedOver < 52) and (not GameOver):
    GetCard(NextCard, Deck, NoOfCardsTurnedOver)
    Choice = ''
    while (Choice != 'y') and (Choice != 'n'):
      Choice = GetChoiceFromUser()
    DisplayCard(NextCard)
    NoOfCardsTurnedOver = NoOfCardsTurnedOver + 1
    Higher = IsNextCardHigher(LastCard, NextCard)
    if (Higher and Choice == 'y') or (not Higher and Choice == 'n'):
      DisplayCorrectGuessMessage(NoOfCardsTurnedOver - 1)
      LastCard.Rank = NextCard.Rank
      LastCard.Suit = NextCard.Suit
    else:
      GameOver = True
  if GameOver:
    DisplayEndOfGameMessage(NoOfCardsTurnedOver - 2)
    updateScore = input("Do you want to add your score to the high score table (y or n)?")
    if updateScore in ["yes","Y","Yes","y"]: 
      UpdateRecentScores(RecentScores, NoOfCardsTurnedOver - 2, date)
  else:
      DisplayEndOfGameMessage(51)
      UpdateRecentScores(RecentScores, 51, date)

if __name__ == '__main__':
  for Count in range(1, 53):
    Deck.append(TCard())
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores.append(TRecentScore())
  Choice = ''
  while Choice != 'q':
    DisplayMenu()
    Choice = GetMenuChoice()
    if Choice == '1':
      LoadDeck(Deck)
      ShuffleDeck(Deck)
      PlayGame(Deck, RecentScores)
    elif Choice == '2':
      LoadDeck(Deck)
      PlayGame(Deck, RecentScores)
    elif Choice == '3':
      DisplayRecentScores(RecentScores)
    elif Choice == '4':
      ResetRecentScores(RecentScores)
    elif Choice == '5':
      DisplayOptions()
      OptionChoice = GetOptionChoice()
      SetOptions(OptionChoice)
