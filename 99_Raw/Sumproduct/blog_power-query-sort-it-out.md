# Power Query: Sort it Out

**Source:** https://sumproduct.com/blog/power-query-sort-it-out/

---

[Home](https://sumproduct.com/)

\> Power Query: Sort it Out

*   January 28, 2020

Power Query: Sort it Out
========================

Power Query: Sort it Out
========================

29 January 2020

_Welcome to our Power Query blog. This week, I look at sorting issues._

I have a very simple query:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-283.jpg)

I also have a simple goal: to sort my data by salesperson, and then show the latest visit date for each salesperson.

I begin by sorting by salesperson, which I can do using the arrow icon at the top of the **_Salesperson_** column.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-288.jpg)

I choose to sort in ascending order.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-272.jpg)

Next, I sort the visit date in descending order:

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-244-1.jpg)

I now have my data in order, so I can remove duplicate names by right-clicking on the **_Salesperson_** column.

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-210-1.jpg)

I choose to ‘Remove Duplicates’.

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-183-1.jpg)

I have one row for each **_Salesperson_**, but I don’t have the latest date for all the salespeople. The sort on date has not been preserved. In order to keep the order, I need an extra step before I remove duplicates: I need to add an index.

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-157-1.jpg)

On the ‘Add Column’ tab, I can add an ‘Index Column’. In this case, it doesn’t matter where I start the index; I choose to start at zero (0).

![](https://sumproduct.com/wp-content/uploads/2025/05/b9ee28d90e6b5bc92ea4aeafdad51628-126-1.jpg)

My data now has an index, so I try removing duplicate names again.

![](https://sumproduct.com/wp-content/uploads/2025/05/0485ccbc83bdeec1d741bad442a1ea5f-103-1.jpg)

This time I do have the latest date for each salesperson. When sorting on multiple columns, I can use an index column to preserve the order on my data whilst carrying out transformations on my data.

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-sort-it-out/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-sort-it-out/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-sort-it-out/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-sort-it-out/#0)

[](https://sumproduct.com/blog/power-query-sort-it-out/#0 "close")

top