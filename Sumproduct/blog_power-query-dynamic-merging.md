# Power Query: Dynamic Merging

**Source:** https://sumproduct.com/blog/power-query-dynamic-merging/

---

[Home](https://sumproduct.com/)

\> Power Query: Dynamic Merging

*   May 5, 2020

Power Query: Dynamic Merging
============================

Power Query: Dynamic Merging
============================

6 May 2020

_Welcome to our Power Query blog. This week, I look at working dynamically with merged queries._

_I have some data from my imaginary salespeople, which I have loaded into Power Query and merged._

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-224-1.jpg)

I use the expand icon next to the column heading of the column _**Tent Packs**__._

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-218-1.jpg)

I select the two columns I need and click OK.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-210-1.jpg)

The problem is, the **M** code created for this step is:

**\= Table.ExpandTableColumn(Source, “Tent Packs”, {“Item”, “Cost”}, {“Item”, “Cost”})**

which specifically mentions the column names **Item** and **Cost**, meaning that if I add more columns to **Tent Packs** they will not be expanded. I can add a new column, **Supplier**, to show this.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-185-1.jpg)

When I look at my merged query:

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-159-1.jpg)

Since the expand step specifies column names, the new column is not included. I need another way to create this step so that it can be dynamic. My current step is:

**\= Table.ExpandTableColumn(Source, “Tent Packs”, {“Item”, “Cost”}, {“Item”, “Cost”})**

The last two parameters are lists of column names: **{“Item”, “Cost”}** and **{“Item”, “Cost”}**. Instead of this, I can get the column names from the table **Tent Packs**:

**\=Table.ExpandTableColumn(Source, “Tent Packs”, Table.ColumnNames(#”Tent Packs”))**

![](<Base64-Image-Removed>)

This time I have all three of my columns. In my case, the linked column in **Tent Sales** has a different name to its corresponding column in **Tent Packs**, _i.e_. **Tent Pack** links to **Pack Number**. If they had the same name, then I can avoid extracting **Pack Number** by removing it from the list of columns.

**\=Table.ExpandTableColumn(Source, “Tent Packs”, Table.ColumnNames(#”Tent Packs”))**

This would change to:

**\= Table.ExpandTableColumn(Source, “Tent Packs”, List.RemoveItems(Table.ColumnNames(#”Tent Packs”), {“Pack Number”}))**

![](<Base64-Image-Removed>)

I can then add steps to this query knowing that all columns from **Tent Packs** will be expanded.

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-dynamic-merging/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-dynamic-merging/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-dynamic-merging/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-dynamic-merging/#0)

[](https://sumproduct.com/blog/power-query-dynamic-merging/#0 "close")

top