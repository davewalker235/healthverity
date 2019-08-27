import sys

def main():
  """
  Compare two files of newline separated strings and return the number of
  strings both files share.

    $ question2.py question2/one.txt question2/two.txt
      9990

  """
  [name, filea, fileb] = sys.argv
  with open(filea, 'r') as fa, open(fileb, 'r') as fb:
    print(len(set(fa) & set(fb)))

main()
