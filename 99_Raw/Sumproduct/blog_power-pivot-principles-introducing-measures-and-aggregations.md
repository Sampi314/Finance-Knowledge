# Power Pivot Principles: Introducing Measures and Aggregations

**Source:** https://sumproduct.com/blog/power-pivot-principles-introducing-measures-and-aggregations/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Introducing Measures and Aggregations

*   April 16, 2018

Power Pivot Principles: Introducing Measures and Aggregations
=============================================================

Power Pivot Principles: Introducing Measures and Aggregations
=============================================================

17 April 2018

_Welcome back to our Power Pivot blog series. Today we talk about measures._

A **measure** is a calculation that can be created to be used in PivotTable analysis. When measures are created, they sit in the values area of the PivotTable ready to be used in a PivotTable. Unlike creating formulae in Excel, a measure in Power Pivot is saved and can be used time and time again.

**_Example_**

Let’s create a simple measure. Select the ‘Power Pivot’ tab on the Ribbon and then choose the ‘Measures’ option.

![](<Base64-Image-Removed>)

Enter the following inputs into the resulting dialog box:

![](<Base64-Image-Removed>)

If we click on ‘Check formula’ Power Pivot will return with this warning message:

![](<Base64-Image-Removed>)

This is because we need to include an aggregation function such as **SUM**, **MAX**, **MIN**, **AVERAGE** or **COUNT**. A quick fix would be to include the ‘**SUM**‘ aggregation in front of the fields, which will make Power Pivot happy:

![](<Base64-Image-Removed>)

Profit will then appear as the sole field in the ‘Values’ section of the PivotTable.

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

Do you see how the value is simply ‘Profit’ and not ‘Sum of Profit’ which is an annoying irritation in PivotTables? This is another benefit of creating a measure. We can now bring in other fields to complete our PivotTable – but more on that next time!

That’s it for this week. Stay tuned to our blog page for more on Power Pivot. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-introducing-measures-and-aggregations/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-introducing-measures-and-aggregations/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-introducing-measures-and-aggregations/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-introducing-measures-and-aggregations/#0)

[](https://sumproduct.com/blog/power-pivot-principles-introducing-measures-and-aggregations/#0 "close")

top