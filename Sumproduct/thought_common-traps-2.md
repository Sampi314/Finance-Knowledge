# Common Traps 2

**Source:** https://sumproduct.com/thought/common-traps-2/

---

[Home](https://sumproduct.com/)

\> Common Traps 2

*   April 12, 2019

Common Traps 2
==============

VBA Blogs: Common Traps 2
=========================

12 April 2019

_Welcome to this week’s VBA blog! In line with previous months, we’re going to keep this month’s blogs on a theme, and this month’s theme is all about common errors and issues that people run into._

This week, we’re going to highlight a common issue that arises when people record macros.

Suppose I have a list of employees and the salaries that they earn. I want a macro that will copy the total salary from this table and paste it elsewhere in my worksheet.

![](<Base64-Image-Removed>)

In the picture above, we are looking to copy the total in B4 and paste it as values in E1. We can record a macro to do this.

![](<Base64-Image-Removed>)

Then, when we want to insert a new name into the list, we might run into issues…

![](<Base64-Image-Removed>)

Wait, what happened? The macro did exactly as we asked it to – go to cell B4, and paste the value into cell E1.

The trick is to make the reference to the cells dynamic instead. Instead of referring to B4, you can go to the target cell and set the Name of the cell to be something unique and relevant, for example:

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

Repeat the process for your target cell, then you can update your macro details accordingly:

![](<Base64-Image-Removed>)

A little clean-up goes a long way!

See you next week for more tips on how to avoid common traps!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/common-traps-2/#0)
    
*   [Register](https://sumproduct.com/thought/common-traps-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/common-traps-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/common-traps-2/#0)

[](https://sumproduct.com/thought/common-traps-2/#0 "close")

top