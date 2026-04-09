# Power Pivot Principles: Slicers for Columns – Part 1

**Source:** https://sumproduct.com/blog/power-pivot-principles-slicers-for-columns-part-1/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Slicers for Columns – Part 1

*   January 11, 2021

Power Pivot Principles: Slicers for Columns – Part 1
====================================================

Power Pivot Principles: Slicers for Columns – Part 1
====================================================

12 January 2021

_Welcome back to the Power Pivot Principles blog. This week, we will talk about creating slicers for columns._

To give this idea a context, suppose there is a dataset with Actual revenue

![](<Base64-Image-Removed>)

and another data set with Budget revenue for a particular list of jobs.

![](<Base64-Image-Removed>)

Both tables are loaded into the Power Pivot Data Model.

From there, a PivotTable is created with a slicer for the **Job** field. Each job in the PivotTable includes its **Actual** and **Budget** revenue, which are the Value fields and may only be added or removed from the PivotTable Field List. The problem now is that I want to create a slicer, where I can also choose to view either one of **Actual**, **Budget**, **Variance** or all of them.

![](<Base64-Image-Removed>)

To do this, I need the help of Power Query to transform my data tables before loading them back into my Power Pivot Data Model. Click on the **Actual** table and navigate to the Data tab on the Ribbon and choose ‘From Table/Range’.

![](<Base64-Image-Removed>)

After checking Data Types and ensuring I am happy with field (column) names, I duplicate the **Actual** table, renaming it to **Budget**. I go to the ‘Source’ step, change the ‘Actual’ in the formula bar (or the Advanced Editor) to ‘Budget’. I do the same with the ‘Changed Type’ step, if necessary. Since the two tables are in the same structure, this way, I save my time and I do not need to close and load, come back to Excel or go to ‘New Source’ and load the **Budget** table into Power Query.

![](<Base64-Image-Removed>)

Next, I need both **Actual** and **Budget** figures for **Job** in one table. I go to the Home tab on the Ribbon and select **‘[Merge Queries](https://sumproduct.com/blog/power-query-common-merging/)
‘****\-> ‘Merge Queries as New’**. The two tables have the **Job** field in common, the ‘[Join Kind](https://sumproduct.com/blog/power-query-if-you-cant-tell-them-apart-join-them/)
‘ will be ‘Full Outer’ as I want to take all possible rows from both tables.

![](<Base64-Image-Removed>)

Then, I expand to take the **Budget** column from the **Budget** table duly merged.

![](<Base64-Image-Removed>)

To get the **Variance** between **Actual** and **Budget**, select both **Actual** and **Budget** columns, go to the ‘Add Column’ tab on the Ribbon, select **Standard -> Subtract**.

![](<Base64-Image-Removed>)

Next, select the **Job** and **Date** columns, navigate to the **Transform -> Unpivot Columns -> Unpivot Other Columns** (this is in case there are additional columns later).

![](<Base64-Image-Removed>)

and now the query table should look like the one below:

![](<Base64-Image-Removed>)

Did you see the light at the end of the tunnel? I will come back next week for the next steps.

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-slicers-for-columns-part-1/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-slicers-for-columns-part-1/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-slicers-for-columns-part-1/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-slicers-for-columns-part-1/#0)

[](https://sumproduct.com/blog/power-pivot-principles-slicers-for-columns-part-1/#0 "close")

top