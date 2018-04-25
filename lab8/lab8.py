import lab8Func

def main():
    playerScore = lab8Func.playerTurn(0)
    dealerScore = lab8Func.dealerTurn(0)
    lab8Func.whoWon(playerScore, dealerScore)

main()
