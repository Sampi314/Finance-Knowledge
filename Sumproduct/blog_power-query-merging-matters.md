# Power Query: Merging Matters

**Source:** https://sumproduct.com/blog/power-query-merging-matters/

---

[Home](https://sumproduct.com/)

\> Power Query: Merging Matters

*   March 16, 2021

Power Query: Merging Matters
============================

Power Query: Merging Matters
============================

17 March 2021

_Welcome to our Power Query blog. This week, I look at solving a problem with a nested join and the M function Table.Buffer()._

It’s time for that evergreen tent data:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-234.jpg)

I want to get the descriptions in the same table as the charges data. In order to do this, I will be merging my data in a couple of different ways, and then I will look at a way to make this merge more efficient.

I start by extracting my tables to Power Query. I will use the charges data as an example, but the process is the same for descriptions.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-296.jpg)

I start by using ‘From Table / Range’ on the ‘Get & Transform’ section of the Data tab. I accept the usual defaults to create a new query.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-239.jpg)

To simplify the connection between my tables, I create an index column which I will call **Table\_Key**.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-226.jpg)

I name my table **Charges**, and only create the connection for my table for now, so that I avoid loading data until I am ready.

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-189.jpg)

I can now repeat the process for my **Descriptions** table.

The most obvious way to bring the data together is to merge the tables. The merge option is in the Home tab, and I choose to ‘Merge Queries as New’ as I wish to keep my queries.

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-168.jpg)

I can then choose how to merge my tables.

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-153.jpg)

This will create a new table with links from the **Charges** table to the matching row in the **Descriptions** table.

![](https://sumproduct.com/wp-content/uploads/2025/05/b9ee28d90e6b5bc92ea4aeafdad51628-130.jpg)

I can then expand the **Description** column to get the data I need.

![](<Base64-Image-Removed>)

This will give me the result I want, but I would like to investigate using a column to get the same result instead.

![](<Base64-Image-Removed>)

If I go back to my **Charges** query, I create a duplicate of the query and create a custom column to pull in the data I need from **Descriptions**.

![](<Base64-Image-Removed>)

I click ‘OK’ to view the results.

![](<Base64-Image-Removed>)

This custom column tries to point to the **Descriptions** table, but I am getting errors because although the syntax is fine, Power Query needs more help to get the field from the correct table. I need to go into the Advanced Editor and view the code to see what is happening.

![](<Base64-Image-Removed>)

The **M** code generated is:

**Let**

    **Source = Excel.CurrentWorkbook(){\[Name=”Table2″\]}\[Content\],**

    **#”Changed Type” = Table.TransformColumnTypes(Source,{{“Order\_Key”, Int64.Type}, {“Order\_Line\_Number”, Int64.Type}, {“Charge\_Line\_Number”, Int64.Type}, {“Amount”, Int64.Type}}),**

    **#”Added Custom” = Table.AddColumn(#”Changed Type”, “Custom”,**

    **each Table.SelectRows(Descriptions,**

     **Value.Equals(Descriptions\[Table\_Key\],\[Table\_Key\])))**

**in**

    **#”Added Custom”**

I have separated the lines

     **each Table.SelectRows(Descriptions,**

     **Value.Equals(Descriptions\[Table\_Key\],\[Table\_Key\])))**

because I am going to add some more code to this.

The part that is confusing Power Query is ‘**each**‘. In this context, **each** can only mean **Charges**, but I need it to consider **Description** as well. I will create two variables, **eachCharge** and **eachDescription**. I am going to create a nested join.

**(eachCharge) =>**

     **Table.SelectRows(Descriptions,**

     **(eachDescription) =>**

     **Value.Equals(eachDescription\[Table\_Key\], eachCharge\[Table\_Key\])))**

The whole **M** code now looks like this:

**let**

    **Source = Excel.CurrentWorkbook(){\[Name=”Table2″\]}\[Content\],**

    **#”Changed Type” = Table.TransformColumnTypes(Source,{{“Order\_Key”, Int64.Type}, {“Order\_Line\_Number”, Int64.Type}, {“Charge\_Line\_Number”, Int64.Type}, {“Amount”, Int64.Type}}),**

    **#”Merged Columns” = Table.CombineColumns(Table.TransformColumnTypes(#”Changed Type”, {{“Order\_Line\_Number”, type text}, {“Order\_Key”, type text}, {“Charge\_Line\_Number”, type text}}, “en-GB”),{“Order\_Line\_Number”, “Order\_Key”, “Charge\_Line\_Number”},Combiner.CombineTextByDelimiter(“:”, QuoteStyle.None),”Table\_Key”),**

    **#”Added Custom” = Table.AddColumn(#”Merged Columns”, “Description”,**

     **(eachCharge) =>**

     **Table.SelectRows(Descriptions,**

     **(eachDescription) =>**

     **Value.Equals(eachDescription\[Table\_Key\], eachCharge\[Table\_Key\])))**

**in**

    **#”Added Custom”**

If I now apply these changes,

![](<Base64-Image-Removed>)

I have a column of tables which can be expanded to give me the description.

![](<Base64-Image-Removed>)

However, this is not evaluating quickly enough for my purposes. I have a large dataset, and this method is proving less efficient than the simple merge. Since I am working with flat files, and not a relational database, I can use **Table.Buffer()** as I have no query folding.

**Table.Buffer(table** as table**)** as table

This buffers a **table** in memory, isolating it from external changes during evaluation.

I am going to hold the contents of **Descriptions** in RAM, so that it is not affected by any external changes. To do this, I need to add a step, and I will do this in the Advanced Editor. The line I will add is before the changes I just made to the **Added Custom** step:

**BufferedTable = Table.Buffer(Descriptions)**

I need to change the reference to **Descriptions** to use **BufferedTable** instead:

  **BufferedTable = Table.Buffer(Descriptions),**

    **#”Added Custom” = Table.AddColumn(#”Merged Columns”, “Description”,**

     **(eachCharge) =>**

     **Table.SelectRows(BufferedTable,**

     **(eachDescription) =>**

     **Value.Equals(eachDescription\[Table\_Key\], eachCharge\[Table\_Key\]))),**

When I apply these changes,

![](<Base64-Image-Removed>)

the merge step evaluates more quickly. However, **Table.Buffer()** should be used with caution, especially with large datasets. The buffering uses RAM, and the amount of RAM that is held by Power Query is limited, which means that if the limits are exceeded, the RAM has to come from the hard drive, which could seriously slow things down. Therefore, **Table.Buffer()** should only be applied where necessary, and models using it should be tested before full scale implementation.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-merging-matters/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-merging-matters/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-merging-matters/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-merging-matters/#0)

[](https://sumproduct.com/blog/power-query-merging-matters/#0 "close")

top