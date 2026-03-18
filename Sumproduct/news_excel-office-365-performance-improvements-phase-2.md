# Excel Office 365 Performance Improvements – Phase 2

**Source:** https://sumproduct.com/news/excel-office-365-performance-improvements-phase-2/

---

[Home](https://sumproduct.com/)

\> Excel Office 365 Performance Improvements – Phase 2

*   September 27, 2018

Excel Office 365 Performance Improvements – Phase 2
===================================================

Excel Office 365 Performance Improvements – Phase 2
===================================================

27 September 2018

![](<Base64-Image-Removed>)

Just under a year on from last year’s [improvement frenzy](https://www.sumproduct.com/news/article/excel-office-365-performance-improvements)
, the Microsoft team have been going gangbusters at “Phase 2”. Microsoft states they continue this project “… to reinforce our commitment to fixing top impacting freezing, slow and not responding performance issues derived from Excel user feedback and usage learnings”. This is what they have been up to…

*   **Lookup functions: VLOOKUP**, **HLOOKUP**, and **MATCH** are three of the most used functions in Excel. If you previously used these to locate exact matches to find items in a table or range in Excel, and see it noticeably take time in seconds or minutes or more, chances are you’ll now see very noticeable improvement in the speed at which you see results.
    
    Microsoft has made them faster by more efficiently finding the item you are looking up. Essentially, they have created an index on-demand when you first search of a range of cells and then reuse it in subsequent lookups from the same range, until data changes in the lookup range.
    

*   **Copying the entire column in a sheet** and selecting the clipboard is faster now because Microsoft optimised the large memory allocations with a more efficient data structure
*   **Undoing pasted cells with conditional formatting** was slow because a paste operation was inefficient in generating an undo record for every cell with conditional formatting and with its own changed priority. It now combines them more efficiently into one undo record with changed priorities for all in it
*   **Undoing inserting a new row** with a copied range with merged cells is now faster because Microsoft has optimised handling of merged cells during an undo operation
*   **Deleting one or more rows with merged cells** is now more efficient because it will skip redundant calls to render the visible grid in the midst of the deletion operation
*   **Viewing filter drop down** for a column with lots of cells with conditional formatting is now faster because the filter drop down algorithm has been made more efficient computing highlight, unique and duplicate values
*   **Scrolling in the visible sheet** after an operation wasn’t optimal, because Excel re-rendered (or at least evaluated) all rows top to bottom (including filtered rows) in the visible sheet. This can be expensive depending on the number of rows and Excel’s ability to calculate for animation related rendering. The optimisation was introduced in the first wave of performance improvements and has been enhanced here
*   **Scrolling, editing of cells, cell selection and filtering operations** in the grid are much faster when lots of rows are filtered / hidden because rendering is better optimised to intelligently defer expensive rendering calls until Excel has calculated the last row in the visible range
*   **Slow transitioning to the next cell after editing** a cell adjacent to a large table or range of cells with data, because after editing a cell adjacent to a large table or range of cells with data, Excel would generate a preview of all cells in that column to Flash Fill, which is on by default. Depending on the size of the adjacent table or range of cells and whether the cells contain additional metadata like conditional formatting, this can be a time consuming and expensive operation. Microsoft now limits the scope of Flash Fill preview to the visible area improving Excel’s responsiveness
*   When **opening any workbook** Excel used to search all existing Ribbon content to ensure every component of the Ribbon rendered correctly. This will now open faster by more intelligently searching in common cases like when the Ribbon item being searched for doesn’t exist. Also, during open Excel now skips updating MRU links synchronously and instead update them asynchronously after opening. Finally, the software scopes the rendering of the grid to the visible grid area when opening workbooks with lots of wrapped text in locales like Japanese
*   **Opening a local workbook when using a third party anti-virus software is faster** because Excel is now more intelligent in avoiding searching for the third party anti-virus vendor registered for scanning when a scan is determined to be redundant
*   Excel now will **open simple CSV text files much faster** by employing a more efficient memory allocation
*   **Flashing scrollbars and slower running VBA code****(than Excel 2010) even when ScreenUpdating property is set to false:** Microsoft has stated they have addressed this by ensuring scrollbars will no longer update when the **ScreenUpdating** property is set to false (just like in Excel 2010). T his in turn diverts CPU cycles away from redundant rendering of the scrollbars and to running user VBA code, improving code execution speed
*   Programmatically **selecting a cell, a range of cells, or a sheet using VBA** is now faster because Excel avoids redundant calls for updating a document’s upload status when running VBA macro code performing operations like selecting a cell, a range of cells or a sheet
*   **Executing the FREQUENCY function for large data sets is faster** because Microsoft has optimised the underlying sorting algorithm for the **FREQUENCY** function for large data sets.

These updates should be noticed by anyone receiving the Office 365 Monthly Channel updates (or better) starting with version 1809 (a fine vintage!).

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/news/excel-office-365-performance-improvements-phase-2/#0)
    
*   [Register](https://sumproduct.com/news/excel-office-365-performance-improvements-phase-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/news/excel-office-365-performance-improvements-phase-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/news/excel-office-365-performance-improvements-phase-2/#0)

[](https://sumproduct.com/news/excel-office-365-performance-improvements-phase-2/#0 "close")

top