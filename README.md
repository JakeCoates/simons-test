# Simons Test
I was provided with a test set out by Simon to take a text file and solve problems with that text file.

## Setup:

```
poetry install
pytest -s
```



## Problem 1
### 1 a

For the first problem I was asked to take the inputs from text file `inputs1.txt` and determine what combination of numbers summed to make the number `2020` and then complete the product of those numbers and that is your answer.

For this task I dediced to use itertools combinations as it is an efficient way to iterate through the different possible combinations with the amount of numbers you would like to compare. For this task it was `2` total numbers to make the number `2020`


---
ANSWER: 1013211

---
### 1 b

For problem 1 b I didn't have to change much but allow for the number of combinations for comparison to be passed into the function

---
ANSWER: 13891280

---


## Problem 2
### 1 a
Problem 2 was a bit different as you had to take each line and each line had limitations built into that line.

I decided to take the data similarly to the previous problem and then clean it up even more to allow for tuples to be used that contained the min, max, character and string. This made for the comparison to be relatively easy to compare.

you can just count how many times that letter has occurred in the string and then compare to the min and max constraints.

reviewing the example in the problem itself the range can be equal to the numbers so the comparison is >= min and <= max

---
ANSWER: 666 🤘

---

### 1 b

As i had prepared the data for the previous problem I decided to just add a basic if check to seperate the two comparisons.

reviewing the example the numbers in the min max section are comparing against the index so are offset by 1 so we take 1 away when indexing.


---
ANSWER: 348

---

# Notes / Improvements
- I would of added more tests in place as the ones I added were extremely basic and were there for me to build the code, but due to the time constraints I didn't add in potential edge cases
- I contemplated building this as an API and the building an extremely basic front end to allow you to push a list to the backend and return a number but it was largely out of scope
- The code potentially isn't the nicest to read as I used a large amount of list comprehension instead of breaking it into for loops that allow you to get more explicit in definitions and checks

---

# Simons Brief

Introduction

------------

Hello and welcome to Simon's coding exercise! I very much appreciate you taking the time to work through the exercises and hope you enjoy doing them.

I expect that you should be able to complete the exercises within 2 hours (don't spend longer - we insist, incomplete is fine). 

In approaching your solution, write your code as if you intended to ship it to production. Tests are expected. While it is great if you can answer the exercises correctly, it is more important that your code is clear, idiomatic and maintainable. Focus on your development patterns, and use of OOP.

Use python to complete this exercise.

If you have any questions please don't hesitate to reach out to us!

The Exercises

-------------
There are two exercises each with two parts. They are described in the files problem1.txt and problem2.txt. Each exercise has a required input which can be found in the input directory.

Please provide your answers in the exercise.txt files

Evaluation

-------------
I will use your answers as a measure of:
- How you can follow and implement a set of requirements
- Is the code you produce well written
- How you ensure your code is robust and working as expected
- How is your solution in terms of being efficient/concise/general 
- Did you get the answers right! :-)
