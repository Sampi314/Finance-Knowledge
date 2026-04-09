# Power Query: Start and End with Grouping

**Source:** https://sumproduct.com/blog/power-query-start-and-end-with-grouping/

---

[Home](https://sumproduct.com/)

\> Power Query: Start and End with Grouping

*   June 13, 2017

Power Query: Start and End with Grouping
========================================

Power Query: Start and End with Grouping
========================================

14 June 2017

_Welcome to our Power Query blog. Today I look at extracting start and end dates for my list of sales employees._

For those following the series, my past blogs have often dipped into the expense accounts of my (fictional) salespeople. For today’s scenario, I will extract the start and end date of my employees’ expense period to show how easy it is when I use the grouping functionality in Power Query.

I created the sheet below using a combined expense query created in [Aggregating Aggravating Worksheets](https://sumproduct.com/blog/power-query-aggregating-aggravating-worksheets/)
.

![](https://sumproduct.com/wp-content/uploads/2025/05/48f37bc5dca2aaaec1a2581f43038351.jpg)

I already have my ‘Expenses’ query, so I begin by double clicking on my query to get into the ‘Query Editor’ screen:

![](https://sumproduct.com/wp-content/uploads/2025/05/9eb956b741a038c851f1e983834c1cfb.jpg)

In [Group and Conquer](https://sumproduct.com/blog/power-query-group-and-conquer/)
, I looked at using grouping to simplify data, and I will be using a similar technique here. On the ‘Transform’ tab, I choose ‘Group By’. Since I am looking for the period for each person, my grouping will be driven by my **_Name_** column. I need to find the start and end date for their expense period. I begin entering the first grouping level, naming my column ‘Start Date’, and making it a minimum of the date:

![](https://sumproduct.com/wp-content/uploads/2025/05/6dd010a18f861aa15d8be4e4ee3ec009.jpg)

So far so good, so what? Now I need to get the end date, so I create another grouping level using the ‘Add aggregation’ button. This will also act on the **_Date_** column, this time taking the maximum value:

![](https://sumproduct.com/wp-content/uploads/2025/05/309b54b41d0000a15931c2ae8c279a97.jpg)

Now all I need to do is click ‘OK’ to see what happens.

![](https://sumproduct.com/wp-content/uploads/2025/05/ca5cc258b02f97314b66313c1bc5838e.jpg)

It all looks good, so I have my result which can be loaded into an Excel sheet.

![](https://sumproduct.com/wp-content/uploads/2025/05/08b1e37be7a4a1afb3b7ee25709e273d.jpg)

Want to read more about Power Query? A complete list of all our Power Query blogs can be found [here](https://www.sumproduct.com/thought/power-query-blog-series)
. Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-start-and-end-with-grouping/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-start-and-end-with-grouping/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-start-and-end-with-grouping/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-start-and-end-with-grouping/#0)

[](https://sumproduct.com/blog/power-query-start-and-end-with-grouping/#0 "close")

top