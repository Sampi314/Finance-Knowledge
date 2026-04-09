# Power Query: PDF Pandemonium – Part 3

**Source:** https://sumproduct.com/blog/power-query-pdf-pandemonium-part-3/

---

[Home](https://sumproduct.com/)

\> Power Query: PDF Pandemonium – Part 3

*   September 28, 2021

Power Query: PDF Pandemonium – Part 3
=====================================

Power Query: PDF Pandemonium – Part 3
=====================================

29 September 2021

_Welcome to our Power Query blog. This week, I continue transforming some data that is coming in from a PDF file._

The tent business is doing well, and the UK division have plans to expand the workforce. I have a PDF file, and it contains tables for 10 stores. [Last week](https://sumproduct.com/blog/power-query-pdf-pandemonium-part-2/)
, I created two Reference Queries, and this week I will continue transforming **Pay Scales.**

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-129.jpg)

I start by keeping the columns I will be needing for this table.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-172.jpg)

This means I can concentrate on the data I need to transform for this table.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-137.jpg)

Having checked the data, I actually only need the pay scale columns, so I select them whilst holding down the **CRTL** key and click on ‘Remove Other Columns’.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-135.jpg)

Power Query incorporates this into the existing ‘Remove Other Columns’ step.

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-110.jpg)

I can remove empty rows from the Home tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-97.jpg)

I can now look at how to transform my data from this into a useful table.

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-88.jpg)

I want to transpose the data, but if I do this with some of the data I need in the column headings, I will lose it. First, I need to demote the column headings so that I have the information in a row. I can do this from the Home tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/b9ee28d90e6b5bc92ea4aeafdad51628-73.jpg)

This creates a ‘Change Type’ step which I delete as I am not ready to decide column types yet. I am now ready to transpose my data, using the option on the Transform tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/0485ccbc83bdeec1d741bad442a1ea5f-65.jpg)

My data is starting to take shape.

![](https://sumproduct.com/wp-content/uploads/2025/05/daf8c4f0259ce428269c0d3d4badd32b-57.jpg)

I can rename the headings.

![](<Base64-Image-Removed>)

I want to show a start and end salary, rather than have the information in one column. I can split the **Salary** column from the Transform tab.

![](<Base64-Image-Removed>)

From the dropdown, I choose to split ‘By Delimiter’; this brings up a dialog.

![](<Base64-Image-Removed>)

I choose to split by space at each occurrence of a space, because this will give me a column with the lower and upper limit.

![](<Base64-Image-Removed>)

I delete the automated ‘Changed Type’ step again. I don’t need **Salary.2**, so I can remove this. As usual, I do this by selecting the columns I want to keep and ‘Remove Other Columns’.

![](<Base64-Image-Removed>)

I want **Salary.1** and **Salary.2** to be numeric columns, so I need to remove the £ signs. I can do this by selecting the columns and replacing £ with blank. I start by using ‘Replace Values’ on the Transform tab.

![](<Base64-Image-Removed>)

This provides a dialog where I can enter the details.

![](<Base64-Image-Removed>)

This will remove the £ signs.

![](<Base64-Image-Removed>)

Next, I change both columns to whole numbers. I can do this from the Home tab or the Transform tab, or by using the right-click menu, and changing the data type.

![](<Base64-Image-Removed>)

I get an error, but I can use ‘Replace Errors’ instead of ‘Replace Values’ this time.

![](<Base64-Image-Removed>)

I want to replace it with _null_, not zero \[0\], since zero is the starting point for ‘Pay Scale A’.

![](<Base64-Image-Removed>)

Next, I need to transform the **Percentage Increase** column. If I make it the data type Percentage, I will get values of over 100: I need to divide the values by 100 first, which I can do from the Transform tab, but first I change the data type to ‘Decimal Number’. This will allow me to access the ‘Standard’ dropdown.

![](<Base64-Image-Removed>)

I choose ‘Divide’ and enter 100 in the dialog.

![](<Base64-Image-Removed>)

I can now set the correct data types for all of the columns.

![](<Base64-Image-Removed>)

I rename the salary columns, and my table is ready to ‘Close & Load’.

![](<Base64-Image-Removed>)

Next time, I will look at the **Stores** query.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-pdf-pandemonium-part-3/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-pdf-pandemonium-part-3/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-pdf-pandemonium-part-3/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-pdf-pandemonium-part-3/#0)

[](https://sumproduct.com/blog/power-query-pdf-pandemonium-part-3/#0 "close")

top