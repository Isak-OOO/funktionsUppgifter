n = 8

if n % 2 == 0:
    for i in range((n//2)+1):
        print(f"{('*'*2*i):^{n}}")
else:
    for i in range ((n//2)+1):
        print(f"{('*'*(2*i+1)):^{n}}")