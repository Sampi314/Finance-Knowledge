# Power Query: Next (Row) Once Again Please

**Source:** https://sumproduct.com/blog/power-query-next-row-once-again-please/

---

[Home](https://sumproduct.com/)

\> Power Query: Next (Row) Once Again Please

*   February 25, 2020

Power Query: Next (Row) Once Again Please
=========================================

Power Query: Next (Row) Once Again Please
=========================================

26 February 2020

_Welcome to our Power Query blog. This week, I look at yet another solution to my “February problem” referencing other rows._

John, my reliable imaginary salesperson, has been filling in data again. This time, I have some information on items purchased by customers in December:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-266.jpg)

He has decided to combine the item and the description in the same column, so I need to move the description into a separate column and remove the extra rows. Unlike the data for last week, this time one of the item codes does not have a description on the next line, so the two previous approaches (detailed [last week](https://www.sumproduct.com/blog/article/power-query-blogs/power-query-next-row-again-please)
 and the [week before](https://www.sumproduct.com/blog/article/power-query-blogs/power-query-next-row-please)
) won’t work.

This week, I look at a solution where I point to the table in the previous step.

I extract my data to Power Query using the ‘From Table’ option on the ‘Get & Transform’ section on the ‘Data’ tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-267-1.jpg)

My first step is to add an index to the table; I can do this from the ‘Add Column’ tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-252-1.jpg)

I choose to start the index from zero (0).

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-226-1.jpg)

I add a custom column from the ‘Add Column’ tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-195-1.jpg)

My new **_Description_** column will point to the **_Item Code/ Description_** value for the next row if **_Customer_** is _null_ on the next row.

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-173-1.jpg)

The **M** code I have used is:

**\= if #”Added Index”{\[Index\]+1} \[Customer\] = null then #”Added Index”{\[Index\]+1} \[#”Item Code/Description”\] else null**

**‘Added Index’** is the name of the previous step, and represents the table created at the previous step.

![](<Base64-Image-Removed>)

This looks good; now I just need to remove the rows where **_Customer_** is _null_.

![](<Base64-Image-Removed>)

Once I click ‘OK’, I should have all the data I need in each row.

![](<Base64-Image-Removed>)

I ‘Close & Load’ my data to Excel.

![](<Base64-Image-Removed>)

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-next-row-once-again-please/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-next-row-once-again-please/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-next-row-once-again-please/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-next-row-once-again-please/#0)

[](https://sumproduct.com/blog/power-query-next-row-once-again-please/#0 "close")

top