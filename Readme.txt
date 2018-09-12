------------------------------------------
Name: Ashwin Rajesh Joshi
Student Id: 1001554272
------------------------------------------

Programming language used: Python

----------------------------------
		Code Structure
----------------------------------
1.	In the interactive mode, InteractiveGame() function is invoked in which, human plays the move if he is first to play and then alphaBetaDecision() function is invoked.
2.	In the alphaBetaDecision() function, succesors of root node(Max Node) are explored if input board state is not terminal state.
3.	For each succesor, minValue() function is called in which first terminal state is checked. If not terminal state, then copy of current gameboard and current Turn is taken. Then the for each succesor of the minNode move is played and maxValue() function is called.
4.	In the maxValue function, same steps are repeated, first a copy of game board passed from minValue() and current Turn is taken and if not terminal state, succesors are expllored and move is played.
5. Once, terminal Node or depth limit is reached in any of the maxValue or minValue functions, they return the utility value. Once returned in either of the maxValue or minValue functions, the backup of the boardgame taken earlier is reset so to explore next succesor.
6. Finally, when actual move is played by the maxNode, moveChange() function is called which changes current Turn and Gameboard and score are printed.
7. Now, when its humans turn to play, humanMove() function is called which takes input from human for the column to play and prints the gameboard and the score after playing a move in that column and again alphaBetaDecision() is invoked.
8. After each actual move by human and computer, the board states are stored in .txt files 'human.txt' and 'computer.txt' respectively.

Command line areguments are as follows:
	python maxconnect4.py interactive <inputTest.txt> <computer-next> 7
	python maxconnect4.py interactive <inputTest.txt> <human-next> 7
Here, computer-next means computer will play first and human-next means human will play first.
NOTE: All files should be at the same location.

How to play a Human move?
When its human turn, user input is asked to enter a column to play. Column number has to be from 1 to 7 representing the columns of the board from left to right respectively. Press enter after entering the column to play.

NOTE: Do not press enter without entering the column number. Also, if the entered column is not valid, you will have to renter a valid column number.