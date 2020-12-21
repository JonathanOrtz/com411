def search(document):
  print("Searching...")
  with open(document) as file:
    for line in file.readlines():
      print(f'Loocked in {line.strip()}')
    print('Done!')
def calling():
  search('data/file/txt/locations.txt')
calling()