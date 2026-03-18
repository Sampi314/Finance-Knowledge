# Power Query: Month Mayhem – Part 8

**Source:** https://sumproduct.com/blog/power-query-month-mayhem-part-8/

---

[Home](https://sumproduct.com/)

\> Power Query: Month Mayhem – Part 8

*   August 20, 2024

Power Query: Month Mayhem – Part 8
==================================

Power Query: Month Mayhem – Part 8
==================================

21 August 2024

_Welcome to our Power Query blog. Today, I complete the challenge._

My salespeople are back from their break and I have more reports to construct. I have a report with a list of the clients they have been working with each month:

![](https://sumproduct.com/wp-content/uploads/2025/05/3741291297de31a01581248852cb3eb9-1.jpg)

I would like to display the amount details in the salesperson sections, but aligned to the relevant month at the top of the page:

![](https://sumproduct.com/wp-content/uploads/2025/05/f5f3bd2d0a70b78c5ce3b05ae83a4a23-1.jpg)

[Last time](https://sumproduct.com/blog/power-query-month-mayhem-part-7/)
, I extracted the interim report headings.

![](https://sumproduct.com/wp-content/uploads/2025/05/c6bbe9a7656141f6972f8c364cecb305-1.jpg)

I extracted them from the **Source Summary** query into a new query which I called **Report Headings** and then appended **Mapping Merge** to get the body of the query that I will be loading to the workbook:

![](https://sumproduct.com/wp-content/uploads/2025/05/8223c0356cf0fdc29ce59c099d464e15-1.jpg)

My transformations are almost done. I still need to add the top heading and fully prepare my data for loading. I need to be able to control the order that the data is appended in, as I want to add this query to the top header (**Months**). I could either start from **Months**, and ‘Append Queries’ from the Home tab, or I can start from **Report Headings** and choose to ‘Append Queries as New’ from the ‘Append Queries’ dropdown on the Home tab. I choose the latter option to create a new query which I will be loading to the workbook.

![](https://sumproduct.com/wp-content/uploads/2025/05/cb24d1a7e07c660dcf5d00fdd556c7a9-1.jpg)

I may use the ‘Two tables’ format, and make sure that I put **Months** first.

![](https://sumproduct.com/wp-content/uploads/2025/05/348e4da08cab3e00d2be2425a87af88e-1.jpg)

I can see that my new query, called **Report Output**, is already looking promising. I just need to remove the indexes I created. I select the column headings of **Section Index** and **Index** whilst holding down the **CTRL** key:

![](https://sumproduct.com/wp-content/uploads/2025/05/088b83b335e19e326eac2b0038fe1564-1.jpg)

I right-click and choose to ‘Remove Columns’. The final transformation is to promote the headers, which I can do from the Home tab or the Transform tab:

![](<Base64-Image-Removed>)

Since some of the columns are a mixture of numbers and text, the ‘Changed Type’ step leaves most of them as data type ‘Any’.

![](<Base64-Image-Removed>)

I select one of the headers and use **CTRL** + **A** to select them all. On the Transform tab, I change ‘Data Type’ to ‘Text’ for all the columns:

![](<Base64-Image-Removed>)

This is incorporated by Power Query into the existing ‘Changed Type’ step. My data is ready for me to ‘Close & Load To…’ from the Home tab:

![](<Base64-Image-Removed>)

I initially choose to set all the queries to ‘Connection Only’ as I only want to load **Report Output**.

![](<Base64-Image-Removed>)

Having done this, I select the **Report Output** query, and right-click to change the ‘Load To…’ settings:

![](<Base64-Image-Removed>)

I choose to load to a Table on the ‘Existing worksheet’:

![](<Base64-Image-Removed>)

I click ‘OK’ and the data is loaded:

![](<Base64-Image-Removed>)

I can remove the filters in the Table tab if I wish:

![](<Base64-Image-Removed>)

My query is now complete.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-month-mayhem-part-8/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-month-mayhem-part-8/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-month-mayhem-part-8/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-month-mayhem-part-8/#0)

[](https://sumproduct.com/blog/power-query-month-mayhem-part-8/#0 "close")

top