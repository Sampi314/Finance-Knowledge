# Valuation Ratios and Projected Earnings

**Source:** https://edbodmer.com/valuation-ratios-and-projected-earnings

---

In this page I demonstrate how you can modify and evaluate earnings growth projections that are published by Market Watch and Yahoo Finance. I show how to put together projections of earnings and statistics on current valuation ratios so you can evaluate cost of capital with expected numbers. I also demonstrate how you can work with the file and change the data that you want to extract. As with other pages that describe how to work with the Financial Analysis Database, the objective is to make sure you are completely comfortable with how the database works and how you can modify things by yourself.

Study of Nestle in Different Countries
--------------------------------------

You cannot find the stock prices on yahoo finance even though you can get some other statistics. You can find the stock prices on investing.com

.

![](https://edbodmer.com/wp-content/uploads/2022/07/image-5.png)

.

Transferring Data to the Current Sheet from Market Watch and Yahoo Sheets
-------------------------------------------------------------------------

When you read in the data, the program is set-up to read in data from various different sheets that tabulate the summary statistics and growth projections. Each of the sheets is just one of the pages on Market Watch or Yahoo. The technique I have created to gather data from the different places is illustrated in the screenshot below. In the top lines you you put the page that the data comes from. Then you put in the column for the match test. After that you put the column of the data. The name in column 9 is for the the Match analysis.

![](https://edbodmer.com/wp-content/uploads/2021/07/image-17.png)

Don’t Worry if Marketwatch or Yahoo Formats Change
--------------------------------------------------

From time to time the format of the Yahoo finance sheet changes or the format of the MarketWatch growth page changes. This used to get me very nervous. But don’t worry about this. You can go to the page and then modify the extraction from the source data. Note that in the screenshot above I have temporarily put the Market Watch and Yahoo sheets for one company (AAPL). Then you can go to the source page and check if the names have changed; if a new statistic has been included; if the column has changed etc. You can change the column and the row numbers using the MATCH and the INDEX. This is illustrated in the screenshot below. Note that to find the data I split the screens using the Windows add new window and then arrange all.

![](https://edbodmer.com/wp-content/uploads/2020/10/image-62-2048x844.png)

Once you have split the screen, you can then modify the MATCH and the INDEX with the INDIRECT function. I have set-up the sheet name until the ! as shown above. Then you can try to find the row number in the detail as in the above screenshot which is the Market Watch summary. This is illustrated in the screenshot below. Note that the data is summarized in the sheet named “Data Current.”

Illustration of How to Extract Additional Data
----------------------------------------------

When you download the yahoo finance information, the data is put into a sheet that looks something like the screenshot below. In this example, I would like to extract the data for the forward dividend per share on an annual basis. You can see that this in the screenshot below. Note that the forward dividend yield has a footnote of 4. Don’t worry about this. Even if it changes in the future you can adjust the current sheet of the file. The title of the item is in column A and the value is in column B.

![](https://edbodmer.com/wp-content/uploads/2021/07/image-18.png)

Once you have decided on the item you want to extract, you copy and paste the title to a column in the “Data Current” sheet. This is illustrated in the screenshot below. After copying the title, put in the name Yahoo Sum (this is not necessary for the calculation) and then put in the fact that the item will come from column B and the test will be from column A as shown in the column BS of the example. Finally you can copy the formula from one of the formulas that uses the Yahoo Summary page.

![](https://edbodmer.com/wp-content/uploads/2021/07/image-19.png)

The final result of extracting the data is shown in the next screenshot. You can see that all of the dividend data is included. The Market Watch Basic is shown in BQ. This data has been extracted using a similar approach, but the Key Data name is used to begin finding the data and then you count down to the lines below to evaluate which data item to extract. You can see that Market Watch uses quarterly dividends.

![](https://edbodmer.com/wp-content/uploads/2021/07/image-20.png)

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=14126&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=10800&rand=0.4609893408358655)