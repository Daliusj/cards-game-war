# cards-game-war

--GAME RULES:
-Objective:
The objective of the War card game is to win all the cards.

-Players:
The game is played with two players

-Setup:
Use a standard 52-card deck.
Shuffle the deck thoroughly.
Deal the entire deck of cards evenly between the players, so each player has their own stack of cards.

-Gameplay:
Each player simultaneously flips over the top card of their stack and places it in the center.
The player with the higher-ranked card wins and takes both cards, placing them at the bottom of their stack.
If there is a tie (both players play cards of the same rank), a "war" is declared.
In a war, each player places three cards face down, followed by one card face up. The player with the higher-ranked face-up card wins all the cards in that round.
If there is another tie during a war, the process is repeated until one player wins.

-Card Ranks:
Cards are ranked in the standard order: 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
Aces are usually considered the highest-ranking cards.

--PROGRAM:
-User interface:
At the start of the game, user is prompted to enter the player's names. If no names are entered Player1 and Player2 names are selected by default.
The program shows player's names and the number of cards held by users.
By pressing Enter (passing empty string) program takes top cards from players decks and shows them between names.
If War is declared program program shows cards by which war was declared, 3 each closed cards and 1 each open card.
Example of war scenario: Player1 19#| A###K : A###5 |23# Player2 
When the game is over, the program shows the name of the winner.
Card colors is not shown. 
Full deck consists 4 each card: 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A

-Under the hood:
Written in OOP mostly
Splitted into 3 files: 
	main.py - main code flow, 
	utils.py - classes and functions,
	config.py - constant strings.
Main code flow:

	RUN
	|
	USER INPUT
	|
	GENERATE RANDOMLY SHUFFLED CARDS DECK (LIST)
	|
	SPLIT CARDS INTO TWO EVEN STACKS (LISTS)
	|
	ASSIGN STACKS TO PLAYERS
	|
	MAIN GAME LOOP----------SHOW INDEX ZERO CARDS
	|						|
	DECLARE THE WINNER		CHECK FOR WAR-------WAR SCENARIO
	|						|
	EXIT					CHECK FOR WINNER
							|
				 			ADD PLAYED CARDS TO WINNERS STACKS END
						 	|
							REMOVE PLAEYD CARDS FROM LOOSERS STACK
							|
					       	ADD POINTS TO WINNER
					     	|
					     	CHECK FOR WINNER
					     	 
    
 
	



