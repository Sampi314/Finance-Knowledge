# The A to Z of DAX Functions – ALL

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-all/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – ALL

*   August 3, 2021

The A to Z of DAX Functions – ALL
=================================

Power Pivot Principles: The A to Z of DAX Functions – ALL
=========================================================

3 August 2021

_In our long-established Power Pivot Principles articles, we are starting a new series on the A to Z of Data Analysis eXpression (DAX) functions. This week this function is **ALL** we can talk about!_

**_The ALL function_**

In Power Pivot, the **ALL** function returns all of the records in a table, or all of the values in a column, ignoring any filters that might have been applied for the file under scrutiny. This function is useful for clearing filters and creating calculations on all rows in a given table.

It is often used in conjunction with the **CALCULATE** function. For example, here, I am going to create a simple ‘**All Months Sales**’ measure:

**\=CALCULATE(\[Sales\],ALL(Sales\[OrderDate (Month)\]))**

![](<Base64-Image-Removed>)

Our resulting PivotTable will look something like this:

![](<Base64-Image-Removed>)

What next? It sort of stands out, doesn’t it? From the **CALCULATE** and **ALL** functions, I can now combine them to create a percentage sales measure which will reflect the inherent seasonality (well, for the last six \[6\] months anyway):

![](<Base64-Image-Removed>)

Remember to include an error trap.

Our PivotTable should look something like this now:

![](<Base64-Image-Removed>)

Not only is this percentage calculated from 2014’s total sales, this measure will always be a percentage. This is subtly different from a normal PivotTable, where percentages may be viewed by changing the Value Field Settings rather than an absolute (dollar) amount. Since this measure is based on a month’s sales divided by all months’ sales, this figure will remain a value between zero \[0\] and one \[1\] no matter how it is formatted or displayed.

_Come back next week for our next post on Power Pivot in the_ _[Blog](https://www.sumproduct.com/blog)
_ _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ _[here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
__._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-all/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-all/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-all/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-all/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-all/#0 "close")

top