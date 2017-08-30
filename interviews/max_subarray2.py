#!/usr/bin/env python
#
# -*- coding: utf-8 -*-

# From "Programming pearls" book. Chapter 8: Algorithm design techniques p.80

# ___________________________________________________________
#                                                      NOTES

# Very intuitive, but not optimal solution. See "Programming pearls" for more details.

# ___________________________________________________________
#                                             IMPLEMENTATION

def MAX_SUBARRAY(A):

    # 0 <= low <= high < len(A)
    def FIND_MAX_SUBARRAY(low, high):

        if low > high:
            return 0

        if low == high:
            return max(0, A[low])

        mid = (low + high) / 2

        # Find max crossing to left
        lmax = 0
        sum  = 0

        for i in range(mid, 0, -1):
            sum = sum + A[i]
            lmax = max(lmax, sum)

        # Find max crossing to right
        rmax = 0
        sum = 0
        for i in range(mid + 1, high):
            sum = sum + A[i]
            rmax = max(rmax, sum);

        return max(lmax + rmax,                            # crossing
                   max(FIND_MAX_SUBARRAY(low, mid),        # left
                       FIND_MAX_SUBARRAY(mid + 1, high)))  # right

    return FIND_MAX_SUBARRAY(0, len(A) - 1)

# ___________________________________________________________
#                                                       TEST

if __name__ == '__main__':
    #                                  |max subarray=43|
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print '\nA=%s' % A
    print 'Sum of max sub-array is: %s\n' % MAX_SUBARRAY(A)
