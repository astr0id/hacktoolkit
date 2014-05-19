"""http://projecteuler.net/problem=056

Powerful digit sum

A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.
Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?

Solution by jontsai <hello@jontsai.com>
"""
from utils import *

EXPECTED_ANSWER = 972

max_so_far = 0

for a in xrange(1, 100):
    for b in xrange(1, 100):
        value = a ** b
        max_so_far = max(sum_digits(value), max_so_far)

answer = max_so_far

print 'Expected: %s, Answer: %s' % (EXPECTED_ANSWER, answer)

