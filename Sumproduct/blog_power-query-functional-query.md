# Power Query: Functional Query

**Source:** https://sumproduct.com/blog/power-query-functional-query/

---

[Home](https://sumproduct.com/)

\> Power Query: Functional Query

*   April 2, 2019

Power Query: Functional Query
=============================

Power Query: Functional Query
=============================

3 April 2019

_Welcome to our Power Query blog. This week, I look at how to make a query more functional._

I have a list of expenses from my imaginary salespeople, which I have uploaded into the Power Query Editor, _viz._

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-458.jpg)

Some of the expenses are from May and some are from June. Ideally, I want to be able to select those expenses which fall into a date period that I can define. One way I can do this is to filter on the **_Date_** column:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-473.jpg)

By selecting the **Date** column and right-clicking, I have some ‘Date/Time Filters’ to select from. I choose to use the ‘Between’ option.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-444.jpg)

When I specify the date selection, I have a list of options that I can use in reference to each date. I have decided to pick dates greater than or equal to 1st June and less than or equal to 30th June. As I have chosen all dates in June, I could just have filtered to select dates in month ‘June’ but later I will allow more flexibility in setting the date range.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-411.jpg)

The June expenses have been selected. Next, I look at the **M** code generated in the Advanced Editor. I am going to amend the code so that I can enter date parameters.

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-347.jpg)

The generated **M** code is:

**let**

    **Source = Excel.CurrentWorkbook(){\[Name=”Expenses\_Folder”\]}\[Content\],**

    **#”Changed Type” = Table.TransformColumnTypes(Source,{{“Date”, type date}, {“Expense Code”, type text}, {“Amount”, type number}, {“Name”, type text}}),**

    **#”Filtered Rows” = Table.SelectRows(#”Changed Type”, each \[Date\] >= #date(2015, 6, 1, 0, 0, 0) and \[Date\] <= #date(2015, 6, 30, 0, 0, 0))**

**in**

    **#”Filtered Rows”**

In the **#date** sections, I am going to introduce two parameters: **datefrom** and **dateto**:

(datefrom, dateto) =>

**let**

    **Source = Excel.CurrentWorkbook(){\[Name=”Expenses\_Folder”\]}\[Content\],**

    **#”Changed Type” = Table.TransformColumnTypes(Source,{{“Date”, type date}, {“Expense Code”, type text}, {“Amount”, type number}, {“Name”, type text}}),**

    **#”Filtered Rows” = Table.SelectRows(#”Changed Type”, each \[Date\] >= #date(Date.Year(datefrom), Date.Month(datefrom), Date.Day(datefrom)) and \[Date\] <= #date(Date.Year(dateto), Date.Month(dateto), Date.Day(dateto)))**

**in**

    **#”Filtered Rows”**

![](<Base64-Image-Removed>)

When I execute this code, Power Query treats my query as a function.

![](<Base64-Image-Removed>)

I can enter my parameters, and invoke the function to see the results. I’ll use 01/06/2015 and 30/06/2015.

![](<Base64-Image-Removed>)

I ‘Close & Load’ the query to save it to the workbook.

![](<Base64-Image-Removed>)

I can amend my query so that it’s more flexible for users by allowing the parameters to come from the worksheet – I’ll look at that in next week’s blog…

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-functional-query/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-functional-query/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-functional-query/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-functional-query/#0)

[](https://sumproduct.com/blog/power-query-functional-query/#0 "close")

top