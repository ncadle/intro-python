# Newton-Raphson method for finding square root

epsilon = 0.01
k = 24.0
guess = k / 2.0
numGuesses = 0
while abs(guess**2 - k) >= epsilon:
    guess = guess - (((guess**2) - k) / (2 * guess))
    numGuesses += 1
print('Number of guesses using Newton-Raphson:',numGuesses)
print('Square root of', k, 'is about', guess)
print('')


# Bisection search 

count = 0
low = 0.0
high = max(1.0, k)
ans = (high + low) / 2.0
while abs(ans**2 - k) >= epsilon:
    count += 1
    if ans**2 < k:
        low = ans
    else:
        high = ans
    ans = (high+low) / 2.0
print('Number of guesses using bisection search:',count)
print(ans, 'is close to the square root of', k)


    






