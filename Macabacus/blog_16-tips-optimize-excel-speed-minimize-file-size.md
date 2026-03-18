# 16 Quick Tips to Optimize Excel Speed & Reduce File Size

**Source:** https://macabacus.com/blog/16-tips-optimize-excel-speed-minimize-file-size

---

16 Quick Tips to Optimize Excel Speed & Reduce File Size
========================================================

![quick tip to optimize excel speed](https://macabacus.com/assets/2023/10/16-quick-tip-to-optimize-excel-speed.png)

“Why is my Excel so slow?!”

Excel spreadsheets seem to have a knack for slowing to a crawl. As your workbook grows in complexity with mounds of data, formulas, and analytics, you may suddenly find yourself tapping your foot, waiting for calculations.

Don’t abandon ship for Google Sheets just yet. With some targeted tuning and optimization, you can whip that sluggish Excel file back into shape.

Build Financial Models in Minutes
---------------------------------

**Enterprise-Grade Financial Modeling** used by 80,000+ professionals across Investment Banking, Private Equity, and Corporate Finance. Ensure consistency, accuracy, and efficiency across your entire organization.

[Get Started](https://macabacus.com/start-trial)
[Book a Demo](https://macabacus.com/demo-request)

Follow these 16 pro tips to speed up Excel and minimize file size for seamless performance.

### **1\. Simplify Formulas**

Formulas are one of the biggest Excel slowdowns, especially highly complex ones with nested functions or thousands of cell references. Simplifying formulas where possible goes a long way.

*   Use helper columns for interim calculations instead of mammoth formulas. Breaking a complex formula into discrete steps in new columns dramatically cuts down complexity.
*   Limit nested functions. Nesting multiple functions loads the calculation engine. Try restructuring formulas to avoid excessive nesting.
*   Reference cells directly instead of full column ranges when you can. Referencing entire columns in formulas causes full-column scanning bogging down Excel.
*   Switch from array formulas to standard formulas when viable. Array formulas chew up calculation cycles.

### **2\. Take Advantage of Excel Tables**

Excel tables come packed with structural advantages compared to free-form data, speeding up file performance.

*   Automatic expanding formatted ranges relieve manual upkeep as data grows. No more dragging cell formats and formulas down new rows.
*   Structured auto-filled columns with headers cuts down on lengthy references. Just refer to the header like Sales\[\[#This Row\],\[Price\]\].
*   Formulas entered in tables apply to new rows automatically without copying down. No manual formula drag down required.
*   Dynamic named ranges automatically capture data in the table. No need to manually define separate named ranges.

### **3\. Scrub Unused Defined Names**

Over time­, Excel workbooks can accumulate a large numbe­r of defined names. This can le­ad to bloated file sizes and de­creased performance­. It often becomes challe­nging to identify and delete­ these unnecessary names using Excel’s Name Manage­r. 

However, [**Macabacus’ Name Scrubbe­r**](https://help.macabacus.com/article/797-file-operations#name-scrubber)
 utility provides a solution. With this tool, you can easily view and de­lete hidden name­s, as well as those with #REF! errors or one­s that are unused but refe­r to constants or arrays. By scrubbing away tens of thousands of unnecessary name­s in just seconds, it streamlines your workbooks, improving the­ir efficiency.

### **4\. Minimize Volatile Functions**

Volatile functions recalculate with every change and can grind Excel to a halt if overused. Limit their presence when you can.

*   Common volatile functions include NOW, TODAY, RAND, OFFSET, INDIRECT.
*   Switch rand() to randbetween(), which is not volatile, refreshing only when arguments change.
*   Replace indirect() with [index/match](https://macabacus.com/blog/how-to-use-index-match-data-retrieval)
    () or vlookup() to avoid full recalcs.
*   Minimize whole column references and entire row ranges, which force volatile functions to scan all cells.
*   Move volatile formulas out of heavily edited areas to avoid excessive triggering.

### **5\. Increase Iteration Settings**

Lower iteration settings restrict complex formula recursions, which is important for minimizing file size. But this comes at an Excel speed cost, so increase iterations to improve performance.

*   In the Excel options menu, find Formulas > Calculation options > Iteration.
*   Raise the maximum iterations from 100 to 200 or 500. Be careful, as high numbers can allow infinite loops.
*   The higher the iteration setting, the more recursions allowed for complex formulas to resolve without errors.

### **6\. Delete Unused Styles**

Built-up cell styles contribute to file bloat. Prune back anything not in use.

*   Head to the Home tab and right-click on a style in the Styles pane.
*   Select delete to remove individual styles no longer needed.
*   On the styles manager menu, sort by usage, then delete styles with zero uses.
*   Reset to clear all custom cell styles and restore the default minimal set.

### **7\. Scrub Styles**

Macabacus’ [**Style Scrubbe­r**](https://help.macabacus.com/article/797-file-operations#style-scrubber)
 offers a convenient solution to re­move numerous unused Exce­l styles effortlessly, the­reby enhancing file size­ reduction and overall stability. Manually dele­ting individual styles in Excel can be impractical, conside­ring the limited capability to dele­te them in bulk. Howeve­r, with Style Scrubber, users can e­asily strip away unnecessary styles with just a fe­w clicks.

### **8\. Avoid Blank Rows and Columns**

Blank rows and columns jammed amid data slow Excel’s calculation sequence. Delete them.

*   Scan for areas with large blank blocks within your data sets and delete them.
*   Sort used and unused rows and columns together with the Go To Special menu.
*   Cut out unneeded whitespace between sets of data.
*   Set your scroll area to avoid far-off blank rows and columns.

### **9\. Limit Charts and Graphics**

Too many charts, especially with complex formatting, can overburden Excel’s graphic engine.

*   Avoid flashy 3D, shadow, and other special effects. Stick to simple, clean charts.
*   Place charts on separate sheets rather than embedded amid data.
*   Consider Excel dashboards on separate files with links to reduced data instead of heavy charts.
*   Delete unused charts instead of just hiding them.

### **10\. Compress Media and Images**

High-resolution images and fancy graphics come at a file size cost. Compress image filesizes for smaller footprints.

*   Use the built-in compress pictures utility in the picture format settings.
*   Convert images like JPGs to lower-resolution versions.
*   Use lossless image compression software for PNGs, such as ImageOptim.
*   Reduce the quality of images with lossy compression through online tools.
*   Swap detailed gradients, shadows, and effects for solid fills and lines.

### **11\. Unlink Unused Worksheets**

Extra worksheets linked to data impact memory usage, especially with objects like formulas, charts, or PivotTables, even if hidden. Unlink all sheets not in use.

*   Review the visibility of each worksheet and consider if they all need to be linked.
*   Right-click on sheet tabs and select Unlink to exclude sheets not being used.
*   Click on cells linking to another sheet, then hit delete to remove formulas pulling in data.
*   Hide or delete inactive worksheets you want to keep for reference to unlink them.

One way to consolidate workbooks is to use [**Macabacus’ Merge Workbooks tool**](https://help.macabacus.com/article/797-file-operations#merge)
. This tool lets you combine sheets from multiple workbooks into a single workbook and optionally rename the sheets in the merged workbook according to your preferences.

### **12\. Consolidate Workbooks**

Connecting extra workbooks and files extends calculation time. Consolidate data sets together into one spreadsheet.

*   Use the Move or Copy menu to pull sheets from other workbooks into one file.
*   Link values between files instead of entire worksheets when possible.
*   Ensure linked workbooks are closed when not needed to free memory.

### **13\. Turn Off AutoSave**

Real-time AutoSave and Versions hog system resources with constant file access and backups. Disable while working for better performance.

*   Head to File > Options > Save and uncheck the Save AutoRecover box.
*   Be sure to manually save regularly to avoid data loss with AutoSave off.
*   Schedule or force Versions purge regularly to avoid version buildup.

### **14\. Quick Save without Recalculation**

[**Macabacus Quick Save tools**](https://help.macabacus.com/article/797-file-operations#quick-save)
 can significantly re­duce the time re­quired to save Excel file­s. The Quick Save command allows you to **save workbooks without re­calculating**, regardless of your calculation settings. 

This is particularly be­neficial when working with large datase­ts or complex formulas, as it eliminates the­ slow recalculation process that occurs during saving. Quick Save is e­specially effective­ for large models that typically take se­veral minutes to save using Exce­l’s standard save function.

### **15\. Disable Page Break Preview**

Page Break Preview rapidly renders content during scrolling, causing lag. Turn it off for faster worksheet navigation.

*   Uncheck the Page Break Preview button under the View tab.
*   Print Preview has the same effect. Use Print Preview only when needed.

### **16\. Fine-Tune File Saving**

Frequent saving forces Excel to repeatedly write and re-read from your hard drive, slowing things down over time. Optimize re-calculation time to improve Excel speed:

*   Set calculation mode to “**Manual**” to prevent full recalculations when saving.
*   Increase autosave intervals from the default 3 minutes to 10-15 minutes.
*   Avoid Shared Workbook mode which can slow saves and trigger excess calculations.

**The Takeaway**
----------------

With its massive grid and calculation power, Excel maintains impressive performance for most. But large, complex models and workbooks can bring even the latest hardware to its knees.

Luckily, targeted optimizations like simplifying formulas, deleting unused elements, compressing media, and consolidating data go a long way. Pair these tactics with performance-enhancing add-ins to keep your Excel files nimble regardless of size.

With Macabacus, you have a range­ of file cleanup and optimization tools at your fingertips. The­se tools offer precise­ control in reducing file size, e­nhancing performance, and ensuring se­amless operation of your Excel workbooks in the­ long run.

Build Financial Models in Minutes
---------------------------------

**Enterprise-Grade Financial Modeling** used by 80,000+ professionals across Investment Banking, Private Equity, and Corporate Finance. Ensure consistency, accuracy, and efficiency across your entire organization.

[Get Started](https://macabacus.com/start-trial)
[Book a Demo](https://macabacus.com/demo-request)

Discover more topics
--------------------

[Webinar: The AI Edge in Investment Banking](https://macabacus.com/lp/webinar-ai-edge-investment-banking)

Join experts from Macabacus & LSEG to learn practical insights about AI’s influence on the future of banking.

[Read more](https://macabacus.com/lp/webinar-ai-edge-investment-banking)

[DCF Excel Template](https://macabacus.com/excel/templates/discounted-cash-flow)

Elevate your investment analysis with our free DCF model template. Understand discounted cash flow principles and perform accurate valuations in Excel.

[Read more](https://macabacus.com/excel/templates/discounted-cash-flow)

[Operating Model Excel Template](https://macabacus.com/excel/templates/operating-model)

Download our free operating model Excel template. Forecast revenue, expenses, and key financial metrics for better decision-making.

[Read more](https://macabacus.com/excel/templates/operating-model)

[LBO Excel Model](https://macabacus.com/excel/templates/lbo-model-short)

Try LBO modeling with our comprehensive Excel template. Understand key concepts, calculate returns, and gain actionable insights.

[Read more](https://macabacus.com/excel/templates/lbo-model-short)