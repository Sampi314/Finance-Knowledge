# Power Query: Split Folder Part 9

**Source:** https://sumproduct.com/blog/split-folder-part-9/

---

[Home](https://sumproduct.com/)

\> Power Query: Split Folder Part 9

*   May 28, 2025

Power Query: Split Folder Part 9
================================

Power Query: Split Folder Part 9
================================

28 May 2025

_Welcome to our Power Query blog. This week, I look at how I can convert a parameter extracted from the workbook into a Power Query parameter._

I have covered the topic of getting files from a folder in several blogs; the latest series was [Excel Files from a Folder Fiddle](https://sumproduct.com/blog/power-query-excel-files-from-a-folder-fiddle-part-3/)
. In this series, I will look at how I may extract files from a folder, where some of the files require different transformations to others. The folder shown below contains expense data for May 2024, but not all formats are the same:

![](https://sumproduct.com/wp-content/uploads/2025/06/5f18106373ad3af09a0b22abeb6dd9ef.jpg)

My task is to transform all the data and append into a single output Table.

In this series, I have used the ‘From Folder’ connector to extract data from the folder and transformed and filtered the filenames selected to create a Folder Filtered query. I then took reference copies of this query which I filtered for each file type and used the Combine functionality to bring the data together for each file type.

I appended my data to create a new query **Monthly Expense Data**, and sorted the data in ascending **Date** order:

![](https://sumproduct.com/wp-content/uploads/2025/06/0c2dfe2f867d4b292d6b7aed33d9570d.jpg)

In [Part 4](https://sumproduct.com/blog/split-folder-part-4/)
, I tested the process by changing and adding data.

In [Part 5](https://sumproduct.com/blog/split-folder-part-5/)
, I refined the process by using internal Power Query parameters in the **Folder Filtered** query.

![](https://sumproduct.com/wp-content/uploads/2025/06/622b678debe9b906931adea57ba7d244.jpg)

The values of the parameters were “EXPENSE” and “NDL”.

![](https://sumproduct.com/wp-content/uploads/2025/06/deae47cdfb0c60e0fe08b6437904ca4d.jpg)

When I clicked OK, the query looked the same, but I was using parameters for the ‘Filtered Rows’ step:

![](https://sumproduct.com/wp-content/uploads/2025/06/9d7a9298a9d88752d1d60e952aa772e2.jpg)

In [Part 6](https://sumproduct.com/blog/split-folder-part-6/)
, I investigated what happened if there wasn’t a file selected of each type and I changed the queries **XLSM Files**, **TXT Files** and **CSV Files** to always have at least one row and changed **Monthly Expense Data** so that it would ignore the extra column and _null_ row that the solution could produce.

Whilst having internal Power Query parameters is better than hard coding, this is only suitable for users who are comfortable using Power Query. In [Part 7](https://sumproduct.com/blog/split-folder-part-7/)
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

This made the process easier for the users to change, but it does leave several questions: why can’t I pick the parameters I have created in the ‘Filtered Rows’ step? Is there a way to make these parameters look like Power Query parameters so we can select them? Yes there is, though it does involve some **M** code.

[Last time](https://sumproduct.com/blog/split-folder-part-8/)
, I compared the existing **M** code in the Advanced Editor for **XLSM\_String** and **P\_XL\_XLSM,** and found that **XLSM\_String** had been defined as a Power Query parameter by assigning metadata values.

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

If I want **P\_XL\_XLSM** to be treated like a Power Query parameter I need to assign metadata so that it has the properties of a parameter. Currently, the **M** code for **P\_XL\_XLSM** is:

**let**

    **Source =  
Excel.CurrentWorkbook(){\[Name=”P\_XL\_XLSM”\]}\[Content\],**

    **Column1 = Source{0}\[Column1\]**

**in**

    **Column1**

I need to take the final value and assign metadata values so that it has the same properties as a Power Query parameter, using code similar to the **M** code for **XLSM\_String**, which is:

**“MARY” meta  
\[IsParameterQuery=true, Type=”Text”, IsParameterQueryRequired=true\]**

My first attempt was to add a step:

**Convert\_to\_Parameter = Column1  
\[IsParameterQuery=true, Type=”Text”, IsParameterQueryRequired=true\]**

This triggered a syntax error:

![](<Base64-Image-Removed>)

I tried skipping the step name, but this is not allowed in a query:

![](<Base64-Image-Removed>)

Next, I decided to mimic the Power Query parameter by entering a new Blank Query:

![](<Base64-Image-Removed>)

When I selected Done, the results look promising. I can’t see the value of the parameter, but it does look like a parameter!

![](<Base64-Image-Removed>)

I rename **Query5** to **Param\_XL\_XLSM**.

![](<Base64-Image-Removed>)

The value is not shown here either. I try using it in the **Folder Filtered** query:

![](<Base64-Image-Removed>)

It works when I enter it in the **M** code, so I try using the cog next to the ‘Filtered Rows’ step to see if I may select it from there:

![](<Base64-Image-Removed>)

It is recognised and I may select it in the dialog. Note that the second parameter **P\_XL\_TXT** is not shown as this is still a query rather than a Power Query parameter.

**Param\_XL\_XLSM** will be updated whenever the user changes the value in the workbook since it uses the **P\_XL\_XLSM** parameter. The only issue is that the value of **Param\_XL\_XLSM** is not displayed since it is using the result of a query as the value.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/split-folder-part-9/#0)
    
*   [Register](https://sumproduct.com/blog/split-folder-part-9/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/split-folder-part-9/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/split-folder-part-9/#0)

[](https://sumproduct.com/blog/split-folder-part-9/#0 "close")

top