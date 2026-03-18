# The A to Z of DAX Functions – DAY

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-day/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – DAY

*   March 21, 2023

The A to Z of DAX Functions – DAY
=================================

Power Pivot Principles: The A to Z of DAX Functions – DAY
=========================================================

21 March 2023

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **DAY**._

**_The_** _**DAY**_ **_function_**

The **DAY** functionis one of the date and time functions. It returns a number from one \[1\] to 31 representing the day of the month. Its syntax is as follows:

**DAY(date)**

It has one \[1\] argument:

*   **date:** this argument is required, and itis a date in date time format or a text representation of a date.

If the argument is a string, it is translated into a datetime value using the same rules applied by the **[DATEVALUE](https://www.sumproduct.com/blog/article/power-pivot-principles/the-a-to-z-of-dax-functions-datevalue)
** function.

Consider the following example, where we will obtain the day from a date column. We have the following data (not displayed in full):

![](<Base64-Image-Removed>)

We can write the following DAX query to add a column to this data containing the day of the month from the column **OrderDate**:

![](<Base64-Image-Removed>)

This DAX query will append a column named “Sales Day” to the end of the table containing the date of the month:

![](<Base64-Image-Removed>)

But wait, there’s more. Consider the following example where we extract the day from a date represented as text. We can write the following DAX query:

![](<Base64-Image-Removed>)

The DAX query above stores the string date of “16/03/2020” into the variable **StringDate**. We can then use the **DAY** function to extract the day from **StringDate**. This will return the following value:

![](<Base64-Image-Removed>)

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-day/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-day/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-day/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-day/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-day/#0 "close")

top