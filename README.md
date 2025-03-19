```
Welcome to Bookbot!

What is the book you would like to analyze? Please enter the file path: frankenstein.txt

Book Analysis Results:
=======================
Total Words: 78456
Unique Words: 12345
Total Sentences: 4567

Most Common Words:
the: 4567
and: 3456
of: 2345
to: 1234
a: 1123
in: 987
that: 876
was: 765
he: 654
it: 543

Report written to frankenstein_report.txt

Would you like to analyze another book? (yes/no): yes

What is the book you would like to analyze? Please enter the file path: moby_dick.txt

Book Analysis Results:
=======================
Total Words: 209456
Unique Words: 34567
Total Sentences: 12345

Most Common Words:
the: 12345
and: 9876
of: 8765
to: 7654
a: 6543
in: 5432
that: 4321
was: 3210
he: 2109
it: 1098

Report written to moby_dick_report.txt

Would you like to analyze another book? (yes/no): no
Thank you for using Bookbot! Goodbye!
```
> A simple Bookbot Python Program run in Terminal

# Bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

Bookbot is a Python command-line application that analyzes text files (e.g., books) and provides useful statistics such as word count, unique word count, and the most common words.

## Features
- Reads and analyzes any `.txt` file.
- Provides:
  - Total word count.
  - Unique word count.
  - Top 10 most common words with their frequencies.
- Cleans text by removing punctuation and converting it to lowercase for accurate analysis.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/MSMITH71910/bookbot.git
