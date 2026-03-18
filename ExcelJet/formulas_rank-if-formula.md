# Rank if formula - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/rank-if-formula

---

[Skip to main content](https://exceljet.net/formulas/rank-if-formula#main-content)

[](https://exceljet.net/formulas/rank-if-formula#)

*   [Previous](https://exceljet.net/formulas/rank-function-example)
    
*   [Next](https://exceljet.net/formulas/rank-race-results)
    

[Rank](https://exceljet.net/formulas#Rank)

Rank if formula
===============

by Dave Bruns · Updated 10 Jan 2021

Related functions 
------------------

[COUNTIFS](https://exceljet.net/functions/countifs-function)

[RANK](https://exceljet.net/functions/rank-function)

![Excel formula: Rank if formula](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/rank%20with%20criteria.png "Excel formula: Rank if formula")

Summary
-------

To rank items in a list using one or more criteria, you can use the COUNTIFS function. In the example shown, the formula in E5 is:

    =COUNTIFS(groups,C5,scores,">"&D5)+1
    

where "groups" is the [named range](https://exceljet.net/glossary/named-range)
 C5:C14, and "scores" is the named range D5:D14. The result is a rank for each person in their own group.

_Note: although data is sorted by group in the screenshot, the formula will work fine with unsorted data._

Generic formula
---------------

    =COUNTIFS(criteria_range,criteria,values,">"&value)+1

Explanation 
------------

Although Excel has a [RANK function](https://exceljet.net/functions/rank-function)
, there is no RANKIF function to perform a conditional rank. However, you can easily create a conditional RANK with the COUNTIFS function.

The COUNTIFS function can perform a conditional count using two or more criteria. Criteria are entered in range/criteria pairs. In this case, the first criteria restricts the count to the same group, using the [named range](https://exceljet.net/glossary/named-range)
 "groups" (C5:C14):

    =COUNTIFS(groups,C5) // returns 5
    

By itself, this will return total group members in group "A", which is 5.

The second criteria restricts the count to only scores greater than the "current score" from D5:

    =COUNTIFS(groups,C5,scores,">"&D5) // returns zero
    

The two criteria work together to count rows where the group is A and the score is higher. For the first name in the list (Hannah), there are no higher scores in group A, so COUNTIFS returns zero. In the next row (Edward), there are three scores in group A higher than 79, so COUNTIFS returns 3. And so on.

To get a proper rank, we simply add 1 to the number returned by COUNTIFS.

### Reversing rank order

To reverse rank order and rank in order (i.e. smallest value is ranked #1) just use the less than operator (<) instead of greater than (>):

    =COUNTIFS(groups,C5,scores,"<"&D5)+1
    

Instead of counting scores greater than D5, this version will count scores less than the value in D5, effectively reversing the rank order.

### Duplicates

Like the [RANK function](https://exceljet.net/functions/rank-function)
, the formula on this page will assign duplicate values the same rank. For example, if a specific value is assigned a rank of 3, and there are two instances of the value in the data being ranked, _both instances_ will receive a rank of 3, and the next rank assigned will be 5. To mimic the behavior of the [RANK.AVG function](https://exceljet.net/functions/rank.avg-function)
, which would assign an average rank of 3.5 in such a case, you can calculate a "correction factor" with a formula like this:

    =(COUNTIFS(groups,C5)+1-(COUNTIFS(group,C5,scores,">"&D5)+1)-(COUNTIFS(groups,C5,scores,"<"&D5)+1))/2
    

The result from this formula above can be added to the original rank to get an average rank. When a value has no duplicates, the above code returns zero and has no effect.

Related formulas
----------------

[![Excel formula: Rank function example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/rank%20function%20example1.png "Excel formula: Rank function example")](https://exceljet.net/formulas/rank-function-example)

### [Rank function example](https://exceljet.net/formulas/rank-function-example)

You can use the RANK function to rank numeric values. RANK has two modes of operation: ranking values where the largest value is #1 (order = 0), and ranking values where the lowest value is #1 (order = 1). In this case, we are ranking test scores, so the highest value should rank #1, so we omit the...

[![Excel formula: Rank race results](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/rank%20race%20results2.png "Excel formula: Rank race results")](https://exceljet.net/formulas/rank-race-results)

### [Rank race results](https://exceljet.net/formulas/rank-race-results)

You can use the RANK function to rank numeric values. RANK has two modes of operation: ranking values so that the largest value is ranked #1 (order = 0), and ranking values so that the smallest value is #1 (order = 1). In this case, we are ranking race times. The lowest/fastest value should rank #1...

[![Excel formula: nth largest value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/nth_largest_value.png "Excel formula: nth largest value")](https://exceljet.net/formulas/nth-largest-value)

### [nth largest value](https://exceljet.net/formulas/nth-largest-value)

In this example, the goal is to extract the top 3 quiz scores for each name from the 5 scores that appear in columns C, D, E, F, and G. In other words, for each name listed, we want the best score, the 2nd best score, and the 3rd best score. This problem can be solved with the LARGE function. Note...

[![Excel formula: Rank without ties](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/rank%20without%20ties.png "Excel formula: Rank without ties")](https://exceljet.net/formulas/rank-without-ties)

### [Rank without ties](https://exceljet.net/formulas/rank-without-ties)

This formula breaks ties with a simple approach: this first tie in a list "wins" and is assigned the higher rank. The first part of the formula uses the RANK function normally: =RANK(C5,points) Rank returns a computed rank, which will include ties when the values being ranked include duplicates...

[![Excel formula: Break ties with helper column and COUNTIF](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/break%20ties%20with%20helper%20column%20and%20COUNTIF.png "Excel formula: Break ties with helper column and COUNTIF")](https://exceljet.net/formulas/break-ties-with-helper-column-and-countif)

### [Break ties with helper column and COUNTIF](https://exceljet.net/formulas/break-ties-with-helper-column-and-countif)

In this example, the goal is to retrieve information about the lowest three estimates in the data shown. The problem is that there are some duplicate values in the estimate column. This means we will have some trouble trying to display the names of the 2nd and 3rd lowest suppliers because the tie...

Related functions
-----------------

[![Excel COUNTIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countifs_function.png "Excel COUNTIFS function")](https://exceljet.net/functions/countifs-function)

### [COUNTIFS Function](https://exceljet.net/functions/countifs-function)

The Excel COUNTIFS function returns the count of cells in a range that meet one or more conditions. Each condition is provided with a separate _range_ and _criteria_, and all conditions must be TRUE for a cell to be included in the count. COUNTIF can be used to count cells...

[![Excel RANK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_rank_0.png "Excel RANK function")](https://exceljet.net/functions/rank-function)

### [RANK Function](https://exceljet.net/functions/rank-function)

The Excel RANK function returns the rank of a numeric value when compared to a list of other numeric values. RANK can rank values from largest to smallest (i.e. top sales) as well as smallest to largest (i.e. fastest time).

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20rank%20values%20with%20the%20RANK%20function.png)](https://exceljet.net/videos/how-to-rank-values-with-the-rank-function)

### [How to rank values with the RANK function](https://exceljet.net/videos/how-to-rank-values-with-the-rank-function)

In this video we'll look at how to rank values in ascending or descending order using the RANK function . Here we have a table that contains five test scores for a group of students and an average score in Column I. How can we rank these students from highest to lowest scores? Well, one option is...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Rank function example](https://exceljet.net/formulas/rank-function-example)
    
*   [Rank race results](https://exceljet.net/formulas/rank-race-results)
    
*   [nth largest value](https://exceljet.net/formulas/nth-largest-value)
    
*   [Rank without ties](https://exceljet.net/formulas/rank-without-ties)
    
*   [Break ties with helper column and COUNTIF](https://exceljet.net/formulas/break-ties-with-helper-column-and-countif)
    

### Functions

*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    
*   [RANK Function](https://exceljet.net/functions/rank-function)
    

### Videos

*   [How to rank values with the RANK function](https://exceljet.net/videos/how-to-rank-values-with-the-rank-function)
    

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