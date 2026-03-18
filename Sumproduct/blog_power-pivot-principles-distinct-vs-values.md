# Power Pivot Principles: DISTINCT vs. VALUES

**Source:** https://sumproduct.com/blog/power-pivot-principles-distinct-vs-values/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: DISTINCT vs. VALUES

*   June 29, 2020

Power Pivot Principles: DISTINCT vs. VALUES
===========================================

Power Pivot Principles: DISTINCT vs. VALUES
===========================================

30 June 2020

_Welcome back to the Power Pivot Principles blog. This week, we will consider the differences between the DISTINCT and VALUES functions in DAX._

We have talked about the **[DISTINCT](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-distinct-function)
** and **[VALUES](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-values-function)
** functions previously. They seem to be very similar. However, there are some differences. Who would bother to create two functions with the same functionality otherwise..?

To recap, both the **DISTINCT** and **VALUES** functions return a one-column table that contains the distinct values from a specified column. Both need to be nested within a formula to get a list of distinct values that may be passed to another function and then counted, summed or used for other aggregated operations.

The **DISTINCT** function has the following syntax:

**DISTINCT(column)**

The **VALUES** function has a similar syntax:

**VALUES(column)**

Let’s continue with an example. There is sales data from 2016 to 2019 for a number of stores, where they track sales by both ‘**Product Key**‘ and ‘**Customer Key**‘:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-191-1.jpg)

We also have a list of products:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-181-1.jpg)

We will load the data to the Power Pivot Data Model, by highlighting the whole data, going to the ‘Power Pivot’ tab on the Ribbon and clicking ‘Add to Data Model’. We rename the tables as ‘**Sales**‘ and ‘**MainProductKey**‘. We also add a [Calendar Table](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-creating-a-calendar-table)
, which will later be used in our PivotTable, and name it ‘**Calendar**‘. We will also define the relationships between them as follows:

![](<Base64-Image-Removed>)

We can count the number of unique customers in two ways:

*   ‘**Unique Customer DISTINCT**‘:

**\=COUNTROWS(DISTINCT(Sales\[Customer Key\]))**

*   ‘**Unique Customer VALUES**‘:

**\=COUNTROWS(VALUES(Sales\[Customer Key\]))**

They show identical results:

![](<Base64-Image-Removed>)

Let’s expand our example by counting the distinct number of key products:

*   ‘**Product Count DISTINCT**‘:

**\=COUNTROWS(DISTINCT(MainProductKey\[Main Product Key\]))**

*   ‘**Product Count VALUES**‘:

**\=COUNTROWS(VALUES(MainProductKey\[Main Product Key\]))**

They no longer display the same result:

![](<Base64-Image-Removed>)

To see it clearly, we load these into PivotTables:

![](<Base64-Image-Removed>)

The **VALUES** function counts blank values, whereas the **DISTINCT** function does not!

That’s it for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-distinct-vs-values/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-distinct-vs-values/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-distinct-vs-values/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-distinct-vs-values/#0)

[](https://sumproduct.com/blog/power-pivot-principles-distinct-vs-values/#0 "close")

top