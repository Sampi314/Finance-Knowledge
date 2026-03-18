# Power Query: Conditional Column Splitting

**Source:** https://sumproduct.com/blog/power-query-conditional-column-splitting/

---

[Home](https://sumproduct.com/)

\> Power Query: Conditional Column Splitting

*   January 29, 2019

Power Query: Conditional Column Splitting
=========================================

Power Query: Conditional Column Splitting
=========================================

30 January 2019

_Welcome to our Power Query blog. This week, I look at an example where one column contains both header and detail data._

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-494.jpg)

I have some tent data where the **_Tent Type_** column contains both header data, the tent size, and more detailed data, size and colour. I want to extract that data into two columns so that I have a size column, and a size and colour column.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-513.jpg)

My first step is to create a query by selecting ‘From Table’ on the ‘Get & Transform’ section of the ‘Data’ tab. The ‘Create Table’ box appears so that I can check the position of my table and indicate if there are headers.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-482.jpg)

In order to format my **_Price_** column correctly, I replace the nulls with zero (0), by right-clicking with the **_Price_** column selected and choosing the option ‘Replace Values’.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-445.jpg)

Next, I create two conditional columns, by using the ‘Conditional Column’ option on the ‘Add Column’ tab:

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-371.jpg)

and a second:

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-320.jpg)

Since the price is zero if **_Tent Type_** holds the tent size rather than the size and colour, I can use the value of **_Price_** to determine how to populate my new columns.

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-268.jpg)

I have my two columns, and now I can complete the values in **_Tent Size_** by right-clicking and choosing to fill down.

![](https://sumproduct.com/wp-content/uploads/2025/05/b9ee28d90e6b5bc92ea4aeafdad51628-225.jpg)

![](https://sumproduct.com/wp-content/uploads/2025/05/0485ccbc83bdeec1d741bad442a1ea5f-187.jpg)

I can now remove the rows where **_Price_** is zero or **_Tent Size and Colour_** is null by filtering on one of these columns – I choose **_Tent Size and Colour_**.

![](https://sumproduct.com/wp-content/uploads/2025/05/daf8c4f0259ce428269c0d3d4badd32b-139.jpg)

I filter using the ‘Text Select’ option, and choose to keep those rows which are not null.

![](<Base64-Image-Removed>)

I can delete the column **_Tent Type_** which is now a duplicate of **_Tent Size and Colour_**, and reorder my columns:

![](<Base64-Image-Removed>)

My tent data is now in the format that I need.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-conditional-column-splitting/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-conditional-column-splitting/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-conditional-column-splitting/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-conditional-column-splitting/#0)

[](https://sumproduct.com/blog/power-query-conditional-column-splitting/#0 "close")

top