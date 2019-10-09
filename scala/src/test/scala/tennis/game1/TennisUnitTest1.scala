package tennis.game1

import org.junit.Assert._
import org.junit.Test


/**
  *  Unit tests
  *
  */
class TennisUnitTest1() {

  @Test
  def checkCalculateScoreForEquality(): Unit = {
    assertEquals("Love-All", Equality.calculateScore(0))
    assertEquals("Fifteen-All", Equality.calculateScore(1))
    assertEquals("Thirty-All", Equality.calculateScore(2))
    assertEquals("Deuce", Equality.calculateScore(3))
  }
//
//  @Test
//  def checkCalculateScoreForMatchPoints(): Unit = {
//    val game = new TennisGame1("player1", "player2")
//    assertEquals("Advantage player1", game.calculateScoreForMatchPoints(3,2, "player1", "player2"))
//    assertEquals("Advantage player2", game.calculateScoreForMatchPoints(2,3,"player1", "player2"))
//    assertEquals("Win for player1", game.calculateScoreForMatchPoints(5,1,"player1", "player2"))
//    assertEquals("Win for player2", game.calculateScoreForMatchPoints(4,4,"player1", "player2"))
//  }

}


