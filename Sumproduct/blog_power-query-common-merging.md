# Power Query: Common Merging

**Source:** https://sumproduct.com/blog/power-query-common-merging/

---

[Home](https://sumproduct.com/)

\> Power Query: Common Merging

*   December 31, 2019

Power Query: Common Merging
===========================

Power Query: Common Merging
===========================

1 January 2020

_Welcome to our Power Query blog. This week, I look at a common problem._

John, my imaginary salesperson, has supplied some data showing which suppliers he has contacted recently.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-298.jpg)

I want to show which suppliers have been contacted in both months. I begin by extracting ‘September Contacts’ to Power Query.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-303-1.jpg)

In this case I don’t want to take the defaults for the location of my table. I have no need for the top heading, it will only cause problems. Instead, I alter the reference to point at the second line, and tick the ‘My table has headings’ box.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-287.jpg)

I rename my query **September Contacts** and ‘Close & Load To…’ from the ‘Home’ tab.

_![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-263.jpg)_

I opt to create only a connection, as I just want to write the suppliers that are common to September and October contacts in my spreadsheet.

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-225.jpg)

I repeat this process for ‘October Contacts’.

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-198.jpg)

I create this query as ‘Connection Only’ too.

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-167-1.jpg)

I can now select **September Contacts** in the ‘Workbook Queries’ pane and right click on it. I choose the Merge option.

![](https://sumproduct.com/wp-content/uploads/2025/05/b9ee28d90e6b5bc92ea4aeafdad51628-137-1.jpg)

I choose to merge by linking on **Supplier Name.** I can view the possible types of join.

![](https://sumproduct.com/wp-content/uploads/2025/05/0485ccbc83bdeec1d741bad442a1ea5f-113-1.jpg)

In this case, the best join for my purposes is the ‘Inner’ join which will give me ‘only matching rows’, i.e. rows of data where the data in the selected column is common to both tables.

![](https://sumproduct.com/wp-content/uploads/2025/05/daf8c4f0259ce428269c0d3d4badd32b-84-1.jpg)

The result of the merge is a query with two columns. I can expand **October Contacts** to check the data.

_![](<Base64-Image-Removed>)_

I take the defaults and expand the data.

![](<Base64-Image-Removed>)

I can see the data matches, so I remove the second column and rename my query to **Contacted in September and October**. This time, when I ‘Close & Load To…’, I want to write to the workbook.

![](<Base64-Image-Removed>)

I want this table to appear next to my original data.

![](<Base64-Image-Removed>)

I now have all the information available on one sheet.

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-common-merging/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-common-merging/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-common-merging/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-common-merging/#0)

[](https://sumproduct.com/blog/power-query-common-merging/#0 "close")

top