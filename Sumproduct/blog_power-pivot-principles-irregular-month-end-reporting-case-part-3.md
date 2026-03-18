# Power Pivot Principles: Irregular Month-End Reporting Case – Part 3

**Source:** https://sumproduct.com/blog/power-pivot-principles-irregular-month-end-reporting-case-part-3/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Irregular Month-End Reporting Case – Part 3

*   August 31, 2020

Power Pivot Principles: Irregular Month-End Reporting Case – Part 3
===================================================================

Power Pivot Principles: Irregular Month-End Reporting Case – Part 3
===================================================================

1 September 2020

_Welcome back to the Power Pivot Principles blog. This week, we continue with our irregular month-end reporting case study._

To recap, we have a sales data set of four product lines in a supermarket over four years. This supermarket has a rule for month-end reporting, which is the reporting end of month day is the final Thursday of a month, regardless of whether it matches the end of the calendar month.

![](<Base64-Image-Removed>)

By using the **EOMONTH** and the **WEEKDAY** functions to [compare the logic](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-irregular-month-end-reporting-case-part-1)
 or by using [‘Fill Up’ calculations](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-irregular-month-end-reporting-case-part-2)
, we worked out the final Thursday of each month to be the ‘**Reporting End of Month**‘:

![](<Base64-Image-Removed>)

Now, we want to get some insights about the sales of each month. First, in the **Sales** table, we create a calculated column ‘**Total Sales**‘:

**\=Sales\[Toilet Rolls\] + Sales\[Face Masks\] + Sales\[Hand Sanitiser\] + Sales\[Canned Food\]**

![](<Base64-Image-Removed>)

Then, we create a **[Calendar Table](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-calendar-table)
**, by going to the Design tab on the Ribbon of the Power Pivot window, choose Date Table à New. After the **Calendar Table** is created, we navigate to the Diagram view to form a relationship between the two tables, by connecting the **Dates** columns:

![](<Base64-Image-Removed>)

Since we have an irregular reporting rule, in the **Calendar Table**, we will create four more columns to specify this rule. We will use the **[LOOKUPVALUE](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-function-lookupvalue)
** function to get the ‘**Reporting End of Month**‘ in the **Calendar Table**, and then get the related ‘**Reporting Month**‘, ‘**Reporting Year**‘, ‘**Reporting Month Number**‘ which we will use later in our PivotTable:

**Reporting End of Month =** **LOOKUPVALUE(Sales\[Reporting End of Month\],Sales\[Date\],’Calendar'\[Date\])**

**Reporting Month = FORMAT(\[Reporting End of Month\],”MMMM”)**

**Reporting Year = YEAR(\[Reporting End of Month\])**

**Reporting Month Number = MONTH(\[Reporting End of Month\])**

![](<Base64-Image-Removed>)

Next, we need to sort the ‘**Reporting Month**‘ by the ‘**Reporting Month Number**‘, otherwise, it will be sorted alphabetically in our PivotTable _i.e._ April goes first instead of January. We highlight the ‘**Reporting Month**‘ column, go to **Home -> Sort by Column -> Sort by Column…** and choose ‘**Reporting Month Number**‘ in the ‘By Column’ box:

![](<Base64-Image-Removed>)

We are now prepared! Now, we will create another measure ‘**Current Month Sales’**:

**\=CALCULATE(SUM(Sales\[Total Sales\]), ‘Calendar'\[Reporting End of Month\])**

![](<Base64-Image-Removed>)

We will create a PivotTable by dragging the ‘**Reporting Year**‘, ‘**Reporting Month**‘, ‘**Reporting End of Month**‘ fields (from the **Calendar Table -> More Fields**) to Rows and ‘**Current Month Sales**‘ (from the **Sales** table) to Values. We can see the sales by month ending on the final Thursday of the month, _viz._

![](<Base64-Image-Removed>)

That’s it for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-irregular-month-end-reporting-case-part-3/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-irregular-month-end-reporting-case-part-3/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-irregular-month-end-reporting-case-part-3/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-irregular-month-end-reporting-case-part-3/#0)

[](https://sumproduct.com/blog/power-pivot-principles-irregular-month-end-reporting-case-part-3/#0 "close")

top