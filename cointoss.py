#Coin Toss App

import random

print(F"Welcome to Coin Toss App")
print(f"\nI will flip a coin a set number of times.")

count_toss = 0
count_heads = 0
count_tails = 0

total_count = int(input("How many times would you like me to flip the coin: "))

see_results = input("Would you like to see the results (y/n): ")

if see_results.startswith("y"):
  for i in range(0,total_count):
    toss = random.randint(0,1)
    count_toss += 1
    if toss == 0:
      print("HEADS")
      count_heads += 1
    else:
      print("TAILS")
      count_tails += 1
    if count_tails == count_heads:
      print(f"At {count_toss} coin flips, the count of heads {count_heads} is the same as the count of tails {count_tails}.")

else:
  for i in range(0,total_count):
    toss = random.randint(0,1)
    count_toss += 1
    if toss == 0:
      count_heads += 1
    else:
      count_tails += 1

percent_heads = (count_heads / total_count) * 100
percent_heads = round(percent_heads, 2)
percent_tails = (count_tails / total_count) * 100
percent_tails = round(percent_tails,2)

print(f"\nResults of Flipping A Coin {total_count} Times:")
print(f"\nSide\t\tCount\t\tPercentage")
print(f"Heads\t\t{count_heads}/{total_count}\t\t{percent_heads}%")
print(f"Tails\t\t{count_tails}/{total_count}\t\t{percent_tails}%")

