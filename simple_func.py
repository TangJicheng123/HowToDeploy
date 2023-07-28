from internal import add1


def simple_add(x: str) -> str:
    y = add1.my_add_func(x)
    return y

if __name__ == "__main__":
    print(f"[test] {simple_add(123)}")