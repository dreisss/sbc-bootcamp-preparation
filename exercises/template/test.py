#!/bin/python3

from solution import main

data = [
  { "input": ["1 2\n"], "output": ["1 2\n"] },
]

for case in data:
  expected = case["output"]
  received = main(case["input"])

  if received != expected:
    print(f"Test failed: expected '{expected}', received '{received}'")
  else:
    print("Tests passed!")
