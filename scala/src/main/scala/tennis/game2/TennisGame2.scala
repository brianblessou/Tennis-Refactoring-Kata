package tennis.game2

import tennis.TennisGame

class TennisGame2(val player1Name: String, val player2Name: String) extends TennisGame {

  var P1point = 0
  var P2point = 0

  var P1res = ""
  var P2res = ""

  def getConcatenatedScore(P1res: String, P2res: String): String = {
    P1res + "-" + P2res
  }

  def calculateScore(): String = {
    var score = ""

    // In case of equality
    if (P1point == P2point) {
      if (P1point >= 3) {
        score = "Deuce"
      } else  {
        P1point match {
          case 0 => score = "Love"
          case 1 => score = "Fifteen"
          case 2 => score = "Thirty"
          case _ => print("Exception")
        }
        score += "-All"
      }
    }

//    // IF P1point > P2Point
//    if (P1point > P2point) {
//
//    }

    // P1point > P2Point
    if (P1point > 0 && P2point == 0) {

      P1point match {
        case 1 => P1res = "Fifteen"
        case 2 => P1res = "Thirty"
        case 3 => P1res = "Forty"
        case _ => print("Exception")
      }
      P2res = "Love"

      score = getConcatenatedScore(P1res, P2res)
    }

    if (P2point > 0 && P1point == 0) {

      P2point match {
        case 1 => P2res = "Fifteen"
        case 2 => P2res = "Thirty"
        case 3 => P2res = "Forty"
        case _ => print("Exception")
      }
      P1res = "Love"
      score = getConcatenatedScore(P1res, P2res)
    }

    // P1point > P2Point && something else
    if (P1point > P2point && P1point < 4) {
      P1point match {
        case 2 => P1res = "Thirty"
        case 3 => P1res = "Forty"
        case _ => print("Exception")
      }

      P2point match {
        case 1 => P2res = "Fifteen"
        case 2 => P2res = "Thirty"
        case _ => print("Exception")
      }


      score = getConcatenatedScore(P1res, P2res)
    }


    if (P2point > P1point && P2point < 4) {

      P1point match {
        case 1 => P1res = "Fifteen"
        case 2 => P1res = "Thirty"
        case _ => print("Exception")
      }

      P2point match {
        case 2 => P2res = "Thirty"
        case 3 => P2res = "Forty"
        case _ => print("Exception")
      }

      score = getConcatenatedScore(P1res, P2res)
    }

    // P1point > P2Point && something else
    if (P1point > P2point && P2point >= 3) {
      score = "Advantage player1"
    }

    if (P2point > P1point && P1point >= 3) {
      score = "Advantage player2"
    }

    // Check for those ones
    if (P1point >= 4 && P2point >= 0 && (P1point - P2point) >= 2) {
      score = "Win for player1"
    }
    if (P2point >= 4 && P1point >= 0 && (P2point - P1point) >= 2) {
      score = "Win for player2"
    }

    return score
  }


  def wonPoint(player: String) {
    if (player == "player1")
      P1point += 1
    else
      P2point += 1
  }
}