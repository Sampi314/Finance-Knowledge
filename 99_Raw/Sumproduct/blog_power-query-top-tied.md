# Power Query: Top Tied

**Source:** https://sumproduct.com/blog/power-query-top-tied/

---

[Home](https://sumproduct.com/)

\> Power Query: Top Tied

*   October 1, 2019

Power Query: Top Tied
=====================

Power Query: Top Tied
=====================

2 October 2019

_Welcome to our Power Query blog. Today, I look at how to rank tied places._

_The figures have come in for my imaginary salespeople:_

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-352.jpg)

_Since the top salesperson gets a bonus, I want to indicate clearly who is top. This principle can be expanded to include as many places as I like. I pull my data into Power Query using ‘From Table’ from the ‘Get & Transform’ section of the ‘Data’ tab._

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-361.jpg)

_I sort my data by **July Sales** using the arrow next to the column name. I then choose to add an index column from the ‘Add Column’ tab (starting at zero)._

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-342.jpg)

_I can now create a custom column, which will allocate the top place if **Index** is 0._

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-314.jpg)

_I click OK, and I can see the top salesperson, Mary._

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-270.jpg)

_I ‘Close & Load’ this to Excel from the ‘Home’ tab._

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-240.jpg)

_However, I have some late results, so I need to go back to my source data._

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-205.jpg)

_Kevin’s results have been added, so I check the results of my query._

![](https://sumproduct.com/wp-content/uploads/2025/05/b9ee28d90e6b5bc92ea4aeafdad51628-168.jpg)

_Well that doesn’t seem fair: Kevin has not reached the bonus category. I need to amend my query._

![](https://sumproduct.com/wp-content/uploads/2025/05/0485ccbc83bdeec1d741bad442a1ea5f-141.jpg)

_Since the index is incremented for each salesperson, Kevin is not getting the correct ranking. I need to group by **July Sales**. I can do this using ‘Group By’ on the ‘Transform’ tab._

![](https://sumproduct.com/wp-content/uploads/2025/05/daf8c4f0259ce428269c0d3d4badd32b-104-1.jpg)

_I also add a new index column._

![](<Base64-Image-Removed>)

_I can now add a new conditional column which will indicate top ranking._

![](<Base64-Image-Removed>)

_I need to link this back to my salespeople. I will link this table to the table I had at step ‘Added Conditional Column’, before I grouped my data. If I look at the ‘Home’ tab, I have the option to ‘Merge Queries’._

![](<Base64-Image-Removed>)

_Since I only have one query, I have to link it to itself, but I can amend the **M** code later._

![](<Base64-Image-Removed>)

_I link on **July Sales**, since that will eventually give me all the salespeople._

![](<Base64-Image-Removed>)

I have generated the following **M** code:

**\= Table.NestedJoin(#”Added Conditional Column1″, {“July Sales”}, #”Added Conditional Column1″, {“July Sales”}, “Added Conditional Column1”, JoinKind.LeftOuter)**

This joins the query to itself at the same point, but I will amend it to link back to the earlier step.

**\= Table.NestedJoin(#”Added Conditional Column1″, {“July Sales”}, #”Added Conditional Column”, {“July Sales”}, “Merged Queries”, JoinKind.LeftOuter)**

Thanks to the similar step names, I only have to change the second “Added Conditional Column1” to “Added Conditional Column”. I call my new column **Merged Queries**.

![](<Base64-Image-Removed>)

_I can expand my new column to get all the rows back, and I will choose to retrieve only the name of the salesperson from **Merged Queries**__**.**_

![](<Base64-Image-Removed>)

_I can now see that Mary and Kevin are both Top, and they will get their bonus! I remove **Index** and **Count** and reorganise my data before I ‘Close & Load’ to Excel._

![](<Base64-Image-Removed>)

_To check the query for more data, I enter the details for more salespeople._

![](<Base64-Image-Removed>)

_When I refresh my query, the results are clear._

![](<Base64-Image-Removed>)

_I clearly have lots of top salespeople due for a bonus!_

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-top-tied/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-top-tied/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-top-tied/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-top-tied/#0)

[](https://sumproduct.com/blog/power-query-top-tied/#0 "close")

top