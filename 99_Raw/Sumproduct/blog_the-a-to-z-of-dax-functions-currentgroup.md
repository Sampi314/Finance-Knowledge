# The A to Z of DAX Functions – CURRENTGROUP

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-currentgroup/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – CURRENTGROUP

*   December 27, 2022

The A to Z of DAX Functions – CURRENTGROUP
==========================================

Power Pivot Principles: The A to Z of DAX Functions – CURRENTGROUP
==================================================================

27 December 2022

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at_ **_CURRENTGROUP_**_._

**_The CURRENTGROUP function_**

The **CURRENTGROUP** function is one of the table manipulation functions. It returns a set of rows from the **table** argument of a **GROUPBY** expressionthat belong to the current row of the **GROUPBY** result. Besides that, the **CURRENTGROUP** function takes no arguments:

**CURRENTGROUP()**

It should be noted that:

*   This function can only be used in conjunction with a **GROUPBY** expression
*   The **GROUPBY** function is like the **SUMMARIZE** function, but the **GROUPBY** function will not perform an implicit [**CALCULATE**](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-az-calculate)
     for any extension columns it adds. Moreover, it also permits the **CURRENTGROUP** function to be used inside aggregation functions in the extension columns that it adds
*   The only place the **CURRENTGROUP** function is supported is as the first parameter to one of the aggregation functions: [**AVERAGEX**](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-az-averagex)
    ,[**COUNTAX**](https://www.sumproduct.com/blog/article/power-pivot-principles/the-a-to-z-of-dax-functions-countax)
    ,**[COUNTX](https://www.sumproduct.com/blog/article/power-pivot-principles/the-a-to-z-of-dax-functions-countx)
    **, **GEOMEANX**, **MAXX**, **MINX**, **PRODUCTX**, **STDEVX.S**, **STDEVX.P**, **SUMX**, **VARX.S**, **VARX.P**.

As an example, consider the following data table:

![](<Base64-Image-Removed>)

You can use the following DAX query to return the number of customers in each country:

**EVALUATE**

    **GROUPBY  
(**

        **Customers,**

        **Customer\[Country\],**

        **“# Customers”,**

        **COUNTX (** **CURRENTGROUP ()****, 1 )**

        **)**

The result is as follows:

![](<Base64-Image-Removed>)

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-currentgroup/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-currentgroup/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-currentgroup/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-currentgroup/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-currentgroup/#0 "close")

top