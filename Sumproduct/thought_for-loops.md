# For Loops

**Source:** https://sumproduct.com/thought/for-loops/

---

[Home](https://sumproduct.com/)

\> For Loops

*   April 14, 2017

For Loops
=========

VBA Blogs: For Loops
====================

14 April 2017

Last week, we showed you how to declare variables. This week, we’re going to use a variable to create a loop. Let’s introduce the For loop.

The basics of the For loop involve taking a variable, incrementing it until it gets to a certain target number, and performing a bit of code for each incremental step. It looks a bit like this:

For X = 1 to 10

<Do this code for each of the 10 times>

Next X

We can use this to put together a simple example that counts the number of coin flips land Heads when we flip them 10 times. Let’s combine a few of the things that we’ve learned. If you like, you can copy the text below into VBA, or type it out yourself.

Sub FlipCoins()

Dim X as Integer

‘Declare an integer that will be incremented

Dim Heads as Integer

‘Declare a variable that will store the number of times a coin lands as Heads

Heads = 0

‘Set the initial value for the counter to be zero

For X = 1 to 10

If Rnd() >= 0.5 Then Heads = Heads + 1

‘Take a random number between 0 and 1.  If the value is greater than or equal to 0.5, then add one to the Heads counter.

Next X

MsgBox “You flipped” & Heads & “Heads over 10 coin flips.  Well done!”

End Sub

Have fun flipping coins!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/for-loops/#0)
    
*   [Register](https://sumproduct.com/thought/for-loops/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/for-loops/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/for-loops/#0)

[](https://sumproduct.com/thought/for-loops/#0 "close")

top