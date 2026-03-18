# Count between dates by age range - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-between-dates-by-age-range

---

[Skip to main content](https://exceljet.net/formulas/count-between-dates-by-age-range#main-content)

[](https://exceljet.net/formulas/count-between-dates-by-age-range#)

*   Previous
*   [Next](https://exceljet.net/formulas/count-birthdays-by-year)
    

[Count](https://exceljet.net/formulas#Count)

Count between dates by age range
================================

by Dave Bruns · Updated 22 Jun 2022

Related functions 
------------------

[COUNTIFS](https://exceljet.net/functions/countifs-function)

[FIND](https://exceljet.net/functions/find-function)

[LEFT](https://exceljet.net/functions/left-function)

[RIGHT](https://exceljet.net/functions/right-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[TEXTBEFORE](https://exceljet.net/functions/textbefore-function)

![Excel formula: Count between dates by age range](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20between%20dates%20by%20age%20range.png "Excel formula: Count between dates by age range")

Summary
-------

To count values between two dates that also fall into specific numeric ranges, you can use a formula based on the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
, with help from the [LEFT](https://exceljet.net/functions/left-function)
, [RIGHT](https://exceljet.net/functions/right-function)
, [FIND](https://exceljet.net/functions/find-function)
, and [LEN](https://exceljet.net/functions/len-function)
 functions. In the example shown the formula in H8, copied down, is:

    =COUNTIFS(joined,">="&start,joined,"<="&end,
    age,">="&LEFT(G8,FIND("-",G8)-1),
    age,"<="&RIGHT(G8,LEN(G8)-FIND("-",G8)))
    

where **start** (H4), **end** (H5), **age** (D5:D16), and **joined** (E5:E16) are [named ranges](https://exceljet.net/glossary/named-range)
. At each new row, the formula returns the count of all rows between start and end dates (inclusive) that also fall into the age ranges shown in column G.

_Note: this is a somewhat advanced formula that demonstrates how the criteria for COUNTIFS can be extended, and quite a lot of the complexity comes from having to parse the age ranges in column G. If you just want to count things between two dates, [this formula is more straightforward](https://exceljet.net/formulas/count-cells-between-dates)
._

Explanation 
------------

The goal of this example is to count rows in the data where the date joined falls between start and end dates (inclusive) and the age also falls into the age ranges seen in column G. The formula is complicated somewhat by the fact that the age range labels are actually text, so we need to extract a low and high number for each age range as a separate step.

_Note: the [named ranges](https://exceljet.net/glossary/named-range)
 shown in this example are entirely optional. They are a way to make the formula easier to enter, read, and copy._

### Count between dates

The main function used to solve this problem is [COUNTIFS](https://exceljet.net/functions/countifs-function)
. To explain how this works, we'll look first at the total seen in cell H6. This total _does not_ take into account age groups, it simply counts all records that fall between the start and end dates. The formula in H6 is:

    =COUNTIFS(joined,">="&start,joined,"<="&end)
    

COUNTIFS is configured with two range/criteria pairs: one to count join dates greater than or equal to the start date in cell H4:

    joined,">="&start // greater than or equal to start
    

and one to count join dates less than or equal to the end date in cell H5:

    joined,"<="&end // less than or equal to end
    

_Note that we are [concatenating](https://exceljet.net/glossary/concatenation)
 the operators inside the formula with the ampersand (&). The COUNTIFS function belongs to a [group of functions](https://exceljet.net/articles/excels-racon-functions)
 that use this syntax._

With this configuration, COUNTIFS returns the total records with a join date greater than or equal to the start and end dates in H4 and H5.

### Count between age range

The formula above counts records using the start and end dates, but does not take age range into account. To further restrict the count to the age ranges shown in column G, we need to add two more range/criteria pairs. The first pair restricts the count to ages _greater than or equal to_ the "low" number:

    age, ">="&LEFT(G8,FIND("-",G8)-1) // low
    

Here, we use the FIND and LEFT function to extract the low number. The [FIND function](https://exceljet.net/functions/find-function)
 returns the position of the hyphen (-) and feeds this number (minus 1) to the [LEFT function](https://exceljet.net/functions/left-function)
 as the number of characters to extract. LEFT returns zero ("0"), which is concatenated to the greater than or equal to [operator](https://exceljet.net/glossary/logical-operators)
 (>=). In the end, we have:

    age,">=0"
    

The second range/criteria pair restricts the count to ages _less than or equal to_ the "high" number in the age range:

    age,"<="&RIGHT(G8,LEN(G8)-FIND("-",G8)) // high
    

As before, we use the FIND function to locate the position of the hyphen (-). The result is subtracted from the total of all characters in the cell (calculated with the [LEN function](https://exceljet.net/functions/len-function)
) and this result is given to the [RIGHT function](https://exceljet.net/functions/right-function)
 for the number of characters to extract from the right side. RIGHT returns 20, which is concatenated to the less than or equal to operator (<=). In the end, we have:

    age,"<=20"
    

As this formula is copied down the range H8:H11, the high and low values in the age ranges are extracted and used as conditions to restrict the count , while the original date logic remains unchanged.

### With SUMPRODUCT

This problem can also be solved with the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
. To get the total in cell H6, you can use a formula like this:

    =SUMPRODUCT((joined>=start)*(joined<=end))
    

To count by age ranges, the formula in H8, copied down, is:

    =SUMPRODUCT((joined>=start)*(joined<=end)*(age>=LEFT(G8,FIND("-",G8)-1)+0)*(age<=RIGHT(G8,LEN(G8)-FIND("-",G8))+0))
    

Note when checking the age, we need to add zero to the result from the LEFT function and the RIGHT function, because these functions return text, and any text value will cause the age checks to fail. Adding zero is an easy way to convert a number represented as text into a true numeric value. This isn't necessary with COUNTIFS above, because [COUNTIFS does some kind of internal magic](https://exceljet.net/articles/excels-racon-functions)
 to evaluate numeric criteria correctly, even though the criteria is provided as text.

### TEXTBEFORE and TEXTAFTER

The new [TEXTBEFORE](https://exceljet.net/functions/textbefore-function)
 and [TEXTAFTER](https://exceljet.net/functions/textafter-function)
 functions can help simplify the formulas above, because they make it easier to parse the age range. The COUNTIFS version can be simplified to:

    =COUNTIFS(joined,">="&start,joined,"<="&end,age,">="&TEXTBEFORE(G8,"-"),age,"<="&TEXTAFTER(G8,"-"))
    

And the SUMPRODUCT version can be written as:

    =SUMPRODUCT((joined>=start)*(joined<=end)*(age>=TEXTBEFORE(G8,"-")+0)*(age<=TEXTAFTER(G8,"-")+0))
    

TEXTBEFORE and TEXTAFTER are currently available in [Excel 365](https://exceljet.net/glossary/excel-365)
 only.

Related formulas
----------------

[![Excel formula: Count cells between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20cells%20between%20dates_0.png "Excel formula: Count cells between dates")](https://exceljet.net/formulas/count-cells-between-dates)

### [Count cells between dates](https://exceljet.net/formulas/count-cells-between-dates)

In this example, the goal is to count the number of cells in column D that contain dates that are between two variable dates in G4 and G5. This problem can be solved with the COUNTIFS function or the SUMPRODUCT function, as explained below. For convenience, the worksheet contains two named ranges...

[![Excel formula: Count cells between two numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20cells%20between%20two%20numbers_0.png "Excel formula: Count cells between two numbers")](https://exceljet.net/formulas/count-cells-between-two-numbers)

### [Count cells between two numbers](https://exceljet.net/formulas/count-cells-between-two-numbers)

In this example, the goal is to count numbers that fall within specific ranges. The lower value comes from the "Start" column, and the upper value comes from the "End" column. For each range, we want to include both the lower value and the upper value. For convenience, the numbers being counted are...

[![Excel formula: Highlight values between](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20values%20between.png "Excel formula: Highlight values between")](https://exceljet.net/formulas/highlight-values-between)

### [Highlight values between](https://exceljet.net/formulas/highlight-values-between)

When you use a formula to apply conditional formatting, the formula is evaluated for each cell in the range, relative to the active cell in the selection at the time the rule is created. So, in this case, if you apply the rule to B4:G11, with B4 as the active cell, the rule is evaluated for each of...

[![Excel formula: Highlight dates between](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20dates%20between.png "Excel formula: Highlight dates between")](https://exceljet.net/formulas/highlight-dates-between)

### [Highlight dates between](https://exceljet.net/formulas/highlight-dates-between)

The AND function takes multiple arguments and returns TRUE only when all arguments return TRUE. The DATE function creates a proper Excel date with given year, month, and day values. Because the reference to B4 is fully relative, it will update as the rule is applied to each cell in the range, and...

[![Excel formula: Summary count by month with COUNTIFS](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/summary%20count%20by%20month%20with%20COUNTIFS_0.png "Excel formula: Summary count by month with COUNTIFS")](https://exceljet.net/formulas/summary-count-by-month-with-countifs)

### [Summary count by month with COUNTIFS](https://exceljet.net/formulas/summary-count-by-month-with-countifs)

In this example, we have a list of 100 issues in Columns B to D. Each issue has a date and priority. We are also using the named range dates for C5:C104 and priorities for D5:D105. Starting in column F, we have a summary table that shows a total count per month, followed by a total count per month...

Related functions
-----------------

[![Excel COUNTIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countifs_function.png "Excel COUNTIFS function")](https://exceljet.net/functions/countifs-function)

### [COUNTIFS Function](https://exceljet.net/functions/countifs-function)

The Excel COUNTIFS function returns the count of cells in a range that meet one or more conditions. Each condition is provided with a separate _range_ and _criteria_, and all conditions must be TRUE for a cell to be included in the count. COUNTIF can be used to count cells...

[![Excel FIND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20find.png "Excel FIND function")](https://exceljet.net/functions/find-function)

### [FIND Function](https://exceljet.net/functions/find-function)

The Excel FIND function returns the position (as a number) of one text string inside another. When the text is not found, FIND returns a #VALUE error.

[![Excel LEFT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20left.png "Excel LEFT function")](https://exceljet.net/functions/left-function)

### [LEFT Function](https://exceljet.net/functions/left-function)

The Excel LEFT function extracts a given number of characters from the left side of a supplied text string. For example, =LEFT("apple",3) returns "app".

[![Excel RIGHT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_right_function.png "Excel RIGHT function")](https://exceljet.net/functions/right-function)

### [RIGHT Function](https://exceljet.net/functions/right-function)

The Excel RIGHT function extracts a given number of characters from the _right_ side of a supplied text string. For example, =RIGHT("apple",3) returns "ple".

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel TEXTBEFORE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textbefore%20function.png "Excel TEXTBEFORE function")](https://exceljet.net/functions/textbefore-function)

### [TEXTBEFORE Function](https://exceljet.net/functions/textbefore-function)

The Excel TEXTBEFORE function returns the text that occurs before a given substring or delimiter. In cases where multiple delimiters appear in the text, TEXTBEFORE can return text before the nth occurrence of the delimiter.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20COUNTIFS%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-countifs-function)

### [How to use the COUNTIFS function](https://exceljet.net/videos/how-to-use-the-countifs-function)

In this video, we'll look at how to use the COUNTIFS function to count cells that meet multiple criteria. Let's take a look. In this first set of tables, we have two named ranges , "number" and "color." In column G, I'll enter a formula that satisfies the conditions in column E. The COUNTIFS...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count cells between dates](https://exceljet.net/formulas/count-cells-between-dates)
    
*   [Count cells between two numbers](https://exceljet.net/formulas/count-cells-between-two-numbers)
    
*   [Highlight values between](https://exceljet.net/formulas/highlight-values-between)
    
*   [Highlight dates between](https://exceljet.net/formulas/highlight-dates-between)
    
*   [Summary count by month with COUNTIFS](https://exceljet.net/formulas/summary-count-by-month-with-countifs)
    

### Functions

*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    
*   [FIND Function](https://exceljet.net/functions/find-function)
    
*   [LEFT Function](https://exceljet.net/functions/left-function)
    
*   [RIGHT Function](https://exceljet.net/functions/right-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [TEXTBEFORE Function](https://exceljet.net/functions/textbefore-function)
    

### Videos

*   [How to use the COUNTIFS function](https://exceljet.net/videos/how-to-use-the-countifs-function)
    

### Articles

*   [Excel's RACON functions](https://exceljet.net/articles/excels-racon-functions)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    

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