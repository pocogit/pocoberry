def p(n):
    """Return True if it is a prime n."""
    for e in range(2,n):
        if n % e == 0:
	    print e
            return False
    return True

def next_p(n):
    """find the closest prime n larger than *n*."""
    i = n
    while True:
        i += 1
        if p(i):
            print(i)


