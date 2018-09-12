'''
Created on Jun 18, 2018

@author: Ashwin
'''
#!/usr/bin/env python

# Written by Chris Conly based on C++
# code provided by Dr. Vassilis Athitsos
# Written to be Python 2.4 compatible for omega

import sys
import MaxConnect4Game
import copy

def succesors(currentGame):
    availColtoPlay = []
    for col in range(0, 7, 1):
        if currentGame.gameBoard[0][col] == 0:
            availColtoPlay.append(col)
    return availColtoPlay

def utility(currentGame):
    currentGame.countScore()
    if currentGame.argvList[3] == "human-next":
        if currentGame.maxPlayer == 2:
            if currentGame.player1Score > currentGame.player2Score:
                return 1
            elif currentGame.player1Score < currentGame.player2Score:
                return -1
            else:
                return 0
        
        elif currentGame.maxPlayer == 1:
            if currentGame.player2Score > currentGame.player1Score:
                return 1
            elif currentGame.player2Score < currentGame.player1Score:
                return -1
            else:
                return 0
    if currentGame.argvList[3] == "computer-next": 
        if currentGame.maxPlayer == 1:
            if currentGame.player1Score > currentGame.player2Score:
                return 1
            elif currentGame.player1Score < currentGame.player2Score:
                return -1
            else:
                return 0
            
        elif currentGame.maxPlayer == 2:
            if currentGame.player2Score > currentGame.player1Score:
                return 1
            elif currentGame.player2Score < currentGame.player1Score:
                return -1
            else:
                return 0        
def evalScoreCheck(player1points, player2points, currentGame):
    utility = 0
    player1Delta = currentGame.player1Score - player1points
    player2Delta = currentGame.player2Score - player2points
    if (currentGame.argvList[3] == 'computer-next' and currentGame.maxPlayer == 1) or (currentGame.argvList[3] == 'human-next' and currentGame.maxPlayer == 2):
        if player1Delta >= player2Delta:
            if player1Delta - player2Delta == player1Delta:
                if player1Delta == 0:
                    utility += 5
            
                elif player1Delta == 1:
                    utility += 7
            
                elif player1Delta == 2:
                    utility += 10
                
                else:
                    utility += 20
    
            if player1Delta - player2Delta >= 5:
                utility += 20
            
            if player1Delta - player2Delta == 4:
                utility += 13
            
            if player1Delta - player2Delta == 3:
                utility += 8
            
            if player1Delta - player2Delta == 2:
                utility += 6
            
            if player1Delta - player2Delta == 1:
                utility += 3    
        
        elif player1Delta < player2Delta:
            if player2Delta - player1Delta == player2Delta:            
                if player2Delta == 1:
                    utility -= 7
            
                elif player2Delta == 2:
                    utility -= 20
                
                else:
                    utility -= 30
    
            if player2Delta - player1Delta >= 5:
                utility -= 45
            
            if player2Delta - player1Delta == 4:
                utility -= 40
            
            if player2Delta - player1Delta == 3:
                utility -= 36
            
            if player2Delta - player1Delta == 2:
                utility -= 25
            
            if player1Delta - player2Delta == 1:
                utility -= 12
    
    elif (currentGame.argvList[3] == 'computer-next' and currentGame.maxPlayer == 2) or (currentGame.argvList[3] == 'human-next' and currentGame.maxPlayer == 1):
        if player2Delta >= player1Delta:
            if player2Delta - player1Delta == player2Delta:
                if player2Delta == 0:
                    utility += 5
            
                elif player2Delta == 1:
                    utility += 7
            
                elif player2Delta == 2:
                    utility += 10
                
                else:
                    utility += 20
    
            if player2Delta - player1Delta >= 5:
                utility += 20
            
            if player2Delta - player1Delta == 4:
                utility += 13
            
            if player2Delta - player1Delta == 3:
                utility += 8
            
            if player2Delta - player1Delta == 2:
                utility += 6
            
            if player2Delta - player1Delta == 1:
                utility += 3    
        
        elif player2Delta < player1Delta:
            if player1Delta - player2Delta == player1Delta:            
                if player1Delta == 1:
                    utility -= 7
            
                elif player1Delta == 2:
                    utility -= 20
                
                else:
                    utility -= 30
            
            if player2Delta - player1Delta >= 5:
                utility -= 45
            
            if player2Delta - player1Delta == 4:
                utility -= 40
            
            if player2Delta - player1Delta == 3:
                utility -= 36
            
            if player2Delta - player1Delta == 2:
                utility -= 25
            
            if player1Delta - player2Delta == 1:
                utility -= 12
    
    
    #print 'calc difference'
    return utility

