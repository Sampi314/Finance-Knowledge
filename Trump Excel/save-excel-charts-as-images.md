# How to Save Excel Charts as Images (save as PNG, JPG, BMP)

**Source:** https://trumpexcel.com/save-excel-charts-as-images

---

[Skip to content](https://trumpexcel.com/save-excel-charts-as-images/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/save-excel-charts-as-images/#below-title)

**Watch video – Save Excel Charts as Images/Pictures**

Excel has a lot of useful in-built charts and you can also combine and create some amazing combination charts as well. Excel charts are a great way to show your data visually and are often the most used ones when you have to present it to your manager/clients.

While your charts may be in Excel, it’s not necessary that it’s the best way to show them to your clients/managers. Often, it would be required to show these charts in a PowerPoint presentation or in an MS Word document of PDFs.

It would have been great had their been an in-built feature to save Excel charts as images, but that’s not the case.

However, there are some ways you can easily save and export charts in Excel as images (JPG, PNG, BMP are some popular ones), and in this tutorial, I will cover these methods.

The method I use would depend on how many charts you have. If you only have a couple of charts that you want to save as images, you can use the copy-paste method, but if you have many, it’s better to use the ‘download as HTML’ or VBA methods.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/save-excel-charts-as-images/#)

Copy the Chart as Save as an Image (MS Paint or Other Graphics Tool)
--------------------------------------------------------------------

A really common method I see a lot of people using is by taking the screenshot of the entire screen (this can be done by hitting the PrintScreen key). Once this is done, you can open MS Paint (or whatever tool you use), paste the screenshot, and then remove everything else and just keep the image.

While this is a fine way to save a chart as an image and works well, there is a better way (which takes less time and the images are more accurate).

Suppose you have an Excel file with a chart as shown below:

![Chart that needs to be saved as an image](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20772%20373'%3E%3C/svg%3E)

Below are the steps to save this chart/graph as an image:

1.  Right-click on the chart that you want to save
2.  Click on Copy![Click on Copy chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20682%20429'%3E%3C/svg%3E)
3.  Open MS Paint (or whatever tool you use)
4.  Paste the image (Control V works for MS Paint)![Paste the chart in MS Paint](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20546%20488'%3E%3C/svg%3E)
5.  If there is any extra white space, just select and drag it so you only have the chart
6.  Click the File tab![Click File tab in MS Paint](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20253%20170'%3E%3C/svg%3E)
7.  Go to Save As
8.  Click on the image format in which you want to save the chart (there is JPG, PNG, and BMP format).![Save the chart as the PNG image](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20443'%3E%3C/svg%3E)

The benefit of this method overtaking a screenshot is that this method only copies the chart and you need to adjust the white space in MS Paint once (this may not be needed if you’re using any other graphics tool).

In case you have two or more charts arranges already in Excel and you want to save this entire arrangement as an image, you can do that by selecting all these charts, copying them, and pasting them in MS Paint.

**Save All the Charts in the Workbook as Images At One Go**
-----------------------------------------------------------

If you have a workbook that has a lot of charts and you want to save all these charts at one go, a better way is to save the Excel workbook as an HTML file.

When you do this, all the charts in your Excel workbook will be **saved as PNG format images** in the downloaded folder.

Suppose you have an Excel workbook with multiple sheets with charts.

Below are the steps to save the file as HTML and save the Excel charts as images in PNG format:

1.  Open the workbook in which you have the charts
2.  Click the File tab![Click File tab in Excel ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20368%20200'%3E%3C/svg%3E)
3.  Click on Save As![Click on Save As](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20618%20595'%3E%3C/svg%3E)
4.  Click on Browse and select the location where you want to save all the chart images![Click on Browse](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20618%20595'%3E%3C/svg%3E)
5.  Change the ‘Save as type’ to Web Page (\*.htm, \*.html)![Save as Web Page HTM or HTML](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20780%20632'%3E%3C/svg%3E)
6.  Click on Save

This will save your Excel file as a web page in the specified folder.

Now to get all the charts as images, go to the folder and you’ll find a folder with the name Filename\_files (where FileName would be the name you gave to the file while saving it).

When you open this folder, you will find all the charts that have been saved as PNG images.

![Excel file saved as an HTML web page](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20782%20179'%3E%3C/svg%3E)

**Note**: When I tried this on my system, it gave me two images (identical) for each chart. So if you have four charts, it will give you eight images.

**Caution**: Before you save the Excel file as HTML, make sure you save a backup copy. Also, when you save a file as HTML, the currently open file is now an HTML file and not the Excel format file. After saving the file, you should close the current file (which is now an HTML file) and open the [Excel version](https://trumpexcel.com/excel-version/)
 (this is why it’s important to take a backup)

**Save All the Charts As Images Using VBA**
-------------------------------------------

You can also use a VBA code to quickly save charts from an Excel workbook to a specific folder.

If you only need to save the active chart (the one that you have selected) into a specific folder, you can use the below VBA code:

ActiveChart.Export ":\\Users\\sumit\\Desktop\\Example\\ChartName.png"

The above code will save the active chart in the Example folder with the name ChartName in the PNG format. You can change the chart name and the folder name/location based on where you want it.

In case you want to save the image/picture in the JPG format, you can use the below code:

ActiveChart.Export ":\\Users\\sumit\\Desktop\\Example\\ChartName.jpg"

You can [run this VBA code](https://trumpexcel.com/run-a-macro-excel/)
 by putting it in the immediate window, placing the cursor at the end of the line and hitting the Enter key (or you can put in a regular module and run the code from there).

But this method would be quite a time taking in case you have a lot of charts. In such a case, you can use a slightly longer VBA code mentioned below:

Sub SaveChartsasImages()
Dim i As Integer
Dim CurrentActiveSheet As Worksheet

Application.ScreenUpdating = False
Application.EnableEvents = False

Set CurrentActiveSheet = ActiveSheet

For Each Sht In Worksheets
    For Each cht In ActiveSheet.ChartObjects
        cht.Activate
        i = i + 1
        ActiveChart.Export "C:\\Users\\sumit\\Desktop\\Example\\" & Sht.Name & "\_chart" & i & ".png"
    Next cht
Next Sht

CurrentActiveSheet.Activate

Application.ScreenUpdating = True
Application.EnableEvents = True

End Sub

The above code goes through each worksheet in the workbook and then within each worksheet it goes to each chart. It then selects the chart and saves it in the specified folder.

All this [looping](https://trumpexcel.com/vba-loops/)
 is done using the For [Each Next loop](https://trumpexcel.com/for-next-loop-excel-vba/)
.

Also, the charts are saved with the name format worksheetname\_chartNumber. This would ensure that you’re able to identify what chart belongs to which worksheet.

Another good thing about using VBA is that you can customize the code to only save charts as images from some specific sheets. For example, if you only want to save charts from sheets that have the prefix 2020 in it, you can modify the code to do this (this can be done using an [IF THEN ELSE statement](https://trumpexcel.com/if-then-else-vba/)
 after the FOR loop line)

Copy and Paste Excel Charts as Images in MS Word or PowerPoint
--------------------------------------------------------------

In most cases, you will have to present your charts in MS Word or PowerPoint documents. This is often the case if you’re creating client reports or documentation.

Just like you can copy and paste an image in MS Paint, you can also do the same with Word or PowerPoint.

But there is one difference…

When you copy a chart/graph in Excel and paste it in MS Word or MS PowerPoint, it doesn’t get pasted as an image. It actually gets pasted as a ‘Microsoft Office Graphic Object’

This option is useful for people who want to have the chart remain a chart even when in MS Word or PowerPoint, so you can edit and format it as a chart. Also, this type of chart is still connected to the data in Excel, and when you update the data in the backend, this pasted chart would also update.

But in case you want this chart to be pasted as an image, below is the way to do this (in this example, I will be using MS Word to showcase the steps, and these would be the same for PowerPoint as well):

1.  Select the chart that you want to copy to MS Word
2.  Right-click and then click on Copy![Click on Copy chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20682%20429'%3E%3C/svg%3E)
3.  Open MS Word document where you want to paste this chart as an image
4.  In the Home tab, within the Clipboard category, click on the Paste icon (the downward-pointing arrow part).![Click on Paste Option in the Home tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20295%20201'%3E%3C/svg%3E)
5.  In the options that appear, click on Paste as Picture option![Paste chart as Picture](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20274%20333'%3E%3C/svg%3E)

The above steps would make sure the chart is pasted as a picture.

In case you simply click on the Paste Button (and not on Paste as Picture), the graph will not be pasted as a picture.

So these are four ways you can quickly save charts in Excel as images. Some methods allow you to choose the format of the image as well (such as using MS Paint or VBA).

In case you only have a few charts, you can use the MS Paint method, but in case there are many charts across sheets that you want to save, it’s better to use the HTML method or the VBA code. And if the final intent is to insert these charts in Word or PowerPoint anyway, it’s better to directly copy and paste these as a picture in these other tools.

Hope you found this tutorial useful.

**You may also like the following Excel tutorials:**

*   [How to do a Picture Lookup in Excel](https://trumpexcel.com/picture-lookup/)
    
*   [How to Insert a Picture in Excel Comment](https://trumpexcel.com/insert-picture-in-excel-comment/)
    
*   [How to Insert an Image Into a Cell in Excel](https://trumpexcel.com/insert-picture-into-excel-cell/)
    
*   [Advanced Excel Charts](https://trumpexcel.com/advanced-charts/)
    
*   [How to Copy Excel Table to MS Word](https://trumpexcel.com/copy-excel-table-to-word/)
    
*   [How to Move Chart to New Sheet in Excel?](https://trumpexcel.com/move-chart-to-new-sheet-excel/)
    
*   [Save As Shortcuts in Excel (Quick and Easy)](https://trumpexcel.com/save-as-shortcuts-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

1 thought on “How to Save Excel Charts as Images (save as PNG, JPG, BMP)”
-------------------------------------------------------------------------

1.  Hi Sumit  
    the trick you share with us is great and added to your other post “How to Insert a Picture in Excel Comment”, I have a question about whether it is possible to insert an image that comes from a cut made with the Snipping Tool to a comment, since currently what I do is go Power Point and with the Save as Picture option I save the clipping as PNG and then I go to excel and apply the option Format Comment to be able to insert it.  
    It is an activity that I have to do for catagos in which I work for more than 100 records a day, it would be useful to me find out how to automate this activity but I don’t know how to do it.  
    Best regards
    
    [Reply](https://trumpexcel.com/save-excel-charts-as-images/#comment-14144)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/save-excel-charts-as-images/#respond)

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