# VBA Blogs: Cleaning Up Recorded Macros

**Source:** https://sumproduct.com/blog/vba-blogs-cleaning-up-recorded-macros/

---

[Home](https://sumproduct.com/)

\> VBA Blogs: Cleaning Up Recorded Macros

*   February 16, 2017

VBA Blogs: Cleaning Up Recorded Macros
======================================

VBA Blogs: Cleaning Up Recorded Macros
======================================

17 February 2017

We’re going to finish off discussion on recording macros by teaching you to clean them up and make them look more professional. Let’s consider the code that we finished off with last week:

![](<Base64-Image-Removed>)

Let’s start by looking at the green lines. The four lines at the top that start with an inverted comma (‘) are comments. In technical terms, any row that starts with an inverted comma is ignored by a macro, so you can type whatever you like in these cells. So, practically speaking, they are used by people to leave notes and remarks about the macro for others to review in the future.

![](<Base64-Image-Removed>)

Secondly, let’s look at each of the lines of real code. The first line selects the “Start” range name. The second line then takes whatever had been selected and copies it. Wouldn’t it make more sense to combine them instead?

![](<Base64-Image-Removed>)

So, instead of selecting a specific cell, then copying the selection, we can instruct Excel to simply copy the specific cell in a single step. In case you’re wondering, this doesn’t work for the Paste command, since Ctrl-V isn’t something you do to a specific cell (think what happens if you copy a picture, rather than another cell) but instead, something you do to an entire sheet. However, if you use Paste Special, you can apply that action to the Range object.

Another tell-tale sign that a macro has been recorded is in the indentation for the code – typically indentation is only used for loops and If statements. We’ll get to those in due course. For now though, you can delete the indents at the start of each line.

Finally, the last bit that we can easily change is the very first lines – what’s the name of the macro? Rather than call it Macro1, we can call it something a bit more meaningful.

![](<Base64-Image-Removed>)

There we go – a more professional looking macro that doesn’t immediately look like it’s been recorded. I hope this short series has been of use to you in starting out on your macro journey. Keep an eye out for our next set of VBA blogs, coming soon!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/vba-blogs-cleaning-up-recorded-macros/#0)
    
*   [Register](https://sumproduct.com/blog/vba-blogs-cleaning-up-recorded-macros/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/vba-blogs-cleaning-up-recorded-macros/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/vba-blogs-cleaning-up-recorded-macros/#0)

[](https://sumproduct.com/blog/vba-blogs-cleaning-up-recorded-macros/#0 "close")

top