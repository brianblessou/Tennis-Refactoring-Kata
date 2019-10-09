package tennis.game1


class MatchPoints(m_score1: Int, m_score2: Int, player1Name: String, player2Name: String) {

  /**
    * Calculate the score if difference of the score is greater than 4
    *
    * @return a string which contains the score
    */
  def calculateScore(): String = {
    val minusResult = m_score1 - m_score2

    if (minusResult == 1) s"Advantage ${player1Name}"
    else if (minusResult == -1) s"Advantage ${player2Name}"
    else if (minusResult >= 2) s"Win for ${player1Name}"
    else s"Win for ${player2Name}"
  }

}



object MatchPoints {

  def apply(m_score1: Int, m_score2: Int, player1Name: String, player2Name: String): MatchPoints
   = new MatchPoints(m_score1, m_score2, player1Name, player2Name)

}