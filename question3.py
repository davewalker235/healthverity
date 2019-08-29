import argparse

def main(filename, part):
  """
  Compare two csv files, --part a returns the number missing from column A,
  --part b returns the number missing from both

  lista.txt is missing 75, Column A is missing 82
  listb.txt is missing 68, Column A is missing 59

    $ question3.py --part a --file question3/lista.txt
      82

  """
  with open(filename, 'r') as file:
    # We're going to keep a counter for each column to track what we expect
    # the integer to be and compare it with the values. This should let us
    # identify the mismatches without much overhead
    properA = 1
    properB = 1
    for line in file:
      [a, b] = line.strip().split(',')

      missingA = str(properA) != a
      missingB = str(properB) != b

      print(a, properA, b, properB, missingA, missingB)

      if part == 'a' and missingA and not missingB:
        return properB

      if part == 'b' and missingA and missingB:
        return properA

      if not missingA: properA += 1
      if not missingB: properB += 1



      # if str(properA) != a and str(properB) != b:
      #   print('parta', a, b, properA, properB)
      #   if part == 'b':
      #     return properA
      #   else:
      #     properA += 1
      #     properB += 1
      #
      # if str(properA) != a and str(properB) == b:
      #   print('partb', a, b, properA, properB)
      #
      #   properA += 1
      #   if part == 'a':
      #     return properB

# Switch to argparse for a nicer interface, I've forgotten a lot of this stuff
parser = argparse.ArgumentParser()
parser.add_argument('--part', default='a')
parser.add_argument('--file', default='question3/lista.csv')
args = parser.parse_args()

print(main(args.file, args.part))
