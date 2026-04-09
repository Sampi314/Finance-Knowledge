# Power Query: Flexible Appending – Part 2

**Source:** https://sumproduct.com/blog/power-query-flexible-appending-part-2/

---

[Home](https://sumproduct.com/)

\> Power Query: Flexible Appending – Part 2

*   November 8, 2022

Power Query: Flexible Appending – Part 2
========================================

Power Query: Flexible Appending – Part 2
========================================

9 November 2022

_Welcome to our Power Query blog. This week, I am continuing to combine data from a folder and to use a translation table to create column names._

You may recall from [last week](https://sumproduct.com/blog/power-query-flexible-appending-part-1/)
 I have three \[3\] Excel workbooks, each with some accounting data. The first file looks like this:

![](https://sumproduct.com/wp-content/uploads/2025/05/19e328d265a42a9cb6c87542777afb5b.jpg)

The second file looks like this:

![](https://sumproduct.com/wp-content/uploads/2025/05/c11aa03c5204741e93bd57f00e21cd30.jpg)

The final file looks like this:

![](https://sumproduct.com/wp-content/uploads/2025/05/fa373774567327552b208b407c824e36.jpg)

There are clearly some differences between the files. The column headings vary by country, and the first file has an extra column.

My goal is to get this data into the same table. For the purposes of this example, I am not required to convert the figures to the same currency. However, I do need to allow for more files appearing from other countries. The files are held in one folder. I have a translation table **Column List** in a separate Excel workbook (shown below) to help me determine the column names in the final table. No other columns are required apart from the ‘entity’ name (_e.g_. ‘Entity 1’).

![](https://sumproduct.com/wp-content/uploads/2025/05/e84db8ebe7576e0d149aadf3d163783d.jpg)

[Last week](https://sumproduct.com/blog/power-query-flexible-appending-part-1/)
 I created a query **ColumnList**:

![](https://sumproduct.com/wp-content/uploads/2025/05/3ecc40fabaa0338bf43df7d105b7b653.jpg)

I also created a parameter called **FolderPath**. The ‘Current Value’ of the parameter is the folder path containing the files that I am going to append.

![](https://sumproduct.com/wp-content/uploads/2025/05/03a43363192c260589d10d8264e87bd7.jpg)

I also created and transformed a query **Transform Sample File**, which will act as the basis for the transformation that I need to apply to each Excel workbook in the folder.

![](https://sumproduct.com/wp-content/uploads/2025/05/c0b1720581f1a0e8c63263077a4dc9bf.jpg)

This week, I will standardise the column names. I add a new blank step with the following **M** code:

**\= Table.FromList(Table.ColumnNames(#”Filtered Rows”))**

The function **Table.ColumnNames()** gets a list of column names from the ‘Filtered Rows’ step and **Table.FromList()** then converts that list into a table. I rename this step to ‘ColNames’, _viz._

![](<Base64-Image-Removed>)

Next, I add a custom column with the following **M** code:

**\= Table.SelectRows(ColumnList,(row) =>  
Text.Contains(\[Column1\], row\[From\]))**

**Table.SelectRows** filters a table by a condition. The first argument is table **ColumnList** while the second one contains a function denoted by ‘**() =>**‘ syntax (you should note there cannot be a space between the equals sign (=) and the greater than sign (>)).

This means that for each row in table **ColumnList**, **Text.Contains** checks whether **Column1** of the current step contains the value in column **From** in table **ColumnList**. It results in a TRUE / FALSE value which is a condition for the filter.

![](<Base64-Image-Removed>)

This **Custom** column generates tables containing rows that meet the condition.

![](<Base64-Image-Removed>)

Within these tables, I would like to get the first value of column **To** by adding “**\[To\]{0}**” to the end of the **M** code.

**Table.SelectRows( ColumnList, (row) => Text.Contains(\[Column1\],  
row\[From\]) )\[To\]{0}**

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

There are some errors for those columns which have no matches from **ColumnList**. I don’t need these columns, so I right-click and apply ‘Remove Errors’ to the **Custom** column, which means I am left with a list of columns I want to keep without hardcoding any column names.

![](<Base64-Image-Removed>)

Next time, I will complete the example by applying the list of from and to values to each of the extracted Excel sheets.

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-flexible-appending-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-flexible-appending-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-flexible-appending-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-flexible-appending-part-2/#0)

[](https://sumproduct.com/blog/power-query-flexible-appending-part-2/#0 "close")

top