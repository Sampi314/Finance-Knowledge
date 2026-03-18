# Charts and Dashboards: Working Capital Adjustment Chart in Detail – Part 2

**Source:** https://sumproduct.com/blog/charts-and-dashboards-working-capital-adjustment-chart-in-detail-part-2/

---

[Home](https://sumproduct.com/)

\> Charts and Dashboards: Working Capital Adjustment Chart in Detail – Part 2

*   June 8, 2023

Charts and Dashboards: Working Capital Adjustment Chart in Detail – Part 2
==========================================================================

Charts and Dashboards: Working Capital Adjustment Chart in Detail – Part 2
==========================================================================

9 June 2023

_Welcome back to this week’s Charts and Dashboards blog series. This week, we continue to explain how to create a Working Capital Adjustment Chart by looking at how we use the inputs to create the chart data._

When [modelling working capital adjustments](https://www.sumproduct.com/thought/working-capital-adjustments)
, a chart is useful to help us visualise the cash flow figures against existing profit and loss projections. We looked at an overview of this in [Working Capital Adjustment Chart](https://sumproduct.com/blog/charts-and-dashboards-working-capital-adjustment-chart/)
, and we are returning to the topic by popular demand to look in more detail at the data behind the chart.

![](<Base64-Image-Removed>)

We will look at how we can take the following data:

![](<Base64-Image-Removed>)

and create a dynamic chart like this:

![](<Base64-Image-Removed>)

Last time, we looked at how we manage the input data:

![](<Base64-Image-Removed>)

This time, we will look at the preparation of the data that is required in order to create the Working Capital Adjustment chart. Before we move onto the ‘Chart Data’ section, we create a ‘Control Account’, as shown in the next image:

![](<Base64-Image-Removed>)

Before we begin, note that the formatting of the cells in Column **G** in the ‘Control Account’ section has been customised:

![](<Base64-Image-Removed>)

The format code is:

**\_(#,##0\_);\[Red\](#,##0);\_(-\_);**

This means that positive numbers will have no decimal places, negative numbers will be red with no decimal places and brackets and zero \[0\], with be a hyphen. Finally, any text entered will not be shown. The underscores ensure everything lines up to the left.

The opening balance label in cell **D21** has the formula:

**\=”Opening  
“&$G$10&”s”**

This concatenates ‘Opening ‘ and the value in cell **$G$10**, and then an ‘s’ to make it plural. In this example, the label has the value ‘Opening Debtors’.

The next label in cell **D22** has the same value as cell **D14**; ‘Sales in Period’.

The label in cell **D23**, has the formula:

**\=”Cash  
“&IF($G$10=”Creditor”,”Payments”,”Receipts”)**

If the value in cell **$G$10** is ‘Creditor’ then ‘Cash ‘ is concatenated with ‘Payments’, otherwise ‘Cash ‘ is concatenated with ‘Receipts’ as in our example.

The final label in cell **D24** has the formula:

**\=”Closing  
“&$G$10&”s”**

This is similar to the formula in cell **D21**; here we are inserting ‘Closing ‘ and ‘s’ around the value in cell **$G$10** to give the result for our example: ‘Closing Debtors’.

Moving on to the values in column **G**, we start with an opening value of 0 in cell **G21**, since this is a simple example. In practice, this value would come from the opening Balance Sheet (‘Prior BS’).

The movement in sales, ‘Sales in Period’ has the same value as the input cell **G14**. This would come from the Income Statement (‘IS’).

We will come back to the ‘Cash Receipts’ in a moment. The ‘Closing Debtors’ amount in cell **G24** , which would appear on the Balance Sheet (‘Current BS’), is given by:

**\=IF(Days\_in\_Year,$G$12/Days\_in\_Year\*G22)**

**$G$12**/**Days\_in\_Year**\***G22** in our example is the ‘Days Receivable’ (currently 90), divided by the **Days\_In\_Year** (usually 365), multiplied by the ‘Sales in Period’ (1000). In our example, this comes to 247. We add a check that **Days\_in\_Year** is not zero \[0\] before performing this calculation to avoid any **#DIV0!** errors.

The movement in costs, ‘Cash Receipts’ in cell **G23** is then the sum of the opening amount and the sales movement subtracted from the closing amount:

**\=G24-SUM(G21:G22)**

This would be the value on the Cash Flow Statement (‘CFS’).

Next time, we will use the values in ‘Control Account’ to create our ‘Chart Data section.

![](<Base64-Image-Removed>)

That’s it for this week. Check back next week for more Charts and Dashboards tips.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/charts-and-dashboards-working-capital-adjustment-chart-in-detail-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/charts-and-dashboards-working-capital-adjustment-chart-in-detail-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/charts-and-dashboards-working-capital-adjustment-chart-in-detail-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/charts-and-dashboards-working-capital-adjustment-chart-in-detail-part-2/#0)

[](https://sumproduct.com/blog/charts-and-dashboards-working-capital-adjustment-chart-in-detail-part-2/#0 "close")

top