# Comprehensive Financial Analysis

**Source:** https://edbodmer.com/comprehensive-financial-database

---

This page and the associated pages explain how to create and use a database that scrapes  a whole bunch of financial data from the internet and creates an historic database of Financial Statements, P/E ratios, EV/EBITDA, operating ratios and other multiples for financial statement analysis, valuation, modelling and cost of capital analysis. You can get this kind of stuff from Bloomberg, but you have to pay a lot for a single terminal and you are stuck with black boxes for how to compute things like the cost of equity capital and presentation of the meaning of different financial ratios. The financial statements, ratio analysis and cost of capital analysis that you can create from downloading various information contains a lot of detail and can be used as the basis corporate financial models (comprehensive financial statements are included). All you do is enter some ticker symbols, then wait as the download proceeds, and you will get a database with valuation multiples and financial statements.  The database can be used to generate historic financial statements for a financial models and it will present different multiples such as the P/E, P/B, EV/Invested capital and EV/EBITDA.  I have spent many years on trying to get this database correct and I hope it is in good shape.  But I do continually adjust the database. Then one day, maket watch and finance yahoo did not allow you to download the files like before. This shows how you can make a better database.

First, I begin the discussion on this page by explaining how to use the database.  Later, I discuss some issues about creating the database.

Step 1: Link the companies to evaluate from one of the lists, or make your own list.

.

