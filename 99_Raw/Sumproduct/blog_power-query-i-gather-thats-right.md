# Power Query: I Gather That’s Right

**Source:** https://sumproduct.com/blog/power-query-i-gather-thats-right/

---

[Home](https://sumproduct.com/)

\> Power Query: I Gather That’s Right

*   December 8, 2020

Power Query: I Gather That’s Right
==================================

Power Query: I Gather That’s Right
==================================

9 December 2020

_Welcome to our Power Query blog. This week, I look at how to gather data from multiple rows._

Just for a change, I have some tent data…

![](<Base64-Image-Removed>)

I want to present one line for each Tent / Awning combination, with any accessories appearing as a list, e.g. ‘Medium Package Groundsheet, Lights’. I begin by extracting my data to Power Query using the ‘From Table’ option on the ‘Get & Transform’ section of the Data tab.

![](<Base64-Image-Removed>)

I take the defaults:

![](<Base64-Image-Removed>)

I am going to group my data, and I can do this from the Transform tab.

![](<Base64-Image-Removed>)

I use the ‘Group By’ functionality, _viz._

![](<Base64-Image-Removed>)

I have used the Advanced options to that I can group by **Tent** and then **Awning**, and I put all the data gathered into a new column called **AccessoryList**.

![](<Base64-Image-Removed>)

This gives me a column for each unique **Tent** / **Awning** combination, plus a table column.

![](<Base64-Image-Removed>)

If I click in the white space next to the word ‘Table’ I can see the data included in that table.

Next, I create a new custom column from the ‘Add Column’ tab which will contain just the accessory data.

![](<Base64-Image-Removed>)

I have treated **AccessoryList** as a table, and selected **Accessories** from that table.

![](<Base64-Image-Removed>)

This has created a list of the accessories. Now I need to format the list the way I want it.

![](<Base64-Image-Removed>)

If I click on the expansion symbol next to the title of **Accessories**, I can choose to ‘Extract Values’.

![](<Base64-Image-Removed>)

I can use a delimiter; I choose a comma.

![](<Base64-Image-Removed>)

I can now remove the table column and I have my data the way I want to present it.

![](<Base64-Image-Removed>)

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-i-gather-thats-right/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-i-gather-thats-right/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-i-gather-thats-right/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-i-gather-thats-right/#0)

[](https://sumproduct.com/blog/power-query-i-gather-thats-right/#0 "close")

top