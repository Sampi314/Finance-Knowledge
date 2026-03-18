# Power Query: Fiddly Fill Down

**Source:** https://sumproduct.com/blog/power-query-fiddly-fill-down/

---

[Home](https://sumproduct.com/)

\> Power Query: Fiddly Fill Down

*   June 30, 2020

Power Query: Fiddly Fill Down
=============================

Power Query: Fiddly Fill Down
=============================

1 July 2020

_Welcome to our Power Query blog. This week, I look at an example where using the standard fill down will not work and I have to use a conditional column to fill down instead._

I have some data on tents supplied by my imaginary company:

![](<Base64-Image-Removed>)

I would like to get this into a more standard format, by filling down the tent and awning types. I begin by extracting my data to Power Query, by using the ‘From Table’ option on the ‘Get & Transform’ section of the Data tab.

![](<Base64-Image-Removed>)

I accept the defaults and tick the box to indicate that my table does indeed have headers.

![](<Base64-Image-Removed>)

I start by filling down my **Tent** column by right-clicking that column and selecting ‘Fill’ and then ‘Down’.

![](<Base64-Image-Removed>)

I continue and fill in the tent types.

![](<Base64-Image-Removed>)

However, if I now do the same thing to **Awning**, the results are not what I want.

![](<Base64-Image-Removed>)

**_Awning_** has been filled in for those rows where only the tent type should appear. The first row featuring ‘Medium’ tent should have _null_ in **Awning**, just as the first row for ‘Large’ does. I remove my ‘Filled Down’ step from ‘APPLIED STEPS’ and don’t fill down for either **Tent** or **Awning**. Instead, I start by adding a conditional column from the ‘Add Column’ tab:

![](<Base64-Image-Removed>)

I am creating a new column which will have the value in **Awning** if **Tent** is _null_, otherwise it will be ‘Don’t Fill’.

![](<Base64-Image-Removed>)

I try filling down again, but this time I select both **Tent** and **Awning Rule**, and then right-click and choose ‘Fill’ and then ‘Down’.

![](<Base64-Image-Removed>)

This gives me a better result:

![](<Base64-Image-Removed>)

The rows where I don’t want the **Awning** value have ‘Don’t Fill’ in them, which I can easily replace.

![](<Base64-Image-Removed>)

I click ‘OK’ and remove the original **Awning** column, moving my new **Awning Rule** column next to **Tent** and then renaming it to **Awning**.

![](<Base64-Image-Removed>)

Next time, I’ll look at another solution using a conditional method to replace the values instead.

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-fiddly-fill-down/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-fiddly-fill-down/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-fiddly-fill-down/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-fiddly-fill-down/#0)

[](https://sumproduct.com/blog/power-query-fiddly-fill-down/#0 "close")

top