# Pivot Table Tips | Exceljet

**Source:** https://exceljet.net/articles/pivot-table-tips

---

[Skip to main content](https://exceljet.net/articles/pivot-table-tips#main-content)

[](https://exceljet.net/articles/pivot-table-tips#)

*   [Previous](https://exceljet.net/articles/can-pivot-tables-save-your-job)
    
*   [Next](https://exceljet.net/articles/the-value-of-improving-a-skill-a-simple-model)
    

Pivot Table Tips
================

by Dave Bruns · Updated 24 Oct 2023

![Things to know about Excel pivot tables](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/things_to_know_cover.png "Things to know about Excel pivot tables")

Summary
-------

Many Excel experts believe that Pivot Tables are the single most powerful tool in Excel. This article provides more than 20 tips you should know to work productively with Excel Pivot Tables.

Quick Links
-----------

*   [Overview](https://exceljet.net/articles/excel-pivot-tables)
    
*   [Why Pivot?](https://exceljet.net/plc/why-pivot-tables)
    
*   [Tips](https://exceljet.net/articles/pivot-table-tips)
    
*   [Examples](https://exceljet.net/pivot-tables)
    
*   [Training](https://exceljet.net/training/core-pivot)
    

Pivot tables are a reporting engine built into Excel. They are the single best tool in Excel for analyzing data _without formulas_. You can create a basic pivot table in about one minute, and begin interactively exploring your data. Below are more than 20 tips for getting the most from this flexible and powerful tool.

### 1\. You can build a pivot table in about one minute

Many people think building a pivot table is complicated and time-consuming, but it's simply not true. Compared to the time it would take you to build an equivalent report manually, pivot tables are incredibly fast. If you have well-structured source data, you can create a pivot table in less than a minute. Start by selecting any cell in the source data:

![Raw data (chocolate sales), ready for a pivot table](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/quickpivot_data.png?itok=GBY8gsZz "Raw data (chocolate sales), ready for a pivot table")  
_Example source data_

Next, follow these four steps:

1.  On the Insert tab of the ribbon, click the PivotTable button
2.  In the Create PivotTable dialog box, check the data and click OK
3.  Drag a "label" field into the Row Labels area (e.g. customer)
4.  Drag a numeric field into the Values area (e.g. sales)

![A quick Excel pivot table showing chocolate sales](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/quickpivot_big.png?itok=bWiaHbSB "A quick Excel pivot table showing chocolate sales")  
_A basic pivot table in about 30 seconds_

The pivot table above shows total sales by product, but you can easily rearrange fields to show total sales by region, by category, by month, and so on. Watch the video below for a quick demonstration:

Video: [How to quickly create a pivot table](https://exceljet.net/videos/how-to-quickly-create-a-pivot-table)

### 2\. Clean your source data

To minimize problems down the road, make sure your data is in good shape. Source data should have no blank rows or columns, and no subtotals. Each column should have a unique name (on one row only) and represent a field for each row/record in the data:

![Perfect data for a pivot table!](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/perfect_data.png?itok=f_NNYIhu "Perfect data for a pivot table!")  
_Perfect data for a pivot table!_

You might sometimes need to add missing data. See this video for tips:

Video: [How to quickly fill in missing data](https://exceljet.net/videos/how-to-fill-in-missing-data-with-a-simple-formula)

### 3\. Count the data first

When you first create a pivot table, use it to generate a simple count first to make sure the pivot table is processing the data as you expect. To do this, simply add any _text field_ as a Value field. You'll see a very small pivot table that displays the total record count, that is, the total number of rows in your data. If this number makes sense to you, you're good to go. If the number doesn't make sense to you, it's possible the pivot table is not reading the data correctly or that the data has not been defined correctly.

![300 first names means we have 300 employees. Check.](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/simple_count_0.png?itok=wAmtQsAU "300 first names means we have 300 employees. Check.")  
_300 first names means we have 300 employees. Check._

### 4\. Plan before you build

Although it's a lot of fun dragging fields around a pivot table, and watching Excel churn out yet another unusual representation of the data, you can find yourself going down a lot of unproductive rabbit holes very easily. An hour later, it's not so fun anymore. Before you start building, jot down what you are trying to measure or understand, and sketch out a few simple reports on a notepad. These simple notes will help guide you through the huge number of choices you have at your disposal. Keep things simple, and focus on the questions you need to answer.

### 5\. Use a table for your data to create a "dynamic range"

If you use an Excel Table for the source data of your pivot table, you get a very nice benefit: your data range becomes "dynamic". A dynamic range will automatically expand and shrink the table as you add or remove data, so won't have to worry that the pivot table is missing the latest data. When you use a Table for your pivot table, the pivot table will always be in sync with your data.

To use a Table for your pivot table:

1.  Select any cell in the data and use the keyboard shortcut Ctrl-T to create a Table
2.  Click the Summarize with PivotTable button (TableTools > Design)
3.  Build your pivot table normally
4.  Profit: data you add to your Table will automatically appear in your Pivot table on refresh

Video: [Use a table for your next pivot table](https://exceljet.net/videos/why-you-should-use-a-table-for-your-pivot-table)

![Creating a simple Table from the data using (Ctrl-T)](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/create_table.png?itok=iAVGHRvJ "Creating a simple Table from the data using (Ctrl-T)")  
_Creating a simple Table from the data using (Ctrl-T)_

![Now that we have a table, we can use Summarize with PivotTable](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/create_table1.png?itok=D1i2P-p1 "Now that we have a table, we can use Summarize with PivotTable")  
_Now that we have a table, we can use Summarize with a  Pivot Table_

> Still need inspiration on why you should learn pivot tables? See [my personal story](https://exceljet.net/articles/can-pivot-tables-save-your-job)
> .

### 6\. Use a pivot table to count things

By default, a Pivot Table will count any text field. This can be a really handy feature in a lot of general business situations. For example, suppose you have a list of employees and want to get a count by department. To get a breakdown by department,  follow these steps:

1.  Create a pivot table normally
2.  Add the Department as a Row Label
3.  Add the employee Name field as a Value
4.  The pivot table will display a count of employee by Department

![Employee breakdown by department](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/count_things2.png?itok=xztwD2qh "Employee breakdown by department")  
_Employee breakdown by department_

### 7\. Show totals as a percentage

In many pivot tables, you'll want to show a percentage rather than a count. For example, perhaps you want to show a breakdown of sales by product. But, rather than show the total sales for each product, you want to show sales as a percentage of the total sales. Assuming you have a field called Sales in your data, just follow these steps:

1.  Add Product to the pivot table as a Row Label
2.  Add Sales to the pivot table as a Value
3.  Right-click the Sales field, and set "Show Values As" to "% of Grand Total"

See the tip below "Add a field more than once to a pivot table" to learn how to show total sales and sales as a percent of total at the same time.

![Changing value display to % of total](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/total_as_percent1.png?itok=qhROIjy4 "Changing value display to % of total")  
_Changing value display to % of total_

![Sum of employees displayed as % of total](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/total_as_percent2.png?itok=TcUkZsZt "Sum of employees displayed as % of total")  
_The sum of employees displayed as % of total_

### 8\. Use a pivot table to build a list of unique values

Because pivot tables summarize data, they can be used to find unique values in a field. This is a good way to quickly see all the values that appear in a field and also find typos, and other inconsistencies. For example, suppose you have sales data and you want to see a list of every product that was sold. To create a product list:

1.  Create a pivot table normally
2.  Add the Product as a Row Label
3.  Add any other text field (category, customer, etc) as a Value
4.  The pivot table will show a list of all products that appear in the sales data

![Every product that appears in the data is listed (including a typo)](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/unique_value2.png?itok=IxMCHnFj "Every product that appears in the data is listed (including a typo)")  
_Every product that appears in the data is listed (including a typo)_

> [Pivot Table video training - quick, clean, and to the point](https://exceljet.net/training/core-pivot)

### 9\. Create a self-contained pivot table

When you've created a pivot table from data in the same worksheet, you can remove the data if you like and the pivot table will continue to operate normally. This is because a pivot table has a _pivot cache_ that contains an exact duplicate of the data used to create the pivot table.

1.  Refresh the pivot table to ensure the cache is up to date (PivotTable Tools > Refresh)
2.  Delete the worksheet that contains the data
3.  Use your pivot table normally

Video: [How to make a self-contained pivot table](https://exceljet.net/videos/how-to-make-a-self-contained-pivot-table)

### 10\. Group a pivot table manually

Although pivot tables automatically group data in many ways, you can also group items manually into your own custom groups. For example, assume you have a pivot table that shows a breakdown of employees by department. Suppose you want to further group the Engineering, Fulfillment, and Support departments into Group 1, and Sales and Marketing into Group 2. Group 1 and Group 2 don't appear in the data, they are your own custom groups. To group the pivot table into the ad hoc groups, Group 1 and Group 2:

1.  Control-click to select each item in the first group
2.  Right-click one of the items and choose Group from the menu
3.  Excel creates a new group, "Group1"
4.  Select Marketing and Sales in column B, and group as above
5.  Excel creates another group, "Group2"

![Starting to group manually](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/manual_group_1.png?itok=22ykr7rk "Starting to group manually")  
_Starting to group manually_

![Half way through manual grouping - Group 1 is done](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/manual_group_2.png?itok=QP6YAofB "Half way through manual grouping - Group 1 is done")  
_Half way through manual grouping - Group 1 is done_

![Finished grouping manually](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/manual_group_3.png?itok=mG1exQPe "Finished grouping manually")  
_Finished grouping manually_

### 11\. Group numeric data into ranges

One of the most interesting and powerful features that every pivot table has is the ability to group numeric data into ranges or buckets. For example, assume you have a list of voting results that includes voter age, and you want to summarize the results by age group:

1.  Create your pivot table normally
2.  Add Age as a Row Label, Vote as a Column Label, and Name as a Value
3.  Right-click any value in the Age field and choose Group
4.  Enter 10 as the interval in the "By:" input area
5.  When you click OK, you'll see the voting data grouped by age into 10-year buckets

Video: [How to group a pivot table by age range](https://exceljet.net/videos/how-to-group-a-pivot-table-by-age-range)

![The source data for voting results](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/group_votes_1.png?itok=iysGZnnW "The source data for voting results")  
_The source data for voting results_

![Grouping the age field into 10 year buckets](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/group_votes_2.png?itok=BLfedmVA "Grouping the age field into 10 year buckets")  
_Grouping the age field into 10-year buckets_

![Done grouping voting results by age range](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/group_votes_3.png?itok=nYozDjWe "Done grouping voting results by age range")  
_Done grouping voting results by age range_

### 12\. Rename fields for better readability

When you add fields to a pivot table, the pivot table will display the name that appears in the source data. Value field names will appear with "Sum of " or "Count of" when they are added to a pivot table. For example, you'll see Sum of Sales, Count of Region, and so on. However, you can simply overwrite this name with your own. Just select the cell that contains the field you want to rename and type a new name.

![Rename a field by typing over the original name](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/rename_field1.png?itok=zoHNMHbo "Rename a field by typing over the original name")  
_Rename a field by typing over the original name_

### 13\. Add a space to field names when Excel complains

When you try to rename fields, you might run into a problem if you try to use exactly the same field name that appears in the data. For example, suppose you have a field called Sales in your source data. As a value field, it appears as _Sum of Sales_, but (sensibly) you want it to say _Sales_. However, when you try to use Sales, Excel complains that the field already exists, and throws a "PivotTable field name already exists" error message.

![Excel doesn't like your new field name](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/rename_field2.png?itok=1E6yjI4q "Excel doesn't like your new field name")  
_Excel doesn't like your new field name_

As a simple workaround, just add a space to the end of your new field name. You can't see a difference, and Excel won't complain.

![Adding a space to the name avoids the problem](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/rename_field3.png?itok=dtGlnnX6 "Adding a space to the name avoids the problem")  
_Adding a space to the name avoids the problem_

### 14\. Add a field more than once to a pivot table

There are many situations when it makes sense to add the same field to a pivot table more than once. It may seem odd, but you can indeed add the same field to a pivot table more than once. For example, suppose you have a pivot table that shows a count of employees by department.

The count works fine, but you also want to show the count as a percentage of total employees. In this case, the simplest solution is to add the same field twice as a Value field:

1.  Add a text field to the Value area (e.g. First name, Name, etc.)
2.  By default, you'll get a count for text fields
3.  Add the same field again to the Value area
4.  Right-click the second instance, and change Show Values As to "% of Grand Total"
5.  Rename both fields as you wish

![Setting a field to show percent of total](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/percent_of_total.png?itok=ctuKZxtT "Setting a field to show percent of total")  
_Setting a field to show percent of total_

![The Name field has been added twice](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/add_field_again1.png?itok=9zurKL91 "The Name field has been added twice")  
_The Name field has been added twice_

### 15\. Automatically format all value fields

Any time you add a numeric field as a Value in a pivot table, you should set the number format directly on the field. You may be tempted to format the values you see in the pivot table directly, but this is not a good idea, because it's not reliable as the pivot table changes. Setting the format directly on the field will ensure that the field is displayed using the format you want, no matter how big or small the pivot table becomes.

For example, assume a pivot table that shows a breakdown of sales by Region. When you first add the Sales field to the pivot table, it will be displayed in General number format, since it's a numeric field. To apply the Accounting number format to the field itself:

1.  Right-click on the Sales field and select Value Field Settings from the menu
2.  Click the Number Format button in the Value field settings dialog that appears
3.  Set the format to Accounting and click OK to exit

![Setting format directly on a value field](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/format_value_field1.png?itok=hSKBj2tC "Setting format directly on a value field")  
_Setting format directly on a value field_

### 16\. Drill down to see (or extract) the data behind any total

Whenever you see a total displayed in a pivot table, you can easily see and extract the data that makes up the total by "drilling down". For example, assume you are looking at a pivot table that shows employee count by department. You can see that there are 50 employees in the Engineering department, but you want to see the actual names. To see the 50 people that make up this number, double-click directly on the number 50, and Excel will add a new sheet to your workbook that contains the exact data used to calculate 50 engineers. You can use this same approach to see and extract data behind totals wherever you see them in a pivot table.

![Double click a total to "drill down"](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/drill_down1.png?itok=Yrwa27W7 "Double click a total to "drill down"")  
_Double click a total to "drill down"_

![The 50 Engineers, extracted into a new sheet automatically](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/drill_down2.png?itok=LsZ9BBM1 "The 50 Engineers, extracted into a new sheet automatically")  
_The 50 Engineers, extracted into a new sheet automatically_

### 17\. Clone your pivot tables when you need another view

Once you have one pivot table set up, you might want to see a different view of the same data. You could of course just rearrange your existing pivot table to create the new view. But if you're building a report that you plan to use and update on an ongoing basis, the easiest thing to do is clone an existing pivot table, so that both views of the data are always available.

There are two easy ways to clone a pivot table. The first way involved duplicating the worksheet that holds the pivot table. If you have a pivot table set up in a worksheet with a title, etc., you can just right-click the worksheet tab to copy the worksheet into the same workbook. Another way to clone a pivot table is to copy the pivot table and paste it somewhere else. Using these approaches, you can make as many copies as you like.

When you clone a pivot table this way, both pivot tables share the same _pivot cache_. This means that when you refresh any one of the clones (or the original) all of the related pivot tables will be refreshed.

Video: [How to clone a pivot table](https://exceljet.net/videos/how-to-clone-a-pivot-table)

### 18\. Un-clone a pivot table to refresh independently

After you've cloned a pivot table, you might run into a situation where you really don't want the clone to be linked to the same pivot cache as the original. A common example is after you've grouped a date field in one pivot table, refresh, and discover that you've also accidentally grouped the same date field in _another_ pivot table that you didn't intend to change. When pivot tables share the same pivot cache, they also share field grouping as well.

Here's one way to un-clone a pivot table, that is, unlink it from the pivot cache it shares with other pivot tables in the same worksheet:

1.  Cut the entire pivot table to the clipboard
2.  Paste the pivot table into a brand-new workbook
3.  Refresh the pivot table
4.  Copy it again to the clipboard
5.  Paste it back into the original workbook
6.  Discard the temporary workbook

Your pivot table will now use its own pivot cache and will not refresh with the other pivot table(s) in the workbook, or share the same field grouping.

### 19\. Get rid of useless headings

The default layout for new pivot tables is the Compact layout. This layout will display "Row Labels" and "Column Labels" as headings in the pivot table. These aren't the most intuitive headings, especially for people who don't often use pivot tables. An easy way to get rid of these odd headings is to switch the pivot table layout from Compact to Outline or Tabular layout. This will cause the pivot table to display the actual field names as headings in the pivot table, which is much more sensible. To get rid of these labels altogether, look for a button called Field Headers on the Analyze tab of the Pivot Table Tools ribbon. Clicking this button will disable headings completely.

![Note the useless and confusing field headings](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/field_headings1.png?itok=X9T6RwVq "Note the useless and confusing field headings")  
_Note the useless and confusing field headings_

![Switching the layout from Compact to Outline](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/field_headings2.png?itok=-AFmuEgC "Switching the layout from Compact to Outline")  
_Switching the layout from Compact to Outline_

![Field headings in Outline layout are much more sensible](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/field_headings3.png?itok=FNsE8ZSi "Field headings in Outline layout are much more sensible")  
_Field headings in the Outline layout are much more sensible_

### 20\. Add a little white space around your pivot tables

This is just a simple design tip. All good designers know that a pleasing design requires a little white space. White space just means empty space set aside to give the layout breathing room. After you create a pivot table, insert an extra column to the left and an extra row or two at the top. This will give your pivot table some breathing room and create a better looking layout. In most cases, I also recommend that you turn off gridlines on the worksheet. The pivot table itself will present a strong visual grid, so the gridlines outside the pivot table are unnecessary, and will simply create visual noise.

![Add a little white space around pivot tables](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/pt_white_space2.png?itok=F_mgtCXW "Add a little white space around pivot tables")  
_A little white space makes your pivot tables look more polished_

> Inspiration: [5 pivot tables you haven't seen before](https://exceljet.net/articles/5-pivot-tables-you-probably-havent-seen-before)
> .

### 21\. Get rid of row and column grand totals

By default, pivot tables show totals for both rows and columns, but you can easily disable one or both of these totals if you don't want them. On the Pivot Table tab of the ribbon, just click the Totals button and choose the options you want.

![Enable and disable grand totals](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/pt_grand_totals.png?itok=PboVJmcE "Enable and disable grand totals")  
_You can remove grand totals for both rows and columns_

### 22\. Format empty cells

If you have a pivot table that has a lot of blank cells, you can control the character that is displayed in each blank cell. By default, empty cells will display nothing at all. To set your own character, right-click inside the pivot table and select Pivot Table options. Then make sure that "Empty cells as:" is checked, and enter the character you want to see. Keep in mind that this setting respects the applied number format. For example. if you are using the accounting number format for a numeric value field, and enter a zero, you'll see a hyphen "-" displayed in the pivot table, since that's how zero values are displayed with the Accounting format.

![Pivot table show empty cells as 0 (zero) with accounting format](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/pt_format_empty_cells.png?itok=tNZVlFZJ "Pivot table show empty cells as 0 (zero) with accounting format")  
_Empty cells set to display 0 (zero) and Accounting number format gives you hyphens_

### 23\. Turn off AutoFit when necessary

By default, when you refresh a pivot table, the columns that contain data are adjusted automatically to best fit the data. Normally, this is a good thing, but it can drive you crazy if you have other things on the worksheet along with the pivot table, or if you have carefully adjusted the column widths manually and don't want them changed. To disable this feature, right-click inside the pivot table and choose PivotTable Options. In the first tab of the options (or the layout tab on a Mac), uncheck "AutoFit Column Widths on Update".

![Pivot table column autofit option for Windows](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/pt_autofit_win.png?itok=AUcwx0cK "Pivot table column autofit option for Windows")  
_Pivot table column autofit option for Windows_

![Pivot table column autofit option for Mac](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/pt_autofit_mac.png?itok=eZhELD-S "Pivot table column autofit option for Mac")  
_Pivot table column autofit option for Mac_

> Need to learn Pivot Tables? We have [solid video training](https://exceljet.net/training/core-pivot)
>  with practice worksheets.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Articles

*   [Can pivot tables save your job?](https://exceljet.net/articles/can-pivot-tables-save-your-job)
    
*   [5 pivot tables you probably haven't seen before](https://exceljet.net/articles/5-pivot-tables-you-probably-havent-seen-before)
    

### Training

*   [Core Pivot](https://exceljet.net/training/core-pivot)
    

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