# This program finds an approximation to the cube root of both
# negative and positive numbwers

x = -0.5
epsilon = 0.01
numGuesses = 0
low = min(0.0, x)
high = max(1, x)
ans = (high + low) / 2.0

while abs(ans**3 - x) >= epsilon and ans**3 < x:
    print('low =',low,'high =',high,'ans =',ans)
    numGuesses += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
if x < 0:
    ans = -ans
print('numGuesses =',numGuesses)
print(ans, 'is close to the cube root of', x)

