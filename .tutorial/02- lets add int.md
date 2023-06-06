# Let's add `int`
- There are two types of numbers the computer will recognize:
  - `int` whole number (ex: 42)
  - `float` any number with a decimal (ex: 1.81)

## int

To change "your score" to a number, we need to add `int` in front of the `input` and place the enitre input in `()`. 

```python
myScore = input("Your score: ")
if myScore > 100000:
  print("Winner!")
else:
  print("Try again 😭")
```

👉 Update your code to look like this:

```python
myScore = int(input("Your score: "))
if myScore > 100000:
  print("Winner!")
else:
  print("Try again 😭")
```
Did it work this time?

The way the computer will read this code is by starting with what is in brackets first ("your score"). The computer thinks this is text because of the `""`. When we add `int`, we are telling the computer, "This is not text. Please convert this to a whole number." Now the variable, `myScore` will store the answer as a number.

### But what about float?

