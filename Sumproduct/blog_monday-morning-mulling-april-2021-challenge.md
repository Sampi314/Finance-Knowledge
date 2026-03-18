# Monday Morning Mulling: April 2021 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-april-2021-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: April 2021 Challenge

*   May 2, 2021

Monday Morning Mulling: April 2021 Challenge
============================================

Monday Morning Mulling: April 2021 Challenge
============================================

3 May 2021

_On the final Friday of each month, we set an Excel / Power Pivot / Power Query / Power BI problem for you to puzzle over for the weekend. On the Monday, we publish a solution. If you think there is an alternative answer, feel free to email us. We’ll feel free to ignore you._

This month, we want to check if a pair of values are of the same category.

**_The Challenge_**

Excel poses a challenge when it comes to categorical data. To identify commonality in different values within different categories can somewhat be difficult on occasion. For instance, I came across a dataset that shows which social media channels certain staff members use:

![](<Base64-Image-Removed>)

Imagine that this data set goes on to for 1,000 rows. Using this data set as a proxy, how hard it is to identify if a pair of users have a common social media channel?

The challenge was “simply” this: could you write a formula to potentially create a list of pairs that use a common social media channel. This must be done in one cell. We even supplied a [starter file](https://sumproduct.com/assets/blog-pictures/2021/fff-mmm/apr/fff/friday-fix-starter-file.xlsx)
 for you!

**_Suggested Solution_**

To start off with, we need to identify what platforms each staff member uses. We will create two lists of social media channel that are to be used to compare both users. I will first start with the ‘User A’ (Hanh). Using the **FILTER** dynamic array function, I will create a dynamic array in **G7** using the following formula

**\=FILTER(Table1\[Category\],Table1\[Value\]=H2)**

![](<Base64-Image-Removed>)

As expected, the only platform ‘User A’ uses is LinkedIn. Now moving to ‘User B’ (Jonathan), I transpose the list of social media channels to create an array in **H6** using

**\=TRANSPOSE(FILTER(Table1\[Category\],Table1\[Value\]=H3))**

![](<Base64-Image-Removed>)

From the data, ‘User B’ uses LinkedIn, Discord, and Instagram.

Now the question is, how do we pair up the list? The answer is simple: we just check if list A equals list B in **H7** by using the following formula

**\=FILTER(Table1\[Category\],Table1\[Value\]=H2)=TRANSPOSE(FILTER(Table1\[Category\],Table1\[Value\]=H3))**

![](<Base64-Image-Removed>)

Now we finally check if the users share a social media channel in **H4** using

**\=MAX((FILTER(Table1\[Category\],Table1\[Value\]=H2)=TRANSPOSE(FILTER(Table1\[Category\],Table1\[Value\]=H3)))\*1)=1**

![](<Base64-Image-Removed>)

There it is! For my satisfaction I will try a different user by changing cell **E3** and I get the following

![](<Base64-Image-Removed>)

Thankfully, it works! You have a check that displays if a pair of users are active on a social media cannel.

You can find the sample file [here](https://sumproduct.com/assets/blog-pictures/2021/fff-mmm/apr/mmm/monday-morning-mulling-april-2021-challenge.xlsx)
.

Until next month!

_The Final Friday Fix will return on Friday 28 May 2021 with a new Excel Challenge. In the meantime, please look out for the Daily Excel Tip on our home page and watch out for a new blog every business workday._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-april-2021-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-april-2021-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-april-2021-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-april-2021-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-april-2021-challenge/#0 "close")

top