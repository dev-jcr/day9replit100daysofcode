# Casting

`If` statements support more than `==`. They support inequality symbols as well. Remember those <, >, and = signs you used in math way back when? Well they are back again, but this time they look a bit different.

<details> <summary> Equality and Inequality Symbols </summary>
  
```python
# equal
5 == 5

# not equal
3 != 5

# greater than
5 > 3

# greater than or equal to
5 >= 3

# less than
3 < 5

# less than or equal to
3 <= 5


```
</details>

This is because the way `input` works behind the scenes is it always assumes what you are typing is text (or a string) and gets stored as a variable in `""`.

*Casting* is where we explicitly tell the computer that what we are typing is a number and not a letter.

&nbsp;

The code below is saying any score greater than 100,000 is a winner. Anything less, try again. 

👉`Run` this code in `main.py` and see what happens:
```python
myScore = input("Your score: ")
if myScore > 100000:
  print("Winner!")
else:
  print("Try again 😭")
```

### We crashed it! How do we tell the computer, "Wait, thats a number!"?

