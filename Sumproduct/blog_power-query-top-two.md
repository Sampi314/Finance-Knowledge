# Power Query: Top Two

**Source:** https://sumproduct.com/blog/power-query-top-two/

---

[Home](https://sumproduct.com/)

\> Power Query: Top Two

*   May 12, 2020

Power Query: Top Two
====================

Power Query: Top Two
====================

13 May 2020

_Welcome to our Power Query blog. This week, I look at splitting my data into the top two (for example) and the rest._

I have some data from my imaginary salespeople that I used in [Power Query: Group Functions](https://sumproduct.com/blog/power-query-group-functions/)
.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-220.jpg)

This time, I want to give the commission total for 2019 to my two top salespeople, and then show an average for everyone else.

I start by extracting my data into Power Query, by using ‘From Table’ in the ‘Get & Transform’ section of the Data tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-213-1.jpg)

I need to find the total commission for each salesperson, so I use the grouping functionality on the ‘Transform’ tab. I group by **Salesperson** and sum the **Commission**.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-206-1.jpg)

I can now apply a descending sort on **Commission** to get my top two salespeople.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-181-1.jpg)

To get my top two salespeople, I can just take the top two rows.

_![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-155-1.jpg)_

I choose to use the ‘Keep Rows’ functionality on the Home tab. This is more flexible than removing the bottom rows, as I don’t have to specify how many rows to remove.

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-134-1.jpg)

I now have my top two, and I am going to convert my salespeople column to a list by using the ‘Convert to List’ functionality on the Transform tab. I will use this later to reassemble my data.

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-114-1.jpg)

I create my list:

![](https://sumproduct.com/wp-content/uploads/2025/05/b9ee28d90e6b5bc92ea4aeafdad51628-92-1.jpg)

I rename the step to create my list **TopTwo**. Now, I need to deal with the others. I create a new step which refers to the data before I removed the bottom columns.

![](https://sumproduct.com/wp-content/uploads/2025/05/0485ccbc83bdeec1d741bad442a1ea5f-74-1.jpg)

The **M** code I have used is:

_**\= #”Sorted Rows”**_

which accesses the data before I removed the bottom rows. This time, I need to remove the top rows using the remove rows functionality on the Home tab.

![](<Base64-Image-Removed>)

I remove the top two rows. To get the average to appear in each column, I will use grouping, but I need to group using a constant so that I can sum the commissions. To do this, I add a custom column from the ‘Add Column’ tab, which always has the same value. The value I am going to use is “Others”, viz.

![](<Base64-Image-Removed>)

I can now group my data from the Transform tab.

![](<Base64-Image-Removed>)

I group by **Custom** and create a new **Commission 2019** column (yes, I know we are in 2020!) which will contain the average.

_![](<Base64-Image-Removed>)_

I have my data for the others, so I rename the step to **Others** and rename **Custom** to **Salesperson**. I am now ready to reassemble my data.

As I did earlier, I create a step to get back to my full data before I removed any rows. This will allow me to keep any columns that do not directly pertain to the calculation, and makes the method more flexible.

![](<Base64-Image-Removed>)

I need to select those rows which are associated with my top two.

_![](<Base64-Image-Removed>)_

The **M** code I have used is:

_**\= Table.SelectRows(Custom2, each (List.Contains(TopTwo,\[Salesperson\])=true ))**_

![](<Base64-Image-Removed>)

This gives me the data for my top two. Now I need to add my ‘others’. I do this by merging my table to itself, and then changing the **M** code generated.

![](<Base64-Image-Removed>)

I check the **M** code generated.

![](<Base64-Image-Removed>)

I have the **M** code

_**\= Table.Combine({Custom3, Custom3})**_

I change this to

_**\= Table.Combine({Custom3, Others})**_

![](<Base64-Image-Removed>)

I now have my data in the form I wanted, with my top two salespeople and the others combined into one average commission.

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-top-two/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-top-two/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-top-two/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-top-two/#0)

[](https://sumproduct.com/blog/power-query-top-two/#0 "close")

top