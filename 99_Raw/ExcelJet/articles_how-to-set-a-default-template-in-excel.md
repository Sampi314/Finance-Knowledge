# How to set a default template in Excel | Exceljet

**Source:** https://exceljet.net/articles/how-to-set-a-default-template-in-excel

---

[Skip to main content](https://exceljet.net/articles/how-to-set-a-default-template-in-excel#main-content)

[](https://exceljet.net/articles/how-to-set-a-default-template-in-excel#)

*   [Previous](https://exceljet.net/articles/how-to-use-the-mod-function-to-repeat-values)
    
*   [Next](https://exceljet.net/articles/how-to-find-text-with-a-formula)
    

How to set a default template in Excel
======================================

by Dave Bruns · Updated 25 Jun 2025

![How to set the default template used for new workbooks in Excel](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/default%20workbook%20template2.png "How to set the default template used for new workbooks in Excel")

Summary
-------

Excel has the ability to use a custom template for all new workbooks. If you find yourself making the same changes to new workbooks (changing row height, font size, zoom, etc.) a default custom template can save you time and trouble.

Do you find yourself creating new workbooks in Excel, then making the same changes to every one? Maybe you like to change font size, zoom percent, or the default row height?

If so, you can save yourself time and trouble by setting a _default template_ for Excel to use each time you create a new workbook. As long as you name the template correctly, and put it in the correct location, Excel will use your custom template to create all new workbooks.

> The biggest challenge with this tip is figuring out the right location for the template file. This can be maddeningly complex, depending on which platform and version of Excel you use. If you get frustrated and can't make things work, you can set up your own startup folder manually, as described below.

### Settings that can be saved in a template

A template can hold many custom options. Here are a few examples of settings that can be saved in a workbook template:

*   Font formatting and styles
*   Display options and zoom settings
*   Page setup and print options
*   Column widths and row heights
*   Page formats and print area settings for each sheet
*   The number (and type) of sheets in new workbooks
*   Placeholder text (titles, column headers, etc.)
*   Data validation settings
*   Macros, hyperlinks and ActiveX controls
*   Workbook calculation options

> These settings only apply to new workbooks created after a custom template file is installed.

### The process

1.  Open a new blank workbook and customize the options as you like
2.  Save the workbook as an **Excel template** with the name "**book**" (Excel will add **.xltx**) \*
3.  Move the template to the startup folder used by Excel
4.  Disable Start screen at General > Start up options) \*\*
5.  Quit and relaunch Excel to be sure settings are fresh
6.  Test to be sure Excel is using the template when new workbooks are created

_\* Based on comments, it seems the name of your workbook must be localized for your version of Excel. For example, if you're using the Czech version, you need to use "Sešit" instead of "book"._

_\* \* Not strictly required, but the "New blank workbook" option on the Start screen seems to ignore a custom template (?)._

### Common startup folder locations

Whenever Excel is launched, it establishes what is called a "startup folder", which is named XLSTART. The key is to put your template file into this folder so that Excel will find it. Unfortunately, the exact location of XLSTART varies according to the versions of Excel and Windows you use. Here are some common locations:

*   C:\\Program Files\\Microsoft Office\\OFFICEx\\XLSTART
*   C:\\Users\\user\\AppData\\Microsoft\\Excel\\XLSTART
*   C:\\Users\\user\\AppData\\Roaming\\Microsoft\\Excel\\XLSTART

### Can't find XLSTART?

If you can't find the startup folder for Excel (XLSTART), you can use the VBA to confirm Excel's start-up path like this:

1.  Run Excel
2.  Open the VBA editor (Alt + F11)
3.  Open the Immediate Window (Control + G)
4.  Type: `? application.StartupPath` in the window
5.  Press Enter

The startup path will appear below the command. Once you've confirmed the location of XLSTART, drop in your template file.

![Use the VBA immediate window to confirm startup path](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/Use%20VBA%20to%20find%20Excel%20startup%20folder.png?itok=15aXzxTv "Use the VBA immediate window to confirm startup path")

### Set your own startup directory

If you can't find Excel's startup directory, or if burying your template deep in an application hierarchy just seems wrong, you can tell Excel to look in _your own startup folder_ by setting an option as follows:

1.  Create a directory called "**xlstart**" where you like.
2.  Put your custom template in the new directory.
3.  At **Options > Advanced > General > Open all files in**, enter the path to **xlstart**.
4.  Test to make sure the template is working.

![You can set your own custom startup path in Advanced Options](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/Set%20custom%20startup%20path%20in%20options.png?itok=q_JQRLBk "You can set your own custom startup path in Advanced Options")  
_Telling Excel about your own startup folder...make sure you use the correct path on your computer!_

### Test to make sure your template is being used

After you go through the steps to set up a default template, make sure you test to confirm your template is being used. One easy way to do this is to (temporarily) give cell A1 in your template a bright yellow or orange fill. That way, you can immediately see if your custom template is being used when you create a new document. Once you're sure things are working, remove the marker.

![Fill color in A1 confirms that the custom template is being used](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/testing%20default%20workbook%20template.png?itok=PU2TUwGv "Fill color in A1 confirms that the custom template is being used")

> Note 25-Jun-2025 - I had trouble getting Excel to use my custom template on a new Windows 11 machine, even though book.sltx was in the correct location. The problem was Excel using a start screen. If your template is still not loading, check to see if the "Start screen" is enabled at File > Options > General > Startup options. If so, uncheck the option "Show the Start screen when this application starts". This setting can prevent the template from loading.

### Setting a default Excel template on the Mac

The process for setting a default Excel template on a Mac is similar to the steps above for Windows. Again, confirming the startup folder can be tricky, depending on whether you have Excel 2011 or 2016 installed (2008 not tested). In Excel 2016, according to Microsoft, [there is currently no startup folder](https://support.microsoft.com/en-us/kb/259921)
. Also, as of mid-2016, the name of the template should be "workbook" (manually remove the .xltx extension) not "book".

Because of confusion around the startup folder, here's what I recommend on a Mac:

1.  Create a new directory in your home documents folder called "**xlstart**".
2.  Go to **Preferences > General > At startup, open all files in**, and set **xlstart** as path.
3.  Open a new workbook and customize the options as you like
4.  Save the workbook as an Excel template with the name "**workbook.xltx**" inside **xlstart**.
5.  Manually remove the extension "**.xltx**" so that the file is named only "**workbook**".
6.  Quit and relaunch Excel to be sure the settings are updated.
7.  Test to confirm Excel uses the template when new workbooks are created.

I tested this with Excel 2011 and Excel 2016 installed on the same Mac in May 2016, and both used the same template as expected.

_Note: Tested again in January 2020. Step #5 above (removing the extension) was not needed. Also, I was able to use 'book.xltx' for the filename, like the Windows version._

### Template for new sheets

A workbook template controls the look and layout of sheets already in the workbook, but not new sheets. When you insert a new sheet, it will inherit Excel's sheet defaults. If you want to control new sheets with your own template, follow the process below.

1.  Open a new blank workbook and delete all sheets except one.
2.  Make desired customizations to the sheet.
3.  Save as an **Excel template** named "**sheet.xltx**" to the location determined above. \*\*
4.  Close the file.

_\*\* If using a non-English version of Excel, you may need to localize this name._

To test that the sheet template is working, open a workbook and add a new sheet. You should see your customizations in all newly inserted sheets.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Thank you for your very clear explanation on how to test for an existing tab name in a workbook using ISREF and INDIRECT. With your guidance, I am able to build a flexible template that can use variables to test...I really like your site layout and your concise directions. Thank you again!

Thierry

[More Testimonials](https://exceljet.net/feedback)

Get [Training](https://exceljet.net/training)

----------------------------------------------

### Quick, clean, and to the point training

Learn Excel with high quality video training. Our videos are quick, clean, and to the point, so you can learn Excel in less time, and easily review key topics when needed. Each video comes with its own practice worksheet.

[View Paid Training & Bundles](https://exceljet.net/training)

[![Excel foundational video course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_excel.png "Excel foundational video course")](https://exceljet.net/training)

[![Excel Pivot Table video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_pivot.png "Excel Pivot Table video training course")](https://exceljet.net/training)

[![Excel formulas and functions video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_formula_0.png "Excel formulas and functions video training course")](https://exceljet.net/training)

[![Excel Charts video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_charts.png "Excel Charts video training course")](https://exceljet.net/training)

[![Video training for Excel Tables](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_excel_tables.png "Video training for Excel Tables")](https://exceljet.net/training)

[![Dynamic Array Formulas](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_dynamic_array_formulas_0.png "Dynamic Array Formulas")](https://exceljet.net/training)