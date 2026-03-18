# Power Pivot Principles: Introducing the DATESBETWEEN Function

**Source:** https://sumproduct.com/blog/power-pivot-principles-introducing-the-datesbetween-function/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Introducing the DATESBETWEEN Function

*   January 6, 2020

Power Pivot Principles: Introducing the DATESBETWEEN Function
=============================================================

Power Pivot Principles: Introducing the DATESBETWEEN Function
=============================================================

7 January 2020

_Welcome back to the Power Pivot Principles blog. This week, we are going to look at the DATESBETWEEN function._

**DATESBETWEEN** is a simple time intelligence function that returns a table that contains a column of dates that begins with the **start\_date** and continues until the **end\_date**. It is especially useful to define a period as a filter in the **CALCULATE** function.

The **DATESBETWEEN** function returns a table containing a single column of date values. It uses the following syntax to operate:

**DATESBETWEEN(<dates>,<start\_date>,<end\_date>)  
**

*   The **<dates>** is a reference to a date/time column
*   The **<start\_date>** is a date expression
*   The **<end\_date>** is a date expression.

Consider the data table shown below (not displayed in full):

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-295.jpg)

This data table contains the sales amount for a specific date with different product types. We also create another calendar table in PowerPivot by using the method introduced [here](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-creating-a-calendar-table)
. The two tables have a relationship like:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-300-1.jpg)

If we want to calculate the sales for a specific product type in a defined period, we create the measure using the **DATESBETWEEN** function.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-284.jpg)

In this case, we define the start date with **DATE** function as 1 July 2016 and the end date as 31 December 2016 and allocate the date parameters to variable **StartingDate** and **EndingDate** respectively. We use **CALCULATE** function to calculate the total sales with filter on the result returned from **DATESBETWEEN** and use the variable **SalesBetweenDate** to assign the value of total sales. We could summarise this in a PivotTable as follows:

![](<Base64-Image-Removed>)

The table above shows the difference between the total sales for the year 2016 and the sales between defined start date and end date for the year 2016. **DATESBETWEEN** provides the flexibility of choosing specific period as the filter for calculation.

Another way of using **DATESBETWEEN** is similar to using the time / date function **DATESYTD**. For example, we could write the measure below to calculate the cumulative sales for each month:

![](<Base64-Image-Removed>)

In this case, we use **DATEADD** to obtain the date one year before and use **LASTDATE** to find the last date in **Calendar\[Date\]**. Hence, we may calculate the sum of the sales by incorporating the **DATESBETWEEN** filter. Then, we create PivotTable based on the date, total sales and cumulative sales. The result would be (not displayed in full):

![](<Base64-Image-Removed>)

The **CumulativeSales** shows the result of rolling total for each month.

That’s it for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-introducing-the-datesbetween-function/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-introducing-the-datesbetween-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-introducing-the-datesbetween-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-introducing-the-datesbetween-function/#0)

[](https://sumproduct.com/blog/power-pivot-principles-introducing-the-datesbetween-function/#0 "close")

top