


def hangman(word):
	wrong = 0 
	stages = ["",
			"_____________           ",
			"|            |		     ",
			"|						 ",
			"|            o  		 ",
			"|           /|\		 ",
			"|           / \		 ",
			"|						 "
			]
	correctLetters = list(word)
	print(stages[3:4])
	board = ["_"] * len(word)
	win = False
	print("Welcome to Hangman")
	while wrong < len(stages) - 1 :
		print("\n" * 2)
		print ((" ".join(board)))
		print ("\n")
		msg = "Guess a letter  "
		guess = input(msg)
		if guess in correctLetters:
			c_ind = correctLetters.index(guess)
			board[c_ind] = guess 
			correctLetters[c_ind] = 'filler'
		else:
			wrong +=1 
		
		#print ((" ".join(board)))
		e = wrong + 1 
		print ("\n".join(stages[0:e]))
		if "_" not in board: 
			print("You Win!")
			print(" ".join(board))
			win = True 
			break
	if not win:
		print("\n".join(stages[0: wrong]))
		print("You lose! Loser! It was {}.".format(word))
		
hangman("pytthon")

	