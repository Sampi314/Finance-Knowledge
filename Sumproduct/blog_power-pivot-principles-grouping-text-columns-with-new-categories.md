# Power Pivot Principles: Grouping Text Columns with New Categories

**Source:** https://sumproduct.com/blog/power-pivot-principles-grouping-text-columns-with-new-categories/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Grouping Text Columns with New Categories

*   June 17, 2019

Power Pivot Principles: Grouping Text Columns with New Categories
=================================================================

Power Pivot Principles: Grouping Text Columns with New Categories
=================================================================

18 June 2019

_Welcome back to our Power Pivot blog. Today, we will use the SEARCH and SWITCH functions to create custom columns that group text columns into new categories._

Last week, we covered the **SEARCH** function and we used it to identify text strings within a column, you can read more about it [here](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-search-function)
. This week, we are going to combine the **SEARCH** function with the **SWITCH** function to demonstrate a potential use case. You can read more about the **SWITCH** function [here](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-switch-function)
.

Let’s look at a similar data table to the one used last week:

![](<Base64-Image-Removed>)

Our task now is to create a new column that works as a new subcategory for each of the products. For example, if we want the new column to classify Business Shoes as Footwear, we would use the following **IF** function:

\=IF(

SEARCH(

“Shoe”,\[Product Type\],,0)>0,

“Footwear”,

“”

)

This creates the following calculated column as follows:

![](<Base64-Image-Removed>)

If we wanted to include Casual Slippers, we would have to use a nested **IF** statement:

\=IF(

SEARCH(

“Shoe\*”,\[Product Type\],,0)>0,

“Footwear”,

IF(

SEARCH(

“Slipper?”, \[Product Type\],,0)>0,

“Footwear”,

“”

)

)

![](<Base64-Image-Removed>)

But what if we wanted to reclassify Gloves and Belts as Clothing? It would result in a potentially nasty nested **IF** statement! As we hinted earlier in this blog, we can use the **SWITCH** function together with the **SEARCH** function instead:

\=SWITCH(

TRUE(),

SEARCH(

“Shoe\*”,\[Product Type\],,0)>0,

“Footwear”,

SEARCH(

“Slippers\*”,\[Product Type\],,0)>0,

“Footwear”,

SEARCH(

“Gloves\*”,\[Product Type\],,0)>0,

“Clothing”,

SEARCH(

“Belt\*”,\[Product Type\],,0)>0,

“Clothing”

)

![](<Base64-Image-Removed>)

In this case, we have to use **TRUE** as the expression so that as the function cycles through each row the expression will be ‘true’, so it will perform the subsequent searches for each row. I f we do not use the **TRUE** function as the expression, we will get the following error message:

![](<Base64-Image-Removed>)

That’s it for this week, until next time, happy pivoting!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-grouping-text-columns-with-new-categories/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-grouping-text-columns-with-new-categories/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-grouping-text-columns-with-new-categories/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-grouping-text-columns-with-new-categories/#0)

[](https://sumproduct.com/blog/power-pivot-principles-grouping-text-columns-with-new-categories/#0 "close")

top