def compCoordinatesCheck(currentGame):
    utility = 0
    if (currentGame.argvList[3] == 'computer-next' and currentGame.maxPlayer == 1) or (currentGame.argvList[3] == 'human-next' and currentGame.maxPlayer == 2):
        if currentGame.gameBoard[5][3] == 1:
            utility += 500
            if currentGame.gameBoard[5][2] == 1:
                utility += 10
            if currentGame.gameBoard[5][4] == 1:
                utility += 10
            if currentGame.gameBoard[4][2] == 1:
                utility += 20
            if currentGame.gameBoard[4][4] == 1:
                utility += 20
            if currentGame.gameBoard[4][1] == 1:
                utility += 20
            if currentGame.gameBoard[4][5] == 1:
                utility += 20
            if currentGame.gameBoard[3][3] == 1:
                utility += 30
            if currentGame.gameBoard[3][4] == 1:
                utility += 20
            if currentGame.gameBoard[3][2] == 1:
                utility += 20
            if currentGame.gameBoard[2][0] == 1:
                utility += 40
            if currentGame.gameBoard[2][6] == 1:
                utility += 40
            if currentGame.gameBoard[2][2] == 1:
                utility += 30
            if currentGame.gameBoard[2][4] == 1:
                utility += 30
            if currentGame.gameBoard[1][3] == 1:
                utility += 40
            if currentGame.gameBoard[1][2] == 1:
                utility += 30
            if currentGame.gameBoard[1][4] == 1:
                utility += 30
            if currentGame.gameBoard[0][1] == 1:
                utility += 40
            if currentGame.gameBoard[0][2] == 1:
                utility += 40
            if currentGame.gameBoard[0][4] == 1:
                utility += 40
            if currentGame.gameBoard[0][5] == 1:
                utility += 40
        elif currentGame.gameBoard[5][3] == 2:
            if currentGame.gameBoard[4][3] == 1:
                utility += 200
                if currentGame.gameBoard[5][2] == 1:
                    utility += 10
                if currentGame.gameBoard[5][4] == 1:
                    utility += 10
                if currentGame.gameBoard[4][2] == 1:
                    utility += 20
                if currentGame.gameBoard[4][4] == 1:
                    utility += 20
                if currentGame.gameBoard[4][1] == 1:
                    utility += 20
                if currentGame.gameBoard[4][5] == 1:
                    utility += 20
                if currentGame.gameBoard[3][3] == 1:
                    utility += 30
                if currentGame.gameBoard[3][4] == 1:
                    utility += 20
                if currentGame.gameBoard[3][2] == 1:
                    utility += 20
                if currentGame.gameBoard[2][0] == 1:
                    utility += 40
                if currentGame.gameBoard[2][6] == 1:
                    utility += 40
                if currentGame.gameBoard[2][2] == 1:
                    utility += 30
                if currentGame.gameBoard[2][4] == 1:
                    utility += 30
                if currentGame.gameBoard[1][3] == 1:
                    utility += 40
                if currentGame.gameBoard[1][2] == 1:
                    utility += 30
                if currentGame.gameBoard[1][4] == 1:
                    utility += 30
                if currentGame.gameBoard[0][1] == 1:
                    utility += 40
                if currentGame.gameBoard[0][2] == 1:
                    utility += 40
                if currentGame.gameBoard[0][4] == 1:
                    utility += 40
                if currentGame.gameBoard[0][5] == 1:
                    utility += 40
                    
        for row in currentGame.gameBoard:   #horizontal check
            if row[0:4] == [1] * 4:
                utility += 1500
            if row[1:5] == [1] * 4:
                utility += 1500
            if row[2:6] == [1] * 4:
                utility += 1500
            if row[3:7] == [1] * 4:
                utility += 1500
            if row[2:5] == [1] * 3:
                utility += 30
                if row[1] == 0:
                    utility += 500
                if row[5] == 0:
                    utility += 500
            if row[0:3] == [1] * 3:
                utility += 20
                if row[3] == 0:
                    utility += 500
            if row[1:4] == [1] * 3:
                utility += 20
                if row[0] == 0:
                    utility += 500
                if row[4] == 0:
                    utility += 500
            if row[3:6] == [1] * 3:
                utility += 20
                if row[6] == 0:
                    utility += 500
                if row[2] == 0:
                    utility += 500
            if row[4:7] == [1] * 3:
                utility += 20
                if row[3] == 0:
                    utility += 500
            
            if row[0:2] == [1] * 2:
                utility += 10
                if row[2] == 0:
                    utility += 15
            if row[1:3] == [1] * 2:
                utility += 10
                if row[3] == 0:
                    utility += 15
                if row[0] == 0:
                    utility += 15
            if row[2:4] == [1] * 2:
                utility += 10
                if row[4] == 0:
                    utility += 15
                if row[1] == 0:
                    utility += 15
            if row[3:5] == [1] * 2:
                utility += 10
                if row[5] == 0:
                    utility += 15
                if row[2] == 0:
                    utility += 15
            if row[4:6] == [1] * 2:
                utility += 10
                if row[6] == 0:
                    utility += 15
                if row[3] == 0:
                    utility += 15
            if row[5:7] == [1] * 2:
                utility += 10
                if row[4] == 0:
                    utility += 15
                    
            for j in range(7):  #vertical check
                if (currentGame.gameBoard[0][j] == 1 and currentGame.gameBoard[1][j] == 1 and
                   currentGame.gameBoard[2][j] == 1 and currentGame.gameBoard[3][j] == 1):
                    utility += 1500
                if (currentGame.gameBoard[1][j] == 1 and currentGame.gameBoard[2][j] == 1 and
                   currentGame.gameBoard[3][j] == 1 and currentGame.gameBoard[4][j] == 1):
                    utility += 1500
                if (currentGame.gameBoard[2][j] == 1 and currentGame.gameBoard[3][j] == 1 and
                   currentGame.gameBoard[4][j] == 1 and currentGame.gameBoard[5][j] == 1):
                    utility += 1500
                    
    elif (currentGame.argvList[3] == 'computer-next' and currentGame.maxPlayer == 2) or (currentGame.argvList[3] == 'human-next' and currentGame.maxPlayer == 1):
        if currentGame.gameBoard[5][3] == 2:
            utility += 200
            if currentGame.gameBoard[5][2] == 2:
                utility += 10
            if currentGame.gameBoard[5][4] == 2:
                utility += 10
            if currentGame.gameBoard[4][2] == 2:
                utility += 20
            if currentGame.gameBoard[4][4] == 2:
                utility += 20
            if currentGame.gameBoard[4][1] == 2:
                utility += 20
            if currentGame.gameBoard[4][5] == 2:
                utility += 20
            if currentGame.gameBoard[3][3] == 2:
                utility += 30
            if currentGame.gameBoard[3][4] == 2:
                utility += 20
            if currentGame.gameBoard[3][2] == 2:
                utility += 20
            if currentGame.gameBoard[2][0] == 2:
                utility += 40
            if currentGame.gameBoard[2][6] == 2:
                utility += 40
            if currentGame.gameBoard[2][2] == 2:
                utility += 30
            if currentGame.gameBoard[2][4] == 2:
                utility += 30
            if currentGame.gameBoard[1][3] == 2:
                utility += 40
            if currentGame.gameBoard[1][2] == 2:
                utility += 30
            if currentGame.gameBoard[1][4] == 2:
                utility += 30
            if currentGame.gameBoard[0][1] == 2:
                utility += 40
            if currentGame.gameBoard[0][2] == 2:
                utility += 40
            if currentGame.gameBoard[0][4] == 2:
                utility += 40
            if currentGame.gameBoard[0][5] == 2:
                utility += 40
        elif currentGame.gameBoard[5][3] != 2:
            if currentGame.gameBoard[4][3] == 2:
                utility += 200
                if currentGame.gameBoard[5][2] == 2:
                    utility += 10
                if currentGame.gameBoard[5][4] == 2:
                    utility += 10
                if currentGame.gameBoard[4][2] == 2:
                    utility += 20
                if currentGame.gameBoard[4][4] == 2:
                    utility += 20
                if currentGame.gameBoard[4][1] == 2:
                    utility += 20
                if currentGame.gameBoard[4][5] == 2:
                    utility += 20
                if currentGame.gameBoard[3][3] == 2:
                    utility += 30
                if currentGame.gameBoard[3][4] == 2:
                    utility += 20
                if currentGame.gameBoard[3][2] == 2:
                    utility += 20
                if currentGame.gameBoard[2][0] == 2:
                    utility += 40
                if currentGame.gameBoard[2][6] == 2:
                    utility += 40
                if currentGame.gameBoard[2][2] == 2:
                    utility += 30
                if currentGame.gameBoard[2][4] == 2:
                    utility += 30
                if currentGame.gameBoard[1][3] == 2:
                    utility += 40
                if currentGame.gameBoard[1][2] == 2:
                    utility += 30
                if currentGame.gameBoard[1][4] == 2:
                    utility += 30
                if currentGame.gameBoard[0][1] == 2:
                    utility += 40
                if currentGame.gameBoard[0][2] == 2:
                    utility += 40
                if currentGame.gameBoard[0][4] == 2:
                    utility += 40
                if currentGame.gameBoard[0][5] == 2:
                    utility += 40
                    
        for row in currentGame.gameBoard:   #horizontal check
            if row[0:4] == [2] * 4:
                utility += 1500
            if row[1:5] == [2] * 4:
                utility += 1500
            if row[2:6] == [2] * 4:
                utility += 1500
            if row[3:7] == [2] * 4:
                utility += 1500
            if row[2:5] == [2] * 3:
                utility += 30
                if row[1] == 0:
                    utility += 500
                if row[5] == 0:
                    utility += 500
            if row[0:3] == [2] * 3:
                utility += 20
                if row[3] == 0:
                    utility += 500
            if row[1:4] == [2] * 3:
                utility += 20
                if row[0] == 0:
                    utility += 500
                if row[4] == 0:
                    utility += 500
            if row[3:6] == [2] * 3:
                utility += 20
                if row[6] == 0:
                    utility += 500
                if row[2] == 0:
                    utility += 500
            if row[4:7] == [2] * 3:
                utility += 20
                if row[3] == 0:
                    utility += 500
            
            if row[0:2] == [2] * 2:
                utility += 10
                if row[2] == 0:
                    utility += 500
            if row[1:3] == [2] * 2:
                utility += 10
                if row[3] == 0:
                    utility += 500
                if row[0] == 0:
                    utility += 500
            if row[2:4] == [2] * 2:
                utility += 10
                if row[4] == 0:
                    utility += 500
                if row[1] == 0:
                    utility += 500
            if row[3:5] == [2] * 2:
                utility += 10
                if row[5] == 0:
                    utility += 500
                if row[2] == 0:
                    utility += 500
            if row[4:6] == [2] * 2:
                utility += 10
                if row[6] == 0:
                    utility += 500
                if row[3] == 0:
                    utility += 500
            if row[5:7] == [2] * 2:
                utility += 10
                if row[4] == 0:
                    utility += 500
        for j in range(7):  #vertical check
            if (currentGame.gameBoard[0][j] == 2 and currentGame.gameBoard[1][j] == 2 and
                currentGame.gameBoard[2][j] == 2 and currentGame.gameBoard[3][j] == 2):
                utility += 1500
            if (currentGame.gameBoard[1][j] == 2 and currentGame.gameBoard[2][j] == 2 and
                currentGame.gameBoard[3][j] == 2 and currentGame.gameBoard[4][j] == 2):
                utility += 1500
            if (currentGame.gameBoard[2][j] == 2 and currentGame.gameBoard[3][j] == 2 and
                currentGame.gameBoard[4][j] == 2 and currentGame.gameBoard[5][j] == 2):
                utility += 1500
        
    return utility

