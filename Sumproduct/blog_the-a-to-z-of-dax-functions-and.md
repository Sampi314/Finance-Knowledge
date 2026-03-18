# The A to Z of DAX Functions – AND

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-and/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – AND

*   August 31, 2021

The A to Z of DAX Functions – AND
=================================

Power Pivot Principles: The A to Z of DAX Functions – AND
=========================================================

31 August 2021

_In our long-established Power Pivot Principles articles, we are starting a new series on the A to Z of Data Analysis eXpression (DAX) functions. You have to ‘**AND** it to us – we are keeping this series going…_

**_The AND function_**

The **AND** function checks whether both its arguments are TRUE, and returns TRUE if and only if both are TRUE; otherwise, it returns FALSE. The syntax is simple:

**AND****(logical\_1, logical\_2)**

where **logical\_1** and **logical\_2** are the logical values you wish to test.

The **AND** function in DAX accepts only two \[2\] arguments. If you need to perform an **AND** operation on multiple expressions, you can create a series of calculations or, better, use the **AND** operator (**&&**) to join all of them in a simpler expression.

Let’s consider an example where we’ll create conditional custom columns in Power Pivot. Here, we have the following dataset:

![](https://sumproduct.com/wp-content/uploads/2025/06/e774d10cbbb9450fc45efbe51abdf434-3.jpg)

We have a table with three categories and a column with customer names. We are going to assume that this table has been retrieved by Power Query (otherwise known as Get & Transform) and loaded into our data model in Power Pivot.

For the purposes of this exercise, let’s assume that we wish to create a conditional column that will return with the value “Included” if a customer is “Y” in Category 1 and “N” in Category 2.

We would use the following code to create our custom column:

**\=IF(AND(\[Category 1\]=”Y”, \[Category 2\]=”N”),”Included”,BLANK())**

As we can see our logic works and we get the desired result:

![](https://sumproduct.com/wp-content/uploads/2025/06/f32e5a15e2cf9c3e4d2d058458ce054d-13.jpg)

What if we want a conditional column with three conditions?

*   **Category1** = “Y”
*   **Category2** = “Y”
*   **Category3** > 1.

Keeping in mind that the **AND** function in Power Pivot only allows for two logical statements, we will have to use a nested **IF** formula:

**\=IF(AND(\[Category 1\]=”Y”,\[Category 2\] = “Y”),IF(\[Category 3\]>1,”Flag”,BLANK()))**

Then we achieve the intended result:

![](<Base64-Image-Removed>)

That’s all well and good, but what if we have four or five criteria? The nested **IF** functions will just continue to grow and grow: is there an alternative to a nested **IF** formula?

As stated above, we may use the ‘**&&**’ operator. The ‘**&&**’ operator serves as a more versatile substitute for the **AND** function so we can write the following formula:

**\=IF(\[Category 1\]=”Y” && \[Category 2\] = “Y” && \[Category 3\]>1,”Flag”,BLANK())**

![](<Base64-Image-Removed>)

The ‘**&&**’ operator allows us to combine several criteria into one logical test for the **IF** formula, simplifying the formula.

_Come back next week for our next post on Power Pivot in the_ _[Blog](https://www.sumproduct.com/blog)
_ _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ _[here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
__._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-and/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-and/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-and/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-and/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-and/#0 "close")

top