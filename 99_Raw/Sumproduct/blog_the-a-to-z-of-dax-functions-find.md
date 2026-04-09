# The A to Z of DAX Functions – FIND

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-find/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – FIND

*   November 21, 2023

The A to Z of DAX Functions – FIND
==================================

Power Pivot Principles: The A to Z of DAX Functions – FIND
==========================================================

21 November 2023

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **FIND**._

**_The_** _**FIND**_ **_function_**

![](<Base64-Image-Removed>)

The **FIND** functionis one of the text functions which the starting position of one text string within another text string. **FIND** is case-sensitive and accent-sensitive. It has the following syntax:

**FIND(find\_text, within\_text \[,  \
\[start\_num\]\[, NotFoundValue\]\])**

*   **find\_text**: this is required and this is the text we want to find
*   **within\_text**: this is required and this is the text that containing the text we want to find
*   **start\_num**: this argument is optional which is the character at which we want to start the search. If the is omitted the default value of one \[1\] will be assigned to it. Thus, it will search from the first character onwards
*   **NotFoundValue**: this argument is optional but it is strongly recommended by Microsoft. This is the numeric value or **BLANK**() to be return if the text is not found. If omitted, it will return an error.

Further, it should be noted:

*   whereas Microsoft Excel has multiple versions of the **FIND f**unction to accommodate single-byte character set (SBCS) and double-byte character set (DBCS) languages, **DAX** uses Unicode and counts each character the same way; therefore, you do not need to use a different version depending upon the character type
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules
*   the **FIND** function is case sensitive
*   it doesn’t support wildcards.

Let’s consider the following examples for the use of **FIND** function in Calculated Columns in Power Pivot. We have the following **Product** table in the Data Model:

![](<Base64-Image-Removed>)

Now, we want to extract the position of the hyphen and those doesn’t have the hyphen we will put a **BLANK**(). Thus, we will add a column to the right of the **ProductName** column and name it is ‘**Position of Hyphen**’ and enter the following **DAX** formula for that column:

![](<Base64-Image-Removed>)

After pressing **ENTER**, we will get the following result:

![](<Base64-Image-Removed>)

The strange thing about this **DAX** function is that the last argument, which is **NotFoundValue**, although apparently optional, can generate errors if omitted. For example, if we search for the hyphen (“**–**”), it will return errors for the whole calculated column if some of the data does not contain said character, _e.g._

**\=FIND(“-“,’Product'\[ProductName\])**

![](<Base64-Image-Removed>)

Hence, make sure you enter the data for **NotFoundValue** arguments when you write the **DAX** formula.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-find/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-find/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-find/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-find/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-find/#0 "close")

top