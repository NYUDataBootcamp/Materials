
### Question 01

Describe and explain what each of these expressions produces in basic Python:

```python
In [1]: 5+2
Out[1]: 7

In [2]: 2 + 5
Out[2]: 7

In [3]: 2**5
Out[3]: 32
```
----

### Question 20

```python
In [ ]: x = "How many characters and words are in this string?"

In [ ]: len(x) # how many characters are in the phrase
Out[ ]: 49
```
This shows how `len` behaves when applied to a string with the result being the number of characters in the string.
```python
In [ ]: # Convert x into a list of characters
   ...: char_list = list(x);
```

As we saw in class we can use the `list` function to convert any `iterable` into a list
```python
In [29]: list?
"""
Init signature: list(self, /, *args, **kwargs)
Docstring:     
list() -> new empty list
list(iterable) -> new list initialized from iterable's items
Type:           type
"""
```
As it turns out, *strings are iterable items and can be converted into a list.*

- - -

*Observation*: We can even check if strings are iterable by running the following
```python
In [ ]: from collections import Iterable
In [ ]: isinstance(x, Iterable)
Out[ ]: True
```
note that it wouldn't be the case for an instance of type `int`
```python
In [ ]: isinstance(1234, Iterable)
Out[ ]: False
```
---

As for the other questions, we can check the **methods** associated with `x` by `x.[TAB]` to find a one that allows us to split the phrase into words. Note the method already output a list
```python
In [ ]: # Convert x to a list of individual words
   ...: word_list = x.split();

In [ ]: word_list
Out[ ]: ['How', 'many', 'characters', 'and', 'words', 'are', 'in', 'this', 'string?']

In [ ]: type(word_list)
Out[ ]: list
```
to check how many words we have, we can just use `len` to our new created list
```
In [ ]: # How many words does x contain?
   ...: len(word_list)
Out[ ]: 9
```


<!-- `Redcarpet.new("Hello World!")`{.ruby} -->
