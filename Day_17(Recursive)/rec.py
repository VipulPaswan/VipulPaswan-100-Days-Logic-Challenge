""" 
Write a recurisive function to print first n natural numbers

1.Assume that the desired recursive function is already defined.
2.Recursive Case
3.Base Case



1.printN(n)         1 2 3 4 5....n-1 n
2.printN(n-1)       1 2 3 4 5....n-1
          print(n)  n
3. n==1             1            

          
"""

def printN(n):
          if(n==1):
                  print(1)
            
          elif(n>1):
                printN(n-1)
                print(n)          
                
printN(5)

#----output --

1
2
3
4
5


'''
🧠 What I learned today — The 3 Essential Techniques of Recursion

These 3 steps apply to almost every recursive function, regardless of language:

1️⃣ Assume the Function Works (Faith Step)

This is the mental trick that makes recursion easier.
You first assume that your recursive function already works for smaller inputs.
This assumption helps build the larger solution without overthinking.

Example thought:

“If printN(n-1) prints numbers from 1 to n-1 correctly,
then I just need to print n.”

2️⃣ Recursive Case (Break the Problem)

Break the big problem into a smaller version of itself.
The recursive case is where:

You reduce the input

You call the function again

You build your full answer step-by-step

This step is where the actual “logic” of recursion happens → reducing the problem.

3️⃣ Base Case (Stopping Condition)

Every recursive function must stop, otherwise it becomes an infinite loop.
The base case defines when the recursion should stop — usually the smallest or simplest input.

Example thought:

“When n becomes 1, stop — because printing 1 is the smallest possible task.”

🔍 Example Concept Used:

A classic recursive pattern — printing the first n natural numbers using only the "assume → reduce → stop" technique:

Recursive case: print numbers from 1 to n-1

Then: print the nth number

Base case: when n == 1 → just print 1

This helps build the sequence in the correct order using pure logic.









'''