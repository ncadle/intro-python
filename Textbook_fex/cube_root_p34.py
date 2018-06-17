# This program finds an approximation to the cube root of both
# negative and positive numbwers

x = -0.5
epsilon = 0.01
numGuesses = 0
low = min(-1.0, x)
high = max(1.0, x)
ans = (high + low) / 2.0

while abs(ans**3 - x) >= epsilon:
    print('low =',low,'high =',high,'ans =',ans)
    numGuesses += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
print('numGuesses =',numGuesses)
print(ans, 'is close to the cube root of', x)

