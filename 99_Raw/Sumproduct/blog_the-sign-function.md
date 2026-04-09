# A to Z of Excel Functions: The SIGN function

**Source:** https://sumproduct.com/blog/the-sign-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The SIGN function

*   June 23, 2025

A to Z of Excel Functions: The SIGN function
============================================

Welcome back to our regular A to Z of Excel Functions blog. Today we look at the SIGN function.

**The SIGN function**

![](https://sumproduct.com/wp-content/uploads/2025/06/SIGN.jpg)

On the face of it, **SIGN** does not appear to be the most adventurous function in Excel.  It determines the sign of a number as:

*   **1:** if positive
*   **\-1:** if negative
*   **0:** if zero \[0\].

The **SIGN** function employs the following syntax to operate:

> **SIGN(number)**

The **SIGN** function has the following argument:

*   **number:** this is required and represents any real **number**.

The examples do not appear to enthral: 

![](https://sumproduct.com/wp-content/uploads/2025/06/SIGN1.jpg)

Can we make this more exciting?  Yes we can!

**_Multiple Criteria with OR_**

Excel has two functions that deal with the logical operator **OR**:

1.  **OR(Condition\_1,Condition\_2,…)** checks to see if any of the logical conditions specified are TRUE.  As long as at least one condition is TRUE, **OR** will be TRUE also
2.  **XOR(Condition\_1,Condition\_2,…)** checks to see if each of the logical conditions specified are TRUE.  As long as an odd number of conditions are TRUE, **XOR** will be TRUE also.  This is often referred to as “exclusive or”.

**XOR** is a new function in Excel 2013 and therefore is not backwards compatible with earlier versions.  In any case, **OR** and **XOR** do not work well with array formulae or functions that behave like arrays (“pseudo-array functions”), such as **SUMPRODUCT**.

At first glance, **SUMPRODUCT(vector1,vector2,…)** appears quite humble.  Consider the following sales report:

![](<Base64-Image-Removed>)

The sales in column **H** are simply the product of columns **F** and **G**, _e.g._ the formula in cell **H12** is simply **\=F12\*G12**.  Then, to calculate the entire amount cell **H23** sums column **H**.  This could all be performed much quicker using the following formula:

> **\=SUMPRODUCT(F12:F21,G12:G21)**

_i.e_. **SUMPRODUCT** does exactly what it says on the tin: it sums the individual products.    

![](<Base64-Image-Removed>)

Where **SUMPRODUCT** comes into its own is when dealing with multiple criteria.  This is done by considering the properties of TRUE and FALSE in Excel, namely:

TRUE\*number = number (_e.g_. TRUE\*7 = 7); _and_

FALSE\*number = 0 (_e.g_. FALSE\*7=0).

Consider the following example:

![](<Base64-Image-Removed>)

we can test columns **F** and **G** to check whether they equal our required values.  **SUMPRODUCT** could be used as follows to sum only sales made by Business Unit 1 for Product Z, _viz._

> **\=SUMPRODUCT((F12:F21=1)\*(G12:G21=”Z”)\*H12:H21)**.

For the purposes of this calculation, **(F12:F21=1)** replaces the contents of cells **F12:F21** with either TRUE or FALSE depending on whether the value contained in each cell equals one \[1\] or not.  The brackets are required to force Excel to compute this first before cross-multiplying.

Similarly, **(G12:G21=”Z”)** replaces the contents of cells **G12:G21** with either TRUE or FALSE depending on whether the value “Z” is contained in each cell. 

Therefore, the only time cells **H12:H21** will be summed is when the corresponding cell in the arrays **F12:F21** and **G12:G21** are both TRUE, then you will get TRUE\*TRUE\*number, which equals the said number.

Notice that **SUMPRODUCT** is not an array formula (_i.e_. you do not use **CTRL + SHIFT + ENTER**), but it is an array function, so again it can use a lot of memory making the calculation speed of the file slow down.

But what if we only need one of these two criteria to be TRUE..?

Let us imagine we run a car sales company with four divisions: North, South, East and West.  Further, we only sell two types of car: the Mercudi and the Lexota:

![](<Base64-Image-Removed>)

Imagine you are the General Manager responsible for the North Division and Mercudi sales.  Each month you have to provide a report summarising the total sales you are responsible for.  This requires analysis of multiple criteria, but it is an **OR**, rather than an **AND**, situation.

We need to include sales of North Division and sales of Mercudi.  However, if we do it this simply sales of Mercudi made by the North Division will be double counted:

![](<Base64-Image-Removed>)

If we specify the criteria in the spreadsheet as follows:

![](<Base64-Image-Removed>)

The formula in this instance would be:

> **\=SUMPRODUCT((F12:F29=G34)\*H12:H29)  
> +SUMPRODUCT((G12:G29=G35)\*H12:H29)  
> \-SUMPRODUCT((F12:F29=G34)\*(G12:G29=G35)\*H12:H29)**

However, there’s a simpler approach…

This is where **SIGN(number)** comes in!  To recall:

*   1 if **number** is positive;
*   0 if **number** is zero; and
*   \-1 if **number** is negative.

It’s only when you start combining this function with **SUMPRODUCT** do you realise how useful it can be.  For example, in our scenario above, consider the following formula:

> **\=SUMPRODUCT(SIGN((F12:F29=G34)+(G12:G29=G35))\*H12:H29)**

Inside the nested **SIGN** function, there are two criteria:

*   Whether the Division is North **(F12:F29=G34)**; and
*   Whether the car sold is the Mercudi **(G12:G29=G35)**.

Each criterion will either be TRUE (1) or FALSE (0), so the possible values inside the **SIGN** function are zero (neither criteria satisfied), one (only one criterion satisfied) or two (both criteria satisfied).  If neither criterion is true, **SIGN** will return a value of zero; if one or more criteria is true, **SIGN** will return a value of one and hence sum the relevant values in column **H**.  This is precisely what is required.

With more criteria considered, the simplicity of **SUMPRODUCT(SIGN)** becomes even more pronounced.

For the sake of brevity here, let’s jump straight to the four criteria scenario:

![](<Base64-Image-Removed>)

In this instance, having been a very successful General Manager, you have acquired greater responsibility: not only do you remain responsible for the North Division and Mercudi sales, but you are now mentor to salesperson Alice and for trying to push credit (finance) sales. 

As before, each month you have to provide a report summarising the total sales you are responsible for, which now considers four criteria: division, car, salesperson and finance:

![](<Base64-Image-Removed>)

If we specify the criteria in the spreadsheet as follows:

![](<Base64-Image-Removed>)

The “long” formula in this instance which would ensure the overlaps are not counted more than once would be:

> **\=SUMPRODUCT((F12:F29=G34)\*J12:J29)  
> +SUMPRODUCT((G12:G29=G35)\*J12:J29)  
> +SUMPRODUCT((H12:H29=G36)\*J12:J29)  
> +SUMPRODUCT((I12:I29=G37)\*J12:J29)  
> \-SUMPRODUCT((F12:F29=G34)\*(G12:G29=G35)\*J12:J29)  
> \-SUMPRODUCT((F12:F29=G34)\*(H12:H29=G36)\*J12:J29)  
> \-SUMPRODUCT((F12:F29=G34)\*(I12:I29=G37)\*J12:J29)  
> \-SUMPRODUCT((G12:G29=G35)\*(H12:H29=G36)\*J12:J29)  
> \-SUMPRODUCT((G12:G29=G35)\*(I12:I29=G37)\*J12:J29)  
> \-SUMPRODUCT((H12:H29=G36)\*(I12:I29=G37)\*J12:J29)  
> +SUMPRODUCT((F12:F29=G34)\*(G12:G29=G35)\*(H12:H29=G36)\*J12:J29)  
> +SUMPRODUCT((F12:F29=G34)\*(G12:G29=G35)\*(I12:I29=G37)\*J12:J29)  
> +SUMPRODUCT((F12:F29=G34)\*(H12:H29=G36)\*(I12:I29=G37)\*J12:J29)  
> +SUMPRODUCT((G12:G29=G35)\*(H12:H29=G36)\*(I12:I29=G37)\*J12:J29)  
> \-SUMPRODUCT((F12:F29=G34)\*(G12:G29=G35)  
> \*(H12:H29=G36)\*(I12:I29=G37)\*J12:J29)**

It’s just so pretty.  PhDs are available for all those of you who can follow this formula in a heartbeat.  Why on earth would you use the **SUMPRODUCT(SIGN)** variant (below) instead? 

> **\=SUMPRODUCT(SIGN((F12:F29=G34)+(G12:G29=G35)  
> +(H12:H29=G36)+(I12:I29=G37))\*J12:J29)**

So yes, **SIGN** is useful in the world of modelling!

_We’ll continue our A to Z of Excel Functions soon.  Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found_ _[here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

*   [Log in](https://sumproduct.com/blog/the-sign-function/#0)
    
*   [Register](https://sumproduct.com/blog/the-sign-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-sign-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-sign-function/#0)

[](https://sumproduct.com/blog/the-sign-function/#0 "close")

top