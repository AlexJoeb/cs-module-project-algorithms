#!/usr/bin/python

import sys

def making_change(amount, denominations):
  # Initalize and populate a list with 0s.
  # Amount of zeros should be one more than `amount`.
  combos = [0] * (amount + 1)

  # Set 0 index of `combos` to 1 to start the chain.
  combos[0] = 1

  # Loop through each coin.
  for i, coin in enumerate(denominations):
    # Loop through each element in the `combos` array.
    for idx in range(1, len(combos), 1):
      # Check to see if idx is greater or equal to the coin denomination.
      if idx >= coin:
        combos[idx] += combos[idx - coin]

  return combos[amount]


# def making_change(amount, denominations):
#   def recurse(amount, idx, denominations):
#     if amount == 0: return 1
#     if amount < 0: return 0
#     if amount > 0 and idx == len(denominations): return 0

#     return recurse(amount - denominations[idx], idx, denominations) + recurse(amount, idx + 1, denominations)
  
#   return recurse(amount, 0, denominations)

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")