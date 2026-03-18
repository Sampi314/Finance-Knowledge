# Power Query: Excel Files from a Folder Fiddle – Part 2

**Source:** https://sumproduct.com/blog/power-query-excel-files-from-a-folder-fiddle-part-2/

---

[Home](https://sumproduct.com/)

\> Power Query: Excel Files from a Folder Fiddle – Part 2

*   November 14, 2023

Power Query: Excel Files from a Folder Fiddle – Part 2
======================================================

Power Query: Excel Files from a Folder Fiddle – Part 2
======================================================

15 November 2023

_Welcome to our Power Query blog. Today, I look at how to resolve an issue I encountered recently when importing Excel files from a folder._

In [Power Query: Returning to the Folder](https://sumproduct.com/blog/power-query-returning-to-the-folder/)
, I looked at how the process to import files from a folder had been made easier by using the ‘Combine Files’ functionality:

![](https://sumproduct.com/wp-content/uploads/2025/05/607f8a35b3fb4819bb22932e5d62c20f.jpg)

This worked successfully for a folder of **CSV** (comma delimited) files.

![](https://sumproduct.com/wp-content/uploads/2025/05/d1a0761f8b8c4d623be4c6103179a0e9.jpg)

The files and functions in the ‘Helper Queries’ folder worked, and my data was successfully combined. However, when I have some Excel files in a folder, the process [last time](https://sumproduct.com/blog/power-query-excel-files-from-a-folder-fiddle-part-1/)
 did not go so smoothly.

![](https://sumproduct.com/wp-content/uploads/2025/05/d02a4bd750957fdaf71003d1657045ae.jpg)

I have a red wavy line under my headings, and a row of errors instead of the rest of the data in the folder. I only have one sheet of data from the first Excel file. If I click on the error, the message is not helpful:

![](https://sumproduct.com/wp-content/uploads/2025/05/84815af63a585d1fc04d0e43bca224c2.jpg)

The first step with this error is ‘Invoke Custom Function1’:

![](https://sumproduct.com/wp-content/uploads/2025/05/fafe5d53496f83e3bd7f5dbad84052ce.jpg)

This has failed to extract the second and third tables. Since the Power Query combine method has failed, I need to find another way to append my data together.

I start by removing the steps after ‘Filtered Hidden Files1’. I can do this by right-clicking on step ‘Invoke Custom Function1’, and choosing to ‘Delete Until End’:

![](https://sumproduct.com/wp-content/uploads/2025/05/6c8b8163efcb59928de68964b781bb2c.jpg)

I receive a warning, and I choose to ‘Delete’:

![](https://sumproduct.com/wp-content/uploads/2025/05/d5415a6881aa3b0e620b59b9cf9669f4.jpg)

I can also remove the queries that Power Query created by removing the **Transform File from PQ\_StandardExpenses\_Excel** group.

![](<Base64-Image-Removed>)

Again, I receive a warning, but I choose to ‘Delete’:

![](<Base64-Image-Removed>)

Now I have removed everything I no longer need; I can create the tables. To see how I would do this, I click on the first ‘Binary’ object in the **Content** column:

![](<Base64-Image-Removed>)

This extracts the contents of the first Excel workbook:

![](<Base64-Image-Removed>)

To get the sheets for all my Excel files, I need to put this solution into a ‘Custom Column’, which I can create from the ‘Add Column’ tab:

![](<Base64-Image-Removed>)

This creates a new column **Extract the Contents**:

![](<Base64-Image-Removed>)

I can expand each Table by using the expand icon next to the heading on **Extract the Contents**:

![](<Base64-Image-Removed>)

I am only interested in the **Data** column, so as I did for **Content**, I select it and right-click to remove other columns:

![](<Base64-Image-Removed>)

I can now extract the data from the tables using the icon next to the **Data** heading.

![](<Base64-Image-Removed>)

I wish to extract all the columns, and I don’t need to ‘Use original column name as prefix’:

![](<Base64-Image-Removed>)

This time, there are no errors! I need to promote the headings using ‘Use First Row as Headers’ from the Home tab:

![](<Base64-Image-Removed>)

I can remove the extra headings by changing the datatype of **Date** to a date. This gives me errors in the **Date** column for the unwanted headings rows:

![](<Base64-Image-Removed>)

I should also change **amount** to a decimal number: this too results in errors in the **amount** column.

![](<Base64-Image-Removed>)

I can right-click on the **Date** column and ‘Remove Errors’:

![](<Base64-Image-Removed>)

Now, I can fill down in the **Name** column, using the option on the right-click menu or the option on the Transform tab:

![](<Base64-Image-Removed>)

My query is complete:

![](<Base64-Image-Removed>)

Although Power Query is being updated to try to help users complete tasks more easily, sometimes things do not go as planned, and we need to go back to the method we used before the improvements had been added. Next time, I will look at what went wrong when I combined binaries using the Power Query helper queries.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-excel-files-from-a-folder-fiddle-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-excel-files-from-a-folder-fiddle-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-excel-files-from-a-folder-fiddle-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-excel-files-from-a-folder-fiddle-part-2/#0)

[](https://sumproduct.com/blog/power-query-excel-files-from-a-folder-fiddle-part-2/#0 "close")

top