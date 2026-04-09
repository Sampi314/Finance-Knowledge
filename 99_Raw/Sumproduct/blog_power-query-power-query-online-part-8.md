# Power Query: Power Query Online – Part 8

**Source:** https://sumproduct.com/blog/power-query-power-query-online-part-8/

---

[Home](https://sumproduct.com/)

\> Power Query: Power Query Online – Part 8

*   September 26, 2023

Power Query: Power Query Online – Part 8
========================================

Power Query: Power Query Online – Part 8
========================================

27 September 2023

_Welcome to our Power Query blog. Today, I look at the ‘Schema tools’ tab in Power Query Online._

In the current series, I am looking at Power Query Online, which I have accessed from Power Apps:

![](<Base64-Image-Removed>)

[Last week](https://sumproduct.com/blog/power-query-power-query-online-part-7/)
, I looked at the ‘Merge Queries’ process to see how it is different to Power Query on the desktop.

![](<Base64-Image-Removed>)

When I merged **Population Data** and **Region Data,**I created a large query called **Merge**. Since this query contains a large quantity of data, it can take time for it to display:

![](<Base64-Image-Removed>)

Rather than wait for it, if I want to perform some actions on the structure of the table, I can use the buttons at the bottom-right to ‘Show schema view’:

![](<Base64-Image-Removed>)

This view also allows me access to a contextual tab on the Ribbon, ‘Schema tools’.

![](<Base64-Image-Removed>)

The ‘Schema tools’ tab contains the functionality that I can apply to columns, such as using ‘Choose columns’ to allow me to specify which columns I want to keep:

![](<Base64-Image-Removed>)

This is also some new functionality – that is, it is new to the GUI interface. The third column in the schema view is **Key.** On the ‘Schema tools’ tab, there is an option in the ‘Transform’ section to ‘Mark as key’:

![](<Base64-Image-Removed>)

I choose to do this for **Country Code**:

![](<Base64-Image-Removed>)

**Country Code** now has a key icon in the **Key** column, and a step ‘Marked key columns’ has been generated. The **M** code for this step is:

**Table.AddKey(#”Changed column type”, {****“Country Code”****},** **false****)**

This uses the function **Table.AddKey()**:

**Table.AddKey(table** as table**, columns** as list**,  
isPrimary** as logical**)** as table

This function adds either a primary or secondary key to a **table.****Columns** is the list of columns that define the key, and **isPrimary** is a logical value which is true for a primary key and false for a secondary key.

This is a database term, where a key or index helps to access the data more efficiently by defining the unique and other commonly used links. The primary key is usually unique, though it can be repeating. Next time, I will look at how we can use these keys in Power Query.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-power-query-online-part-8/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-power-query-online-part-8/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-power-query-online-part-8/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-power-query-online-part-8/#0)

[](https://sumproduct.com/blog/power-query-power-query-online-part-8/#0 "close")

top