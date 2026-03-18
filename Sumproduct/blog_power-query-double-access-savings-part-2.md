# Power Query: Double Access Savings – Part 2

**Source:** https://sumproduct.com/blog/power-query-double-access-savings-part-2/

---

[Home](https://sumproduct.com/)

\> Power Query: Double Access Savings – Part 2

*   August 2, 2022

Power Query: Double Access Savings – Part 2
===========================================

Power Query: Double Access Savings – Part 2
===========================================

3 August 2022

_Welcome to our Power Query blog. This week, I filter and expand the data in the two Access databases from last week._

I have two Access databases. These are deliberately very simple, as I am demonstrating a concept here. The first database (imaginatively called ‘Commodity Groups’) contains the **Commodity\_Groups** table:

![](<Base64-Image-Removed>)

In another database, in the same directory, I have the **Commodity\_Sub\_Groups** table. Funnily enough, the name of this database is ‘**Commodity Sub-groups**‘:

![](<Base64-Image-Removed>)

[Last time](https://sumproduct.com/blog/power-query-double-access-savings-part-1/)
, I used ‘From Folder’ to extract the databases into Power Query:

![](<Base64-Image-Removed>)

I then chose to transform my data in the Power Query editor:

![](<Base64-Image-Removed>)

This week, I shall start by filtering my data, so I only keep the files I want. For this example, I could add other databases to the folder, so I want to allow these to be selected, but I want to exclude the large ‘**Access Database SP**‘, as I do not need tables from this database and including it could slow down my query. In the filter dropdown on **Name**, I unselect ‘**Access Database SP**‘.

![](<Base64-Image-Removed>)

There is another filter I need to do, in order to ensure that I only pick Access database files. I need to use ‘Text Filters’ in the filter dropdown for **Extension**, as there is only one value currently, so I can’t select it on the checkbox without selecting everything:

![](<Base64-Image-Removed>)

I choose only those files where the **Extension** equals ‘.accdb’. This is the only item in the dropdown for the value.

![](<Base64-Image-Removed>)

Note that I must include this step even if there are only Access database files in my folder; I will show why later. Now I have the files I need; I can choose to ‘Combine Files’ using the icon to the right of the **Content** heading.

![](<Base64-Image-Removed>)

(Also notice that Power Query has not managed to combine the ‘Filtered Rows’ and ‘Filtered Rows1’ steps!)

This takes me to the ‘Combine Files’ dialog:

![](<Base64-Image-Removed>)

I can click on the table icon to check the data, but I must not click OK, as the process would then try to append the data in the tables.

![](<Base64-Image-Removed>)

Instead, I click on the folder icon, and then I can click ‘OK’.

![](<Base64-Image-Removed>)

Next time, I will continue examining and combining my data in the Power Query editor.

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-double-access-savings-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-double-access-savings-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-double-access-savings-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-double-access-savings-part-2/#0)

[](https://sumproduct.com/blog/power-query-double-access-savings-part-2/#0 "close")

top