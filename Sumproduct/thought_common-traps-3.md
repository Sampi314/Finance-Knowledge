# Common Traps 3

**Source:** https://sumproduct.com/thought/common-traps-3/

---

[Home](https://sumproduct.com/)

\> Common Traps 3

*   April 19, 2019

Common Traps 3
==============

VBA Blogs: Common Traps 3
=========================

19 April 2019

_Welcome to this week’s VBA blog! In line with previous months, we’re going to keep this month’s blogs on a theme, and this month’s theme is all about common errors and issues that people run into._

This week, we’re going to highlight a common issue that follows on from last week’s macro.

Last week, we copied and pasted a cell value into a new location:

![](<Base64-Image-Removed>)

Of course, once the macro finishes running, we might click somewhere on the sheet and hit Enter to move down a row:

![](<Base64-Image-Removed>)

Goodness, what’s happened here? If we go back to the moment just before we hit Enter, you might notice something about the image:

![](<Base64-Image-Removed>)

See the dotted green border around the cell B4? Often referred to as the “dancing ants” colloquially, this indicates that a cell has been cut or copied or is otherwise on the clipboard for use. Zooming out further, we might have seen the note in the bottom left corner of the screen:

![](<Base64-Image-Removed>)

This is a common problem when macros are written, that clean-up isn’t properly done once the macro finishes, so people may be caught unawares by what is left over in the clipboard.

How do we avoid this? After pasting our result, we simply need to use the line:

Application.CutCopyMode = False

Thus, we end up with the code:

![](<Base64-Image-Removed>)

Nice and simple! Come back next week for more practical tips to avoid common traps!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/common-traps-3/#0)
    
*   [Register](https://sumproduct.com/thought/common-traps-3/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/common-traps-3/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/common-traps-3/#0)

[](https://sumproduct.com/thought/common-traps-3/#0 "close")

top