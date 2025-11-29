Full Stack Developer – Screening Test

This repository contains my solutions for the screening test.
I completed the test using Python 3, and I have added comments inside each file to explain my thinking and the small decisions I took while writing the code.
My goal was to keep the logic simple, readable, and close to how I normally code so that anyone reviewing it can follow the flow easily.

My Approach (Problem-wise)
1. Calculator Class
I created a class with four basic methods (add, subtract, multiply, divide).
I kept the functions small and handled division carefully so that division by zero doesn’t break the program.

2. Odd Number Generator
For generating odd numbers, I used a loop that starts from 1 and keeps increasing by 2.
This avoids unnecessary checks and keeps the logic straightforward.

3. Conditional Odd Sequence (Step of 3)
This problem extends the previous one, so I reused the idea but changed the increment to 3.
Only numbers that are odd and follow the step pattern get printed.

4. Multiples Counter (3, 5, 7)
I used a simple loop and checked each number with the modulo operator.
Based on whether the number is divisible by 3, 5, or 7, I increased separate counters.

How to Run the Files:
Each problem is in its own .py file.
You can run any file using:

python3 filename.py
(Depending on your system, python may also work)
