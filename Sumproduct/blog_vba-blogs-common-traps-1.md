# VBA Blogs: Common Traps 1

**Source:** https://sumproduct.com/blog/vba-blogs-common-traps-1/

---

[Home](https://sumproduct.com/)

\> VBA Blogs: Common Traps 1

*   April 4, 2019

VBA Blogs: Common Traps 1
=========================

VBA Blogs: Common Traps 1
=========================

5 April 2019

_Welcome to this week’s VBA blog! In line with previous months, we’re going to keep this month’s blogs on a theme, and this month’s theme is all about common errors and issues that people run into._

Suppose I’m entering in a simple formula that checks a value for a particular name, and provides an answer. It might look something like this:

\=IF(G2=”Amy”,1,IF(G2=”Billy”,2,3))

If I’m using VBA to populate this, I might think that I can just use the following line of code:

rng.Formula = “IF(G2=”Amy”,1,IF(G2=”Billy”,2,3))”

However, this quickly gives me an error:

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

Hm, what’s happened here? Using quotation marks has meant that my VBA code is processing the second set of quotation marks just before Amy as the end of my text string, and is expecting the code to stop at that point (or do something to add onto the text string, such as concatenate additional items).

What can we do to avoid this problem? Well, if we want to tell VBA that we want to use those quotes as part of the text string, we need to type it in twice:

rng.Formula = “IF(G2=””Amy””,1,IF(G2=””Billy””,2,3))”

This tells VBA that the quotation mark isn’t the end of the string – it’s merely a character that we want to use. Then, the formula works perfectly:

![](<Base64-Image-Removed>)

Hopefully you won’t get caught out using hard-coded parameters in the future now! See you next week for more common traps in VBA!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/vba-blogs-common-traps-1/#0)
    
*   [Register](https://sumproduct.com/blog/vba-blogs-common-traps-1/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/vba-blogs-common-traps-1/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/vba-blogs-common-traps-1/#0)

[](https://sumproduct.com/blog/vba-blogs-common-traps-1/#0 "close")

top