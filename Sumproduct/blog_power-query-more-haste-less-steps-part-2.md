# Power Query: More Haste Less Steps Part 2

**Source:** https://sumproduct.com/blog/power-query-more-haste-less-steps-part-2/

---

[Home](https://sumproduct.com/)

\> Power Query: More Haste Less Steps Part 2

*   April 26, 2022

Power Query: More Haste Less Steps Part 2
=========================================

Power Query: More Haste Less Steps Part 2
=========================================

27 April 2022

_Welcome to our Power Query blog. This week I look again at a query with too many steps._

[Last time](https://sumproduct.com/blog/power-query-more-haste-less-steps-part-1/)
, I looked at a **Dates** query:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-37-1.jpg)

I deliberately went the long way round to create this query! Ignoring the first three \[3\] steps, it has taken me 12 steps to achieve my goal. This time I will look at how I could have achieved the same result with less steps, whilst still using the User Interface (UI).

The first task was to create a **Month Name** column with a short month name format. Last time, this took six \[6\] steps. One of the reasons for this is that I used the Transform tab options, which meant I had to duplicate columns to keep my original. Many functions exist on the Transform tab and the ‘Add Column’ tab for precisely this reason. Instead of duplicating a column like I did last time,

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-50-1.jpg)

I can go to the ‘Add Column’ tab, and add a column from the ‘Dates’ section:

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-38-1.jpg)

I can then add the **Month Name** column in one step.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-33-1.jpg)

This replaces the two \[2\] steps I took to achieve this last time. The next step is to change **Month Name** to show the first three \[3\] characters of the month. [Last time](https://sumproduct.com/blog/power-query-more-haste-less-steps-part-1/)
, I used ‘Split Column’ on the Transform tab to split the column ‘By Positions’, creating a ‘Split Column by Position’ step:

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-25-1.jpg)

This automatically generated a ‘Changed Type1’ step. I then had to delete the unwanted column, creating a ‘Removed Column’ step and rename the one I wanted to keep to ‘month’, creating a ‘Renamed Column1’ step:

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-21-1.jpg)

Would it surprise you to learn that I could create a column containing the short name in one step? This time, the Transform tab is the most appropriate:

![](<Base64-Image-Removed>)

Instead of splitting the column, I can simply transform this column using ‘Extract First Characters’:

![](<Base64-Image-Removed>)

This gives me the new format for **Month Name** in one step:

![](<Base64-Image-Removed>)

Next time, I’ll look at how I can improve the functionality used to create a **Quarter** column in my required format.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-more-haste-less-steps-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-more-haste-less-steps-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-more-haste-less-steps-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-more-haste-less-steps-part-2/#0)

[](https://sumproduct.com/blog/power-query-more-haste-less-steps-part-2/#0 "close")

top