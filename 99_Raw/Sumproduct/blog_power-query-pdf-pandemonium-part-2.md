# Power Query: PDF Pandemonium – Part 2

**Source:** https://sumproduct.com/blog/power-query-pdf-pandemonium-part-2/

---

[Home](https://sumproduct.com/)

\> Power Query: PDF Pandemonium – Part 2

*   September 21, 2021

Power Query: PDF Pandemonium – Part 2
=====================================

Power Query: PDF Pandemonium – Part 2
=====================================

22 September 2021

_Welcome to our Power Query blog. This week, I start to transform some data from a PDF file._

The tent business is doing well, and the UK division have plans to expand the workforce. I have a PDF file, and it contains tables for 10 stores. [Last week](https://sumproduct.com/blog/power-query-pdf-pandemonium-part-1/)
, I imported my data, _viz._

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-132.jpg)

The key to making my transformations as immune to change as possible is to keep the data I need rather than delete the data I don’t. Looking at the columns, the easiest way to see if there is any useful data in there is to use the filter icon; **Column1** is clearly very useful.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-175.jpg)

However, **Column8** is not:

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-141.jpg)

However, rather than delete **Column8**, I should keep what I need. On the Home tab, there is an option to ‘Choose Columns’:

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-138.jpg)

I can use this to specify columns I want to keep. It’s much easier than selecting them all for large tables!

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-113.jpg)

I choose to select the first seven \[7\] columns.

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-99.jpg)

I can see that the heading data from the tables is in **Column1**, which suggests that transposing my data would be useful. I can do this from the Transform tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-91.jpg)

This swaps the rows and the columns and is much closer to the format I want to see.

![](https://sumproduct.com/wp-content/uploads/2025/05/b9ee28d90e6b5bc92ea4aeafdad51628-76.jpg)

I can check the data in my columns again to see which ones I want to keep. However, it is clear that this time the column names will change with the extra text that is present in my source data.

![](https://sumproduct.com/wp-content/uploads/2025/05/0485ccbc83bdeec1d741bad442a1ea5f-68.jpg)

Before I decide which columns to keep, I need some way of identifying them. I will promote the first column to the column headings, which I can do from the Transform Tab.

![](<Base64-Image-Removed>)

I choose ‘Use First Row as Headers’:

![](<Base64-Image-Removed>)

Power Query has created a ‘Changed Type’ step, but this references column names, so I delete it. I can pick the columns I want to keep in the same way as I did earlier.

![](<Base64-Image-Removed>)

I have the data I want to keep, but there are two tables in here: the store data and the pay scales.

![](<Base64-Image-Removed>)

I can keep this query, which I will call **All Data**, and make Reference queries: one for the store table and one for the pay scales table. I can create reference queries from the ‘Home’ tab.

![](<Base64-Image-Removed>)

I described the benefits of using reference queries in the blog [Reliable References](https://sumproduct.com/blog/power-query-reliable-references/)
. I call this Reference Query **Pay Scales**.

![](<Base64-Image-Removed>)

I also create another Reference Query, **Stores**. I will transform **Pay Scales** next time…

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-pdf-pandemonium-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-pdf-pandemonium-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-pdf-pandemonium-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-pdf-pandemonium-part-2/#0)

[](https://sumproduct.com/blog/power-query-pdf-pandemonium-part-2/#0 "close")

top