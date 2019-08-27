My python skills are a bit rusty, so please excuse the simplicity of the code
Also, with my background in web development memory space allocation has never
been something that I've really had to be concerned with. Home Solar
multiprocessing and general API limitations

https://github.com/davewalker235/exercism
Project Euler

Question 1
===============================================================================
In all honesty in my main work doing web development I've never had to really
dig into memory use and Big O notation. In the past I've used python's
multiprocessing module to overcome some painfully slow API access issues for
NRG's Home Solar usage data. I've also done some async work with Bloomberg's
excel api. This is an area that I'd like to improve in, unfortunately it's
never been something my work has demanded. I'm familiar with the concepts and
would be eager to learn and practice strategies for optimizing memory use and
writing more efficient code.


Question 2
===============================================================================

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

Given the opportunity I'd be interested to learn more. In the past I have done
a bit of experimentation on ProjectEuler.net to get better at writing
efficient code for large or computationally intensive tasks. However, this type
of work has not been something I commonly encounter in my day to day work. If
I had to make this work for a billion lines I would do a lot more discovery
about the use case and then dig into research on various data structures and
diffing algorithms. I'd also develop a more robust benchmarking data set to
test against.


Question 3
===============================================================================
