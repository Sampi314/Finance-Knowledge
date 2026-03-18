# Power Pivot Principles: Conditional Custom Columns with Four Categories

**Source:** https://sumproduct.com/blog/power-pivot-principles-conditional-custom-columns-with-four-categories/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Conditional Custom Columns with Four Categories

*   April 15, 2019

Power Pivot Principles: Conditional Custom Columns with Four Categories
=======================================================================

Power Pivot Principles: Conditional Custom Columns with Four Categories
=======================================================================

16 April 2019

_Welcome back to our Power Pivot blog. Today, we discuss how to create conditional custom columns using the AND ‘&&’ and OR ‘||’ operators together._

Today, we discuss how to create a custom column that requires both the **AND** and **OR** functions nested in an **IF** statement for our required result.

Let’s have a look at the following Table:

![](<Base64-Image-Removed>)

We have a Table with four categories this time, and a column with the customer names we have all grown so very fond of.

For the purposes of this exercise, let’s assume that we wish to create a conditional column that will return with the value “Eligible” if a customer is “Y” in Category 1 and either “>0” in Category 3 or “1” in Category 4.

We would use the following code to create our custom column:

\=**IF**(**AND**(\[Category 1\]=”Y”,**OR**(\[Category 3\]>0,\[Category 4\]=1)),”Eligible”,**BLANK**())

As we can see our logic works and we get the desired result:

![](<Base64-Image-Removed>)

That’s easy, but what if we want a conditional column with four conditions? Where we want a ‘Eligible’ to appear when a customer has both “Y” in Category 1 and “Y” in Category 2 and either “>0” in Category 3 or “1” in Category 4.

We will have to use a nested **IF** and **AND** formula:

\=**IF**(**AND**(**AND**(\[Category 1\]=”Y”,\[Category 2\]=”Y”),**OR**(\[Category 3\]>0,\[Category 4\]=1)),”Eligible”,**BLANK**())

The formula is a little complicated, but it achieves the intended result:

![](<Base64-Image-Removed>)

Let’s see if we can do better using the “**||**” and “**&&**” operators:

\=**IF**((\[Category 1\]=”Y” && \[Category 2\]=”Y”) && (\[Category 3\]>0 || \[Category 4\]=1),”Eligible”,**BLANK**())

![](<Base64-Image-Removed>)

We think this formula has improved readability compared to the nested **IF** statements.

That’s it for this week, tune in next week for more Power Pivot, until then happy pivoting!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-conditional-custom-columns-with-four-categories/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-conditional-custom-columns-with-four-categories/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-conditional-custom-columns-with-four-categories/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-conditional-custom-columns-with-four-categories/#0)

[](https://sumproduct.com/blog/power-pivot-principles-conditional-custom-columns-with-four-categories/#0 "close")

top