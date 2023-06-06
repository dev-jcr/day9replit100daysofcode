print("What generation are you part of?")
print()
gen = int(input("What year were you born?"))
if gen < 1925:
  print("You are older than prostitution")
elif gen >= 1925 and gen <= 1946 :
  print("You are part of the Traditionalist generation!")
elif gen > 1946 and gen <= 1964 :
  print("You are part of the Baby Boomers generation!")
elif gen > 1964 and gen <= 1981:
  print("You are part of the Generation X!")
elif gen > 1981 and gen <= 1995 :
  print("You are part of the Traditionalist generation!")
elif gen > 1995 and gen <= 2015 :
  print("You are part of the Traditionalist generation!")
else:
  print("You are part of the Alpha generation! Congratulations! you are barely starting to live when the world is starting to die")
  
