My python skills are a bit rusty, so please excuse the simplicity of the code
Also, with my background in web development memory space allocation has never
been something that I've really had to be concerned with. Home Solar
multiprocessing and general API limitations

https://github.com/davewalker235/exercism
Project Euler

In all honesty in my main work doing web development I've never had to really
dig into memory use and Big O notation. In the past I've used python's
multiprocessing module to overcome some painfully slow API access issues for
NRG's Home Solar usage data. I've also done some async work with Bloomberg's
excel api. This is an area that I'd like to improve in, unfortunately it's
never been something my work has demanded. I'm familiar with the concepts and
would be eager to learn and practice strategies for optimizing memory use and
writing more efficient code.

# Question 1

## Part A
This is a pattern I commonly use in erlang, so I've ported the basic idea to python here. It's just a recursive function that jumps through the data structure passing a counter
and a set of seen indecies. Once it encounter's an index that it's already seen it
can infer that the logic will start looping and it returns the current counter value.

## Part B
In solving part A I would need to do more research on python's garbage collector
and make sure I'm just passing references to the originial list without copying
it. The set of seen indicies will be an issue since it will grow to the size
of the unique values the seed list outputs. Lookup time on the set will also be
an issue, and obviously my test cases are too small to benchmark effectively. This
would require some research into different search algorithms and data structures.
Currently, this is not one of my strengths.


# Question 2

## Part A

Obviously this is a pretty naive solution, but given the time constraints this
will work. I haven't done any serious load testing, but there are a
couple basic test files in the question2 folder with about 10k lines for a
sanity check.

The question wording was a bit vague as to the exact requirements so I'm
operating under the assumption the output should do a full comparison of the
files regardless of order. Otherwise this could be simplified to do a line diff
by reading through both files in parallel. Most of my experience is in web
development, so I'm not very comfortable with advance algorithms and memory
use for heavy data processing.

## Part B

Absolutely. Again, large data processing is not my main skill. There are a
plethora of diffing strategies out there that would need to be researched. I'd
probably also want to consider using a different language to optimize memory
use, Rust comes to mind. This would also require a more robust testing and
benchmarking strategy than I've put together for this exercise.

# Question 3

##
