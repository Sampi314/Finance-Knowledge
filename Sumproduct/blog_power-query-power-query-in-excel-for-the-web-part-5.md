# Power Query: Power Query in Excel for the web Part 5

**Source:** https://sumproduct.com/blog/power-query-power-query-in-excel-for-the-web-part-5/

---

[Home](https://sumproduct.com/)

\> Power Query: Power Query in Excel for the web Part 5

*   February 18, 2026

Power Query: Power Query in Excel for the web Part 5
====================================================

_Welcome to our Power Query blog.  This week, we continue to look at some of the features of Power Query in Excel for the web by transforming a CSV file._

Recently, I welcomed the arrival of more Power Query functionality to Excel for the web.  I have looked at how I can now create a query from data in the current online workbook (aka project).  This week. I will continue extracting data from other online files.

I will be enlisting the help of my imaginary salespeople, beginning with Derek.  I plan to extract data from a CSV file called **PQ\_StandardExpense\_CSV\_1**.   In [Part 3](https://sumproduct.com/blog/power-query-power-query-in-excel-for-the-web-part-3/)
, I successfully linked to a CSV file in my company’s SharePoint.

![](<Base64-Image-Removed>)

Moving swiftly on from [last week’s adventures](https://sumproduct.com/blog/power-query-power-query-in-excel-for-the-web-part-4/)
 with ‘Add table using examples’, let’s ‘Transform data’:

![](<Base64-Image-Removed>)

When I extract this CSV file in the desktop version of Excel, I would usually expect to see the headers promoted in the automated steps, which would have had a knock-on effect on the ‘Changed column type’ step.  I begin by deleting the ‘Changed column type’ step.  I choose to ‘Use first row as headers’ from the Transform tab:

![](<Base64-Image-Removed>)

The new automated ‘Changed column type’ step is still not helping me, so I delete it again.  Whilst the pound (**£**) sign in **amount** may be confusing the algorithms as it does not appear to have been extracted correctly, I would have expected the **Date** column to be given the correct data type.  I assign the correct data type to **Date** and turn my attention to the amount column.  I need to remove the first character.  Whilst I know a way to do this using the **M** function **Text.RemoveRange** which I will show in a moment, let’s see what ‘Column from Examples’ on the ‘Add Column’ tab can do with this.

![](<Base64-Image-Removed>)

This approach is also valid: the algorithm has used the symbol in the first character position as a delimiter.

> **Table.AddColumn(#”Changed column type”, “Amount”, each Text.AfterDelimiter(\[amount\], “�”), type text)**

I have chosen to use the new column name **Amount**, which still describes the column content, but allows me to keep the orginal **amount** column for comparison. Since **M** is case-sensitive, this will not be a problem. I would rather avoid using the symbol as a delimiter since it has not been interpreted correctly, so I will use an alternative approach.  Note than when I enter a new step in the Formula bar, I do not begin with an equal sign (**\=**).

> **Table.AddColumn(#”Changed column type”, “Amount”, each Text.RemoveRange(\[amount\], 0), type text)**

This **M** code adds a column to the table created by the ‘Changed column type’ step which is created by removing the character in the first position of **amount**.  Note that the first position is zero \[0\], not one \[1\].  This gives me the same result as the ‘Inserted Text After Delimiter’ step, and I don’t need to be concerned whether the symbol is interpreted correctly.

![](<Base64-Image-Removed>)

I may delete the ‘Inserted Text After Delimiter’ step.  I also rename my step from ‘Custom’ to ‘Removed first character’.   I have a cog symbol next to my step which allows me to use the ‘Custom Column’ dialog box to change the **M** code:

![](<Base64-Image-Removed>)

I may now change the data type of this column.  I only want one ‘Changed column type’ step so I drag ‘Removed first character’ above this step and then change the data type of **Amount** to decimal number

![](<Base64-Image-Removed>)

The change is added to the existing step, and I am ready to fill down the **Name** column.  I must follow the usual rule and replace the blank column values with _null_ values using the right-click menu.  I may then right-click again and choose to ‘Fill’ and then choose ‘Down’:

![](<Base64-Image-Removed>)

I need to delete the **amount** column and my data will be ready to be appended to the other accounting data. 

Come back next time for more ways to use Power Query!            

*   [Log in](https://sumproduct.com/blog/power-query-power-query-in-excel-for-the-web-part-5/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-power-query-in-excel-for-the-web-part-5/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-power-query-in-excel-for-the-web-part-5/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-power-query-in-excel-for-the-web-part-5/#0)

[](https://sumproduct.com/blog/power-query-power-query-in-excel-for-the-web-part-5/#0 "close")

top