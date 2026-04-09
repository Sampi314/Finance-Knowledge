# Power Query: More Fun with (Un)Pivot

**Source:** https://sumproduct.com/blog/power-query-more-fun-with-unpivot/

---

[Home](https://sumproduct.com/)

\> Power Query: More Fun with (Un)Pivot

*   December 17, 2019

Power Query: More Fun with (Un)Pivot
====================================

Power Query: More Fun with (Un)Pivot
====================================

18 December 2019

_Welcome to our Power Query blog. This week, I look at another use for unpivoting._

John, my imaginary salesperson, has been creative with his accounts again.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-307.jpg)

In this case, I’d like to see a column for months, a column for amounts, a column for expense category and for tips – that way, it’s much easier to add future data, as additional categories can be readily added.

I start by extracting the data into Power Query using the ‘From Table’ option on the ‘Get & Transform’ section of the ‘Data’ tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-310-1.jpg)

As with [last week’s blog](https://www.sumproduct.com/blog/article/power-query-blogs/power-query-fun-with-unpivottable)
, I need to remove the ‘Changed Type’ step because it refers to specific month columns:

**\= Table.TransformColumnTypes(Source,{{“Expense Type”, type text}, {“August Amount”, Int64.Type}, {“August Tips”, Int64.Type}, {“September Amount”, Int64.Type}, {“September Tips”, Int64.Type}, {“October Amount”, Int64.Type}, {“October Tips”, Int64.Type}, {“November Amount”, Int64.Type}, {“November Tips”, Int64.Type}})**

I delete this step.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-294.jpg)

I need to avoiding referencing month names in the columns; to achieve this, I select the **_Expense Type_** column, and opt to unpivot the other columns.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-270.jpg)

The **M** code generated is:

**\= Table.UnpivotOtherColumns(Source, {“Expense Type”}, “Attribute”, “Value”)**

This is good because there is no mention of the month columns. The months, amounts and tip titles now appear as data under the **_Attribute_** column. I need to perform further transformations to sort out this column. I begin by splitting the **_Attribute_** column into the separate titles.

![](<Base64-Image-Removed>)

I opt to use ‘Split Columns’ on the ‘Transform’ tab, and choose ‘By Delimiter’.

![](<Base64-Image-Removed>)

I choose to split at ‘Space’.

![](<Base64-Image-Removed>)

I can rename **_Attribute.1_** to **_Month_**. **_Attibute.2_** contains my two other column headings, so I need to pivot this column by selecting it and using the ‘Pivot’ option on the ‘Transform’ menu.

![](<Base64-Image-Removed>)

I need to choose what to put in my new columns; they should contain the associated **_Value_**, since that contains the amount.

![](<Base64-Image-Removed>)

Finally, I choose to order by month, since that makes the data easier to read. I need to create a temporary column with month number in order to do this, as I don’t want the months in alphabetical order!

![](<Base64-Image-Removed>)

I create this column and sort by it.

![](<Base64-Image-Removed>)

I can now delete the **_Month Number_** column.

![](<Base64-Image-Removed>)

My data is now ready to append and update if further months are added. Next time, I will look at another example of unpivoting.

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-more-fun-with-unpivot/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-more-fun-with-unpivot/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-more-fun-with-unpivot/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-more-fun-with-unpivot/#0)

[](https://sumproduct.com/blog/power-query-more-fun-with-unpivot/#0 "close")

top