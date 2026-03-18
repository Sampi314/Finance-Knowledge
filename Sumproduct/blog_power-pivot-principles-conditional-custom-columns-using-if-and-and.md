# Power Pivot Principles: Conditional Custom Columns Using IF, AND, and ‘&&’

**Source:** https://sumproduct.com/blog/power-pivot-principles-conditional-custom-columns-using-if-and-and/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Conditional Custom Columns Using IF, AND, and ‘&&’

*   April 1, 2019

Power Pivot Principles: Conditional Custom Columns Using IF, AND, and ‘&&’
==========================================================================

Power Pivot Principles: Conditional Custom Columns Using IF, AND, and ‘&&’
==========================================================================

2 April 2019

_Welcome back to our Power Pivot blog. Today, we discuss how to create conditional custom columns with multiple criteria._

Today we discuss the different methods to create conditional custom columns in Power Pivot.

Let’s have a look at the following data set:

![](<Base64-Image-Removed>)

We have a table with three categories and a column with customer names. We are going to assume that this table has been retrieved by Power Query (otherwise known as Get & Transform) and loaded into our data model in Power Pivot.

For the purposes of this exercise let’s assume that we wish to create a conditional column that will return with the value “Included” if a customer is “Y” in Category 1 and “N” in Category 2.

We would use the following code to create our custom column:

\=IF(AND(\[Category 1\]=”Y”, \[Category 2\]=”N”),”Included”,BLANK())

As we can see our logic works and we get the desired result:

![](<Base64-Image-Removed>)

What if we want a conditional column with three conditions?

*   Category1 = “Y”
*   Category2 = “Y”
*   Category3 > 1

Keeping in mind that the **AND** function in Power Pivot only allows for two logical statements:

AND(Logical 1, Logical 2)

We will have to use a dreaded nested **IF** formula:

\=IF(AND(\[Category 1\]=”Y”,\[Category 2\] = “Y”),IF(\[Category 3\]>1,”Flag”,BLANK()))

We achieve the intended result:

![](<Base64-Image-Removed>)

That’s all well and good, but what if we have four or five criteria? The nested **IF** functions will just continue to grow and grow: is there an alternative to a nested **IF** formula?

We can use the ‘**&&**‘ operator.

The ‘**&&**‘ operator serves as a substitute to the **AND** function so we can write the following formula:

\=IF(\[Category 1\]=”Y” && \[Category 2\] = “Y” && \[Category 3\]>1,”Flag”,BLANK())

![](<Base64-Image-Removed>)

The ‘**&&**‘ operator allows us to combine several criteria into one logical test for the **IF** formula drastically simplifying the formula. That being said, the ‘**&&**‘ operator is a great way to avoid creating nasty nested **IF** formulae when creating our custom columns in Power Pivot.

That’s it for this week, tune in next week when we cover the **OR** operator. Until then, happy Pivoting!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-conditional-custom-columns-using-if-and-and/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-conditional-custom-columns-using-if-and-and/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-conditional-custom-columns-using-if-and-and/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-conditional-custom-columns-using-if-and-and/#0)

[](https://sumproduct.com/blog/power-pivot-principles-conditional-custom-columns-using-if-and-and/#0 "close")

top