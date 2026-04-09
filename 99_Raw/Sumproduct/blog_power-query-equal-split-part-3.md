# Power Query: Equal Split Part 3

**Source:** https://sumproduct.com/blog/power-query-equal-split-part-3/

---

[Home](https://sumproduct.com/)

\> Power Query: Equal Split Part 3

*   January 23, 2024

Power Query: Equal Split Part 3
===============================

Power Query: Equal Split Part 3
===============================

24 January 2024

_Welcome to our Power Query blog. Today, I look at a slightly different problem where I need to divide amounts over rows._

Over the last two \[2\] blogs, I have been looking at an issue that Mary, my top imaginary salesperson had. She had some accounting data, which she needed to split equally for two suppliers:

![](<Base64-Image-Removed>)

In [Part 1](https://sumproduct.com/blog/power-query-equal-split/)
, I created two queries:

![](<Base64-Image-Removed>)

I looked at a simple way to achieve the result I want, which assumes that I always have two suppliers:

![](<Base64-Image-Removed>)

[Last time](https://sumproduct.com/blog/power-query-equal-split-part-2/)
, I refined this solution to make it more flexible, by using a parameter for the number of suppliers:

![](<Base64-Image-Removed>)

This time, I am going to look at a slightly difference scenario. I still begin with the same accounting data, but this time, there are no suppliers to link to.

![](<Base64-Image-Removed>)

I will split the rows into two \[2\] equal parts. I already have the query I extracted in [Part 1](https://sumproduct.com/blog/power-query-equal-split/)
:

![](<Base64-Image-Removed>)

I am going to take a reference copy, because I want my new query to be updated when **Accounts** is updated.

![](<Base64-Image-Removed>)

I call the new query **AccountsNoSupplier**:

![](<Base64-Image-Removed>)

I begin by selecting **Name** and **Month**, and right-clicking to ‘Fill Down’:

![](<Base64-Image-Removed>)

This gives me my tidy query:

![](<Base64-Image-Removed>)

There is no other table to link to duplicate the rows. Instead, I will use another method. As I know I will have two rows for this example, I start in the Transform tab, where I divide the **Amount** column using the Standard dropdown:

![](<Base64-Image-Removed>)

I choose to divide by two \[2\]:

![](<Base64-Image-Removed>)

This gives me half the amount on each row. Next, on the ‘Add Column’ tab, I create a ‘Duplicate Column’:

![](<Base64-Image-Removed>)

I select **Amount** and **Amount-Copy**, and on the Transform tab, I choose to ‘Unpivot Columns’:

![](<Base64-Image-Removed>)

This gives me extra rows:

![](<Base64-Image-Removed>)

I can tidy up my data, and I have the amounts split over two \[2\] columns for each **Expense Type**:

![](<Base64-Image-Removed>)

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-equal-split-part-3/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-equal-split-part-3/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-equal-split-part-3/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-equal-split-part-3/#0)

[](https://sumproduct.com/blog/power-query-equal-split-part-3/#0 "close")

top