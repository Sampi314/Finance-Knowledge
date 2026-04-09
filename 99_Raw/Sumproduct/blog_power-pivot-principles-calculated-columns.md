# Power Pivot Principles: Calculated Columns

**Source:** https://sumproduct.com/blog/power-pivot-principles-calculated-columns/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Calculated Columns

*   April 9, 2018

Power Pivot Principles: Calculated Columns
==========================================

Power Pivot Principles: Calculated Columns
==========================================

10 April 2018

_Welcome back to our Power Pivot blog. Today, we consider how to create a calculated column._

A **calculated column** is a simple formulaic calculation applied to an entire column that remains in the table you created it in. It can be later used by measures and other calculated columns to create more complex expressions.

**_Example_**

Let’s go through an example to walk through how to add a calculated column into the Power Pivot model.

![](https://sumproduct.com/wp-content/uploads/2025/05/3c21e34ad071f72dd0ba77322575d4ff.jpg)

Let’s say we want to add a column into the model which will calculate ‘Gross Profit’. Next to the last column of data in your Power Pivot model will be a blank column with the title ‘Add Column’.

![](https://sumproduct.com/wp-content/uploads/2025/05/ccbe51aa9f63ef7172b0875b77afc186.jpg)

Double click on the heading and type ‘Gross Profit’, note, ensure all columns in your Power Pivot data model have a unique name. In the formula bar, you can type out the formula shown below or by selecting the columns of data you wish to use in the formula:

**\=\[SalesAmount\]-\[TotalProductCost\]**

![](https://sumproduct.com/wp-content/uploads/2025/05/1a0411838af6ac7a3b5017d17d03f459.jpg)

The new calculated column will appear in the data model as follows:

![](https://sumproduct.com/wp-content/uploads/2025/05/c6bb7b8bbcca7620a5829002f9646ad8.jpg)

As this new calculated column contains a formula, it will be computed for each row in the data set. When the underlying data is refreshed the columns are recalculated each time.

This column may now be used in another calculated column, measure, chart, and even PivotTable like any other column in your data model.

Another useful calculated column to have might be a year column. To create this, add a new column, rename it ‘Year’ and use the **YEAR** function:

\=**YEAR(Sales\[OrderDate\])** 

![](<Base64-Image-Removed>)

That’s it for this week. Stay tuned to our blog page for more on Power Pivot. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-calculated-columns/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-calculated-columns/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-calculated-columns/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-calculated-columns/#0)

[](https://sumproduct.com/blog/power-pivot-principles-calculated-columns/#0 "close")

top