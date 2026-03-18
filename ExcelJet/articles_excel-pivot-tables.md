# Excel Pivot Tables | Exceljet

**Source:** https://exceljet.net/articles/excel-pivot-tables

---

[Skip to main content](https://exceljet.net/articles/excel-pivot-tables#main-content)

[](https://exceljet.net/articles/excel-pivot-tables#)

*   [Previous](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
    
*   [Next](https://exceljet.net/articles/excel-formula-errors)
    

Excel Pivot Tables
==================

by Dave Bruns · Updated 19 Oct 2023

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Attachment](https://exceljet.net/file/5534/download?token=p20jGYLt)
 (29.83 KB)

![Excel Pivot Tables](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/excel_pivot_tables.jpg "Excel Pivot Tables")

Summary
-------

Pivot tables are the fastest and easiest way to quickly analyze data in Excel. This article is an introduction to Pivot Tables and their benefits, and a step-by-step guide with sample data.

Quick Links
-----------

*   [Overview](https://exceljet.net/articles/excel-pivot-tables)
    
*   [Why Pivot?](https://exceljet.net/plc/why-pivot-tables)
    
*   [Tips](https://exceljet.net/articles/pivot-table-tips)
    
*   [Examples](https://exceljet.net/pivot-tables)
    
*   [Training](https://exceljet.net/training/core-pivot)
    

Pivot tables are one of the most powerful and useful features in Excel. With very little effort, you can use a pivot table to build good-looking reports for large data sets. If you need to be convinced that Pivot Tables are worth your time, [watch this short video](https://exceljet.net/plc/why-pivot-tables)
. 

_Grab the [sample data](https://exceljet.net/articles/excel-pivot-tables#sample_data)
 and give it a try. Learning Pivot Tables is a skill that will pay you back again and again. Pivot tables can dramatically increase your efficiency in Excel._

### What is a pivot table?

You can think of a pivot table as a report. However, unlike a static report, a pivot table provides an [interactive view of your data](https://exceljet.net/videos/what-is-a-pivot-table)
. With very little effort (and no formulas) you can look at the _same data from many different perspectives_. You can group data into categories, break down data into years and months, filter data to include or exclude categories, and even build charts.

_The beauty of pivot tables is they allow you to interactively explore your data in different ways._

### Contents

*   [Sample data](https://exceljet.net/articles/excel-pivot-tables#sample_data)
    
*   [Insert Pivot table](https://exceljet.net/articles/excel-pivot-tables#insert)
    
*   [Add fields](https://exceljet.net/articles/excel-pivot-tables#add_fields)
    
*   [Sort by value](https://exceljet.net/articles/excel-pivot-tables#sorting)
    
*   [Refresh data](https://exceljet.net/articles/excel-pivot-tables#refresh)
    
*   [Second value field](https://exceljet.net/articles/excel-pivot-tables#second_value)
    
*   [Apply number formatting](https://exceljet.net/articles/excel-pivot-tables#number_formatting)
    
*   [Group by date](https://exceljet.net/articles/excel-pivot-tables#group_by_date)
    
*   [Add percent of total](https://exceljet.net/articles/excel-pivot-tables#percent_of_total)
    
*   [Benefits summary](https://exceljet.net/articles/excel-pivot-tables#benefits)
    
*   [More resources](https://exceljet.net/articles/excel-pivot-tables#more_resources)
    

Step-by-step tutorial
---------------------

To understand pivot tables, you need to work with them yourself. In this section, we'll build several pivot tables step-by-step from a set of sample data. With experience, the pivot tables below can be built in about 5 minutes.

### Sample data

The [sample data](https://exceljet.net/sites/default/files/attachments/sample%20data%20for%20pivot%20table.xlsx)
 contains 452 records with 5 fields of information: Date, Color, Units, Sales, and Region. This data is perfect for a pivot table.

![Sample sales data already in an Excel Table](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/sample%20sales%20data%20in%20excel%20table%20ept.png?itok=TjY6zDWf "Sample sales data already in an Excel Table")

Data in a proper [Excel Table](https://exceljet.net/articles/excel-tables)
 named "Table1". Excel Tables are a [great way to build pivot tables](https://exceljet.net/videos/why-you-should-use-a-table-for-your-pivot-table)
, because they automatically adjust as data is added or removed. 

_Note: I know this data is very generic. But generic data is good for understanding pivot tables – you don't want to get tripped up on a detail when learning the fun parts._

### Insert Pivot Table

1\. To start off, select _any cell in the data_ and click Pivot Table on the Insert tab of the ribbon:

![Click the button at Insert > Pivot Table](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/ept_pivot_table_insert_button.png?itok=qKlofIZ- "Click the button at Insert > Pivot Table")

Excel will display the Create Pivot Table window. Notice the data range is already filled in. The default location for a new pivot table is New Worksheet.

2\. Override the default location and enter H4 to place the pivot table on the current worksheet:

![Create Pivot Table window](https://exceljet.net/sites/default/files/images/articles/inline/ept_create_pivot_table_widow.png "Create Pivot Table window")

3\. Click OK, and Excel builds an empty pivot table starting in cell H4.

![New empty pivot table staring at cell H4](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/new%20empty%20pivot%20table%20ept.png?itok=0jQu_hiz "New empty pivot table staring at cell H4")

_Note: there are good reasons to place a pivot table on a different worksheet. However, when learning pivot tables, it's helpful to see both the source data and the pivot table at the same time._

Excel also displays the PivotTable Fields pane, which is empty at this point. Note all five fields are listed, but unused:

![Fields pane for new empty pivot table](https://exceljet.net/sites/default/files/images/articles/inline/pivot%20table%20fields%20pane%20empty%20ept.png "Fields pane for new empty pivot table")

To build a pivot table, drag fields into one of the Columns, Rows, or Values area. The Filters area is used to apply global filters to a pivot table.

_Note: the pivot table fields pane shows how fields were used to create a pivot table. Learning to "read" the fields pane takes a bit of practice. See below and [also here](https://exceljet.net/pivot-tables)
 for more examples._

### Add fields

1\. Drag the Sales field to the Values area.

Excel calculates a grand total of 26356. This is the sum of all sales values in the entire data set:

![Grand total of all data in data set](https://exceljet.net/sites/default/files/images/articles/inline/grand%20total%20of%20all%20data%20ept.png "Grand total of all data in data set")

2\. Drag the Color field to the Rows area.

Excel breaks out sales by Color. You can see Blue is the top seller, while Red comes in last:

![Breakdown by color](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/breakdown%20by%20color%20ept.png?itok=Kf1ZEdyL "Breakdown by color")

Notice the Grand Total remains 26356. This makes sense because we are still reporting on the full set of data.

Let's take a look at the fields pane at this point. You can see Color is a Row field, and Sales is a Value field:

![Pivot table fields pane - sales by color](https://exceljet.net/sites/default/files/images/articles/inline/pivot%20table%20fields%20pane%20sales%20by%20color%20ept.png "Pivot table fields pane - sales by color")

### Number formatting

Pivot Tables can apply and maintain number formatting automatically to numeric fields. This is a big time-saver when data changes frequently.

1\. Right-click any Sales number and choose Number Format:

![Right-click and select Number Format](https://exceljet.net/sites/default/files/images/articles/inline/right%20click%20select%20number%20format%20ept.png "Right-click and select Number Format")

2\. Apply Currency formatting with zero decimal places, then click OK:

![Currency number format with zero decimal places](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/apply%20number%20format%20ept.png?itok=qI6fWhlE "Currency number format with zero decimal places")

In the resulting pivot table, all sales values have Currency format applied:

![Pivot table with Currency format applied](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/pivot%20table%20currency%20format%20applied%20ept.png?itok=YChoZkfd "Pivot table with Currency format applied")

Currency format will continue to be applied to Sales values, even when the pivot table is reconfigured, or new data is added.

### Sorting by value

1\. Right-click any Sales value and choose Sort > Largest to Smallest.

![Right-click and select Sort > Largest to smallest](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/right%20click%20select%20sort%20ept.png?itok=9qSC5eIc "Right-click and select Sort > Largest to smallest")

Excel now lists top-selling colors first. This sort order will be maintained when data changes, or when the pivot table is reconfigured. 

![Breakdown by color, top selling colors first](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/breakdown%20by%20color%20sorted%20ept.png?itok=-zqvdIJj "Breakdown by color, top selling colors first")

### Refresh data

Pivot table data needs to be "refreshed" in order to bring in updates. To reinforce how this works, we'll make a big change to the source data and watch it flow into the pivot table.

1\. Select cell F5 and change $11.00 to $2000.

2\. Right-click anywhere in the pivot table and select "Refresh".

![To update data, right-click and choose "Refresh"](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/right%20click%20select%20refresh.png?itok=TIYo8OLn "To update data, right-click and choose "Refresh"")

Notice "Red" is now the top-selling color, and automatically moves to the top:

![Pivot table after data refresh](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/pivot%20table%20after%20refresh.png?itok=kRRjc9EH "Pivot table after data refresh")

3\. Change F5 back to $11.00 and refresh the pivot again.

_Note: changing F5 to $2000 is not realistic, but it's a good way to force a change you can easily see in the pivot table. Try changing an existing color to something new, like "Gold" or "Black". When you refresh, you'll see the new color appear. You can use undo to go back to the original data and pivot._

### Second value field

You can add more than one field as a Value field.

1\. Drag Units to the Value area to see Sales and Units together:

![Breakdown by color with Sales and Units](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/breakdown%20by%20color%20with%20units%20ept.png?itok=Cv_UZnNO "Breakdown by color with Sales and Units")

### Percent of total

There are different ways to display values. One option is to show values as a percent of the total. If you want to display the same field in different ways, add the field twice.

1\. Remove the Units from the Values area

2\. Add the Sales field (again) to the Values area.

3\. Right-click the second instance and choose "% of grand total":

![Right-click select Show values as > percent of total ](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/right%20click%20select%20show%20values%20as%20percent%20of%20total%20ept.png?itok=rfOwE-J7 "Right-click select Show values as > percent of total ")

The result is a breakdown by color along with a percent of the total:

![Pivot table - breakdown by color with percentage](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/breakdown%20by%20color%20with%20percentage%20ept.png?itok=2zDy4b7i "Pivot table - breakdown by color with percentage")

_Note: the number format for percentage has also been adjusted to show 1 decimal._

Here is the Fields pane at this point:

![Pivot table fields pane - sales by color with percentage](https://exceljet.net/sites/default/files/images/articles/inline/pivot%20table%20fields%20pane%20sales%20with%20percentage%20ept.png "Pivot table fields pane - sales by color with percentage")

### Group by date

Pivot tables have a special feature to group dates into units like years, months, and quarters. This grouping can be customized.

1\. Remove the second Sales field (Sales2). 

2\. Drag the Date field to the Columns area.

3\. Right-click a date in the header area and choose "Group":

![Right click a date and select group](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/right%20click%20date%20select%20group%20ept.png?itok=gi5llif0 "Right click a date and select group")

4\. When the Group window appears, group by Years only (deselect Months and Quarters):

![Date grouping settings - group by Years only](https://exceljet.net/sites/default/files/images/articles/inline/group%20by%20date%20years%20only.png "Date grouping settings - group by Years only")

We now have a pivot table that groups sales by color and year:

![Two-way pivot table - sales by color and year](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/breakdown%20by%20color%20by%20year%20ept.png?itok=mw_PWSqw "Two-way pivot table - sales by color and year")

Notice there are no sales of Silver in 2016 and 2017. We can guess that Silver was introduced as a new color in 2018. Pivot tables often reveal patterns in data that are difficult to see otherwise.

Here is the Fields pane at this point:

![Pivot table fields pane - sales by color and by year](https://exceljet.net/sites/default/files/images/articles/inline/pivot%20table%20fields%20pane%20sales%20by%20color%20and%20year%20ept.png "Pivot table fields pane - sales by color and by year")

### Two-way Pivot

Pivot tables can plot data in various two-dimensional arrangements.

1\. Drag the Date field out of the columns area

2\. Drag Region into the Columns area.

Excel builds a two-way pivot table that breaks down sales by color and region:

![Two-way pivot table - sales by color and region](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/breakdown%20by%20color%20and%20region%20ept.png?itok=hls8ke6r "Two-way pivot table - sales by color and region")

3\. Swap Region and Color (i.e. drag Region to the Rows area and Color to the Columns area). 

Excel builds another two-dimensional pivot table:

![Two-way pivot table - sales by region and color](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/breakdown%20by%20region%20and%20color%20ept.png?itok=7iuLDcsp "Two-way pivot table - sales by region and color")

Again notice that total sales ($26,356) is the same in _all pivot tables above_. Each table presents a different view of the _same data_, so they all sum to the _same total_.

The above example shows how quickly you can build different pivot tables from the same data. You can create [many other kinds of pivot tables](https://exceljet.net/pivot-tables)
, using all kinds of data.

### Key Pivot Table benefits

**Simplicity**. Basic pivot tables are very simple to set up and customize. There is no need to learn complicated formulas.

**Speed**. You can create a good-looking, useful report with a pivot table in minutes. Even if you are very good with formulas, [pivot tables are faster to set up and require much less effort](https://exceljet.net/videos/why-pivot-tables)
.

**Flexibility**. Unlike formulas, pivot tables don't lock you into a particular view of your data. You can quickly rearrange the pivot table to suit your needs. You can even [clone a pivot table](https://exceljet.net/videos/how-to-clone-a-pivot-table)
 and build a separate view.

**Accuracy**. As long as a pivot table is set up correctly, you can rest assured results are accurate. In fact, a pivot table will often highlight problems in the data faster than any other tool.

**Formatting**. A Pivot table can apply automatically apply consistent number and style formatting, even as data changes.

**Updates**. Pivot tables are designed for ongoing updates. If you base a pivot table on an Excel Table, the table resizes as needed with new data. [All you need to do is click Refresh](https://exceljet.net/videos/how-to-refresh-data-in-a-pivot-table)
, and your pivot table will show you the latest.

**Filtering**. Pivot tables contain several tools for filtering data. Need to look at North America and Asia, but exclude Europe? A pivot table makes it simple.

**Charts**. Once you have a pivot table, you can easily [create a pivot chart](https://exceljet.net/videos/how-to-create-a-pivot-chart-2016)
.

### More pivot table resources

*   [Pivot table examples](https://exceljet.net/pivot-tables)
    
*   [Pivot table tips](https://exceljet.net/articles/pivot-table-tips)
    
*   [Pivot tables versus formulas](https://exceljet.net/videos/why-pivot-tables)
    
*   [Pivot table training](https://exceljet.net/training/core-pivot)
    

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