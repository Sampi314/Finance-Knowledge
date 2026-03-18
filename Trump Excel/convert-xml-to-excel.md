# How to Import XML File into Excel | Convert XML to Excel

**Source:** https://trumpexcel.com/convert-xml-to-excel

---

[Skip to content](https://trumpexcel.com/convert-xml-to-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/convert-xml-to-excel/#below-title)

The XML file format is quite commonly used on the web, and there is a possibility that sometimes you may have to work with the data in the XML file.

Now you can’t use the XML file directly, as it’s not meant to be read by humans (but machines).

In such a case, it would help to know how to convert the XML file to Excel so you can easily work with the data and analyze it.

In this tutorial, I will show you two really simple ways to **import an XML file into Excel using Power Query**.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/convert-xml-to-excel/#)

What is an XML File?
--------------------

XML stands for **Extensible Markup Language**. An XML file can hold data in a format that can easily be read by apps and systems.

But it’s not as easy to read for humans, which is why we may have to transform it into a format that’s easier to use.

If it contains a lot of text data, then you can use a text editor to read the XML file, and if it contains data, then you can import that XML file into Excel and then work with the data.

XML is quite widely accepted as a file format to store and transmit data over the web.

A lot of popular file formats, such as Microsoft Office Open XML, LibreOffice, OpenDocument, XHTML, and SVG, also use the XML file format.

Most popular websites on the Internet have their sitemap in an XML format.

This is a file that contains the details of all the important pages and categories on a website. Here is an example of the [sitemap from Forbes](https://www.forbes.com/sitemap_index.xml)
.

Now let’s see how to convert an XML file to Excel using Power Query.

Import XML File to Excel
------------------------

If you already have an XML file (either downloaded on your system or a link to it on the web), you can easily convert it into data in an Excel file.

Thanks to **Power Query** (now called ‘Get & Transform’)

### Import XML File that is Saved On your System

For the purpose of this tutorial, I’ll use an XML file that contains the sitemap for Forbes. You can download the file by [going to this link](https://www.forbes.com/sitemap_index.xml)
, then right-click and save the file.

Once you have the XML file on your system, follow the below steps to get the XML file data into Excel:

1.  Open the Excel file where you want to get the data from the XML file
2.  Click the Data tab![Data tab in the ribbon in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20671%20201'%3E%3C/svg%3E)
3.  In the ‘Get & Transform’ data group, click on the ‘Get Data’ option![Click on the Get Data drop down](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20712%20201'%3E%3C/svg%3E)
4.  Go to the ‘From file’ option
5.  Click on ‘From XML’![Click on From XML option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20494%20581'%3E%3C/svg%3E)
6.  In the input data dialog box that opens up, locate the XML file that you want to import and select it
7.  Click Import. This will import the XML file into power query and open the Navigator dialog box
8.  Select the data from the XML file that you want to import. In this case, I would click on ‘sitemap’ in the left pane![Click on the Sitemap option in the left pane](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20780%20330'%3E%3C/svg%3E)
9.  \[Optional\] Click on the Transform Data button, if you want to transform the data before loading it into Excel (such as change the column names or remove some columns)
10.  Click on Load

The above steps would [insert a new worksheet](https://trumpexcel.com/insert-new-worksheet-excel/)
 in the Excel file, and load all the data from the XML file into the new worksheet.

![XML data in the Excel file](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20516'%3E%3C/svg%3E)

The great thing about using Power Query to fetch the data from an XML file into Excel is that in case the XML file updates and there are new records in it, you don’t have to repeat the same process.

You can simply right-click on any cell in the table and refresh the query.

![Click on Refresh](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20523'%3E%3C/svg%3E)

Also read: [How to Insert PDF into Excel](https://trumpexcel.com/embed-pdf-file-excel/)

### Import XML File into Excel using the web URL

In the above example, we first downloaded the XML file on the system and then imported the data into Excel.

In case you have a web URL that contains the XML file (such as this one – https://www.forbes.com/sitemap\_index.xml), you don’t even need to download the file. you can connect Power Query to that URL and extract the XML data into Excel.

Below are the steps to connect power query do a web URL that contains the XML data and import that data into Excel:

1.  Open the Excel file where you want to import the data
2.  Click the Data tab![Data tab in the ribbon in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20671%20201'%3E%3C/svg%3E)
3.  In the Get & Transform group, click on the ‘Get Data’ option![Click on the Get Data drop down](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20712%20201'%3E%3C/svg%3E)
4.  Go to the ‘From Other Sources’ option
5.  Click on ‘From Web’![Click on from Web](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20756'%3E%3C/svg%3E)
6.  In the ‘From Web’ dialog box, copy and paste the URL that has the XML data![Enter the URL from which you want to get the XML data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20701%20219'%3E%3C/svg%3E)
7.  Click OK. This will open the Navigator dialog box where you can choose which XML data to import
8.  Click on ‘sitemap’, which is the XML data that I want in Excel![Sitemap in the left pane navigator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20750%20443'%3E%3C/svg%3E)
9.  \[Optional\] Click on the Transform Data button, if you want to transform the data before loading it into Excel (such as change the column names or remove some columns)
10.  Click on Load

The above steps would insert a new worksheet in the Excel file, and load all the data from the XML file into the new worksheet.

And again, in case the data updates in this URL, simply refresh the query to get the new data in Excel.

So these are two simple ways that you can use to convert an XML file into Excel.

If you have the XML file on your system, you can import the data easily using Power Query. And if you have a web URL of the XML file, then you can also fetch that data into Excel.

I hope you found this tutorial useful.

**Other Excel tutorials you may also like:**

*   [8 Ways to Reduce Excel File Size (that actually work)](https://trumpexcel.com/reduce-excel-file-size/)
    
*   [How to Automatically Open Specific Excel File on Startup](https://trumpexcel.com/automatically-open-excel-file-startup/)
    
*   [Inserting Excel Tables Into Word](https://trumpexcel.com/copy-excel-table-to-word/)
    
*   [How to Recover Unsaved Excel Files \[All Options + Precautions\]](https://trumpexcel.com/recover-unsaved-excel-files/)
    
*   [Microsoft Excel Won’t Open – How to Fix it! (6 Possible Solutions)](https://trumpexcel.com/microsoft-excel-wont-open/)
    
*   [How to Convert Excel to PDF Using VBA](https://trumpexcel.com/convert-excel-to-pdf/)
    
*   [Split Each Excel Sheet Into Separate Files (Step-by-Step)](https://trumpexcel.com/split-each-excel-sheet-into-separate-files/)
    
*   [Combine Data from Multiple Workbooks in Excel (using Power Query)](https://trumpexcel.com/combine-data-from-multiple-workbooks/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

1 thought on “How to Import XML File into Excel | Convert XML to Excel”
-----------------------------------------------------------------------

1.  Perfect. Took me 3 minutes to execute. Thanks so much.- Dan.
    
    [Reply](https://trumpexcel.com/convert-xml-to-excel/#comment-15984)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/convert-xml-to-excel/#respond)

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