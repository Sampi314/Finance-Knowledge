# The A to Z of DAX Functions – LCM

**Source:** https://sumproduct.com/blog/power-pivot-principles-the-a-to-z-of-dax-functions/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – LCM

*   March 17, 2026

The A to Z of DAX Functions – LCM
=================================

__In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions.  This week, we look at **LCM**.__ 

**_The_** _**LCM**_ **_function_**

![](https://sumproduct.com/wp-content/uploads/2026/03/image-97.png)

The **LCM** function is one of the mathematical and trigonometric functions.  It returns the least common multiple of two integers.  The least common multiple is the smallest positive integer that is a multiple of both integer arguments.  You can use **LCM** to add fractions with different denominators, align scheduling cycles or synchronise periodic events in your data model.  It employs the following syntax:

_**LCM**_**(number1,** **number2)**

There are two \[2\] main arguments in this function:

*   **number1**: this argument is required.  It is the first positive integer (or an expression that evaluates to an integer) for which you want the least common multiple.  If the value is not an integer, it is truncated
*   **number2**: this argument is required.  It is the second positive integer (or an expression that evaluates to an integer) for which you want the least common multiple.  If the value is not an integer, it is truncated.

Here are a few remarks about the **LCM** function:

*   if any argument is non-numeric, **LCM** returns the _#VALUE!_ error value
*   if any argument is less than zero \[0\], **LCM** returns the _#NUM!_ error value
*   if **LCM(a, b)** >= 2^53, **LCM** returns the _#NUM!_ error value
*   if either argument is zero \[0\], **LCM** returns zero, since the least common multiple of any number and zero is zero
*   the **LCM** function is related to the **GCD** (Greatest Common Divisor) function.  Indeed, for any two positive integers **a** and **b**, the relationship **LCM(a, b)** × **GCD(a, b)** = **a × b** always holds
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

Rather than demonstrate each scenario separately, we can use a single DAX query with a table constructor to showcase all the key behaviours of the **LCM** function at once:

**EVALUATE**

**{**

  **(“LCM(5,2)”,5,2,LCM(5,2)),**

  **(“LCM(24,36)”,24,36,LCM(24,36)),**

                                 **(“LCM(5.8,3.2)”,5.8,3.2,LCM(5.8,3.2)),**

                                **(“LCM(5,3)”,5,3,LCM(5,3)),**

  **(“LCM(LCM(4,6),10)”,4,6,LCM(LCM(4,6),10))**

**}**

This will return the following Table:

![](<Base64-Image-Removed>)

**_Simple_** **_examples_**

Rows 2 and 3 show the basics.  LCM(5, 2) returns 10 because the multiples of 5 are 5, 10, 15, 20, … and the multiples of 2 are 2, 4, 6, 8, 10, 12, … so the smallest common value is 10.  Similarly, **LCM(24,** **36)** in row 3 returns 72, the smallest number divisible by both 24 and 36.  You can verify: 72 ÷ 24 = 3 and 72 ÷ 36 = 2.

**A** **practical** **scheduling** **scenario**

Row 4 demonstrates a common real-world use case.  Imagine Machine A requires servicing every 12 days and Machine B every 18 days.  **LCM(12, 18)** = 36, telling us both machines will be serviced on the same day every 36 days.  This is exactly the kind of scenario where **LCM** is handy in data models involving scheduling or resource planning.

**_Decimal_** **_handling_**

Rows 5 and 6 highlight an important behaviour.  While Microsoft’s documentation states that non-integer values are “truncated”, in practice LCM(5.8, 3.2) in row 5 returns 6 — this is because 5.8 is rounded to 6 and 3.2 is rounded to 3, giving LCM(6, 3) = 6.  Compare this with row 6, where **LCM(5, 3)** returns 15.  The difference between these two rows confirms that **LCM** rounds its inputs to the nearest integer rather than simply stripping the decimal portion.  This is an important nuance to keep in mind when working with non-integer values.

**_Nesting_** **_LCM_** **_for_** **_three_** **_or_** **_more_** **_numbers_**

Row 7 shows that if you need the **LCM** of more than two numbers, you can nest the function.  **LCM(LCM(4, 6), 10)** returns 60, which is the least common multiple of 4, 6 and 10.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section.  In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
.  If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-the-a-to-z-of-dax-functions/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-the-a-to-z-of-dax-functions/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-the-a-to-z-of-dax-functions/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-the-a-to-z-of-dax-functions/#0)

[](https://sumproduct.com/blog/power-pivot-principles-the-a-to-z-of-dax-functions/#0 "close")

top