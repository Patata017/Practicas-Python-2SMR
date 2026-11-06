import Factorial

def permutacion (n,k):
    fn=Factorial(n)
    fnk=Factorial(n-k)
    per=fn/fnk
    return per
