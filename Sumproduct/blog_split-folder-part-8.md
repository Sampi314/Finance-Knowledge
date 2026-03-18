# Power Query: Split Folder Part 8

**Source:** https://sumproduct.com/blog/split-folder-part-8/

---

[Home](https://sumproduct.com/)

\> Power Query: Split Folder Part 8

*   May 21, 2025

Power Query: Split Folder Part 8
================================

Power Query: Split Folder Part 8
================================

21 May 2025

_Welcome to our Power Query blog. This week, I examine the difference between the types of parameters I have been using._

I have covered the topic of getting files from a folder in several blogs; the latest series was [Excel Files from a Folder Fiddle](https://sumproduct.com/blog/power-query-excel-files-from-a-folder-fiddle-part-3/)
. In this series, I will look at how I may extract files from a folder, where some of the files require different transformations to others. The folder shown below contains expense data for May 2024, but not all formats are the same:

![](<Base64-Image-Removed>)

My task is to transform all the data and append into a single output Table.

In this series, I have used the ‘From Folder’ connector to extract data from the folder and transformed and filtered the filenames selected to create a Folder Filtered query. I then took reference copies of this query which I filtered for each file type and used the Combine functionality to bring the data together for each file type.

I appended my data to create a new query **Monthly Expense Data**, and sorted the data in ascending **Date** order:

![](<Base64-Image-Removed>)

In [Part 4](https://sumproduct.com/blog/split-folder-part-4/)
, I tested the process by changing and adding data.

In [Part 5](https://sumproduct.com/blog/split-folder-part-5/)
, I refined the process by using internal Power Query parameters in the **Folder Filtered** query.

![](<Base64-Image-Removed>)

The values of the parameters were “EXPENSE” and “NDL”.

![](<Base64-Image-Removed>)

When I clicked OK, the query looked the same, but I was using parameters for the ‘Filtered Rows’ step:

![](<Base64-Image-Removed>)

In [Part 6](https://sumproduct.com/blog/split-folder-part-6/)
, I investigated what happened if there wasn’t a file selected of each type and I changed the queries **XLSM Files**, **TXT Files** and **CSV Files** to always have at least one row and changed **Monthly Expense Data** so that it would ignore the extra column and _null_ row that the solution could produce.

Whilst having internal Power Query parameters is better than hard coding, this is only suitable for users who are comfortable using Power Query. [Last time](https://sumproduct.com/blog/split-folder-part-7/)
, I changed the process to use cells from the Excel workbook for the parameters.

![](<Base64-Image-Removed>)

Note that they do not look like the parameters I created in [Part 5](https://sumproduct.com/blog/split-folder-part-5/)
.

![](<Base64-Image-Removed>)

If I go back to the **Folder Filtered** query and use the cog next to the ‘Filtered Rows’ step, I am not able to select the parameters from the Excel worksheet:

![](<Base64-Image-Removed>)

To use these filters, I must adjust the **M** code in the step instead. I change it from

**\=  
Table.SelectRows(#”Uppercased Text”, each Text.Contains(\[Name\],  
XLSM\_String) or Text.Contains(\[Name\], TXT\_String))**

to

**\=  
Table.SelectRows(#”Uppercased Text”, each Text.Contains(\[Name\],  
P\_XL\_XLSM) or Text.Contains(\[Name\], P\_XL\_TXT))**

Note that the IntelliSense does recognise the new parameters:

![](<Base64-Image-Removed>)

The output remains the same:

![](<Base64-Image-Removed>)

This made the process easier for the users to change, but it does leave several questions: why can’t I pick the parameters I have created in the ‘Filtered Rows’ step? Is there a way to make these parameters look like Power Query parameters so we may select them? Yes there is, though it does involve some **M** code.

Let’s start by comparing the existing **M** code in the Advanced Editor for **XLSM\_String** and **P\_XL\_XLSM.**

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

The **M** code for **XLSM\_String** is:

**“MARY” meta \[IsParameterQuery=true,  \
Type=”Text”, IsParameterQueryRequired=true\]**

whereas the **M** code for **P\_XL\_XLSM** is

**let**

    **Source =  
Excel.CurrentWorkbook(){\[Name=”P\_XL\_XLSM”\]}\[Content\],**

    **Column1 = Source{0}\[Column1\]**

**in**

    **Column1**

The **M** code for **P\_XL\_XLSM** is easy to follow:

*   the Source step extracts the cell identified by the Named Range **P\_XL\_XLSM**
*   the ‘Column1’ step then drills down into the value in the cell.

The **M** code for **XLSM\_String** may seem less familiar. This is defining metadata for the parameter. In a new Blank Query, I may query the existing metadata for **XLSM\_String**:

![](<Base64-Image-Removed>)

The **M** code I have used is:

**\= Value.Metadata(XLSM\_String)**

The syntax for **Value.Metadata** is:

**Value.Metadata(value as any) as any**

The function returns a record containing the metadata of **value**. If I try to do this for **P\_XL\_XLSM** I get a different result:

![](<Base64-Image-Removed>)

This means that **P\_XL\_XLSM** is a query and the only metadata available relates to whether it may be folded. I may view this metadata by clicking on the word “Record” in the previous image.

![](<Base64-Image-Removed>)

For more on query folding, please see [Power Query: Folding Table](https://sumproduct.com/blog/power-query-folding-table/)
.

If I want **P\_XL\_XLSM** to be treated like a Power Query parameter, I need to assign metadata so that it has the properties of a parameter. As I will show next time, this is possible, although it does not get treated _exactly_ like a parameter created from the User Interface.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/split-folder-part-8/#0)
    
*   [Register](https://sumproduct.com/blog/split-folder-part-8/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/split-folder-part-8/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/split-folder-part-8/#0)

[](https://sumproduct.com/blog/split-folder-part-8/#0 "close")

top