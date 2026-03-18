# Power Pivot Principles: Slicers for Columns – Part 2

**Source:** https://sumproduct.com/blog/power-pivot-principles-slicers-for-columns-part-2/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Slicers for Columns – Part 2

*   January 18, 2021

Power Pivot Principles: Slicers for Columns – Part 2
====================================================

Power Pivot Principles: Slicers for Columns – Part 2
====================================================

19 January 2021

_Welcome back to the Power Pivot Principles blog. This week, we will continue to talk about slicers for columns._

[Last week](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-slicers-for-columns-part-1)
, using Power Query, we combined and transformed the **Actual** revenue table

![](<Base64-Image-Removed>)

and the **Budget** revenue table

![](<Base64-Image-Removed>)

to one **Data** table like the one below:

![](<Base64-Image-Removed>)

We load this table to Excel, from the ‘Queries & Connections’ panel, right-click on the **Data** table and select ‘Load To…’. An ‘Import Data’ dialog will appear. In here, we will tick the box ‘Add this data to the Data Model’.

![](<Base64-Image-Removed>)

In the Power Pivot Data Model, we will create a [Calendar table](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-creating-a-calendar-table)
 and link the **Date** columns of the tables to form a relationship between them. Then, we will create a PivotTable and load this to a new worksheet in Excel and drag the fields to the appropriate areas as illustrated below:

![](<Base64-Image-Removed>)

Next, we will create slicers. Navigate to the ‘PivotTable Analyze’ contextual tab on the Ribbon and select ‘Insert Slicers’. In the ‘Insert Slicers’ dialog, tick the Job and Attribute boxes.

![](<Base64-Image-Removed>)

We will have the slicers displayed on top of the PivotTable. Select both slicers, right-click and choose ‘Size and Properties’ then check ‘Don’t move or size with cells’ to fix the slicers in their places. You can read more about working with slicers [here](https://www.sumproduct.com/thought/slicer-of-good-fortune)
.

![](<Base64-Image-Removed>)

Now, we’re good to go…

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-slicers-for-columns-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-slicers-for-columns-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-slicers-for-columns-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-slicers-for-columns-part-2/#0)

[](https://sumproduct.com/blog/power-pivot-principles-slicers-for-columns-part-2/#0 "close")

top