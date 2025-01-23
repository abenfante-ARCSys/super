from a import * 

print(*list(locals().items()), sep='\n')

if __name__ == "__main__":
  func()
