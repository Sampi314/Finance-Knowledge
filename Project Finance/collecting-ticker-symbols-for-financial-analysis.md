# Guide for Implementing  the New Financial Database

**Source:** https://edbodmer.com/collecting-ticker-symbols-for-financial-analysis

---

This page explains how you can create a financial database with many years of financial data without paying high fees for Bloomberg or something similar. The database includes financial statements, stock prices and corresponding valuation ratios and multiples. I have been working on an approach to retrieve financial data and then use the data as a basis for financial models or in valuation analysis for many years. Even if you have Bloomberg I hope you will take a look at the file if for no other reason to see just how much you can do with some macros and some structured excel formulas. The file goes to Yahoo Finance and retrieves both market data (stock prices) and accounting data. I have tried to make effective presentations of financial ratios, multiples, cost of capital and other issues central to financial analysis in this file after the data is retrieved from the internet. I have made many changes to this process over the years and the tool described below is something you can adjust for yourself. I have used it in legal proceedings where I testify on the cost of capital. I have adjusted the tool so it can be used to retrieve data for international companies and adjust for exchange rates. An illustration of two of the pages that you can use is shown below.

.

![](https://edbodmer.com/wp-content/uploads/2025/01/image-6.png)

.

.

Restrictions to Finance.yahoo and Marketwatch Data that was Previously Available
--------------------------------------------------------------------------------

Life has began to really suck when you try to get data. In the past you could get financial data from market watch wihout much effort — just using a macro with workbooks.open. This is no longer possible. Similarly, you could get stock price data from finance.yahoo which was wonderful because you could evaluate something called adjusted stock prices that adjusts for dividends. This is also no longer possible. Further, you could hack the FRED database to compare the data with just about any economic data series. This has changed also. After losing access to the data I was seriously depressed. But then I suppose you can use challenges as opportunities. I paid a couple of hundred dollars to access the finance.yahoo data and then revised the database. Now there is more historic data. Now the tickers are consistent (no switching between marketwatch and yahoo). Now the process is more structured and organized as when you re-do something it should improve.

.

Acquiring Data
--------------

If you want to use the database, you have a few options.

1.  Make a list of stocks (about 30) and include the yahoo ticker. Put the list in a spreadsheet as illustrated in the screenshot below. Then attach your spreadsheet to an email sent to edwardbodmer@gmail.com. I will download the data into from yahoo and you can either create the spreadsheet yourself or I can put it together. I am doing this simply because I want people to use the process and get other stuff from me (mostly my ideas about finance).
2.  You purchase the finance.yahoo and you can follow the process below.
3.  I have been collecting a lot of companies from around the world. I have put the raw stock price and financial data in zipped files. If the companies you are interested in are part of the zipped files, you are all set and you can run the program.
4.  I am working on automating the data with Python but I am not finished. When you automate the data gathering, you still have to find the yahoo ticker and the time savings may not be as dramatic as you think.

.

**[Excel File that Reads Financial Data from MarketWatch and Finance.Yahoo that Can be Connected with Analysis Files](https://edbodmer.com/wp-content/uploads/2024/02/Read-Data-23-Feb-2023.xlsb)
**

.

If you have paid for finance.yahoo (as you can see below that I have by the GOLD tab), then you can google finance.yahoo.com and get the company. On the left you need just two things. Frist is the historic data to get the stock prices. The second is the financials which puts multiple years of financial statement data in a reasonably consistent format. For now, you can download the three annual financial statements. These will be consolidated in subsequent steps.

When I have used the database in the past for case studies on valuation or to demonstrate the history of an industry

The second file below inculdes the analyis. You can create this file by moving the sheets from the file above to after the break sheet. This is explained in the step by step process below. This file includes the presentation and analysis of the data.

![](https://edbodmer.com/wp-content/uploads/2025/01/image.png)

.

The screenshot below illustrates putting data in a folder that will be uploaded.

![](https://edbodmer.com/wp-content/uploads/2025/01/image-1.png)

.

The screenshot below shows two folders that contain all of the files.

Update the stock price indicies

![](https://edbodmer.com/wp-content/uploads/2025/01/image-2.png)

.

![](https://edbodmer.com/wp-content/uploads/2025/01/image-5.png)

.

.

![](https://edbodmer.com/wp-content/uploads/2025/01/image-3.png)

.

**[Database and Comprehensive Analysis of Corporations Derived from Uploading Data From Yahoo and Marketwatch](https://edbodmer.com/wp-content/uploads/2024/02/Financial-Analysis-Template-22-December-2024-1.xlsb)
**

.

![](https://edbodmer.com/wp-content/uploads/2025/01/image-4.png)

**[Excel File with Comprehensive Financial Analysis from Reading Stock Price and Financials - Various Companies](https://edbodmer.com/wp-content/uploads/2023/11/Financial-Analysis-Template-19-November-2023-Malaysia-1.xlsb)
**

.

I used to put the read ticker and the analysis into the same sheet. But the analysis sheet uses a lot of INDIRECT functions and it is faster to separate the read data from the analysis. This causes a couple of extra steps, but I think the time saving is work the extra manual steps. You can see below that the read file may take 1/2 an hour. It would take even longer if the process was combined.

.

*   Step 1: Find prior versions of read data and financial analysis (attached to buttons)
*   Step 2: Enter Tickers in the read data file
*   Step 3: Clear data from the read data file
*   Step 4: Run the Read Finanials, Read Stock Prices and Economic Variables (May take 1/2 hour)
*   Step 5: Remove Range Names from the Read Data file
*   Step 6: Copy Menu Page to the Financial Analysis File (Do not copy last ticker sheet name in column M)
*   Step 7: Re-save the Read Data File with only Data — i.e. remove the menu sheet
*   Step 8: Go to the financial analysis sheet and clear the data
*   Step 9: Select all sheets from the Read Data sheet and then copy them to the end of the Financial Analysis Sheet
*   Step 10: Go to the summary graph in the financial analysis sheet.

.

I put a version of the files above. But if you are looking for particular industries you may want to find some other examples where I have put together stock lists. You can find this in the resource library.

If you have requested the financial library (send me an email to www.edwardbodmer@gmail.com), you can look in Chapter 1 and find examples of how to use the file and find examples of analysis with different companies around the world. The files are in Folder H as illustrated below.

.

![](https://edbodmer.com/wp-content/uploads/2023/11/image-12.png)

.

The next sections work through the various steps in more detail and discuss some of the problems.

.

#### **Step 1: Find Yahoo and MarketWatch Tickers**

Finding the correct tickers on Market Watch and Yahoo can be the most time consuming part of the process for companies outside of the US where the company has an ADR (American Deposit Registary) stock price as well as a stock traded on a local exchange. As explained below, the Market Watch financials are expressed in the local currency of the company.  This means that to compare the company to stock prices, the stock prices must also be expressed in the same local currency.

This section explains how to enter the ticker symbols on the menu sheet to create a new financial analysis database.  Finding the appropriate ticker symbols can be the most time consuming part of the process of implementing the Financial Analysis Database. The good news is that Market Watch has become much better in reporting accounting information for companies outside of the U.S. that trade on different exchanges. On this page I demonstrate how to search for the Market Watch and the Yahoo Symbol. I also explain how to add country codes for the Market Watch symbol. If the currency of the financial statements is different from the currency of the stock prices, ratios like the P/E ratio and the Price to Book Ratio will be incorrect in the historic analysis. This page demonstrates how to deal with this issue through reading in exchange rates. As with other pages that describe how to work with the Financial Analysis Database, the objective is to make sure you are completely comfortable with how the database works and how you can modify things by yourself. An updated version of the file that is used to perform the comprehensive analysis is attached to the button below. This example has only two stocks

.

**[Excel File with Comprehensive Financial Analysis from Reading Stock Price and Financials - International Utility Case](https://edbodmer.com/wp-content/uploads/2023/11/Financial-Analysis-Template-19-November-2023-Oll-and-Renewables-1.xlsb)
**

.

**[Instructions for Downloading Files with Macros](https://edbodmer.com/downloading-files-with-macros/)
**

.

#### GBP problem (Shell Example)

Unfortunately, the yahoo database for stock prices uses pence instead of pounds when compiling the data. This means that when you compare stock prices to the book value per share or the earnings per share, you will get ratios that are off by 100. To resolve this you can use the copy and paste special with multiply and multiply the stock price data by .01 — this would be the case for example with Shell and BP. Note that for Shell and for BP, even though the stock price is in USD for the ADR (American Deposit Recipts), the financial statements are in GBP as illustrated below. Further note that you can find the currency in the balance sheet and not the income statement of the markewatch website.

.

![](https://edbodmer.com/wp-content/uploads/2024/02/image.png)

.

The screenshot below illustrates the yahoo stock price for SHELL.L from yahoo.

.

![](https://edbodmer.com/wp-content/uploads/2024/02/image-2.png)

.

I did not bother putting and automatic change in the analysis.

.

#### Acquiring Tickers for U.S. Companies trading on U.S. Exchanges

For the simple example to start with, I have entered three ticker symbols for U.S. companies as shown in the screenshot below.  To get the other tickers, I suggest that you use go to a search engine and then throw the markewatch ticker and the yahoo ticker into the spreadsheet. As with other pages that describe how to work with the Financial Analysis Database, the objective is to make sure you are completely comfortable with how the database works and how you can modify things by yourself.

#### Step 2: Enter the Tickers in the Read Data Sheet

If you want to use and existing set of tickers such as for the Dow 30 stocks, you can also go to the bottom of the sheet where I have put in some examples of companies to use.  To use the selected companies, just copy the ticker symbols in to column D and column F of the menu sheet and then copy the company names into column B. You can also copy the currency adjustment factors into column C which will normally be 1.0 except for UK companies and the pence/pounds problem as well as companies that do not have stocks in local currency on yahoo.

For the selected companies I have included the ticker symbols and potential adjustments for currencies (one of the horrible examples is that Yahoo Finance uses Pence for UK companies while Market Watch uses Pounds. This means when comparing earnings to stock price and other statistics, an adjustment is required.)  Another problem occurs for Japanese companies where Yahoo does not report stock prices in Yen. Note that you should put the extra end of the URL into the main sheet.

.

.

![](https://edbodmer.com/wp-content/uploads/2021/05/image-4.png)

.

#### Note on Re-ordering the data

You can copy the tickers from an earlier version. All data before the red ticker symbol is fixed and you can copy and paste as values. Sometimes you may want to re-order the data. To do this you can use the file attached to the button below where you type in the order of the data in column A.

.

**[Excel file with use of XLOOKUP to adjust the order of companies for reading in the financial data](https://edbodmer.com/wp-content/uploads/2024/02/Re-Order-1.xlsx)
**

.

#### Step 3: Download Data in the Retrieve Data Book by Pressing Buttons on Menu Sheet

Once you have collected the ticker symbols, you can run the three downloading buttons (the third of which is not be necessary unless you are making a CAPM analysis). The screenshot below shows the buttons that you press on the menu sheet.  After you press the buttons, there should be a message at the bottom of the sheet that shows which URL is being scrapped.  This is illustrated in the second screenshot. Do not forget to clear the sheets first.  Reading the financial data may take a long time and it may be a good idea to even re-start your computer or get more RAM.

.

.

![](https://edbodmer.com/wp-content/uploads/2023/09/image-3-2048x1142.png)

.

.

![](https://edbodmer.com/wp-content/uploads/2023/09/image-4-2048x1137.png)

.

The screenshot below illustrates the pages that come up when you are reading the individual companies from MarketWatch.

.

![](https://edbodmer.com/wp-content/uploads/2024/02/image-1.png)

.

Don’t forget to read the stock prices.

.

.

#### Marketwatch Reading Data when New Data is Entered and the Financial Data is Incomplete

Sometimes when you read the maketwatch data, you do not get the full output for multiple years because it seems that marketwatch is entering the data. If this happens, you can wait a few days if this is possible. Alternatively, if you have an older version of the read data, you can replace the individulal sheets. For example, you have read the data for Shell a month ago but this time when you run the read data, you only get partial data. You can go to the individual sheets for Shell Income statement up to the quarterly cash flow and replace the sheets (you may want to move the yahoo sheet so it is the most current).

.

#### Step 4: Use a Template for the Analysis Book and Copy the Ticker Symbols and the Company Names

After reading the data, find a file that includes the full analysis with the graphs and the layout of the financial statements etc. Once you find this data (you can use the button above), then you use this sheet with the companies that you have read in. To do this, first make sure the menu sheet has the same layout as the menu sheet from your file which has all of the ticker symbols and company names. You can just copy and paste special the company database. I have illustrated the menu sheet from the consolidated sheet below. It may be too obvious to write down, but it is a very good idea to copy all of the files with new names and with the dates.

.

![](https://edbodmer.com/wp-content/uploads/2023/11/image-11.png)

.

#### .

#### Step 5: Delete the Ticker and the Break Sheet from the Retrieve Data Book and Select All Sheets

After copying the data, you can delete the sheets and then you can select all of the sheets. One the sheets are selected you can move them to the Analysis Book. I suggest not to save the file at this step.

When copying the data, it works much better if you use the create copy option.

.

![](https://edbodmer.com/wp-content/uploads/2023/11/image-13.png)

.

.

.

![](https://edbodmer.com/wp-content/uploads/2023/11/image-15.png)

.

#### Step 7: Move the Sheets into the Analysis Book and You are Ready to Go

.

Use ALT, E, M to move the sheets and then select the analysis book. You should move all of the sheets to the end — after the Break sheet in the Analysis Workbook.

.

![](https://edbodmer.com/wp-content/uploads/2023/11/image-16.png)

.

### Step 4: Review the Data

The screenshot below shows the results of one of the website scrapes that is put in a separate sheet. Note that the revenues have a B behind the numbers and other numbers have M behind.  Because of this, a function is used to summarise the data.

![](https://edbodmer.com/wp-content/uploads/2018/09/Findata5.jpg)

.

.

Explanation of How to Collect Tickers and Download Data
-------------------------------------------------------

The thing that takes me the most time in structuring the database on historic financial data is simply to find the appropriate ticker symbols.  For companies like those in the Dow 30, you can just google the Dow 30 and get the list of companies.  The ticker symbols for these companies are the same in Yahoo and Market Watch.  So, you can google the name of the company along with yahoo finance.  For companies that are not in the US and primarily trade on other exchanges, the process is a little more complex. Take for example the case of EDF in France.  You can google EDF Market Watch and find the ADR.  When you look at the financials in Market Watch you will see that financial statements are in Euro and not in USD.  This means when you get the stock price from Yahoo, you must also get the data in Euro.  So you must get the ticker symbol from Yahoo that uses Euro for stock prices (rather than the ADR).

The case is illustrated below for a UK company called Interserve.  When you make a google search for the company with Market Watch,  a couple of options appear.  Note in the screenshot below there are different ticker symbols for Interserve. You cannot simply take the first option without checking the Market Watch site to see which of the tickers includes the financial statements.

![](https://edbodmer.com/wp-content/uploads/2018/09/Findata-8.jpg)

The screenshot below shows the Market Watch site using the IRV ticker symbol.  Note that you do not see any financial statements.  The URL in the screenshot shows that the URL is IRV.  But when you look at the page, you can see a menu that includes items for “OVERVIEW” and for “CHARTS.”  But in the menu, there is no “FINANCIALS” option. When you see no financial statements, there will be nothing to download and if you use this IRV ticker in the financial database, there will be no financial statements for the company.

.

![](https://edbodmer.com/wp-content/uploads/2018/09/Findata-7.jpg)

.

In the screenshot below, the ISVJF ticker is used as shown in the URL at the top.  Now the menu on the page includes FINANCIALS after the “OVERVIEW”.  Because the FINANCIALS are included, this ticker ISVJF should work in the file while the ticker in the above file will not work.  Note that because the company is in London, the financials are in Sterling and not in USD.

![](https://edbodmer.com/wp-content/uploads/2018/09/Findata6.jpg)

The financials in GBP are shown in the screenshot below. I have circled the currency of the financials.  As the financials are in GBP, the stock price must be in the same currency as stated above.

![](https://edbodmer.com/wp-content/uploads/2018/09/Findata-11.jpg)

.

One of the main aspects of the financial database is combining stock prices with the financials to compute things like P/E, EV/EBITDA and Price to Book.  Market Watch does not (to my knowledge) have stock prices that can be easily downloaded. This is why I use the Yahoo website.  When you look for the Interserve stock price you find something like the following.  Notice that I have circled the ticker with the .L at the end.

![](https://edbodmer.com/wp-content/uploads/2018/09/Findata-10.jpg)

The screenshot below shows the IRV.L in Yahoo.  Note how the price is in GBP. Note that even though the Yahoo site states that the price is in GBP.  But the price is really in pence.  This means that when you make calculations like Price to Book Ratio, the book value per share is pounds and the stock price is in pence.  This means the ratio must be divided by 100.

![](https://edbodmer.com/wp-content/uploads/2018/09/Findata-12.jpg)

For some companies such as TEPCO in Japan, you can get the financials from Market Watch in Yen.  But for Yahoo, the stock prices are not reported in Yahoo (only in USD).  In this case you can enter an exchange rate to adjust the downloaded stock prices.  A similar problem arises with companies in the UK.  Market Watch reports data in GBP but Yahoo reports data in Pence.  To resolve these issues you can enter a currency adjustment in the menu page of the file.  This currency adjustment is shown in column C of the excerpt below.  These adjustments and the general way ticker symbols are entered into the file are illustrated in the excerpt below.  Note that the Yahoo and Market Watch symbols are the same for companies traded in the U.S. but the ticker symbols are different for companies traded outside the U.S.

![](https://edbodmer.com/wp-content/uploads/2018/04/Multiples-1.jpg)

If you want to see the process of finding ticker symbols along with some discussion of the file, you can watch the video below.  In this video I simply show you how to do a search for the ticker symbols and then enter the ticker symbols into the file to create a new database. The challenging issues are for companies that are primarily traded in markets outside the U.S.

Videos that Demonstrate how to Collect Ticker Symbols in Different Countries and Put Together a Database
--------------------------------------------------------------------------------------------------------

The video below demonstrates how to use the file once the tickers have been entered and the types of information you can get from the file including: (1) comparative reports of P/E, EV/EBITDA, P/B, ROE etc.; (2) a historic layout of data that you can use as the basis of financial models; (3) an interactive report for single companies; and (4) cost of capital analysis.

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=14112&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=10932&rand=0.4227009916395069)