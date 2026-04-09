# The A to Z of DAX Functions – CUSTOMDATA

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-customdata/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – CUSTOMDATA

*   January 3, 2023

The A to Z of DAX Functions – CUSTOMDATA
========================================

Power Pivot Principles: The A to Z of DAX Functions – CUSTOMDATA
================================================================

3 January 2023

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at_ **_CUSTOMDATA_**_._

**_The CUSTOMDATA function_**

The **CUSTOMDATA** function is one of the information functions. Similar to last week’s **[CURRENTGROUP](https://www.sumproduct.com/blog/article/power-pivot-principles/the-a-to-z-of-dax-functions-currentgroup)
**function, this function does not have parameters in its syntax:

**CUSTOMDATA()**

The **CUSTOMDATA** function returns the content of the **CUSTOMDATA** property in the connection string. This function will return a blank value, if the **CUSTOMDATA** property was not defined at the time of connection. For example:

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

It should be further noted that:

*   the **CUSTOMDATA** is a volatile function
*   this function is mainly useful in custom security systems where the caller uses the **CUSTOMDATA** function to communicate security parameters to the AS DAX system
*   when an application employs custom authentication, this function is often used in the implementation of expressions for role-based security
*   there is no support for this function in calculated tables or columns
*   using the **CUSTOMDATA** function in DAX expressions of the model, including RLS filters and measures, has been found to cause performance problems if the connection string does not include the **CustomData** argument. In this case, the performance problem may be fixed by simply supplying a value to the **CustomData** in the connection string
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-customdata/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-customdata/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-customdata/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-customdata/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-customdata/#0 "close")

top