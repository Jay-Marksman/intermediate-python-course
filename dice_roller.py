import random
def main():
# roll two onehundred-sided die and total 
  die = 2
die_sum = 0
for i in range(0,2):
  roll = random.randint(1,100)
  die_sum += roll
  print(f'You rolled a(n) {roll}')
print(f'You have rolled a total of {die_sum}')

if __name__== "__main__":
  main()
