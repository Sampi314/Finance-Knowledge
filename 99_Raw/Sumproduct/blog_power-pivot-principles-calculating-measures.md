# Power Pivot Principles: Calculating Measures

**Source:** https://sumproduct.com/blog/power-pivot-principles-calculating-measures/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Calculating Measures

*   February 8, 2021

Power Pivot Principles: Calculating Measures
============================================

Power Pivot Principles: Calculating Measures
============================================

9 February 2021

_Welcome back to the Power Pivot Principles blog. This week, we’ll examine an example of how to convert a field to a measure._

If you followed our blog last week, we [summarised a budget](https://www.sumproduct.com/blog/article/power-pivot-principles/power-pivot-principle-summarising-a-budget)
 in Power Pivot. To refresh your memory, here is the summary of that budget, _viz._

![](<Base64-Image-Removed>)

Before we begin, measures in Power Pivot are Data Analysis Expressions (DAX) formulae that are used for advanced calculations, using various aggregations such as **SUM**, **AVERAGE** and **COUNT**, for those of you wondering.

Today, we are going to create two simple measures for sales and cost of goods sold (COGS) in Power Pivot, as an example to illustrate today’s subject. Let’s first look at the Charts of Account sheet and pay special attention to items described as Income and Expenses (Groups P and T in the screenshot) that will be useful in our desired calculations.

![](<Base64-Image-Removed>)

To create a measure, click on Measures on the Power Pivot tab and select ‘New Measure…’

![](<Base64-Image-Removed>)

In the dialog box, select the table name **Budget** and we’ll name our measure ‘**Total Sales**‘.

![](<Base64-Image-Removed>)

The next step is to write the DAX code to calculate ‘**Total Sales**‘ and change the Category to Currency:

**\=CALCULATE(-SUM(Budget\[Amount\]), COA\[Group\] = “P”)**

![](<Base64-Image-Removed>)

Using the same steps as above, we will next create another measure for ‘**Cost of Goods Sold (COGS)**‘:

**\=CALCULATE(-SUM(Budget\[Amount\]), COA\[Group\] = “T”)**

![](<Base64-Image-Removed>)

As we can see now, both the calculated measures appear in the ‘PivotTable Fields’ pane.

![](<Base64-Image-Removed>)

If we place these measures in the PivotTable, we can get the following result:

![](<Base64-Image-Removed>)

That’s it for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-calculating-measures/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-calculating-measures/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-calculating-measures/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-calculating-measures/#0)

[](https://sumproduct.com/blog/power-pivot-principles-calculating-measures/#0 "close")

top