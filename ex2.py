# 2-)

fibonacci = [0, 1]

userInput = int(input('Digite um número: '))
last = 1
secondLast = 0

if userInput == 0 or userInput == 1:
    print('Pertence a sequência')
else:
   for i in range(userInput):
       num = last + secondLast
       fibonacci.append(num)
       secondLast = last
       last = num
       i += 1
   if (userInput in fibonacci):
       print('Pertence a sequência')
   else:
       print('Não pertence a sequência')
