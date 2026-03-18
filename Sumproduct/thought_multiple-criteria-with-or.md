# Multiple Criteria with OR

**Source:** https://sumproduct.com/thought/multiple-criteria-with-or/

---

[Home](https://sumproduct.com/)

\> Multiple Criteria with OR

*   May 14, 2025

Multiple Criteria with OR
=========================

How to sum data based on satsfying at least one of several criteria.

Multiple Criteria with OR: a True SIGN of the Times…
====================================================

In this article, we revisit (yet again!) one of the most queried areas of modelling: how to sum data based upon multiple criteria. The twist this time: what if only one of the various criteria specified has to be true? By Liam Bastick, director with SumProduct Pty Ltd.

Query
-----

I have looked through a previous article on working with Multiple Criteria (see [Dealing with Multiple Criteria](https://www.sumproduct.com/thought/multiple-criteria)
 for further information), but this addresses how to sum data when all criteria specified are true. What if I require at least one criterion to hold instead?

Advice
------

I am seriously thinking of writing a book on dealing with multiple criteria, such is the volume of queries on the subject! This time, I am considering an OR situation, i.e. I don’t need all criteria specified to hold.

Excel has two functions that deal with OR:

1.  **OR(Condition\_1,Condition\_2,…)** checks to see if any of the logical conditions specified are TRUE. As long as at least one condition is TRUE, **OR** will be TRUE also;
2.  **XOR(Condition\_1,Condition\_2,…)** checks to see if each of the logical conditions specified are TRUE. As long as at one and only one condition is TRUE, **XOR** will be TRUE also. This is often referred to as “exclusive or”.

**XOR** is a new function in Excel 2013 and therefore is not backwards compatible with earlier versions. In any case, **OR** and **XOR** do not work well with array formulae or functions that behave like arrays (“pseudo-array functions”), such as **SUMPRODUCT**.

Oh yes, good ol’ **SUMPRODUCT** once more…

### A Recap on SUMPRODUCT

At first glance, **SUMPRODUCT(vector1,vector2,…)** appears quite humble. Consider the following sales report:

![](https://sumproduct.com/wp-content/uploads/2025/05/4d1e83dcc79379e208561c9ce5ed6bc8.jpg)

Example Sales Report

The sales in column **H** are simply the product of columns **F** and **G**, e.g. the formula in cell **H12** is simply **\=F12\*G12**. Then, to calculate the entire amount cell **H23** sums column **H**. This could all be performed much quicker using the following formula:

\=SUMPRODUCT(F12:F21,G12:G21)

i.e. **SUMPRODUCT** does exactly what it says on the tin: it **sums** the individual **products**.

![](https://sumproduct.com/wp-content/uploads/2025/05/456b44838231a884e678acb4973256cf.jpg)

Example Sales Report – SUMPRODUCT Solution

For more on SumProduct, please see [SumProduct Squared..?](https://www.sumproduct.com/thought/sumproduct-squared)

### Dealing with Multiple Criteria where ALL must be TRUE, using SUMPRODUCT

Where **SUMPRODUCT** comes into its own is when dealing with multiple criteria. This is done by considering the properties of TRUE and FALSE in Excel, namely:

*   TRUE\*number = number (e.g. TRUE\*7 = 7); and
*   FALSE\*number = 0 (e.g. FALSE\*7=0).

Consider the following example:

![](<Base64-Image-Removed>)

Example ‘Dummy’ Database

we can test columns **F** and **G** to check whether they equal our required values. **SUMPRODUCT** could be used as follows to sum only sales made by Business Unit 1 for Product Z, viz.

\=SUMPRODUCT((F12:F21=1)\*(G12:G21=”Z”)\*H12:H21).

For the purposes of this calculation, **(F12:F21=1)** replaces the contents of cells **F12:F21** with either TRUE or FALSE depending on whether the value contained in each cell equals 1 or not. The brackets are required to force Excel to compute this first before cross-multiplying.

Similarly, **(G12:G21=”Z”)** replaces the contents of cells G12:G21 with either TRUE or FALSE depending on whether the value **“Z”** is contained in each cell.

Therefore, the only time cells **H12:H21** will be summed is when the corresponding cell in the arrays **F12:F21** and **G12:G21** are both TRUE, then you will get TRUE\*TRUE\*number, which equals the said number.

Notice that **SUMPRODUCT** is not an array formula (i.e. you do not use CTRL+SHIFT+ENTER, please see [Array of Light](https://www.sumproduct.com/thought/array-of-light)
), but it is an array function, so again it can use a lot of memory making the calculation speed of the file slow down.

But what if we only need one of these two criteria to be TRUE..?

### Illustrative Scenario

Let us imagine we run a car sales company with four divisions: North, South, East and West. Further, we only sell two types of car: the Mercudi and the Lexota. The [attached Excel file](https://sumproduct.com/assets/thought-files/e-m/sp-multiple-criteria-with-or.xls)
 can be used to follow this illustration:

![](<Base64-Image-Removed>)

Car Sales – Two Criteria

You are the General Manager responsible for the North Division and Mercudi sales. Each month you have to provide a report summarising the total sales you are responsible for. This requires analysis of multiple criteria, but it is an OR, rather than an AND, situation.

We need to include sales of North Division and sales of Mercudi. However, if we do it this simply sales of Mercudi made by the North Division will be double counted:

![](<Base64-Image-Removed>)

Considering Two Criteria

If we specify the criteria in the spreadsheet as follows:

![](<Base64-Image-Removed>)

Two Criteria Specified

The formula in this instance would be:

\=SUMPRODUCT((F12:F29=G34)\*H12:H29)  
+SUMPRODUCT((G12:G29=G35)\*H12:H29)  
\-SUMPRODUCT((F12:F29=G34)\*(G12:G29=G35)\*H12:H29).

However, there’s a simpler approach…

### Introducing SIGN

Not many know this obscure but useful little Excel function. **SIGN(Number)** is:

*   1 if **Number** is positive;
*   0 if **Number** is zero; and
*   \-1 if **Number** is negative.

It’s only when you start combining this function with **SUMPRODUCT** do you realise how useful it can be. For example, in our scenario above, consider the following formula:

\=SUMPRODUCT(SIGN((F12:F29=G34)+(G12:G29=G35))\*H12:H29).

Inside the nested **SIGN** function, there are two criteria:

*   Whether the Division is North **(F12:F29=G34)**; and
*   Whether the car sold is the Mercudi **(G12:G29=G35)**.

Each criterion will either be TRUE (1) or FALSE (0), so the possible values inside the **SIGN** function are zero (neither criteria satisfied), one (only one criterion satisfied) or two (both criteria satisfied). If neither criteria is true, **SIGN** will return a value of zero; if one or more criteria is true, **SIGN** will return a value of one and hence sum the relevant values in column **H**. This is precisely what is required.

With more criteria considered, the simplicity of **SUMPRODUCT(SIGN)** becomes even more pronounced.

### Extending the Idea

The [attached Excel file](https://sumproduct.com/assets/thought-files/e-m/sp-multiple-criteria-with-or1.xls)
 considers three and four criteria, as well as two. For the sake of brevity here, I will jump straight to the four criteria scenario:

![](<Base64-Image-Removed>)

Car Sales – Four Criteria

In this example, having been a very successful General Manager, you have acquired greater responsibility: not only do you remain responsible for the North Division and Mercudi sales, but you are now mentor to salesperson Alice and for trying to push credit (finance) sales.

As before, each month you have to provide a report summarising the total sales you are responsible for, which now considers four criteria: division, car, salesperson and finance:

![](<Base64-Image-Removed>)

Considering Four Criteria

If we specify the criteria in the spreadsheet as follows:

![](<Base64-Image-Removed>)

Four Criteria Specified

The “long” formula in this instance which would ensure the overlaps are not counted more than once would be:

\=SUMPRODUCT((F12:F29=G34)\*J12:J29)  
+SUMPRODUCT((G12:G29=G35)\*J12:J29)  
+SUMPRODUCT((H12:H29=G36)\*J12:J29)  
+SUMPRODUCT((I12:I29=G37)\*J12:J29)  
\-SUMPRODUCT((F12:F29=G34)\*(G12:G29=G35)\*J12:J29)  
\-SUMPRODUCT((F12:F29=G34)\*(H12:H29=G36)\*J12:J29)  
\-SUMPRODUCT((F12:F29=G34)\*(I12:I29=G37)\*J12:J29)  
\-SUMPRODUCT((G12:G29=G35)\*(H12:H29=G36)\*J12:J29)  
\-SUMPRODUCT((G12:G29=G35)\*(I12:I29=G37)\*J12:J29)  
\-SUMPRODUCT((H12:H29=G36)\*(I12:I29=G37)\*J12:J29)  
+SUMPRODUCT((F12:F29=G34)\*(G12:G29=G35)\*(H12:H29=G36)\*J12:J29)  
+SUMPRODUCT((F12:F29=G34)\*(G12:G29=G35)\*(I12:I29=G37)\*J12:J29)  
+SUMPRODUCT((F12:F29=G34)\*(H12:H29=G36)\*(I12:I29=G37)\*J12:J29)  
+SUMPRODUCT((G12:G29=G35)\*(H12:H29=G36)\*(I12:I29=G37)\*J12:J29)  
\-SUMPRODUCT((F12:F29=G34)\*(G12:G29=G35)  
\*(H12:H29=G36)\*(I12:I29=G37)\*J12:J29).

It’s just so pretty. PhD’s are available for all those of you who can follow this formula in a heartbeat. Why on earth would you use the **SUMPRODUCT(SIGN)** variant (below) instead?

\=SUMPRODUCT(SIGN((F12:F29=G34)+(G12:G29=G35)  
+(H12:H29=G36)+(I12:I29=G37))\*J12:J29).

Erm, maybe because it’s shorter, easier to read, less memory intensive, takes less time to calculate, is less prone to reference errors, has fewer opportunities for logic errors,…

Until next time.

[More Thoughts](https://www.sumproduct.com/thought)

*   [Log in](https://sumproduct.com/thought/multiple-criteria-with-or/#0)
    
*   [Register](https://sumproduct.com/thought/multiple-criteria-with-or/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/multiple-criteria-with-or/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/multiple-criteria-with-or/#0)

[](https://sumproduct.com/thought/multiple-criteria-with-or/#0 "close")

top