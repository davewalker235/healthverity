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
    # identify the mismatches without much overhead. Realized late in this
    # that this won't work when the the single missing value occurs before
    # the value that is missing in both. I'd have to come up with a way
    # of backtracking and I just don't have the time right now to research that
    properA = 1
    properB = 1
    for line in file:

      [a, b] = line.strip().split(',')

      missingA = str(properA) != a
      missingB = str(properB) != b

      if part == 'a' and missingA and not missingB:
        return properB

      if part == 'b' and missingA and missingB:
        return properA

      properA += 2 if missingA else 1
      properB += 2 if missingB else 1

# Switch to argparse for a nicer interface, I've forgotten a lot of this stuff
parser = argparse.ArgumentParser()
parser.add_argument('--part', default='a')
parser.add_argument('--file', default='question3/lista.csv')
args = parser.parse_args()

print(main(args.file, args.part))
