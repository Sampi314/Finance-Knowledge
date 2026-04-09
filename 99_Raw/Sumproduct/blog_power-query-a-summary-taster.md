# Power Query: A Summary Taster

**Source:** https://sumproduct.com/blog/power-query-a-summary-taster/

---

[Home](https://sumproduct.com/)

\> Power Query: A Summary Taster

*   March 23, 2017

Power Query: A Summary Taster
=============================

Power Query: A Summary Taster
=============================

24 March 2017

_Welcome to our Power Query blog. Today I look at a way of extracting data from groupings._

Following on from [last week’s blog](https://www.sumproduct.com/blog/article/power-query-blogs/power-query-group-and-conquer)
 on grouping in Power Query, despite having simplified my data into groupings, I can still access data that makes up the group to provide more information.

At the end of that article, I had made some changes to a query of mine, ‘**ACCT\_Order\_Charges\_with\_Group**‘. I will be making more changes, but to avoid causing problems to the grouping query, I will create a copy of the query. I already have taken the grouping a step further from the end of the last blog to show which item group is the best seller:

![](https://sumproduct.com/wp-content/uploads/2025/05/0ff776db0f90ac5ec0c1029ab97e6bbc.jpg)

The easiest way to make a copy of my query is in the Excel workbook: the ‘Workbook Queries’ pane should be displayed (if it’s not use the ‘Show Pane’ option on the ‘POWER QUERY’ tab, or in the ‘Get and Transform’ section). Right clicking my query gives me the option to ‘Duplicate’ it.

![](https://sumproduct.com/wp-content/uploads/2025/05/02bf26bad4361093eb98d2961ec8e690.jpg)

I duplicate my query, and give it a new name ‘**Order\_Charges\_Summarising**‘:

![](https://sumproduct.com/wp-content/uploads/2025/05/11861221351f253bc447da8308e45205.jpg)

Now, suppose I was at this stage and I needed to find out the most expensive selling item in each item group. I need to see the data behind the grouping, and to do this I need to modify the grouping step. I click on the gear icon next to the ‘Grouped Rows’ step and add a column (‘aggregation’) ‘**Details**‘ which will act on all rows:

![](https://sumproduct.com/wp-content/uploads/2025/05/aed119418ca777c501db5a3557d22039.jpg)

Clicking ‘OK’ gives me a new column, which contains tables. Clicking on the word ‘Table’ has two effects. Firstly, I get a warning because other steps exist after my ‘Grouped Rows’ step and secondly, I see the contents of my table _viz_.

![](https://sumproduct.com/wp-content/uploads/2025/05/96120301df123ef050fab2c409bef00a.jpg)

The warning reminds me to remove the last two steps, which I can do since they were only introduced to tidy up my grouped data. Having removed them, I need to find a way to get at the data in the tables so that I can work out which item was the most expensive selling item in each item group. I am going to need a custom column, and I am going to use a record. The formula I use is:

**\= Table.Max(\[Details\], “Amount”)**

![](<Base64-Image-Removed>)

Clicking on any record will show me what is in it (and creates a step):

![](https://sumproduct.com/wp-content/uploads/2025/05/5878e9947e16f8f1977b7773ec4dcf28.jpg)

Since I have chosen to use a record, what is shown is not just the most expensive item in the group, but also the other data associated with that item, in effect a row within a row. I delete the last step and go back to the ‘Added Custom’ step. I then choose to use the expand icon next to the **_MaxRecord_** column name to expand all the records:

![](https://sumproduct.com/wp-content/uploads/2025/05/3bf671d0912a04e25c64f7da000e12bf.jpg)

I only want the ‘**Amount**‘ and ‘**Description**‘ and I’ll keep the column names for now.

![](https://sumproduct.com/wp-content/uploads/2025/05/cab79ee1937d42e5eb326048c59a750f.jpg)

What I have is the description of the most expensive item in each group, and the price for that item, so I change the names accordingly, remove my **_Details_** column and reorder ready to load.

![](https://sumproduct.com/wp-content/uploads/2025/05/69f1ccb92ea4cec7470591200e0d0c02.jpg)

This is a simple example of getting data from records when the data has been grouped.

Want to read more about Power Query? A complete list of all our Power Query blogs can be found [here](https://www.sumproduct.com/thought/power-query-blog-series)
. Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-a-summary-taster/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-a-summary-taster/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-a-summary-taster/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-a-summary-taster/#0)

[](https://sumproduct.com/blog/power-query-a-summary-taster/#0 "close")

top