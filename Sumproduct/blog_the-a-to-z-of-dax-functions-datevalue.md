# The A to Z of DAX Functions – DATEVALUE

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-datevalue/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – DATEVALUE

*   March 14, 2023

The A to Z of DAX Functions – DATEVALUE
=======================================

Power Pivot Principles: The A to Z of DAX Functions – DATEVALUE
===============================================================

14 March 2023

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **DATEVALUE.**_

**_The_** _**DATEVALUE**_ **_function_**

The **DATEVALUE** functionis one of the date and time functions. It is used to convert a date in the form of text to a date in datetime format. It operates using the following syntax:

**DATEVALUE(date\_text)**

There is only one \[1\] argument for this function:

*   **date\_text**: this argument is required, and is a text string that represents a date.

It should be noted that:

*   the **DATEVALUE** function uses the locale settings of the model to understand the text value specified within **date\_text** when performing its conversion
    *   if the locale settings of the model represent dates in the format of Month/Day/Year, then the string “1/8/2020” will be converted to a datetime value of January 8th, 2020
    *   if the locale settings of the model represent dates in the format of Day/Month/Year, then the string “1/8/2020” will be converted to datetime value of August 1st, 2020.
*   if the year portion of **date\_text** is omitted, the **DATEVALUE** function uses the current year from your computer’s built-in clock and time information in **date\_text** is ignored.

Consider the following example DAX query:

![](https://sumproduct.com/wp-content/uploads/2025/06/f21521a60ac2ecf6d6c60d0bfb0158a2.jpg)

Under our locale settings (DD/MM/YYYY) this code will return as follows:

![](https://sumproduct.com/wp-content/uploads/2025/06/f3371c287981f12dcbf38928aaad3927.jpg)

However, the last two dates may also return the 10th August and the 2nd June respectively. This is dependent upon your machine’s date and time settings.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-datevalue/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-datevalue/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-datevalue/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-datevalue/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-datevalue/#0 "close")

top