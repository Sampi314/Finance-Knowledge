# Power Query: More Room for a View

**Source:** https://sumproduct.com/blog/power-query-more-room-for-a-view/

---

[Home](https://sumproduct.com/)

\> Power Query: More Room for a View

*   May 26, 2020

Power Query: More Room for a View
=================================

Power Query: More Room for a View
=================================

27 May 2020

_Welcome to our Power Query blog. This week, I continue my look at some new additions to the View tab, which are still not available on all versions of Power Query. Today, I look at ‘Column Profile’ and ‘Column Quality’._

_As I mentioned [last week](https://www.sumproduct.com/blog/article/power-query-blogs/power-query-room-for-a-view)
, I have been waiting since last year for this to hit my version of Power Query, but as yet it is only available in some versions. It is however available in Power BI – where the View tab has some interesting new features._

**_Column Profile_**

If you tick the ‘Column Profile’ box, then for the column selected, you will see information at the bottom of the screen:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-212-1.jpg)

One thing that become apparent from this data is the count. The count is 1,000, but the data I have has many more rows than that. Currently, the new column analysis functionality only samples the first 1,000 rows by default. I can change this by left-clicking at the bottom of the screen, where it currently says ‘column profiling based on top 1000 rows’.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-204-1.jpg)

I can change this to profile ‘…based on entire data set’:

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-197-1.jpg)

This information varies slightly depending upon the Data Type of the column. The previous screen is for a date column, whereas the next screen is for a text column.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-173-1.jpg)

I have an ‘Empty string’ count and no average. Empty string is “”, whereas empty is _null_. I have lots of _null_ rows, which is why there are two values, but _null_ is not considered to be the minimum value. Another point to note is that I am no longer filtering on **Custom**, but now I can see the column distribution data! It seems that if I access the other column analysis data first, I am able to see the distribution data too without filtering as long as the datatype is not ‘Any’.

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-147-1.jpg)

There is also an option to group by text length for text columns. This changes into a bar chart which is not a great option in such a small display pane though.

![](<Base64-Image-Removed>)

This also keeps a bar chart format if I move to a numeric column.

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-109-1.jpg)

In the numeric column, I have the option of grouping by value or sign.

![](https://sumproduct.com/wp-content/uploads/2025/05/b9ee28d90e6b5bc92ea4aeafdad51628-86-1.jpg)

In a date column, I can group by Value, Year, Month, Day, Week of the Year or Day of the Week.

![](https://sumproduct.com/wp-content/uploads/2025/05/0485ccbc83bdeec1d741bad442a1ea5f-71-1.jpg)

I can also choose to filter by specific values, by selecting a bar and right clicking.

**_Column Quality_**

If I select the checkbox for ‘Column Quality’, I can see more data. I have unchecked the other column analysis boxes to make the column quality data clearer.

![](https://sumproduct.com/wp-content/uploads/2025/05/daf8c4f0259ce428269c0d3d4badd32b-53-1.jpg)

There are three coloured dots: one for valid, one for errors and one for empty.

The errors are those recognised by Power Query, and empty means a blank or _null_ entry, ‘valid’ denoting the rest. The values are given as percentages, but if I hover over the quality for a particular column, I can see the number of rows for each category:

![](https://sumproduct.com/wp-content/uploads/2025/05/22c6daeb82d7d69ac88f878227e04b28-38-1.jpg)

_There is a suggestion to improve quality if that is possible, which for my example is ‘Remove Empty’._

_In summary, there are some inconsistencies with the way the analysis data appears, but it is a good start, which will hopefully be improved on in future releases, and installed in all versions of Power Query._

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-more-room-for-a-view/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-more-room-for-a-view/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-more-room-for-a-view/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-more-room-for-a-view/#0)

[](https://sumproduct.com/blog/power-query-more-room-for-a-view/#0 "close")

top