# Filter Tips with No Health Warning

**Source:** https://sumproduct.com/thought/filter-tips-with-no-health-warning/

---

[Home](https://sumproduct.com/)

\> Filter Tips with No Health Warning

*   May 14, 2025

Filter Tips with No Health Warning
==================================

Considering the pros and cons of both the AutoFilter and the Advanced Filter.

Filter Tips with No Health Warning
==================================

Every Excel user seems reasonably familiar with AutoFilter, but what about its lesser known sibling? This article considers the pros and cons of both the AutoFilter and Advanced Filter. By Liam Bastick, Director with SumProduct Pty Ltd.

Query
-----

I keep using AutoFilter for data analysis but I can’t help noticing there’s an Advanced Filter too. What does it do? Am I using AutoFilter correctly?

Advice
------

We often filter data using Excel. For many, the AutoFilter seems to provide sufficient options, or else they will interrogate the data using PivotTables (see [\>Pivotal PivotTables](https://www.sumproduct.com/thought/pivotal-pivottables)
 for further information).

Sometimes, more complex analysis is required. One way this may be conducted is with Advanced Filters, but before I talk about this functionality, let me recap the AutoFilter.

### AutoFilter

In Excel 2007 and later versions, filtering may be performed by creating a Table first (see [Tables](https://www.sumproduct.com/thought/tables)
 for more details).

If your data is not in an Excel Table, or you are using Excel 2003 and earlier versions, then you should construct your database first as follows:

*   **Headings**: In the row immediately above the data, enter a heading for each column;
*   **No blank rows or columns**: You can leave blank cells in a row or column but make sure that there are no completely blank rows or columns within the database;
*   **Separate the data from the rest of your spreadsheet**: Keep the database on a worksheet away from other data. Imagine the database is an island with a “moat” of blank cells entirely surrounding the dataset.

![](https://sumproduct.com/wp-content/uploads/2025/05/image-01-database-layout1.gif)

Example Database Layout

To activate the AutoFilter, the top row (the headings) should be selected, and then:

### Excel 2003 and earlier

*   From the drop down menus, go to Data -> Filter -> AutoFilter (ALT + D + F + F)

![](https://sumproduct.com/wp-content/uploads/2025/05/image-02-excel-2003-autofilter-alt-d-f-f-300x266-1.gif)

### Excel 2007 and later

*   On the Data tab of the Ribbon, go to the Sort & Filter group and click the AutoFilter icon (ALT + A + T)
*   ALT + D + F + F still works

![](https://sumproduct.com/wp-content/uploads/2025/05/image-03-excel-2007-autofilter-alt-a-t.gif)

The database may now be filtered to select data that meets certain condition by clicking on the drop down arrows to the right of each heading, viz.

![](<Base64-Image-Removed>)

Data Filtering

This could be summarised in a PivotTable too, and the [attached Excel workbook](https://sumproduct.com/assets/user-upload/sp-advanced-filters.xls)
 provides an illustration of this.

The arrows will change appearance when a filter has been applied to that column. The filter can be removed by clicking on the filter button once more, or you can clear all filters in one bound (in any version of Excel) using the keyboard shortcut ALT + D + F + S (which is “Show All” in Excel 2003 / earlier and “Clear” in Excel 2007 / later).

This Excel feature does have limitations however. Filtering based on more complex criteria may not be possible and data may be filtered based only on visible cells:

![](<Base64-Image-Removed>)

Filter Visible Data Only

Moreover, there is an upper limit on the number of categories that may be filtered. For Excel 2003 and earlier versions, this limit is 1,000, but this has been increased ten-fold to 10,000 for Excel 2007 (although Excel 2010 only appears to show 9,998) and later versions:

### Excel 2003 and earlier

![](<Base64-Image-Removed>)

### Excel 2007 and later

![](<Base64-Image-Removed>)

For many, the capabilities of AutoFilter far exceed its limitations, and sufficient analysis can be performed with this feature. Sometimes, however, the following tool may prove more bountiful:

### Advanced Filter

Using the same database set-up, it is possible to undertake more complicated analysis using he Advanced Filter. First, select the database and then:

### Excel 2003 and earlier

*   From the drop down menus, go to Data -> Filter -> Advanced Filter (ALT + D + F + A)

![](<Base64-Image-Removed>)

### Excel 2007 and later

*   On the Data tab of the Ribbon, go to the Sort & Filter group and click the Advanced Filter icon (ALT + A + Q)
*   ALT + D + F + A still works

![](<Base64-Image-Removed>)

This activates the following dialog box:

![](<Base64-Image-Removed>)

Advanced Filter Dialog Box

It is very simple to use (it is the criteria which takes practice!). The List Range is simply the database to be reported upon including the top row headings. It does not have to include all columns but should include all rows.

Data may be filtered either in place or else the database may be copied to another location for ease of use (if the ‘Copy to another location’ option is selected to facilitate this, the ‘Copy to:’ range becomes active).

The ‘Unique records only’ checkbox is very useful as it will automatically eliminate any duplicates from the analysis. However, a duplicate occurs only when the complete record (i.e. the values in all columns specified in the ‘List range’) appears elsewhere in the database.

This just leaves the ‘Criteria range:’, which as I alluded to above, is where the magic happens. A criteria range consists of a minimum of two rows as follows:

![](<Base64-Image-Removed>)

Example Criteria Table

The first row is always the headings row. It does not always have to be populated, but if the table is to include criteria based on a certain field (column of data), the heading must match the heading in the source data table precisely.

The second and subsequent rows contain the criteria to be evaluated. These cells may be blank, contain formulae, values or text. Criteria on the same row must all be true to be filtered, whereas criteria on different rows are alternative criteria that may be met for filtering purposes.

In this illustration above, for a record to pass filtering it must either meet Criteria 1, 2 and 3 simultaneously or else Criteria 4, 5 and 6 concurrently.

Real-life examples might include the following:

### March Sales for the North Division

![](<Base64-Image-Removed>)

### Camera Sales for Feb and Apr 2012

![](<Base64-Image-Removed>)

With a little imagination, reports can be constructed identifying duplicate data, top ten sales and even incomplete records (see the [attached Excel file](https://sumproduct.com/assets/user-upload/sp-advanced-filters1.xls)
 for illustrations).

### Word to the Wise…

Both of these types of filtering have limitations. One key restriction is that if the source database were to change, just like PivotTables, the filter reports would need to be re-run. Unlike PivotTables, however, there is no ‘Refresh All’ option.

If source data is likely to change, it may be better to consider alternative solutions to working with multiple criteria (please see [Multiple Criteria](https://www.sumproduct.com/thought/multiple-criteria)
 for more information).

[More Thoughts](https://www.sumproduct.com/thought)

*   [Log in](https://sumproduct.com/thought/filter-tips-with-no-health-warning/#0)
    
*   [Register](https://sumproduct.com/thought/filter-tips-with-no-health-warning/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/filter-tips-with-no-health-warning/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/filter-tips-with-no-health-warning/#0)

[](https://sumproduct.com/thought/filter-tips-with-no-health-warning/#0 "close")

top