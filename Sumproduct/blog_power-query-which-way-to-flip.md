# Power Query: Which Way to Flip

**Source:** https://sumproduct.com/blog/power-query-which-way-to-flip/

---

[Home](https://sumproduct.com/)

\> Power Query: Which Way to Flip

*   July 28, 2020

Power Query: Which Way to Flip
==============================

Power Query: Which Way to Flip
==============================

29 July 2020

_Welcome to our Power Query blog. This week, I look at transposing versus unpivoting data._

It can be confusing when deciding how to manipulate data, particularly when the options may sound similar:

*   **Transposing data:** this essentially treats rows as columns and columns as rows. The original column names are not used, so transposing a table twice just removes the column names and leaves generic column headings such as ‘Column1’
*   **Unpivoting data:** this takes any selected column and translates it into attribute-value pairs. Therefore, if I have a column headed ‘Tents’ with Small, Medium and Large as values, I will get two columns, one with Tents as every value (the Attribute column) and one with the Small, Medium and Large values. The column names are not preserved. If I unpivot twice, then I get a new attribute column with ‘Attribute’ and ‘Value’ as the value and a new value column with all the values from the previous columns, _i.e._ Tents, Small, Tents, Medium, Tents, Large.

What I need, is an example!

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-173-1.jpg)

I have some tent data, but it’s not in a table format. I need to start by extracting my data to Power Query by using ‘From Table’ on the ‘Get & Transform’ section of the Data tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-161-1.jpg)

I don’t click that my data has headers, as that is not how the data is currently organised.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-154-1.jpg)

I start by transposing my data. I can do this from the Transform tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-136-1.jpg)

This has sorted out my first two columns, which now contain the supplier and tent type data respectively. The order numbers are all along the top row, which is not what I want. I need to unpivot my order data. First, however, I need to get my order numbers into the column headings, as I know that unpivoting will create a column of my headings next to the values.

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-115-1.jpg)

I use ‘Promote first Row as Headers’ from the Transform tab.

![](<Base64-Image-Removed>)

I have my order data ready to unpivot, and I need to select all the columns with order numbers and the **Order Number** column, and unpivot them from the Transform tab:

![](<Base64-Image-Removed>)

It’s quicker to choose the first two columns and then unpivot the rest.

![](<Base64-Image-Removed>)

I can now fill down the **Supplier** column by right-clicking and choosing ‘Fill’ and then ‘Fill Down’.

![](<Base64-Image-Removed>)

I rename my headings and change the type on my currency column to finish my table.

![](<Base64-Image-Removed>)

From this example, I notice that before transposing, I must make sure that no data I want is in the headings, as I will lose it. Conversely, if I unpivot, the data in the headings is used, so before unpivoting I need to check the data that I want to appear as a column is in the headings.

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-which-way-to-flip/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-which-way-to-flip/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-which-way-to-flip/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-which-way-to-flip/#0)

[](https://sumproduct.com/blog/power-query-which-way-to-flip/#0 "close")

top