# How to Calculate Correlation Coefficient in Excel (2 Easy Ways)

**Source:** https://trumpexcel.com/correlation-coefficient-excel

---

[Skip to content](https://trumpexcel.com/correlation-coefficient-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/correlation-coefficient-excel/#below-title)

Excel is a powerful tool that has some amazing functions and functionalities when working with statistics.

Finding a correlation between two data series is one of the most common statistical calculation when working with large datasets,

I was working as a financial analyst a few years ago, and although we were not heavily involved in statistical data, finding correlation was something we still had to do quite often.

In this tutorial, I will show you two really easy ways to **calculate correlation coefficient in Excel**. There is already a built-in function to do this, and you can also use the Data Analysis Toolpak.

So let’s get started!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/correlation-coefficient-excel/#)

What is the Correlation Coefficient?
------------------------------------

Since this is not a statistics class, let me briefly explain what is the correlation coefficient, and then we’ll move on to the section where we calculate the correlation coefficient in Excel.

A correlation coefficient is a value that tells you how closely two data series are related.

A commonly used example is the weight and height of 10 people in a group. If we calculate the correlation coefficient for the height and weight data for these people, we will get a value between -1 and 1.

A value less than zero indicates a negative correlation, which means that if the height increases then the weight decreases, or if the weight increases at then the height decrease.

And a value more than zero indicates a positive correlation, which means that if the height increases then the weight increases, and if the height decreases then the weight decreases.

The closer the value is to 1, the stronger is the positive correlation. So a value of .8 would indicate that the height and weight data are strongly correlated.

Note: There are different types of correlation coefficients and statistics, but in this tutorial, we’ll be looking at the most common one which is the Pearson correlation coefficient

Now, let’s see how to calculate this correlation coefficient in Excel.

Also read: [Weighted Average Formula in Excel](https://trumpexcel.com/weighted-average-in-excel/)

Calculating Correlation Coefficient in Excel
--------------------------------------------

As I mentioned, there are a couple of ways you can calculate the correlation coefficient in Excel.

### Using CORREL Formula

CORREL is a statistics function that was introduced in Excel 2007.

Suppose you have a data set as shown below where you want to calculate the correlation coefficient between the height and the weight of 10 people.

![Dataset for Correlation formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20364%20310'%3E%3C/svg%3E)

Below is the formula that would do this:

\=CORREL(B2:B12,C2:C12)

![Correlation formula in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20540%20422'%3E%3C/svg%3E)

The above CORREL function takes two arguments – the series with the height data points and the series with the weight data points.

And that’s it!

As soon as you hit enter, Excel does all the calculations in the back-end it gives you one single Pearson correlation coefficient number.

In our example, that value is a little over .5, which indicates that there is a fairly strong positive correlation.

This method is best used if you have two series and all you want is the correlation coefficient.

But if you have multiple series and you want to find out the correlation coefficient of all these series, then you can also consider using the data analysis tool pack in Excel (covered next)

### Using the Data Analysis Toolpak

Excel has a Data Analysis Toolpak that can be used to quickly calculate various statistics values (including getting the correlation coefficient).

But the Data Analysis Toolpak is disabled by default in Excel. So the first step would be to enable the data analysis tool back and then use that to calculate the Pearson correlation coefficient in Excel.

#### Enabling the Data Analysis Toolpak

Below are the steps to enable the Data Analysis Toolpak in Excel:

1.  Click the File tab![Click the File tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20543%20203'%3E%3C/svg%3E)
2.  Click on Options![Click on Options](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20400%20780'%3E%3C/svg%3E)
3.  In the Excel Options dialog box that opens up, click on the Add-ins option in the sidebar pane![Click on Addin](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20492'%3E%3C/svg%3E)
4.  In the Manage drop-down, select Excel add-ins![Select Excel Add-ins](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20313'%3E%3C/svg%3E)
5.  Click on Go. This will open the add-ins dialog box
6.  Check the Analysis Toolpak option![Check Analysis Toolpak](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20407%20495'%3E%3C/svg%3E)
7.  Click on Ok

The above steps would add a new group in the Data tab in the Excel ribbon called Analysis. Within this group, you would have the Data Analysis option

![Data analysis option in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20752%20127'%3E%3C/svg%3E)

#### Calculating the Correlation Coefficient Using Data Analysis Toolpak

Now that you have the analysis tool back available in the ribbon, let’s see how to calculate the correlation coefficient using it.

Suppose you have a data set as shown below and you want to find out the correlation between the three series (height and weight, height and income, and weight and income)

![Data for correlation using Data analysis toolpak](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20444%20311'%3E%3C/svg%3E)

Below are the steps to do this:

1.  Click the Data tab![Click the Data tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20691%20201'%3E%3C/svg%3E)
2.  In the Analysis group, click on the Data Analysis option![Click on Data Analysis icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20535%20201'%3E%3C/svg%3E)
3.  In the Data Analysis dialog box that opens up, click on ‘Correlation’![Select Correlation in Data Analysos toolpak dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20583%20254'%3E%3C/svg%3E)
4.  Click OK. This will open the Correlation dialog box
5.  For input range, select the three series – including the headers![Select the input range](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20592%20309'%3E%3C/svg%3E)
6.  For ‘Grouped by’, make sure ‘Columns’ is selected![Select Grouped by as columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20592%20309'%3E%3C/svg%3E)
7.  Select the option – ‘Label in First Row’. This will make sure that in the resulting data would have the same headers and it would be a lot easier to understand the results![Check Labels in first row](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20592%20309'%3E%3C/svg%3E)
8.  In the Output options, choose where you want the resulting table. I’m going to go with cell G1 on the same worksheet. You can also choose to get your results in a new worksheet or a new workbook![Enter the output result destination](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20592%20309'%3E%3C/svg%3E)
9.  Click OK

As soon as you do this, Excel would calculate the correlation coefficient for all the series and give you a table as shown below:

![Output showing correlation of all series](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20750%20252'%3E%3C/svg%3E)

Note that the resulting table is static, and would not update in case any of the data points in your table change. In case of any change, you will have to repeat the above steps again to generate a new table of correlation coefficients.

So these are two quick and easy methods to calculate correlation coefficient in Excel.

I hope you found this tutorial useful!

**Other Excel tutorials you may also like:**

*   [How to Calculate Standard Deviation In Excel (Step-by-Step)](https://trumpexcel.com/standard-deviation/)
    
*   [How to Find Outliers in Excel (and how to handle these)](https://trumpexcel.com/find-outliers-excel/)
    
*   [Calculating Moving Average in Excel \[Simple, Weighted, & Exponential\]](https://trumpexcel.com/moving-average-excel/)
    
*   [How to Calculate Compound Annual Growth Rate (CAGR) in Excel](https://trumpexcel.com/calculate-cagr-excel/)
    
*   [One Variable Data Table in Excel](https://trumpexcel.com/one-variable-data-table-in-excel/)
    
*   [Two Variable Data Table in Excel](https://trumpexcel.com/two-variable-data-table-in-excel/)
    
*   [Scenario Manager in Excel](https://trumpexcel.com/scenario-manager-in-excel/)
    
*   [Using Solver in Excel](https://trumpexcel.com/solver-in-excel/)
    
*   [Calculate P-value in Excel](https://trumpexcel.com/p-value-excel/)
    
*   [How to Get Descriptive Statistics in Excel?](https://trumpexcel.com/descriptive-statistics-excel/)
    
*   [Calculate the Coefficient of Variation (CV) in Excel](https://trumpexcel.com/calculate-coefficient-of-variation-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/correlation-coefficient-excel/#respond)

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