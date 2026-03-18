# List.Contains Function in Power Query M (9 Examples)

**Source:** https://trumpexcel.com/power-query/functions/list-contains

---

[Skip to content](https://trumpexcel.com/power-query/functions/list-contains/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/power-query/functions/list-contains/#below-title)

The List.Contains function checks whether a specific value exists in a list.

It returns true if the value is found and false if it’s not. Think of it as Power Query’s version of an “IN” operator.

This is one of those functions you’ll use all the time. Whether you’re filtering rows, building conditional columns, or validating data, List.Contains keeps your code clean and readable.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/power-query/functions/list-contains/#)

List.Contains Syntax
--------------------

\= List.Contains(list as list, value as any, optional equationCriteria as any) as logical

*   **list** – The list of values to search through
*   **value** – The value you want to find in the list
*   **equationCriteria** (optional) – A comparer function that controls how values are compared. By default, the function uses case-sensitive comparison (Comparer.Ordinal)

**What it returns:** A logical value (TRUE or FALSE). Returns TRUE if the value is found in the list, and FALSE if it’s not.

When to Use List.Contains
-------------------------

Use this function when you need to:

*   Check if a value exists in a list of allowed or blocked items
*   Filter table rows based on a list of values (like SQL’s IN operator)
*   Add conditional columns that categorize data based on list membership
*   Replace long chains of or conditions with cleaner, more readable code
*   Validate data by confirming that expected values are present in a column

Example 1: Basic Value Check
----------------------------

Let’s start with the simplest use case. You have a list of values and want to check if a specific value exists in it.

Suppose you have a list of product IDs and want to verify whether ID 103 is in the list.

Add a new step (by clicking on the fx icon next to the formula bar) and use this formula:

\= List.Contains({101, 102, 103, 104, 105}, 103)

**Result:** TRUE

The function scans through each item in the list and finds 103, so it returns true.

![01 List contains power query returns true](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201358%20247'%3E%3C/svg%3E)

Now let’s check for a value that doesn’t exist:

\= List.Contains({101, 102, 103, 104, 105}, 110)

**Result:** FALSE

Since 110 is not in the list, the function returns false.

![01 List contains power query returns false](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201339%20244'%3E%3C/svg%3E)

This also works with text values:

\= List.Contains({"Apple", "Banana", "Cherry"}, "Banana")

**Result:** TRUE

![01 Item found in a list power query](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201524%20227'%3E%3C/svg%3E)

If you want to check whether a value is not in a list, simply add _not_ before the function.

For example:

\= not List.Contains({101, 102, 103, 104, 105}, 110)

![01 Using List Contains with not power query](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201438%20221'%3E%3C/svg%3E)

This returns TRUE because 110 is not in the list. The not operator flips the result — if List.Contains returns false, not turns it into true, and vice versa.

Example 2: Using If with List.Contains
--------------------------------------

Sometimes a simple TRUE or FALSE isn’t meaningful enough.

You can combine _List.Contains_ with an _if_ statement to return a more descriptive result.

Suppose you have a list of discontinued product codes and want to check whether a specific product is still active or has been discontinued.

\= if List.Contains({"P001", "P005", "P009"}, "P003") then "Discontinued" else "Active"

**Result**: Active

![02 Using if with List Contains](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202122%20229'%3E%3C/svg%3E)

Since “P003” is not in the discontinued list, the formula returns “Active”.

Now let’s check for a product that is in the list:

\= if List.Contains({"P001", "P005", "P009"}, "P005") then "Discontinued" else "Active"

**Result**: Discontinued

![02 Using if with List Contains negative](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202126%20227'%3E%3C/svg%3E)

Since “P005” is found in the discontinued list, the formula returns “Discontinued”.

Example 3: Checking a Table Column for a Value
----------------------------------------------

In real-world scenarios, you typically work with tables rather than hardcoded lists.

Suppose you have an Orders table with columns OrderID, Product, and Amount, and you want to check if “Laptop” exists anywhere in the Product column.

![03 Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201542%20726'%3E%3C/svg%3E)

With the table loaded in Power Query, add a custom step by clicking the fx button in the formula bar and entering the following formula:

\= List.Contains(Source\[Product\], "Laptop")

**Result:** TRUE (if “Laptop” exists in the Product column)

![03 Check if item exists in a column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201258%20223'%3E%3C/svg%3E)

In this formula, Source\[Product\] extracts the Product column as a list, and List.Contains checks whether “Laptop” appears in that list.

Note: If your query has a “Changed Type” step after Source, you can reference that step instead (e.g., #”Changed Type”\[Product\]).

You can also write this as a complete formula in a blank query:

\= let  
    Source = Excel.CurrentWorkbook(){\[Name="Orders"\]}\[Content\],  
    HasLaptop = List.Contains(Source\[Product\], "Laptop")  
in  
    HasLaptop

The first line references the Orders table from your Excel workbook, and the second line checks if “Laptop” exists in the Product column.

**Note**: _List.Contains_ function is case-sensitive by default. If you want to do a case-insensitive search, see the next example.

Example 4: Case-Insensitive Search
----------------------------------

By default, List.Contains treats uppercase and lowercase letters as different values.

This matters when your data has inconsistent casing. For example, “laptop”, “Laptop”, and “LAPTOP” would all be treated as different values.

Suppose you have a list of product categories and want to check if “electronics” exists, regardless of how it’s capitalized:

\= List.Contains({"Electronics", "Clothing", "Furniture"}, "electronics")

**Result:** FALSE

![04 List Contains is case sensitive](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201841%20217'%3E%3C/svg%3E)

Even though “Electronics” is in the list, the lowercase “electronics” doesn’t match because the default comparison is case-sensitive.

To make it case-insensitive, use the _Comparer.OrdinalIgnoreCase_ function as the third argument:

\= List.Contains({"Electronics", "Clothing", "Furniture"}, "electronics", Comparer.OrdinalIgnoreCase)

**Result:** TRUE

![04 Making List Contains case insensitive](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201861%20489'%3E%3C/svg%3E)

Now the function ignores case differences and finds a match.

This is especially useful when working with user-entered data where casing is inconsistent.

Example 5: Filter Rows Using List.Contains
------------------------------------------

This is where List.Contains really shines. You can use it inside Table.SelectRows to filter a table based on a list of values.

This is Power Query’s equivalent of the IN operator in SQL.

Suppose you have a Sales table with columns Region, Product, and Revenue, and you only want to keep rows where the Region is “North” or “West”.

![05 Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201544%20841'%3E%3C/svg%3E)

Instead of writing:

\= Table.SelectRows(Source, each \[Region\] = "North" or \[Region\] = "West")

You can write this much cleaner version:

\= Table.SelectRows(Source, each List.Contains({"North", "West"}, \[Region\]))

![05 Formula to filter by region power query](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201872%20584'%3E%3C/svg%3E)

Both formulas produce the same result, but the _List.Contains_ version is much easier to read and maintain.

And when the list grows to 5, 10, or 20 values, the difference becomes even more significant.

Example 6: Exclude Rows Using List.Contains
-------------------------------------------

Now let’s tackle the opposite scenario. Instead of keeping matching rows, you want to remove them.

Suppose you have an Employees table and want to exclude rows where the Department is “Temp” or “Intern”.

![06 Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201536%201037'%3E%3C/svg%3E)

Add a new step (by clicking on the fx icon next to the formula bar) and use this formula:

\= Table.SelectRows(Source, each not List.Contains({"Temp", "Intern"}, \[Department\]))

![06 Exclude rows using list contains power query](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202069%20771'%3E%3C/svg%3E)

By adding not before List.Contains, the filter is reversed. Only rows where the Department is not “Temp” or “Intern” are kept.

This is cleaner than writing out multiple AND conditions:

\= Table.SelectRows(Source, each \[Department\] <> "Temp" and \[Department\] <> "Intern")

Both approaches give the same result, but the _List.Contains_ version scales much better when you have a longer exclusion list.

Example 7: Add a Conditional Column
-----------------------------------

This next one comes up quite often in data cleaning and categorization tasks.

You can use List.Contains inside an if…then…else statement to create a new column that categorizes rows based on list membership.

Suppose you have a Products table with columns Product and Price, and you want to add a column that marks certain products as “On Sale”.

![07 Database](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201067%20838'%3E%3C/svg%3E)

With the table loaded in Power Query, go to Add Column > Custom Column and use this formula:

\= if List.Contains({"Jeans", "Skirt", "Socks"}, \[Product\]) then "On Sale" else "Regular"

![07 using if then with List contains](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202103%201192'%3E%3C/svg%3E)

The formula checks each row’s Product value against the list. If it’s found, the new column shows “On Sale”. Otherwise, it shows “Regular”.

This is much cleaner than writing a long if \[Product\] = “Jeans” or \[Product\] = “Skirt” or \[Product\] = “Socks” then… statement.

Example 8: Partial Match Using Custom Equation Criteria
-------------------------------------------------------

Now let’s get into something more advanced.

The equationCriteria parameter isn’t limited to built-in comparers. You can pass a custom function that defines how values are compared. This lets you do partial matching.

Suppose you have a list of product names and want to check if any of them contain the word “Pro”:

\= List.Contains({"iPhone Pro", "Galaxy Standard", "Pixel Pro Max"}, "Pro", (x, y) => Text.Contains(x, y))

**Result:** TRUE

![08 check for partial match case sensitive](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202111%20454'%3E%3C/svg%3E)

Here, instead of checking for an exact match, the custom function (x, y) => Text.Contains(x, y) checks whether each list item (x) contains the search value (y). Since “iPhone Pro” contains “Pro”, the function returns true.

Note that you can further simplify this formula by using:

\= List.Contains({"iPhone Pro", "Galaxy Standard", "Pixel Pro Max"}, "Pro", Text.Contains)

In the above formula, the TEXT.CONTAINS function would automatically figure out that it would take two arguments:

1.  One from the list that mentions the brand names
2.  The second one is going to be the word “Pro”

You can also make this case-insensitive by adding a comparer inside Text.Contains:

\= List.Contains({"iPhone Pro", "Galaxy Standard", "Pixel Pro Max"}, "pro", (x, y) => Text.Contains(x, y, Comparer.OrdinalIgnoreCase))

**Result:** TRUE

![08 check for partial match case insensitive](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202288%20451'%3E%3C/svg%3E)

This finds a match even though “pro” is lowercase and the list items have “Pro” with a capital P.

Example 9: Using a Separate Query as the List
---------------------------------------------

Here’s a practical pattern that makes your Power Query solutions dynamic and easy to maintain.

Instead of hardcoding values in the formula, you can reference a separate table as the filter list. This way, users can update the filter criteria without touching the M code.

Suppose you have two tables in Excel (named SalesTable and FilterTable):

![09 Dataset tables](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201325%20827'%3E%3C/svg%3E)

First, load both tables into Power Query and save them as a connection.

Then, in the SalesTable query, add a new step with this formula:

\= Table.SelectRows(Source, each List.Contains(FilterTable\[Region\], \[Region\]))

![09 Filter Data based on table](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201920%20592'%3E%3C/svg%3E)

In this formula, FilterTable\[Region\] pulls the Region column from the FilterTable query as a list.

The formula then checks each row in the Sales table to see if its Region value exists in that list.

The beauty of this approach is that when someone adds or removes a region from the Filter Table in Excel, the query automatically updates the next time it’s refreshed.

Note: Make sure the FilterTable query is set to “Connection Only” (right-click the query > Load To > Only Create Connection) so it doesn’t load as a separate table in your workbook.

Tips & Common Mistakes
----------------------

*   **Default is case-sensitive:** List.Contains uses Comparer.Ordinal by default, meaning “Apple” and “apple” are treated as different values. Use Comparer.OrdinalIgnoreCase as the third argument when case shouldn’t matter.
*   **Don’t confuse with List.ContainsAny:** List.Contains checks for a single value. If you need to check whether any value from one list exists in another list, use List.ContainsAny instead.
*   **Use it instead of multiple OR conditions:** Whenever you find yourself writing \[Column\] = “A” or \[Column\] = “B” or \[Column\] = “C”, replace it with List.Contains({“A”, “B”, “C”}, \[Column\]). It’s cleaner and easier to maintain.
*   **Extract columns as lists first:** To check values against a table column, use the Table\[Column\] syntax to extract the column as a list before passing it to List.Contains.
*   **Performance with large lists:** For very large lists (thousands of items), List.Contains checks each item sequentially. If performance becomes an issue, consider using Table.Join or Table.NestedJoin instead, as these operations can be more efficient for large datasets.

Other Related Power Query Functions
-----------------------------------

*   List.ContainsAny – Checks if any value from one list exists in another list
*   List.ContainsAll – Checks if all values from one list exist in another list
*   List.FindText – Returns a list of values that contain specific text
*   List.AnyTrue – Returns true if any expression in a list is true
*   List.AllTrue – Returns true if all expressions in a list are true
*   [List.Count](https://trumpexcel.com/power-query/functions/list-count/)
     – Returns the total number of items in a list.
*   [List.IsDistinct](https://trumpexcel.com/power-query/functions/list-isdistinct/)
     – Checks whether all values in a list are unique.

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