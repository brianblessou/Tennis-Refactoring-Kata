package tennis.game1

class Regular(m_score1: Int, m_score2: Int) {
  def calculateScore(): String = {
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


object Regular {

  def apply(m_score1: Int, m_score2: Int): Regular = new Regular(m_score1, m_score2)

}
