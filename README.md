# ChatGPT Payment Tracker

This project was inspired by me skimming through Python basics materials and picking up the concepts I was still lacking for my machine learning path.

The story is simple. My friend and I shared a ChatGPT Plus account, and it usually stumped me when I was asked whether my friend had paid for that month or not. So, I just wanted to create something useful with a little personal touch.


## Main Features:

Add new entries
Read a selected number of entries
Search entries by category
Automatically create the CSV file if it does not exist
Exit through a simple command-line menu
Python Concepts Used

## What I Learned:
In this project, I practiced using variables and constants to store program data, and I organized the code into reusable functions with parameters and default arguments. I used `if`, `elif`, and `else` statements to handle different menu options, together with `for` and `while` loops to process records and keep the program running.

I used dictionaries to represent each payment entry and worked with user input using `input()`, along with string methods such as `.strip()` and `.lower()` to clean and standardize the input.

For data storage, I practiced file handling with `with open(...)` and used Python's `csv` module, including `csv.DictReader` and `csv.DictWriter`, to read and write CSV records. I also used the `os` module to check whether the data file already existed and create it when necessary.

Other concepts I practiced include `enumerate()` for tracking rows, Boolean flags for checking search results, basic type hints such as `-> None`, and breaking the program into smaller functions so that each part has a clear responsibility.

## Reflection and Future Improvements
At this point, the application's scope stops at being a command-line tool, and it basically contains what I need. Since I usually work on my computer, it is very quick for me to open the Python program and update the local CSV file.

However, the update process could be made simpler and less prone to errors. I will work on this if I have time.

In addition, I also want to implement some more sophisticated filtering options in the future.

Overall, the project was a good use of my time over the weekend, as it helped me see many Python concepts in practice. It may perhaps turn into something bigger in the future. I do not know yet.
