from sub import b


def func():
  print("hello, world!")
  b.a_func(1)
  b.a_func(0)


def main():
  func()


if __name__ == "__main__":
  main()
