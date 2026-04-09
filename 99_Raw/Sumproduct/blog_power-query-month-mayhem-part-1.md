# Power Query: Month Mayhem – Part 1

**Source:** https://sumproduct.com/blog/power-query-month-mayhem-part-1/

---

[Home](https://sumproduct.com/)

\> Power Query: Month Mayhem – Part 1

*   July 2, 2024

Power Query: Month Mayhem – Part 1
==================================

Power Query: Month Mayhem – Part 1
==================================

3 July 2024

_Welcome to our Power Query blog.  Today, I look at an example where I need to realign some of the data._

My salespeople are back from their break and I have more reports to construct. I have a report with a list of the clients they have been working with each month:

![](https://sumproduct.com/wp-content/uploads/2025/05/3231ce84be1998fe02e718a01e5e1df3-1.jpg)

I would like to display the amount details in the salesperson sections but aligned to the relevant month at the top of the page:

![](https://sumproduct.com/wp-content/uploads/2025/05/e8a3dc433ac17d78d9d9a37b459bc043-1.jpg)

I will start in a new blank workbook and go to the ‘Get & Transform’ section on the Data tab, where I choose to use the ‘Get Data’ dropdown. I select ‘From File’ and then ‘From Excel Workbook’:

![](https://sumproduct.com/wp-content/uploads/2025/05/8625c684c4f5878021f9198be95cef92-1.jpg)

Having browsed to the source file, I choose to open it.

![](https://sumproduct.com/wp-content/uploads/2025/05/33e02cc49259acfd06f419d6659535bf-1.jpg)

In the Navigator screen, I can see that **Sheet1** contains the data. I click the ‘Transform Data’ button to bring my data into the Power Query editor:

![](https://sumproduct.com/wp-content/uploads/2025/05/d8934a2c05ceeae5a42d4365054f3f6f-1.jpg)

Power Query has performed some steps automatically for me. Since I will be using the column headers in a query later, I do not want to keep the ‘Promoted Headers’ step. I go to the ‘Promoted Headers’ step, and right-click to access the ‘Delete Until End’ option:

![](https://sumproduct.com/wp-content/uploads/2025/05/7a93f89a8612e65ec58aa241d1c9e578-1.jpg)

I receive a prompt to ensure I mean to delete all subsequent steps:

![](https://sumproduct.com/wp-content/uploads/2025/05/b7c26ed46bcba84f794c8237a27f8e8b-1.jpg)

I choose to Delete.

One of the challenges for this example, is to keep related data together, and ensure that I will be able to display it in the correct order. The best way to do this, is to create my own key by adding an index. From the ‘Add Column’ tab, I choose to add an ‘Index Column’ starting ‘From 1’:

![](<Base64-Image-Removed>)

I will need to create more than one key, and therefore more than one index. I change the name of the new column to **Source Full Index** to indicate that this index will help me to keep the order of the full data set.

![](<Base64-Image-Removed>)

Having recorded the position of the data, I need a way of keeping the sections of data together whilst I am transforming the data to move the amounts to different columns. I plan to use another key (index) for this.

I remove the subheading rows by filtering on the first column:

![](<Base64-Image-Removed>)

Having done this, I create another key. I add another index starting from one \[1\], and this time I call it **Section Index**:

![](<Base64-Image-Removed>)

Next time, I will recombine the data, and show how this will help me to identify the data in each section.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-month-mayhem-part-1/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-month-mayhem-part-1/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-month-mayhem-part-1/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-month-mayhem-part-1/#0)

[](https://sumproduct.com/blog/power-query-month-mayhem-part-1/#0 "close")

top