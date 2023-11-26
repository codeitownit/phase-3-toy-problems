# phase-3-toy-problems

#### **By Everlyn Njeri 24/11/2023**
## Project Description
#### Converting 12-hour time to 24-hour time
    Define a function, which will be given an hour (always in the range of 1 to 12, inclusive), a minute (always in the range of 0 to 59, inclusive), and a period (either "am" or "pm") as input and returns a four-digit string that encodes that time 
    in 24-hour time, as shown below: 

        12.30 am will return 0030 

        12.30 pm returns 1230

        1.40am returns 0140

        11.30 pm returns 2330

#### Two numbers are positive 
    Write a function, which takes three integers a, b, and c as arguments, 
    and returns True if exactly two of of the three integers are positive numbers (greater than zero), 
    and False - otherwise, as shown below: 

        (2, 4, -3) == True

        (-4, 6, 8) == True

        (4, -6, 9) == True

        (-4, 6, 0) == False

        (4, 6, 10) == False

        (-14, -3, -4) == False

#### Consonant value
    Given a lowercase string that has alphabetic characters only and no spaces, write a program that returns the highest value of consonant substrings. Consonants are any letters of the alphabet except "aeiou".We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.

    For the word "zodiacs", solve("zodiacs") = 26

    For example, for the word "zodiacs", let's cross out the vowels. We get: "z d cs"

    -- The consonant substrings are: "z", "d" and "cs" and the values are z = 26, d = 4 and cs = 3 + 19 = 22. The highest is 26.

    For the word "strength", solve("strength") = 57.

    The consonant substrings are: "str" and "ngth" with values "str" = 19 + 20 + 18 = 57 and "ngth" = 14 + 7 + 20 + 8 = 49. The highest is 57.


## Setup/Installation Requirements
    - Clone the repository to any desired folder in your computer
    - Open the cloned folder with vscode.
    - Run individual files in your terminal using the command `python3 name_of_the_file` i.e `python3 time_converter.py`.
    - And you are good to go
   

## Known Bugs
    The toy problem work fine.

## Technologies used
    - Python 3
    - Terminal
## License
   This project is **free to use** and does not contains any license.

