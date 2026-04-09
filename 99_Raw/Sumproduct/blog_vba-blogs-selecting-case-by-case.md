# VBA Blogs: Selecting Case By Case

**Source:** https://sumproduct.com/blog/vba-blogs-selecting-case-by-case/

---

[Home](https://sumproduct.com/)

\> VBA Blogs: Selecting Case By Case

*   February 14, 2019

VBA Blogs: Selecting Case By Case
=================================

VBA Blogs: Selecting Case By Case
=================================

15 February 2019

_This month, we’re talking about the Select Case statement in VBA. We had a question from a client that we thought we’d take the opportunity to answer here._

A client has asked us about the overall efficiency of the Select Case statement, and whether it was a problem that we might have dozens of different Case statements. In particular, his concern was that if the macro found the answer in the very first statement, that it would then waste time checking against every other Case in the list. Given that this was being run once per row, for thousands of rows, he felt justifiably concerned!

Well, there’s an easy way to test this. We can take the numeric example we showed last week, and amend it slightly so that two cases overlap:

![](<Base64-Image-Removed>)

In this instance, if we provide a margin value of 0.8, it should trigger the first case statement. Then, if we don’t get a second message box, then we can confirm it stops after hitting the first Case statement. Otherwise, if we get the second message box, then we will know that it jumps to End Select once it’s completed a Case successfully.

As it turns out, it does jump to the end. So even if you have dozens of Case statements, if the first one is true, it will ignore the rest and go straight to the end, saving a bit of processing time from checking the other Cases.

So there you go – all the useful things to know about how to use Select Case. Have fun with it, and we’ll see you at the next blog with something new to learn!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/vba-blogs-selecting-case-by-case/#0)
    
*   [Register](https://sumproduct.com/blog/vba-blogs-selecting-case-by-case/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/vba-blogs-selecting-case-by-case/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/vba-blogs-selecting-case-by-case/#0)

[](https://sumproduct.com/blog/vba-blogs-selecting-case-by-case/#0 "close")

top