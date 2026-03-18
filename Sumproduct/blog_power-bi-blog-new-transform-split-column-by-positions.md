# Power BI Blog: New Transform – Split Column by Positions

**Source:** https://sumproduct.com/blog/power-bi-blog-new-transform-split-column-by-positions/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: New Transform – Split Column by Positions

*   August 14, 2019

Power BI Blog: New Transform – Split Column by Positions
========================================================

Power BI Blog: New Transform – Split Column by Positions
========================================================

15 August 2019

_Welcome back to this week’s Power BI blog series. This week, we are going to look at a new transformation in Power BI: split column by positions._

In the [latest July updates](https://www.sumproduct.com/news/article/july-2019-updates-for-power-bi-desktop)
, Microsoft has just added a new data transformation to Power BI which allows users to split text columns at specific positions within a given text value. It may be found under the ‘Split Column’ menu in the ‘Home’ or ‘Transform’ tab of the Power Query Editor Ribbon.

![](<Base64-Image-Removed>)

The new Split Column by Position is extremely helpful when I have a data set such as the one below, where I want to extract information of both customer groups (indicated by the first capital letter) and customer names:

![](<Base64-Image-Removed>)

On clicking the ‘By Position’, an option pop-up dialog will appear. Here, in the ‘Positions’ box, I can specify a comma separated list of positions to split at: it could be one, two or however many positions by which I wish to split my column.

What’s interesting here is that it also tries to detect and give us recommendations for those positions based on data in preview rows within the Power Query Editor. (For your information, I did not put the number ‘0, 1, 6’ there – the software did!).

![](<Base64-Image-Removed>)

My data is now transformed as I expect in just one click!

![](<Base64-Image-Removed>)

Then, I rename the new columns and I only need to trim the texts contained in the ‘Customer Name’ column to get a cleaner data set:

![](<Base64-Image-Removed>)

Coming back to the ‘Split Column by Positions’, what if I want to split the text column into rows?

![](<Base64-Image-Removed>)

Clicking OK, I have this new data set, with text column split into rows, and all values in the ‘Sales’ column next to it will be duplicated.

![](<Base64-Image-Removed>)

That’s it for this week, check back next week for more Power BI tips.

In the meantime, please remember we offer training in Power BI which you can find out more about [\>here](https://www.sumproduct.com/courses)
. If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-new-transform-split-column-by-positions/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-new-transform-split-column-by-positions/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-new-transform-split-column-by-positions/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-new-transform-split-column-by-positions/#0)

[](https://sumproduct.com/blog/power-bi-blog-new-transform-split-column-by-positions/#0 "close")

top