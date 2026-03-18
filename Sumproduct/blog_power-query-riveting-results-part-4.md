# Power Query: Riveting Results Part 4

**Source:** https://sumproduct.com/blog/power-query-riveting-results-part-4/

---

[Home](https://sumproduct.com/)

\> Power Query: Riveting Results Part 4

*   January 4, 2022

Power Query: Riveting Results Part 4
====================================

Power Query: Riveting Results Part 4
====================================

5 January 2022

_Welcome to our Power Query blog. This week, I start to create a parameter from a cell in Excel._

My salespeople are taking a _really_ long break. This week, I continue looking at the exam results I created in [Power Query: Riveting Results Part 1](https://sumproduct.com/blog/power-query-riveting-results-part-1/)
:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-82.jpg)

I will be grading the results, and I will be using this example to explore parameters. [Last week](https://sumproduct.com/blog/power-query-riveting-results-part-3/)
, I added parameters to the query **Exam Results.**

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-116.jpg)

Whilst I can change these parameters in Power Query, I’d now like to have parameters that I can change from Excel. On a new Excel Sheet, I have some data for the thresholds:

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-86.jpg)

I start by defining a Name for the first threshold. I can do this by selecting the cell and right-clicking:

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-82.jpg)

I define the Name to be ‘Grade\_9’:

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-68.jpg)

I can now see this in Power Query. In the Power Query Editor, I create a new Blank Query. I can do this by right-clicking in the Queries pane (this is one of several methods to create a Blank Query):

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-59.jpg)

In my Blank Query, I enter the following **M** code:

**\= Excel.CurrentWorkbook()**

This will show me what is in the current Excel Workbook:

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-56.jpg)

There is the **Grade\_9** I created. The value will be in the ‘Table’ next to it.

Next time, I will extract this data into a parameter, and look at why this is different from a parameter created from the ‘Manage Parameters’ dialog.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-riveting-results-part-4/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-riveting-results-part-4/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-riveting-results-part-4/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-riveting-results-part-4/#0)

[](https://sumproduct.com/blog/power-query-riveting-results-part-4/#0 "close")

top