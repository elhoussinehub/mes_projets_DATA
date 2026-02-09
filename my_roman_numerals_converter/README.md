# Welcome to My Roman Numerals Converter
***

## Task

What is the problem? And where is the challenge?
The goal is to write a function that converts normal (Arabic) numbers into Roman numerals.
The challenge is to correctly represent each part of the number using Roman symbols (I, V, X, L, C, D, M) and handle special cases like 4 (IV), 9 (IX), 40 (XL), 900 (CM), etc.

## Description

How have you solved the problem?
I created a list of tuples, each containing a number and its corresponding Roman symbol.
Then, I used a loop to repeatedly subtract values from the input number while adding the matching Roman symbols to the result string.
The algorithm goes from the largest to the smallest value until the number becomes zero.

Example:

14 → 10 (X) + 4 (IV) → XIV

2022 → 2000 (MM) + 20 (XX) + 2 (II) → MMXXII

## Installation

No installation required.
You only need Python 3 installed on your computer.
To run the script:

python roman_converter.py

## Usage

You can call the function directly from Python, or run the script in your terminal.

Example:
from roman_converter import number_to_roman

print(number_to_roman(14))     # XIV
print(number_to_roman(79))     # LXXIX
print(number_to_roman(845))    # DCCCXLV
print(number_to_roman(2022))   # MMXXII


Or, if you want to run it from the terminal:

./my_project 2022


Output:

MMXXII

## The Core Team

Houssine El Malki
