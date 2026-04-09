# Power Pivot Principles: Introducing the ALLNOBLANKROW Function

**Source:** https://sumproduct.com/blog/power-pivot-principles-introducing-the-allnoblankrow-function/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Introducing the ALLNOBLANKROW Function

*   October 5, 2020

Power Pivot Principles: Introducing the ALLNOBLANKROW Function
==============================================================

Power Pivot Principles: Introducing the ALLNOBLANKROW Function
==============================================================

6 October 2020

_Welcome back to the Power Pivot Principles blog. This week, we will talk about the ALLNOBLANKROW in DAX._

The **ALLNOBLANKROW** returns all the rows except for the blank rows in a table, or all the values in a column, ignoring any filters that may have been applied. This function has the following syntax:

**ALLNOBLANKROW({table / column\[,column\[,column\[,…\]\]\]})**

in which:

*   **table**: the table over which all context filters are removed
*   **column**: a column over which all context filters are removed.

The return value, in particular, is a table, when the passed parameter was a table, or a column of values, when the passed parameter was a column.

The **ALLNOBLANKROW** function does not consider truly blank rows in a table, but only handles the blank row that is a special case generated in a parent table, when one or more of the child tables in the relationship contain non-matching values or blank values. Clear as mud?

Let’s consider an example. Imagine there is a **Store\_ID** table which lists five store IDs and their respective names:

![](<Base64-Image-Removed>)

Also, there is a **Car\_Sales\_Record** table which records the sales of car by **Date**, **Store ID** and **Sales Person**:

![](<Base64-Image-Removed>)

The above two tables are already loaded into the Power Pivot Data Model and a relationship is set up between them, by connecting the **Store ID** fields in the two tables, _viz._

![](<Base64-Image-Removed>)

Before we do anything, we may notice that there are only five store details recorded in the **Store\_ID** table. Meanwhile, car sales are listed in _six_ stores in the **Car\_Sales\_Record** table. There is one store missing information here. Therefore, when we create a PivotTable working with **Store Name** field, a **(blank)** cell will be displayed:

![](<Base64-Image-Removed>)

We will create a measure to count the table rows using the **ALLNOBLANKROW** function:

**Count\_AllNoBlankRow:=COUNTROWS(ALLNOBLANKROW(Store\_ID\[Store Name\]))**

![](<Base64-Image-Removed>)

To compare, we will create another measure using the **[ALL](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-all)
** function:

**Count\_All:=COUNTROWS(ALL(Store\_ID\[Store Name\]))**

![](<Base64-Image-Removed>)

The results show a difference of one (1) row in the table rows count.

The DAX formula using the **ALLNOBLANKROW** function returns five (5). This is because the number of rows in the parent **Store\_ID** table is five (5), but there are entries in the **Car\_Sales\_Record** table for an unaccounted store, _i.e._ store number 6 is not present in the **Store\_ID** table. This is not counted, as the **ALLNOBLANKROW** function excludes blank rows when it is counting.

Meanwhile, the DAX formula using the **ALL** function return six (6). This is because the number of rows in the parent **Store\_ID** table is five (5), but again, there are entries in the **Car\_Sales\_Record** table for store number 6 that are not present in the **Store\_ID** table.

One thing worth noting is that the **ALLNOBLANKROW** function does not count any truly blank rows: it only handles the special blank row on the parent table. We will create two other measures to count table rows. Instead of counting **Store Name** from the **Store\_ID** table, we will count **Store ID** from the **Car\_Sales\_Record** table:

**Count\_AllNoBlankRow\_Car\_Sales:=COUNTROWS(ALLNOBLANKROW(Car\_Sales\_Record\[Store ID\]))**

**Count\_All\_Car\_Sales:=COUNTROWS(ALL(Car\_Sales\_Record\[Store ID\]))**

![](<Base64-Image-Removed>)

Now the two measures return the same results, which is because the **ALLNOBLANKROW** function does not count truly blank rows in a table, but only handles the blank row that is a special case generated in a parent table, when one or more of the child tables in the relationship contain non-matching values or blank values.

To extend this example, we can revisit the **[VALUES](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-values-function)
** and **[DISTINCT](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-distinct-function)
** functions:

**Count\_Values:=COUNTROWS(VALUES(Store\_ID\[Store Name\]))**

**Count\_Distinct:=COUNTROWS(DISTINCT(Store\_ID\[Store Name\]))**

![](<Base64-Image-Removed>)

The **VALUES** function counts and displays blank values, whereas the **DISTINCT** function does not. You can read more about the comparison between the **VALUES** and **DISTINCT** functions [here](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-distinct-vs-values)
.

That’s it for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-introducing-the-allnoblankrow-function/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-introducing-the-allnoblankrow-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-introducing-the-allnoblankrow-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-introducing-the-allnoblankrow-function/#0)

[](https://sumproduct.com/blog/power-pivot-principles-introducing-the-allnoblankrow-function/#0 "close")

top