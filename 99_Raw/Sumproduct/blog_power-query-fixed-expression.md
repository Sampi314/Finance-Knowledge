# Power Query: Fixed Expression

**Source:** https://sumproduct.com/blog/power-query-fixed-expression/

---

[Home](https://sumproduct.com/)

\> Power Query: Fixed Expression

*   June 15, 2021

Power Query: Fixed Expression
=============================

Power Query: Fixed Expression
=============================

16 June 2021

_Welcome to our Power Query blog. This week, I look at the M function Expression.Constant()._

I have different types of constant data in each column as follows:

![](<Base64-Image-Removed>)

I am going to use the following function to show how data like this is created in **M** code:

            **Expression.Constant(value** as any**)** as text

This returns the **M** source code representation of a constant **value**.

I will create a custom column on the ‘Add Column’ tab for each of my columns.

![](<Base64-Image-Removed>)

The results for **Last Name** are:

![](<Base64-Image-Removed>)

For text values, I get the original text in speech marks (**“”**). I would argue with the Microsoft definition, as the value returned is type Any, not Text. This process will be repeated if I apply **Expression.Constant()** to **EC Last Name**.

![](<Base64-Image-Removed>)

Now I have two speech marks around each quotation mark. Curious to see what happens next? Me too…

![](<Base64-Image-Removed>)

So, I am adding two, then four, then eight speech marks. That’s enough for that one, I think. On to **Employee ID**:

![](<Base64-Image-Removed>)

My numerical value is simply converted to type Any. Applying **Expression.Constant()** to **EC Employee ID** would just add speech marks and I don’t want to do that again!

The next column is **Start Date**:

![](<Base64-Image-Removed>)

This time, the value returned is the **M** code that would be used to create the date from the base values of year, month and day.

![](<Base64-Image-Removed>)

Similarly for **Duration**, I get the **M** code to create the duration from the number of days, hours, minutes and seconds.

![](<Base64-Image-Removed>)

Finally, I get a similar result for **Time**, where I have the **M** code to create the time value from the number of hours, minutes and seconds.

Next time I’ll look at a related function **Expression.Evaluate()**.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-fixed-expression/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-fixed-expression/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-fixed-expression/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-fixed-expression/#0)

[](https://sumproduct.com/blog/power-query-fixed-expression/#0 "close")

top