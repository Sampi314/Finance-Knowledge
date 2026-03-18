# Take it to the Limit

**Source:** https://sumproduct.com/thought/take-it-to-the-limit/

---

[Home](https://sumproduct.com/)

\> Take it to the Limit

*   May 14, 2025

Take it to the Limit
====================

And I can't tell you why.

Take it to the Limit
====================

_We address Excel’s limits. Sometimes a little difficult, you might need the vision of an eagle to take it to the limit… By Liam Bastick, director (and Excel MVP) with SumProduct Pty Ltd._

### Query

I have heard you say that you can do anything in Excel – eventually – all that limits you is imagination. Is that strictly true?

### Advice

Erm, not quite. There are hard and fast limits defined by the software and these limits are reproduced below. It should be noted that where limitations are attributable to available memory, this depends not just on your computer’s memory but whether you are running 32-bit or 64-bit Excel, as 32-bit Excel is typically restricted to _c._2GB of available memory depending upon your computer’s specifications, applications open and the version of Excel you are running.

The specifications and limitations can be classified into five sections:

1.  Calculations
2.  Charting
3.  PivotTables and PivotCharts
4.  Sharing workbooks
5.  Workbooks and worksheets

I now summarise the main specifications and limitations of each.

| Feature Maximum Limit |
| --- |
| Area dependency Limited by available memory |
| Area dependency per worksheet Limited by available memory |
| Arguments in a function 255, unless restricted by syntax otherwise |
| Cross-worksheet array formula dependency Limited by available memory |
| Cross-worksheet dependency 64,000 worksheets that can refer to other sheets |
| Dependency on a single cell 4 billion formulae that can depend on a single cell |
| Earliest date allowed for calculation January 1, 1900 (January 1, 1904, if 1904 date system) |
| Internal length of formula 16,384 bytes |
| Iterations 32,767 |
| Largest allowed negative number -1.00 x 10308 |
| Largest allowed negative number via formula -1.7976931348623158 x 10308 |
| Largest allowed positive number 1.00 x 10308 |
| Largest allowed positive number via formula 1.7976931348623158 x 10308 |
| Largest amount of time that can be entered 9999:59:59 |
| Latest date allowed for calculation December 31, 9999 |
| Length of formula contents 8,192 characters |
| Linked cell content length from closed workbooks 32,767 |
| Nested levels of functions 64 (Excel 2007 onwards); 7 previously |
| Number of available worksheet functions 341, although this really depends upon your definition of “available functions” |
| Number precision 15 digits |
| Selected ranges 2,048 |
| Size of the operand stack 1,024 |
| Smallest allowed negative number -2.23 x 10\-308 |
| Smallest allowed positive number 2.23 x 10\-308 |
| User defined function categories 255 |
| Worksheet arrays Limited by available memory |

| Feature Maximum Limit |
| --- |
| Charts linked to a worksheet Limited by available memory |
| Data point for all data series in one chart Limited by available memory |
| Data points in a data series for 2-D charts Limited by available memory |
| Data points in a data series for 3-D charts Limited by available memory |
| Data series in one chart 255 |
| Worksheets referred to by a chart 255 |
| Charts linked to a worksheet Limited by available memory |

| Feature | Maximum Limit |
| --- | --- |
| Calculated item formulas in a PivotChart report | Limited by available memory |
| Calculated item formulas in a PivotTable report | Limited by available memory |
| Items displayed in filter drop-down lists | 10,000 (Excel 2007 and later); 1,000 previously |
| Length for a relational PivotTable string | 32,767 |
| Length of the MDX name for a PivotTable item | 32,767 |
| PivotTable reports on a sheet | Limited by available memory |
| Report filters in a PivotChart report | 256 (although this may be limited by available memory) |
| Report filters in a PivotTable report | 256 (although this may be limited by available memory) |
| Row or column fields in a PivotTable report | Limited by available memory |
| Unique items per field | 1,048,576 |
| Value fields in a PivotChart report | 256 |
| Value fields in a PivotTable report | 256 |
| Calculated item formulas in a PivotChart report | Limited by available memory |

| Feature | Maximum Limit |
| --- | --- |
| Cells that can be highlighted in a shared workbook | 32,767 |
| Colours used to identify changes made by different users when change highlighting is turned on | 32 (each user is identified by a separate colour; changes made by the current user are highlighted with navy blue) |
| Days that change history is maintained | 32,767 (default is 30 days) |
| Excel Tables in a shared workbook | 0 (zero). Note: a workbook that contains one or more Excel Tables cannot be shared. |
| Personal views in a shared workbook | Limited by available memory |
| Users who can open and share a shared workbook at the same time | 256 |
| Workbooks that can be merged at one time | Limited by available memory |

| Feature | Maximum Limit |
| --- | --- |
| Adjustable cells in Solver | 200 |
| Changing cells allowed in Scenario Manager | 32  |
| Characters in a header or footer | 255 |
| Colours in a workbook | 16 million colours (32 bit with full access to 24 bit colour spectrum) |
| Column width | 255 characters |
| Conditional formats | Limited by available memory |
| Custom functions | Limited by available memory |
| Custom number formats in a cell | 4 (positive, negative, zero and text) or 3 (two conditions and a remainder) |
| Fields in a data form | 32  |
| Fill styles | 256 |
| Hyperlinks in a worksheet | 66,530 hyperlinks |
| Items displayed in filter drop-down lists | 10,000 from Excel 2007 onwards; 1,000 previously |
| Line styles | 256 |
| Line weight | 256 |
| Linked sheets | Limited by available memory |
| Named views in a workbook | Limited by available memory |
| Names in a workbook | Limited by available memory |
| Non-contiguous cells that can be selected | 2,147,483,648 cells, although if you selected one cell a second at that rate, it would still take you slightly over 68 years without eating, drinking or sleeping! However, note that you may only select a maximum of 2,048 separate ranges |
| Number formats in a workbook | Between 200 and 250, depending upon the language version of Excel installed |
| Open workbooks | Limited by available memory and system resources |
| Page breaks | 1,026 horizontal and vertical |
| Panes in a window | 4   |
| Reports | Limited by available memory |
| Row height | 409 points |
| Scenarios in Scenario Manager | Limited by available memory; a summary report shows only the first 251 scenarios |
| Sheets in a workbook | Limited by available memory (default is 3 sheets in Excel 2007 onwards; 16 previously) |
| Sort references | 64 in a single sort; unlimited when using sequential sorts |
| Total number of characters that a cell can contain | 32,767 characters |
| Undo levels | 100 |
| Unique cell formats/cell styles | 64,000 |
| Unique font types | 1,024 global fonts available for use; 512 per workbook |
| Windows in a workbook | Limited by available memory |
| Workbook parameters | 255 parameters per workbook |
| Worksheet size | 1,048,576 rows by 16,384 columns |
| Zoom range | 10% to 400% |

### Word to the Wise

It should be noted that the closer you push Excel to the edge of its capabilities, the more likely a workbook will fail, _i.e._ it will corrupt and / or crash. These limits put pressure on available memory more so than file size ever could. The limits are provided for information only and Excel works much better if you stay far, far away from these thresholds. You have been warned!

If you have any questions regarding the limits of Excel please feel free to drop Liam a line at [liam.bastick@sumproduct.com](mailto:liam.bastick@sumproduct.com)

[More Thoughts](https://www.sumproduct.com/thought)

*   [Log in](https://sumproduct.com/thought/take-it-to-the-limit/#0)
    
*   [Register](https://sumproduct.com/thought/take-it-to-the-limit/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/take-it-to-the-limit/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/take-it-to-the-limit/#0)

[](https://sumproduct.com/thought/take-it-to-the-limit/#0 "close")

top