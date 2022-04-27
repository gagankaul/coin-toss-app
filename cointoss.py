#Coin Toss App

import random
import time

#Welcome message
print(F"Welcome to Coin Toss App")
print(f"\nI will flip a coin a set number of times.")

#Get user input
total_flips = int(input("How many times would you like me to flip the coin: "))
see_results = input("Would you like to see the results of each flip(y/n): ").lower()

print(f"\nFlipping!!!\n")

start_time = time.time()
count_heads = 0
count_tails = 0

#The main loop
for flip in range(0,total_flips):
  toss = random.randint(0,1)
  if toss == 0:
    count_heads += 1
    if see_results.startswith("y"):
      print("HEADS")
  else:
    count_tails += 1
    if see_results.startswith("y"):
      print("TAILS")
  
  if (count_tails == count_heads):
    print(f"At {flip + 1} coin flips, the count of heads {count_heads} is the same as the count of tails {count_tails}.")

#Calculate percentages
percent_heads = round(count_heads * 100 / total_flips, 2)
percent_tails = round(count_tails * 100 / total_flips, 2)

#Print the results
print(f"\nResults of Flipping A Coin {total_flips} Times:")
print(f"\nSide\t\tCount\t\tPercentage")
print(f"Heads\t\t{count_heads}/{total_flips}\t\t{percent_heads}%")
print(f"Tails\t\t{count_tails}/{total_flips}\t\t{percent_tails}%")

print(f"\nTime elapsed: {time.time() - start_time} seconds.")