# 8 Ways to Reduce Excel File Size (that actually work)

**Source:** https://trumpexcel.com/reduce-excel-file-size

---

[Skip to content](https://trumpexcel.com/reduce-excel-file-size/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/reduce-excel-file-size/#below-title)

Excel workbooks have been known to become painfully slow and heavy as more data/formulas/images are added to it.

Sometimes, it’s easy to get rid of the extra flab and keep the excel file size in check, and sometimes, it isn’t.

And since Excel is not a web-based tool, most of us work and collaborate by sending Excel files via email. And a large Excel file that weighs 50 MB can be hard to share with your colleagues/clients.

In my last job, we used Lotus Notes email client, which is snail-slow, and sending heavy Excel files over that was torture.

While there is no magical way to reduce the size of an Excel workbook, there are a few techniques that you can use to cut down some flab.

Note: The impact of these techniques to reduce Excel file size would depend on your data. For some, it may help reduce the size by 50% and for some, it may only end up reducing the size by 5%.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/reduce-excel-file-size/#)

Tips to Reduce Excel File Size
------------------------------

Below are the techniques you can use to reduce the file size of your Excel workbook.

For each tip, I have done some testing and have added the snapshots to show you the impact on file size. The results you get would vary depending upon your data and files.

Based on your workbook, you can use one or more of these tips.

### Remove Unnecessary Worksheets/Data

The best solutions are often the easiest ones.

And this technique is more of common sense and less of any Excel wizardry.

If you have an Excel workbook that has some worksheets that are not needed (and are not being used in any [formulas](https://trumpexcel.com/excel-functions/)
), see if you can get rid of those.

This has a direct correlation with the Excel file size. So as soon as you delete some of the worksheets and save the workbook, you will instantly see a reduced file size.

**Test Results:**

I created an Excel file with 10 worksheets where each worksheet has 2.6 million data points (26 columns with 100,000 data points in each column).

![Reduce Excel File Size - Test 1 original](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20745%20177'%3E%3C/svg%3E)The resulting size of this workbook is 143 MB (and it’s taking quite some time to save and open).

![Reduce Excel File Size - Test 1 result1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20745%20166'%3E%3C/svg%3E)

Now when I deleted five sheets, the size reduced by half (duh).

As you can see, data that you have your worksheet has a direct correlation with the file size.

### Convert to Binary Format (XLSB)

Do you know that just by saving an Excel file in the XLSB format can reduce the file size?

Yes, it’s true.

All you have to do is while saving a workbook, use the .xlsb format.

Here are the steps to do this:

1.  Click the File tab.![Click on File Tab in Ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20237%20145'%3E%3C/svg%3E)
2.  Click on Save As.![Click on Save As in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20290%20326'%3E%3C/svg%3E)
3.  Click on Browse.![Click on Browse in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20304'%3E%3C/svg%3E)
4.  In the Save As dialog box, change the file type to Excel Binary Workbook (.xlsb)![Save as xlsb file](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20795%20516'%3E%3C/svg%3E)

**Test Results**

I had an Excel workbook that took 14.6 MB of space.

After converting the same file to the XLSB format, I was able to reduce the size to 10.4 MB (a size reduction of ~28%).

![Reduce Excel File Size - binary file xlsb](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20514%20122'%3E%3C/svg%3E)

#### What is XLSB?

When you save an Excel file (.xlsx or .xlsm), it gets saved in the [XML format](https://trumpexcel.com/convert-xml-to-excel/)
.

For example, if I change the file extension of the XLSX file to ZIP and then open it, this is what I get.

![Reduce Excel File Size - xlsx zip folder](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20522%20203'%3E%3C/svg%3E)

And if I further go in the ‘xl’ folder and then go in the worksheet folder, it shows me the worksheets in that workbook (and these worksheets are saved as an XML document).

![Reduce Excel File Size - xlsx zip folder worksheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20790%20129'%3E%3C/svg%3E)

Now let’s do the same with an XLSB file.

So I first change the file extension to ZIP, then open it and locate sheet1. Here is what you get:

![Reduce Excel File Size - xlsb zip folder worksheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20756%20172'%3E%3C/svg%3E)

You’ll notice that both XLSX and XLSB saves the worksheet in a different format.

XLSX/XLSM saves it as an XML file and XLSB saves it as a binary (.bin) file.

And without getting too technical, XML files are large in size as compared to a binary file.

So when you save your Excel workbook in the XLSB format, the file size is reduced. In our above example, the size reduction was ~30%.

#### XLSB Vs XLSX/XLSM

When it comes to using the XLSB format, size reduction is a huge benefit. But you need to be a bit cautious when working with the XLSB format.

**Advantages of XLSB format:**

1.  It reduces the Excel file size. This can be helpful when you have large files and you want to share it over email. You can quickly reduce the size by saving it in XLSB.
2.  XLSB files tend to open and save faster than XML file. Based on the limited tests I did, XLSB files were opening and saving 25%-50% faster. This difference is noticeable in large Excel files only. With smaller files, both XLSB and XLSX are fast.

While XLSB looks great, there are a few reasons you should stick to using XLSX/XLSM files:

1.  With XLSB format, you have no way of knowing whether it has a macro or not. This makes it riskier as someone can use it to execute malicious code.
2.  XLSB files are encoded in proprietary bin file format while XML is an open-source readable file format. This means that if you’re using third-party tools with Excel, it’s better to use XML format.
3.  Power Query cannot read data from an XLSB file. So if you use Power Query, it’s better to have your data in XLSX/XLSM formats.

As a general rule, if your file size is small (less than 5 MB), it’s better to stick to XLSX/XLSM formats.

Based on what I heard from people and read on many forums, a lot of people prefer to use XLSB as the file format when it comes to using Excel.

Here is a [good article](https://analystcave.com/excel-working-with-large-excel-files-the-xlsb-format/)
 on understanding the XLSB format.

### Remove Unnecessary Formulas

Too many formulas will bloat your workbook file size.

So if you have a data set that you need, but don’t need the formulas in it, it’s better to convert these formulas into values.

Here are the steps to quickly [convert formulas to values](https://trumpexcel.com/convert-formulas-to-values-excel/)
 in Excel:

1.  Select the entire worksheet/dataset.
2.  Press the **F5** key.
3.  In the Go To dialog box, click on ‘Special’.![Click the Special Button after pressing F5 - in Go To dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20419%20348'%3E%3C/svg%3E)
4.  In the Go To Special dialog box, select Formulas.![Click on Formulas in Go To special dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20378%20430'%3E%3C/svg%3E)
5.  Click OK.

The above steps would select all the cells that have a formula in it.

Now use the below steps to convert these formulas into values:

1.  Copy the selected cells (control + C)
2.  Click the Home tab.![Home Tab in Excel Ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20325%20151'%3E%3C/svg%3E)
3.  In the Clipboard group, click on Paste.![Click on Paste Icon in the Ribbon in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20195'%3E%3C/svg%3E)
4.  Click on Paste Value icon.![Click on Paste as Values Icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20178%20440'%3E%3C/svg%3E)

The above steps would convert all the cells with formulas into values.

**Test Results**

I created an Excel file with 2.7 million data points (1048576\*26) and then added three columns with formulas (SUM, COUNT and AVERAGE).

Then I converted these formulas into values and saved the file with a different name.

Below is the result:

![Reduce Excel File Size - with and without formulas](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20546%20107'%3E%3C/svg%3E)

The file with no formulas is ~8% less in size (and note that I only had 3 columns of formulas).

In case you have a lot of formulas, it can add to the size.

**NOTE**: [Volatile formulas](https://trumpexcel.com/excel-volatile-formulas/)
 can really bloat your file size. As a part of the test, when I replaced the SUM formula with a volatile formula (OFFSET), it lead to a jump in the file size (from 186 MB to 198 MB). So if you have volatile formulas that you can replace with non-volatile formulas, or can convert these into values, it will help you reduce the file size.

### Compress Images (Before and After Uploading)

If you work with Excel files that have images in it, you need to optimize these images and make sure the size is less.

The problem with images is that as you compress these, there is also a reduction in quality, which you may not want.

When working with images, the best way to keep the size of your Excel file low is by compressing the images before you insert it into Excel.

A good online tool to do this is [TinyPNG](https://tinypng.com/)
 (or you can use Photoshop or any other similar tool).

It’s a free tool that can reduce the size of an image by up to 90% and still maintains decent image quality.

Below is the screenshot where I was able to compress an image with the size of 3.9 MB to 331 KB with minimal loss in quality.

![File Size reduced by TinyPNG](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20795%20236'%3E%3C/svg%3E)

Once you have uploaded these compressed images to Excel, you can further compress it using the inbuilt option in Excel.

Here are the steps to compress an image in Excel:

1.  Select the image that you want to compress.
2.  Click on the Picture Tools Format tab. This is a contextual tab that only appears when you click on a picture.![Click on Picture Tools Format Tab in Excel ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20788%20166'%3E%3C/svg%3E)
3.  In the Adjust group, click on ‘Compress Picture’ option.![Click on Compress Pictures Option in the Excel ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20788%20166'%3E%3C/svg%3E)
4.  In the Compress Pictures dialog box:
    *   Deselect ‘Apply only to this picture’ if you want to compress all the images in the workbook.
    *   Select Email (96 ppi) for maximum compression.![Compress Pictures Dialog Box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20410%20351'%3E%3C/svg%3E)
5.  Click OK.
6.  Save the file.

This will compress all the images and help you reduce the file size of your Excel workbook.

**Test Results:**

I used the compress imge option in Excel using one image.

Below are the results:

![Reduce Excel File Size - image compression](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20530%20104'%3E%3C/svg%3E)

By using the compress image option, file size reduced from 445 KB to 43 KB (~90% reduction in file size).

This would depend on the image as well. An image that is already compressed may not lead to a huge size reduction.

### Remove Pivot Cache to Save Space

If you work with [Pivot tables](https://trumpexcel.com/pivot-table/)
 and struggle with large Excel files, knowing about [Pivot cache](https://trumpexcel.com/pivot-cache-excel/)
 can be useful.

When you [create a pivot table](https://trumpexcel.com/creating-excel-pivot-table/)
 using a data set, Excel automatically creates the Pivot Cache.

Pivot cache is an object that holds a replica of the data source.

While you can’t see it, it is a part of the workbook and is connected to the Pivot Table. When you make any changes in the Pivot Table, it does not use the data source, rather it uses the Pivot Cache.

While you think that you are directly linked to the source data, in reality, you access the pivot cache (and not the source data) when you make changes in the pivot table.

Now since you’re creating a replica of the data set, it takes some space.

So as soon as you create a Pivot table, you will notice that the size of the Excel file increase.

![Size of Excel Files with Pivot Table](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20534%20102'%3E%3C/svg%3E)

In the above example, as soon as I add the Pivot table, the size of the file increases two-fold.

Now, there are two ways you can reduce the file size when working with Pivot tables.

1.  Keep the source data and delete the Pivot Cache
2.  Keep the Pivot Cache and delete the source data

Let’s look at both these techniques.

#### Keep the Source Data and Delete Pivot Cache

When you’re done with the Pivot table and are saving it, you can force Excel to only save the source data and the resulting Pivot Table, and not the Pivot Cache.

Doing this will make your Excel file lighter, and you have a way to recreate the Pivot cache when you need it the next time.

Below is the difference in size when you save an Excel file with and without Pivot Cache.

![File Size with and without Pivot Cache](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20526%20104'%3E%3C/svg%3E)

Here are the steps to **NOT** save the Pivot Cache:

1.  Select any cell in the Pivot Table.
2.  Click the Analyze tab.![Click the Analyze Tab in Excel Pivot Table Contextual Tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20567%20160'%3E%3C/svg%3E)
3.  Click on Pivot Table ‘Options’ icon.![Click on the Options Button in Analyze Tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20275%20197'%3E%3C/svg%3E)
4.  In the Pivot Table Options dialog box, click on Data tab.![click on Data in Pivot table Options dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20564%20189'%3E%3C/svg%3E)
5.  In the Pivot Table Data options, **uncheck** ‘Save source data with file’. This option ensures that the Pivot Cache is not saved when you save the workbook (and helps in reducing Excel file size).![Uncheck Save Data Source Option in Pivot table Options dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20564%20373'%3E%3C/svg%3E)
6.  Check the option – ‘Refresh data when opening the file’. This option ensures that soon as you open the workbook, the Pivot Table is refreshed and the Pivot Cache is automatically generated. If you don’t check this option, you’ll have to [refresh the Pivot table](https://trumpexcel.com/refresh-pivot-table-excel/)
     manually to generate the Pivot Cache.![Check Refresh Data when opening the file option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20564%20373'%3E%3C/svg%3E)
7.  Click OK.

Now when you save the file with the Pivot table, you’ll notice a reduced file size.

#### Keep the Pivot Cache and Delete the Source Data

Another way reduce Excel file size is to delete the source data of a Pivot Table and keep the Pivot Cache only.

This works as a Pivot Cache is a mirror image of your data and you don’t access the source data when making changes to the Pivot Table, instead, you use the Pivot Cache.

Below is are results when I saved the Excel file without the source data.

![Reduce Excel File Size - by not saving source data in Pivot table](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20533%20108'%3E%3C/svg%3E)

To do this, just delete the data (either by deleting the data or the [worksheet](https://trumpexcel.com/delete-sheets-excel/)
 that has the data).

When you want to get the source data back, double-click on the ‘Grand Total’ cell of the Pivot table and it will instantly generate the entire data set in a new worksheet.

### Compress the File (ZIP IT)

This is something you can do outside of the Excel application.

When you zip an Excel file, you’ll see a size reduction of about 10-15% immediately.

You can then share this zipped file to via email, and the person receiving this can unzip the file and use the Excel workbook.

Here are the steps to Zip an Excel file (for Windows):

1.  Right-click on the Excel File
2.  Hover your cursor on the Send to option.
3.  Click on the ‘Compressed (zipped) folder’ option.![Compressed Zipped Folder Option in Windows](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20713%20627'%3E%3C/svg%3E)

This will create a zipped file for the selected Excel workbook.

You’ll also notice a reduction in file size (as shown below).

**Test Results**

![Size Reduction in Excel by Zipping the file](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20547%20113'%3E%3C/svg%3E)

With this technique, I was able to reduce the file size of the Excel workbook by 8%.

This technique works better for files that are in the 20-50 MB range. As the file size increases, the percentage reduction is not very high.

### Remove Data formatting

Data formatting such as applying a background color, or adding borders, or [changing font style](https://trumpexcel.com/best-excel-fonts/)
 can all add to the file size.

Although, based on my tests, I noticed that it doesn’t have a huge impact.

Below are the sizes of two Excel workbooks, one with 2.6 million data points (in one worksheet), and the other with the same data but formatting applied to it (cell color, border, and italicized).

**Test Results**

You can see the difference between the two files is not that huge (although it does make an impact when you have a lot of data).

![Reduce Excel File Size - Test 2 formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20518%20124'%3E%3C/svg%3E)

The file with data is 14.6 MB and the file with data and formatting is 14.9 MB.

So if you want to reduce the file size of your Excel workbook, you can look for formatting you don’t need. Removing it can save you some disk space.

Here are the steps to instantly remove all the formatting, while keeping the data intact:

1.  Select the entire dataset (from which you want to remove formatting).
2.  Click the Home tab.![Home Tab in Excel Ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20325%20151'%3E%3C/svg%3E)
3.  In the Editing group, click on ‘Clear’.![Click on Clear in Excel Ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20279%20118'%3E%3C/svg%3E)
4.  Click on ‘Clear Formats’.![Click on Clear Formats in Excel Ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20203%20279'%3E%3C/svg%3E)
5.  Save the workbook.

### Remove Conditional formatting

Just like regular data formatting, [conditional formatting](https://trumpexcel.com/excel-conditional-formatting/)
 also adds to the file size.

However, based on my tests, I noticed that the difference is less (unless you have multiple rules applied to multiple sheets with huge datasets).

Nevertheless, it’s a good idea to [remove conditional formatting](https://trumpexcel.com/remove-conditional-formatting-excel/)
 from any dataset where you don’t need it.

Apart from the size, there is another good reason to remove conditional formatting – SPEED.

Conditional formatting is volatile and whenever there is any change in the worksheet, it recalculates. This can lead to a slower workbook.

**Test Results**

I created a file with 27.2 million data points and applied 5 conditional formatting rules to it.

The difference in size seems to be only a few KBs.

![Excel File Size difference with Conditional Formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20703%20112'%3E%3C/svg%3E)

**Also Read**: [Tips to Make Slow Excel Spreadsheets Fast](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/)

Excel Performance Booster Tips
------------------------------

While the above methods will help you reduce Excel file size, here are some additional tips to improve the performance of Excel Workbooks:

1.   Avoid using volatile formulas. Apart from increasing the file size, volatile formulas also make you workbooks slow. Examples of volatile functions include [RAND](https://trumpexcel.com/excel-rand-function/)
    , [TODAY](https://trumpexcel.com/excel-today-function/)
    , [OFFSET](https://trumpexcel.com/excel-offset-function/)
    , [INDIRECT](https://trumpexcel.com/excel-indirect-function/)
    , etc.
2.  If you have a need to create summaries of a large dataset, instead of using formulas, see if you can use a Pivot Table instead. A Pivot table is fast and very intuitive as compared to formulas.
3.  If you extract data from multiple sources or [combine data from multiple files](https://trumpexcel.com/combine-data-from-multiple-workbooks/)
    , use [Power Query](https://trumpexcel.com/category/power-query/)
     to get and transform the data. You can save the data as a Power Query connection instead of keeping it in the worksheet. You can easily create Pivot Table using the connections created using Power Query.
4.  Convert your tabular data into an [Excel table](https://trumpexcel.com/excel-table/)
     and use the Excel table in formulas. It makes your workbook perform faster and formulas created using Excel Table structured references are easier to manage (as these are more intuitive).
5.  Avoid referencing entire row or column in a formula. This will help your formulas be more efficient.
6.  If you have a lot of formulas in your workbook, turn off Automatic calculation and switch to manual calculation. By doing this, every time there is a change in the worksheets, the formulas wouldn’t recalculate. You can make this change by going to the Formula tab and changing the ‘Calculation Options’.

Hope you find the method and tips in this tutorial useful.

What else I could add to this tutorial to make it more useful? Please let me know in the comments section.

**You May Also Like the Following Excel Tutorials:**

*   [How to Recover Unsaved Excel Files](https://trumpexcel.com/recover-unsaved-excel-files/)
    .
*   [100+ Excel Interview Questions](https://trumpexcel.com/excel-interview-questions/)
    .
*   [Best Excel Books](https://trumpexcel.com/best-excel-books/)
     (to Level up your Excel Skills).
*   [200+ Excel Keyboard Shortcuts](https://trumpexcel.com/excel-keyboard-shortcuts/)
    .
*   [10 Ways to Clean Data in Excel](https://trumpexcel.com/clean-data-in-excel/)
    .
*   [How to Turn On AutoSave in Excel](https://trumpexcel.com/turn-on-autosave-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

25 thoughts on “8 Ways to Reduce Excel File Size (that actually work)”
----------------------------------------------------------------------

1.  Very helpful tips. Thanks a lot.
    
    [Reply](https://trumpexcel.com/reduce-excel-file-size/#comment-14773)
    
2.  Awesome content, really helpful. You covered all the points with the most precise knowledge for a layman to know.
    
    Also, I would like you to please make some content for using power queries to connect data in cell pivot tables.
    
    Thanks
    
    [Reply](https://trumpexcel.com/reduce-excel-file-size/#comment-13868)
    
3.  I found very useful tips here & became very grateful To You Dada
    
    [Reply](https://trumpexcel.com/reduce-excel-file-size/#comment-13582)
    
4.  fuck
    
    [Reply](https://trumpexcel.com/reduce-excel-file-size/#comment-13528)
    
5.  Hi, I reduced my file from 40 to 1,3 MB, by deleting all formating from row 400 to the bottom of the document.
    
    [Reply](https://trumpexcel.com/reduce-excel-file-size/#comment-13127)
    
6.  If multiple pivot tables are used with the same root data rather than creating a new pivot table, copy an existing table and change the pivot selections. Each new table creates a new pivot cache – increasing the file size, copying an existing table enables the same cahe to be used multiple times, and also holds an advantage of updating one pivot updates all.
    
    [Reply](https://trumpexcel.com/reduce-excel-file-size/#comment-12804)
    
7.  Super cool!
    
    No tips were helping and I already wanted to leave the page… when I reached your mentioning of pivots. What a nonsense to save the complete data source with every pivot… reduced my excel from 29747 KB to 1461 KB, so a reduction of 95.09%! Thanks a lot!
    
    [Reply](https://trumpexcel.com/reduce-excel-file-size/#comment-12327)
    
8.  Awesome post. Changing the file format to binary reduced my file size from 40 mb to 3 mb. That really made my day!
    
    [Reply](https://trumpexcel.com/reduce-excel-file-size/#comment-12204)
    
    *   Glad the tutorial helped!
        
        [Reply](https://trumpexcel.com/reduce-excel-file-size/#comment-12205)
        
9.  When sheets are copied between workbooks, ALL Styles from the parent are added to the new workbook  
    This can be done many, many times and I’ve had files with over 80,000 of them  
    Such a file is much larger and takes ages to open  
    Removing extra Styles individually is tedious at best but can be done easily and quickly with VBA
    
    [Reply](https://trumpexcel.com/reduce-excel-file-size/#comment-12020)
    
10.  Thank you for sharing these very useful tips
    
    [Reply](https://trumpexcel.com/reduce-excel-file-size/#comment-11611)
    
11.  Thank you. It worked for me. very useful tips to reduce the size of excel book
    
    [Reply](https://trumpexcel.com/reduce-excel-file-size/#comment-11515)
    
12.  thank you for sharing, this helped a great deal.
    
    [Reply](https://trumpexcel.com/reduce-excel-file-size/#comment-11416)
    
13.  Wow. Thank you. I didn’t have to do all the steps and I’ve already reduced my file by 45%!
    
    [Reply](https://trumpexcel.com/reduce-excel-file-size/#comment-11144)
    
14.  It works and really thankful to author.
    
    [Reply](https://trumpexcel.com/reduce-excel-file-size/#comment-10999)
    
15.  Sir I really appreciate to this articals about reducing excel sheet  
    i applied this today  
    thanks so much guidence us.
    
    [Reply](https://trumpexcel.com/reduce-excel-file-size/#comment-10964)
    
16.  Hi Sumit,
    
    Thanks so much for your article. It would be very useful to me today as I need to compress an Excel sheet that’s shot up in size post an update to the formulae in it.
    
    I found an article on LinkedIn that also addressed another issue that causes Excel size bloats which isn’t mentioned here. You may want to check it out.
    
    Currently, doing a Google search for “why is my excel file so big linkedin” would show produce the link to this article by Jonathon Power.
    
    I hope you’re able to test it and include it in your comprehensive article, which has already been close to a one-stop shop for me. Thanks again for putting it up.
    
    [Reply](https://trumpexcel.com/reduce-excel-file-size/#comment-10844)
    
17.  hmmm..impracive
    
    [Reply](https://trumpexcel.com/reduce-excel-file-size/#comment-10631)
    
18.  I like most of the suggestions.
    
    I’ve had some bad experiences with the XLSB file format where the file was unrecoverable. I learned early on to save different versions as I work so I didn’t lose a ton of time. I’m willing to try it again.
    
    Does anyone have a reliable experience working with XLSB files over a period of months vs. a few times? And with file sizes larger than the 5MB threshold mentioned.
    
    [Reply](https://trumpexcel.com/reduce-excel-file-size/#comment-10618)
    
19.  Hi,  
    What about using worksheets formulas in a VBA code rather than in cells?
    
    TY,  
    Shay
    
    [Reply](https://trumpexcel.com/reduce-excel-file-size/#comment-10562)
    
20.  With XLSB files there will be a macro warning and Power Query can read them.
    
    [Reply](https://trumpexcel.com/reduce-excel-file-size/#comment-10492)
    
21.  One of the most important for me is to avoid applying formats to complete rows / columns.  
    Also, if we delete data from some rows/columns, those might still be part of the used range. So, deleting those adjacent rows/columns without data and then save the workbook help us in reducing the size.
    
    [Reply](https://trumpexcel.com/reduce-excel-file-size/#comment-10484)
    
22.  I found that using Tables, saves space when there are formulas in the columns. I had a large range, something like 25,000 rows x 150 columns, with the bulk of columns containing formulas. This reduced my xlsm file from 18Mb to 5Mb (and going to xlsb dropped it further). I suspect it only stores the formula once per column for a table, rather for every row!
    
    [Reply](https://trumpexcel.com/reduce-excel-file-size/#comment-10483)
    
    *   Thanks for sharing Ed. I will test it out and add this to my article.
        
        [Reply](https://trumpexcel.com/reduce-excel-file-size/#comment-10496)
        
23.  Compress the file (ZIP it) may not really save you much. An \*.xlsx file is already compressed (you can confirm this by renaming any \*.xlsx file into a \*.zip)
    
    [Reply](https://trumpexcel.com/reduce-excel-file-size/#comment-10479)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/reduce-excel-file-size/#respond)

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