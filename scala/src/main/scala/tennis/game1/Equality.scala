package tennis.game1



object Equality {
  /**
    * Calculate the score if the players have the score
    *
    * @return a string which contains the score
    */
  def calculateScore(m_score1: Int): String = {
    m_score1 match {
      case 0 => "Love-All"
      case 1 => "Fifteen-All"
      case 2 => "Thirty-All"
      case _ => "Deuce"
    }
  }
}