def humanMoveDefense(currentGame):
    utility = 0
    if (currentGame.argvList[3] == 'computer-next' and currentGame.maxPlayer == 2) or (currentGame.argvList[3] == 'human-next' and currentGame.maxPlayer == 1):
        #Check 4 & 3 in a row for opponent player 1 horizontal
        for row in currentGame.gameBoard:
            if row[0:4] == [1] * 4:
                utility -= 1500
            if row[1:5] == [1] * 4:
                utility -= 1500
            if row[2:6] == [1] * 4:
                utility -= 1500
            if row[3:7] == [1] * 4:
                utility -= 1500
                
            if row[2:5] == [1] * 3:
                utility += 30
                if row[1] == 2:
                    utility += 2500
                if row[5] == 2:
                    utility += 2500
            if row[0:3] == [1] * 3:
                utility += 20
                if row[3] == 2:
                    utility += 2500
            if row[1:4] == [1] * 3:
                utility += 20
                if row[0] == 2:
                    utility += 2500
                if row[4] == 2:
                    utility += 2500
            if row[3:6] == [1] * 3:
                utility += 20
                if row[6] == 2:
                    utility += 2500
                if row[2] == 2:
                    utility += 2500
            if row[4:7] == [1] * 3:
                utility += 20
                if row[3] == 2:
                    utility += 2500
            
        for j in range(7):  #vertical check
            if (currentGame.gameBoard[0][j] == 1 and currentGame.gameBoard[1][j] == 1 and
                currentGame.gameBoard[2][j] == 1 and currentGame.gameBoard[3][j] == 1):
                utility -= 1500
            if (currentGame.gameBoard[1][j] == 1 and currentGame.gameBoard[2][j] == 1 and
                currentGame.gameBoard[3][j] == 1 and currentGame.gameBoard[4][j] == 1):
                utility -= 1500
            if (currentGame.gameBoard[2][j] == 1 and currentGame.gameBoard[3][j] == 1 and
                currentGame.gameBoard[4][j] == 1 and currentGame.gameBoard[5][j] == 1):
                utility -= 1500
                
            if (currentGame.gameBoard[0][j] == 1 and currentGame.gameBoard[1][j] == 1 and
                currentGame.gameBoard[2][j] == 1 and currentGame.gameBoard[3][j] == 2):
                utility += 2500
            if (currentGame.gameBoard[1][j] == 1 and currentGame.gameBoard[2][j] == 1 and
                currentGame.gameBoard[3][j] == 1 and currentGame.gameBoard[4][j] == 2):
                utility += 2500
            if (currentGame.gameBoard[2][j] == 1 and currentGame.gameBoard[3][j] == 1 and
                currentGame.gameBoard[4][j] == 1 and currentGame.gameBoard[5][j] == 2):
                utility += 2500
    
    elif (currentGame.argvList[3] == 'computer-next' and currentGame.maxPlayer == 1) or (currentGame.argvList[3] == 'human-next' and currentGame.maxPlayer == 2):
        for row in currentGame.gameBoard:
            if row[0:4] == [2] * 4:
                utility -= 1500
            if row[1:5] == [2] * 4:
                utility -= 1500
            if row[2:6] == [2] * 4:
                utility -= 1500
            if row[3:7] == [2] * 4:
                utility -= 1500
                
            if row[2:5] == [2] * 3:
                utility += 30
                if row[1] == 1:
                    utility += 2500
                if row[5] == 1:
                    utility += 2500
            if row[0:3] == [2] * 3:
                utility += 20
                if row[3] == 1:
                    utility += 2500
            if row[1:4] == [2] * 3:
                utility += 20
                if row[0] == 1:
                    utility += 2500
                if row[4] == 1:
                    utility += 2500
            if row[3:6] == [2] * 3:
                utility += 20
                if row[6] == 1:
                    utility += 2500
                if row[2] == 1:
                    utility += 2500
            if row[4:7] == [2] * 3:
                utility += 20
                if row[3] == 1:
                    utility += 2500
            
        for j in range(7):  #vertical check
            if (currentGame.gameBoard[0][j] == 2 and currentGame.gameBoard[1][j] == 2 and
                currentGame.gameBoard[2][j] == 2 and currentGame.gameBoard[3][j] == 2):
                utility -= 1500
            if (currentGame.gameBoard[1][j] == 2 and currentGame.gameBoard[2][j] == 2 and
                currentGame.gameBoard[3][j] == 2 and currentGame.gameBoard[4][j] == 2):
                utility -= 1500
            if (currentGame.gameBoard[2][j] == 2 and currentGame.gameBoard[3][j] == 2 and
                currentGame.gameBoard[4][j] == 2 and currentGame.gameBoard[5][j] == 2):
                utility -= 1500
                
            if (currentGame.gameBoard[0][j] == 2 and currentGame.gameBoard[1][j] == 2 and
                currentGame.gameBoard[2][j] == 2 and currentGame.gameBoard[3][j] == 1):
                utility += 2500
            if (currentGame.gameBoard[1][j] == 2 and currentGame.gameBoard[2][j] == 2 and
                currentGame.gameBoard[3][j] == 2 and currentGame.gameBoard[4][j] == 1):
                utility += 2500
            if (currentGame.gameBoard[2][j] == 2 and currentGame.gameBoard[3][j] == 2 and
                currentGame.gameBoard[4][j] == 2 and currentGame.gameBoard[5][j] == 1):
                utility += 2500
    
    return utility      
            
