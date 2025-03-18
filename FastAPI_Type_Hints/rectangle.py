class rectangle:
    # Rectangle constructor
    def __init__(self, w: int, h: int) -> None:
        self.width = w
        self.height = h

# compute area of rectangle
def area(r: rectangle) -> int:
    return r.width * r.height

if __name__ == "__main__":
    

    r1 = rectangle(10, 20)
    print("area = ", area(r1))