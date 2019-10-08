package tennis


class TennisGame1(val player1Name: String, val player2Name: String) extends TennisGame {
  var m_score1: Int = 0
  var m_score2: Int = 0

  def wonPoint(playerName: String) {
    if (playerName == "player1")
      m_score1 += 1
    else
      m_score2 += 1
  }

  /**
    * Calculate the score if the players have the score
    *
    * @return a string which contains the score
    */
  def calculateEqualScore(): String = {
    m_score1 match {
      case 0 => "Love-All"
      case 1 => "Fifteen-All"
      case 2 => "Thirty-All"
      case _ => "Deuce"
    }
  }

  /**
    * Calculate the score if difference of the score is greater than 4
    *
    * @return a string which contains the score
    */
  def calculateGteFour(): String = {
    val minusResult = m_score1 - m_score2
    if (minusResult == 1)  "Advantage player1"
    else if (minusResult == -1)  "Advantage player2"
    else if (minusResult >= 2) "Win for player1"
    else "Win for player2"
  }

  def calculateScore(): String = {
    var score: String = ""
    var tempScore = 0
    if (m_score1 == m_score2) {
      score = calculateEqualScore()
    }
    else if (m_score1 >= 4 || m_score2 >= 4) {
      score = calculateGteFour()
    }
    else {
      for (i <- 1 until 3 by 1) {
        if (i == 1) tempScore = m_score1
        else {
          score += "-";
          tempScore = m_score2;
        }
        val tempScore2 = tempScore match {
          case 0 => "Love"
          case 1 => "Fifteen"
          case 2 => "Thirty"
          case 3 => "Forty"
        }
        score += tempScore2
      }
    }

    return score
  }

  }