# INDEX and MATCH two-column lookup - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/index-and-match-two-column-lookup

---

[Skip to main content](https://exceljet.net/formulas/index-and-match-two-column-lookup#main-content)

[](https://exceljet.net/formulas/index-and-match-two-column-lookup#)

*   [Previous](https://exceljet.net/formulas/index-and-match-on-multiple-columns)
    
*   [Next](https://exceljet.net/formulas/index-and-match-with-multiple-criteria)
    

[Lookup](https://exceljet.net/formulas#Lookup)

INDEX and MATCH two-column lookup
=================================

by Dave Bruns · Updated 29 Apr 2025

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[XMATCH](https://exceljet.net/functions/xmatch-function)

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[CHOOSECOLS](https://exceljet.net/functions/choosecols-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7918/download?token=RcPVkV3L)
 (15.24 KB)

![Excel formula: INDEX and MATCH two-column lookup](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/INDEX_and_MATCH_two-column_lookup.png "Excel formula: INDEX and MATCH two-column lookup")

Summary
-------

To create a lookup formula that returns two columns from the source data, you can use an [INDEX and MATCH formula](https://exceljet.net/articles/index-and-match)
. In the example shown, the formulas in K11 and K12 are, respectively: 

    =INDEX(data,XMATCH(K6,code),XMATCH(K7,size)) // width
    =INDEX(data,XMATCH(K6,code),XMATCH(K7,size)+1) // height

Where **data** (C6:H16), **code** (B6:B16), and **size** (C4:H4) are [named ranges](https://exceljet.net/glossary/named-range)
. With "A5" in cell K6, and "Medium" in cell K7, the first formula returns a Width of 1.5 and the second formula returns a Length of 7.5. When the inputs for code (K6) or size (K7) are changed, the formulas calculate a new result.

_Notes: (1) the values in row 4 are not merged cells but instead use "Center across selection" alignment as explained below. (2) It is possible to use the_ [_XLOOKUP function_](https://exceljet.net/functions/xlookup-function)
 _as well. See below for details._

Generic formula
---------------

    =INDEX(data,XMATCH(A1,array),XMATCH(array,array))

Explanation 
------------

In this example, the goal is to look up Width and Length based on inputs for Code (K6) and Size (K7). While finding the correct row based on the Code value is straightforward, the problem of how to best retrieve both columns of data (Width and Length) is more challenging. One good way to solve this problem is with an INDEX and MATCH formula, but you can also use XLOOKUP as explained below. For convenience, **data** (C6:H16), **code** (B6:B16), and **size** (C4:H4) are [named ranges](https://exceljet.net/glossary/named-range)
.

_Note: If you are new to INDEX with MATCH, see this overview:_ [_How to use INDEX and MATCH_](https://exceljet.net/articles/index-and-match)
_._

### Heading configuration

One important detail in this problem is that the Size information in row 4 is configured in a special way. The values "Small", "Medium", and "Large" appear in cells C1, E1, and G1, respectively. The cells in row 4 are _not_ merged. To show each Size centered over the two columns for Width and Length, the Horizontal Alignment is set to Center Across Selection as seen below:

![Heading use Center Across Selection](https://exceljet.net/sites/default/files/images/formulas/inline/INDEX_and_MATCH_two-column_lookup_setup.png "Heading use Center Across Selection")

This is important because we need to match the correct size, which must correspond to the six columns of data. In other words, when we match "Medium", we need to get a reference to column 3, as explained in more detail below. Note that this means some cells in row 4 are blank, but this doesn't matter as long as we use an exact match setting for MATCH or XMATCH.

### Two-way INDEX and MATCH

Essentially, this formula uses a standard [two-way INDEX and MATCH formula](https://exceljet.net/formulas/two-way-lookup-with-index-and-match)
. The INDEX function is provided with the data to return, and the MATCH function is used two times. The first MATCH calculates the correct row number, and the second MATCH calculates the correct column number(s). The generic syntax looks like this:

    =INDEX(data,XMATCH(),XMATCH())

_Note: We are using XMATCH in this example because the configuration is slightly simpler since XMATCH defaults to an exact match, so there is no need to provide match\_type. However,_ t_he regular MATCH function will work fine as well._

In the worksheet shown, the specific formula used in cell K11 is:

    =INDEX(data,XMATCH(K6,code),XMATCH(K7,size))

Working from the inside out, the first [XMATCH function](https://exceljet.net/functions/xmatch-function)
 returns a row based on the code in cell K6:

    XMATCH(K6,code) // returns 5

Because "A5" is the fifth value in **code** (B6:B16), the first XMATCH function returns 5. The second XMATCH function is used to find the correct column, like this:

    XMATCH(K7,size) // returns 3

Because "Medium" is the third value in **size** (C4:H4), the MATCH function returns 3. After simplifying the formula to show the results returned by XMATCH, we have the following:

    =INDEX(data,5,3) // returns 1.5

INDEX then retrieves the value at row 5 and column 3 in **data** (C6:H16), which is 1.5. The formula to return the Length in cell K12 is almost exactly the same:

    =INDEX(data,XMATCH(K6,code),XMATCH(K7,size)+1)

Notice the only difference is that we are adding 1 to the column number. The result is that we retrieve the value in the _next column_, which holds the value for Length. The formula works like this:

    =INDEX(data,5,3+1)
    =INDEX(data,5,4)
    =7.5

### With the MATCH function

As mentioned above, you can use the regular MATCH function instead of XMATCH, but you must provide 0 for _match\_type_ to enable an exact match like this:

    =INDEX(data,MATCH(K6,code,0),MATCH(K7,size,0))
    =INDEX(data,MATCH(K6,code,0),MATCH(K7,size,0)+1)

For more details, see [How to use the MATCH function](https://exceljet.net/functions/match-function)
.

### Single formula

You can modify the formula slightly to return both Width and Length at the same time:

    =INDEX(data,XMATCH(K6,code),XMATCH(K7,size)+{0;1})

Notice the only change is to replace 1 with the [array constant](https://exceljet.net/glossary/array-constant)
 {0;1}. The formula now evaluates like this:

    =INDEX(data,5,3+{0;1})
    =INDEX(data,5,{3;4})
    ={1.5;7.5}

By adding 0 and 1 to the column number returned by XMATCH, we end up with two numbers in an array {3;4} that are provided to the [INDEX function](https://exceljet.net/functions/index-function)
 as _column\_num_. The result is that INDEX returns values from both columns, and these values [spill](https://exceljet.net/glossary/spill)
 into the range K11:K12 when using a [current version of Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
.

You might notice that we provided the array constant as {0;1} and not {1,0}. By providing the values in _rows_, we get back a _vertical array_. If we used {1,0} instead, we would get a _horizontal array_ and would need to use the [TRANSPOSE function](https://exceljet.net/functions/transpose-function)
 to flip the orientation of the final result.

### XLOOKUP

This problem can also be solved with the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
, but the formula is not quite as straightforward. We start by configuring XLOOKUP to match the code like this:

    =XLOOKUP(K6,code,data)

This formula will return the entire row of widths and lengths for the code entered in K6. Next, we can [nest](https://exceljet.net/glossary/nesting)
 this formula inside a second XLOOKUP, which has been configured to retrieve the size:

    =XLOOKUP(K7,size,XLOOKUP(K6,code,data))

The inner XLOOKUP retrieves all the values for "A5" in an array, and the outer XLOOKUP selects the correct value for Width based on a size of "Medium" (1.5). However, getting the Length is more challenging because we can't just add 1 as we did with INDEX and MATCH above. Instead of nesting one XLOOKUP inside another, I think a better approach is to use the XLOOKUP together with XMATCH and the newer [CHOOSECOLS function](https://exceljet.net/functions/choosecols-function)
 like this:

    =CHOOSECOLS(XLOOKUP(K6,code,data),XMATCH(K7,size)) // width
    =CHOOSECOLS(XLOOKUP(K6,code,data),XMATCH(K7,size)+1) // length

As before, the inner XLOOKUP retrieves all the values for the code in K6 in an array. This time, however, the array is returned to the CHOOSECOLS function, which uses XMATCH to select the Width based on the size in K7. As in the original example above, XMATCH matches on size and returns a column number. CHOOSECOLS then returns the specified column. Because CHOOSECOLS uses a numeric index for a column, we can simply add 1 to the first formula to get Length, just as we did in the INDEX and MATCH formula above.

This works fine, and it's a nice demonstration of how CHOOSECOLS can make it possible to use a numeric index for columns. However, we now have three functions in the mix, and I don't see any advantage to using XLOOKUP in this case. Let me know if you disagree!

_Note: because XLOOKUP returns a valid reference, we could use the_ [_OFFSET function_](https://exceljet.net/functions/offset-function)
 _to return both Width and Length at the same time by expanding the reference by one column. But OFFSET is a_ [_volatile function,_](https://exceljet.net/glossary/volatile-function)
 _so I avoid using it when possible._

### XLOOKUP vs INDEX and MATCH

This problem illustrates a key difference between XLOOKUP and INDEX and MATCH. Because INDEX and MATCH formulas use a _numeric index_ for both rows and columns, it is easy to modify these values before they are used in the INDEX function. XLOOKUP, on the other hand, deals with _ranges_. To make column ranges dynamic, you sometimes need to use another function like CHOOSECOLS. Both XLOOKUP and INDEX and MATCH offer flexibility and functionality for manipulating and retrieving data, but your choice between them will depend on the specific needs of your project.

> For an in-depth comparison, see [XLOOKUP vs INDEX and MATCH](https://exceljet.net/articles/xlookup-vs-index-and-match)

Related formulas
----------------

[![Excel formula: Two-way lookup with INDEX and MATCH](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/two-way%20lookup%20with%20INDEX%20and%20MATCH.png "Excel formula: Two-way lookup with INDEX and MATCH")](https://exceljet.net/formulas/two-way-lookup-with-index-and-match)

### [Two-way lookup with INDEX and MATCH](https://exceljet.net/formulas/two-way-lookup-with-index-and-match)

In this example, the goal is to perform a two-way lookup, sometimes called a matrix lookup . This means we need to create a match on both rows and columns and return the value at the intersection of this two-way match The core of this formula is INDEX, which is simply retrieving a value from C6:G10...

[![Excel formula: INDEX and MATCH with variable columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX_and_MATCH_with_variable_columns.png "Excel formula: INDEX and MATCH with variable columns")](https://exceljet.net/formulas/index-and-match-with-variable-columns)

### [INDEX and MATCH with variable columns](https://exceljet.net/formulas/index-and-match-with-variable-columns)

In this example, the goal is to demonstrate how an INDEX and (X)MATCH formula can be set up so that the columns returned are variable. This approach illustrates one benefit of the 2-step process used by INDEX and MATCH: Because INDEX expects a numeric index for row and column numbers, it is easy to...

[![Excel formula: Step-based lookup example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/step-based_lookup_example.png "Excel formula: Step-based lookup example")](https://exceljet.net/formulas/step-based-lookup-example)

### [Step-based lookup example](https://exceljet.net/formulas/step-based-lookup-example)

This worksheet demonstrates a clever way to look up prices that change based on a selected tier. Imagine a pricing system where the cost of a product depends on both the product color and a tier (e.g., "Bronze," "Silver," or "Gold"). The challenge is to pull the correct price based on both inputs...

Related functions
-----------------

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel XMATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xmatch_function.png "Excel XMATCH function")](https://exceljet.net/functions/xmatch-function)

### [XMATCH Function](https://exceljet.net/functions/xmatch-function)

The Excel XMATCH function performs a lookup and returns a _position_ of a value in a range. It is a more robust and flexible successor to the MATCH function. XMATCH supports approximate and exact matching, reverse search, and wildcards (\* ?) for partial matches. ...

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

[![Excel CHOOSECOLS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20choosecols%20function.png "Excel CHOOSECOLS function")](https://exceljet.net/functions/choosecols-function)

### [CHOOSECOLS Function](https://exceljet.net/functions/choosecols-function)

The Excel CHOOSECOLS function returns specific columns from an array or range. The columns to return are provided as numbers in separate arguments. Each number corresponds to the numeric index of a column in the given array.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Basic%20XLOOKUP%20Example-play.png)](https://exceljet.net/videos/basic-xlookup-example)

### [Basic XLOOKUP example](https://exceljet.net/videos/basic-xlookup-example)

In this video, we’ll set up the XLOOKUP function with a basic example. The XLOOKUP function is a more flexible replacement for VLOOKUP , and it's just as easy to use. In this worksheet, we have population data for some of the largest cities in the world. Let's configure the XLOOKUP function to...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20do%20a%20two-way%20lookup%20with%20INDEX%20and%20MATCH-thumb.png)](https://exceljet.net/videos/how-to-do-a-two-way-lookup-with-index-and-match)

### [How to do a two-way lookup with INDEX and MATCH](https://exceljet.net/videos/how-to-do-a-two-way-lookup-with-index-and-match)

In this video we'll look at how to set up a classic two-way lookup using INDEX and MATCH . Here we have a list of salespeople with monthly sales figures. What we want to do is add a formula in Q6 that looks up and retrieves a sales number based on the name and month above. To do this, we'll use the...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Two-way lookup with INDEX and MATCH](https://exceljet.net/formulas/two-way-lookup-with-index-and-match)
    
*   [INDEX and MATCH with variable columns](https://exceljet.net/formulas/index-and-match-with-variable-columns)
    
*   [Step-based lookup example](https://exceljet.net/formulas/step-based-lookup-example)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [XMATCH Function](https://exceljet.net/functions/xmatch-function)
    
*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [CHOOSECOLS Function](https://exceljet.net/functions/choosecols-function)
    

### Videos

*   [Basic XLOOKUP example](https://exceljet.net/videos/basic-xlookup-example)
    
*   [How to do a two-way lookup with INDEX and MATCH](https://exceljet.net/videos/how-to-do-a-two-way-lookup-with-index-and-match)
    

### Articles

*   [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
    
*   [XLOOKUP vs INDEX and MATCH](https://exceljet.net/articles/xlookup-vs-index-and-match)
    

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