import argparse

def main(filename, part):
  """
  Compare two files of newline separated strings and return the number of
  strings both files share.

  lista.txt is missing 75, Column A is missing 82

    $ question3.py --part a --file question3/lista.txt
      82

  """
  with open(filename, 'r') as file:
    properA = 0
    properB = 0
    for line in file:
      properA += 1
      properB += 1
      [a, b] = line.strip().split(',')

      if str(properA) != a and str(properB) != b:
        if part == 'b':
          return properA
        else:
          properA += 1
          properB += 1

      if str(properA) != a and str(properB) == b:
        properA += 1
        if part == 'a':
          return b

# Switch to argparse for a nicer interface, I've forgotten a lot of this stuff
parser = argparse.ArgumentParser()
parser.add_argument('--part', default='a')
parser.add_argument('--file', default='question3/lista.csv')
args = parser.parse_args()

print(main(args.file, args.part))
