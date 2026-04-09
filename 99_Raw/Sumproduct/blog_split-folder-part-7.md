# Power Query: Split Folder Part 7

**Source:** https://sumproduct.com/blog/split-folder-part-7/

---

[Home](https://sumproduct.com/)

\> Power Query: Split Folder Part 7

*   May 14, 2025

Power Query: Split Folder Part 7
================================

Power Query: Split Folder Part 7
================================

14 May 2025

_Welcome to our Power Query blog. This week, I extract the parameters from the Excel workbook._

I have covered the topic of getting files from a folder in several blogs; the latest series was [Excel Files from a Folder Fiddle](https://sumproduct.com/blog/power-query-excel-files-from-a-folder-fiddle-part-3/)
. In this series, I will look at how I may extract files from a folder, where some of the files require different transformations to others. The folder shown below contains expense data for May 2024, but not all formats are the same:

![](https://sumproduct.com/wp-content/uploads/2025/06/d7c7cb34f641bf33a882be069f503ec8.jpg)

My task is to transform all the data and append into a single output Table.

In [Part 1](https://sumproduct.com/blog/split-folder-part-1/)
, I used the ‘From Folder’ connector to extract data from the folder and transformed / filtered the data to ensure I only had the expense data.

![](https://sumproduct.com/wp-content/uploads/2025/06/81f32e77ba234b668c7d54f4d3ad5363.jpg)

I took three \[3\] reference copies of **Folder Filtered**, one for each file type:

![](https://sumproduct.com/wp-content/uploads/2025/06/e6e0a4d30384df2a60b196b4481c3ef8.jpg)

In [Part 2](https://sumproduct.com/blog/split-folder-part-2/)
, I transformed the data in **XLSM Files** and **TXT Files**.

![](https://sumproduct.com/wp-content/uploads/2025/06/4971f0b5e57c3d2e43ececc401cb23da.jpg)

![](https://sumproduct.com/wp-content/uploads/2025/06/30af7ca48d7435760a40406d2e99e559.jpg)

In [Part 3](https://sumproduct.com/blog/split-folder-part-3/)
, I transformed the **CSV Files**. Currently, there is only one CSV file, but I assume that there could be more when I refresh the data, so I used the ‘Combine Files’ approach.

![](https://sumproduct.com/wp-content/uploads/2025/06/db343fb1913586945ceb7b43575c8a86.jpg)

I appended my data to create a new query **Monthly Expense Data**, and sorted the data in ascending **Date** order:

![](https://sumproduct.com/wp-content/uploads/2025/06/8a559e2ac84b93c1aff973c58d3e1e69.jpg)

In [Part 4](https://sumproduct.com/blog/split-folder-part-4/)
, I tested the process by changing and adding data.

In [Part 5](https://sumproduct.com/blog/split-folder-part-5/)
, I refined the process by using internal Power Query parameters in the **Folder Filtered** query.

![](https://sumproduct.com/wp-content/uploads/2025/06/4747b9b12160ade7106b95049abc98a6.jpg)

The values of the parameters were “EXPENSE” and “NDL”.

![](https://sumproduct.com/wp-content/uploads/2025/06/f3ed38c7170c56a89dc9e039959e0720.jpg)

When I clicked OK, the query looked the same, but I was using parameters for the ‘Filtered Rows’ step:

![](<Base64-Image-Removed>)

[Last time](https://sumproduct.com/blog/split-folder-part-6/)
, I investigated what happened if there wasn’t a file selected of each type and I changed the queries **XLSM Files**, **TXT Files** and **CSV Files** to always have at least one row and changed **Monthly Expense Data**, so that it would ignore the extra column and _null_ row that the solution could produce.

Whilst having internal Power Query parameters is better than hard coding, this is only suitable for users who are comfortable using Power Query. This time, I’ll look at getting the data from the Excel worksheet instead.

On a new worksheet, which I call ‘Inputs’, I create two labels and two named ranges.

![](<Base64-Image-Removed>)

The named ranges are **P\_XL\_XLSM** and **P\_XL\_TXT**. I right-click on cell C4, and choose to ‘Get Data from Table/Range’:

![](<Base64-Image-Removed>)

This gives me a new query **P\_XL\_XLSM**:

![](<Base64-Image-Removed>)

I don’t want the default steps, so I delete ‘Changed Type’ and ‘Promoted Headers’. I right-click on the cell and choose to ‘Drill Down’:

![](<Base64-Image-Removed>)

This gives me a single value for **P\_XL\_XLSM**:

![](<Base64-Image-Removed>)

I repeat this process for **P\_XL\_TXT**:

![](<Base64-Image-Removed>)

Since these queries each contain one data item, the icon is text. Note that they do not look like the parameters I created in [Part 5](https://sumproduct.com/blog/split-folder-part-5/)
.

![](<Base64-Image-Removed>)

If I go back to the **Folder Filtered** query and use the cog next to the ‘Filtered Rows’ step, I am not able to select the parameters from the Excel worksheet:

![](<Base64-Image-Removed>)

To use these filters, I must adjust the **M** code in the step instead. I change it from:

**\=  
Table.SelectRows(#”Uppercased Text”, each Text.Contains(\[Name\],  
XLSM\_String) or Text.Contains(\[Name\], TXT\_String))**

to

**\= Table.SelectRows(#”Uppercased  
Text”, each Text.Contains(\[Name\], P\_XL\_XLSM) or Text.Contains(\[Name\],  
P\_XL\_TXT))**

Note that the IntelliSense does recognise the new parameters:

![](<Base64-Image-Removed>)

The output remains the same:

![](<Base64-Image-Removed>)

If the user changes one of the values in the ‘Inputs’ sheet, the filter changes when the query is refreshed:

![](<Base64-Image-Removed>)

This will make the process easier for the users to change, but it does leave the question: why can’t I pick the parameters I have created in the ‘Filtered Rows’ step? Is there a way to make these parameters look like Power Query parameters so we can select them? Yes, there is, and I’ll cover this next time.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/split-folder-part-7/#0)
    
*   [Register](https://sumproduct.com/blog/split-folder-part-7/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/split-folder-part-7/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/split-folder-part-7/#0)

[](https://sumproduct.com/blog/split-folder-part-7/#0 "close")

top