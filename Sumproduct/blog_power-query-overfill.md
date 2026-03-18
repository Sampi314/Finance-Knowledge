# Power Query: Overfill

**Source:** https://sumproduct.com/blog/power-query-overfill/

---

[Home](https://sumproduct.com/)

\> Power Query: Overfill

*   February 4, 2020

Power Query: Overfill
=====================

Power Query: Overfill
=====================

5 February 2020

_Welcome to our Power Query blog. This week, I look at filling issues._

I have a very simple query:

![](<Base64-Image-Removed>)

John, my favourite imaginary salesperson has been a little lazy when filling in his visit data. He should fill in the date for all visit and phone calls. I need to fill down the data, but only for those rows which have either ‘Visit’ or ‘Telephone’ in the **_Contact Method_**.

Sadly, there is not currently a simple method to conditionally fill down data using **M** code. The easiest method is to start with ‘Fill Down’ which can be accessed by right-clicking the **_Date_** column.

![](<Base64-Image-Removed>)

This will fill in all the dates:

![](<Base64-Image-Removed>)

I can then create a conditional column from the ‘Add Column’ tab.

![](<Base64-Image-Removed>)

I only want the date to appear if the **_Contact Method_** is not ‘Email’.

![](<Base64-Image-Removed>)

I can now remove the original date column and rename **_Date2_** to **_Date_**.

![](<Base64-Image-Removed>)

This gives me the data with the dates filled in if the contact was not via email.

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-overfill/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-overfill/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-overfill/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-overfill/#0)

[](https://sumproduct.com/blog/power-query-overfill/#0 "close")

top