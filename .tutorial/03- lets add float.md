# Let's add float

You would do the exact same thing, except using `float` for a decimal number. In the code below, I want to find pi to 3 decimal places. 

👉 Copy this code and see if it works!

```python
myPi = float(input("What is Pi to 3dp? "))
if myPi == 3.142 :
  print("Exactly!")
else:
  print("Try again 😭")
```
You did it!


We are casting that input as a `float` which means we are expecting a decimal number. The code will not crash if we put a `.` and then numbers after it to signify a decimal number.

