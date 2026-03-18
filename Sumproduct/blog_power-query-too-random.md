# Power Query: Too Random

**Source:** https://sumproduct.com/blog/power-query-too-random/

---

[Home](https://sumproduct.com/)

\> Power Query: Too Random

*   March 1, 2022

Power Query: Too Random
=======================

Power Query: Too Random
=======================

2 March 2022

_Welcome to our Power Query blog. This week, I look at another way of generating random data._

Whilst producing the masterpieces that are Power Query blogs, I often need to generate random data. In Excel, I favour the **RANDBETWEEN()** function, but there are also functions I can use in Power Query. This week I look at the **Number.RandomBetween()** function, which is even more like my favourite Excel function, but with an important difference!

This **M** function has the following syntax:

**Number.RandomBetween(bottom as number, top as number) as number**

The output is a random number between **bottom** and **top**. To show how it is used, I have created a list of numbers from one \[1\] to 20:

![](<Base64-Image-Removed>)

I then convert the list to a table using the ‘To Table’ option from the Convert section on the Transform tab.

![](<Base64-Image-Removed>)

I now have a table, which means I can add columns:

![](<Base64-Image-Removed>)

I choose to add a ‘Custom Column’ from the ‘Add Column’ tab:

![](<Base64-Image-Removed>)

I decide I want values between zero \[0\] and 100:

![](<Base64-Image-Removed>)

The **M** code I have used is:

**\= Number.RandomBetween(0,100)**

This gives me some random values:

![](<Base64-Image-Removed>)

My first question is whether **Number.RandomBetween()** is volatile like it’s Excel cousin **RANDBETWEEN().** I can check this by refreshing, which I can do using ‘Refresh Preview’ on the Home tab:

![](<Base64-Image-Removed>)

Yes, I have new values. This is important to know as it means I need some way of stabilising the output if I want to use it to generate stable data. In Excel I would Copy and ‘Paste Special’ to keep the values.

To see if something similar is possible, I select **RandomBetween** and right-click, I have the option to ‘Duplicate Column’:

![](<Base64-Image-Removed>)

This creates another column:

![](<Base64-Image-Removed>)

Notice that the step ‘Duplicated Column’ does not have a cog icon next to it, but this is misleading. If I refresh data again, I can see if the values change in **RandomBetween – Copy**:

![](<Base64-Image-Removed>)

**RandomBetween – Copy** changes to match **RandomBetween**. Power Query executes all the steps, which means it generates the values for **RandomBetween** and then takes a copy. Similarly, if I add another step:

![](<Base64-Image-Removed>)

Even without refreshing, **Number.RandomBetween()** is generated for each step. I would need to export to Excel and take a copy from there to get a stable data set.

I will look at another random function next time.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-too-random/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-too-random/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-too-random/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-too-random/#0)

[](https://sumproduct.com/blog/power-query-too-random/#0 "close")

top