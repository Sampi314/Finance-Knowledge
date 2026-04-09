# The A to Z of DAX Functions – EXACT

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-exact/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – EXACT

*   September 26, 2023

The A to Z of DAX Functions – EXACT
===================================

Power Pivot Principles: The A to Z of DAX Functions – EXACT
===========================================================

26 September 2023

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **EXACT**._

**_The_** _**EXACT**_ **_function_**

![](https://sumproduct.com/wp-content/uploads/2025/06/8cc47e13a94d5709663cd87565e5010b.jpg)

The **EXACT** functionis one of the text functions where it compares two text strings and returns TRUE if they are _exactly_ the same, otherwise returns FALSE. The **EXACT** function is case-sensitive, but it ignores any formatting differences. It employs the following syntax:

**EXACT(text1, text2)**

It has two \[2\] arguments:

*   **text1:** this is required and, this represents the first text string or column that contains text
*   **text2:** this is required and, this represents the second text string or column that contains text.

Let’s consider the following example here where we have the following **Random\_Number** table:

![](https://sumproduct.com/wp-content/uploads/2025/06/dab99dda54f36157bb8e74635b54b97d.jpg)

Let’s ignore the ‘**Row no.**’ field for now as we will use it later in the PivotTable to view all entries here. We have two \[2\] columns, **A** and **B** here. The number three \[3\] on the first \[1st\] row is a number whilst the number three \[3\] on the second \[2nd\] row is text. We will write an **EXACT** function here to generate the Boolean list where the exact match occurs:

![](https://sumproduct.com/wp-content/uploads/2025/06/9629a9dd3776cf8b98d3d68d991420e0.jpg)

We have to use the **MAX** function here to aggregate columns **A** and **B** so that the **EXACT** function reads properly. Then, we will put the new measure in the Values field in the PivotTable and the ‘**Row no.**’ column in the Rows field of the PivotTable:

![](https://sumproduct.com/wp-content/uploads/2025/06/f481669265156e3a55e3f43c54f90bfb.jpg)

Since the **EXACT** function is case sensitive, the third and sixth rows result in FALSE values whilst the rest of the table has TRUE values.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-exact/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-exact/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-exact/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-exact/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-exact/#0 "close")

top