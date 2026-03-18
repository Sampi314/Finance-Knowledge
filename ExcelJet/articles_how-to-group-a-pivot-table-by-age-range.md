# How to group a pivot table by age range | Exceljet

**Source:** https://exceljet.net/articles/how-to-group-a-pivot-table-by-age-range

---

[Skip to main content](https://exceljet.net/articles/how-to-group-a-pivot-table-by-age-range#main-content)

[](https://exceljet.net/articles/how-to-group-a-pivot-table-by-age-range#)

*   [Previous](https://exceljet.net/articles/collapse-the-ribbon-when-you-dont-need-it)
    
*   [Next](https://exceljet.net/articles/calculating-the-break-even-point-for-google-adwords)
    

How to group a pivot table by age range
=======================================

by Dave Bruns · Updated 23 Oct 2023

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Attachment](https://exceljet.net/file/907/download?token=FRNOiuxN)
 (28.9 KB)

![How to group pivot table data by age](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/group_by_age_thumb.png "How to group pivot table data by age")

Summary
-------

In this article, we look at how to use a pivot table to group voting data by age. This is a good example of the "group by number" feature that all pivot tables share.

### Grouping data with pivot tables

One of the most powerful features of pivot tables is their ability to group data. Any field added as a row or column label is automatically grouped by the values that appear in that field. For example, you might use a pivot table to group a list of employees by department. In this case, with the department field added as a row label, the pivot table neatly breaks out a count of employees by department, with a new row for each department that appears in the source data.

![Pivot table example: grouping employees by department](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/group_by_department.png?itok=3jFBVP_T "Pivot table example: grouping employees by department")

### Voting results source data

Many people stop with this basic automatic grouping, but pivot tables can also group data in more sophisticated ways. For example, you can also use a pivot table to group data by numbers – summarizing data by age range, price range, or any numerical range that makes sense for your data. To illustrate, let’s assume you have a list of voting results that includes voter age, and you want to summarize the results by age group. Your data might look something like this:

![Pivot table source data: voting results with age](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/group_by_age_pivot0.png?itok=f9s4C6Tw "Pivot table source data: voting results with age")

### The basic pivot table

To get started grouping the data by age, first create your pivot table normally. Next, add the field Age as a Row Label, and the field Vote as a Column Label. Finally, add Name as a Value. In the example below, we also renamed Grand Total to Total. At this point, our pivot table looks like this:

![Pivot table example: grouping voting data ungrouped](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/group_by_age_pivot1.png?itok=SdSw8XPp "Pivot table example: grouping voting data ungrouped")

### Grouping by age

Although this pivot table is interesting, it’s not very useful, since the automatic grouping by actual age is too granular. We don't care that five 20-year-olds voted for Option B – we want to see voting results by age ranges, like 20-29, 30-39, etc. This is easily done using the grouping feature built in to pivot tables. To group results by age, right-click any value in the Age field and choose Group from the menu.

![Pivot table example: grouping by age](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/group_by_age_pivot2.png?itok=llMuAR80 "Pivot table example: grouping by age")

### Specifying the interval

When the Grouping dialog box appears, enter any interval that makes sense in the “By:” input area.  For this example, we’ll group by 10 years.

![Pivot table example: grouping by age, specifying the interval](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/group_by_age_pivot3.png?itok=bQhJv69p "Pivot table example: grouping by age, specifying the interval")

### The final result

When you click OK, you’ll see your data neatly grouped by age at 10 year intervals.

![Final pivot table: voting data grouped by age](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/group_by_age_pivot4.png?itok=YZ7RSlfg "Final pivot table: voting data grouped by age")

You can use this same approach to group numeric data in many useful ways. You can group customers by total sales, group employees by their time at a company, group weather data by temperature – the list is endless.

### Learning pivot tables

Pivot tables are easy to create but hard to control. Our short video course, [Core Pivot](https://exceljet.net/training/core-pivot)
, walks you step-by-step through the most important features of Pivot Tables.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Articles

*   [How to group a pivot table by age range](https://exceljet.net/videos/how-to-group-a-pivot-table-by-age-range)
    

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