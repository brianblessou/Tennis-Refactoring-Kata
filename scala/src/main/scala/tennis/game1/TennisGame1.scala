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
    * Increment the score for a player who won the set
    *
    * @param playerName, a string
    */
  def wonPoint(playerName: String) {
    if (playerName == player1Name)
      m_score1 += 1
    else
      m_score2 += 1
  }


  /**
    * Calculate the score in case of Equality, Match points or Regular game
    *
    * @return a string which indicate the
    */
  def calculateScore(): String = {
    if (m_score1 == m_score2) {
      Equality(m_score1).calculateScore()
    }

    else if (m_score1 >= 4 || m_score2 >= 4) {
      MatchPoints(m_score1, m_score2, player1Name, player2Name).calculateScore()
    }
    else {
      Regular(m_score1, m_score2).calculateScore()
    }
  }
}