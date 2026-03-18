# Table.TransformColumns Function in Power Query M (6 Examples)

**Source:** https://trumpexcel.com/power-query/functions/table-transformcolumns

---

[Skip to content](https://trumpexcel.com/power-query/functions/table-transformcolumns/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/power-query/functions/table-transformcolumns/#below-title)

The _Table.TransformColumns_ function in Power Query lets you apply transformations to one or more columns in a table simultaneously.

Instead of modifying each column individually with separate steps, you can clean, convert, or manipulate multiple columns in a single operation.

This function is particularly useful when you need to add prefixes or suffixes, format text, perform calculations, or apply custom functions across your dataset efficiently.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/power-query/functions/table-transformcolumns/#)

Table.TransformColumns Syntax
-----------------------------

Below is the syntax of the _Table.TransformColumns_ function in Power Query.

\= Table.TransformColumns(  
    table as table,  
    transformOperations as list,  
    optional defaultTransformation as function,  
    optional missingField as MissingField.Type  
) as table

*   **table** – The source table you want to transform.
*   **transformOperations** – A list that specifies which columns to modify and how. Each transformation can be written in two formats:
    *   { “ColumnName”, TransformFunction } – transforms the column without changing its type
    *   { “ColumnName”, TransformFunction, NewType } – transforms the column and sets a new data type
*   **defaultTransformation** (optional) – A function that applies to all columns NOT listed in transformOperations. This is useful when you want to apply a blanket transformation to most columns.
*   **missingField** (optional) – Specifies what happens if a column listed in transformOperations doesn’t exist. Options include:
    *   MissingField.Error – Throws an error (default behavior)
    *   MissingField.Ignore – Skips the missing column without error
    *   MissingField.UseNull – Creates the column with null values

**What it returns:** A new table with the specified transformations applied to the designated columns.

When to Use Table.TransformColumns
----------------------------------

Use this function when you need to:

*   Transform multiple columns simultaneously in a single step
*   Add prefixes or suffixes to values (like converting 1, 2, 3 to Q1, Q2, Q3)
*   Apply text formatting functions (uppercase, lowercase, trim, proper case)
*   Convert data types while also modifying the values
*   Handle missing columns gracefully without causing errors
*   Clean and standardize data across several columns at once

Example 1: Adding a Prefix to Make Values More Readable
-------------------------------------------------------

Let’s start with a common scenario.

You have a sales report with a Quarter column containing just numbers (1, 2, 3, 4).

To make reports clearer, you want to display them as Q1, Q2, Q3, and Q4.

![Dataset to transform column by adding a prefix](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201529%20860'%3E%3C/svg%3E)

Add a new step (by clicking on the fx icon next to the formula bar) and use this formula:

\= Table.TransformColumns(  
    Source,  
    {{"Quarter", each "Q" & Text.From(\_), type text}}  
)

![Table transform columns function to add prefix to each element in the column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201550%201204'%3E%3C/svg%3E)

In the above formula, _each “Q” & Text.From(\_)_ creates a function that takes each value, converts it to text, and adds “Q” in front.

The underscore \_ represents the current cell value (1, 2, 3, or 4).

_Text.From(\_)_ converts the number to text so it can be concatenated with “Q”.

The type text at the end sets the column’s data type to text.

Example 2: Adding a Suffix to Values
------------------------------------

Here’s another common use case.

You have a table with product dimensions, but the values are just numbers without units. You want to add “cm” to make the measurements clear.

![Dataset to add suffix to each value in the column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202034%20785'%3E%3C/svg%3E)

Add a new step (by clicking on the fx icon next to the formula bar) and use this formula:

\= Table.TransformColumns(  
    Source,  
    {  
        {"Length", each Text.From(\_) & " cm", type text},  
        {"Width", each Text.From(\_) & " cm", type text},  
        {"Height", each Text.From(\_) & " cm", type text}  
    }  
)

![Suffix is added to all the columns using table transofrmcolumns function 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201769%201128'%3E%3C/svg%3E)

Here, _each Text.From(\_) & ” cm”_ converts the number to text and appends ” cm” at the end.

The formula applies the same transformation to all three columns.

Note that after this transformation, the values become text and cannot be used for calculations.

Example 3: Cleaning and Standardizing Text Data
-----------------------------------------------

This next one comes up quite often in data cleaning.

You have imported customer data where names have inconsistent formatting, and emails have extra spaces.

You want to clean everything up in one step.

![Dataset to transform two columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201533%20839'%3E%3C/svg%3E)

Add a new step (by clicking on the fx icon next to the formula bar) and use this formula:

\= Table.TransformColumns(  
    Source,  
    {  
        {"Name", Text.Proper, type text},  
        {"Email", Text.Trim, type text}  
    }  
)

![Formula to transform multiple columns using different functions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201547%201192'%3E%3C/svg%3E)

_Text.Proper_ capitalizes the first letter of each word (proper case formatting).

_Text.Trim_ removes leading and trailing spaces from the email addresses.

For built-in functions that take a single argument, you don’t need the each keyword. Just pass the function name directly.

Example 4: Formatting Currency Values
-------------------------------------

Now let’s tackle something more advanced.

You have a financial report where amounts are plain numbers, but you want to display them as formatted currency with a dollar sign and thousands separator.

![Dataset with numbers that needs to be formatted in the column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201544%20722'%3E%3C/svg%3E)

Add a new step (by clicking on the fx icon next to the formula bar) and use this formula:

\= Table.TransformColumns(  
    Source,  
    {  
        {"Budget", each "$" & Number.ToText(\_, "N0"), type text},  
        {"Actual", each "$" & Number.ToText(\_, "N0"), type text}  
    }  
)

![Table transform columns function to change the column number formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201690%201073'%3E%3C/svg%3E)

Number.ToText(\_, “N0”) formats the number with thousands separators and no decimal places.

We then add a “$” prefix to create the currency format.

The “N0” format code means “Number with 0 decimal places.”

Example 5: Converting Month Numbers to Month Names
--------------------------------------------------

Here’s a scenario you’ll encounter frequently when building reports.

You have data with month numbers (1-12) and want to display actual month names for better readability.

![Dataset with month number that needs to be converted into month name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201548%20855'%3E%3C/svg%3E)

Add a new step (by clicking on the fx icon next to the formula bar) and use this formula:

\= Table.TransformColumns(  
    Source,  
    {{"Month", each Date.MonthName(#date(2000, \_, 1)), type text}}  
)

![Month number to names power query](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201706%201194'%3E%3C/svg%3E)

_#date(2000, \_, 1)_ creates a date using the month number (the year and day don’t matter here).

_Date.MonthName()_ extracts the full month name from that date.

This is a clever workaround since Power Query doesn’t have a direct “number to month name” function.

Example 6: Applying the Same Transformation to All Other Columns
----------------------------------------------------------------

This next one is invaluable when dealing with many columns.

When most columns need the same transformation, use the optional third parameter (defaultTransformation) instead of listing every column.

Suppose you have a table where most columns contain text that should be numbers:

![Dataset to numbers as text in columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202507%20725'%3E%3C/svg%3E)

You want to convert all month columns to numbers while leaving Category as text.

Add a new step (by clicking on the fx icon next to the formula bar) and use this formula:

\= Table.TransformColumns(  
    Source,  
    {{"Category", Text.Upper, type text}},  
    Number.FromText  
)

![Text has been converted into numbers using the table transform function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202507%201071'%3E%3C/svg%3E)

The second argument only specifies the Category column (converting to uppercase).

The third argument Number.FromText applies to ALL other columns (Jan, Feb, Mar, Apr).

This approach saves you from listing every column that needs the same transformation.

Tips & Common Mistakes
----------------------

*   **When to use \`each\`:** Use the each keyword when your transformation needs to reference the current value (using \_) or when using operators like & or +. For built-in functions that take a single argument (like Text.Upper, Text.Trim, Number.FromText), you can pass the function name directly without each.
*   **Understanding the underscore:** The underscore \_ is shorthand for the current cell value. each “Q” & Text.From(\_) means “for each value, add Q in front of it converted to text.”
*   **Double curly braces for multiple columns:** Each transformation is a list within the main list. Use double curly braces: { {“Column1”, Function1}, {“Column2”, Function2} }. A common error is using single braces, which causes errors.
*   **Values become text after adding prefix/suffix:** Once you concatenate text (like adding “Q” or “cm”), the column becomes text type, and you cannot perform mathematical operations on it.
*   **Cannot access other columns:** Table.TransformColumns only works with one column at a time. If you need to transform a column based on values from another column, use Table.AddColumn or Table.TransformRows instead.
*   **Case sensitivity:** Column names in Power Query are case-sensitive. “Quarter” and “quarter” are treated as different columns.

**Related Functions**

*   **[Table.RenameColumns](https://trumpexcel.com/power-query/functions/table-renamecolumns/)
    ** – Renames one or more columns in a table. Use this when you need to change column headers for clarity, consistency, or to match expected naming conventions downstream.
*   **Table.TransformColumnTypes** – Changes only the data types of columns without modifying the values. Use this when you just need type conversion without value transformation.
*   **Table.TransformRows** – Transforms entire rows at once, allowing you to create new records based on values from multiple columns. Useful when your transformation logic depends on values from other columns.
*   **Table.ReplaceValue** – Replaces specific values in columns based on conditions. Better suited for find-and-replace scenarios rather than applying functions to every value.
*   [**Table.Group**](https://trumpexcel.com/power-query/functions/table-group/)
     – Group rows that have identical key values allowing you to aggregate data within each group.

[All Power Query Functions](https://trumpexcel.com/power-query/functions/)

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free Excel Tips EBook Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK