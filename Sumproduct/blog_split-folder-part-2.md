# Power Query: Split Folder Part 2

**Source:** https://sumproduct.com/blog/split-folder-part-2/

---

[Home](https://sumproduct.com/)

\> Power Query: Split Folder Part 2

*   April 9, 2025

Power Query: Split Folder Part 2
================================

Power Query: Split Folder Part 2
================================

9 April 2025

_Welcome to our Power Query blog. This week, I begin to_ _transform the data for the file type queries._

I have covered the topic of getting files from a folder in several blogs; the latest series was [Excel Files from a Folder Fiddle](https://sumproduct.com/blog/power-query-excel-files-from-a-folder-fiddle-part-3/)
. In this series, I will look at how I may extract files from a folder, where some of the files require different transformations to others. The folder shown below contains expense data for May 2024, but not all formats are the same:

![](<Base64-Image-Removed>)

My task is to transform all the data and append into a single output Table.

[Last time](https://sumproduct.com/blog/split-folder-part-1/)
, I used the ‘From Folder’ connector to extract data from the folder and transformed and filtered the data to ensure I only had the expense data.

![](<Base64-Image-Removed>)

I took three \[3\] reference copies of **Folder Filtered**, one for each file type:

![](<Base64-Image-Removed>)

This time, I will transform the data in these new queries. Since I have already filtered to keep only those files associated with expenses, I begin by filtering on the **Extension** column. I will start with the **XLSM Files** query:

![](<Base64-Image-Removed>)

Since the XLSM files all have the same sheet name, I may use the ‘Combine Files’ icon to combine the data:

![](<Base64-Image-Removed>)

I use the sheet rather than the Table to ensure that all the files will be accessed:

![](<Base64-Image-Removed>)

The files in my example only contain one sheet: ‘Expenses’. I click OK to continue:

![](<Base64-Image-Removed>)

The algorithms create the **Transform File from XLSM Files** folder, containing the helper queries and created steps in **XLSM Files** which have combined the data. I may fill down in the **Name** column in **Transform Sample File** or **XLSM Files**.

![](<Base64-Image-Removed>)

The **XLSM Files** query is complete:

![](<Base64-Image-Removed>)

I repeat the combine process for **TXT Files**:

![](<Base64-Image-Removed>)

For this example, it makes more sense for me to apply the transformations to **Transform Sample File (2)**. To make the process clearer, I rename the helper files to reflect the file type:

![](<Base64-Image-Removed>)

Note that, although the value in brackets doesn’t change to reflect the new name, the parameters do reference the correct files. This is a bug!

I may now make my changes to **TXT\_Transform Sample File**. I begin by merging **Column2** and **Column3** to get the expense title and data into the same column:

![](<Base64-Image-Removed>)

I would like to keep the columns I need by selecting them and choosing to ‘Remove Other Columns’.

![](<Base64-Image-Removed>)

I now need to create a ‘Conditional Column’ from the ‘Add Column’ tab:

![](<Base64-Image-Removed>)

I fill down on the **Name** column:

![](<Base64-Image-Removed>)

Row 7 will eventually be the column headers. I must avoid having a column name featuring “John Smythe” as it would appear in a rename step, and this will not exist for the other expense files. I need another conditional column:

![](<Base64-Image-Removed>)

This will set the value in **Name Generic** to the text “Name” for the row containing the headings, otherwise it will contain the value in the column **Name**:

![](<Base64-Image-Removed>)

I may now remove the **Name** column and the first six \[6\] rows, and promote the first row into the headings:

![](<Base64-Image-Removed>)

All that remains is to ‘Replace Values’ in the Name column, and replace the string “Name:” with nothing:

![](<Base64-Image-Removed>)

There is a warning sign on the **TXT Files** query. There is an error:

![](<Base64-Image-Removed>)

**Column1** cannot be found! If I go to the ‘Expanded Table Column1’ step, I can see that there is indeed no **Column1**. This can be fixed by removing the ‘Changed Type’ step:

![](<Base64-Image-Removed>)

I delete the step, select all the columns and ‘Detect Data Type’ from the Transform tab:

![](<Base64-Image-Removed>)

My data is ready to append. Next time, I’ll transform **CSV Files**.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/split-folder-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/split-folder-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/split-folder-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/split-folder-part-2/#0)

[](https://sumproduct.com/blog/split-folder-part-2/#0 "close")

top