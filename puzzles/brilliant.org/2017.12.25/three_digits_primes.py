import numpy
import itertools


def get_sieve(size=1000):
    arr = numpy.full(size, True, dtype=bool)
    arr[0] = arr[1] = False
    # Eliminate even numbers (except 2)
    for i in xrange(4, size, 2):
        arr[i] = False

    for i in xrange(2, size):
        if arr[i]:  # is prime
            for j in xrange(i * i, size, i):
                arr[j] = False

    return arr


if __name__ == '__main__':
    # https://brilliant.org/weekly-problems/2017-12-25/intermediate/?p=3
    # Are there any three distinct digits such that all six permutations are prime numbers?
    size = 1000
    sieve = get_sieve(size=size)
    primes = [x[0] for x in zip(range(size), sieve) if x[1]]
    print "primes:\n%s" % (primes,)
    digits = (1, 3, 7, 9)  # no even digits and 5
    three_digit_permutation_primes_exist = False
    for abc in itertools.combinations(digits, 3):
        is_prime = True
        for a1, b1, c1 in itertools.permutations(abc, 3):
            x = a1 * 100 + b1 * 10 + c1
            if not sieve[x]:
                print "not prime %s, counterexample: %s" % (abc, x)
                is_prime = False
                break
        if is_prime:
            print "prime: %s" % (abc,)
            three_digit_permutation_primes_exist = True
    if three_digit_permutation_primes_exist:
        print "Yes"
    else:
        print "No"
    # For combination with repetition the answer would be yes with:
    # (1, 1, 3), (1, 9, 9) and (3, 3, 7)
