# Power Query: Totally Random

**Source:** https://sumproduct.com/blog/power-query-totally-random/

---

[Home](https://sumproduct.com/)

\> Power Query: Totally Random

*   February 22, 2022

Power Query: Totally Random
===========================

Power Query: Totally Random
===========================

23 February 2022

_Welcome to our Power Query blog. This week, I look at one way of generating random data._

Whilst producing the masterpieces that are these [Power Query blogs](https://www.sumproduct.com/thought/power-query-blog-series)
, I often need to generate random data. In Excel, I favour the **RANDBETWEEN()** function, but there are also functions I can use in Power Query. This week, I look at the **Number.Random()** function.

This **M** function has the following syntax:

**Number.Random() as number**

The output is a random number between zero \[0\] and one \[1\]. To show how it is used, I have created a list of numbers from one \[1\] to 20:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-62-1.jpg)

I then convert the list to a table using the ‘To Table’ option from the Convert section on the Transform tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-83.jpg)

I now have a table, which means I may add columns:

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-62.jpg)

I choose to add a ‘Custom Column’ from the ‘Add Column’ tab:

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-57.jpg)

I am going to make a deliberate mistake. In the ‘Custom Column’ dialog, I name the new column **Number.Random**:

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-48.jpg)

The **M** code I have used is:

**\= Number.Random**

Power Query detects no syntax errors, so I click OK:

![](<Base64-Image-Removed>)

A function in every column is not quite what I am looking for! If I click on one of the ‘Function’ values, I can invoke it:

![](<Base64-Image-Removed>)

This process has created two steps, ‘Number Random’ and ‘Invoked FunctionNumber Random’ (the odd spacing is down to Power Query, not me!).

The first step, ‘Number Random’, is the function page:

![](<Base64-Image-Removed>)

Therefore, the second step is calling the function. The step ‘Invoked FunctionNumber Random’ produces the number I wanted in the column. Notice the **M** code used:

![](<Base64-Image-Removed>)

The **M** code is:

 **= #”Number Random”()**

Since I know the ‘Number Random’ step is the function, I can see that, even though the function has no parameters, I still need to enter the brackets \[**()**\]. I can go back and correct the column I added.

I go back to the ‘Added Column’ step and use the cog (gear) icon next to it to change the definition of the column.

![](<Base64-Image-Removed>)

I have changed the **M** code to:

**\= Number.Random()**

This time, with the small change to the **M** code, I get the result I would like:

![](<Base64-Image-Removed>)

Readers who have tried **Number.Random()** in earlier versions of Power Query will notice that its behaviour in a column has improved. In previous versions, the same random number appeared for every row! Now I can use this column as a starting point for larger random values and dates by transforming the data.

I will look at another random function next time.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-totally-random/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-totally-random/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-totally-random/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-totally-random/#0)

[](https://sumproduct.com/blog/power-query-totally-random/#0 "close")

top