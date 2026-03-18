# Adding Ratios to Financial Analysis Page

**Source:** https://edbodmer.com/adjusting-summary-financial-analysis-page

---

This page explains how to interpret, adjust and change the summary financial analysis page of the financial database. This page includes summary statistics including returns, market values, valuation ratios, credit ratios, forecast earnings and other data. After reading in the data I often go to this page to make sure the financial ratios have been correctly established. If you are reading in data for one industry you can also scan ratios such as the price to book ratio, the return on equity, EBITDA trends and other items across different companies. I have put three graphs wtih dropdown boxes in the summary page so you can hopefully evaluate different ratios and tell a story about the company. The financial ratios and other summary information is in the sheet named “Single Company Graph”. This webpage illustrates how the Single Company Graph can be used in financial analysis and it also explains how you can modify the sheet to do things like add more financial ratios and also how you can trace the analysis to make sure the numbers are correct.

The Single Company Graph includes three different graphs. The top graph is primarily used for equity analysis with data like ROE, P/E, Net Income and the Price to Book ratio. The graph is primarily from the free cash flow perspective.  I have include a few graphs that illustrate the types of ratios you can use once you have the data loaded.  This analysis of graphs can be more effective if you compare graphs within and industry.  You could also work through the calculations and create your own ratios. The third graph shows how to evaluate quarterly data as well as annual data. The quarterly graph has annual numbers divided by four for the first periods and then quarterly data taken from the quarterly statements. There are a few different ways to use the quarterly data and some of these are illustrated in the page.

The idea is that you can push the spinner box up and down to find the same ratio for different companies. The second concept is that you can quickly look at different comparisons to get a story about what is happening with the company. The forecasts allow you to quickly evaluate the forecast relative to the history.

![](https://edbodmer.com/wp-content/uploads/2021/07/image-15.png)

Note that when you are looking at data that does not have forecasts, many of the items will be FALSE or zero. The screenshot below illustrates the Single Company page for Air Asia and the effect of the pandemic on financial data.

![](https://edbodmer.com/wp-content/uploads/2021/07/image-16.png)

Tracing the Location of the Item that is Graphed
------------------------------------------------

You may want to drill down and find how the source of the data that is used in the anlysis. You also may want to add other data to graphs or other analysis. This page demonstrates how to make adjustments and understand calculation of the data.

1.  The ultimate source of data is the individual sheets for financial statements and for stock prices. This data is in turn put into the income statement extract and the balance statement extract sheets. You can add variables extracted by using the title of items in the income statement or balance sheet (including quarterly statemets). This is accomplished by using the INDIRECT function and the MATCH statement. The INDIRECT function requires a careful definition of the sheet name. The MATCH function requires the name of the item you are extracting (for example interest expense) to be exactly the same as the item in the individual statements. The sheet below is an example of how to look for the source data.

![](https://edbodmer.com/wp-content/uploads/2021/10/image.png)

With the name Interest Expense found, you can go to the Income Statement Extract sheet and collect the quarterly data. The screenshot below illustrates how to adjust the MATCH function to find the item. Note that the result of the MATCH is the row number of the Interest Expense in the screenshot above.

![](https://edbodmer.com/wp-content/uploads/2021/10/image-3.png)

The data is extracted from a very long CHOOSE Function that is implemented either in the Equity Trend Analysis, the EBITDA Trend Analysis or the Quarterly Analysis. The CHOOSE function is used because the companies and the different items must be selected. The CHOOSE function is computed on the This makes a simple INDEX function difficult to use. The CHOOSE function is way too long and I hate that I did not do this in a more elegant manner. But if you want to find the items you can go to the page named “Equity Trend Analysis” for the first graph and “EBITDA Trend Analysis” for the second graph. The list in the “Equity Trend Analysis” shown in the screenshot below demonstrates how the long CHOOSE function can be adjusted. The cell reference column demonstrates how you can go to the relevant sheet and then further trace the data.

![](https://edbodmer.com/wp-content/uploads/2021/07/image-14.png)

Once you go to the relevant cell reference you can then see where the data comes from.

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=14092&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=11504&rand=0.46127250267525266)