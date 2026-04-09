# Monday Morning Mulling: May 2022 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-may-2022-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: May 2022 Challenge

*   May 29, 2022

Monday Morning Mulling: May 2022 Challenge
==========================================

Monday Morning Mulling: May 2022 Challenge
==========================================

30 May 2022

_On the final Friday of each month, we set an Excel / Power Pivot / Power Query / Power BI problem for you to puzzle over for the weekend. On the Monday, we publish a solution. If you think there is an alternative answer, feel free to email us. We’ll feel free to ignore you._

The challenge this month was to create a PivotTable that showed the sales amount made by each salesperson in their individual business units, as well as a percentage breakdown for each business unit and the percentage contribution of each business unit to total sales. Easy, yes?

**_The Challenge_**

In this challenge, we required you to create a PivotTable that showed the amount of sales made by each salesperson in their individual business units, as well as a percentage breakdown for each business unit and the percentage contribution of each business unit to total sales.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-24-1.jpg)

You can download the question file [here](https://sumproduct.com/assets/blog-pictures/2022/fff-mmm/may/sp-creating-subtotals-in-power-pivot---challenge.xlsx)
.

As always, there were a few requirements:

*   this problem should be solved entirely in Power Pivot and with the help of measures
*   filtering should not modify the proportion contribution of each business unit to total sales.

**_Suggested Solution_**

You can find our Excel file [here](https://sumproduct.com/assets/blog-pictures/2022/fff-mmm/may/sp-creating-subtotals-in-power-pivot---suggested-solution.xlsx)
 which demonstrates our suggested solution. However, before explaining our solution, we will clarify the common idea how we came up with it first.

**For Excel Office 365, Excel on the Web, and Office Beta / Insider versions**

These Excel versions allow us to use DAX functions in Power Pivot which help shorten a lot of steps.

Firstly, we must begin by adding the data table to the Data Model in Power Pivot, so that we may manipulate it with DAX.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-31-1.jpg)

Secondly, create a new measure in Power Pivot for total sales using formula:

**\=SUM(Data(Amount))**

![](<Base64-Image-Removed>)

**Note:** Before moving on to the next step, I wish to point out that we may make a PivotTable like this by just changing the value field setting of the sales measure we defined above to ‘% of Parent Row Total’. This approach will breach our second condition since, in this circumstance, if you filter by business unit, the percentage breakdown will vary.

![](<Base64-Image-Removed>)

Thirdly, create a measure (**Sales Grand Total**) in Power Pivot for sales grand total using **[CALCULATE](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-az-calculate)
** and **[ALLEXCEPT](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-az-allexcept)
** DAX functions. We are using **ALLEXCEPT** to remove all filters from grand total apart from the **Data\[Amount\]** column:

**\=CALCULATE(\[Sales\], ALLEXCEPT(Data, Data\[Amount\]))**

![](<Base64-Image-Removed>)

The next step would be to create a measure in Power Pivot for **Sales as % of Grand Total** by **DIVIDE** DAX function:

**\=DIVIDE(\[Sales\], \[Sales Grand Total\])**

![](<Base64-Image-Removed>)

Then, we have to create a measure in Power Pivot for Business Unit Subtotal using **[CALCULATE](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-az-calculate)
** and **[ALL](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-az-all)
** DAX function:

**\=CALCULATE(\[Sales\], ALL(Data\[Sales Person\]))**

![](<Base64-Image-Removed>)

The next step would be to create a measure in Power Pivot for Sales as % of BU subtotal using:

**\=DIVIDE(\[Sales\], \[BU Subtotal\])**

![](<Base64-Image-Removed>)

Moving on, we must create a measure in Power Pivot for ‘**Pct Breakdown**‘ using **IF** and the **ISFILTERED** DAX functions:

**\=IF(ISFILTERED(Data\[Sales Person\]), \[Sales as Pct of BU Subtotal\], \[Sales as Pct of Grand Total\])**

![](<Base64-Image-Removed>)

Finally, in the Insert section, we can insert a PivotTable from the Data Model. The PivotTable may then be added using ‘Business Unit’ and ‘Sales Person’ as row fields, and Sales and Pct Breakdown as value fields, _viz._

![](<Base64-Image-Removed>)

This will produce the result required:

![](<Base64-Image-Removed>)

_The Final Friday Fix will return on Friday 24 June 2022 with a new Excel Challenge. In the meantime, please look out for the Daily Excel Tip on our home page and watch out for a new blog every business working day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-may-2022-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-may-2022-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-may-2022-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-may-2022-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-may-2022-challenge/#0 "close")

top