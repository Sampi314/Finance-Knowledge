# The A to Z of DAX Functions – CALENDARAUTO

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-calendarauto/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – CALENDARAUTO

*   December 7, 2021

The A to Z of DAX Functions – CALENDARAUTO
==========================================

Power Pivot Principles: The A to Z of DAX Functions – CALENDARAUTO
==================================================================

7 December 2021

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at the **CALENDARAUTO** function._

![](https://sumproduct.com/wp-content/uploads/2025/06/f3540372eded2729d1354298bed3eabe.jpg)

The **CALENDARAUTO** function automatically looks through your model and tries to find and return a table of appropriate dates to use. Similar to the **[CALENDAR](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-az-calendar)
** function, while we can use this function to create a new separate [Calendar table in Power BI](https://www.sumproduct.com/blog/article/power-bi-tips/power-bi-blog-calendar-tables)
, Power Pivot (_i.e._ the Excel version) does not allow you to create a new table the same way that Power BI does. However, the **CALENDARAUTO** DAX function is still available in Power Pivot because it returns a table of values, and that resulting table can be nested in other DAX formulae to create calculations and measures.

Its syntax is as follows:

**CALENDARAUTO(\[FiscalYearEndMonth\])**

It has only one optional argument:

*   **FiscalYearEndMonth:** an integer or DAX expression that returns an integer from one \[1\] to 12. By default, it will use calendar years (or an equivalent value of 12).

It should be noted that:

*   this function ignores all calculated columns or calculated tables. It will return an error if the model does not have any imported datetime values
*   the rules are as follows:
    *   the earliest date in the model which is not in a calculated column or calculated table is taken as the **MinDate**
    *   the latest date in the model which is not in a calculated column or calculated table is taken as the **MaxDate**
    *   the date range returned is dates between the beginning of the fiscal year associated with **MinDate** and the end of the fiscal year associated with **MaxDate**
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

**_Examples_**

Assuming that the MinDate and MaxDate in the data model are 1-Mar-20 and 25-May-21, respectively:

*   the formula below returns all dates between 1-Jan-20 to 31-Dec-21.

**CALENDARAUTO()**

*   the formula below returns all dates between 1-Jul-19 to 30-Jun-21.

**CALENDARAUTO(6)**

_Come back next week for our next post on Power Pivot in the_ _[Blog](https://www.sumproduct.com/blog)
_ _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-calendarauto/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-calendarauto/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-calendarauto/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-calendarauto/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-calendarauto/#0 "close")

top