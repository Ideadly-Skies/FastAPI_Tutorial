def division(x: int, y: int) -> int:
    return (x // y)

# check this code for type errors using mypy
if __name__ == "__main__":
    a = division(10, 2)
    print(a)

    b = division(5, 2.5)
    print(b)

    c = division("Hello", 10)
    print(c)

    x: int = 3
    y: float = 3.14
    nm: str = 'abc'
    married: bool = False
    names: list = ['a', 'b', 'c']
    marks: tuple = (10, 20, 30)
    marklist: dict = {'a': 10, 'b': 20, 'c': 30}