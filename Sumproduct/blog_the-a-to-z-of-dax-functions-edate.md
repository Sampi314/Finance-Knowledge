# The A to Z of DAX Functions – EDATE

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-edate/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – EDATE

*   July 18, 2023

The A to Z of DAX Functions – EDATE
===================================

Power Pivot Principles: The A to Z of DAX Functions – EDATE
===========================================================

18 July 2023

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **EDATE**._

**_The_** _**EDATE**_ **_function_**

The **EDATE** function is one of date and time functions and, it returns the date that is the indicated number of months before or after the start date. It employs the following syntax:

**EDATE(start\_date, months)**

It has two \[2\] arguments:

*   **start\_date**: this is required and represents the date in datetime or text format that represents the start date
*   **months**: this is also required and represents an integer to denote the number of months before or after the **start\_date**.

The following should be noted:

*   DAX works with dates in datetime format, so dates stored in other formats are converts implicitly, whereas Microsoft Excel stores said dates as a sequential serial number instead
*   if **start\_date** is not a valid date, the **EDATE** function will return an error
*   if **months** is not an integer, it will be truncated
*   the **EDATE** function utilises the client computer’s locale and date time settings to interpret the text value when the date parameter is a text representation of the date to complete the conversion. The string “1/8/2009” is regarded as a datetime value corresponding to January 8, 2009 if the current date time settings indicate a date in the format of Month/Day/Year. The same text would be regarded as a datetime value corresponding to August 1, 2009 if the current date time settings indicate a date in the format of Day/Month/Year
*   the final day of the relevant month is returned if the desired date falls after that day. For instance, the return date of February 28, 2009 from the following functions: **EDATE**(“2009-01-29”, 1), **EDATE**(“2009-01-30”, 1) and **EDATE**(“2009-01-31”, 1), is one month after the start date
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

Consider the following example:

![](https://sumproduct.com/wp-content/uploads/2025/06/b10132665086135e86ba556bc3b8528d.jpg)

The follow DAX code is used to add 9 months to 17 January 2022 which results in the following table:

![](https://sumproduct.com/wp-content/uploads/2025/06/c28a772f3880d83c7566d2facc7cabb7.jpg)

Besides adding months to the **start\_date** we may subtract months as well:

![](https://sumproduct.com/wp-content/uploads/2025/06/e7c836d2805eb81285fa5f525dced120.jpg)

This will return the following table:

![](https://sumproduct.com/wp-content/uploads/2025/06/fdaea4391473050c4c336fb2c019ddf2.jpg)

Let’s have one example using a DAX measure with the following **Dates** table:

![](https://sumproduct.com/wp-content/uploads/2025/06/35f9645f1fdc01725917e3c94e121f3f.jpg)

Now we can create a measure to add one \[1\] month to the **Start Date** column with the following DAX code:

![](https://sumproduct.com/wp-content/uploads/2025/06/672de0344fdac9de557445fb5095e546.jpg)

Here we receive an error message here since we need to specify an aggregation here to get a single result so, we must modify the DAX code as follows:

![](https://sumproduct.com/wp-content/uploads/2025/06/e0db1ecf7e9055446265083871865878.jpg)

After we put this into the Pivot Table, we will obtain the following visual:

![](<Base64-Image-Removed>)

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-edate/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-edate/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-edate/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-edate/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-edate/#0 "close")

top