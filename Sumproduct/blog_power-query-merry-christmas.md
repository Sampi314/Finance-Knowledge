# Power Query: M(erry) Christmas

**Source:** https://sumproduct.com/blog/power-query-merry-christmas/

---

[Home](https://sumproduct.com/)

\> Power Query: M(erry) Christmas

*   December 24, 2024

Power Query: M(erry) Christmas
==============================

Power Query: M(erry) Christmas
==============================

25 December 2024

_Welcome to our Power Query blog. This week, I take a break from all things fuzzy to help out a familiar face._

I have received a request from a Mr. S Claus, who is having some issues with his workforce. The Elf Service are complaining about being continually shelved, and Mr. Claus has resorted to asking the reindeer to create a Present List. They are refusing to pull together, so he has the following Table:

![](https://sumproduct.com/wp-content/uploads/2025/05/198f866f7b8dca58879e1a03ef31c5f5-1.jpg)

He would like one list, and to avoid upsetting the Elves again, he needs any duplicates to be removed. Since he’s quite busy, he would like me to automate this process.

I start by naming the Table **SC\_List,** by changing ‘Table Name:’ in the ‘Table Design’ tab. I right-click on the Table and choose to ‘Get Data from Table/Range’. I now have a query **SC\_List**:

![](https://sumproduct.com/wp-content/uploads/2025/05/c7cc430231bc955ffb06b028d2f353b2-1.jpg)

I may remove the ‘Changed Type’ step, as all my data is text, and I will not be keeping these columns. I note that if I right-click on a column header, I have the option to ‘Add as New Query’:

![](https://sumproduct.com/wp-content/uploads/2025/05/81fc8c24ac194d228f06b96025c7221c-1.jpg)

If I did this to each column, I could create nine \[9\] queries, which may then be appended together.

Let’s look at the **M** code generated when I create a query for **Dasher**:

![](https://sumproduct.com/wp-content/uploads/2025/05/17848520bdb85836b3b70102dd3140b8-1.jpg)

The **M** code is simply:

**\= Source\[Dasher\]**

This gives me an idea. Rather than creating lots of queries and appending them, I may add lists together using the function **List.Combine()** (which I last looked at a long time ago in [‘All Over Running Totals’](https://sumproduct.com/blog/power-query-all-over-running-totals/)
). For example, to combine the **Dasher** and **Rudolf** columns I could use the **M** code:

**\= List.Combine({Source\[Dasher\], Source\[Rudolf\]})**

![](<Base64-Image-Removed>)

This is looking good; let’s add the rest of the herd.

![](<Base64-Image-Removed>)

The **M** code is:

**\= List.Combine({Source\[Dasher\],  
Source\[Prancer\], Source\[Dancer\], Source\[Vixen\], Source\[Donner\],  
Source\[Blitzen\], Source\[Cupid\], Source\[Comet\],Source\[Rudolf\]})**

Perfect, 90 rows are now on the list! Now, I need to get rid of the duplicates. I can do this without adding another step. Instead of **List.Combine()**, I use **List.Union()**:

![](<Base64-Image-Removed>)

The **M** code is now

**\=  
List.Union({Source\[Dasher\], Source\[Prancer\], Source\[Dancer\], Source\[Vixen\],  
Source\[Donner\], Source\[Blitzen\], Source\[Cupid\], Source\[Comet\],Source\[Rudolf\]})**

For this example, **List.Union()** is ideal as it extracts items from all the lists but only shows them once. I rename the query **SC\_Elves\_List**, and ‘Close & Load’ from the Home tab:

![](<Base64-Image-Removed>)

The list is even in the Elves favourite colour! When Rudolf decides to add more ‘toys’:

![](<Base64-Image-Removed>)

I simply refresh the query and the new rows appear:

![](<Base64-Image-Removed>)

Mr. Claus is happy (actually, quite jolly). Merry Christmas!

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-merry-christmas/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-merry-christmas/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-merry-christmas/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-merry-christmas/#0)

[](https://sumproduct.com/blog/power-query-merry-christmas/#0 "close")

top