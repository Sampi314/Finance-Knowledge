# Power BI Blog: Monthly New Customers

**Source:** https://sumproduct.com/blog/power-bi-blog-monthly-new-customers/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Monthly New Customers

*   June 9, 2021

Power BI Blog: Monthly New Customers
====================================

Power BI Blog: Monthly New Customers
====================================

10 June 2021

_Welcome back to this week’s edition of the Power BI blog series. This week, we will look at how to create a simple measure to count the number of new customers in a database for each month._

We are going to look at a simple database where we have three columns, the **Date** column, the **ID** column and the **Sales** column.

![](<Base64-Image-Removed>)

In this database, we are interested in counting the number of new customers each month. Let’s try to do this in **DAX**.

First, we shall need to count cumulative number unique customers in the dataset. We can do this with the following **DAX** code:

**Cumulative New Customers =**

**CALCULATE(**

    **DISTINCTCOUNT(CustomerID\[ID\]),**

        **ALL(**

            **CalendarTable\[Dates\]**

        **)**

    **)**  

![](<Base64-Image-Removed>)

This will provide the count of the cumulative total of unique customers for each month. Then, we can also calculate the accumulated total of new customers up to and including the previous month, so that we can subtract the two to calculate the new customers for the last period.

We can do this with the following **DAX** code:

**\# Customers Last Month =**

**CALCULATE(**

    **DISTINCTCOUNT(**

        **CustomerID\[ID\]),**

            **DATEADD(**

                **CalendarTable\[Dates\],**

                **-1,**

                **MONTH**

        **)**

    **)**

![](<Base64-Image-Removed>)

Now we can simply subtract the two to obtain the number of new customers each month.

**New Customers = \[Cumulative New Customers\] – \[# Customers Last Month\]**

![](<Base64-Image-Removed>)

That’s it for this week!

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://www.sumproduct.com/courses/)
. If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-monthly-new-customers/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-monthly-new-customers/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-monthly-new-customers/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-monthly-new-customers/#0)

[](https://sumproduct.com/blog/power-bi-blog-monthly-new-customers/#0 "close")

top