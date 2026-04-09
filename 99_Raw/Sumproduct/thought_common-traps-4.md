# Common Traps 4

**Source:** https://sumproduct.com/thought/common-traps-4/

---

[Home](https://sumproduct.com/)

\> Common Traps 4

*   May 3, 2019

Common Traps 4
==============

VBA Blogs: Common Traps 4
=========================

3 May 2019

_Welcome back to the VBA blog series! We’re going to continue with last month’s blog theme, focusing on common errors and issues that people run into._

When we record macros, we’ll often see references to ranges and sheets and so forth. We discussed the pitfalls of using “A1” style references in VBA and how to replace them with Named Ranges in [Common Traps 2](https://www.sumproduct.com/blog/article/vba-blogs/vba-blog-common-traps-2)
.

This time, we’re going to look at the sheet naming convention in a recorded macro. Let’s take a look:

![](<Base64-Image-Removed>)

Here, we have recorded a macro that selected Sheet1, go to cell **A1**, put a value of 10 in the cell and hit enter.

Now, suppose an enterprising analyst decides that the innocuously named “Sheet1” should actually be named something more descriptive, such as “Output”. This results in an error occurring:

![](<Base64-Image-Removed>)

When we click on Debug, we can see the specific area that has fallen over:

![](<Base64-Image-Removed>)

The way we are referring to the sheet here, as “Sheet1”, means that the VBA code will be looking for the sheet named “Sheet1”, which no longer exists. In the Project window, we can see how this works:

![](<Base64-Image-Removed>)

The name inside the brackets (i.e. Output, Sheet2) is effectively the tab name, from the perspective of the user (i.e. what you consider the sheet name to be, that you might rename below the grid). The name in front of the brackets (i.e. Sheet1, Sheet2) refers to the name of the VBA Worksheet object.

So when we refer to Sheets(“Sheet1”), what we’re actually doing is going to the list of all of the sheets, and finding the one that is labelled “Sheet1”. To improve this, what we can consider doing instead is going to the VBA object called “Sheet1” instead, by calling on it as follows:

![](<Base64-Image-Removed>)

This way, we are working directly with the sheet in question, and it won’t break if someone changes the name on the Excel side. This isn’t foolproof, of course, as someone can still rename it in VBA and it will still break in that instance, but hopefully it reduces the likelihood of unintentional errors being caused.

See you next week for more VBA tips!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/common-traps-4/#0)
    
*   [Register](https://sumproduct.com/thought/common-traps-4/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/common-traps-4/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/common-traps-4/#0)

[](https://sumproduct.com/thought/common-traps-4/#0 "close")

top