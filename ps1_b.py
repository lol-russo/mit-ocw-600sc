# Problem Set 1, from Lecture 2 https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-4-machine-interpretation-of-a-program/MIT6_00SCS11_ps1.pdf

# Problem 2
#
# Now write a program that calculates the minimum fixed monthly payment needed in order pay
# off a credit card balance within 12 months. We will not be dealing with a minimum monthly
# payment rate.
#
# Take as raw_input() the following floating point numbers:
#    1. the outstanding balance on the credit card
#    2. annual interest rate as a decimal
#
# Print out the fixed minimum monthly payment, number of months (at most 12 and possibly less
# than 12) it takes to pay off the debt, and the balance (likely to be a negative number).
#
# Assume that the interest is compounded monthly according to the balance at the start of the
# month (before the payment for that month is made). The monthly payment must be a multiple of
# $10 and is the same for all months. Notice that it is possible for the balance to become negative
# using this payment scheme. In short:
#
# Monthly interest rate = Annual interest rate / 12.0
# Updated balance each month = Previous balance * (1 + Monthly interest rate) – Minimum
# monthly payment
