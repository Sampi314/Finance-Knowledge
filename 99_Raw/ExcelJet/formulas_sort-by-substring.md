# Sort by substring - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sort-by-substring

---

[Skip to main content](https://exceljet.net/formulas/sort-by-substring#main-content)

[](https://exceljet.net/formulas/sort-by-substring#)

*   [Previous](https://exceljet.net/formulas/sort-by-one-column)
    
*   [Next](https://exceljet.net/formulas/sort-by-two-columns)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Sort by substring
=================

by Dave Bruns · Updated 13 Aug 2024

Related functions 
------------------

[SORTBY](https://exceljet.net/functions/sortby-function)

[TEXTBEFORE](https://exceljet.net/functions/textbefore-function)

[TEXTAFTER](https://exceljet.net/functions/textafter-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8069/download?token=Rs256wZV)
 (22.61 KB)

![Excel formula: Sort by substring](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sort_by_substring.png "Excel formula: Sort by substring")

Summary
-------

To sort data by a substring, you can use the [SORTBY function](https://exceljet.net/functions/sortby-function)
 together with the [TEXTBEFORE](https://exceljet.net/functions/textbefore-function)
 and [TEXTAFTER](https://exceljet.net/functions/textafter-function)
 functions. In the worksheet shown, we are sorting the codes in column B by color. The formula in cell D5 is:

    =SORTBY(B5:B16,TEXTBEFORE(TEXTAFTER(B5:B16,"-"),"-"))

The result in column D is a list of the same codes sorted by color in alphabetical order.

Generic formula
---------------

    =SORTBY(range,TEXTBEFORE(TEXTAFTER(range,"-"),"-"))

Explanation 
------------

We have a list of 12 codes in Column B. Each code consists of a prefix (two letters), a color (variable), and a 4-digit number, all separated by hyphens (e.g., AX-Red-6387). The goal is to sort this list based on the color substring so that all codes with the same color are grouped together in the output in alphabetical order. The 2-letter prefix and 4-digit number should be ignored during sorting. This is a good example of a situation where the SORTBY function is necessary instead of the standard SORT function. The formula in cell D5 looks like this:

    =SORTBY(B5:B16,TEXTBEFORE(TEXTAFTER(B5:B16,"-"),"-"))

Working from the inside out, the first step is to isolate the color from the rest of the code. To do this, we use a combination of the [TEXTAFTER function](https://exceljet.net/functions/textafter-function)
 and the [TEXTBEFORE function](https://exceljet.net/functions/textbefore-function)
. First, TEXTAFTER is used to extract text that appears _after_ the first hyphen:

    TEXTAFTER(B5:B16,"-")

You can see the result in the screen below:

![Using TEXTAFTER to extract text after the first hyphen](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/sort_by_substring_TEXTAFTER_function.png "Using TEXTAFTER to extract text after the first hyphen")

The result from TEXTAFTER is delivered directly to the TEXTBEFORE function:

    =TEXTBEFORE(TEXTAFTER(B5:B16,"-"),"-")

The TEXTBEFORE function then extracts just the text that occurs _before the first hyphen_. This can be a bit confusing. The main thing to keep in mind is that TEXTBEFORE is working with the _output_ from TEXTAFTER. This means there is only _one hyphen_ at this point (see the screen above) since TEXTAFTER has already removed the other hyphen. The screen below shows the result after TEXTBEFORE runs:

![Using TEXTAFTER to isolate the color](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/sort_by_substring_TEXTBEFORE_function.png "Using TEXTAFTER to isolate the color")

At this point, we have isolated and extracted the color for each code. The final step is to use the colors to sort the original codes, which is done with the [SORTBY function](https://exceljet.net/functions/sortby-function)
, which is the outermost function:

    =SORTBY(B5:B16,TEXTBEFORE(TEXTAFTER(B5:B16,"-"),"-"))

SORTBY is configured to sort the range B5:B16 using the colors returned by TEXTBEFORE and TEXTAFTER. The final result looks like this:

![SORTBY sorts the codes by the color substring](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/sort_by_substring_SORTBY_function.png "SORTBY sorts the codes by the color substring")

### Sort by state

There are many other practical cases where the approach described above can be adapted to sort data by a substring. For example, the worksheet below shows how you can sort data in the form "City, State ZIP" by State:

![Using the same approach to sort location data by state](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/sort_by_substring_by_State.png "Using the same approach to sort location data by state")

The formula in cell D5 is very similar to the original formula above. The difference is that the delimiters have been adjusted to match the data:

    =SORTBY(B5:B16,TEXTBEFORE(TEXTAFTER(B5:B16,", ")," "))

### Sort by state and city

Since SORTBY supports sorting by more than one value, we can extend the formula above to sort by State, and then by City. The result looks like this:

![Extending the formula to sort by state and then by city](https://exceljet.net/sites/default/files/images/formulas/inline/sort_by_substring_by_state_and_city.png "Extending the formula to sort by state and then by city")

In this version, we've incorporated the [LET function](https://exceljet.net/functions/let-function)
 to keep things streamlined. The formula in cell D5 looks like this:

    =LET(
    data,B5:B16,
    states,TEXTBEFORE(TEXTAFTER(data,", ")," "),
    cities,TEXTBEFORE(data,","),
    SORTBY(data,states,1,cities,1)
    )

This is how the formula works:

1.  Open with the LET function so that we can use variables.
2.  Declare a variable named "data" and assign the range B5:B16 as the value.
3.  Declare a variable named "states" and use TEXTBEFORE and TEXTAFTER to extract just the state abbreviations. 
4.  Declare a variable named "cities" and use TEXTBEFORE to extract just the city names.
5.  Use the SORTBY function to sort **data** by **states** and then by **cities**.

This is a nice example of how the LET function can organize a more complex formula in a way that makes it easier to read and understand.

Related formulas
----------------

[![Excel formula: Sort by custom list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort%20by%20custom%20list.png "Excel formula: Sort by custom list")](https://exceljet.net/formulas/sort-by-custom-list)

### [Sort by custom list](https://exceljet.net/formulas/sort-by-custom-list)

In this example, we are sorting a table with 10 rows and 3 columns. In the range J5:J7 (the named range custom ), the colors "red", "blue", and "green" are listed in the desired sort order. The goal is to sort the table using values in the Group column in this same custom order. The SORTBY function...

Related functions
-----------------

[![Excel SORTBY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sortby_function.png "Excel SORTBY function")](https://exceljet.net/functions/sortby-function)

### [SORTBY Function](https://exceljet.net/functions/sortby-function)

The Excel SORTBY function sorts the contents of a range or array based on the values from another range or array. The range or array used to sort does not need to be in the source data or in the output.

[![Excel TEXTBEFORE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textbefore%20function.png "Excel TEXTBEFORE function")](https://exceljet.net/functions/textbefore-function)

### [TEXTBEFORE Function](https://exceljet.net/functions/textbefore-function)

The Excel TEXTBEFORE function returns the text that occurs before a given substring or delimiter. In cases where multiple delimiters appear in the text, TEXTBEFORE can return text before the nth occurrence of the delimiter.

[![Excel TEXTAFTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textafter%20function.png "Excel TEXTAFTER function")](https://exceljet.net/functions/textafter-function)

### [TEXTAFTER Function](https://exceljet.net/functions/textafter-function)

The Excel TEXTAFTER function returns the text that occurs after a given substring or delimiter. In cases where multiple delimiters appear in the text, TEXTAFTER can return text after the nth occurrence of a delimiter....

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Basic%20SORTBY%20function%20example-play.png)](https://exceljet.net/videos/basic-sortby-function-example)

### [Basic SORTBY function example](https://exceljet.net/videos/basic-sortby-function-example)

In this video, we’ll look at a basic example of sorting with the SORTBY function . In this worksheet, we have a list of names, scores, and groups. Currently, the data is not sorted. Our goal is to sort this data by group, then by score in descending order. I’ll start off by placing the cursor in...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Sort%20by%20custom%20list%20with%20SORTBY-Play.png)](https://exceljet.net/videos/sort-by-custom-list-with-sortby)

### [Sort by custom list with SORTBY](https://exceljet.net/videos/sort-by-custom-list-with-sortby)

In this video, we'll look at how to sort with SORTBY function using a custom list. One challenge that comes up frequently when sorting is a need to sort in a custom order. For example, in this worksheet, we have a list of opportunities, and we want to sort the list in the order that stages appear...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sort by custom list](https://exceljet.net/formulas/sort-by-custom-list)
    

### Functions

*   [SORTBY Function](https://exceljet.net/functions/sortby-function)
    
*   [TEXTBEFORE Function](https://exceljet.net/functions/textbefore-function)
    
*   [TEXTAFTER Function](https://exceljet.net/functions/textafter-function)
    

### Videos

*   [Basic SORTBY function example](https://exceljet.net/videos/basic-sortby-function-example)
    
*   [Sort by custom list with SORTBY](https://exceljet.net/videos/sort-by-custom-list-with-sortby)
    

### Training

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