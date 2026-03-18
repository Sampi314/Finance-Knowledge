# Power Query: Cleanse, Tone and Upload

**Source:** https://sumproduct.com/blog/power-query-cleanse-tone-and-upload/

---

[Home](https://sumproduct.com/)

\> Power Query: Cleanse, Tone and Upload

*   December 12, 2017

Power Query: Cleanse, Tone and Upload
=====================================

Power Query: Cleanse, Tone and Upload
=====================================

13 December 2017

_Welcome to our Power Query blog. This week I look at combining several Power Query functions in order to standardise some incoming data._

For today’s example, I will use my reliable fictional salespeople – but as usual, they have thrown some problems into my data.

![](<Base64-Image-Removed>)

Derek has helpfully entered the expense codes as I would like to describe them, but Mary and Paul have been less consistent. I would like to change the expense codes to the standard names so that I can calculate totals, but without having to go through and change each entry manually – in a large dataset many people may have used ‘Gas’ instead of ‘Petrol’. First, I need to create a query for my data, which I do on the ‘Data’ tab in the ‘Get and Transform’ section. I opt to create a query ‘From Table’:

![](<Base64-Image-Removed>)

My data is not yet in a table, so this will be done as part of the query creation process; I am prompted for the boundaries and whether I have titles. I can then create my query.

![](<Base64-Image-Removed>)

From the ‘File’ or ‘Home’ tab, I choose to ‘Close and Load To’, in order to create a connection.

![](<Base64-Image-Removed>)

I don’t want to load data to my workbook at this point, as nothing has yet changed.

To replace the non-standard entries in **_Expense Code_**, I need a reference table. This avoids the need to ‘hard code’ anything (if you don’t know what this means ask a programmer and watch them grimace). Therefore, I right click on my query and look at my options:

![](<Base64-Image-Removed>)

I have a ‘Reference’ option, so I choose this. The difference between ‘Duplicate’ and ‘Reference’ is subtle: if I choose ‘Reference’, the new query is based on the results of the first table, rather than replicating it entirely.

![](<Base64-Image-Removed>)

Thus, it looks just like my first table – I rename this table to ‘Expense Codes Substitutes’ so that it’s easier to understand its purpose. I remove the **_Name_** column as I am only interested in the expense codes for now.

![](<Base64-Image-Removed>)

I have too many similar entries, so in the ‘Reduce Rows’ section, I choose the ‘Remove Rows’ dropdown and select ‘Remove Duplicate Rows’.

![](<Base64-Image-Removed>)

My next step will be to decide which cells are standard entries and which are substitute entries. Now that my initial data has been reduced to unique values, I need to go back to Excel to indicate manually which values need to be substituted with a standard value. I close and load to the existing worksheet.

![](<Base64-Image-Removed>)

Next, I need to add a column to my new table called **_Substitute_** and reorganise my data so that Power Query can read what and when to substitute for each entered expense code.

![](<Base64-Image-Removed>)

I have indicated substitutes where appropriate (and deliberately missed one!) I now need to create a new query for my edited table:

![](<Base64-Image-Removed>)

I call the new query ‘Substitutes’ and create it as connection only (since I have not changed it, I don’t need to load it).

Back in the worksheet, I right-click my original query ‘Table1’ and join it to ‘Substitutes’, using the ‘Merge’ option. Since the data in ‘Substitutes’ came from ‘Table1’ this is known as _self-referencing_.

![](<Base64-Image-Removed>)

I select **_Expense Code_** from each table and choose the ‘Left Outer’ join option and click ‘OK’.

![](<Base64-Image-Removed>)

I can now expand my **_Substitutes_** column:

![](<Base64-Image-Removed>)

I only want the **_Substitute_** column from the ‘Substitutes’ table:

![](<Base64-Image-Removed>)

I can now delete the original **_Expense Code_** field and rename **_Substitute_** to be the new **_Expense Code_**… but wait, Mary has no substitute set up for ‘Sundries’ (see I missed one on purpose!). To show that everything can be refreshed, I continue with my deletion and renaming here, and load my query to the same worksheet.

![](<Base64-Image-Removed>)

I manually edit my ‘Substitutes’ table to make sure all the substitutes are populated (including ‘Sundries’), and refresh the data using the ‘Refresh All’ option on the ‘Data’ tab.

![](<Base64-Image-Removed>)

My data is now updated with standard expense code names. I will still need to maintain the substitute table, but I have no need to trawl through my data to find any non-standard entries that don’t already appear on my substitute table, as an update will add any unrecognised entries to my substitute table. To prove this, I add an ‘A4 folder’ to Paul’s expenses ready to add it to my table:

![](<Base64-Image-Removed>)

Obviously, the update is not quite sure how to treat the extra information in my manual table, but a line has appeared and I need to adjust the data. A new row has appeared for Paul in the final table. I simply update my manual table and refresh again.

![](<Base64-Image-Removed>)

All the data is now showing the correct expense code, as required.

Want to read more about Power Query? A complete list of all our Power Query blogs can be found [here](https://www.sumproduct.com/thought/power-query-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-cleanse-tone-and-upload/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-cleanse-tone-and-upload/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-cleanse-tone-and-upload/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-cleanse-tone-and-upload/#0)

[](https://sumproduct.com/blog/power-query-cleanse-tone-and-upload/#0 "close")

top