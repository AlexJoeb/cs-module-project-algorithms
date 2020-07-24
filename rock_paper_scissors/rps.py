#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  # Write a function `rock_paper_scissors` to generate all of the possible plays that can be made in a game of "Rock Paper Scissors", 
  # given some input `n`, which represents the number of plays per round. 

  # -- Hints --
  #  * Define a list with all of the possible Rock Paper Scissors plays.
  options = ['rock', 'paper', 'scissors']
  possibles = []

  if n == 0: return [[]]

  # Define a helper function.
  # Use `cache` as placeholder array before pushing to `possibles`.
  # The entire instance of `cache` will be appended to `possibles`, if conditions met.
  # `counter` is used to cross-check against `n` - to see if there is the right amount of items in the cache.
  def helper(cache, counter):
    if counter == 0:
      possibles.append(cache)
      return
    
    for index, option in enumerate(options):
      helper(cache + [option], counter - 1)

  helper([], n)
  return possibles


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')