def evalFunction(currentGame):
    utilityEval = 0
    player1points = 0
    player2points = 0
    #print 'eval pochlo'
    player1points = currentGame.player1Score
    player2points = currentGame.player2Score
    currentGame.countScore()
    #print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
    utilityScoreCheck = evalScoreCheck(player1points, player2points, currentGame)
    utilityEval += utilityScoreCheck
    utilitycompCoord = compCoordinatesCheck(currentGame)
    utilityEval += utilitycompCoord
    utilityhumanMoveDefense = humanMoveDefense(currentGame)
    utilityEval += utilityhumanMoveDefense
    return utilityEval 

def MyprintGameBoardToFile(fileObj, currentGame):
        for row in currentGame.gameBoard:
            fileObj.write(''.join(str(col) for col in row) + '\n')
        fileObj.write('%s\n' % str(currentGame.currentTurn))
            
def maxValue(currentGame, alpha, beta):
    currentGame.depthLimit -= 1
    if currentGame.pieceCount == 42 or currentGame.depthLimit == 0:
        if currentGame.pieceCount == 42:
            return utility(currentGame), -1
        elif currentGame.depthLimit == 0:
            return evalFunction(currentGame), -1
    vMax = -100000   
    availColtoPlay = list(succesors(currentGame))
    updatedGameBoard = copy.deepcopy(currentGame.gameBoard)
    currentTurntempmax = copy.deepcopy(currentGame.currentTurn)
    for currCol in availColtoPlay:
        currentGame.playPiece(currCol)
        #currentGame.depthLimit -= 1
        currentGame.currentTurn = moveChange(currentGame)
        utilityReturned, colReturned = minValue(currentGame, alpha, beta)
        currentGame.depthLimit += 1
        vMax = max(vMax, utilityReturned)
        if vMax == utilityReturned:
            maxCol = currCol
        currentGame.gameBoard = copy.deepcopy(updatedGameBoard)
        currentGame.checkPieceCount()
        currentGame.currentTurn = copy.deepcopy(currentTurntempmax)
        if vMax >= beta[0]:
            return vMax, maxCol     #return maxCol, maxVal        
        alpha[0] = max(alpha[0], vMax)
    try:    
        return vMax, maxCol     #return maxCol, maxVal  
    except:
        return vMax, -1     #return maxCol, maxVal           
        
