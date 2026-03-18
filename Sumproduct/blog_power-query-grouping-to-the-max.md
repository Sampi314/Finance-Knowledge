# Power Query: Grouping to the Max

**Source:** https://sumproduct.com/blog/power-query-grouping-to-the-max/

---

[Home](https://sumproduct.com/)

\> Power Query: Grouping to the Max

*   September 24, 2019

Power Query: Grouping to the Max
================================

Power Query: Grouping to the Max
================================

25 September 2019

_Welcome to our Power Query blog. Today, I look at groups and how to interrogate them._

I have some financial information which I plan to group:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-357.jpg)

I want to summarise this information by item group. To do this, I can create a query using ‘From Table’ from the ‘Get & Transform’ section of the Data tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-366.jpg)

In order to summarise my data, I use the ‘Group by’ option, which is on both the Home and Transform tabs.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-346.jpg)

I use the Advanced option as I am going to add together two aggregations.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-318.jpg)

This gives me two new columns and far less rows!

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-274.jpg)

If I click on the icon next to the **Item Details** column, I can expand the details behind the grouping. I can also click on the white space next to each ‘Table’ to view the contents.

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-244.jpg)

This is one way to see the data behind the grouping; another method is to use the **M** function **Table.Max()**:

Table.Max(**table** as table, **comparisonCriteria** as any, optional **default** as any) as any

This returns the largest row in the **table**, given the **comparisonCriteria**. If the **table** is empty, the optional **default** value is returned.

I decide to find out which is the most expensive item in each group. The table that I will use for the **Table.Max()** functionality is my **Item\_Details** column. I create a custom column from the ‘Add Column’ tab.

![](<Base64-Image-Removed>)

The **M** code I have entered is:

**\= Table.Max(\[Item Details\], “Amount”)**

This will allow me to find the item in each group with the highest value (**Amount**). The function returns a record containing the details for the most expensive item. Executing this code creates a new column of records.

![](<Base64-Image-Removed>)

I can view the data for each row by clicking on the white space next to ‘Record’, as shown in the previous screenshot. I can also expand the new column to extract the data I want to see:

![](<Base64-Image-Removed>)

I choose the data I wish to show. In order to prove that this data is from the correct item group, I will expand the item group too, and keep the original column name, so that I may compare my original and expanded columns.

![](<Base64-Image-Removed>)

I can see that the item group columns match, so I remove the columns I no longer need.

![](<Base64-Image-Removed>)

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-grouping-to-the-max/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-grouping-to-the-max/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-grouping-to-the-max/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-grouping-to-the-max/#0)

[](https://sumproduct.com/blog/power-query-grouping-to-the-max/#0 "close")

top