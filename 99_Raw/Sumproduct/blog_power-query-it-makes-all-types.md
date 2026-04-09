# Power Query: It Makes All Types

**Source:** https://sumproduct.com/blog/power-query-it-makes-all-types/

---

[Home](https://sumproduct.com/)

\> Power Query: It Makes All Types

*   March 28, 2023

Power Query: It Makes All Types
===============================

Power Query: It Makes All Types
===============================

29 March 2023

_Welcome to our Power Query blog. This week, we create a linked type._

I have been asked to add the tent types to the sheet showing the availability of salespeople for the upcoming conferences:

![](<Base64-Image-Removed>)

I start by extracting the data. On the ‘Get & Transform’ section of the Data tab, I use the ‘Get Data’ dropdown:

![](<Base64-Image-Removed>)

I choose ‘From Microsoft Access Database’ from the ‘From Database’ dropdown. I can then browse to the location of the database and view the tables:

![](<Base64-Image-Removed>)

I select the **Items** table and choose to ‘Transform Data’.

![](<Base64-Image-Removed>)

I can see at the bottom-left of the screen that I have 18 columns of data. The manager is adamant that all 18 columns should be available on the sheet. I choose ‘Close & Load To…’ from the ‘Close & Load’ dropdown on the Home tab:

![](<Base64-Image-Removed>)

The requirement is for the Table to appear at cell **K12**, so I choose this location and click OK:

![](<Base64-Image-Removed>)

If you’d like to know why my output is a blue table, check out [Power Query Tables Don’t Have to be Green](https://sumproduct.com/blog/power-query-power-query-tables-do-not-have-to-be-green/)
!

Most of the data is not visible from the main area where the rest of the Tables are. I need a better way of giving the users access to the data. I go back to the **Items** query and select all my data by clicking in any column and using **CTRL** + **A**:

![](<Base64-Image-Removed>)

In the Transform tab, I locate the ‘Structured Column’ section, and choose ‘Create Data Type’:

![](<Base64-Image-Removed>)

Clicking on this will allow me to create a custom rich (aka linked) data type.

![](<Base64-Image-Removed>)

I am prompted to name my data type and indicate the ‘Display column’. This is the column that will be the key to access the other data, and that the users will be most likely to identify the data by.

![](<Base64-Image-Removed>)

I choose to call my data type ‘Tents’ and choose **Item\_Name** to appear in the sheet and link to the other data.

If I had chosen the Advanced option, then I could select which data to associate with the data type and change the order of the selected data:

![](<Base64-Image-Removed>)

I am happy with the ‘Selected columns’ so I click OK, and the query is converted to a data type:

![](<Base64-Image-Removed>)

I can now ‘Close & Load’ to go back to Excel:

![](<Base64-Image-Removed>)

Now the table is one column, it fits in with the other data. The icon next to the tent name tells the user that this is a linked data type. If I click on one of the tent names, I can access the linked menu:

![](<Base64-Image-Removed>)

Clicking on one of these options would add a column with that title e.g. ‘Height’, containing the data for all the tent types. In this example however, clicking on the icon in the first column is more useful:

![](<Base64-Image-Removed>)

This accesses the card for each title, meaning that all the data is available for viewing if required.

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-it-makes-all-types/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-it-makes-all-types/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-it-makes-all-types/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-it-makes-all-types/#0)

[](https://sumproduct.com/blog/power-query-it-makes-all-types/#0 "close")

top