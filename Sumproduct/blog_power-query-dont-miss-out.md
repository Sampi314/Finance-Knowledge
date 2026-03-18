# Power Query: Don’t Miss Out

**Source:** https://sumproduct.com/blog/power-query-dont-miss-out/

---

[Home](https://sumproduct.com/)

\> Power Query: Don’t Miss Out

*   February 16, 2021

Power Query: Don’t Miss Out
===========================

Power Query: Don’t Miss Out
===========================

17 February 2021

_Welcome to our Power Query blog. This week, I look at the Excel.Workbook() M function_

UK readers may recall an embarrassing situation for the UK government last year when they ‘misplaced’ thousands of positive COVID-19 tests on an Excel worksheet! The good news for the rest of us, is that thanks to changes to the **Excel.Workbook()****M** function, data should be harder to lose. The full description of this function is as follows:

**Excel.Workbook(workbook** as binary, optional **UseHeaders** as any, optional **DelayTypes** as nullable logical**)** as table  

This function returns the contents of the Excel workbook, where:

*   **UseHeaders:**can be _null_ or a logical (true / false) value, indicating whether the first row of each returned table should be treated as a header or an options record (see below for more details on the options record). The default value is false.
*   **DelayTypes:** can also be _null_ or a logical (true / false) value, indicating whether the columns of each returned table should be left untyped. Again, the default value is false.

If an option record is specified for **UseHeaders** (and **DelayTypes** is _null_), this means if a file path or content is specified, _e.g._

**\= Excel.Workbook(\[Content\])**

then these parameters will be added as

**\= Excel.Workbook(\[Content\])\[UseHeaders…\].**

(There is another example later when I cover how to use the function to troubleshoot issues.)

In this case, the following record fields may be provided:

*   **UseHeaders****:** this may be _null_ or a logical (true / false) value, indicating whether the first row of each returned table should be treated as a header. And guess what? The default value is still false
*   **DelayTypes****:** this may be be _null_ or a logical (true / false) value, indicating whether the columns of each returned table should be left untyped. Just for a change the default value here is false too
*   **InferSheetDimensions****:** yet again, this may be _null_ or a logical (true / false) value, indicating whether the area of a worksheet that contains data should be inferred by reading the worksheet itself, rather than by reading the dimensions metadata from the file. This can be useful in cases where the dimensions metadata is incorrect. Note that this option is only supported for Open XML Excel files, not for legacy Excel files. The default value here is purple. Oh no, wait, I got that wrong, it’s false.

The parameter **InferSheetDimensions** should help to stop data from going missing. In the Microsoft Pages on troubleshooting, there is a section on checking if the dimensions are correct and how to fix them, including using the **InferSheetDimensions** parameter in **Excel.Workbook()**.

To view the dimensions of a worksheet:

1.  Rename the **.xlsx**_etc._ file with a **.zip** extension
2.  Open the file in File Explorer
3.  Navigate into xlworksheets
4.  Copy the **xml** file for the problematic sheet (for example, Sheet1.xml) out of the zip file to another location
5.  Inspect the first few lines of the file. If the file is small enough, open it in a text editor. If the file is too large to be opened in a text editor, run the following command from a Command Prompt: **more Sheet1.xml**
6.  Look for a **<dimension …/>** tag (for example, <dimension ref=”A1:C200″ />)
7.  If your file has a dimension attribute that points to a single cell (such as <dimension ref=”A1″ />), Power Query uses this attribute to find the starting row and column of the data on the sheet
8.  However, if your file has a dimension attribute that points to multiple cells (such as <dimension ref=”A1:AJ45000″/>), Power Query uses this range to find the starting row and column **as well as the ending row and column**. If this range doesn’t contain all the data on the sheet, some of the data will **_not_** be loaded.

To fix incorrect dimensions, you can remedy issues caused by incorrect dimensions by performing one of the following actions:

1.  Open and resave the document in Excel. This action will overwrite the incorrect dimensions stored in the file with the correct value
2.  Ensure the tool that generated the Excel file is fixed to output the dimensions correctly
3.  Update your **M** query to ignore the incorrect dimensions. As of the December 2020 release of Power Query, **Excel.Workbook()** now supports an **InferSheetDimensions** option. When true, this option will cause the function to ignore the dimensions stored in the workbook and instead determine them by inspecting the data instead.

Here’s an example of how to provide this option:

**Excel.Workbook(File.Contents(“C:MyExcelFile.xlsx”), \[DelayTypes = true, InferSheetDimensions = true\])**

Since Power Query automatically uses the dimensions when getting data from Excel worksheets, if there are problems, then this parameter will allow us to override them. This is not an issue when loading from tables or specified ranges. The problem is generally caused by software that creates Excel workbooks, hence the advice to “…ensure the tool that generated the Excel file is fixed to output the dimensions correctly…”. This may not be within the Power Query user’s control, so it’s useful to know that Power Query can bypass these issues.

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-dont-miss-out/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-dont-miss-out/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-dont-miss-out/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-dont-miss-out/#0)

[](https://sumproduct.com/blog/power-query-dont-miss-out/#0 "close")

top