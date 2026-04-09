# The A to Z of DAX Functions – ALLCROSSFILTERED

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-allcrossfiltered/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – ALLCROSSFILTERED

*   March 1, 2022

The A to Z of DAX Functions – ALLCROSSFILTERED
==============================================

Power Pivot Principles: The A to Z of DAX Functions – ALLCROSSFILTERED
======================================================================

1 March 2022

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **ALLCROSSFILTERED**._

**_The ALLCROSSFILTERED function_**

The **ALLCROSSFILTERED** function clears all filters which are applied to a table. It has the following syntax:

**\=ALLCROSSFILTERED(table)**

The argument is defined as follows:

*   **table**: this is required and represents the **table** you wish to clear the filters on.

It should be noted that:

*   **ALLCROSSFILTERED** may only be used to clear filters but not return a table
*   **ALLCROSSFILTERED** can be used only as a **CALCULATE** modifier and cannot be used as a table function
*   **ALLCROSSFILTERED** removes all the filters on an expanded table (like **ALL**) and on columns and tables that are cross-filtering the table argument because of bidirectional cross-filters set on relationships directly or indirectly connected to the expanded table
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

Please see my example below:

Consider the Table **Sales**:

![](<Base64-Image-Removed>)

and another Table **Categories**:

![](<Base64-Image-Removed>)

They are linked as follows:

![](<Base64-Image-Removed>)

Do ensure (by double-clicking on the link) that the ‘Cross filter direction’ is set to ‘Both’, _viz._

![](<Base64-Image-Removed>)

I now create three \[3\] measures as follows:

1.  **Total Sales = SUM(Sales\[Amount\])**
2.  **ALL Categories Sales = CALCULATE(\[Total Sales\], ALL(Categories))**
3.  **ALLCROSSFILTERED Categories Sales = CALCULATE(\[Total Sales\], ALLCROSSFILTERED(Categories))**

This results in the following output matrix in Power BI (**ALLCROSSFILTERED** only works in Power BI, not Power Pivot in Excel presently):

![](<Base64-Image-Removed>)

In more complicated models, **ALLCROSSFILTERED** will have further propagated effects. Consider the following arrangement:

![](<Base64-Image-Removed>)

Here, using **ALLCROSSFILTERED** on the **Product** table will remove the (cross) filters to both the **Sales** and **Imagery** tables too.

_Come back next week for our next post on Power Pivot in the_ _[Blog](https://www.sumproduct.com/blog)
_ _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-allcrossfiltered/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-allcrossfiltered/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-allcrossfiltered/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-allcrossfiltered/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-allcrossfiltered/#0 "close")

top