def minValue(currentGame, alpha, beta):
    currentGame.depthLimit -= 1
    if currentGame.pieceCount == 42 or currentGame.depthLimit == 0:
        if currentGame.pieceCount == 42:
            return utility(currentGame), -1
        elif currentGame.depthLimit == 0:
            return evalFunction(currentGame), -1
        
    availColtoPlay = list(succesors(currentGame))
    vMin = 100000    
    updatedGameBoard = copy.deepcopy(currentGame.gameBoard)
    currentTurnTempmin = copy.deepcopy(currentGame.currentTurn)
    for currCol in availColtoPlay:
        currentGame.playPiece(currCol)
        currentGame.currentTurn = moveChange(currentGame)
        utilityReturned, colReturned = maxValue(currentGame, alpha, beta)
        currentGame.depthLimit += 1
        vMin = min(vMin, utilityReturned)
        if vMin == utilityReturned:
            minCol = currCol
        currentGame.gameBoard = copy.deepcopy(updatedGameBoard)
        currentGame.checkPieceCount()
        currentGame.currentTurn = copy.deepcopy(currentTurnTempmin)        
        if vMin <= alpha[0]:
            return vMin, minCol    #return maxCol, maxVal
        beta[0] = min(beta[0], vMin)
    try:
        return vMin, minCol    #return maxCol, maxVal
    except:
        return vMin, -1    #return maxCol, maxVal

