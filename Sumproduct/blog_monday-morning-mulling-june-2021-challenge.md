# Monday Morning Mulling: June 2021 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-june-2021-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: June 2021 Challenge

*   June 27, 2021

Monday Morning Mulling: June 2021 Challenge
===========================================

Monday Morning Mulling: June 2021 Challenge
===========================================

28 June 2021

_On the final Friday of each month, we are going to set an Excel / Power BI challenge for you to puzzle over so that you can get your “Excel fix”. Challenge your office colleagues to see who can solve the puzzle quickest. There are no prizes at this stage: you are playing for bragging rights only!_

This month, we set a fairly straightforward challenge. Can you come up with a formula to give us a list of capabilities that each person in a team can provide?

In this instance, we have a list of employees where we know what division each person works in. We also have a list of capabilities that each employee brings to the team. If we select an employee, we’d like to know what their whole team brings to the table.

![](<Base64-Image-Removed>)

So to do this, we naturally follow some basic steps – what’s your employee’s name, and what division are they from? So simple, so **INDEX(MATCH()).**

\=INDEX(Table1\[Division\],MATCH(Employee\_Selection,Table1\[Employee\],0))

Then, we might even be able to find a list of all the employees that work in that division. That’s what **FILTER** is for, right?

\=FILTER(Table1\[Employee\],Table1\[Division\]=Division\_Selected)

Then, of course, we just need to filter our capability list on the list of employees. Simple, right?

\=FILTER(Table2\[Capabilities\],Table2\[Employee\]=Division\_Employees)

![](<Base64-Image-Removed>)

Wait, what?

**_The Answer_**

This problem suffers from a problem that has plagued arrays, not just in Excel. The system is simply not equipped to let us calculate “an array of arrays” – that is, we can’t feed in a variable number of employees into our capability filter and expect it to know how to combine the results.

The trick to working around this problem is to define the filter relationship more directly. Instead of creating a criteria to see if the Employee column matches the Division\_Employees, we can instead try to create a series of {1,0} results that correspond to that check.

MATCH(Table2\[Employee\],Division\_Employees,0)

This will give us positive numbers (reflecting the employee’s position in our selected list) or #N/A if it can’t find the employee in the list. Recognising this, we need to wrap it in an error check:

IFNA(MATCH(Table2\[Employee\],Division\_Employees,0),0)

This will yield only positive numbers and zeroes in our list.

![](<Base64-Image-Removed>)

Because positive numbers can be used as substitute for TRUE when a formula is expecting a Boolean TRUE/FALSE input, this is all we need to fill in our FILTER result.

![](<Base64-Image-Removed>)

\=FILTER(Table2\[Capabilities\],IFNA(MATCH(Table2\[Employee\],Division\_Employees,0),0))

There we go! By switching the filter direction of the “array of arrays”, we can get an array result that lines up with our filter table, allowing us to get the result that we’re looking for.

Did you have a better solution? Let us know, we’d be glad to hear if there are better ways to work around this problem!

_The Final Friday Fix will return on Friday 25 June 2021 with a new Excel Challenge. In the meantime, please look out for the Daily Excel Tip on our [home page](https://www.sumproduct.com/)
 and watch out for a [new blog](https://www.sumproduct.com/blog)
 every business workday._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-june-2021-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-june-2021-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-june-2021-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-june-2021-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-june-2021-challenge/#0 "close")

top