# If I use VBA Then I get better at it!

**Source:** https://sumproduct.com/thought/if-i-use-vba-then-i-get-better-at-it/

---

[Home](https://sumproduct.com/)

\> If I use VBA Then I get better at it!

*   March 24, 2017

If I use VBA Then I get better at it!
=====================================

VBA Blogs: If I use VBA Then I get better at it!
================================================

24 March 2017

To see the start of our VBA blog series, click [here](https://www.sumproduct.com/blog/article/vba-blogs/introduction-to-vba)
.

This week, we’re going to cover the use of the IF statement in VBA. This is a very useful tool to help apply conditional rules in macros. For example, if you want a macro to run A if a cell is positive, and B if it is negative, you can use the IF statement to check the cell value, and choose what will happen in the true and false cases.

The basic command looks like this:

If <X is true> Then

<Do something>

Else

<Do something else>

End If

You can also use it to run only if the check is true, as long as what you are doing will fit on one line, such as:

If <X is true> Then <Do something>

In this instance, if X is false, nothing will happen.

Let’s look at a specific example. Suppose we want to check if the cell A1 contains a value. If it does, let’s clear the content of the cell. If not, we will copy the value from B1 into A1. We could do this as follows:

If Range(“A1”).Value <> “” Then

Range(“A1”).ClearContents

Else

Range(“B1”).Copy

Range(“A1”).PasteSpecial xlPasteAll

End If

In this, the use of “<>” in the first line means “not equal to”; that is, that the value in cell A1 is not equal to a blank space.

Next Friday will be our Final Friday Fix, so stay tuned for that next week! This blog will see you next in April!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/if-i-use-vba-then-i-get-better-at-it/#0)
    
*   [Register](https://sumproduct.com/thought/if-i-use-vba-then-i-get-better-at-it/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/if-i-use-vba-then-i-get-better-at-it/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/if-i-use-vba-then-i-get-better-at-it/#0)

[](https://sumproduct.com/thought/if-i-use-vba-then-i-get-better-at-it/#0 "close")

top