![](https://edbodmer.com/wp-content/uploads/2024/11/image.png)

.

![](https://edbodmer.com/wp-content/uploads/2024/11/image-1.png)

.

.

**[Excel File with Comprehensive Financial Analysis from Reading Stock Price and Financials - Various Companies](https://edbodmer.com/wp-content/uploads/2023/11/Financial-Analysis-Template-19-November-2023-Malaysia-1.xlsb)
**

.

The files should be in a folder that you have downloaded from yahoo finance.

.

![](https://edbodmer.com/wp-content/uploads/2024/11/image-2.png)

.

![](https://edbodmer.com/wp-content/uploads/2024/11/image-3.png)

.

![](https://edbodmer.com/wp-content/uploads/2024/11/image-4.png)

**[Excel File with Comprehensive Financial Analysis from Reading Stock Price and Financials - International Utility Case](https://edbodmer.com/wp-content/uploads/2023/11/Financial-Analysis-Template-19-November-2023-Oll-and-Renewables-1.xlsb)
**

.

The database is created by download and retrieving data from the internet (Market Watch and Yahoo finance) as well as a couple of data series from FRED for interest rates and for exchange rates.  The real advantage of the process explained on this page is that if you were to go to MarketWatch that has very nice historic data it would take you a very long time to re-type the data by hand.  You would also have to change the B that is in MarketWatch to billions and M to millions and so forth.  Finally, you would not be able to easily compare the financial data to stock prices because MarketWatch has nice financial statement data but no stock prices.  With the data downloading procedure you can present historic multiples for at least five historic years along with financial data like ROIC, ROE, Price to Book and other ratios like the growth rate in revenues and EBITDA. You can also evaluate the cost of capital using the horrible CAPM as well as more interesting methods that use a regression analysis of the market to book ratio and the implied P/E ratio. You can also go to the financial statement page and get a big head start on creating financial models. The databases are flexible meaning that you can pick your ticker symbols, press a button, patiently wait for a while and you get a comprehensive financial database.  Please note that you may have to sometimes update the database when yahoo changes the URL or when I add some enhancements to the file.  You can download the Financial Database with examples and without tickers filled by clicking on the button below.  Please not that when yahoo changes the format of its reports the database must have little revisions.  You can try this yourself or send me an e-mail at edwardbodmer@gmail.com where you find snags.

Please note that I have worked on this database for 20 years since I first discovered how to scrape data into excel. I used the database originally for my cost of capital testimony. My point is that I continually update the file and if you tried toe file a while ago you may have been pissed at me. I promise that it is getting better and much more easy to use. The current version of the file is attached to the top button below.

**[Excel File with Comprehensive Financial Analysis from Reading Stock Price and Financials - International Utility Case](https://edbodmer.com/wp-content/uploads/2023/11/Financial-Analysis-Template-19-November-2023-Oll-and-Renewables-1.xlsb)
**

**[File with Database that can be Updated with Tickers that Produces Historic Multiples, Historic Financials and Other Statistics](https://edbodmer.com/wp-content/uploads/2022/08/Comprehensive-Stock-Analysis-Utility-Companies.xlsm)
**

**[Excel File with Financial Analysis of Airline Companies Demonstrating how to Upload Financial Data from Different Countries](https://edbodmer.com/wp-content/uploads/2021/09/Airline-Companies.xlsb)
**

**[Excel File with Financial Analysis of U.S. Utility Companies for Cost of Capital Analysis with Analyst Growth](https://edbodmer.com/wp-content/uploads/2021/09/Airline-Companies.xlsb)
**

**[Excel File with Financial Analysis of U.S. GE versus Siemens Illustrating Process of Downloading Data](https://edbodmer.com/wp-content/uploads/2021/09/Siemens-and-GE.xlsb)
**

**[Excel File that Uploads Financial Data for Pakistan from Market Watch and Converts to Format for Financial Model](https://edbodmer.com/wp-content/uploads/2021/02/1.-Pakistan-Companies.xlsb)
**

General Description of the Financial Database
---------------------------------------------

You maybe saying to yourself what is the big deal; I can get so much data from the internet anyway (or maybe you pay scads of money to Bloomberg). You can indeed get amazing financial data websites like Market Watch for free including historic financial statements and analyst earnings projections. But key information is missing. Take the case of Market Watch. While historic financials are reported, Market Watch does not allow you to download stock prices so you can compute historic P/E ratios etc. Also Market Watch reports 2.5 billion as 2.5B and you need to adjust for the B,M and even T for trillions. Yahoo Finance has a lot of data also, in particular for stock prices. But the financial statement data is not as detailed and, again, the historic ratios for things ranging from ROIC to forward P/E are not available. Further, after may 2017, yahoo data is a pain to download.

The ability to scrape valuation multiples, cost of capital and historic financial data is, I believe, one of the most important items on my website although few of you seem very interested. As shown below, in one of the pages you can set-up your financial forecast; in another one of the pages you can review a whole bunch of ratios for a company to get a background for valuation and forecasting; in other pages you can create valuation analyses from comparative multiples; in yet other pages you can develop cost of capital analysis that is far better than the traditional CAPM B.S.

Using the Database File for Extracting Financial Statements and Creating Historic Analysis for Financial Models
---------------------------------------------------------------------------------------------------------------

One of the really painful things about creating a corporate model with history is getting the financial data and then arranging it in a consistent format across years.  [I have made other videos explaining how you can use the Read\_PDF.xlsm](https://edbodmer.com/using-read-pdf/)
 file and put data together with the a UDF called the UNION function in cases where you can only get data from financial reports in PDF format.  If you can find tickers and MarketWatch publishes the financials, you can use the financial database. When you create the financial database, the process of acquiring data is much easier and all you have to do is to press the button to download the data. An example of the historic data for modelling analysis is shown in the screenshot below.  [This idea of starting with historic data is absolutely crucial in my opinion and is discussed in the A-Z corporate modelling section.](https://edbodmer.com/acquiring-data-for-corporate-model/)
 If you don’t understand history and use history as a basis for your forecasts, your forecasts are utterly worthless (just like your politics would be). As the amount of detail provided by Market Watch is comprehensive, the financial database file can be used to download data that you can then use to create a financial model.

![](https://edbodmer.com/wp-content/uploads/2022/07/image-7.png)

When I made this analysis I wanted to make a comparison across different companies.  I still believe that this is the most important way to use the file.  But if you want to get started with the file, it may be a good idea to begin with a single company and make sure everything is working. When you do this, you can begin with a company that presents its data in USD.  The screenshot below illustrates how to begin the process.  You go to the sheet named “Menu Sheet” and just put in the ticker for one company.  In the example I have used Macy’s department stores that has a ticker symbol of M.  The other thing that you should make sure is correct is the date of the financial statements.  After you have put in the ticker symbol, you can press the button to read the financial date and read the stock price data.  You should first clear the sheets with the clear sheets button.  The start time and the end time in lines 9 and 10 show how long the reading process takes.

![](https://edbodmer.com/wp-content/uploads/2022/07/image-8.png)

After you press the read button for one company you can watch as the data is read into the file.  Then you will see separate sheets for the data that has been read into the file.  The screenshot below illustrates one of these sheets for the income statement.  There are a whole lot of these sheets for each company and if you include many different companies, there will be very many sheets. Once you have all of the data collected including the stock prices, the rest of the sheets organize data and compute ratios from the data using INDIRECT function along with LOOKUP and MATCH.  In the screenshot below you can see that the data still has M for million and B for billion etc.  The file includes functions to fix this and multiply the numbers to make sure the numbers have a common currency.

![](https://edbodmer.com/wp-content/uploads/2020/04/Raw-Data-from-Mkt-Watch-1.png)

Once you read in the data you can look at some financial ratios.  A good sheet to look at is the is the sheet named “Single Company Graph”. This sheet evaluate various ratios from equity perspective and free cash flow perspective. The first sheet illustrates the EPS and EBITDA.  The top graph is the equity perspective and the bottom sheet is the free cash flow perspective.  I have include a few graphs that illustrate the types of ratios you can use once you have the data loaded.  This analysis of graphs can be more effective if you compare graphs within and industry.  You could also work through the calculations and create your own ratios.

![](https://edbodmer.com/wp-content/uploads/2020/04/Financial-Summary-1-1.png)

![](https://edbodmer.com/wp-content/uploads/2020/04/Financial-Summary-3.png)

![](https://edbodmer.com/wp-content/uploads/2019/06/Historic-for-model-1.jpg)

Let’s say that you are in the middle of a year and second quarter results have been published. If you use the last full historic year when making your forecast, the historic data may be stale.  To rectify this situation you when you go to the page for downloading data, I have put a couple of techniques to use the quarterly data and create a forecast of the current year. As shown in the screenshot below, you can just use the quarterly data to create a year to date numbers (maybe this is ok when you are in the third quarter). Alternatively, you can evaluate the growth rate in quarterly data compared to the same quarters of the prior year and then create a growth rate. Finally, you can use the EPS forecast and the revenue forecast published by MarketWatch and Yahoo and try to derive the remaining expenses and revenues.  These methods are illustrated on the screenshot below.  There are a few different ways to use the quarterly data and some of these are illustrated in the page. The video below the screenshot explains how to find the ticker symbols and create a database that you can then use to create a corporate model.

![](https://edbodmer.com/wp-content/uploads/2019/06/Projected-Full-Year.jpg)

Using the Financial Database File to Compare Financial Performance of Individual Companies
------------------------------------------------------------------------------------------

The excerpt below is an example of how you can look at different companies to try and tell a story.  You can use drop down boxes for selecting different ratios and selecting different companies.  Then you can do things like quickly working through different companies and observe the ROIC, growth in EBITDA, forward P/E ratios etc.

![](https://edbodmer.com/wp-content/uploads/2019/06/Single-Graph-Page.jpg)

Using the Financial Database File to Evaluate Time Series and Comparative Data and the Proposition of Stability.
----------------------------------------------------------------------------------------------------------------

If multiples are used in valuation, they should be stable across time and stable within an industry. One of the main advantages of this database is that you can evaluate this proposition of stability.  Most of the analyses demonstrate that the proposition of stability is false.  You can use the drop down box to compare EV/EBITDA multiples, P/E multiples, P/B multiples and so forth. The first screen shot from the file demonstrates how you can compare ROIC across companies.  If a company has a low ROIC, it may be difficult to increase to the industry average.

![](https://edbodmer.com/wp-content/uploads/2018/04/Multiples-3.jpg)

The second example demonstrates comparison of the P/E ratio across companies.  The first question from looking at a table like this is determining whether you believe the ratios are constant across time and across the sample.  As explained in the corporate finance theory pages, there are very good reasons that P/E ratios should should not be constant across either companies or across time.  In this case, the median P/E ratio is pretty stable.  But don’t be mislead.  The individual companies have wide swings.

![](https://edbodmer.com/wp-content/uploads/2018/04/Multiples-2.jpg)

Using the Database Files for Analysis of Cost of Capital
--------------------------------------------------------

I originally created the database file to analyse cost of capital using price to book ratios and market to book ratios. For years I have been going crazy about finding alternatives to the CAPM that do not depend on the estimated equity market risk premium, the beta or the alternative possible risk free rates.  The screenshots below illustrate a couple examples of how to use the financial database in computing the cost of capital.  The first screenshot is for utility companies in the U.S. where I make a regression equation from the price to book ratio and the forward return on equity.  When you try this, you should understand that the relationship can be affected by changes in expected return and growth rates.  The simple formula for price to book is P/B = (ROE-g)/(k-g).  In solving for k, the formula is k-g = (ROE-g)/(P/B) or k = (ROE – g)/(P/B)+g.  The screenshot below illustrates computation of the cost of capital using the price to book ratio with a regression equation and with the growth rate formula.  In the screenshot you can see how to change the sample of companies to come up with different cost of capital estimates.

![](https://edbodmer.com/wp-content/uploads/2019/06/Price-to-Book.jpg)

The screenshot below illustrates how cost of capital is computed using the value driver formula. The formula for the P/E ratio is P/E = (1-g/ROE)/(k-g).  This formula can be re-arranged as k-g = (1-g/ROE)/P/E or k = (1-g/ROE)/PE + g.  In the analysis below the growth is adjusted and the long-term growth is estimated. The formula is very sensitive to the growth rate. A user defined function is used to compute the cost of capital with different long-term and short-term growth rates.

![](https://edbodmer.com/wp-content/uploads/2019/06/PE-and-Growth.jpg)

Creating a Database: Step by Step Case with A Couple of Companies without Exchange Rate Issues (All Data is in USD)
-------------------------------------------------------------------------------------------------------------------

In this section I describe how to use the financial database in a simple case.  I hope this takes away any intimidation you may have about using the file. If you want to follow along with this you can start from a blank sheet.  Putting a few companies into the file should only take a few minutes.  You can download the Financial Database with examples and without tickers filled by clicking on the button below.

**[File with Database that can be Updated with Tickers that Produces Historic Multiples, Historic Financials and Other Statistics](https://edbodmer.com/wp-content/uploads/2022/08/Comprehensive-Stock-Analysis-Utility-Companies.xlsm)
**

**[File with Structure for Creating Financial Database that Displays Historic P/E, EV/EBITDA etc. as well as Historic Statements](https://edbodmer.com/wp-content/uploads/2018/09/Financial-Download-Blank.xlsm)
**

You can create the financial database that includes historic multiples, cost of capital analysis and historic financial data structured for financial models by entering ticker symbols on the first page of the spreadsheets available for download below. The historic database can also be used for cost of capital analysis and many other analytical tasks.

### Step 1: Clear the Sheets

To work through a case using the financial database from A-Z first clear the data in the sheets. You can do this by pressing the box named “Clear Sheets” on the menu sheet as shown in the screenshot below. When you press this button, all of the sheets after the sheet named “Break Sheet” will be deleted.  (Do not delete the sheet named Break Sheet or the Clear Sheets macro will not operate properly.) Note the #N/A is shown.

![](https://edbodmer.com/wp-content/uploads/2018/09/Findata-1.jpg)

![](https://edbodmer.com/wp-content/uploads/2021/05/image-5.png)

### Step 2: Enter Ticker Symbols in Menu Sheet

After clearing the sheets, enter the ticker symbols on the menu sheet.  Finding the appropriate ticker symbols can be the most time consuming part of the process. This can be a bit painful for companies outside of the US where the company has an ADR stock price as well as a stock price in local currency.  For the simple example to start with, I have entered three ticker symbols for U.S. companies as shown in the screenshot below.  To get the other tickers, I suggest that you use go to a search engine and then throw the markewatch ticker and the yahoo ticker into the spreadsheet.

If you want to use and existing set of tickers such as for the Dow 30 stocks, you can also go to the bottom of the sheet where I have put in some examples of companies to use.  To use the selected companies, just copy the ticker symbols in to column D and column F of the menu sheet and then copy the company names into column B. You can also copy the currency adjustment factors into column C which will normally be 1.0 except for UK companies and the pence/pounds problem as well as companies that do not have stocks in local currency on yahoo.

For the selected companies I have included the ticker symbols and potential adjustments for currencies (one of the horrible examples is that Yahoo Finance uses Pence for UK companies while Market Watch uses Pounds. This means when comparing earnings to stock price and other statistics, an adjustment is required.)  Another problem occurs for Japanese companies where Yahoo does not report stock prices in Yen. Note that you should put the extra end of the URL into the main sheet.

![](https://edbodmer.com/wp-content/uploads/2021/05/image-4.png)

### Step 3: Download Data by Pressing Buttons on Menu Sheet

After you have collected the ticker symbols, you can run the three downloading buttons (the third of which is not be necessary unless you are making a CAPM analysis). The screenshot below shows the buttons that you press on the menu sheet.  After you press the buttons, there should be a message at the bottom of the sheet that shows which URL is being scrapped.  This is illustrated in the second screenshot. Please do not forget to clear the sheets first.  Reading the financial data may take a long time and it may be a good idea to even re-start your computer or get more RAM.

![](https://edbodmer.com/wp-content/uploads/2018/09/Findata3.jpg)

Finding the correct tickers on Market Watch and Yahoo can be the most time consuming part of the process for companies outside of the US where the company has an ADR stock price as well as a stock traded on a local exchange. As explained below, the Market Watch financials are expressed in the local currency of the company.  This means that to compare the company to stock prices, the stock prices must also be expressed in the same local currency.

![](https://edbodmer.com/wp-content/uploads/2021/05/image-6.png)

![](https://edbodmer.com/wp-content/uploads/2021/05/image-7.png)

Downloading Comprehensive Financial Data for Different Industries and Selected Groups of Companies
--------------------------------------------------------------------------------------------------

You can create your own files for different industries by entering ticker symbols in the menu page of the files that are available for download below.  This ticker symbol business can be a bit tricky if the companies report financial statements in different currencies than the USD.   I have included a few examples of how you can download files below for various industries that are attached to the buttons below so you can see how the programs work before you try things yourself. After you look through the stuff that is produced, you can to press the buttons to download and arrange the data.   The file for insurance companies is different from the other files because of financial reporting.  For insurance and financial companies, financial statements are reported in a different format from industrial companies.  The file to download named insurance companies includes an example of how the process can work when there are different financial statements.    . Please note: When you open the files, run the macro titled “RECALCULATE ALL” (find the button on the second page). .

Videos that Demonstrate how to Collect Ticker Symbols in Different Countries and Put Together a Database
--------------------------------------------------------------------------------------------------------

The video below demonstrates how to use the file once the tickers have been entered and the types of information you can get from the file including: (1) comparative reports of P/E, EV/EBITDA, P/B, ROE etc.; (2) a historic layout of data that you can use as the basis of financial models; (3) an interactive report for single companies; and (4) cost of capital analysis.

Technical Discussion of the Financial Database File
---------------------------------------------------

Macros are used in the files that allow you to enter ticker symbols and then get a whole lot of data. The process adjusts URLs market watch and yahoo.com according to ticker symbols and then puts financial data into a lot of sheets. The INDIRECT function is then used to gather data together and summarize data in different ways. You can update the data like with other files although depending on your internet speed it may take a bit longer to read all of the stuff when you update your analysis. It has taken a lot of iterations to develop this file and I will probably change it in the future.  I had thought you may be interested in the method for reading the data into the file and then arranging the data for comparison.  I am told by young people that this is not interesting.  People seem to want to press a button and just be finished.  Apparently you do not want to look at any VBA code or other techniques.

Despite what I have been told, I have made various videos that describe technical details of how to develop the databases.  I have also put a set of power point slides together that documents technical details of developing the file.

**[Power Point Slides that Describe Technical Details of the Financial Databases](https://edbodmer.com/wp-content/uploads/2018/04/A-Z-Reading-Financial-Ratios.pptx)
**

![](https://edbodmer.com/wp-content/uploads/2021/07/image-13.png)

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=1396&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=10104&rand=0.03765117221067715)