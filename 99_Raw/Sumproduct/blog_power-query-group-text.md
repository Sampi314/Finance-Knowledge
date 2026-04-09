# Power Query: Group Text

**Source:** https://sumproduct.com/blog/power-query-group-text/

---

[Home](https://sumproduct.com/)

\> Power Query: Group Text

*   May 4, 2021

Power Query: Group Text
=======================

Power Query: Group Text
=======================

5 May 2021

_Welcome to our Power Query blog. This week, I look at how to modify a grouping statement to accommodate text fields._

I have some data for my imaginary salespeople:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-205.jpg)

They have been selling off some of the old stock, and I want to see the sales figures for each tent type and who has sold it. I start by extracting my data into Power Query using ‘From Table / Range’ in the ‘Get & Transform Data’ section of the Data tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-264.jpg)

I accept the ‘Create Table’ defaults and view my data in the Power Query Editor.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-210.jpg)

I am going to group my data using the ‘Group By’ option on the Transform tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-199.jpg)

I want to group by **Tent Type**. To begin with, I want to see the sales totals:

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-168.jpg)

I can achieve this by grouping on **Tent Type** and summing **Price**.

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-147.jpg)

I also want to see which salespeople sold the tents. I go back to the ‘Grouped Rows’ step.

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-136.jpg)

If I go into the ‘Advanced’ options, I can add another aggregation, but all the operations are aimed at numerical values. However, I am going to go ahead and use a sum, and then amend the **M** code produced.

![](https://sumproduct.com/wp-content/uploads/2025/05/b9ee28d90e6b5bc92ea4aeafdad51628-115.jpg)

This gives me an error, which is not surprising since I am trying to add up text values!

![](https://sumproduct.com/wp-content/uploads/2025/05/0485ccbc83bdeec1d741bad442a1ea5f-104.jpg)

Having failed to add up Derek, I look at the **M** code produced:

**\= Table.Group(#”Changed Type”, {“Tent Type”}, {{“Sales Total”, each List.Sum(\[Price\]), type nullable number}, {“Sold By”, each List.Sum(\[Salesperson\]), type nullable text}})**

I am interested in the code associated with the **Sold By** column.

**{“Sold By”, each List.Sum(\[Salesperson\]), type nullable text}**

This is currently using **List.Sum()** to add up the **Salesperson** column. If I am going to add up text, then I need a text function **Text.Combine().** This will allow me to compile a list of the salespeople, separated by a separator of my choice.

**{“Sold By”, each Text.Combine(\[Salesperson\], “, “), type nullable text}**

I have chosen to separate the salespeople with a comma and a space. The full step now looks like this:

**\= Table.Group(#”Changed Type”, {“Tent Type”}, {{“Sales Total”, each List.Sum(\[Price\]), type nullable number}, {“Sold By”, each Text.Combine(\[Salesperson\], “, “), type nullable text}})**

![](<Base64-Image-Removed>)

I now have a list of salespeople in the **Sold By** column.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-group-text/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-group-text/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-group-text/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-group-text/#0)

[](https://sumproduct.com/blog/power-query-group-text/#0 "close")

top