# The A to Z of DAX Functions – ISATLEVEL

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isatlevel/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – ISATLEVEL

*   August 26, 2025

The A to Z of DAX Functions – ISATLEVEL
=======================================

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (**DAX**) functions.  This week, we look at **ISATLEVEL**._

**_The_** _**ISATLEVEL**_ **_function_**

![](<Base64-Image-Removed>)

The **ISATLEVEL** function is one of visual calculation function that reports whether the column is present at the current level.

> **ISATLEVEL(column)**

There is just the one \[1\] main argument in this function:

*   **column**: this is a grouping column in the date grid.

Here are a few remarks about this function:

*   this function can be used only in visual calculations
*   this function is “specialised” for visual calculations, hence it is guaranteed to be compatible with functions that navigate the levels of a hierarchy in the data matrix, such as **EXPAND** and **COLLAPSE**
*   a hierarchy level can contain more than one \[1\] column.  For example, in a \[Year\], \[Quarter\], \[Month\] hierarchy, the level that contains the \[Quarter\] column also includes the \[Year\] column at the same level.

Imagine a Data hierarchy with Levels **Total** **\->** **Year** **\->** **Quarters** **\->** **Month**.  We will attach this hierarchy on any visual (For this example we will use Matrix Visual).  Then on the ribbon **Home** **\->** **New** **visual** **calculation**.  Inside any calculation we write these codes:

> **IsYearLevel = ISATLEVEL(\[Fiscal Year\])**
> 
> **IsQuarterLevel = ISATLEVEL(\[Fiscal Quarter\])**
> 
> **IsMonthLevel = ISATLEVEL(\[Month\])**
> 
> **IsQuarterLevelAfterExpand = EXPAND(ISATLEVEL(\[Fiscal Quarter\]), ROWS)**
> 
> **IsQuarterLevelAfterCollapse = COLLAPSE(ISATLEVEL(\[Fiscal Quarter\]), ROWS)**

![](<Base64-Image-Removed>)

At render time, the visual calculation evaluates which level is “active” for that cell using **ISATLEVEL**.  With the Boolean value, we can write suitable measure for the level to return the value we want it to.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section.  In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_.  If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isatlevel/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isatlevel/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isatlevel/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isatlevel/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isatlevel/#0 "close")

top