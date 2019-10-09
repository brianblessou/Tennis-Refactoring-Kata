package tennis.game1


object Regular {

  def calculateScore(m_score1: Int, m_score2: Int): String = {
    getScore(m_score1) + "-" + getScore(m_score2)
  }

  private def getScore(tempScore: Int): String = {
    tempScore match {
      case 0 => "Love"
      case 1 => "Fifteen"
      case 2 => "Thirty"
      case 3 => "Forty"
    }
  }

}
