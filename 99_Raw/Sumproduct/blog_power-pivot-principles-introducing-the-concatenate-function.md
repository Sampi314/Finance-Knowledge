# Power Pivot Principles: Introducing the CONCATENATE Function

**Source:** https://sumproduct.com/blog/power-pivot-principles-introducing-the-concatenate-function/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Introducing the CONCATENATE Function

*   June 3, 2019

Power Pivot Principles: Introducing the CONCATENATE Function
============================================================

Power Pivot Principles: Introducing the CONCATENATE Function
============================================================

4 June 2019

_Welcome back to our Power Pivot blog. Today, we introduce the CONCATENATE function._

The **CONCATENATE** function takes two text strings and joins them into one text string. It uses the following syntax to operate:

**CONCATENATE**( <text1>, <text2>)

Simple?

Let’s move on to an example. Assuming we have the following Table with product descriptions split up into three columns arranged in a “realistic” but poor way, _viz._

![](<Base64-Image-Removed>)

We want to combine the data into a product description column of some sort, such as

![](<Base64-Image-Removed>)

Using the **CONCATENATE** function in Power Pivot:

\=CONCATENATE(

‘Concatenate'\[Column1\],

CONCATENATE(

‘Concatenate'\[Column2\],’Concatenate'\[Column3\]

)

)

we obtain

![](<Base64-Image-Removed>)

With that example, the limitations of the **CONCATENATE** function becomes painfully apparent, it can only accept two text inputs at once!

Imagine the nightmare nested **CONCATENATE** formula we would have to create if we wanted to include spaces ” ” in between each column.

Luckily, there is an alternative. We can use the ‘&’ operator, it is the equivalent text concatenation _operator_.

Using the ‘&’ operator, we can concatenate the three columns like this, also including the spaces in between!

**\=’Concatenate'\[Column1\]&****” “****&’Concatenate'\[Column2\]&****” “****&’Concatenate'\[Column3\]**

![](<Base64-Image-Removed>)

Of course, if you really wanted you could combine the ‘&’ operator into the **CONCATENATE** function:

\=CONCATENATE(

‘Concatenate'\[Column1\]&” “,’Concatenate'\[Column2\]&” “&’Concatenate'\[Column3\]

)

![](<Base64-Image-Removed>)

But we probably wouldn’t… the ‘&’ operator is just much easier to use, and simpler for other users to understand.

That’s it for this week, tune in next week for more Power Pivot! Until then, happy pivoting!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-introducing-the-concatenate-function/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-introducing-the-concatenate-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-introducing-the-concatenate-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-introducing-the-concatenate-function/#0)

[](https://sumproduct.com/blog/power-pivot-principles-introducing-the-concatenate-function/#0 "close")

top