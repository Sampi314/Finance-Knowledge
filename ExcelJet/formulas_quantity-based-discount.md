# Quantity based discount - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/quantity-based-discount

---

[Skip to main content](https://exceljet.net/formulas/quantity-based-discount#main-content)

[](https://exceljet.net/formulas/quantity-based-discount#)

*   [Previous](https://exceljet.net/formulas/position-of-max-value-in-list)
    
*   [Next](https://exceljet.net/formulas/rank-and-score-with-index-and-match)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Quantity based discount
=======================

by Dave Bruns · Updated 13 Aug 2024

Related functions 
------------------

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[IFNA](https://exceljet.net/functions/ifna-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7870/download?token=IU-E5mD0)
 (16.17 KB)

![Excel formula: Quantity based discount](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/quantity_based_discount.png "Excel formula: Quantity based discount")

Summary
-------

One way to set up a quantity-based discount formula is to place the discounted items in a lookup table, then perform a two-way lookup. In the example shown, the formula in E5 is:

    =XLOOKUP(B5,item,XLOOKUP(C5,quantity,discount,0,-1),0)

Where **item** (H5:H11), **quantity** (H5:H11), and **discount** (I5:L11) are [named ranges](https://exceljet.net/glossary/named-range)
. As the formula is copied down, it references the discount table to determine the correct discount for each item and quantity.

Generic formula
---------------

    =XLOOKUP(A1,item,XLOOKUP(B1,quantity,discount,0,-1),0)

Explanation 
------------

The goal is to calculate discounts on a per-item and per-quantity basis using the discount table at the right in the workbook shown. The purpose of the discount table is to allow each item to have its own set of discounts. Notice that Donuts have a different discount for a quantity of 24. The discounts for other items can be customized as well.

This is a classic two-way lookup problem. The formula must perform an exact match on the item name and an approximate match on the quantity. Note that not all of the items listed in column C appear in the discount table. This means we also need to handle the case of the item not being found (i.e. items that do not appear in the discount table are not discounted). This problem can be solved with XLOOKUP or INDEX and MATCH. Both approaches are explained below.

_Note: This is a more advanced example. [See this page](https://exceljet.net/formulas/if-with-other-calculations)
 for a very simple quantity-based discount._

### Useful links

*   [How to use the XLOOKUP function](https://exceljet.net/functions/xlookup-function)
    
*   [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
    

### XLOOKUP solution

One way to solve this problem is with the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
. XLOOKUP is a modern and flexible replacement for older functions like VLOOKUP, and HLOOKUP. The generic syntax for XLOOKUP is:

    =XLOOKUP(lookup,lookup_array,return_array,[not_found],[match_mode],[search_mode])

In this problem, the trick is to use XLOOKUP twice: once to retrieve discount information based on the quantity and once to retrieve discount information based on the item. The screen below shows the two lookups that are required:

![There are two separate lookups required](https://exceljet.net/sites/default/files/images/formulas/inline/quantity_based_discount_2_separate_lookups.png "There are two separate lookups required")

Let's start with quantity, which is lookup #1 in the screen above. The goal is to retrieve the correct set of discounts for the quantity in column C. To do this, we use XLOOKUP like this:

    XLOOKUP(C5,quantity,discount,0,-1)

The _lookup\_value_ comes from cell C5. The _lookup\_array_ is the named range **quantity** (I4:L4). For _return\_array_, we provide the named range **discount** (I5:L11). Because we want a discount of 0% for items that do not appear in the discount table, we provide zero (0) for the _if\_not\_found_ argument. Finally, because the quantity lookup is not an exact match, we provide -1 for _match\_mode_. This tells XLOOKUP to perform an exact match when available and the next smallest item if not.

Notice that XLOOKUP will happily accept a horizontal range for _lookup\_array_ and that the _return\_array_ can be a two-dimensional range containing _all discount values_. This means that XLOOKUP will return an _entire column_ of discounts after matching a given quantity. For example, with the number 12 in cell C5, XLOOKUP returns all discounts in column K in an array like this:

    {0.1;0.1;0.1;0.1;0.1;0.1;0.1}

These decimal values correspond to the percentages seen in the range K5:K11. Because we set _match\_mode_ to -1, XLOOKUP will continue to return the same set of discounts until the quantity reaches 24. So, at this point, we have 7 discount values, but we still need to select the correct discount based on the item name. This is lookup #2 in the screen above.

_Note: It happens that all discounts for a quantity of 12 are 10%, but the table is structured to allow the discounts to be customized on a per-item basis and the formula will continue to work correctly._

To retrieve the correct discount for an item, we start off like this:

    =XLOOKUP(B5,item,

The _lookup\_value_ comes from cell B5 and the _lookup\_array_ is the named range **item** (H5:H11). Now we need to add the _return\_array_. This is where things get tricky. If we provide the named range **discount**, we'll get back all discounts in the matching row. For Lemons, the result looks like this:

    =XLOOKUP(B5,item,discount) // returns {0,0.05,0.1,0.15}

However, we don't want all of the discounts for Lemons. Instead, we want the _single_ discount associated with a quantity of 12. So, in order to get that result, we provide lookup formula #1 as the _return\_array_:

    =XLOOKUP(B5,item,XLOOKUP(C5,quantity,discount,0,-1)) // returns 0.1

Recall that the result from lookup #1 is the entire column of discounts associated with a quantity of 12. The final result is 0.1 which, when formatted as a percentage, will display as 10%. This is the correct discount for 12 Lemons.

We are nearly finished, but we have one more requirement: when an item is not found in the discount table, we should assume that there is no discount for that item. In other words, we should assume a discount of 0%. To accomplish this in XLOOKUP, we can provide zero for the _if\_not\_found_ argument. The final formula in cell E5 is:

    =XLOOKUP(B5,item,XLOOKUP(C5,quantity,discount,0,-1),0)

As the formula is copied down, it uses the discount table to find the right discount for each item and quantity. When no discount is available for a given item, it returns zero (0).

### Applying the discount

The formula in column F calculates the total price for each item and applies the discount in column E with this formula:

    =C5*D5*(1-E5) // apply discount

When the discount is zero, the quantity x price calculation is not affected.

### INDEX and MATCH option

This problem can also be solved nicely with an [INDEX and MATCH formula](https://exceljet.net/articles/index-and-match)
 like this:

    =INDEX(discount,MATCH(B5,item,0),MATCH(C5,quantity,1))

This traditional two-way lookup formula is an example of how the INDEX and MATCH can sometimes be more intuitive than using XLOOKUP twice. In a nutshell, we feed the named range **discount** into the [INDEX function](https://exceljet.net/functions/index-function)
 as the _array_ argument. For _row\_num_, we use the [MATCH function](https://exceljet.net/functions/xmatch-function)
 for an exact match on item:

    MATCH(B5,item,0) // get row num

 For _column\_num_, we use the MATCH function for an approximate match on quantity:

    MATCH(C5,quantity,1) // get column num

After the MATCH function is evaluated, we have 5 for row, and 3 for column, and INDEX returns the value at that location: 

    INDEX(discount,5,3) // returns 0.1

The result is 0.1, which will display as 10% when [formatted as a percentage](https://exceljet.net/glossary/percentage-number-format)
. This is the correct discount for 12 Lemons. Note that if the item is not found in the discount table, MATCH will return #N/A, and INDEX will return the same. To handle the case where the item is not found in the discount table (and therefore the discount should be 0%), we wrap the entire INDEX and MATCH formula inside the [IFNA function](https://exceljet.net/functions/ifna-function)
, and provide zero for _value\_if\_na_ like this:

    =IFNA(INDEX(discount,MATCH(B5,item,0),MATCH(C5,quantity,1)),0)

We could use the [IFERROR function](https://exceljet.net/functions/iferror-function)
 instead of IFNA, but IFNA is more specific and therefore a safer option in this case, since it will only trap #N/A errors. For more information about XLOOKUP versus INDEX and MATCH, [see this article](https://exceljet.net/articles/xlookup-vs-index-and-match)
.

### VLOOKUP + MATCH option

Since all discounts are in a single table with the lookup value (Item) in the first column, it is possible to use VLOOKUP + MATCH to solve this problem as well. The trick is to use the MATCH function to locate the right column number to return to VLOOKUP:

    =IFNA(VLOOKUP(B5,$H$5:$L$11,MATCH(C5,$H$4:$L$4,1),0),0)

Because VLOOKUP requires the lookup values to be part of the table, and the quantities in row 4 start in the next column, we can't use the named ranges mentioned above directly, so this formula uses [absolute references](https://exceljet.net/glossary/absolute-reference)
 instead. See a more detailed example of a VLOOKUP + MATCH formula [here](https://exceljet.net/formulas/vlookup-two-way-lookup)
.

Related formulas
----------------

[![Excel formula: XLOOKUP two-way exact match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20two-way%20exact%20match.png "Excel formula: XLOOKUP two-way exact match")](https://exceljet.net/formulas/xlookup-two-way-exact-match)

### [XLOOKUP two-way exact match](https://exceljet.net/formulas/xlookup-two-way-exact-match)

One of XLOOKUP's features is the ability to lookup and return an entire row or column. This feature can be used to nest one XLOOKUP inside another to perform a two-way lookup. The inner XLOOKUP returns a result to the outer XLOOKUP, which returns a final result. Note: XLOOKUP performs an exact...

[![Excel formula: XLOOKUP basic approximate match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20basic%20approximate%20match.png "Excel formula: XLOOKUP basic approximate match")](https://exceljet.net/formulas/xlookup-basic-approximate-match)

### [XLOOKUP basic approximate match](https://exceljet.net/formulas/xlookup-basic-approximate-match)

In the example shown, the table in B4:C13 contains quantity-based discounts. As the quantity increases, the discount also increases. The table in E4:F10 shows the discount returned by XLOOKUP for several random quantities. XLOOKUP is configured to use the quantity in column E to find the...

Related functions
-----------------

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel IFNA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_ifna_function.png "Excel IFNA function")](https://exceljet.net/functions/ifna-function)

### [IFNA Function](https://exceljet.net/functions/ifna-function)

The Excel IFNA function is a simple way to handle #N/A errors specifically without catching other errors. The IFNA function allows you to specify a custom value or message to display instead of the #N/A error. If no error #N/A error occurs the formula returns a normal result....

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Basic%20XLOOKUP%20Example-play.png)](https://exceljet.net/videos/basic-xlookup-example)

### [Basic XLOOKUP example](https://exceljet.net/videos/basic-xlookup-example)

In this video, we’ll set up the XLOOKUP function with a basic example. The XLOOKUP function is a more flexible replacement for VLOOKUP , and it's just as easy to use. In this worksheet, we have population data for some of the largest cities in the world. Let's configure the XLOOKUP function to...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Basic%20XLOOKUP%20approximate%20match-Play.png)](https://exceljet.net/videos/basic-xlookup-approximate-match)

### [Basic XLOOKUP approximate match](https://exceljet.net/videos/basic-xlookup-approximate-match)

In this video, we’ll set up the XLOOKUP function to perform an approximate match. In this worksheet, the table in B5:C9 contains quantity-based discounts. As the quantity increases, the discount also increases. Let's set up the XLOOKUP function to calculate the correct discount for each quantity...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20look%20things%20up%20with%20INDEX%20and%20MATCH-thumb.png)](https://exceljet.net/videos/how-to-look-things-up-with-index-and-match)

### [How to look things up with INDEX and MATCH](https://exceljet.net/videos/how-to-look-things-up-with-index-and-match)

In this video we're going to combine INDEX and MATCH together to look things up. Here we have the city population data we looked at before. We used the INDEX function to retrieve information about a city with a hard-coded position value. When we supply a number, INDEX retrieves information for the...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [XLOOKUP two-way exact match](https://exceljet.net/formulas/xlookup-two-way-exact-match)
    
*   [XLOOKUP basic approximate match](https://exceljet.net/formulas/xlookup-basic-approximate-match)
    

### Functions

*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [IFNA Function](https://exceljet.net/functions/ifna-function)
    

### Videos

*   [Basic XLOOKUP example](https://exceljet.net/videos/basic-xlookup-example)
    
*   [Basic XLOOKUP approximate match](https://exceljet.net/videos/basic-xlookup-approximate-match)
    
*   [How to look things up with INDEX and MATCH](https://exceljet.net/videos/how-to-look-things-up-with-index-and-match)
    

### Articles

*   [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
    

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