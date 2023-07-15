from rps import *

def test_p1_play():
  game = Game()
  assert game.play_hand("p1", "rock") == "p1 has played rock"

def test_p2_play():
  game = Game()
  assert game.play_hand("p2", "rock") == "p2 has played rock"

def test_rocks_draw():
  game = Game()
  game.play_hand("p1", "rock")
  game.play_hand("p2", "rock")
  assert game.result() == "Draw"

def test_papers_draw():
  game = Game()
  game.play_hand("p1", "paper")
  game.play_hand("p2", "paper")
  assert game.result() == "Draw"

def test_p1_paper_wins():
  game = Game()
  game.play_hand("p1", "paper")
  game.play_hand("p2", "rock")
  assert game.result() == "p1 wins"

def test_p2_paper_wins():
  game = Game()
  game.play_hand("p2", "paper")
  game.play_hand("p1", "rock")
  assert game.result() == "p2 wins"