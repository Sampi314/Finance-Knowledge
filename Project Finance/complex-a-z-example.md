# A-Z Case 1

**Source:** https://edbodmer.com/complex-a-z-example

---

This page illustrates a more real world and complex example of converting data using the read pdf to excel program.  In the example, you need to make a couple of adjustments to the raw data you get from the PDF file. You also should to use the single data in rows method and you need to do some of your own work to get the titles moved around properly. Hopefully you can see how the program can be used when data does not come out in a nice smooth manner from a pdf file.

Before looking at this page, [note that if you want to see the fundamental of reading from a pdf file, go to the basic page.](https://edbodmer.com/read-pdf-to-excel/)

My friend Ayat suggested this when she told me that the read pdf program works sometimes, but other times it is a pain.  She was very frustrated and prompted me to re-think the explanation process.

![](https://edbodmer.com/wp-content/uploads/2018/07/Hyat-Comment.jpg)

So here goes my explanation….

As a reminder, when working with the conversion, you need to download the download the file with the various macros as usual.  After opening the file, make sure that the status bar at the bottom of your excel file has the Shift, CNTL A instructions.  The file is available for download below.

**[Read PDF to Excel File that Allows you to Format Data After Copying from PDF File (Press Shift, Cntl, A)](https://edbodmer.com/wp-content/uploads/2019/04/Read-PDF-to-Excel.xlsm)
**

Step 1: Get the PDF Data
------------------------

The example that Ayat gave me, is from a file named “Jordan Food Consumption by Area.”  Some of the titles are in Arabic ans some in English. I have put this file on the website for download below.  When you try and select the area for copying, it is not easy.  This should make you say Sh…….  there may be some problems here.  After you mess around with the mouse, you should be able to get the data as illustrated in the screenshot below.

**[Example of PDF File that has Some Painful Problems and Does Not Download to Excel in a Clean Way](https://edbodmer.com/wp-content/uploads/2018/07/Jordans-Food-consumption-per-area.pdf)
**

![](https://edbodmer.com/wp-content/uploads/2018/07/Hyat-Read-PDF1.jpg)

Step 2: Copy the Data into an Excel File
----------------------------------------

As usual, the next step is to copy the data to excel.  When you copy the data into excel, you get something like what is illustrated in the screenshot below.  The data are in separate rows with one data item at a time.  At first, you may say this is not too bad.  But when you look further, the data is a real mess. The biggest problem is that the first row column of data is way at the bottom.

![](https://edbodmer.com/wp-content/uploads/2018/07/Hyat-Read-PDF-Import.jpg)

Clean up the Data by Hand
-------------------------

You maybe saying, Bodmer you are Sh…. Can’t you make the VBA code address this.  Well I cannot.  Instead, you can get rid of all of the titles and just make concentrate on the data.  The numbers are what you want in excel anyway.  Towards the bottom, there are some more numbers.  Make sure to include these. The cleaned-up data for the second page of the Jordan Food file is illustrated in the screenshot below.

![](https://edbodmer.com/wp-content/uploads/2018/07/Hyat-Cleaned-By-Hand.jpg)

Running the Read PDF Program for Data in Separate Rows
------------------------------------------------------

After you clean up the data, then use the SHIFT CNTL A to access the macros in the read pdf file.  But this time use the second green button because the data is structured in separate rows with a single piece of data in each row. When you press the green button for this data in single row option, a second menu appears.  This menu allows you to re-arrange the data using different options.  In the case of the second page of the Jordan Food File, there are 31 rows and 8 columns.  The best method is to select the option that allows you to define a fixed number of rows for re-formatting.  Then press the number 31 for the rows that will be put in each column.

![](https://edbodmer.com/wp-content/uploads/2018/07/Hyat-Read-PDF-Single-Column.jpg)

Adjusting Output After Read Pdf
-------------------------------

After pressing the Read PDF buttons, the following format should appear.  This is pretty good news, but the data is transformed and the rows are not in the same columns as the original rows.

![](https://edbodmer.com/wp-content/uploads/2018/07/Hyat-PDF-Result.jpg)

Don’t worry too much about this format.  Just do some manual work and put in the row and column titles that correspond to the data.  These should be in the original raw data sheet as shown in the screenshot below.

![](https://edbodmer.com/wp-content/uploads/2018/07/Hyat-Read-PDF-2.jpg)

After you find the correct titles, then go to the re-formatted sheets and put the column and row titles into the cells. When you are finished copying, the data should look something like below.

![](https://edbodmer.com/wp-content/uploads/2018/07/Hyat-Titles.jpg)

Now we are finally there.  The last step is just to transpose the data.  Now you have a database from the read pdf file.  It was a little painful, but it shouldn’t take all that long.

![](https://edbodmer.com/wp-content/uploads/2018/07/Hyat-Final-Transposed.jpg)

If you are having trouble with some of the steps in this case and you would like to see the data in the various sheets you can download the file below.

**[Excel File with Demonstration of Read PDF Case for Difficult Case Where Data is Not Clean in Excel](https://edbodmer.com/wp-content/uploads/2018/07/Ayat-Read-PDF-1.xlsx)
**

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=4740&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=10376&rand=0.27951762535699864)