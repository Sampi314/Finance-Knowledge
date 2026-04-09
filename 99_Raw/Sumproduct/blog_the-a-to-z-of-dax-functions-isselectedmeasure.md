# The A to Z of DAX Functions – ISSELECTEDMEASURE

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isselectedmeasure/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – ISSELECTEDMEASURE

*   January 20, 2026

The A to Z of DAX Functions – ISSELECTEDMEASURE
===============================================

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (**DAX**) functions.  This week, we look at **ISSELECTEDMEASURE**._

**_The_** _**ISSELECTEDMEASURE**_ **_function_**

![](<Base64-Image-Removed>)

The **ISSELECTEDMEASURE** is a Boolean indicating whether the measure that is currently in context is one of those specified in the list of parameters:

**`ISSELECTEDMEASURE(M1, M2, ...)`**

The **ISSELECTEDMEASURE** is a Boolean indicating whether the measure that is currently in context is one of those specified in the list of parameters:

**ISSELECTEDMEASURE(M1, M2, …)**

There is one \[1\] repeatable argument in this function:

*   **M1, M2, …**: this is a list of measures.

Here are a few remarks about the **ISSELECTEDMEASURE** function:

*   it can only be referenced in the expression for a calculation item
*   it is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

As an example, let’s say we have the following table named **Sales**:

![](<Base64-Image-Removed>)

The **Total Revenue** and **Total Cost** is:

![](<Base64-Image-Removed>)

We can create a new ‘Calculation Item’ called **Increase** by using the following code:

**`IF (       ISSELECTEDMEASURE ( [Total Revenue] ),       SELECTEDMEASURE() * 1.10,       IF (           ISSELECTEDMEASURE ( [Total Cost] ),           SELECTEDMEASURE() * 1.05,           SELECTEDMEASURE()       )`**

![](<Base64-Image-Removed>)

This code lets the revenue increase by 10% and cost increase by 5%.  Therefore, we can generate the following table:

![](<Base64-Image-Removed>)

Total Revenue increased 10% (9,300 up to 10,230), whilst Total Cost rose 5% (from 5,550 to 5,828).

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section.  In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_.  If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isselectedmeasure/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isselectedmeasure/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isselectedmeasure/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isselectedmeasure/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isselectedmeasure/#0 "close")

top