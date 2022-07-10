# Chained_Matrix_Multiplication_DP

### Programing Language:
Python

### Purpose:
This program determines the optimal groupings for chained matrix multiplication. <br>
The optimal solution is one with the least number of calulations.

### How it works:
User input is NOT needed. <br>
This program is hard coded for 4 matrices with the following dimensions:<br>
10X5, 5X20, 20X10, and 10X5<br>

The matrices' dimensions are given in a list form as follows: [10, 5, 20, 10, 5].<br>

The program takes the dimensions of the matrices, and calculates the number of calculations required for multiplications. <br>
It returns the groupings for the optimal solutions. <br>

The output for the hard coded example is:

[0, 1000, 1500, 1500]
[None, 0, 1000, 1250]
[None, None, 0, 1000]
[None, None, None, 0]

[None, 0, 0, 0]
[None, None, 1, 2]
[None, None, None, 2]
[None, None, None, None]

( A0 ) ( ( ( A1 ) ( A2 ) ) ( A3 ) )
