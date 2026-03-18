# Final Friday Fix: June 2021 Challenge

**Source:** https://sumproduct.com/blog/final-friday-fix-june-2021-challenge/

---

[Home](https://sumproduct.com/)

\> Final Friday Fix: June 2021 Challenge

*   June 24, 2021

Final Friday Fix: June 2021 Challenge
=====================================

Final Friday Fix: June 2021 Challenge
=====================================

25 June 2021

_On the final Friday of each month, we are going to set an Excel / Power BI challenge for you to puzzle over so that you can get your “Excel fix”. Challenge your office colleagues to see who can solve the puzzle quickest. There are no prizes at this stage: you are playing for bragging rights only!_

We’ve talked at long length about Dynamic Arrays and how the value that they add to Excel and the solutions that we can build with them. But sometimes, as we keep pushing to solve ever increasingly difficult problems, we end up hitting some fairly hard limits.

In this instance, we have a list of employees where we know what division each person works in. We also have a list of capabilities that each employee brings to the team. If we select an employee, we’d like to know what their whole team brings to the table.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-173.jpg)

So to do this, we naturally follow some basic steps – what’s your employee’s name, and what division are they from? So simple, so **INDEX(MATCH())**.

  =INDEX(Table1\[Division\],MATCH(Employee\_Selection,Table1\[Employee\],0))  

Then, we might even be able to find a list of all the employees that work in that division. That’s what **FILTER** is for, right?

  =FILTER(Table1\[Employee\],Table1\[Division\]=Division\_Selected)  

Then, of course, we just need to filter our capability list on the list of employees. Simple, right?

  =FILTER(Table2\[Capabilities\],Table2\[Employee\]=Division\_Employees)  

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-228.jpg)

Wait, what?

**_The Challenge_**

This month’s challenge is very straightforward. Can you come up with a formula to give us a list of capabilities that each person in the team can provide?

_Sounds easy? Then why not have a go? We’ll publish one solution in Monday’s blog. Have a great weekend in the meantime!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/final-friday-fix-june-2021-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/final-friday-fix-june-2021-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/final-friday-fix-june-2021-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/final-friday-fix-june-2021-challenge/#0)

[](https://sumproduct.com/blog/final-friday-fix-june-2021-challenge/#0 "close")

top