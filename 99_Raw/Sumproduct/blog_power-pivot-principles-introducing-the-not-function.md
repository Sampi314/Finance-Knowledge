# Power Pivot Principles: Introducing the NOT Function

**Source:** https://sumproduct.com/blog/power-pivot-principles-introducing-the-not-function/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Introducing the NOT Function

*   May 27, 2019

Power Pivot Principles: Introducing the NOT Function
====================================================

Power Pivot Principles: Introducing the NOT Function
====================================================

28 May 2019

_Welcome back to our Power Pivot blog. Today, we introduce the NOT function._

Sometimes we must create custom columns that return with either TRUE or FALSE values. We may also have to create custom columns that have inverse values to another logical column. For example, if we create a custom column with TRUEor FALSE values, we would create another column with the inverse TRUE or FALSE value for each row.

To kick start this example we are going to revisit the custom columns we created for the [Conditional Custom Columns Using IF, OR and ‘||’](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-conditional-custom-columns-using-if-or-and)
 blog.

We will use the following Table:

![](<Base64-Image-Removed>)

After importing the Table into our data model we are going to create a simple custom column that returns with TRUE when Category 1 is ‘Y’ or Category 2 is ‘N’ (you can read more about using the ‘||’ delimiter [here](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-conditional-custom-columns-using-if-or-and)
):

\=**IF**(\[Category 1\]=”Y” || \[Category 2\]=”N”,**TRUE**,**FALSE**)

![](<Base64-Image-Removed>)

Say we need to create a column with the inverse TRUE or FALSE values, we can use the **IF** function:

\=**IF**(Table1\[Included\]=**TRUE**,**FALSE**,**TRUE**)

![](<Base64-Image-Removed>)

We can also use the **NOT** function.

The **NOT** function uses the following syntax:

\=**NOT**(\[Calculated Column\])

With that in mind we can create the following calculated column:

\=**NOT**(Table1\[Included\])

![](<Base64-Image-Removed>)

Rather simple, yes?

One important point to note is that the **NOT** function requires the \[Calculated Column\] input to have TRUE or FALSE values. Text values will not be accepted by the **NOT** function, even if they literally say ‘TRUE’ or ‘FALSE’.

![](<Base64-Image-Removed>)

That’s it for this week, tune in next week for more Power Pivot! Until then, happy pivoting!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-introducing-the-not-function/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-introducing-the-not-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-introducing-the-not-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-introducing-the-not-function/#0)

[](https://sumproduct.com/blog/power-pivot-principles-introducing-the-not-function/#0 "close")

top