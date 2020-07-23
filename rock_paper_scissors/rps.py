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


    

  #  * Another problem that asks you to generate a bunch of permutations, so we're probably going to want to opt for using recursion again. 
  #     Since we're building up a list of results, we'll have to pass the list we're constructing around to multiple recursive calls so that
  #     each recursive call can add to the overall result. However, the tests only give our function `n` as input. To get around this, 
  #     we could define an inner recursive helper function that will perform the recursion for us, while allowing us to preserve the outer 
  #     function's function signature. 
  #  * In Python, you can concatenate two lists with the `+` operator. However, you'll want to make sure that both operands are lists!
  #  * If you opt to define an inner recursive helper function, don't forget to make an initial call to the recursive helper function to kick off the recursion.

#   var roundChoice = function(cache, counter) {
#     for(var i = 0; i < options.length; i++){
#       cache.push(options[i]);
#       if(counter === n){
#         possibles.push(cache.slice());
#       }else{
#         roundChoice(cache, counter + 1);
#       }
#       cache.pop();
#      }
#    }
#   roundChoice([], 1);
#   return allPossibilities;
# }

  pass


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')