# Power Query: Fun with (Un)Pivot

**Source:** https://sumproduct.com/blog/power-query-fun-with-unpivottable/

---

[Home](https://sumproduct.com/)

\> Power Query: Fun with (Un)Pivot

*   December 10, 2019

Power Query: Fun with (Un)Pivot
===============================

Power Query: Fun with (Un)Pivot
===============================

11 December 2019

_Welcome to our Power Query blog. This week, I look at a use for unpivoting._

John, my imaginary salesperson, has been creative with his accounts again…

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-310.jpg)

I asked for a monthly total, but I wanted a single month column rather than a column for each month – that way, it’s much easier to add future data.

I start by extracting the data into Power Query using the ‘From Table’ option on the ‘Get & Transform’ section of the ‘Data’ tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-314-1.jpg)

I opt to take the defaults as I have headings.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-298.jpg)

Usually, I don’t have a problem with the automated step that Power Query carries out to set the data types, _i.e._ ‘Changed Type’. However, this could cause me problems if John adds (or removes) months from his table as the month columns have been specified:

**\= Table.TransformColumnTypes(Source,{{“Expense Type”, type text}, {“September”, Int64.Type}, {“October”, Int64.Type}, {“November”, Int64.Type}})**

I delete this step.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-274.jpg)

On the ‘Transform’ menu, I have several options when it comes to unpivoting columns. I can unpivot them all, or those I select, or those I don’t select. As for the ‘Changed Type’ step, it’s important that I don’t end up with a step where the months columns are named. Although I want to unpivot my month columns, I don’t want to name them explicitly. The answer is to select the **_Expense Type_** column, and opt to unpivot the other columns instead.

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-236.jpg)

The **M** code generated is:

**\= Table.UnpivotOtherColumns(Source, {“Expense Type”}, “Attribute”, “Value”)**

This is good because there is no mention of the month column names. The months now appear as data under the **_Attribute_** column. I rename this column **_Month_**, and I rename the **_Value_** column to **_Amount_**. I also set the data types, since I had to delete that step before.

![](<Base64-Image-Removed>)

My data is now ready to append and update if further months are added. I ‘Close & Load’ to load the transformed data into my Excel workbook.

![](<Base64-Image-Removed>)

I add a month to the original data to check that everything works as expected:

![](<Base64-Image-Removed>)

When I refresh the data, I can see that my transformed data is now complete.

![](<Base64-Image-Removed>)

Next time I will look at a more complex example with unpivoting.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-fun-with-unpivottable/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-fun-with-unpivottable/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-fun-with-unpivottable/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-fun-with-unpivottable/#0)

[](https://sumproduct.com/blog/power-query-fun-with-unpivottable/#0 "close")

top