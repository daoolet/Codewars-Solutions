def fibonacci(n: int) -> int:
    """Given a positive argument n, returns the nth term of the Fibonacci Sequence.
    """
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
        
    return a