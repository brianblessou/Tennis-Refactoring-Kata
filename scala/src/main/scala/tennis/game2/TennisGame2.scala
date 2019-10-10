package tennis.game2

import tennis.TennisGame


/**
  * Class to play a tennis game between two players.
  *
  * It will calculate the score in case of equality, match points or regular game
  *
  * @param player1Name, a string
  * @param player2Name, a string
  */
class TennisGame2(val player1Name: String, val player2Name: String) extends TennisGame {

  var P1point = 0
  var P2point = 0

  var P1res = ""
  var P2res = ""

  /**
    * Main function to calculate the final score depending on the points of each player
    *
    * @return a result, the result of the game
    */
  def calculateScore(): String = {

    if (matchIsFinished(P1point, P2point)) {
      getWinner(player1Name, player2Name, P1point > P2point)
    } else if (P1point == P2point) {
      calculScoreIfEquality(P1point)
    } else if (P1point > P2point) {
      calculateScoeForDifferentScore(player1Name, P1point)
    } else  {
      calculateScoeForDifferentScore(player2Name, P2point)
    }
  }

  /**
    * Get the player who won the game
    *
    * @param player1Name a string
    * @param player2Name a string
    * @param player1Won a boolean, true if player1 won else false
    * @return a string, the result of the game
    */
  def getWinner(player1Name: String, player2Name: String, player1Won: Boolean): String = {
    if (player1Won) s"Win for ${player1Name}" else s"Win for ${player2Name}"
  }

  /**
    * Calcul score in case of equality
    *
    * @param playerPoint an int
    * @return a string, the score name
    */
  def calculScoreIfEquality(playerPoint: Int): String = {
    playerPoint match {
      case 0 => "Love-All"
      case 1 => "Fifteen-All"
      case 2 => "Thirty-All"
      case _ => "Deuce"
    }
  }


  /**
    * Calculate the result of a set if no equality
    *
    * @param playerName, a string
    * @param playerPoint, an int
    * @return a string, the nresult of the set
    */
  def calculateScoeForDifferentScore(playerName: String, playerPoint: Int): String = {
    if (playerPoint == 0) {
      getConcatenatedScore(getScore(P1point), getScore(P2point))
    } else if (playerPoint < 4) {
      getConcatenatedScore(getScore(P1point), getScore(P2point))
    } else  {
      s"Advantage ${playerName}"
    }
  }


  /**
    * Function to get the score name at the end of the set
    *
    * @param playerScore
    * @return a string, the score name for a player
    */
  def getScore(playerScore: Int): String = {
    playerScore match {
      case 0 => "Love"
      case 1 =>"Fifteen"
      case 2 => "Thirty"
      case 3 => "Forty"
    }
  }

  /**
    * Test if the match is finished or not.
    *
    * @param player1Point an Int
    * @param player2Point an Int
    * @return a Boolean,
    */
  def matchIsFinished(player1Point: Int, player2Point: Int): Boolean = {
    (player1Point >= 4 || player2Point >= 4) && Math.abs(player1Point - player2Point) >= 2
  }


  /**
    * Concatenate the final score name for two players.
    *
    * @param player1Result a string
    * @param player2Result a string
    * @return a string, score concatenated
    */
  def getConcatenatedScore(player1Result: String, player2Result: String): String = {
    player1Result + "-" + player2Result
  }


  def wonPoint(player: String) {
    if (player == "player1")
      P1point += 1
    else
      P2point += 1
  }

}