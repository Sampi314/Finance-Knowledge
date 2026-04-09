# Power Query: Appending Files

**Source:** https://sumproduct.com/blog/power-query-appending-files/

---

[Home](https://sumproduct.com/)

\> Power Query: Appending Files

*   December 27, 2016

Power Query: Appending Files
============================

Power Query: Appending Files
============================

28 December 2016

_Welcome our new Power Query blog. Today we append to an existing query._

Whilst it is possible to extract multiple CSV (comma separated values) files at the same time (more on this in a later blog entry), imagine a scenario where similar files appear at intervals and need to be added to a table. This blog entry builds on [Power Query – Getting Started](https://sumproduct.com/blog/power-query-getting-started/)
, where a simple CSV file was extracted, transformed and loaded.

In the same workbook choose to create a new query, by using the ‘From File’ option and browsing to the location of another simple expense CSV file. Take the default options for uploading the file, and choose to ‘Edit’ in order to access the Power Query Editor screen. Once the data is in a similar format to the data already extracted from the first CSV file, the next step is to create an append query. The location of the ‘Append’ option varies slightly according to the Excel version – in Excel 2016 onwards it is under ‘Combine Queries’, but in 2013 and 2010 it is on the ‘Home’ tab in the ‘Combine group’ option. The screenshot shown below is from Excel 2013:

![](https://sumproduct.com/wp-content/uploads/2025/05/1b9cc0aadd440e9eb81a4a2b7364c7a2.jpg)

As the dropdown shows, another query can be appended to this query, or another query can be combined with this query to create a new query. For the scenario where the expense files are always required to be uploaded together, the ‘Append Queries’ option is fine.

![](https://sumproduct.com/wp-content/uploads/2025/05/b33aaa871bd7efea847f99fdcabc89d4.jpg)

The ‘Append’ screen, as shown above, allows multiple queries to be combined, but for the purposes of this scenario, ‘Two Tables’ is sufficient. The other query is selected (all queries in the workbook are available).

![](https://sumproduct.com/wp-content/uploads/2025/05/c57ea9ebfda511001e799122c785be14.jpg)

The data appears in the same query, and a step is created in **M** code combining the data in the current query with the standard expense query that already exists. If any columns are duplicated, then check column names are the same (and in the same case) in both queries.

The total rows are shown at the bottom of the screen – simply close and load to see the data in an excel workbook:

![](<Base64-Image-Removed>)

Further files can be appended using the same method if they arrive after the first files have been appended – the option to append multiple queries also allows data to be combined easily.

In order to extract a larger quantity of similar files, there is another option: extracting from a folder, and this will be the subject of the next blog entry…

Want to read more about Power Query? A complete list of all our Power Query blogs can be found [here](https://www.sumproduct.com/thought/power-query-blog-series)
. Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-appending-files/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-appending-files/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-appending-files/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-appending-files/#0)

[](https://sumproduct.com/blog/power-query-appending-files/#0 "close")

top