def alphabetaDecision(currentGame):
    alpha = [-1000]
    beta = [1000]   
    # Check if board is not full
    if currentGame.pieceCount == 42:
        print 'Input Board state is full. No more possible moves.'
        currentGame.countScore()
        print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
        return
    
    availColtoPlay = list(succesors(currentGame))
    rootSuccesorsUtility = [-10000] * 7
    updatedGameBoard = copy.deepcopy(currentGame.gameBoard)
    currentTurnTemp = copy.deepcopy(currentGame.currentTurn)    
    for currCol in availColtoPlay:
        currentGame.playPiece(currCol)
        currentGame.currentTurn = moveChange(currentGame)
        utilityReturned, colReturned = minValue(currentGame, alpha, beta)
        currentGame.depthLimit += 1
        rootSuccesorsUtility[currCol] = utilityReturned
        currentGame.checkPieceCount()
        currentGame.gameBoard = copy.deepcopy(updatedGameBoard)
        currentGame.currentTurn = copy.deepcopy(currentTurnTemp)
        
    ActualMove = rootSuccesorsUtility.index(max(rootSuccesorsUtility))
    #print 'list is: ', rootSuccesorsUtility
    #print 'ActualMove is: ', ActualMove
    currentGame.playPiece(ActualMove)
    currentGame.checkPieceCount()
    currentGame.countScore()
    print('\n\nmove %d: Player %d, column %d\n' % (currentGame.pieceCount, currentGame.currentTurn, ActualMove + 1))
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
    currentGame.currentTurn = moveChange(currentGame)
    currentGame.printGameBoard()   
    
    if currentGame.pieceCount == 42:
        return
    if currentGame.argvList[1] == 'one-move':
        currentGame.printGameBoardToFile()
        return
    fileObjComp = open('Computer.txt', 'w')
    MyprintGameBoardToFile(fileObjComp, currentGame)
    fileObjComp.close()
    humanMove(currentGame)
    if currentGame.pieceCount == 42:
        return
    
    alphabetaDecision(currentGame)
    
