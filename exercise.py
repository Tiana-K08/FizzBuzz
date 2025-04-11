max_num = 101
 
for num in range(1, max_num):
  if num % 3 == 0 and num % 5 == 0:
    print('FizzBuzz')
  elif num % 5 == 0:
    print('Buzz')
  elif num % 3 == 0:
    print('Fizz')
  else:
    print(num)