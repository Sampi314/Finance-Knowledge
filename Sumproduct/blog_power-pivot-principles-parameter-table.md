# Power Pivot Principles: Parameter Table

**Source:** https://sumproduct.com/blog/power-pivot-principles-parameter-table/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Parameter Table

*   February 24, 2020

Power Pivot Principles: Parameter Table
=======================================

Power Pivot Principles: Parameter Table
=======================================

25 February 2020

_Welcome back to the Power Pivot Principles blog. This week, we are going to learn a way to introduce a parameter table into Power Pivot._

In a previous [blog](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-hasonevalue-function)
, we introduced the DAX function **HASONEVALUE**. This week we are going to use this function as a filter to create a parameter table. The parameter table is useful when we want to add a slicer to a PivotTable and modify the calculation dynamically with different dimensions or DAX expressions.

To use it, we must define a table that has no relationships with any other table (_i.e._ it is a disconnected table). The purpose of this table is to define a list of possible options for altering the calculations performed by one or more existing measures.

Let’s have a look at a simple example. Consider we have the following data table:

![](<Base64-Image-Removed>)

We create a parameter table with different FX rates. This table has no relationships with other tables, and usually has only one column, containing the parameter values. In our case, the table contains the description for **Country** and its corresponding **FX Rate**.

![](<Base64-Image-Removed>)

We add both tables to the Power Pivot data modelling interface and write the following measures. The first measure is the sum of total sales.

![](<Base64-Image-Removed>)

For the second measure, we use **HASONEVALUE** to filter out the FX rate chosen by the end user. To obtain the selected value, we use the **VALUES** function in the measure that uses the parameter. If the selection is not on one specific parameter, the measure returns default value of total sales. It should be noted that if the selection is multiple, which in most cases may be an invalid selection, the measure returns the default value as well.

![](<Base64-Image-Removed>)

Next, we export the measure and create a PivotTable based upon the filter **Customer** and insert a slicer based on the field **Country** in the parameter table.

![](<Base64-Image-Removed>)

The measure filters the value selected and calculates the result accordingly. At this stage, no specific value is selected in parameter table, the value returns from field **ForeignCurrencySales** remains the same as the field **TotalSales**. If we choose one value from the slicer (JPY for example), the result would be:

![](<Base64-Image-Removed>)

The field **ForeignCurrencySales** correctly calculated the value by using the FX rate listed in the parameter table (73.73). Thus, we can make the calculation dynamically with the selection on specific parameter in the slicer.

That’s it for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://sumproduct.com/blog/power-pivot-principles-parameter-table/?id=152)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-parameter-table/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-parameter-table/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-parameter-table/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-parameter-table/#0)

[](https://sumproduct.com/blog/power-pivot-principles-parameter-table/#0 "close")

top