# Power Query: Find a Table

**Source:** https://sumproduct.com/blog/power-query-find-a-table/

---

[Home](https://sumproduct.com/)

\> Power Query: Find a Table

*   May 11, 2021

Power Query: Find a Table
=========================

Power Query: Find a Table
=========================

12 May 2021

_Welcome to our Power Query blog. This week, I look at what to do when the location of a table is changed._

I have a query for some data that I have been receiving from my imaginary salespeople. However, when I try to open the query, I get an error message.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-200.jpg)

Power Query can’t find a table called **Tent\_Sales**. The first step I should take is to look at the ‘Source’ step, which is usually the first step in my query.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-259.jpg)

The ‘Source’ step is also failing. The **M** code in my source step is:

\= Table.NestedJoin(#”Tent Sales”, {“Tent Pack”}, #”Tent Packs”, {“Pack Number”}, “Tent Packs”, JoinKind.LeftOuter)

There is no mention of **Tent\_Sales** here. A good way to see where the error has come from, is to check the query dependency diagram. This can be found on the View tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-206.jpg)

This gives me some clues. This query has come from a merge of **Tent Sales** and **Tent Packs**, and both queries have come from the current workbook. Therefore, I take a look at the **Tent Sales** query.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-196.jpg)

Apart from seeing the same error, I notice I have a ‘Go To Error’ button.

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-165.jpg)

This takes me to the source step, which has the following **M** code:

\= Excel.CurrentWorkbook(){\[Name=”Tent\_Sales”\]}\[Content\]

I now know which step is pointing to **Tent\_Sales**. If that table no longer exists, I need to know what tables do exist in the workbook. I go back to Excel and choose the Formulas tab.

![](<Base64-Image-Removed>)

I select the ‘Name Manager’, and I can see the tables that exist in the workbook. **Tent\_Sales7** looks suspiciously similar to the table that I am missing.

![](<Base64-Image-Removed>)

If I edit the name, I can see that the Table exists on the ‘New Location’ sheet, and the description tells me that this is the correct Table. Someone has copied the data from ‘Old Location’ to ‘New Location’ without realising that the Table name will change or that a query is dependent upon it. To fix this, I go to the sheet ‘New Location’.

![](<Base64-Image-Removed>)

If I access the ‘Table Design’ tab. I can see the Table name. I may either change it here or else change the query to use the new name. Since the original name is more logical, I opt to change the Table names on this sheet.

![](<Base64-Image-Removed>)

Now my Tables have their original names back, the queries are loading correctly. Having seen how easy it is to move and rename Tables, I decide to make sure that the sheet is protected.

![](<Base64-Image-Removed>)

I can just protect the sheet without a password, which will alert the user that the sheet is protected, but allow them to unprotect it, or otherwise I may create a password. This will allow me to stop users from changing the data on the sheet – however I MUST take note of the password used.

![](<Base64-Image-Removed>)

If the sheet is protected, not only is the user prevented from changing the data in the sheet, but they are also prevented from changing the table name in the ‘Name Manager’ (notice the greyed-out buttons).

![](<Base64-Image-Removed>)

My Tables are now “safer” and the queries load correctly.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-find-a-table/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-find-a-table/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-find-a-table/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-find-a-table/#0)

[](https://sumproduct.com/blog/power-query-find-a-table/#0 "close")

top