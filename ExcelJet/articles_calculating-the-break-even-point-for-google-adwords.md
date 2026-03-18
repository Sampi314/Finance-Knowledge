# Calculating the break-even point for Google Adwords | Exceljet

**Source:** https://exceljet.net/articles/calculating-the-break-even-point-for-google-adwords

---

[Skip to main content](https://exceljet.net/articles/calculating-the-break-even-point-for-google-adwords#main-content)

[](https://exceljet.net/articles/calculating-the-break-even-point-for-google-adwords#)

*   [Previous](https://exceljet.net/articles/how-to-group-a-pivot-table-by-age-range)
    
*   [Next](https://exceljet.net/articles/how-to-use-mac-function-keys-with-excel)
    

Calculating the break-even point for Google Adwords
===================================================

by Dave Bruns · Updated 14 Mar 2025

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Attachment](https://exceljet.net/file/825/download?token=EHCZ7KwP)
 (50.2 KB)

![Google adwords profitability worksheet](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/adwords_main.png "Google adwords profitability worksheet")

Summary
-------

In this article, we build a model using the seldom-seen Data Table to visualize at what point an Adwords campaign becomes profitable.

_This article describes one way to model Adwords profitability in Excel. If you want to try out the spreadsheet, it's attached below._

The most satisfying and powerful thing you can do with Excel is to model a real-world problem in a way that helps you make a better decision. For a model to be effective, it needs to expose inputs in a way that makes sense, and generate results that are easy to interpret.

In this article, we'll use the seldom-seen Data Table to build a simple model that helps you visualize the profitability of a Google Adwords campaign.

![Adwords worksheet - finished](https://exceljet.net/sites/default/files/images/articles/inline/adwords_main.png "Adwords worksheet - finished")

Just like those word problems from your school days, the key is setting up the problem correctly.

### A quick Adwords primer

Adwords is Google's primary advertising service. For the purpose of this article, we'll be discussing only Pay-per-click (PPC) advertising on Google's search network.

When people search for things on Google, they use certain keywords. For example, they might search for "best todo list manager" or "japanese survival knife". With Adwords, advertisers can bid on specific keywords. If the bid is high enough, the ads are displayed on the search result page, along with the search results. If a user clicks on an ad, the advertiser pays Google the amount of the bid. If a user doesn't click on the ad, the advertiser pays nothing.

### Making money with Adwords

In order to make money by advertising with Adwords, an advertiser must "convert" enough users into customers to pay for the clicks that don't result in a sale, and still make a profit.

For example, if you, the advertiser, have a product that costs $100, and you bid on a keyword that costs $1.00 per click, you need to make a sale at least every 100 clicks just to break even:

100 clicks @ $1.00 = $100 = 1 sale

If you're able to get more than one sale every 100 clicks, you'll make money. If you get less than one sale per 100 clicks, you'll lose money. If you have to pay $2.00 per click, you'll need to make a sale at least every 50 clicks.

As you can see, if you're going to use Adwords PPC to advertise, it's important to understand the break-even point - that is, the conditions under which you'll start to make money.

_Note: To keep this article to the point, I am skipping a lot of potential complexity that could be part of Adwords. For example, you would normally bid on more than one keyword at the same time, the actual cost per click varies due to competition, etc._

### Modeling the problem

Based on the information above, there are 3 key drivers of profit:

(1) the price of the product  
(2) the average cost per click  
(3) the percentage of clicks that can be converted to a sale

We can think of these as inputs (variables) for our problem. Intuitively, we know that a lower cost per click will allow us to buy more clicks per sale, and a higher conversion rate means we'll need to buy fewer clicks to get each sale.

But what's the best way to model the problem in Excel, so that we can see how the cost per click and conversion rate work together to determine profit? As usual, there is more than one way to skin the cat with Excel. However, the modest Data Table turns out to be a pretty good way to visualize the problem.

### Setting things up

First things first, we need to provide an area on the worksheet meant for inputs. I like to group inputs together and label them in one area of the worksheet. For this problem, we'll have:

1.  Average CPC - the average Cost Per Click
2.  Conversion rate - the percentage of clicks that can be converted into a sale
3.  Conversion value - the price of the product, less other costs (i.e. shipping)
4.  Daily budget - this determines how many clicks you can buy each day
5.  Campaign days - the number of days the campaign will run

![Adwords worksheet - inputs](https://exceljet.net/sites/default/files/images/articles/inline/adwords_inputs.png "Adwords worksheet - inputs")

Now, we need to add an Outputs area. This is an area on the worksheet where will run the main calculations with fixed inputs. Specifically, we'll figure out:

1.  Ads clicked per day = daily\_budget / average\_cpc
2.  Ads clicked in campaign = campaign\_days \* clicks\_per\_day
3.  Conversions per day = clicks\_per\_day \* conversion\_rate
4.  Total conversions = campaign\_days \* conversions\_per\_day
5.  Gross profit = total\_conversions \* value\_per\_conversion
6.  Ad costs = clicks\_per\_campaign \* average\_cpc
7.  Net Profit = gross\_profit - total\_ad\_costs

![Adwords worksheet - outputs](https://exceljet.net/sites/default/files/images/articles/inline/adwords_outputs.png "Adwords worksheet - outputs")

With these formulas in place, we can actually figure out the break-even point manually, by fiddling around with the average cost per click and our estimated conversion rate.

But we don't want to do that manually. We want Excel to do the hard work for us!

Enter the Data Table.

### The Data Table

A Data Table is a dynamic table that shows the results of various input cells. Data Tables can handle either 1 or 2 inputs. In our case, a 2-input Data Table is a good fit, since we can cost per click as one input, and conversion rate as the other.

To create the data table:

1.  Add a reference to Net Profit to the upper left cell of the table
2.  Enter Average CPC estimates in the left column of the table
3.  Enter Conversion rate estimates in the top row of the table
4.  Select the entire table area
5.  Choose Data > Data Tools > What-If Analysis > Data Table
6.  In the Data table dialog box, select Conversion Rate for the Row Input
7.  In the Data table dialog box, select Average CPC for the Column Input
8.  Click OK.

![Adwords worksheet - data table input](https://exceljet.net/sites/default/files/images/articles/inline/adwords_datatable.png "Adwords worksheet - data table input")

When you click OK, Excel will fill the table with Net Profit values that correspond to each pair of Average CPC and Conversion rate values. By using a currency number format with negative values displayed in red, you can easily see at a glance which combinations are profitable. Better yet, you can continue to adjust any of the main inputs, and all values plotted in the table will be updated dynamically.

![Adwords worksheet - finished](https://exceljet.net/sites/default/files/images/articles/inline/adwords_main.png "Adwords worksheet - finished")

### Conclusion

Data Tables take a bit of work to set up, and they are limited to 2 inputs only, but they are a nice way to model a problem in a simple visual format.

Is this worksheet helpful to you? Would you approach this problem differently? Let me know in the comments below.

_Credits: This model was inspired by an example in_ [_John Walkenbach's_](http://spreadsheetpage.com/)
 _excellent book,_ [_Excel 2010 Bible_](http://www.amazon.com/Excel-2010-Bible-ebook/dp/B0062O85IW)
_._

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