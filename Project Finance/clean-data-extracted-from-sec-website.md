# Retrieve Data for Historic Analysis (SEC Method)

**Source:** https://edbodmer.com/clean-data-extracted-from-sec-website

---

This web page demonstrates how to efficiently retrieve data for your financial models.  If you want 5 years of data including 5 quarters of quarterly data, On you can go to the pages that explain how to download data and you can get the data into excel from market watch (there are a log of little tools to get rid of the adds, find the data, compute financial ratios etc. [The link to his page is attached to this sentence.](https://edbodmer.com/using-financial-database-for-historical-financial-statement/)
 On this page I focus on how to automate acquiring data from the Securities and Exchange Commission (SEC) when you want to retrieve more years of data.  The SEC has data back to the mid 1990’s in various forms and you can find good data. The technique on this page explains how to efficiently gather data and then put it together. I put this page here in part because I forget how to do this myself and I need to document things in order to remember them. I describe how to create a macro to read in the data and then clean up the data using other VBA programs and how the use the Union function. Other pages demonstrate how to use the Read pdf file to extract data into annual reports and how to read financial statement data from Market Watch into an excel file.  The Securities and Exchange Commission in the U.S. publishes a lot of data that can be used in corporate finance and modelling.  This data includes financial statements (10K for annual and 10Q for quarterly), acquisitions, new securities issues and investor analyst presentations.  I have made a file that automatically reads the interactive data published on the SEC website and then compile the data into a set of usable data.  Making the data usable includes a macro described below along with the UNION function. The SEC clean up file allows you to copy the data into an excel file and then it cleans up the data. The SEC clean up data file works with a macro that is somewhat like the read pdf to excel function.  To operate the clean up SEC system, you can download the file that includes the macros below. The file must be opened  after you copy data from the SEC website.  Once the file is opened, follow the instructions in the file.  At the bottom of this webpage I introduce a method to use the interactive data to make an automatic download.  The file below has the macro that you can use to clean up the data.

**[Excel File with Macros that Allow you to Quickly Format HTML Files from the SEC Website into Excel](https://edbodmer.com/wp-content/uploads/2020/04/Format-SEC.xlsm)
**

.

.

If you send me an email — edwardbodmer@gmail.com – then I will send you a bunch of resources. One of the pages shown on the screenshot below has files that are associated with reading data from the SEC website.

![](https://edbodmer.com/wp-content/uploads/2023/02/image-12.png)

.

.

The GE; the Amazon and the Apple examples are attached to the buttons below.

.

**[Excel File for Reading Data from the SEC website for GE. with Macros that Allow you Download the Files and Put them Together](https://edbodmer.com/wp-content/uploads/2023/02/SEC-Read-GE.xlsm)
**

.

**[Excel File for Reading Data from the SEC website for Amazon.with Macros that Allow you Download the Files](https://edbodmer.com/wp-content/uploads/2023/02/SEC-Read-Amazon.xlsm)
**

.

**[Excel File for Reading Data from the SEC website for Apple with Macros that Allow you Download the Files](https://edbodmer.com/wp-content/uploads/2023/02/SEC-Read-Apple.xlsm)
**

.

.

Automatic Read with Interactive Data
------------------------------------

Since 2009, you can download financial statement data directly into an excel sheet using the SEC website.  This is fantastic except that it is clumsy to manually download data, then put the data together from different years and then re-formatting the data.  I will work through how to create VBA code to make the process work much more quickly.  The first step to making the process more automatic is to create a macro that reads the data and puts the files into a defined folder. To see how this works, go to a page like this and right click on the red text that says “View Excel Document”.    When you right on the text named to “View Excel Document” which will find the appropriate URL.  After that copy the address and you will see a URL like the one below.  The link below is for Amazon with a code of 1018724.

### Step 1: Go to SEC Website and Find the company

https://www.sec.gov/Archives/edgar/data/1018724/000101872419000004/Financial\_Report.xlsx

### First, Go to SEC Website and Get the URL’s

You can put in the company name and then use 10-K if you want a bunch of historic data. The next two screenshots illustrate this. You should right click on the “view excel document” and then paste the URL’s into excel

**Illustration of finding the data and searching on 10-K**

![](https://edbodmer.com/wp-content/uploads/2022/08/image-5.png)

![](https://edbodmer.com/wp-content/uploads/2020/04/SEC-from-Interactive.png)

### Copy the URL into the Spreadsheet

It is a little bit painful but put in the URL’s. Maybe you can find a pattern and automate this.

![](https://edbodmer.com/wp-content/uploads/2022/08/image-6.png)

### Find the Files that you create in a directory

![](https://edbodmer.com/wp-content/uploads/2022/08/image-2.png)

![](https://edbodmer.com/wp-content/uploads/2022/08/image-11.png)

### Run the Initialise Button

Open the files. You can open them one by one or open them one at a time or in bulk.

Step on the Income statement or other statements. When you step on the income statement press SHIFT, CNTL, I

When you run the initialise button, it will create short-cuts for Shift-CNTL,I etc. Then you can put the sheets together.

![](https://edbodmer.com/wp-content/uploads/2022/08/image-12.png)

For the first, make sure that column A is filled. Delete extra rows like the footnotes above. In the case of GE there are multiple companies and you probably want to delete the companies below the top.

.

.

It is easy to put this link into workbooks open.  But the number at the end is not the same.  So instead you can use an error checking routine.  Different URLS’s for Amazon for different years are shown in the screenshot below.  Note that the final numbers are not all the same.

![](https://edbodmer.com/wp-content/uploads/2020/04/URLs-for-Different-Years.png)

Once you read in the URL’s, you can put the files together into different sheets.  I have created a macro that works through data once you have the company code number used by the SEC.  The screenshot below illustrates how you can filter through different files published by the SEC and save the files. The files are saved into an area you define.  Once you have the excel files defined, you can put the income statement, the cash flow statement and the balance sheet together.  I have made macros with short cuts (SHIFT, CNTL, I) for the income statement (SHIFT, CNTL, C) for the cash flow statement and (SHIFT, CNTL, B) for the balance sheet.  This allows you to quickly open the financial statement files and then put them together.

Using the Union Function to Put Together Financial Statements
-------------------------------------------------------------

I have tried to make a very painful process as easy as possible.  I have not been able to make it fully automatic, but I hope you can get a file together if minutes rather than days. Like many functions, the UNION function is an array function.  This means the output does not go into one cell but rather into a series of cells.  To operate the UNION function you should leave a long space and then select the long space.  After that, you begin typing the UNION function.  Then like with any function press the tab key.  After that, you can select multiple other columns (or rows) that will be combined into one single column,  At the end press the SHIFT, CNTL, ENTER sequence.

Here is a step by step review of the union function:

### Step 1: Insert some columns at the left of the sheet

### Step 2: Use the Union Function which is an array function (SHIFT, CNTL, ENTER).

Don’t forget to make enough space for a long list of columns.  The argument for the UNION function is the different titles for the stuff the you read in.  The use of the UNION function is illustrated in the screenshot below.

### ![](https://edbodmer.com/wp-content/uploads/2020/05/SEC-Union-Function.png)

![](https://edbodmer.com/wp-content/uploads/2020/05/SEC-Union-Finished-Before-Re-strucutre.png)

### Step 3 Clean up the Union Function Output.

The union function does not always put things in a nice order.  So you can copy and paste special as values, the titles and then move then around.  The screenshot below illustrates the union function output before it has been cleaned up.  Note that there are two titles for income.  You can put these titles together and clean up the top stuff.  The second screenshot shows the cleaned up version.  Also get rid of the zeros at the end.

![](https://edbodmer.com/wp-content/uploads/2020/05/SEC-Reformatted-after-Union.png)

### Step 4: Use the IDMAT (Index and match) to put together year by year date

You apply the INDMAT function, from the adjusted UNION function list.  You compare the master list with the year by year lists and then collect the data.  The INDMAT is illustrated in the screenshot below. When you use the INDMAT, use the entire row for the title of the individual year and use the entire rpw of data.  As you proceed with more columns you can group (temporary hide) columns that you have finished with using SHIFT, ALT, –>.  The finished result after the INDMAT is illustrated in the second screenshot below.

Step 5: Clean Up the Data with Multiple Rows
--------------------------------------------

Once you have finished with the INDMAT, it will look a bit messy as shown in the screenshot below.  But you can insert some columns (to save the original stuff for future years).  Then you can copy and paste the information to the blank columns (or even a blank sheet).  The final column will finally look clean and you have a lot of valuable history.  The result is shown in the second screenshot.

![](https://edbodmer.com/wp-content/uploads/2020/05/SEC-After-INDMAT-Before-Restructure.png)

![](https://edbodmer.com/wp-content/uploads/2020/05/SEC-Reformatting-IS.png)

![](https://edbodmer.com/wp-content/uploads/2020/05/SEC-Finished-Format.png)

The video below is lengthy and bad but it goes through this.

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=2858&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=11388&rand=0.19545425483912082)