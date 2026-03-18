# After You

**Source:** https://sumproduct.com/thought/after-you/

---

[Home](https://sumproduct.com/)

\> After You

*   May 4, 2018

After You
=========

VBA Blogs: After You
====================

4 May 2018

Having stumbled upon the **Find** method last week, we’re going to lay fingers on some of the parameters. [Last time](https://www.sumproduct.com/blog/article/vba-blogs/vba-blog-lost-and-found)
 we did the basic search looking for a simple string within a Range.

Let’s go back to our worksheet last week:

![](<Base64-Image-Removed>)

If we were to perform a simple search for the string “up” on this Range, using the subroutine from last time, it would return “turn up” in **B1**. This is because the **Find** method starts from the upper left corner from the range.

Notice how the cursor is on **C5**. If we were to press Ctrl + F in Excel and use the _Find_ dialogue, it would start the search from that cell.

What if we wanted to find a string with “up” after the word “sight”? How can we tell VBA to behave in the same way as the **Find** dialogue?

This is where the **After** parameter comes in handy. **After** takes a Range of a single cell to use as the basis to search from. If you give **After** a range that is bigger than 1×1, then it will generate the following error:

![](<Base64-Image-Removed>)

**After** is the second parameter of the **Find** method, so we can simply pass it after our search string. We can amend our code as follows:

**Sub** FindAfter()

**Dim** searchRange **As** Range

**Set** searchRange = Range(“A1:E10”)

**Debug.Print** searchRange.Find(“up”, Range(“C5”))

**Debug.Print** searchRange.Find(“up”, Range(“C5”)).Address

**End Sub**

This will result in:

![](<Base64-Image-Removed>)

Success! Notice that **Find** went across the row, which is the default.

Next week we will descry setting parameters in the **Find** function to go down the columns instead.

See you next time!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/after-you/#0)
    
*   [Register](https://sumproduct.com/thought/after-you/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/after-you/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/after-you/#0)

[](https://sumproduct.com/thought/after-you/#0 "close")

top