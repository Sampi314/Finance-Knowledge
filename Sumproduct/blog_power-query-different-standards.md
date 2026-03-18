# Power Query: Different Standards

**Source:** https://sumproduct.com/blog/power-query-different-standards/

---

[Home](https://sumproduct.com/)

\> Power Query: Different Standards

*   November 27, 2018

Power Query: Different Standards
================================

Power Query: Different Standards
================================

28 November 2018

_Welcome to our Power Query blog. This week, I look at the differences in the way that the ‘Standard’ button works on the ‘Transform’ and ‘Add Column’ tabs._

Last week I looked at the ‘Merge Column’ functionality and the current differences between the way it works on the ‘Transform’ and ‘Add Column’ tabs. This time I will look at the ‘Standard’ option available on these tabs for numeric columns. In this case, there are reasons why the standard option behaves differently for each tab.

I will start with some simple data, and I am going to focus on the price. In the ‘Transform’ tab, I can modify my price column using ‘Standard’ options:

![](<Base64-Image-Removed>)

I can choose to apply a ‘Standard’ reduction by multiplying my prices by 0.9.

![](<Base64-Image-Removed>)

This will change the existing column.

![](<Base64-Image-Removed>)

However, I have decided I want to keep my existing column, and see discounted prices in a new column. In this case, I should use the ‘Add Column’ tab instead:

![](<Base64-Image-Removed>)

The process looks the same as for the ‘Transform’ tab, until I come to enter the value used for multiplication. I see I have the option to use values from a column as an alternative to using a fixed value. This was not available in the ‘Transform’ tab. I use a fixed value for now, and complete my action. I would have liked the option to name my new column, but I can change it later.

![](<Base64-Image-Removed>)

A new column **_Multiplication_** has appeared. If I rename this to ‘Sale Price’ I can see both of my prices:

![](<Base64-Image-Removed>)

Since I was given the option to select values from a column as part of the ‘Standard’ multiplication functionality, I try selecting two numeric columns to see what options are available on ‘Standard’.

![](<Base64-Image-Removed>)

Having selected **_Price_** and **_Quantity_**, I have the option of creating a new column by combining the values in my selected columns. I can perform all the ‘Standard’ operations with the exception of ‘Percentage’.

![](<Base64-Image-Removed>)

I opt to multiply my columns and create a new column which I rename to show the potential returns if I sell all my stock at pre-sales prices. I can create another column from the **_Sale Price_** and **_Quantity_** to show the effects of the proposed sale.

![](<Base64-Image-Removed>)

Whereas the ‘Standard’ option from the ‘Transform’ column enables me to perform simple operations on a numeric column, the ‘Standard’ option from the ‘Add Column’ tab may be used to combine data from more than one column, and present my results whilst still showing the original data. Some ‘Standard’ options are even available for more than two columns.

![](<Base64-Image-Removed>)

This can be a quick way to create a new column via addition or multiplication without creating a custom column.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-different-standards/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-different-standards/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-different-standards/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-different-standards/#0)

[](https://sumproduct.com/blog/power-query-different-standards/#0 "close")

top