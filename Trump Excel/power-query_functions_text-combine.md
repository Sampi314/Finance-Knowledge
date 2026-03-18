# Text.Combine Function in Power Query M (8 Examples)

**Source:** https://trumpexcel.com/power-query/functions/text-combine

---

[Skip to content](https://trumpexcel.com/power-query/functions/text-combine/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/power-query/functions/text-combine/#below-title)

The Text.Combine function joins a list of text values into a single text string.

You can optionally specify a separator (like a comma or space) to place between each value.

This is the standard function for concatenation in Power Query. Whether you’re merging name columns, building addresses, or combining grouped row values into a single cell, Text.Combine is your go-to function.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/power-query/functions/text-combine/#)

Text.Combine Syntax
-------------------

\= Text.Combine(texts as list, optional separator as nullable text)

*   **texts** – A list of text values you want to combine into one string
*   **separator** (optional) – A text delimiter to place between each value. If omitted, the values are joined with no separator

**What it returns:** A single text value containing all the items from the list joined together.

When to Use Text.Combine
------------------------

Use this function when you need to:

*   Merge multiple columns into one (such as First Name + Last Name into Full Name)
*   Build full addresses from separate City, State, and Zip columns
*   Create concatenated keys by joining multiple column values
*   Combine grouped row values into a comma-separated string (like TEXTJOIN across rows)
*   Convert a list of values into a single delimited string

Example 1: Basic Combine Without a Separator
--------------------------------------------

Let’s start with the simplest use case.

Suppose you want to join two text values into one without any separator between them.

Open a blank query in Power Query and use the below formula in the formula bar

\= Text.Combine({"Power", "Query"})

**Result:** PowerQuery

![01 Combine text without separator Power query](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201087%20253'%3E%3C/svg%3E)

Since no separator is specified, the function simply joins the two values directly with nothing in between.

Example 2: Combine with a Separator
-----------------------------------

Here’s the most common way you’ll use this function.

Suppose you have a city name and state abbreviation, and you want to combine them with a comma and space in between.

Enter the below formula in the formula bar in Power Query

\= Text.Combine({"Excel", "Power Query", "DAX"}, " | ")

**Result:** Excel | Power Query | DAX

![01 Combine text without separator Power query](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201477%20238'%3E%3C/svg%3E)

The second argument ” | ” tells the function to insert a pipe symbol with a space on both sides between each word.

You can use any text as the separator. A hyphen, a comma, a semicolon. Whatever works for your data.

Example 3: Combining Table Columns into a New Column
----------------------------------------------------

This next one comes up quite often in data cleaning.

Suppose you have a table with three columns: First Name, Middle Name, and Last Name. You want to combine them into a single Full Name column.

![03 Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201547%20840'%3E%3C/svg%3E)

With the table loaded in Power Query, go to **Add Column > Custom Column** and use this formula and click OK:

\= Text.Combine({\[First Name\], \[Middle Name\], \[Last Name\]}, " ")

![03 Formula used in custom column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202100%201317'%3E%3C/svg%3E)

**Result:** A new column with values like Doug J Elis, Anna M Jorayew, and Rada Mihaylova.

![03 Custom column added to combine columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202167%201189'%3E%3C/svg%3E)

In this formula, the curly braces {} create a list from the three column values for each row. The space ” ” is used as the separator between them.

Notice something important with the third row. Rada has no middle name (null value), and the result is Rada Mihaylova with a single space.

Not Rada  Mihaylova with a double space.

That’s because Text.Combine skips null values automatically.

_More on this in the next example._

Example 4: How Text.Combine Handles Null Values
-----------------------------------------------

This is where Text.Combine really shines.

When your data has missing values (nulls), Text.Combine simply ignores them. It doesn’t insert extra separators or return an error.

Use the formula below in Power Query Formula Bar:

\= Text.Combine({"John", null, "Smith"}, " ")

**Result**: John Smith

![04 Combine with Null](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201282%20217'%3E%3C/svg%3E)

The null value in the middle is completely skipped. You get a clean result without any double commas or trailing separators.

Now compare this to what happens if you have an empty string instead of null:

\= Text.Combine({"John", "", "Smith"}, " ")

**Result**: John Smith

![04 Combine with blank string](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201269%20211'%3E%3C/svg%3E)

An empty string is not the same as null. The function treats it as a valid value and includes the extra separator.

This distinction matters.

If your data has empty strings instead of nulls and you’re getting unwanted double separators, you may need to replace empty strings with null first, using a step like this:

\= Table.ReplaceValue(Source, "", null, Replacer.ReplaceValue, {"YourColumn"})

Example 5: Text.Combine vs. the Ampersand (&) Operator
------------------------------------------------------

You might wonder why you’d use Text.Combine when you can just use the & operator to join text.

The key difference is how they handle null values.

With the ampersand operator, if any value is null, the entire result becomes null:

\= "Sumit" & " " & null & " " & "Bansal"

**Result:** null

![05 Combining null with ampersand](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201189%20217'%3E%3C/svg%3E)

With Text.Combine, nulls are skipped, and you still get a usable result:

\= Text.Combine({"Sumit", null, "Bansal"}, " ")

**Result:** Sumit Bansal

![05 Combine null with Text Combine function power query](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201343%20227'%3E%3C/svg%3E)

Here’s a quick comparison:

| Feature | Text.Combine | Ampersand (&) |
| --- | --- | --- |
| Null handling | Skips nulls automatically | Returns null if any value is null |
| Separator | Built-in separator parameter | Must manually add separator strings |
| Input format | Takes a list {} | Chains individual values |
| Best for | Multiple columns, Group By | Simple two-value joins with no nulls |
| Syntax | Text.Combine({val1, val2}, sep) | val1 & sep & val2 |
| Error risk | Low — handles nulls gracefully | High — any null breaks the result |
| Readability | Clean with many values | Gets messy with 3+ values |

Use _&_ when you’re joining two values, and you’re sure neither will be null. Use _Text.Combine_ for everything else.

Example 6: Combining Non-Text Values (Numbers and Dates)
--------------------------------------------------------

This is the most common error people run into with _Text.Combine_.

Suppose you have a table with a text column (Product) and a numeric column (Quantity), and you want to combine them.

![06 Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202015%20843'%3E%3C/svg%3E)

If you try the formula below in a custom column directly:

\= Text.Combine({\[Product\], \[Quantity\]}, " - ")

…you’ll get an error because Quantity is a number, not text. Text.Combine only works with text values.

![06 Error because of data type](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202390%201967'%3E%3C/svg%3E)

The fix is simple. Wrap the non-text value with Text.From():

\= Text.Combine({\[Product\], Text.From(\[Quantity\])}, " - ")

![06 Result combines correctly after Text from function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202400%20964'%3E%3C/svg%3E)

The same approach works for dates and other data types.

Always use _Text.From()_ to convert non-text values before passing them to _Text.Combine_.

If you’re working with a list of mixed types, you can convert the entire list at once using _List.Transform_:

\= Text.Combine(List.Transform({100, 200, 300}, each Text.From(\_)), ", ")

**Result:** 100, 200, 300

![06 Transform list first with text from](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201837%20238'%3E%3C/svg%3E)

Example 7: Concatenating Row Values with Group By
-------------------------------------------------

Now let’s tackle something more advanced. This is the Power Query equivalent of Excel’s TEXTJOIN across rows.

Suppose you have a table of products grouped by brand, and you want to combine all product names for each brand into a single comma-separated string.

![07 Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201070%201106'%3E%3C/svg%3E)

What you want is a result like:

![07 Result Needed](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201430%20399'%3E%3C/svg%3E)

To do this, click on the fx icon (next to the Formula Bar) and then use the formula below:

\= Table.Group(Source, {"Brand"}, {{"Products", each Text.Combine(\[Product\], ", "), type text}})

**Result:** Each brand now has all its products listed in a single cell, separated by commas.

![07 Formula to group and combine](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202276%20750'%3E%3C/svg%3E)

In this formula, Table.Group groups the table by the Brand column.

For each group, each Text.Combine(\[Product\], “, “) takes all the Product values in that group and joins them with a comma and space.

Example 8: Sorting Values Before Combining in Group By
------------------------------------------------------

Here’s a gotcha that catches a lot of people.

When you use Text.Combine inside a Group By, the concatenated values appear in whatever order they were in the original data. Even if you sorted the data in a previous step, Power Query may not preserve that order.

To guarantee a specific sort order, use _List.Sort_ inside the _Text.Combine_ expression.

Using the same Brand/Product table from the previous example, here’s how to sort the products alphabetically before combining:

\= Table.Group(Source, {"Brand"}, {{"Products", each Text.Combine(List.Sort(\[Product\], Order.Ascending), ", "), type text}})

![08 Result Data grouped in ascending order](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202115%20748'%3E%3C/svg%3E)

The only difference from the previous example is List.Sort(\[Product\], Order.Ascending) wrapped around the column reference. This sorts the product names alphabetically before joining them.

You can also use Order.Descending to reverse the sort order.

Tips & Common Mistakes
----------------------

*   **Null vs. empty string:** Text.Combine skips null values but does NOT skip empty strings. If you’re getting unexpected double separators (like A, , C), your data likely has empty strings instead of nulls. Replace them with null before combining.
*   **All values must be text:** Text.Combine only accepts text values. If your list contains numbers, dates, or logical values, wrap them with Text.From() to avoid errors.
*   **Don’t confuse with Combiner.CombineTextByDelimiter:** Combiner.CombineTextByDelimiter is a different function. It returns a function (not text), and it’s used primarily with Table.CombineColumns for merging columns through the UI. Text.Combine directly returns a text value.
*   **Sort order in Group By:** Text.Combine does not sort values. When used inside Table.Group, the output order depends on the original data order. Use List.Sort inside the expression or Table.Buffer after sorting to guarantee order.
*   **Merge Columns is the GUI shortcut:** If you just need to combine two or three columns with a separator, you can also select the columns and use Transform > Merge Columns from the ribbon. Behind the scenes, Power Query uses Combiner.CombineTextByDelimiter for this.

Other Related Power Query Functions
-----------------------------------

*   [Text.Contains](https://trumpexcel.com/power-query/functions/text-contains/)
     – It checks whether a text value contains a specific substring or not.
*   Text.Split – Splits a text string into a list by a separator (the inverse of Text.Combine)
*   Text.From – Converts a number, date, or other value to its text representation
*   List.Transform – Applies a function to each item in a list (useful for converting values before combining)
*   List.Sort – Sorts the items in a list in ascending or descending order
*   Table.Group – Groups rows by one or more columns and applies aggregation functions
*   Text.Trim – Removes leading and trailing whitespace from a text value

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