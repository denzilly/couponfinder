# Coupon Finder

This is a simple script to find coupon codes for domino's NL.

It is pretty basic and takes a while, considering most codes that I have seen are 6 digits, it takes around 2 days to check all of them.
It uses selenium to drive a browser and place a pretend order, trying coupon codes in sequence, one-by-one. It stores successful coupons to a .csv file in the
directory from which it was run.
