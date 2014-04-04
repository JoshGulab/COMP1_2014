#questions
1.GetPlayerName
2.I have put a while loop into the UpdateRecentScores() function. if they press enter they will be asked again to enter their name.
		def UpdateRecentScores(RecentScores, Score):
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
        Count = NO_OF_RECENT_SCORES
      RecentScores[Count].Name = PlayerName
      RecentScores[Count].Score = Score
      valid = True
3. valid variable is a boolean type