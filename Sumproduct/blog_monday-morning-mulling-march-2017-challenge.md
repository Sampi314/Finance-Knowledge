# Monday Morning Mulling: March 2017 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-march-2017-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: March 2017 Challenge

*   April 2, 2017

Monday Morning Mulling: March 2017 Challenge
============================================

Monday Morning Mulling: March 2017 Challenge
============================================

3 April 2017

Last week, we looked at a strange event – in certain cases when you are creating running totals, Power Query stores the number in strange ways. Let’s just recap quickly.

In this example, we have a calculation that is summing up the total bottles of wine that have been received in the last month, based on a number of shipments for several different vintages.

![](<Base64-Image-Removed>)

You can see that the SumTotal column is correctly adding up the running total of the number received, even considering that the rows are not ordered.

The next step involves expanding out the Table column on the right hand side. When this is done, look what happens to the running total:

![](<Base64-Image-Removed>)

Now, why does this happen? As it turns out, it’s a quirk in the way that Power Query is doing calculations. Remember that when Power Query downloads data, it only performs the calculations on a _preview_ of the dataset initially. Occasionally it gets lazy, and doesn’t perform the calculations properly across the dataset, resulting in the sort of error you see above.

We can stop this from happening by doing something that forces Power Query to load the entire table. A few different functions will do this (something like Reverse Rows would do the trick!), but you can use Table.Buffer to get Power Query to work. You can see this working with a simple table of random numbers. When we just add a column of random numbers using Number.Random, we get the following:

![](<Base64-Image-Removed>)

See how those random numbers have been calculated? However, when we add in an extra line using Table.Buffer, the calculations work properly:

![](<Base64-Image-Removed>)

Isn’t that strange! Now you know – don’t get caught out!

If you think you have a challenging problem that’s hard to solve, let us know, and maybe we’ll feature it in next month’s Final Friday Fix! Happy April everybody!

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-march-2017-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-march-2017-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-march-2017-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-march-2017-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-march-2017-challenge/#0 "close")

top