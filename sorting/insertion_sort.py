#!/usr/bin/env python
#
# -*- coding: utf-8 -*-

# Chapter 2: Insertion Sort p.16-18

# ___________________________________________________________
#                                                      NOTES

# We start with the second one and traverse previous(sorted one) one for suitable place to
# insert it. If we find such place we have to shift all. Do we have place to shift?  We
# could have if we imagine that current element (for which we search proper place) is
# removed from the array and there is gap. Now int is not a problem to shift. So the more
# sorted the array is, the less work insertion sort will do.

# The numbers that we wish to sort are also known as the 'keys'.

# Code highlights:

# Shifting array elements backward

# while (j >= 0) and (A[j] > key):
#     A[j + 1] = A[j]
#     j = j - 1

# ___________________________________________________________
#                                             IMPLEMENTATION

def INSERTION_SORT(A):

    for i in range(1, len(A)):
        key = A[i]             # 'remove' current element
        j = i - 1              # start traverse previous(already sorted) starting from the biggest one

        while (j >= 0) and (A[j] > key):
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key

# ___________________________________________________________
#                                                       TEST

if __name__ == '__main__':
    import random

    L = [random.randint(1, 50) for _ in range(10)]

    print L
    INSERTION_SORT(L)
    print L
