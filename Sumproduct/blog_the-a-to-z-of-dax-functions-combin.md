# The A to Z of DAX Functions – COMBIN

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-combin/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – COMBIN

*   May 10, 2022

The A to Z of DAX Functions – COMBIN
====================================

Power Pivot Principles: The A to Z of DAX Functions – COMBIN
============================================================

10 May 2022

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **COMBIN**._

**The COMBIN function**

Are you often **COMBIN** the DAX functions to see how many subsets you can make? This function returns the number of combinations for a given number of items (_i.e._ the number of distinct subsets of items where order is unimportant). You should use **COMBIN** to determine the total possible number of groups for a given number of items.

The **COMBIN** function employs the following syntax to operate:

**COMBIN(number, number\_chosen)**

The **COMBIN** function has the following arguments:

*   **number:** this is required and represents the number of items
*   **number\_chosen:** this is also required. This denotes the number of items in each combination.

It should be further noted that:

*   numeric arguments are truncated to integers
*   if either argument is nonnumeric, **COMBIN** returns the _#VALUE!_ error value
*   if **number** < 0, **number\_chosen** < 0, or **number** < **number\_chosen**, **COMBIN** returns the _#NUM!_ error value
*   a combination is any set or subset of items, regardless of their internal order. Combinations are distinct from permutations, for which the internal order is significant
*   the number of combinations is as follows, where **number** = **n** and **number\_chosen** = **k**:

![](<Base64-Image-Removed>)

where:

![](<Base64-Image-Removed>)

*   and **n!** denotes **n** x (**n** – 1) x … x 2 x 1
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

Please see my example below:

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

Sorry to ruin the ending of Series 927 for you…

_Come back next week for our next post on Power Pivot in the_ _[Blog](https://www.sumproduct.com/blog)
_ _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-combin/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-combin/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-combin/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-combin/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-combin/#0 "close")

top