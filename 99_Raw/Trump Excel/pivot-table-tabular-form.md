# Change Pivot Table to Tabular Form

**Source:** https://trumpexcel.com/pivot-table-tabular-form

---

[Skip to content](https://trumpexcel.com/pivot-table-tabular-form/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/pivot-table-tabular-form/#below-title)

When working with Pivot Tables in Excel, I always ensure that my Pivot Tables are displayed in the tabular form.

I don’t know why, but Microsoft has decided that any default Pivot Table would be shown in the Compact form.

While powerful, the standard Compact Form in Pivot Tables can sometimes feel a bit… well, compact.

In this article, I will show you how to get your pivot tables in the tabular format. I’ll show you how to **convert an existing Pivot Table into the Tabular form**, as well as changing a setting so that every time you make a new Pivot Table, it **automatically uses the Tabular format**.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/pivot-table-tabular-form/#)

Compact vs. Tabular Layout: What’s the Difference?
--------------------------------------------------

Before I jump into the “how,” let me quickly show you the “why.”

Let me show you what is the issue with the Compact form Pivot Table and why it is a better idea to convert it into the Tabular form.

### Compact Form (Default but Not Ideal)

Below is an example of a Pivot Table in Compact form.

![Pivot table in compact form](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20589%201070'%3E%3C/svg%3E)

While it looks clean, organized, and all right at first glance, here are the issues with the compact form:

*   **All in One Column:** The “Row Labels” column jumps between regions (East, North) and product categories (Clothing, Electronics), making it hard to tell what’s what at a glance.
*   **Not database-friendly**: This format doesn’t follow proper database structure. For it to be database-friendly, one column should contain one specific type of information, e.g., one column should have only regions (East, North, South, West), another column should have only product categories (Clothing, Electronics, Furniture), and a third column should have the sales numbers.
*   **Hard to sort or filter**: If you want to sort by region or [filter by product type](https://trumpexcel.com/filter-data-pivot-table-excel/)
    , it’s nearly impossible because they’re all mixed together in one column.
*   **Generic Labels:** The column header for your row fields is simply labeled ‘Row Labels’.

While this layout saves horizontal space, it can be a pain to work with.

Enters… Tabular Form!

### Tabular Form (Ideal Format)

Below is an example of a Pivot Table in Tabular form.

![Pivot table in tabular form](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20819%201061'%3E%3C/svg%3E)

The Tabular Form presents your data in a more traditional and structured way.

*   **Separate Columns for Each Field:** Every field you place in the ‘Rows’ area gets its own dedicated column.
*   **Classic Table Look:** This layout resembles a standard, easy-to-read data table.
*   **Easier to Export and Analyze:** Because of its clean structure, it’s much simpler to copy, paste, and integrate with other applications.

Unless you have a very strong reason to use Compact form, the Tabular Form is the way to go.

Now let’s see how to convert your Pivot Tables to tabular form.

Change Pivot Table to Tabular Form (For Existing Pivot Tables)
--------------------------------------------------------------

The fastest way to switch your existing Pivot Table to Tabular Form is through the Excel Ribbon.

It only takes a few clicks!

Here’s the data from a Pivot Table currently in the default Compact Form:

![Pivot table in compact form](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20589%201070'%3E%3C/svg%3E)

Here are the steps to change this Pivot Table into Tabular form:

1.  Click anywhere inside your Pivot Table. This will make the “PivotTable Analyze” and “Design” tabs appear in the Ribbon.
2.  Go to the **Design** tab.

![Click on the 'Design' tab in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20914%20533'%3E%3C/svg%3E)

1.  In the “Layout” group, click on the **Report Layout** dropdown.
2.  Select **Show in Tabular Form**.

![Click on the 'Show in tabular form' option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201087%201128'%3E%3C/svg%3E)

That’s it! Your Pivot Table will instantly switch to the much cleaner Tabular Form.

_**A Quick Note:**_ You might notice that after switching, some cells in the outer fields are blank. To make it even easier to read, you can go back to the **Report Layout** drop-down and select **Repeat All Item Labels**. This will fill in the blank cells, making your table complete.

Set Tabular Form as the Default for New Pivot Tables
----------------------------------------------------

If you find yourself constantly switching to Tabular Form every time you [create a Pivot Table](https://trumpexcel.com/creating-excel-pivot-table/)
, you can save yourself some hassle by making it your default layout.

Here’s how to set it and forget it:

1.  Click on **File** and then choose **Options**.
2.  In the Excel Options dialog box, select the **Data** category from the left-hand pane.

![Click on the data option in the Excel options dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201785%20962'%3E%3C/svg%3E)

3.  Click on the **Edit Default Layout…** button.

![Click on the Edit Layout button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201785%20962'%3E%3C/svg%3E)

4.  In the “Edit Default Layout” dialog box, click the **Report Layout** dropdown.
5.  Choose **Show in Tabular Form**.

![Click on the Show in Tabular form option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201262%20983'%3E%3C/svg%3E)

6.  Click **OK** to close the current dialog box, and then **OK** again to close the Excel Options.

Now, any new Pivot Table you create will automatically start in the Tabular Form.

**Pro Tip**: While you are in the _Edit Default Layout_ dialog box, also consider checking the ‘_Repeat all item labels_‘ option. This way, any pivot table in tabular form would automatically have all the blank cells filled with the item label in that column.

_**Caveat:**_ This setting only affects new Pivot Tables created on your computer. It won’t change the layout of any existing Pivot Tables.

VBA to Change All Existing Pivot Tables to Tabular Form
-------------------------------------------------------

What if you have a workbook filled with dozens of Pivot Tables in the old Compact Form?

Changing them one by one would be a nightmare.

This is where a little bit of VBA magic can come in handy.

You can use the a simple VBA macro code (given below) to convert every Pivot Table in your workbook to Tabular Form all at once.

Here’s the VBA code:

    Sub ConvertAllPivotTablesToTabular()
    'Code developed by Sumit Bansal from https://trumpexcel.com
    Dim ws As Worksheet
    Dim pt As PivotTable
    Dim counter As Long
    counter = 0
    
    For Each ws In ThisWorkbook.Worksheets
        For Each pt In ws.PivotTables
            pt.RowAxisLayout xlTabularRow
            counter = counter + 1
        Next pt
    Next ws
    
    If counter > 0 Then
        MsgBox counter & " Pivot Table(s) have been successfully switched to Tabular Form.", vbInformation
    Else
        MsgBox "No Pivot Tables were found in this workbook.", vbExclamation
    End If
    
    End Sub

**How to Use the VBA Code:**

1.  Open the Visual Basic for Applications (VBA) editor by pressing **Alt + F11**.
2.  In the VBA editor, click on **Insert** in the menu bar and then select **Module**.

![Click on the Insert button and then click on Module](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20785%20726'%3E%3C/svg%3E)

3.  Copy and paste the code above into the new module window.

![Copy-paste the VBA code into the module](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202560%20912'%3E%3C/svg%3E)

4.  Place the cursor anywhere in the code and then press the F8 key or click on the Run icon in the toolbar.

![Run the VBA code](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201094%20564'%3E%3C/svg%3E)

5.  Close the VB editor.

This script will loop through every worksheet and every Pivot Table, applying the Tabular Form layout to each one.

Once the file has converted all the pivot tables into tabular form, it will also show you a message box stating how many pivot tables have been changed.

![Message box about pivot tables converted to tabular form](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201295%20503'%3E%3C/svg%3E)

_**CAUTION:**_ Actions done by a VBA macro cannot be undone using Ctrl + Z. It’s always a good practice to save a backup of your workbook before running any code.

Hopefully, Microsoft will soon realize that Tabular form is the better option and make it the default option. Till then, you can use the methods shown in this article to get to the Tabular form.

I hope you found this tutorial helpful!

**Other Excel articles you may also like:**

*   [How to Delete a Pivot Table in Excel](https://trumpexcel.com/delete-pivot-table/)
    
*   [Preparing Source Data For Pivot Table](https://trumpexcel.com/source-data-for-pivot-table/)
    
*   [How to Group Numbers in Pivot Table in Excel](https://trumpexcel.com/group-numbers-in-pivot-table/)
    
*   [Using Slicers in Excel Pivot Table](https://trumpexcel.com/slicers-excel-pivot-table/)
      
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/pivot-table-tabular-form/#respond)

Comment

Name Email Website

  

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free Excel Tips EBook Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK