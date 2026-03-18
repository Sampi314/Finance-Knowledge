# Power Query: Pivot Problems

**Source:** https://sumproduct.com/blog/power-query-pivot-problems/

---

[Home](https://sumproduct.com/)

\> Power Query: Pivot Problems

*   January 12, 2021

Power Query: Pivot Problems
===========================

Power Query: Pivot Problems
===========================

13 January 2021

_Welcome to our Power Query blog. This week, I look at an example using a pivot._

I have some tent data, just for a change…

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-72-1.jpg)

I want to reorganise this data into separate columns for price, quantity and discount. I extract the data to Power Query by using ‘From Table’ from the ‘Get & Transform’ section of the Data tab. I am only interested in the main table, not in the title at the top of the sheet.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-61-1.jpg)

I start by filling down on **Tent** so that all rows are populated. I can do this by selecting **Tent** and then right-clicking to select Fill and then Down.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-53-1.jpg)

I want to use ‘Pivot Columns’ from the Transform tab, as it will create new columns from the values in **Property**, which sounds like what I want.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-45-1.jpg)

I know the values for these columns are in **Amounts**, and that I don’t want to aggregate this data in any way.

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-36-1.jpg)

When I try to pivot, I get an error, which was not the plan. I take a closer look at the problem.

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-30-1.jpg)

The error message tells me that ‘There were too many elements in the numeration to complete the operation’. I can see that the error only occurs with tent type ‘Wedding’, so I delete the ‘Pivoted Column’ step and look again at my data.

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-27-1.jpg)

I have two entries for tent type ‘Wedding’ with different **Property** values. Since **Property** is being pivoted, this is giving me duplicate errors. I need to distinguish between these two entries outside of the data being pivoted. I need a new column. I want to pull out the price of the tent and include that in my **Tent** column. I start by adding a conditional column from the ‘Add Column’ tab.

![](<Base64-Image-Removed>)

I only want the amount to appear in my new column if it is the price of the tent.

![](<Base64-Image-Removed>)

I can now fill down on this column as I did for **Tent** earlier.

![](<Base64-Image-Removed>)

I will merge the **Tent** and **Price** columns from the Transform tab. The merge from the Transform tab does not keep the original columns, which is what I want in this particular case.

![](<Base64-Image-Removed>)

I select both columns in the order I want them to appear, and create an appropriate separator.

![](<Base64-Image-Removed>)

Now I can distinguish between the tents, so I pivot **Property** again.

![](<Base64-Image-Removed>)

This time I get my data in a format I can use.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-pivot-problems/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-pivot-problems/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-pivot-problems/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-pivot-problems/#0)

[](https://sumproduct.com/blog/power-query-pivot-problems/#0 "close")

top