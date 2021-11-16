# 0x01. Python - if/else, loops, functions

![python loop](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/233/code.png)

## Resources
**Read or watch**:

- [More Control Flow Tools (Read until “4.6. Defining Functions” included)](https://alx-intranet.hbtn.io/rltoken/jpjs5EnZTpBLLEremJYjPQ)
- [IndentationError](https://alx-intranet.hbtn.io/rltoken/F9n2AE-fpEPzt2PfBMGYAQ)
- [How To Use String Formatters in Python 3](https://alx-intranet.hbtn.io/rltoken/ZdtRIAkFu8dMBT99DcFBNg)
- [Learn to Program](https://alx-intranet.hbtn.io/rltoken/ElQgZYNHrLI7kV_ysEB1hQ)
- [Learn to Program 2 : Looping](https://alx-intranet.hbtn.io/rltoken/ElQgZYNHrLI7kV_ysEB1hQ)
- [Pycodestyle – Style Guide for Python Code](https://alx-intranet.hbtn.io/rltoken/TuTTnEg_Rwn8U1g3PEsZmA)
**man or help**:

- python3
## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
- Why Python programming is awesome
- Why indentation is so important in Python
- How to use the if, if ... else statements
- How to use comments
- How to affect values to variables
- How to use the while and for loops
- How is Python’s for different from C‘s?
- How to use the break and continues statements
- How to use else clauses on loops
- What does the pass statement do, and when to use it
- How to use range
- What is a function and how do you use functions
- What does return a function that does not use any return statement
- Scope of variables
- What’s a traceback
- What are the arithmetic operators and how to use them

## Requirements
### Python Scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.\*)
- All your files must be executable
- The length of your files will be tested using wc
### C Scripts
- Allowed editors: vi, vim, emacs
- All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options -Wall -Werror -Wextra -pedantic -std=gnu89
- All your files should end with a new line
- Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
- You are not allowed to use global variables
- No more than 5 functions per file
- In the following examples, the main.c files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own main.c files at compilation. Our main.c files might be different from the one shown in the examples
- The prototypes of all your functions should be included in your header file called lists.h
- Don’t forget to push your header file
- All your header files should be include guarded
### Tasks
### 0. Positive anything is better than negative nothing       mandatory
This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print whether the number stored in the variable number is positive or negative.

- You can find the source code here
- The variable number will store a different value every time you will run this program
- You don’t have to understand what import, random. randint do. Please do not touch this code
- The output of the program should be:
	- The number, followed by
		- if the number is greater than 0: is positive
		- if the number is 0: is zero
		- if the number is less than 0: is negative
	- followed by a new line
```
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py
-4 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py
0 is zero
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py
-3 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py
-10 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py
10 is positive
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py
-5 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py
6 is positive
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py
7 is positive
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py
5 is positive
guillaume@ubuntu:~/0x01$
```
Repo:

- GitHub repository: alx-higher_level_programming
- Directory: 0x01-python-if_else_loops_functions
- File: 0-positive_or_negative.py
### 1. The last digit
This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable number.

- You can find the source code here
- The variable number will store a different value every time you will run this program
- You don’t have to understand what import, random.randint do. Please do not touch this code. This line should not change: number = random.randint(-10000, 10000)
- The output of the program should be:
	- The string Last digit of, followed by
	- the number, followed by
	- the string is, followed by the last digit of number, followed by
		- if the last digit is greater than 5: the string and is greater than 5
		- if the last digit is 0: the string and is 0
		- if the last digit is less than 6 and not 0: the string and is less than 6 and not 0
	- followed by a new line
```
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 4205 is 5 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -626 is -6 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 1144 is 4 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -9200 is 0 and is 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 5247 is 7 and is greater than 5
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -9318 is -8 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 3369 is 9 and is greater than 5
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -5224 is -4 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -4485 is -5 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 3850 is 0 and is 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 5169 is 9 and is greater than 5
guillaume@ubuntu:~/0x01$
```
Repo:

- GitHub repository: alx-higher_level_programming
- Directory: 0x01-python-if_else_loops_functions
- File: 1-last_digit.py