def humanMove(currentGame):
    currColtoPlay = input("Enter a Column to Play from 1 to 7 : ")
    if currColtoPlay < 1 or currColtoPlay > 7 or currColtoPlay == '':
        humanMove(currentGame)
    else:
        if currColtoPlay == 0:
            print "Check Column enter. Enter a Column to Play from 1 to 7 : "
            humanMove(currentGame)
                
        validMoveCheck(currColtoPlay - 1, currentGame)  #checking if move is valid
            
        updatedGameBoard = copy.deepcopy(currentGame.gameBoard) #board state copied
        currentGame.playPiece(currColtoPlay - 1)
        currentGame.checkPieceCount()
        currentGame.countScore()
        print('\n\nmove %d: Player %d, column %d\n' % (currentGame.pieceCount, currentGame.currentTurn, currColtoPlay))
        print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
        currentGame.currentTurn = moveChange(currentGame)
        currentGame.printGameBoard()
        fileObjhuman = open('human.txt', 'w')
        MyprintGameBoardToFile(fileObjhuman, currentGame)
        fileObjhuman.close()

def moveChange(currentGame):
    if currentGame.currentTurn == 1:
        currentGame.currentTurn = 2
    else:
        currentGame.currentTurn = 1
    return currentGame.currentTurn

def validMoveCheck(currColtoPlay, currentGame):
    try:
        if currentGame.gameBoard[0][currColtoPlay] == 0:
            return
    except:
        print "Move not valid. Check Column entered"
        currColtoPlay = input("Enter a Column to Play from 1 to 7.")
        validMoveCheck(currColtoPlay, currentGame)  #checking if move is valid

