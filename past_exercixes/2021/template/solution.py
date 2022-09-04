#!/bin/python3

from sys import stdin, stdout

def main(input: "list[str]") -> "list[str]":
  return input

if __name__ == "__main__":
  result = main(stdin.readlines())
  stdout.writelines(result)
