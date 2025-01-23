from sub import b


def func():
  print("hello, world!")
  b.c.a_func(1)
  b.c.a_func(0)


def main():
  func()


if __name__ == "__main__":
  main()
