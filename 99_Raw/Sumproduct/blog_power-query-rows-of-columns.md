# Power Query: Rows of Columns

**Source:** https://sumproduct.com/blog/power-query-rows-of-columns/

---

[Home](https://sumproduct.com/)

\> Power Query: Rows of Columns

*   September 10, 2019

Power Query: Rows of Columns
============================

Power Query: Rows of Columns
============================

11 September 2019

_Welcome to our Power Query blog. Today, I split a column into rows._

I have received some sales data from John, my favourite imaginary salesperson. He’s decided to merge some of his data.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-364.jpg)

I have a list of companies on each line, instead of one row for each company. I want to have one row per company so that I can link to other company data.

I start by extracting my data to Power Query using ‘From Table’ on the ‘Get & Transform’ section of the Data tab:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-374.jpg)

I keep the headings and create my table.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-354.jpg)

I want to split the column **_Company_**. I select this column and right-click to see the options:

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-326.jpg)

I can split my column ‘By Delimiter…’, so I choose this option.

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-280.jpg)

I can choose to split by semicolon (;) – however, I don’t want to split into multiple columns, as each separate piece of data will be a company, so I look at the ‘Advanced options’ available.

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-250.jpg)

I can split into rows, so I choose this option instead.

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-211.jpg)

I now have a row for each company, with one simple step (and no **M** code knowledge required!). The generated **M** code is:

**\= Table.ExpandListColumn(Table.TransformColumns(#”Changed Type”, {{“Company”, Splitter.SplitTextByDelimiter(“;”, QuoteStyle.Csv), let itemType = (type nullable text) meta \[Serialized.Text = true\] in type {itemType}}}), “Company”)**

This has used the **M** function **Table.ExpandListColumn()**:

**Table.ExpandListColumn(table** as table, **column** as text) as table

Given a column of list data in a table, this creates a copy of a row for each value in its list.

Power Query has converted the **_Company_** column to a column of lists by using **Splitter.SplitTextByDelimiter()**, and then converted that list into rows. In this case, my data was delimited by a simple semicolon, but there are also options to use special characters, making this a very powerful function when dealing with complex columns.

![](<Base64-Image-Removed>)

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-rows-of-columns/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-rows-of-columns/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-rows-of-columns/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-rows-of-columns/#0)

[](https://sumproduct.com/blog/power-query-rows-of-columns/#0 "close")

top