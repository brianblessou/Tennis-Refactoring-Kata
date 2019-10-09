package tennis.game1

/**
  * Calcul the score in case of equality
  */
class Equality(m_score1: Int) {

  /**
    * Calculate the score if the players have the score
    *
    * @return a string which contains the score
    */
  def calculateScore(): String = {
    m_score1 match {
      case 0 => "Love-All"
      case 1 => "Fifteen-All"
      case 2 => "Thirty-All"
      case _ => "Deuce"
    }
  }
}

object Equality {
  def apply(m_score1: Int): Equality = new Equality(m_score1)
}