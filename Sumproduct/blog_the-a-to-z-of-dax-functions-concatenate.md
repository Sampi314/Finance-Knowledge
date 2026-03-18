# The A to Z of DAX Functions – CONCATENATE

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-concatenate/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – CONCATENATE

*   May 31, 2022

The A to Z of DAX Functions – CONCATENATE
=========================================

Power Pivot Principles: The A to Z of DAX Functions – CONCATENATE
=================================================================

31 May 2022

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **CONCATENATE**._

**_The CONCATENATE function_**

This function joins two text strings together to form one text string. The **CONCATENATE** function employs the following syntax to operate:

**CONCATENATE(text1, text2)**

The **CONCATENATE** function has the following arguments:

*   **text1** and **text2****:** these arguments are required, and represent the **text** strings to be joined to form a single text string
*   these strings may include text and / or numbers
*   column (field) references may also be used.

It should be further noted that:

*   the **CONCATENATE** function joins two text strings into one text string. The joined items may be text, numbers or Boolean values represented as text, or a combination of those items. You may also use a column reference if the column contains appropriate values
*   the **CONCATENATE** function in DAX accepts only two arguments, whereas the Excel CONCATENATE function accepts up to 255 arguments. If you need to concatenate multiple columns, you can create a series of calculations or, better, use the concatenation operator (**&**) to join all of them in a simpler expression
*   if you want to use text strings directly, rather than using a column reference, you must enclose each string in double quotation marks
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

Please see my example below:

![](https://sumproduct.com/wp-content/uploads/2025/06/f32e5a15e2cf9c3e4d2d058458ce054d-37.jpg)

_Come back next week for our next post on Power Pivot in the_ _[Blog](https://www.sumproduct.com/blog)
_ _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-concatenate/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-concatenate/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-concatenate/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-concatenate/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-concatenate/#0 "close")

top