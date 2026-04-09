# How to Group Dates in Pivot Tables in Excel (by Years, Months, Weeks)

**Source:** https://trumpexcel.com/group-dates-in-pivot-tables-excel

---

[Skip to content](https://trumpexcel.com/group-dates-in-pivot-tables-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/group-dates-in-pivot-tables-excel/#below-title)

The ability to quickly group dates in Pivot Tables in Excel can be quite useful.

It helps you analyze data by getting different views by dates, weeks, months, quarters, and years.

For example, if you have credit card data, you may want to group it in different ways (such as grouping by months or quarters or years).

Similarly, if you have a call center data, then you may want to group it by minutes or hours.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/group-dates-in-pivot-tables-excel/#)

**Watch Video – Grouping Dates in Pivot Tables (Grouping by Months/Years)**

How to Group Dates in Pivot Tables in Excel
-------------------------------------------

Suppose you have a dataset as shown below:

![Group Dates in Pivot Tables in Excel - DataSet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20339%20375'%3E%3C/svg%3E)

It has sales data by Date, Stores, and Regions (East, West, North, and South). The data spans across 300+ rows and 4 columns.

Here is a simple pivot table summary created using this data:

![Group Dates in Pivot Tables in Excel - Pivot](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20241%20314'%3E%3C/svg%3E)

This pivot table summarizes sales data by date, but it isn’t quite helpful as it shows all the 300+ dates. In such as case, it would be better to have the dates grouped by years, quarters, and/or months

**[Download Data and follow along](https://trumpexcel.com/wp-content/uploads/2015/11/Group-Dates-in-Pivot-Table.xlsx)
**.

### Grouping by Years in a Pivot Table

The dataset shown above have dates for two years (2014 and 2015).

Here are the steps to group these dates by years:

*   Select any cell in the Date column in the Pivot Table.
*   Go to Pivot Table Tools –> Analyze –> Group –> Group Selection.![Group Dates in Pivot Tables in Excel - Group Selection](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20128'%3E%3C/svg%3E)
*   In the Grouping dialogue box, select Years.
    *   While grouping dates, you can select more than one options. By default, Months option is already selected. You can select additional option along with Month. To deselect Month, simply click on it.
    *   It picks the ‘Starting at’ date and ‘Ending at’ date based on the source data. If you want, you can change these.![Group Dates in Pivot Tables in Excel - Grouping Dialogue Box Years](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20242%20310'%3E%3C/svg%3E)
*   Click OK

This would summarize the pivot table by years.

![Group Dates in Pivot Tables in Excel - Pivot by years](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20252%20133'%3E%3C/svg%3E)

This summarization by years may be useful when you have more number of years. In this case, it would be better to have the quarterly or monthly data.

### Grouping by Quarters in a Pivot Table

In the above dataset, it makes more sense to drill down to quarters or months to have a better understanding of the sales.

Here is how you can group these by quarters:

*   Select any cell in the Date column in the Pivot Table.
*   Go to Pivot Table Tools –> Analyze –> Group –> Group Selection.![Group Dates in Pivot Tables in Excel - Group Selection](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20128'%3E%3C/svg%3E)
*   In the Grouping dialogue box, select Quarters and deselect any other selected option(s).![Group Dates in Pivot Tables in Excel - group by quarters](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20242%20306'%3E%3C/svg%3E)
*   Click OK.

This would summarize the pivot table by quarters.

![Group Dates in Pivot Tables in Excel - Grouping Dialogue Box quarters](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20250%20167'%3E%3C/svg%3E)

The issue with this pivot table is that it combines the Quarterly sales value for 2014 as well as 2015. Hence, for each quarter, the sales value is the sum of sales values in Quarter 1 in 2014 and 2015.

In a real life scenario, you are most likely to analyze these [quarters](https://trumpexcel.com/calculate-quarter-from-date-excel/)
 for each year separately. To do this:

*   Select any cell in the Date column in the Pivot Table.
*   Go to Pivot Table Tools –> Analyze –> Group –> Group Selection.![Group Dates in Pivot Tables in Excel - Group Selection](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20128'%3E%3C/svg%3E)
*   In the Grouping dialogue box, select Quarters as well as Years. You can select more than one option by simply clicking on it.![Group Dates in Pivot Tables in Excel - Month and Year](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20241%20309'%3E%3C/svg%3E)
*   Click OK.

This would summarize the data by Years and then within years by Quarters. Something as shown below:

![Group Dates in Pivot Tables in Excel - Quarter and Year Summary](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20306%20234'%3E%3C/svg%3E)

_Note: I am using the tabular form layout in the above snapshot._

When you group dates by more than one time-frame group, something interesting happens. If you look at the field list, you will notice a new field has automatically been added. In this case, it is Years.

Note that this new field that has appeared is not a part of the data source. This field has been created in the [Pivot Cache](https://trumpexcel.com/pivot-cache-excel/)
 to quickly group and summarizes data. When you ungroup the data, this field will vanish.

The benefit of having this new field is that now you can analyze the data with quarters in rows and years in columns, as shown below:

![Group Dates in Pivot Tables in Excel - Year in column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20413%20167'%3E%3C/svg%3E)

All you need to do is drop the Year field from Row area to Columns area.

![Group Dates in Pivot Tables in Excel - Drag Year](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20260%20476'%3E%3C/svg%3E)

### Grouping by Months in a Pivot Table

Similar to the way we grouped the data by quarters, we can also do this by months.

Again, it is advisable to use both Year and Month to group the data instead of only using months (unless you only have data for one or less than a year).

Here are the steps to do this:

*   Select any cell in the Date column in the Pivot Table.
*   Go to Pivot Table Tools –> Analyze –> Group –> Group Selection.
*   In the Grouping dialogue box, select Months as well as Years. You can select more than one option by simply clicking on it.![Grouping by Months in Excel Pivot Table - Select of Months and Years](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20244%20308'%3E%3C/svg%3E)
*   Click OK.

This would group the date field and summarize the data as shown below:

![Grouping by Months - Summary](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20228%20482'%3E%3C/svg%3E)

Again, this would lead to a new field of Years getting added to the PivotTable fields. You can simply drag the years’ field to the columns area to get the years in columns and months is rows. You will get something as shown below:

![Group Dates in Pivot Tables in Excel - Year in column Months Rows](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20410%20283'%3E%3C/svg%3E)

### Grouping by Weeks in a Pivot Table

While analyzing data such as store sales or website traffic, it makes sense to analyze it on a weekly basis.

When working with dates in Pivot Tables, grouping dates by week is a bit different than grouping by months, quarters, or years.

Here is how you can group dates by weeks:

*   Select any cell in the Date column in the Pivot Table.
*   Go to Pivot Table Tools –> Analyze –> Group –> Group Selection.![Group Dates in Pivot Tables in Excel - Group Selection](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20128'%3E%3C/svg%3E)
*   In the Grouping dialogue box, select Days and deselect any other selected option(s). As soon as you do this, you would notice that the Number of Days option (at the bottom right) becomes available.
    *   There is no inbuilt option to group by weeks. You need to group by days and specify the number of days to be used while grouping.
    *   Note that for this to work, you need to select Days option only.
*   In Number of days, enter 7 (or use the spin button to make the change).![Pivot Cache in Pivot Table Excel - Select DaysPNG](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20492%20316'%3E%3C/svg%3E)
*   If you click OK at this point, your data would be grouped by weeks starting with January 4, 2014 – which is a Saturday. So the grouping would be from Saturday to Friday every week. To change this grouping and to begin the week from Monday, you need to change the start date (by default it picks the start date from the source data).
    *   In such a case, you can either start the date on December 30, 2013, or January 6, 2014 (both Mondays).
*   Click OK.

This will group the dates by weeks as shown below:

![Group Dates in Pivot Table in Excel - Week start monday](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20324%20396'%3E%3C/svg%3E)

Similarly, you can group dates by specifying any other number of days. For example, instead of weekly, you can group dates in a biweekly interval.

_Note:_

*   _When you group dates by using this method, you can not group it using any other option (such as months, quarters or years)._
*   _Calculated field/item would not work when you group using Days._

### Grouping by Seconds/Hours/Minutes in a Pivot Table

If you working with high volumes of data (such as call center data), you may want to group it by seconds or minutes or hours.

You can use the same process to group the data by seconds, minutes, or hours.

Suppose you have the call center data as shown below:

![Group Dates in Pivot Tables in Excel - Call center data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20399%20302'%3E%3C/svg%3E)

In the above data, the date is recorded along with the time. In this case, it may make sense for the call center manager to analyze how the call resolve numbers are changing per hour.

Here is how to group the days by Hours:

*   Create a pivot table with Date in the Rows area and Resolved in the Values area.
*   Select any cell in the Date column in the Pivot Table.
*   Go to Pivot Table Tools –> Analyze –> Group –> Group Selection.![Group Dates in Pivot Tables in Excel - Group Selection](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20128'%3E%3C/svg%3E)
*   In the Grouping dialogue box, select Hours.![Group Dates in Pivot Tables in Excel - select hours](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20244%20311'%3E%3C/svg%3E)
*   Click OK.

This will group the data by hours and you will get something as shown below:

![Group Dates in Pivot Tables in Excel - by hours resolved](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20274%20270'%3E%3C/svg%3E)

You can see that the Row Labels here are 09, 10, and so on.. which are the hours in a day. 09 would mean 9 AM and 18 would be 6 PM. Using this pivot table, you can easily identify that most calls are resolved during 1-2 PM.

Similarly, you can also group the dates on seconds and minutes.

How to Ungroup Dates in a Pivot Table in Excel
----------------------------------------------

To ungroup dates in pivot tables:

*   Select any cell in the date cells in the pivot table.
*   Go to PivotTable Tools –> Analyze –> Group –> Ungroup.![Group Dates in Pivot Table in Excel - Ungroup](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20655%20133'%3E%3C/svg%3E)

This would instantly ungroup any grouping that you have done.

**[Download the Example File](https://trumpexcel.com/wp-content/uploads/2015/11/Group-Dates-in-Pivot-Table.xlsx)
.** 

**Other Pivot Table Tutorials You May Like:**

*   [Creating a Pivot Table in Excel – A Step by Step Tutorial](https://trumpexcel.com/creating-excel-pivot-table/)
    .
*   [Preparing Source Data For Pivot Table](https://trumpexcel.com/source-data-for-pivot-table/)
    .
*   [How to Group Numbers in Pivot Table in Excel](https://trumpexcel.com/group-numbers-in-pivot-table/)
    .
*   [How to Filter Data in a Pivot Table in Excel.](https://trumpexcel.com/filter-data-pivot-table-excel/)
    
*   [How to Apply Conditional Formatting in a Pivot Table in Excel.](https://trumpexcel.com/apply-conditional-formatting-pivot-table-excel/)
    
*   [How to Refresh Pivot Table in Excel.](https://trumpexcel.com/refresh-pivot-table-excel/)
    
*   [How to Add and Use an Excel Pivot Table Calculated Field](https://trumpexcel.com/excel-pivot-table-calculated-field/)
    .
*   [Using Slicers in Excel Pivot Table.](https://trumpexcel.com/slicers-excel-pivot-table/)
    
*   [How to Replace Blank Cells with Zeros in Excel Pivot Tables](https://trumpexcel.com/replace-blank-cells-with-zeros-excel-pivot-tables/)
    .
*   [Count Distinct Values in Pivot Table](https://trumpexcel.com/count-distinct-pivot-table/)
    
*   [Sort Pivot Table in Excel](https://trumpexcel.com/sort-pivot-table-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

10 thoughts on “How to Group Dates in Pivot Tables in Excel (by Years, Months, Weeks)”
--------------------------------------------------------------------------------------

1.  Unfortunately doesn’t appear to work in Excel 365. There is no longer a grouping option unless you set each group manually and add new dates to an existing group!
    
    [Reply](https://trumpexcel.com/group-dates-in-pivot-tables-excel/#comment-13693)
    
2.  Hi Sumit,  
    I like this tool, but is there a way to set up the quarters to correspond to my company FISCAL calendar? For us, Q1 is OCT-NOV-DEC.  
    Thanks for all you do! I’ve been a quiet follower for a long time.
    
    [Reply](https://trumpexcel.com/group-dates-in-pivot-tables-excel/#comment-3237)
    
3.  Great learning part for new commer.
    
    [Reply](https://trumpexcel.com/group-dates-in-pivot-tables-excel/#comment-3225)
    
4.  Hi , Is this Pivot Date grouping by year, month, etc. is only available in Powerpivot OR it can be done in Excel 2010 also with some add-in ?
    
    [Reply](https://trumpexcel.com/group-dates-in-pivot-tables-excel/#comment-2648)
    
    *   This is available in regular pivot tables and you can use it Excel 2010. No add-in is needed
        
        [Reply](https://trumpexcel.com/group-dates-in-pivot-tables-excel/#comment-2649)
        
        *   Thanks Sumit,
            
            Well I am using Excel 2010 standard. I do not see that ‘Analyze’ menu option on Ribbon. What can be the reason?
            
            [Reply](https://trumpexcel.com/group-dates-in-pivot-tables-excel/#comment-2650)
            
            *   Hey Yogirajoo.. It is a contextual tab. So it becomes available when you click on any cell within the pivot table.
                
                [Reply](https://trumpexcel.com/group-dates-in-pivot-tables-excel/#comment-2651)
                
                *   Thanks Sumit,  
                    Well I already tried that way. Even in Ribbon customize option I don’t see Ananlyze tab at all
                    
                *   Hi Yogirajoo,  
                    In Excel 2010, the Analyze Tab is named as Options
                    
                    Hi Sumit,  
                    I learned a new thing which is very helpful for me. I was doing this manually
                    
                *   Yes Mohsin,
                    
                    I also realized that when I checked button by button. Thanks for the clue.
                    
                    Sumit, thanks again for this good , useful tip !
                    

### Leave a Comment [Cancel reply](https://trumpexcel.com/group-dates-in-pivot-tables-excel/#respond)

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