# Power Query: The Delete Dilemma

**Source:** https://sumproduct.com/blog/power-query-the-delete-dilemma/

---

[Home](https://sumproduct.com/)

\> Power Query: The Delete Dilemma

*   July 21, 2020

Power Query: The Delete Dilemma
===============================

Power Query: The Delete Dilemma
===============================

22 July 2020

_Welcome to our Power Query blog. This week. I look at data from a sheet made up of a number of tables, with a random amount of data that needs to be excluded._

Mary, one of my imaginary salespeople, has sent in a slightly unusual report of the tents available from a particular supplier.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-177-1.jpg)

I want to put the tent, supplier and report date into a table, and delete the lines at the top (there will be an unknown number of these). I begin by extracting my data to Power Query, using ‘From Table’ on the ‘Get & Transform’ section of the Data tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-165-1.jpg)

The ‘Create Table’ dialog box tries to default to the table I happen to be in, but I need to change this to include all of my data; instead of using ‘From Table’, I will adopt another approach.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-159-1.jpg)

I select ‘From Workbook’ in the dropdown from the ‘From File’ option on the ‘New Query’ options, and select my current workbook.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-141-1.jpg)

I select the sheet.

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-120-1.jpg)

I can see that all my data has been included; I can now choose to ‘Transform Data’.

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-100-1.jpg)

Power Query has automated some steps, but I don’t want to include most of them, so I delete all steps after the ‘Navigation’ step.

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-87-1.jpg)

I need to remove the top rows, but I want to avoid specifying how many of these rows there are. I plan to delete all rows above the date value. I begin by adding an index from the ‘Add Column’ tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/b9ee28d90e6b5bc92ea4aeafdad51628-70-1.jpg)

Next, I create a duplicate column of **Column3** (which contains the report date value) on the ‘Add Column’ tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/0485ccbc83bdeec1d741bad442a1ea5f-56-1.jpg)

In order to get rid of all the data apart from the date, I convert **Column3 – Copy** to Data Type ‘Date’. This may be done from the Transform tab.

![](<Base64-Image-Removed>)

This means that apart from the date, the data values are now either _null_ or _Error_. If I right-click my column, I can replace the errors with _null_ values.

![](<Base64-Image-Removed>)

This gives me _null_ values, and I can now fill down by right-clicking, choosing to ‘Fill’ and then choosing to ‘Fill Down’. The rows above the date do not matter as I want to delete them.

![](<Base64-Image-Removed>)

I need to delete the _null_ value rows, so I filter and choose values that are not _null_.

![](<Base64-Image-Removed>)

This gives me the rows with a date value.

![](<Base64-Image-Removed>)

I have the date column. Now, I want to get the supplier into a column. I create another duplicate of **Column3**:

![](<Base64-Image-Removed>)

I convert the Data Type on my new column to ‘Date’ because I want to isolate the value with the date.

![](<Base64-Image-Removed>)

I create a new conditional column from the ‘Add Column’ tab.

![](<Base64-Image-Removed>)

If the value is not _null_, then I want to put the supplier from **Column2** into my new column, which I call **Supplier**. The values with errors will remain as errors.

![](<Base64-Image-Removed>)

I can now right-click on **Supplier** and replace the errors with _null_.

![](<Base64-Image-Removed>)

Having done this, I can fill down my **Supplier**, as before.

![](<Base64-Image-Removed>)

I have one more row to remove, and I can do this by filtering on **Column1** to remove _null_ values.

![](<Base64-Image-Removed>)

I have one final row to delete, but this time it has values in all columns.

![](<Base64-Image-Removed>)

The data I need in the top row has already been moved to columns. I could just delete the top row, but instead I choose to identify it by creating a new conditional column.

![](<Base64-Image-Removed>)

I choose to create a new column which will indicate a row should be deleted if the value in **Supplier** matches the value in **Column2**.

![](<Base64-Image-Removed>)

I can then filter the **Delete Me** column to remove everything that isn’t _null_.

![](<Base64-Image-Removed>)

I now consider the column headings, but first I want to remove **Column3 – Copy1** because the errors might cause problems. I also remove my other temporary columns at the same time.

![](<Base64-Image-Removed>)

I can now promote the first row to headers from the Transform tab.

![](<Base64-Image-Removed>)

I just need to tweak the supplier and date headings.

![](<Base64-Image-Removed>)

My final step is to ‘Close & Load’ my data into Excel.

![](<Base64-Image-Removed>)

If I go back and alter the data by adding some extra rows to be deleted, I can check my transformation.

![](<Base64-Image-Removed>)

I create another line at the top and an extra space before the tent data. Then, I refresh the query.

![](<Base64-Image-Removed>)

The extra lines appear in the source.

![](<Base64-Image-Removed>)

The data is still transformed correctly.

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-the-delete-dilemma/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-the-delete-dilemma/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-the-delete-dilemma/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-the-delete-dilemma/#0)

[](https://sumproduct.com/blog/power-query-the-delete-dilemma/#0 "close")

top