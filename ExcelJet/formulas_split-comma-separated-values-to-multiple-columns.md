# Split comma-separated values to multiple columns - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns

---

[Skip to main content](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns#main-content)

[](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns#)

*   [Previous](https://exceljet.net/formulas/sort-comma-separated-values)
    
*   [Next](https://exceljet.net/formulas/split-dimensions-into-three-parts)
    

[Text](https://exceljet.net/formulas#Text)

Split comma-separated values to multiple columns
================================================

by Dave Bruns · Updated 12 Oct 2025

Related functions 
------------------

[TEXTSPLIT](https://exceljet.net/functions/textsplit-function)

[REDUCE](https://exceljet.net/functions/reduce-function)

[LAMBDA](https://exceljet.net/functions/lambda-function)

[DROP](https://exceljet.net/functions/drop-function)

[FILTERXML](https://exceljet.net/functions/filterxml-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/9360/download?token=gUBs_i8J)
 (36.56 KB)

![Excel formula: Split comma-separated values to multiple columns](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/split-comma-separated-values.png "Excel formula: Split comma-separated values to multiple columns")

Summary
-------

To split comma-separated values (CSV) into multiple columns with a formula, you can use the [TEXTSPLIT function](https://exceljet.net/functions/textsplit-function)
. In the example below, we use TEXTSPLIT together with [REDUCE](https://exceljet.net/functions/reduce-function)
 and [VSTACK](https://exceljet.net/functions/vstack-function)
 to split all comma-separated values in column B into multiple columns in one step. The formula in cell D5 looks like this:

    =DROP(REDUCE("",B5:B15,LAMBDA(a,v,VSTACK(a,TEXTSPLIT(v,",")))),1)
    

Because there are 5 values in each row, the result is a horizontal array of separate values that [spills](https://exceljet.net/glossary/spill)
 across 5 columns in the range D5:H15. The REDUCE function is needed to allow TEXTSPLIT to process all 11 values in column B at once. See below for a much simpler formula to process one row at a time.

> This is a formula-based solution. If you don't want to use a formula, you can use Excel's [Text-to-Columns](https://exceljet.net/glossary/text-to-columns)
>  feature, which is a one-off manual process. If you need more automation, or are working with larger sets of data, possibily split across many files, [Power Query](https://exceljet.net/glossary/power-query)
>  is a better solution.

Generic formula
---------------

    =TEXTSPLIT(A1,",")

Explanation 
------------

In this example, the goal is to split comma-separated values (CSV) in column B into multiple columns, as seen in the worksheet shown. Each text string in column B contains 5 fields separated by commas, so we expect to get 5 columns of data as a result. The header row in column D is manually entered.

> One disadvantage of the TEXTSPLIT + REDUCE + VSTACK formula featured in this article is that it is somewhat complex. See below for a [TEXTSPLIT + TEXTJOIN alternative](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns#textsplit-with-textjoin-alternative)
>  formula that is much simpler, but note that it will fail on large sets of data.

### Table of Contents

*   [How TEXTSPLIT works](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns#how-textsplit-works)
    
*   [TEXTSPLIT to split one row](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns#textsplit-to-split-one-row)
    
*   [TEXTSPLIT with REDUCE to split all rows](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns#textsplit-with-reduce-to-split-all-rows)
    
*   [TEXTSPLIT with a dynamic range](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns#textsplit-with-a-dynamic-range)
    
*   [Choose specific columns](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns#choose-specific-columns)
    
*   [TEXTSPLIT with TEXTJOIN alternative](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns#textsplit-with-textjoin-alternative)
    
*   [Formula for Legacy Excel](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns#formula-for-legacy-excel)
    
*   [Extract nth field](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns#extract-nth-field)
    
*   [Text-to-columns alternative](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns#text-to-columns-alternative)
    

### How TEXTSPLIT works

The core of the solution is the TEXTSPLIT function, which is designed to split delimited text strings into multiple columns or rows. For example, if we give TEXTSPLIT a string like "red,blue,green", and provide a comma (",") as the column delimiter, it will return an array that contains three values:

    =TEXTSPLIT("red,blue,green",",") // returns {"red","blue","green"}
    

Because we provided a comma (",") as the _column delimiter_, TEXTSPLIT splits the text string into a _horizontal array_ of values. When this array is returned to the worksheet, it spills into _multiple columns_.

> For more details on how TEXTSPLIT works, see our [TEXTSPLIT function page](https://exceljet.net/functions/textsplit-function)
> .

### TEXTSPLIT to split one row

Before we look at how TEXTSPLIT can be configured to process a range of values, let's see how we can use TEXTSPLIT to split a _single row_ of comma-separated values. In the worksheet shown, the text in cell B5 is "Jim,Brown,33,Seattle,WA". To split this text into five separate values, we can use the following formula in cell D5:

    =TEXTSPLIT(B5,",")
    

Although TEXTSPLIT can take up to six separate [arguments](https://exceljet.net/glossary/function-argument)
, in this case, we only need to provide the first two arguments, _text_ and _col\_delimiter_. Notice we must provide the comma as [text](https://exceljet.net/glossary/text-value)
 surrounded by double quotes (","). The result is a horizontal array with five values like this:

    {"Jim","Brown","33","Seattle","WA"}
    

This array is returned to cell D5. Because the comma has been provided as the _column delimiter_, the five values [spill](https://exceljet.net/glossary/spill)
 into the range D5:H5:

![Split a single row of comma-separated values with TEXTSPLIT](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/split-comma-separated-values-single-row.png "Split a single row of comma-separated values with TEXTSPLIT")

When we copy the formula down to cell D15, we have results for all 11 rows split into comma-separated values into multiple columns:

![Split a all rows of comma-separated values with copy paste](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/split-comma-separated-values-all-rows.png "Split a all rows of comma-separated values with copy paste")

At this point, you might think we can simply give TEXTSPLIT a range of values to process all rows at the same time. Like this:

    =TEXTSPLIT(B5:B15,",")
    

However, due to a limitation in Excel, this won't work. Excel will not allow a formula to return an [array of arrays](https://exceljet.net/glossary/array-of-arrays)
. Instead, Excel will truncate the results to the first value only:

![TEXTSPLIT fails when given a range](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/split-comma-separated-values-all-rows-textsplit-fail.png "TEXTSPLIT fails when given a range")

To make a formula that will process all rows at the same time, we need to upgrade the formula significantly.

> There is no requirement to process all rows at the same time. Setting up the formula to handle one row at a time is much simpler, but it does require copying the formula down to each row.

### TEXTSPLIT with REDUCE to split all rows

One way to make Excel process all comma-separated values in column B at the same time is to use the REDUCE function in a formula like this:

    =DROP(REDUCE("",B5:B15,LAMBDA(a,v,VSTACK(a,TEXTSPLIT(v,",")))),1)
    

When we enter this formula in cell D5, all results are returned in one go:

![Splitting all rows with a formula using TEXTSPLIT and REDUCE](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/split-comma-separated-values-reduce-and-textsplit.png "Splitting all rows with a formula using TEXTSPLIT and REDUCE")

This is a pretty advanced formula, so let's work through it step-by-step. At a high level, we use the [REDUCE function](https://exceljet.net/functions/reduce-function)
 to loop through the text values in B5:B15 one by one. For each new value, we apply the [TEXTSPLIT function](https://exceljet.net/functions/textsplit-function)
 to split each comma-separated value and use the VSTACK function to stack the results vertically. REDUCE works by applying a custom [LAMBDA function](https://exceljet.net/functions/lambda-function)
 to each value in a given array, and it accumulates results to a single value. The generic syntax looks like this:

    REDUCE(initial_value,array,lambda(a,v,calculation))
    

The `a` is the accumulator (the running result), and `v` is each value in the array. These values are passed into the LAMBDA by REDUCE for each iteration. The actual work is done by the LAMBDA function, which is configured like this:

    LAMBDA(a,v,VSTACK(a,TEXTSPLIT(v,",")))
    

As REDUCE loops through the range, the LAMBDA function splits each value `v` with TEXTSPLIT:

    TEXTSPLIT(v,",") // split value by comma
    

And then adds the result to the accumulating results `a` with the VSTACK function:

    VSTACK(a,TEXTSPLIT(v,",")) // stack results vertically
    

Because the REDUCE function has been configured to start with an empty text string (""):

    REDUCE("",B5:B15,LAMBDA(...))
    

We will end up with an extra blank row at the top of our results. To remove this blank row, we use the [DROP function](https://exceljet.net/functions/drop-function)
:

    DROP(REDUCE(...),1)
    

DROP removes the first row from the array returned by REDUCE. The final result is a single array that contains 11 rows, just like the source data column B. This array lands in cell D5 and spills into the range D5:H15.

> The reason this formula works is that the REDUCE function returns a _single array_, instead of an array of arrays. The final array is built up one row at a time using the VSTACK function as REDUCE loops over the values.

### TEXTSPLIT with a dynamic range

Because the REDUCE version of the formula is much more complicated than the original text split formula above, you might wonder — why bother? One answer is that this formula will work with any number of rows. In other words, you can feed a dynamic range into this formula, and the results will expand to include all values in the range. For example, we can adjust the formula to use a dynamic range by adding the [TRIMRANGE function](https://exceljet.net/functions/trimrange-function)
 like this:

    =DROP(REDUCE("",TRIMRANGE(B5:B1000),LAMBDA(a,v,VSTACK(a,TEXTSPLIT(v,",")))),1)
    

Or we can use the [dot operator syntax](https://exceljet.net/functions/trimrange-function#alternative-syntax-with-the-dot-operator)
 like this:

    =DROP(REDUCE("",B5:.B1000,LAMBDA(a,v,VSTACK(a,TEXTSPLIT(v,",")))),1)
    

In both cases, the range provided to reduce will expand to include new values added up to row 1000. You can see how this works below, where I have adjusted the formula to use the dot operator syntax and added a new comma-separated text value to cell B16:

![TEXTSPLIT with a dynamic range](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/split-comma-separated-values-dynamic-range.png "TEXTSPLIT with a dynamic range")

Notice the range provided to REDUCE is now `B5:.B1000`, which expands to include new values added up to row 1000. All empty trailing rows are automatically removed from the range before it is passed to REDUCE.

### Choose specific columns

If you only want specific columns from the CSV you can easily adjust the formula to include the [CHOOSECOLS function](https://exceljet.net/functions/choosecols-function)
. For example, to get just the first name, state, and age, you can use a formula like this

    =LET(
    rng,B5:.B1000,
    result,DROP(REDUCE("",rng,LAMBDA(a,v,VSTACK(a,TEXTSPLIT(v,",")))),1),
    CHOOSECOLS(result,{1,5,3})
    )
    

Here, we've adjusted the formula to use the [LET function](https://exceljet.net/functions/let-function)
 in order to define two variables: `rng` and `result`. The `rng` variable is the range of values to process, and `result` is the array of results from the REDUCE function. We then use the CHOOSECOLS function to select only columns 1, 5, and 3 from the result array. Notice we are using the dynamic range syntax explained in the previous section, so the results will expand if new values are added. Also, we have reordered the columns by passing the array {1,5,3} to CHOOSECOLS:

    CHOOSECOLS(result,{1,5,3})

Here is the final result:

![Choosing specific columns to return with CHOOSECOLS](https://exceljet.net/sites/default/files/images/formulas/inline/split-comma-separated-values-choose-specific-columns.png "Choosing specific columns to return with CHOOSECOLS")

### TEXTSPLIT with TEXTJOIN alternative

A different and simpler way to approach this problem is to use a formula based on TEXTSPLIT and TEXTJOIN:

    =TEXTSPLIT(TEXTJOIN(";",,B5:B15),",",";")

![Alternative formula based on TEXTJOIN and TEXTSPLIT](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/split-comma-separated-values-textjoin-and-textsplit.png "Alternative formula based on TEXTJOIN and TEXTSPLIT")

This is a clever approach that relies on TEXTSPLIT's ability to split text into rows and columns at the same time. Basically, we use the [TEXTJOIN function](https://exceljet.net/functions/textjoin-function)
 first to [concatenate](https://exceljet.net/glossary/concatenation)
 all values in the range using a semicolon (";") as the delimiter. Then we feed the concatenated text into the TEXTSPLIT function, which is configured to use a comma (",") for the column delimiter and a semicolon (";") for the row delimiter. TEXTSPLIT then splits the concatenated text into rows and columns at the same time. This works great, and the formula runs quickly. However, there is an important limitation. 

Excel cells have a hard limit of 32,767 characters, and if TEXTJOIN produces a result that exceeds this limit, it returns a #CALC! error, which causes the formula to fail. What this means is that if you have a lot of data, the formula may not work. At some point, as the range expands and/or the number of CSV fields increases, the character count of the concatenated text will exceed 32,767, and the formula will return an error. The TEXTSPLIT + REDUCE + VSTACK formula will continue to work on larger data sets, but it will slow down.

The bottom line? TEXTSPLIT + TEXTJOIN is a compact and elegant formula that leverages TEXTSPLIT's ability to split text into 2d arrays. It works great on smaller data sets, but it will fail on large data sets.

### Formula for Legacy Excel

> Note: Before TEXTSPLIT, you could use a hacky workaround formula based on the FILTERXML function to split comma-separated values into multiple columns. This approach doesn't make any sense to use today. However, I'm leaving it here for reference as a reminder of how complicated things used to be before the introduction of [dynamic arrays](https://exceljet.net/glossary/dynamic-array)
> , [spills](https://exceljet.net/glossary/spill)
>  and [TEXTSPLIT](https://exceljet.net/functions/textsplit-function)
> . This approach only works in Windows versions of Excel, since the Mac version of Excel does not have the FILTERXML function.

In older versions of Excel without TEXTSPLIT, you can use a more complicated formula based on the [FILTERXML function](https://exceljet.net/functions/filter-function)
 with help from the [SUBSTITUTE](https://exceljet.net/functions/substitute-function)
 and [TRANSPOSE](https://exceljet.net/functions/transpose-function)
 functions. The formula looks like this:

    =TRANSPOSE(FILTERXML("<x><y>"&SUBSTITUTE(B5,",","</y><y>")&"</y></x>","//y"))
    

![Splitting comma-separated text with FILTERXML function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/split_text_to_array_filterxml_option.png "Splitting comma-separated text with FILTERXML function")

To use FILTERXML, we need [XML](https://en.wikipedia.org/wiki/XML#:~:text=Extensible%20Markup%20Language%20(XML)%20is,free%20open%20standards%E2%80%94define%20XML.)
, so the first task is to add XML markup to the text. We are going to arbitrarily make each field in the text an element, enclosed with a parent element. We start with the [SUBSTITUTE function](https://exceljet.net/functions/substitute-function)
 here:

    SUBSTITUTE(B5,",","</y><y>")
    

The result from SUBSTITUTE is a text string like this:

    "Jim</y><y>Brown</y><y>33</y><y>Seattle</y><y>WA"
    

To ensure well-formed XML tags and to wrap all elements in a parent element, we prepend and append more XML tags like this:

    "<x><y>"&SUBSTITUTE(B5,",","</y><y>")&"</y></x>"
    

This yields a text string like this (line breaks added for readability)

    "<x>
    <y>Jim</y>
    <y>Brown</y>
    <y>33</y>
    <y>Seattle</y>
    <y>WA</y>
    </x>"
    

This text is delivered directly to the FILTERXML function as the _xml_ argument, with an Xpath expression of "//y":

    FILTERXML("<x><y>Jim</y><y>Brown</y><y>33</y><y>Seattle</y><y>WA</y></x>","//y")
    

Xpath is a parsing language and "//y" selects all elements. The result from FILTERXML is a vertical array like this:

    {"Jim";"Brown";33;"Seattle";"WA"}
    

Because we want a horizontal array in this instance, we wrap the [TRANSPOSE function](https://exceljet.net/functions/transpose-function)
 around FILTERXML:

    =TRANSPOSE({"Jim";"Brown";33;"Seattle";"WA"})
    

The result is a horizontal array like this:

    {"Jim","Brown",33,"Seattle","WA"}
    

In older versions of Excel, you can enter this formula as a [multi-cell array formula](https://exceljet.net/glossary/multi-cell-array-formula)
 in D5:H5. In Excel 365, the array will spill into the range D5:H5 automatically.

_I learned the FILTERXML trick from Bill Jelen in a_ [_MrExcel video_](https://www.youtube.com/watch?v=S-pnxg1pZVc&list=RDCMUCXbicpVq_ALWG4ijPKsR7ZQ&index=5)
_. FILTERXML is not available in Excel on the Mac, or in Excel Online. This is a nerdy workaround for difficult problems in older versions of Excel, but it doesn't make sense in a modern version of Excel. The new_ [_TEXTSPLIT function_](https://exceljet.net/functions/textsplit-function)
 _is a much better method._

> If you don't want to use FILTERXML, or can't because you are using Excel on a Mac, [this example](https://exceljet.net/formulas/split-text-with-delimiter)
>  shows another way to split text with a delimiter. This approach requires a bit more setup.

### Extract nth field

With either option above, you may want to extract just the nth field from a single text string. To do that, you can use the [INDEX function](https://exceljet.net/functions/index-function)
. For example, to extract just the age with TEXTSPLIT, you can use a formula like this:

    =INDEX(TEXTSPLIT(B5,","),3) // get age
    

Notice we have simply [nested](https://exceljet.net/glossary/nesting)
 the original formula inside the INDEX function. With FILTERXML, the formula looks like this:

    =INDEX(TRANSPOSE(FILTERXML("<x><y>"&SUBSTITUTE(B5,",","</y><y>")&"</y></x>","//y")),3)
    

### Text-to-columns alternative

Formulas work great when you need a solution that is dynamic, because formulas will update automatically if data changes. However, if you only need a one-off manual process, you can also use Excel's [Text-to-Columns](https://exceljet.net/glossary/text-to-columns)
 feature.

Related formulas
----------------

[![Excel formula: Split text with delimiter](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Split%20text%20with%20delimiter.png "Excel formula: Split text with delimiter")](https://exceljet.net/formulas/split-text-with-delimiter)

### [Split text with delimiter](https://exceljet.net/formulas/split-text-with-delimiter)

The gist of this formula is to replace a given delimiter with a large number of spaces using SUBSTITUTE and REPT, then use the MID function to extract text related to the "nth occurrence" and the TRIM function to get rid of the extra space. In this snippet, the delimiter ( delim ) is replaced with...

[![Excel formula: Get first word](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_get_first_word_1.png "Excel formula: Get first word")](https://exceljet.net/formulas/get-first-word)

### [Get first word](https://exceljet.net/formulas/get-first-word)

FIND returns the position (as a number) of the first occurrence of a space character in the text. This position, minus one, is fed into the LEFT function as num\_chars . The LEFT function then extracts characters starting at the left side of the text, up to (position - 1). Handling one word If a...

[![Excel formula: Extract nth word from text string](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20nth%20word%20from%20text%20string.png "Excel formula: Extract nth word from text string")](https://exceljet.net/formulas/extract-nth-word-from-text-string)

### [Extract nth word from text string](https://exceljet.net/formulas/extract-nth-word-from-text-string)

In this example, the goal is to extract the nth word from the text string given in column B. The article below explains two approaches. The first approach is based on the new TEXTSPLIT function , which makes it very easy to split text with a custom delimiter. The second approach is a more...

[![Excel formula: Extract word that begins with specific character](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20word%20that%20begins%20with.png "Excel formula: Extract word that begins with specific character")](https://exceljet.net/formulas/extract-word-that-begins-with-specific-character)

### [Extract word that begins with specific character](https://exceljet.net/formulas/extract-word-that-begins-with-specific-character)

Starting from the inside out, the MID function is used to extract all text after "@": MID(B5,FIND("@",B5),LEN(B5)) The FIND function provides the starting point, and for total characters to extract, we just use LEN on the original text. This is a bit sloppy, but it avoids having to calculate the...

[![Excel formula: Extract multiple lines from a cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20multiple%20lines%20from%20a%20cell.png "Excel formula: Extract multiple lines from a cell")](https://exceljet.net/formulas/extract-multiple-lines-from-a-cell)

### [Extract multiple lines from a cell](https://exceljet.net/formulas/extract-multiple-lines-from-a-cell)

At the core, this formula looks for a line delimiter ("delim") and replaces it with a large number of spaces using the SUBSTITUTE and REPT functions. Note: In older versions of Excel on a Mac, use CHAR(13) instead of CHAR(10). The CHAR function returns a character based on it's numeric code. The...

[![Excel formula: Split text and numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split%20text%20and%20numbers.png "Excel formula: Split text and numbers")](https://exceljet.net/formulas/split-text-and-numbers)

### [Split text and numbers](https://exceljet.net/formulas/split-text-and-numbers)

Overview The formula looks complex, but the mechanics are in fact quite simple. As with most formulas that split or extract text, the key is to locate the position of the thing you are looking for. Once you have the position, you can use other functions to extract what you need. In this case, we...

[![Excel formula: Split text string at specific character](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split_text_string_at_specific_character.png "Excel formula: Split text string at specific character")](https://exceljet.net/formulas/split-text-string-at-specific-character)

### [Split text string at specific character](https://exceljet.net/formulas/split-text-string-at-specific-character)

In this example, the goal is to split a text string at the underscore("\_") character with a formula. Notice the location of the underscore is different in each row. This means the formula needs to locate the position of the underscore character first before any text is extracted. There are two...

Related functions
-----------------

[![Excel TEXTSPLIT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textsplit%20function.png "Excel TEXTSPLIT function")](https://exceljet.net/functions/textsplit-function)

### [TEXTSPLIT Function](https://exceljet.net/functions/textsplit-function)

The Excel TEXTSPLIT function splits text by a given delimiter to an array that spills into multiple cells. TEXTSPLIT can split text into rows or columns.

[![Excel REDUCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20reduce%20function.png "Excel REDUCE function")](https://exceljet.net/functions/reduce-function)

### [REDUCE Function](https://exceljet.net/functions/reduce-function)

The Excel REDUCE function applies a custom LAMBDA function to each element in a given array and accumulates results to a single value.

[![Excel LAMBDA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lambda.png "Excel LAMBDA function")](https://exceljet.net/functions/lambda-function)

### [LAMBDA Function](https://exceljet.net/functions/lambda-function)

The Excel LAMBDA function provides a way to create custom functions that can be reused throughout a workbook, without VBA or macros.

[![Excel DROP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20drop%20function.png "Excel DROP function")](https://exceljet.net/functions/drop-function)

### [DROP Function](https://exceljet.net/functions/drop-function)

The Excel DROP function returns a subset of a given array by "dropping" rows and columns. The number of rows and columns to remove is provided by separate _rows_ and _columns_ arguments. Rows and columns can be dropped from the start or end of the given array....

[![Excel FILTERXML function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20filterxml.png "Excel FILTERXML function")](https://exceljet.net/functions/filterxml-function)

### [FILTERXML Function](https://exceljet.net/functions/filterxml-function)

The Excel FILTERXML function returns specific data from XML text using the specified XPath expression.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Split text with delimiter](https://exceljet.net/formulas/split-text-with-delimiter)
    
*   [Get first word](https://exceljet.net/formulas/get-first-word)
    
*   [Extract nth word from text string](https://exceljet.net/formulas/extract-nth-word-from-text-string)
    
*   [Extract word that begins with specific character](https://exceljet.net/formulas/extract-word-that-begins-with-specific-character)
    
*   [Extract multiple lines from a cell](https://exceljet.net/formulas/extract-multiple-lines-from-a-cell)
    
*   [Split text and numbers](https://exceljet.net/formulas/split-text-and-numbers)
    
*   [Split text string at specific character](https://exceljet.net/formulas/split-text-string-at-specific-character)
    

### Functions

*   [TEXTSPLIT Function](https://exceljet.net/functions/textsplit-function)
    
*   [REDUCE Function](https://exceljet.net/functions/reduce-function)
    
*   [LAMBDA Function](https://exceljet.net/functions/lambda-function)
    
*   [DROP Function](https://exceljet.net/functions/drop-function)
    
*   [FILTERXML Function](https://exceljet.net/functions/filterxml-function)
    

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