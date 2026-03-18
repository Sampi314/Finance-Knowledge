# Power Query: If You Can’t Tell Them Apart, Join Them

**Source:** https://sumproduct.com/blog/power-query-if-you-cant-tell-them-apart-join-them/

---

[Home](https://sumproduct.com/)

\> Power Query: If You Can’t Tell Them Apart, Join Them

*   October 10, 2017

Power Query: If You Can’t Tell Them Apart, Join Them
====================================================

Power Query: If You Can’t Tell Them Apart, Join Them
====================================================

11 October 2017

_Welcome to our Power Query blog. This week I look at how to merge queries to compare two similar lists._

Sometimes, the tasks I have to do are less than thrilling. I could be given two long lists of employees, and told to find who is missing from each list:

![](https://sumproduct.com/wp-content/uploads/2025/05/972f797e7bacbfe7f0cf399a37cc97cb.jpg)

With Power Query, there is an easy way to do this.

I have two lists of employees which look virtually identical, but of course they are not. The first step I take is to use Power Query to load my lists. I begin by creating my first query.

![](https://sumproduct.com/wp-content/uploads/2025/05/5df03b9caad7ea0ebf8ee43d48a73d39.jpg)

On the ‘POWER QUERY’ tab, I use the ‘From Table / Range’ option in the ‘Excel Data’ section. I can either convert my data into a table before I use this option or let Power Query do this as part of my query creation.

![](https://sumproduct.com/wp-content/uploads/2025/05/a46317382b05926d5069a83c527814ec.jpg)

My data appears in a new query, which I call ‘Employee Table 1’. I choose the ‘Close and Load to’ option on the ‘Close and Load’ section on the ‘Home’ tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/6fe0b108e803e912a9bfedf701ac843b.jpg)

I only want to create the connection as I am going to use my queries for comparison. Having created the first query, I repeat the process for the second employee list.

![](https://sumproduct.com/wp-content/uploads/2025/05/b6d6e238fdcfb259d6683e1419c52342.jpg)

My next step is to merge my queries and to do this I can right-click on one of my employee queries (I could have chosen to use the option from the ‘Combine’ section of the ‘POWER QUERY’ tab).

![](https://sumproduct.com/wp-content/uploads/2025/05/21e344e27037341191e44a75ef887926.jpg)

I select the ‘Merge’ option.

![](https://sumproduct.com/wp-content/uploads/2025/05/681f0b5ac7d027758dcec74e632aabfc.jpg)

In the ‘Merge’ screen, I specify the second employee table, and I see a preview of the data in both queries. I want to merge my tables completely, so I select all columns in both tables.

At the bottom of the screen I have the option to specify the ‘Join Kind’, and this will determine what data I see when the queries are merged.

I am interested in the joins that will either find my matching or missing data, which are the last three on the drop down. I will run through each option in turn.

**_‘Inner’_**

This will give me those employees that are on both lists. I pick this option first.

![](<Base64-Image-Removed>)

The rows I can see initially are those rows which match the criteria in the first table, and I have an extra column which is labelled ‘Employee Table 2’, which contains a table. I choose to expand the second table to see which rows match the criteria in the second table:

![](<Base64-Image-Removed>)

I don’t need to use any original column names as a prefix, so I uncheck that box and choose ‘OK’.

![](<Base64-Image-Removed>)

I have 42 employees in both tables.

**_‘Left Anti’_**

I opt to merge my tables again, and this time I pick join type ‘Left Anti’.

![](<Base64-Image-Removed>)

This time I am interested in the first table, since this will show me those employees in ‘Employee Table 1’ who are missing from ‘Employee Table 2’. I find four employees and two seem a little familiar… Notice Zoe, as she’ll come up again later…

Just to show that the second table will be empty (as I am looking for employees that don’t appear here), I expand the table _viz._

![](<Base64-Image-Removed>)

**_‘Right Anti’_**

My final choice is to create a merge with a ‘Right Anti’ join. In the Query Editor, this looks a little strange before I expand the table.

![](<Base64-Image-Removed>)

This is because I am seeing the results from the first table, and since I am looking for values that are in the second table and not in the first table, it is empty. I choose to expand the second table:

![](<Base64-Image-Removed>)

I have two employees that are missing from the first table – and it wouldn’t take too much investigation to discover that Zoe has changed her name from Green to Brown!

Want to read more about Power Query? A complete list of all our Power Query blogs can be found [here](https://www.sumproduct.com/thought/power-query-blog-series)
.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-if-you-cant-tell-them-apart-join-them/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-if-you-cant-tell-them-apart-join-them/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-if-you-cant-tell-them-apart-join-them/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-if-you-cant-tell-them-apart-join-them/#0)

[](https://sumproduct.com/blog/power-query-if-you-cant-tell-them-apart-join-them/#0 "close")

top