def oneMoveGame(currentGame):
    if currentGame.pieceCount == 42:    # Is the board full already?
        print 'BOARD FULL\n\nGame Over!\n'
        sys.exit(0)
    if currentGame.depthLimit == 0:
        print 'Check depth limit. It is 0'
        currentGame.printGameBoard()
        currentGame.countScore
        print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
        return
    outFile = copy.deepcopy(currentGame.argvList[3])
    currentGame.gameFile = open(outFile, 'w')
    currentGame.argvList[3] = 'computer-next'    
    alphabetaDecision(currentGame)

    #print 'Game state after move:'
    #currentGame.printGameBoard()

    #currentGame.countScore()
    #print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    #currentGame.printGameBoardToFile()
    currentGame.gameFile.close()


def interactiveGame(currentGame):
    # Fill me in
    if currentGame.depthLimit == 0:
        print 'Check depth limit. It is 0'
        currentGame.printGameBoard()
        currentGame.countScore
        print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
        return
    if currentGame.argvList[3] == 'human-next':
    #if argv[3] == 'human-next':
        currColtoPlay = input("Enter a Column to Play from 1 to 7.")
        if currColtoPlay < 1 or currColtoPlay > 7 or currColtoPlay == '':
            interactiveGame(currentGame)
        else: 
            if currColtoPlay == 0:
                print "Check Column enter. Enter a Column to Play from 1 to 7."
                interactiveGame(currentGame)
                
            validMoveCheck(currColtoPlay - 1, currentGame)  #checking if move is valid
            currentGame.playPiece(currColtoPlay - 1)
            print('\n\nmove %d: Player %d, column %d\n' % (currentGame.pieceCount, currentGame.currentTurn, currColtoPlay))
            currentGame.currentTurn = moveChange(currentGame)
            alphabetaDecision(currentGame)
            print 'alphabetaDecision return zala'
            currentGame.countScore()
            print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
            return
    else:
        alphabetaDecision(currentGame)
        currentGame.countScore()
        print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
        return

def main(argv):
    # Make sure we have enough command-line arguments
    if len(argv) != 5:
        print 'Four command-line arguments are needed:'
        print('Usage: %s interactive [input_file] [computer-next/human-next] [depth]' % argv[0])
        print('or: %s one-move [input_file] [output_file] [depth]' % argv[0])
        sys.exit(2)
    
    game_mode, inFile = argv[1:3]

    if not game_mode == 'interactive' and not game_mode == 'one-move':
        print('%s is an unrecognized game mode' % game_mode)
        sys.exit(2)

    currentGame = MaxConnect4Game.maxConnect4Game() # Create a game
    # Try to open the input file
    try:
        currentGame.gameFile = open(inFile, 'r')
    except IOError:
        sys.exit("\nError opening input file.\nCheck file name.\n")
        
    # Read the initial game state from the file and save in a 2D list
    file_lines = currentGame.gameFile.readlines()
    currentGame.gameBoard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
    currentGame.currentTurn = int(file_lines[-1][0])
    currentGame.gameFile.close()
    print '\nMaxConnect-4 game\n'
    print 'Game state before move:'
    currentGame.printGameBoard()
    # Update a few game variables based on initial state and print the score
    currentGame.checkPieceCount()
    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))   
    # Taking currentGame.maxPlayer as the one who plays first so the algo for comp will always start with MaxVal call
    if currentGame.currentTurn == 1:
        currentGame.maxPlayer = 1
        currentGame.minPlayer = 2
    elif currentGame.currentTurn == 2:
        currentGame.maxPlayer = 2
        currentGame.minPlayer = 1
    else:
        print 'Check input file. Current Turn row.'
        sys.exit()
        
    # Checking if input board is not full  
    if currentGame.pieceCount == 42:
        print 'Input Board state is full. No more possible moves.'
        sys.exit()
    
    currentGame.argvList = argv
    currentGame.depthLimit = int(argv[4])
    if game_mode == 'interactive':
        interactiveGame(currentGame) # Be sure to pass whatever else you need from the command line
    else: # game_mode == 'one-move'
        # Set up the output file
        outFile = argv[3]
        try:
            currentGame.gameFile = open(outFile, 'w')
        except:
            sys.exit('Error opening output file.')
        oneMoveGame(currentGame) # Be sure to pass any other arguments from the command line you might need.


if __name__ == '__main__':
    main(sys.argv)