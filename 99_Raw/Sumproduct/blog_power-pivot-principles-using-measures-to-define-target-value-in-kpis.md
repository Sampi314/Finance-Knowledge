# Power Pivot Principles: Using Measures to Define Target Value in KPIs

**Source:** https://sumproduct.com/blog/power-pivot-principles-using-measures-to-define-target-value-in-kpis/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Using Measures to Define Target Value in KPIs

*   November 16, 2020

Power Pivot Principles: Using Measures to Define Target Value in KPIs
=====================================================================

Power Pivot Principles: Using Measures to Define Target Value in KPIs
=====================================================================

17 November 2020

_Welcome back to the Power Pivot Principles blog. This week, we will talk about using measures to define target values for KPIs._

[Last week](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introduction-to-kpi)
, we introduced the Key Performance Indicator functionality in Power Pivot, which is a quantifiable measurement for gauging business objectives.

In last week’s example, we had the **SalesData** table, with sales by stores and by product types, in the first quarter of FY20 / 21, which has already been loaded into the Power Pivot Data Model:

![](<Base64-Image-Removed>)

Then, we created a KPI by comparing the **Total Sales** of each store with the target sales defined by an absolute value of $30,000:

![](<Base64-Image-Removed>)

To make the KPI more dynamic, we may consider using a measure as the target value. In particular, we want to compare **Total Sales** of each store against the **Average Sales by Store**. First, we need to create the **Average Sales by Store** measure, by dividing the **Total Sales** (using the **[DIVIDE](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-divide-function)
** function) by the number of unique stores (using the **[DISTINCTCOUNT](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-function-distinctcount)
** function):

**\=CALCULATE(DIVIDE(\[Total Sales\],DISTINCTCOUNT(Sales\[Store Key\])),ALL(Sales\[Store Key\]))**

![](<Base64-Image-Removed>)

In the PivotTable, the **Total Sales** is now shown against the **Average Sales by Store**:

![](<Base64-Image-Removed>)

To adjust the KPI, navigate to the Power Pivot tab on the Ribbon, choose **KPIs – > Manage KPIs…**, and then the Key Performance Indicator dialog will appear. Under the ‘Define target value’ section, we select Measure and choose ‘Average Sales by store’ from the dropdown menu. We can also change the status thresholds and icon style to our liking:

![](<Base64-Image-Removed>)

Now, we can see the **Total Sales Status** with icons indicating the sales performance of each store compared to the **Average Sales by store**:

![](<Base64-Image-Removed>)

That’s it for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-using-measures-to-define-target-value-in-kpis/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-using-measures-to-define-target-value-in-kpis/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-using-measures-to-define-target-value-in-kpis/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-using-measures-to-define-target-value-in-kpis/#0)

[](https://sumproduct.com/blog/power-pivot-principles-using-measures-to-define-target-value-in-kpis/#0 "close")

top