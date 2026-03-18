# Charts and Dashboards: The Point and Figure Chart – Part 3

**Source:** https://sumproduct.com/blog/charts-and-dashboards-the-point-and-figure-chart-part-3/

---

[Home](https://sumproduct.com/)

\> Charts and Dashboards: The Point and Figure Chart – Part 3

*   August 3, 2023

Charts and Dashboards: The Point and Figure Chart – Part 3
==========================================================

Charts and Dashboards: The Point and Figure Chart – Part 3
==========================================================

4 August 2023

_Welcome back to our Charts and Dashboards blog series. This week, we continue to explain how to create a bespoke Point and Figure chart by looking at how we use the prepare data to transform the chart data._

_**Transform Data**_

The next thing we need to do is to create another table called **Transform\_Data** to summarise our index Data. The first column of the new table will be called **Unique Index**. The length of this column will be the maximum number of the **Index** column in the **Data** Table. Thus, we have a nice table with a single column as follows:

![](<Base64-Image-Removed>)

Next, we will add the **Date** column for this table where it will get the reversal date for these Index with the following formula:

**\=INDEX(Data\[Date\],MATCH(\[@\[Unique Index\]\],Data\[Index\],1))**

![](<Base64-Image-Removed>)

This part of the formula **MATCH(\[@\[Unique Index\]\],Data\[Lag Index\],1)** will try to match the largest value of the index first then it will go for the smallest. As the way we structure our **Lag****Index** column in **Data Table**, this formula will look through the data from bottom to top and it will stop at the first match it found. Then the **INDEX** function will help us get that date which is the end date of the stock price having an up or down direction. If some users seek to look for the start date of stock price having up or down direction, they can apply the following formula for the column:

**\=INDEX(Data\[Date\],MATCH(\[@\[Unique  \
Index\]\],Data\[Index\],0))**

Next, we need to add two \[2\] column which is **Min** and **Max** columns for the **Transform\_Data** Table we have. We will need to find the maximum and minimum adjusted stock price for the given index. Hence, we employ the following formula:

**\=MAX(IF(\[@\[Unique Index\]\]=Data\[Index\],Data\[Adj  \
Close\]),**

 **IF(\[@\[Unique  \
Index\]\]=Data\[Lag Index\],Data\[Adj Close\]))**

The **IF** function inside the **MAX** function will get all the stock prices that have the same **Index** and **Lag Index** then the **MAX** function will return a single maximum value for that index.

![](<Base64-Image-Removed>)

Similarly, we can do the same for the **Min** column:

**\=MIN(IF(\[@\[Unique Index\]\]=Data\[Index\],Data\[Adj Close\]),**

 **IF(\[@\[Unique Index\]\]=Data\[Lag  \
Index\],Data\[Adj Close\]))**

We are now ready to plot this chart!!!

That’s it for this week. Check back next week for more Charts and Dashboards tips.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/charts-and-dashboards-the-point-and-figure-chart-part-3/#0)
    
*   [Register](https://sumproduct.com/blog/charts-and-dashboards-the-point-and-figure-chart-part-3/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/charts-and-dashboards-the-point-and-figure-chart-part-3/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/charts-and-dashboards-the-point-and-figure-chart-part-3/#0)

[](https://sumproduct.com/blog/charts-and-dashboards-the-point-and-figure-chart-part-3/#0 "close")

top