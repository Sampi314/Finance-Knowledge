# Excel for Mac: Power Query – Creating Data Types

**Source:** https://sumproduct.com/blog/excel-for-mac-power-query-creating-data-types/

---

[Home](https://sumproduct.com/)

\> Excel for Mac: Power Query – Creating Data Types

*   March 7, 2025

Excel for Mac: Power Query – Creating Data Types
================================================

_This week in our series about Microsoft Excel for Mac, we show an easy way to overcome a limitation of Power Query in Excel for Mac.  As of February 2025, Power Query on Mac does not have the ‘Create Data Type’ button.  No problem!  Keep reading to find out how to create data types without the button._

If you use Excel for Mac, and you’ve been watching the gradual introduction of Power Query features over the last few years, you know that it doesn’t have all the capabilities that it has on Windows.  The Excel team has been adding more and more capability to Mac, but it’s still missing some key features.  One in particular is the ‘Create Data Type’ button on the Transform tab of the Power Query Editor. 

![](https://sumproduct.com/wp-content/uploads/2025/06/image-84.png)

Fortunately, this shouldn’t hold you back if you want to create data types in your queries.  Just follow the simple steps below.  This assumes that you have a query already, but if you want to create a query to bring data from a table/range so you can turn it into a data type, check our article about how to do that on Mac – [Excel for Mac: Power Query – From Table/Range](https://www.sumproduct.com/blog/article/excel-for-mac-power-query-from-table-range)

Begin by opening the Power Query Editor, which you can do by pressing **Opt**+**F12** or by going to the Data tab of the ribbon and opening the ‘Get Data (Power Query)’ menu.  Choose ‘Launch Power Query Editor…’

![](https://sumproduct.com/wp-content/uploads/2025/06/image-85.png)

In the Power Query Editor window, choose the query that you want to use to create a data type.

In the ‘Applied Steps’ choose the step that has the table of data in the form that you want.

NOTE: Complete any steps required to clean the data before you continue with the step below that will create a data type.

Add a step to the query, by right-clicking on the selected step and choosing ‘Insert step after’.

![](<Base64-Image-Removed>)

Click into the formula bar for that step and replace the contents with the following code:

**Table.CombineColumnsToRecord(#”PreviousStep”, “Name”, {“Name”, “Column1”, “Column2”, “Column3″}, \[DisplayNameColumn=”Name”, TypeName=”Excel.DataType”\])**

You need to replace the previous step name and the column names so that it works with your data.  Inside the curly brackets, you can specify only the columns that you want to add to the data type.  Other columns will be kept as is.  For this example, we’ll use the following table, which has columns **Item, ItemId, Suggested Price** and **Price Level**.  The previous step name in our example is ‘ReorderedCols’.

![](<Base64-Image-Removed>)

In our example, the step becomes:

**Table.CombineColumnsToRecord(#”ReorderedCols”, “Item”, {“Item”, “ItemId”, “Suggested Price”, “Price Level”}, \[DisplayNameColumn=”Item”, TypeName=”Excel.DataType”\])**

We made these changes:

*   **PreviousStep** was replaced with **ReorderedCols**.
*   **Name** was replaced with **Item** (this was replaced in three \[3\] places).
*   **Column1** was replaced with **ItemId**.
*   **Column2** was replaced with **Suggested Price**.
*   **Column3** was replaced with **Price Level**.

Having made the replacements, press **RETURN** to commit the changes to that step.  If you wish, you may rename the step if you want, since it likely has a name such as ‘Custom**.’**  In this example we have called it ‘Created Data Type’.  The column **Item** that contains the data type will now just show ‘\[Record\]’ in each row.  Don’t worry about that.  When the data gets loaded into your sheet, it will show the value that’s in the column named in the second argument, which is also called **Item.**

![](<Base64-Image-Removed>)

That’s all you need to do.  Now just close the Power Query Editor and see the data loaded into your sheet.  It will appear as a data type in the cell, and you can write a formula that will refer to the data type cell and a field name from that data type, such as:

**\=A2.Suggested Price**

You can also click on the data type icon in the cell to open the card and see all the fields.  Then you can click on the button next to any field to add that field to the next column.

![](<Base64-Image-Removed>)

**TIP**

Power Query is case-sensitive, so make sure you type the step name and column names exactly as they appear, otherwise you’ll get an error.

We hope you find this week’s topic helpful.  Check back for more details about Excel for Mac and how it’s different to Excel for Windows.

*   [Log in](https://sumproduct.com/blog/excel-for-mac-power-query-creating-data-types/#0)
    
*   [Register](https://sumproduct.com/blog/excel-for-mac-power-query-creating-data-types/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/excel-for-mac-power-query-creating-data-types/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/excel-for-mac-power-query-creating-data-types/#0)

[](https://sumproduct.com/blog/excel-for-mac-power-query-creating-data-types/#0 "close")

top