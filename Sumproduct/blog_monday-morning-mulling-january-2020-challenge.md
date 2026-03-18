# Monday Morning Mulling: January 2020 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-january-2020-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: January 2020 Challenge

*   February 2, 2020

Monday Morning Mulling: January 2020 Challenge
==============================================

Monday Morning Mulling: January 2020 Challenge
==============================================

3 February 2020

_On the final Friday of each month, we set an Excel problem for you to puzzle over for the weekend. On the Monday, we publish a solution. If you think there is an alternative answer, feel free to email us. We’ll feel free to ignore you._

Welcome to this month’s Monday Morning Mulling. Were you able to work around the flexible Income Statement in our [last blog](https://sumproduct.com/blog/final-friday-fix-january-2020-challenge/)
?

To recap, last Friday we posted an interesting problem, where I have a Chart of Accounts which is subject to change, such as line items may be added or removed.

![](<Base64-Image-Removed>)

I also have the calculation results for each item in the Chart of Accounts, which will be used to build the financial report:

![](<Base64-Image-Removed>)

I want to create a financial statement that automatically updated to changes in Chart of Accounts, without having to manually add or remove items when the Chart of Accounts changes so that column **E**_(below)_ is generated formulaically (_i.e._ no Power Query or VBA):

![](<Base64-Image-Removed>)

**_Suggested solution:_**

Firstly, I need to prepare the Chart of Accounts ready for flexible financial statement. I am going to create a formula-based rank for items in each group, so that they will be sorted accordingly (this means the data should be sorted initially as well). I add two new columns, **Level 2 Rank** and **IS Rank** (“IS” stands for Income Statement). In the image below, I create a **Level 2 Rank** as follows:

![](<Base64-Image-Removed>)

The formula in cell **I11**

**\=IF(F11<>F10,1,IF(G11<>G10,I10+1,I10))**

provides a similar rank for all of the **Level 2** items with the same description, assuming the Chart of Accounts has been sorted accordingly. This ranking is repeated for each time the **Level 1** description changes (_e.g._ from Income to Salary Expenditure).

Then, I concatenate the text of Level 1 and this ranking, which later will be used in my lookup:

![](<Base64-Image-Removed>)

Going back to my Income Statement, I create a series and use this to look up the relevant group in the Chart of Accounts based upon the rank:

![](<Base64-Image-Removed>)

To look up the line items, I use **INDEX** and **MATCH** functions in combination to create the descriptions. If there is no item match, the formula will return a blank. For example, the formula in cell **E94** is

**\=IFERROR(INDEX(COA\[Level 2\],MATCH(CONCATENATE(D$92,D94),COA\[IS Rank\],0)),””)**

![](<Base64-Image-Removed>)

I can delete rows containing no line items and use a **SUMIFS** formula to pull the relevant data from the calculation section to fill in the financial statements.

![](<Base64-Image-Removed>)

Success! If the Chart of Accounts is changed in the future, I just need to insert or remove rows and copy the formulae across the cells. The Income Statement is now flexible assuming the Chart of Accounts is sorted!

Do you find this tip useful? Or have you encountered similar problems? We’re happy to help. Otherwise, we’ll see you next month for our next Final Friday Fix.

_The Final Friday Fix will return on Friday 28 February with a new Excel Challenge. In the meantime, please look out for the Daily Excel Tip on our home page and watch out for a new blog every business workday._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-january-2020-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-january-2020-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-january-2020-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-january-2020-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-january-2020-challenge/#0 "close")

top