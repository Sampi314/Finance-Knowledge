# Monday Morning Mulling: March 2019 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-march-2019-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: March 2019 Challenge

*   March 31, 2019

Monday Morning Mulling: March 2019 Challenge
============================================

Monday Morning Mulling: March 2019 Challenge
============================================

1 April 2019

On the final Friday of each month, we set an Excel problem for you to puzzle over for the weekend. On the Monday, we publish a solution. If you think there is an alternative answer, feel free to email us. We’ll feel free to ignore you.

Welcome to this month’s Monday Morning Mulling. Were you able to work around the error found in our last [blog](https://www.sumproduct.com/)
?

Last week we posted an interesting problem, where Power Pivot would return with an error when we loaded a table with two very similar columns in them.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-460.jpg)

Do note that these columns were accepted by Power Query and even successfully exported into a table in Excel.

So, how do we get around this?

The answer may surprise you. Change the column names! If you had not noticed, the original table had two very similar column names ‘Transaction Type’ and ‘Transaction type’:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-475.jpg)

The two columns were only distinguished by the capitalised ‘T’ in ‘type’. Power Pivot does not recognise the capitalization as a distinguishing factor, therefore treated both columns as duplicates.

The simple solution, change the column name:

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-446.jpg)

The column ‘Transaction type’ has been renamed to ‘Internal / External’. Let’s try to load this table into our Data Model:

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-413.jpg)

Success! We are now able to work with this data table in Power Pivot. So how did you go? Did you find a solution other than changing the column names? Let us know, we’d be keen to hear if you think you have a better way of circumventing this error. Otherwise, we’ll see you next month for our next Final Friday Fix!

_The Final Friday Fix will return on Friday 26April with a new Excel Challenge. In the meantime, please look out for the Daily Excel Tip on our home page and watch out for a new blog every business workday._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-march-2019-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-march-2019-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-march-2019-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-march-2019-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-march-2019-challenge/#0 "close")

top