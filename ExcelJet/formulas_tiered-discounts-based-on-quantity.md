# Tiered discounts based on quantity - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/tiered-discounts-based-on-quantity

---

[Skip to main content](https://exceljet.net/formulas/tiered-discounts-based-on-quantity#main-content)

[](https://exceljet.net/formulas/tiered-discounts-based-on-quantity#)

*   [Previous](https://exceljet.net/formulas/textsplit-get-numeric-values)
    
*   [Next](https://exceljet.net/formulas/unique-rows)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Tiered discounts based on quantity
==================================

by Dave Bruns · Updated 22 Aug 2024

Related functions 
------------------

[MAP](https://exceljet.net/functions/map-function)

[VSTACK](https://exceljet.net/functions/vstack-function)

[DROP](https://exceljet.net/functions/drop-function)

[IF](https://exceljet.net/functions/if-function)

[MIN](https://exceljet.net/functions/min-function)

[MAX](https://exceljet.net/functions/max-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8442/download?token=0UJ3WKzn)
 (18.4 KB)

![Excel formula: Tiered discounts based on quantity](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/tiered_discounts_based_on_quantity.png "Excel formula: Tiered discounts based on quantity")

Summary
-------

To distribute a quantity into separate tiers, where each tier has a discounted price based on a threshold, you can use a formula based on the [MAP function](https://exceljet.net/functions/map-function)
. In the worksheet shown, the distributed quantities in the range D7:D13 are generated with a single formula in cell D7:

    =LET(
      quantity,C4,
      thresholds,C7:C13,
      prevthresholds,DROP(VSTACK(0,thresholds),-1),
      MAP(thresholds,prevthresholds,LAMBDA(a,b,
        IF(quantity<=b,0,
          IF(quantity>a,a-b,quantity-b))
      ))
    )
    

This formula distributes the quantity in C4 (850) into separate values using the threshold entered in C7:C13. The result is a single array that contains the quantities seen in D7:D13.

_Note: The formula above is advanced and shows how to use a function like MAP to calculate all quantities in one step. In older versions of Excel, you can use a more traditional approach, which is also explained below. The workbook attached includes both approaches._

Generic formula
---------------

    =LET(
    quantity,A1,
    thresholds,range,
    prevthresholds,DROP(VSTACK(0,thresholds),-1),
    MAP(thresholds,prevthresholds,LAMBDA(a,b,MAX(0,MIN(quantity,a)-b)))
    )

Explanation 
------------

This example shows a workbook designed to apply discounts based on seven pricing tiers. The total quantity of items is entered as a variable in cell C4. The discount is applied via the unit costs in E7:E13, which decrease as the quantity increases. The first 200 items have an undiscounted price of $1.00. The next 300 items have a discounted unit price of $0.90. The next 250 items have a unit price of $0.80, and so on.

The main challenge in this problem is calculating the correct quantities in the range D7:D13. The goal is to write a formula to distribute the quantity in C4 (850) into separate tiers based on the thresholds entered in C7:C13. Once these numbers are in place, calculating the line totals in column F is a simple matter of multiplying the quantity in column D by the unit cost in column E. 

### Understanding the problem

As mentioned above, the challenge in this example is figuring out a good way to calculate quantities per tier in the range D7:D13. Essentially, we need to distribute the quantity in cell C4 into separate "buckets" according to the thresholds given in C7:C13. We fill one bucket at a time, beginning with the first tier. Once that bucket is full, we move on to the next bucket. We continue in this way, filling up each bucket in turn until we have exhausted the quantity in cell C4. Translating this idea into cells on the worksheet, the logic we need to implement looks like this:

*   If the quantity is less than or equal to the previous threshold, we are done and the result should be 0. In other words, the current tier has not been reached.
*   If the quantity exceeds the current threshold, the result is the difference between the current and previous threshold. We subtract the previous threshold from the current threshold.
*   Otherwise, the result is the difference between the quantity and the previous threshold. We subtract the previous threshold from the quantity.

Below, I explain two ways to solve this problem. The first method keeps the worksheet structure intact and uses the MAP function to generate all tier quantities simultaneously. This method requires Excel 365. The second method restructures the worksheet and uses a more straightforward traditional formula that will work in all versions of Excel.

### MAP solution in Excel 365

The worksheet shown above uses a single formula in cell D7 to calculate all quantities in D7:D13:

    =LET(
      quantity,C4,
      thresholds,C7:C13,
      prevthresholds,DROP(VSTACK(0,thresholds),-1),
      MAP(thresholds,prevthresholds,LAMBDA(a,b,
        IF(quantity<=b,0,
          IF(quantity>a,a-b,quantity-b))
      ))
    )
    

At a high level, we use the [MAP function](https://exceljet.net/functions/map-function)
 to calculate the final result. MAP is designed to work with like-sized arrays, iterating through an array one element at a time and performing a custom calculation at each step. The formula works like this:

First, we define the variable "quantity" as equal to cell C4 and the variable "thresholds" as equal to the range C7:C13:

    quantity,C4,
    thresholds,C7:C13,

This step makes the formula easier to read and more portable since the only worksheet references occur in the first two lines. Next, we need to create an array of "previous thresholds" in order to implement the logic explained above. To do that, we define "prevthresholds" with the [VSTACK function](https://exceljet.net/functions/vstack-function)
 and the [DROP function](https://exceljet.net/functions/drop-function)
 like this:

    prevthresholds,DROP(VSTACK(0,thresholds),-1)

Working from the inside out, we first use VSTACK to insert a zero at the start of the "thresholds" array. This effectively "pushes down" the items in the array so that the current and previous thresholds are "aligned", which allows MAP to work with both values at the same time. Then, we use the DROP function to remove the final last value since we don't need it. After this code runs, we have an array that contains seven numbers:

    {0;200;500;750;1500;3000;5000}

Note this array is similar to the original threshold values, except we have a zero as the start and the last value has been removed. Next, we use the MAP function to generate the quantities per tier like this:

      MAP(thresholds,prevthresholds,LAMBDA(a,b,
        IF(quantity<=b,0,
          IF(quantity>a,a-b,quantity-b))
      ))
    

Notice the first two arguments are the arrays created in the previous steps. Next, we have a custom [LAMBDA calculation](https://exceljet.net/functions/lambda-function)
. Inside the LAMBDA, "a" is the "thresholds" array, and "b" is the "prevthresholds" array. (See our [MAP page](https://exceljet.net/functions/map-function)
 for an explanation of this structure). The logic is implemented with a nested IF formula:

    LAMBDA(a,b,
        IF(quantity<=b,0,
          IF(quantity>a,a-b,quantity-b))

*   If the quantity is less than or equal to the previous threshold, the result should be 0.
*   Otherwise, if the quantity exceeds the current threshold, subtract the previous threshold from the current threshold.
*   Otherwise, subtract the previous threshold from the quantity.

MAP iterates through each of the seven thresholds and generates a result for each tier using the logic above. The final result is an array of seven quantities, one for each tier:

    {200;300;250;100;0;0;0}

The array lands in cell D7, and the values spill into the range D7:D13.

_Note: This problem is a good example of how new functions in Excel can be used to solve hard problems neatly. However, it is also a case where choosing MAP is not obvious. The trick here is to create an array of "previous thresholds" so that current and previous values are simultaneously available. Knowing when and how to do this is part of the learning curve of new functions like MAP. I'm sure there are many ways to solve this problem with other dynamic array functions._

### MIN and MAX alternative

The logic inside the nested IF in the formula above can be "compressed" by [replacing IF](https://exceljet.net/articles/replace-ugly-ifs-with-max-or-min)
 with the MIN and MAX functions like this:

    =LET(
    quantity,C4,
    thresholds,C7:C13,
    prevthresholds,DROP(VSTACK(0,thresholds),-1),
    MAP(thresholds,prevthresholds,LAMBDA(a,b,MAX(0,MIN(quantity,a)-b)))
    )

Both formulas return the same results, but the second formula is more concise. The trade-off is that it is more difficult to understand at a glance, especially for those new to this technique.

### Traditional solution for older versions of Excel

In older versions of Excel that do not support dynamic array formulas, I recommend changing the worksheet's structure to make it easier to solve with a more traditional formula by inserting "previous threshold" values before the existing threshold values. You can see this approach in the worksheet below:

![Calculating the same results in older versions of Excel](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/tiered_discounts_based_on_quantity_legacy_excel.png "Calculating the same results in older versions of Excel")

In this worksheet, the "From" column contains previous threshold values, and the To column contains the original threshold values. The formula in cell E7, copied down, looks like this:

    =IF($C$4<=C7,0,IF($C$4>D7,D7-C7,$C$4-C7))

As the formula is copied down, it calculates the quantity for each tier, following the same logic as the MAP formula but without the dynamic array capabilities. This approach processes each row individually.

*   If the quantity is less than or equal to the previous threshold, the result should be 0.
*   Otherwise, if the quantity exceeds the current threshold, subtract the previous threshold from the current threshold.
*   Otherwise, subtract the previous threshold from the quantity.

Like the MAP formula above, we can replace the nested IF structure with a more compact formula using MAX and MIN like this:

    =MAX(0,MIN($C$4,D7)-C7)

Both formulas will return the same results.

_Note: I created this example to show how Excel's new MAP function can be used to solve tricky problems in an elegant way. Excel's new functions are very powerful, but it's often not clear how you would use a function like MAP. By the time I finished with the traditional formula approach, I was reminded yet again of the power of restructuring a worksheet to simplify a problem. Do not overlook this "one simple trick" to make hard problems easier to solve :)_

Related formulas
----------------

[![Excel formula: Quantity based discount](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/quantity_based_discount.png "Excel formula: Quantity based discount")](https://exceljet.net/formulas/quantity-based-discount)

### [Quantity based discount](https://exceljet.net/formulas/quantity-based-discount)

The goal is to calculate discounts on a per-item and per-quantity basis using the discount table at the right in the workbook shown. The purpose of the discount table is to allow each item to have its own set of discounts. Notice that Donuts have a different discount for a quantity of 24. The...

[![Excel formula: Income tax bracket calculation](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/income%20tax%20bracket%20calculation_0.png "Excel formula: Income tax bracket calculation")](https://exceljet.net/formulas/income-tax-bracket-calculation)

### [Income tax bracket calculation](https://exceljet.net/formulas/income-tax-bracket-calculation)

In this example, the goal is to calculate the total income tax owed in a progressive tax system with multiple tax brackets, as shown in the worksheet. The article below first reviews how taxes are computed in a progressive system. Next, it shows how to accomplish this task in Excel using two...

Related functions
-----------------

[![Excel MAP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exxeljet%20map%20function.png "Excel MAP function")](https://exceljet.net/functions/map-function)

### [MAP Function](https://exceljet.net/functions/map-function)

The Excel MAP function "maps" a custom LAMBDA function to each value in a supplied [array](https://exceljet.net/glossary/array)
. The LAMBDA is applied to each value, and the result from MAP is an array of results with the same dimensions as the original array.

[![Excel VSTACK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20vstack%20function.png "Excel VSTACK function")](https://exceljet.net/functions/vstack-function)

### [VSTACK Function](https://exceljet.net/functions/vstack-function)

The Excel VSTACK function combines arrays vertically into a single array. Each subsequent array is appended to the bottom of the previous array....

[![Excel DROP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20drop%20function.png "Excel DROP function")](https://exceljet.net/functions/drop-function)

### [DROP Function](https://exceljet.net/functions/drop-function)

The Excel DROP function returns a subset of a given array by "dropping" rows and columns. The number of rows and columns to remove is provided by separate _rows_ and _columns_ arguments. Rows and columns can be dropped from the start or end of the given array....

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel MIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20min%20function.png "Excel MIN function")](https://exceljet.net/functions/min-function)

### [MIN Function](https://exceljet.net/functions/min-function)

The Excel MIN function returns the smallest numeric value in the data provided. The MIN function ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel MAX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20max%20function.png "Excel MAX function")](https://exceljet.net/functions/max-function)

### [MAX Function](https://exceljet.net/functions/max-function)

The Excel MAX function returns the largest numeric value in the data provided. MAX ignores empty cells, the logical values TRUE and FALSE, and text values.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Quantity based discount](https://exceljet.net/formulas/quantity-based-discount)
    
*   [Income tax bracket calculation](https://exceljet.net/formulas/income-tax-bracket-calculation)
    

### Functions

*   [MAP Function](https://exceljet.net/functions/map-function)
    
*   [VSTACK Function](https://exceljet.net/functions/vstack-function)
    
*   [DROP Function](https://exceljet.net/functions/drop-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [MIN Function](https://exceljet.net/functions/min-function)
    
*   [MAX Function](https://exceljet.net/functions/max-function)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    
*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    

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