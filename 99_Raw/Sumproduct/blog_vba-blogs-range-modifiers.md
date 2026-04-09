# VBA Blogs: Range Modifiers

**Source:** https://sumproduct.com/blog/vba-blogs-range-modifiers/

---

[Home](https://sumproduct.com/)

\> VBA Blogs: Range Modifiers

*   August 17, 2017

VBA Blogs: Range Modifiers
==========================

VBA Blogs: Range Modifiers
==========================

18 August 2017

Last week we spoke about ranges and how you can refer to them in different ways. This week, we’re going to look at some of the ways you can apply range modifiers to change what set of cells exactly you’re referring to.

![](<Base64-Image-Removed>)

The first two are probably the most common ones that we tend to see in code. The Offset property is a simple way of choosing cells with reference to a single base cell. This can be used to start in a single row, and loop through code a number of times, referring to a new row with each loop. The loop variable that is increasing in size (e.g. in a For loop) can be set as the ‘r’ value in the Offset property, for example.

The second property is useful when you know where your data starts at the top of a column, but you don’t know where it ends. Range(“A1”).End(xlDown) will go to the bottom of your dataset, so you can determine where your last data point is.

You can actually combine these properties together as well – to select the next new row at the bottom of your data, you can use Range(“A1”).End(xlDown).Offset(1,0) to firstly go to A1, go down to the bottom of your data, then offset the result by one row down, to pick the next blank row.

These are really useful tools that you can use to adjust the ranges that you refer to, helping you run loops or work with uncertain sizes of data. Next week is the Final Friday Fix, but we’ll return in September with other range properties and methods that you can apply. See you then!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/vba-blogs-range-modifiers/#0)
    
*   [Register](https://sumproduct.com/blog/vba-blogs-range-modifiers/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/vba-blogs-range-modifiers/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/vba-blogs-range-modifiers/#0)

[](https://sumproduct.com/blog/vba-blogs-range-modifiers/#0 "close")

top