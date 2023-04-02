import random

name = 'Kevin'

Question = 'Will I be Rich One Day?'

Answer = ''

Random_number = random.randint(1,9)

print(Random_number)

if Random_number == 1:
  Answer = 'Yes-definitely'
elif Random_number == 2:
  Answer = 'It is decidedly slow'
elif Random_number == 3:
  Answer = 'Without a doubt'
elif Random_number == 4:
  Answer = 'Reply hazy, try again'
elif Random_number == 5:
  Answer = 'Ask again later'
elif Random_number == 6:
  Answer = 'Better not tell you now'
elif Random_number == 7:
  Answer = 'My sources say no'
elif Random_number == 8:
  Answer = 'Outlook not so good'
elif Random_number == 9:
  Answer = 'Very doubtful'
else:
  Answer = 'Error'

print(name + ' asks:' + Question)

print("Magic 8-Ball's answer: " + Answer)

