package tennis.game1

import tennis.TennisGame

/**
  * Class to play a tennis game between two players.
  *
  * It will calculate the scrore in case of equality, match points or regular game
  *
  * @param player1Name, a string
  * @param player2Name, a string
  */
class TennisGame1(val player1Name: String, val player2Name: String) extends TennisGame {
  var m_score1: Int = 0
  var m_score2: Int = 0


  /**
    *
    * @param playerName
    * @throws java.lang.Exception
    */
  @throws(classOf[Exception])
  def wonPoint(playerName: String) {
    if (playerName == player1Name)
      m_score1 += 1
    else if (playerName == player2Name)
      m_score2 += 1
    else
      throw new Exception(s"player name is not correct")
  }


  /**
    * Calculate the score in case of Equality, Match points or Regular game
    *
    * @return a string which indicate the
    */
  def calculateScore(): String = {
    if (m_score1 == m_score2) {
      Equality.calculateScore(m_score1)
    }

    else if (m_score1 >= 4 || m_score2 >= 4) {
      MatchPoints(player1Name, player2Name).calculateScore(m_score1, m_score2)
    }
    else {
      Regular.calculateScore(m_score1, m_score2)
    }
  }
}