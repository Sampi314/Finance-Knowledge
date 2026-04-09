# Power Query: Emerging from Merging

**Source:** https://sumproduct.com/blog/power-query-emerging-from-merging/

---

[Home](https://sumproduct.com/)

\> Power Query: Emerging from Merging

*   November 12, 2019

Power Query: Emerging from Merging
==================================

Power Query: Emerging from Merging
==================================

13 November 2019

_Welcome to our Power Query blog. This week we look at extracting from merged Excel cells._

I have some data from John, one of my imaginary salespeople:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-328.jpg)

John has almost followed the expected format, but he’s decided to merge the date cells instead of using auto fill. I need the date on each row. I begin by extracting the data to Power Query by using the ‘From Table’ option on the ‘Get & Transform’ section of the Data tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-332.jpg)

I accept the defaults.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-317.jpg)

I can sort out my data by using ‘Fill Down’ which is available from the Transform tab or if I right click on a selected column, viz.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-291.jpg)

I select ‘Fill’ and ‘Down’.

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-249.jpg)

The dates are now populated correctly. However, there are other ways that John likes to merge cells in Excel:

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-222.jpg)

In this case he’s merged **Contact 1** and **Contact 2** for the dates, as well as merging the rows. I extract this data again into Power Query:

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-189.jpg)

I can see that the **Contact 2** column is currently redundant, so I will remove it using the ‘Remove Columns’ option on the Home tab and create a new one.

![](https://sumproduct.com/wp-content/uploads/2025/05/b9ee28d90e6b5bc92ea4aeafdad51628-156.jpg)

I can now fill down as before.

![](https://sumproduct.com/wp-content/uploads/2025/05/0485ccbc83bdeec1d741bad442a1ea5f-130.jpg)

I need to split **Contact 1**, so I use ‘Split Column’ from the Transform tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/daf8c4f0259ce428269c0d3d4badd32b-97-1.jpg)

I split by delimiter, but I need to create two new columns not three, so I won’t split for every occurrence of **SPACE**.

![](<Base64-Image-Removed>)

I choose to split at the ‘Right-most delimiter’.

![](<Base64-Image-Removed>)

Now I need to remove the ‘and’ from the names in **Contact 1.1**. There are several ways I can approach this. I can split the column again and delete the column with ‘and’. Another way is to create a custom column. In this example, I will use ‘Add Column by Examples’ on the ‘Add Column’ tab to see which method Power Query applies.

![](<Base64-Image-Removed>)

After only one example, Power Query has opted to transform the column so that only the characters before the **SPACE** delimiter appear:

\= TextBeforeDelimiter(\[Contact 1.1\],””)

![](<Base64-Image-Removed>)

I remove the column I no longer need and rename the contact information. I also reorder my data.

![](<Base64-Image-Removed>)

I now have the data in a standard format so that I can append it to data from other salespeople.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-emerging-from-merging/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-emerging-from-merging/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-emerging-from-merging/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-emerging-from-merging/#0)

[](https://sumproduct.com/blog/power-query-emerging-from-merging/#0 "close")

top