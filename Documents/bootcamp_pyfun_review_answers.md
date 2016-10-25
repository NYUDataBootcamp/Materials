# Python Fundamentals Review

In this file, we will review all of the material that has been covered in "Python Fundamentals 1" and "Python Fundamentals 2." This is _not_ for a grade and is meant to be used as a checkpoint for yourself.

The material covered in this review (and in the Python Fundamentals sections) is foundational. If you have questions, please ask. It will be important to understand this material for the rest of this course. Some of these are meant to be a little challenging to stretch you -- If there are problems that you can't do, don't despair -- Instead of getting worried, ask questions! As if we haven't said this enough times: IF YOU NEED HELP, PLEASE ASK QUESTIONS!!!

## Types

We have discussed various types that are used within Python. This section will ask you about these types. For each question with multiple answers, circle all of the types that apply.

1. Which of the following are numerical types
  - string
  - list
  - int (Yes)
  - float (Yes)
  - tuple
  - dictionary
  - bool

2. Which of the following would you typically use to store text?
  - string (Yes)
  - list
  - int
  - float
  - tuple
  - dictionary
  - bool

3. Which of the following would you use to store keys and values?
  - string
  - list
  - int
  - float
  - tuple
  - dictionary (Yes)
  - bool

4. Which of the following would you use to store items that you wanted to iterate over?
  - string (Yes)
  - list (Yes)
  - int
  - float
  - tuple (Yes)
  - dictionary (Yes)
  - bool

5. What do each of the following types do when they are multiplied by 2?
  - string (concatenates string together twice --> `"abc"*2 => "abcabc"`
  - list (concatentates lists together twice --> `[1, 2]*2 => [1, 2, 1, 2]`
  - int (double the integer)
  - float (doubles the float)
  - tuple (error)
  - dictionary (error)
  - bool (returns 2 if true and 0 if false)

6. What is the type and value of each of the following commands? If you don't know, can you think of a way to find out?
  - `2 * 3` (Int)
  - `2 * 3.0` (Float)
  - `"abc" * 3` (string)
  - `list("abc") * 2` (list)
  - `str(int(float("12.34")))` (string)
  - `[1, 2, 3] + ["one", "two", "three"]` (list)
  - `dict(zip([1, 2, 3], ["one", "two", "three"]))` (dictionary)
  - `1 > 0` (boolean)
  - `1 < 0` (boolean)

7. What do we mean when we talk about "tab completion" for a type? We are referring to the fact that after typing an object `x` we can type a `.` and then hit tab to reveal all of its corresponding methods

## Writing python code and using Spyder

The information covered in this section is probably a bit less "fundamental" than what was covered in the previous section, but knowing the answers to this section can help you write your code more efficiently.

8. What is Spyder? The environment that we have used for programming so far

9. How do you open Spyder? Open a terminal and type `spyder`

10. How could you find out more information about a function in Spyder? For example, if you wanted to know more about the `print` function where could you find that information? Type `print?` in the ipython terminal or search in object inspector

11. What is it when you leave notes to yourself within your code? How do you make these notes? A comment -- We leave them using `#`

12. What is a cell block and how do we make one? How do we run only a single block at a time? How would we run an entire file at once? We create cell blocks with `#%%`. We can run one at a time using `Ctrl+Enter`. We can run an entire file by clicking green arrow at top

13. How do we change our "working directory" to the data bootcamp folder? Use upper right corner folder

## Practice problems

These are practice problems that apply the concepts we have discussed so far

14. Suppose that we borrow 200 for one year at an interest rate of 5 percent. If we pay interest plus principal at the end of the year, what is our total payment? Compute this using variables `principal` and `i` (for interest rate). Print your answer.

```python
principal = 200
i = 0.05
print(principal * (1 + i))
```

15. Imagine that now you wanted to compute the interest plus principal for multiple interest rates. How would you store multiple interest rates? Now print the answer for a principal of 200 and interest rates of 1, 2, 5, and 10 percent (Hint: easiest way is to do this in a loop).

```python
i_values = [0.01, 0.02, 0.05, 0.10]
principal = 200

for ir in i_values:
    print(principal * (1 + ir)
```

16. (Challenging) This will be your first chance at doing "text analysis" in this course. Enter the code below into Python. It is a poem by Edgar Allan Poe. It is secretly dedicated to Poe's friend. The name is written by taking one letter from each line -- In particular, if you are on line i then use the ith letter (if you were on line 7 then you would use the 7th letter, not including spaces, which is s). Your job is to print the name of his friend (letter by letter is fine) that it was dedicated to. I will give two hints: use the string method for splitting (either `.split(/n)` or `.splitlines()`) to break the code up into lines and then the second hint is that you will want to ignore the spaces and punctuation (find a string method that you can use get rid of them).

```python
txt = """For her this rhyme is penned, whose luminous eyes,
Brightly expressive as the twins of Loeda.
Shall find her own sweet name, that, nestling lies
Upon, the page, enwrapped from every reader.
Search narrowly the lines! — they hold a treasure
Divine—a talisman—an amulet
That must be worn at heart. Search well the measure
The words—the syllables! Do not forget
The trivialest point, or you may lose your labor!
And yet there is in this no Gordian knot
Which one might not undo without a saber,
If one could merely comprehend the plot.
Enwritten upon the leaf where now are peering
Eyes scintillating soul, there lies perdus
Three eloquent words oft uttered in the hearing
Of poets, by poets as the name is a poet's, too.
Its letters, although naturally lying
Like the knight Pinto—Mendez Ferdinando
Still form a synonym for Truth. Cease trying!
You will not read the riddle, though you do the best you can do."""

punctuation = [" ", ",", "!", "-", "."]
for p in punctuation:
    txt = txt.replace(p, "")

name = ""
lines = txt.splitlines()
for i in range(len(lines)):
    name = name + lines[i][i]

print(name)
```

17. Sum all of the numbers less than 200. What is the value?

```python
total = 0.0
for i in range(200):
    total = total + i

print("The value is", total)
```

18. Create a list that computes the cumulative sum from 0 to 10 (not including 10). The answer should be `[ 0,  1,  3,  6, 10, 15, 21, 28, 36, 45]`. Save this list as `cs` which we will use in the next couple problems.

```python
total = 0
cs = []
for i in range(10):
    total = total + i
    cs.append(total)
```

19. How would you get the 4th element (6) from `cs`?

```python
print(cs[3])
```

20. How would you get the first 4 elements from `cs`?

```python
print(cs[:4])
```

21. How would you get the last 4 elements from `cs`?

```python
print(cs[-4:])
```

22. Write a function which takes a first name and last name and returns the combination of the names. For example, if `firstname = "Chase"` and `lastname = "Coleman"` then the function should return `"Chase Coleman"`.

```python
def combine_names(first, last):
    return first + " " + last
```

23. Write a function which takes two first names and returns the names in alphabetical order. For example, if `name1 = "Chase"` and `name2 = "Chad"` then the function should return `("Chad", "Chase")`.

```python
def order_names(name1, name2):
    if name1 < name2:
        return (name1, name2)
    else:
        return (name2, name1)
```

24. Take the list of growth rates `g = [0.02, 0.07, 0.08]`. Write a list comprehension that multiplies each element by 100. Do the same exercise by using a loop and storing them in a new list.

```python
g = [0.02, 0.07, 0.08]
g_p = [gi*100 for gi in g]
```

25. Think about everything we've done so far. If you have questions, raise your hand or write an email to us. ASK QUESTIONS.

:)

