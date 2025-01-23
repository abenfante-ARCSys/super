import pckg_a

print(*list(locals().items()), sep='\n')

if __name__ == "__main__":
  pckg_a.a.func()
