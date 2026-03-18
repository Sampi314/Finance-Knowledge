# Power Pivot Principles: Credit Transactions

**Source:** https://sumproduct.com/blog/power-pivot-principles-credit-transactions/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Credit Transactions

*   March 15, 2021

Power Pivot Principles: Credit Transactions
===========================================

Power Pivot Principles: Credit Transactions
===========================================

16 March 2021

_Welcome back to the Power Pivot Principles blog. This week, we’ll continue where we left off last week, revealing “the truth” about the different negative and positive values._

To refresh your memory, I would like to first show you the results from [last week](https://www.sumproduct.com/blog/article/power-pivot-principles/power-pivot-principles-budget-vs-actuals)
, _viz._

![](<Base64-Image-Removed>)

Yes, I remember leaving you guys on a precipice. The values for some aggregations of the Budget data are negative, whereas they are positive for Actual’s data. The reason for this difference is that Actual transactions are recorded as absolute values. Wondering what to do next? Let me give a hint by refreshing your memory, _viz._

![](<Base64-Image-Removed>)

I know I made it obvious, but yes, the ‘**Is Credit**‘ column is going to help us determine the difference between negative and positive values. That is, credit transactions (determined by the ‘**Y**‘) should have negative values.

To incorporate for the credit transactions, I will create a new calculated column:

**\=IF(‘Transaction'\[Is Credit\]=”Y”,  
\-‘Transaction'\[Transaction\_Amount\],’Transaction'\[Transaction\_Amount\])**

![](<Base64-Image-Removed>)

I have named the column as **Actual\_Amount** and it looks like, _viz._

![](<Base64-Image-Removed>)

Now, I can replace the **Transaction\_Amount** with **Actual\_Amount** in my original table from last week.

![](<Base64-Image-Removed>)

Finally, my updated quarterly Budget vs Actuals table looks like, _viz._

![](<Base64-Image-Removed>)

That’s it for this week!

Come back next week to see how we use the disconnected table for performing a sensitivity analysis by staying tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-credit-transactions/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-credit-transactions/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-credit-transactions/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-credit-transactions/#0)

[](https://sumproduct.com/blog/power-pivot-principles-credit-transactions/#0 "close")

top