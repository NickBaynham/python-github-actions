def fib(n: int) -> int:
    return n if n < 2 else fib(n-1)+fib(n-2)

def test_fib():
    assert fib(10) == 54
