# Final Friday Fix: March 2019 Challenge

**Source:** https://sumproduct.com/blog/final-friday-fix-march-2019-challenge/

---

[Home](https://sumproduct.com/)

\> Final Friday Fix: March 2019 Challenge

*   March 28, 2019

Final Friday Fix: March 2019 Challenge
======================================

Final Friday Fix: March 2019 Challenge
======================================

29 March 2019

_On the final Friday of each month, we’re going to set an Excel challenge for you to puzzle over so that you can get your “Excel fix”. Challenge your office colleagues to see who can solve the puzzle quickest. There’s no prizes at this stage, you’re playing for bragging rights only!_

**Confusing Column Names with Power Query and Power Pivot**

Welcome to this week’s Friday Fix. This week we are pulling inspiration from our consulting work, this being related to a task that we’ve been asked to do as part of our consulting business.

The problem here relates to how Excel, Power Query and Power Pivot handles a table with similar column names. The premiss here is that we can normally import data from Excel into Power Query, make a couple of data transformations then export the data to Power Pivot to create measures and other calculations with the data table.

Let’s just jump right into our example, assume we have the following table:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-461.jpg)

We import this data table into Power Query:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-476.jpg)

The next step, say we wish to export the data from Power Query into a table in Excel:

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-447.jpg)

… no problems here so far.

Now let’s try to add the data into the data model in Power Pivot. Excel returns with this error message:

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-414.jpg)

‘We couldn’t get data from the Data Model. Here’s the error message we got:

Duplicate column ‘\[Column Name\]’ in the rowset.  
An error occurred while processing table ‘\[Table Name\]’.  
The current operation was cancelled because another operation in the transaction failed.

This leaves us in a sticky a tricky situation as our data table did not have any duplicate columns, did it? So how do we go about fixing this?

This is the challenge this week: can you find a solution that will allow you to circumvent this error in Excel when adding the table above into the data model in Power Pivot?

_Sound easy? Have a go. We’ll publish what we think is the best solution in Monday’s blog. Have a great weekend!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/final-friday-fix-march-2019-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/final-friday-fix-march-2019-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/final-friday-fix-march-2019-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/final-friday-fix-march-2019-challenge/#0)

[](https://sumproduct.com/blog/final-friday-fix-march-2019-challenge/#0 "close")

top