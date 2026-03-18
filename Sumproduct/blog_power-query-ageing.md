# Power Query: Ageing

**Source:** https://sumproduct.com/blog/power-query-ageing/

---

[Home](https://sumproduct.com/)

\> Power Query: Ageing

*   April 14, 2020

Power Query: Ageing
===================

Power Query: Ageing
===================

15 April 2020

_Welcome to our Power Query blog. This week, I look at calculating age._

_I have some data for my imaginary salespeople. This week, I intend to calculate their age._

![](<Base64-Image-Removed>)

I extract my data to Power Query using ‘From Table’ on the ‘Get & Transform’ section of the Data tab.

![](<Base64-Image-Removed>)

_I accept the defaults._

![](<Base64-Image-Removed>)

_If I select the **DOB** column, on the ‘Add Column’ tab, I have the option of choosing ‘Age’ on the ‘Date’ dropdown of the ‘From Date’ section._

![](<Base64-Image-Removed>)

_This doesn’t look much like an age. This is because it gives me the duration in days, hours, minutes and seconds between the current date and_ **DOB**_. That’s very accurate, but not quite what I am looking for. I choose to add another column, this time based on **Age**._

![](<Base64-Image-Removed>)

_Using the Duration dropdown, I can create a new column for the total number of years in the **Age** column._

![](<Base64-Image-Removed>)

_This is much better, but it’s still a little too accurate for my needs. I choose to round down the value (no adult likes to round up their age!)._

![](<Base64-Image-Removed>)

_I do this on the Transform tab, where I can choose to ‘Round Down’ from the Rounding dropdown in the ‘Number Column’ section._

![](<Base64-Image-Removed>)

_Now I have the age of my salespeople in the format I require. I rename my column and remove the column I used to get to my result._

![](<Base64-Image-Removed>)

_I can also use this method to calculate the age of a product or a duration in years between two dates._

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-ageing/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-ageing/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-ageing/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-ageing/#0)

[](https://sumproduct.com/blog/power-query-ageing/#0 "close")

top