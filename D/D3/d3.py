

def fibonacci(n):
    """Fibonacchi Sequence Generator

    Args:
        n (int): Sequence length

    Yields:
        _int_: fibonacchi number
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

input_sequence = [1, 2, 5, 10]

if __name__ == "__main__":

    for i in input_sequence:
        print(list(fibonacci(i)))