# Power Query: Keeping it Current – Part 1

**Source:** https://sumproduct.com/blog/power-query-keeping-it-current-part-1/

---

[Home](https://sumproduct.com/)

\> Power Query: Keeping it Current – Part 1

*   July 5, 2022

Power Query: Keeping it Current – Part 1
========================================

Power Query: Keeping it Current – Part 1
========================================

6 July 2022

_Welcome to our Power Query blog. This week, I copy a query to the workbook data has been extracted from._

In [Power Query: Sheets Ahead – Part 1](https://sumproduct.com/blog/power-query-sheets-ahead-part-1/)
, I uploaded data from multiple sheets into another workbook. I had some simple monthly data:

![](https://sumproduct.com/wp-content/uploads/2025/05/39869967246118ba3ca0b95136ffedca.jpg)

This sheet is for January; I had a similar sheet in the same workbook for February:

![](https://sumproduct.com/wp-content/uploads/2025/05/49bbd77fa742a7a3f29634a6d68f2dee.jpg)

I created a query that not only concatenated this data, but also included the sheets for other months as they appeared if I refreshed it. This query was in a separate workbook:

![](https://sumproduct.com/wp-content/uploads/2025/05/d183256424fe9831bbb3d59353a78c2e.jpg)

The query created a Table in the separate workbook:

![](https://sumproduct.com/wp-content/uploads/2025/05/869ed243e517f79d540b674493d3136b.jpg)

However, what if I needed to create this Table in the original workbook?

I want to demonstrate the differences and the challenges when I move from concatenating data in an external workbook to the current workbook. I start by taking a copy of **Monthly Sales**. There are several ways I can do this, as I described in [Power Query: It’s Good to Share (a Query](https://sumproduct.com/blog/power-query-its-good-to-share-a-query/)
). I choose to right-click on my query and ‘Copy’:

![](https://sumproduct.com/wp-content/uploads/2025/05/7a826c15edd0bd1e1ebae56ff612d4c3.jpg)

Then, I open the workbook containing the original data.

![](https://sumproduct.com/wp-content/uploads/2025/05/413b3b2371b36fdbdef50fed3f860705.jpg)

It currently has no queries as I can see if I use the ‘Queries & Connections’ button on the Data tab. If I right-click in the ‘Queries & Connections’ pane, I have a paste option:

![](https://sumproduct.com/wp-content/uploads/2025/05/20e9243cfc0254cec03ea0e7703be2d9.jpg)

When I paste my query, the results don’t look good!

![](https://sumproduct.com/wp-content/uploads/2025/05/5cf7f3bc471af1e203b61fed5d246ca7.jpg)

The message is telling me the query can’t access the workbook because I have it open. This is true since it is this workbook. However, I have the **M** code, and I can change it to work with my current workbook. I will be doing this next time.

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-keeping-it-current-part-1/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-keeping-it-current-part-1/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-keeping-it-current-part-1/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-keeping-it-current-part-1/#0)

[](https://sumproduct.com/blog/power-query-keeping-it-current-part-1/#0 "close")

top