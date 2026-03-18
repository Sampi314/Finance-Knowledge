# Power Pivot Principles: Introducing the Function INTERSECT

**Source:** https://sumproduct.com/blog/power-pivot-principles-introducing-the-function-intersect/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Introducing the Function INTERSECT

*   January 20, 2020

Power Pivot Principles: Introducing the Function INTERSECT
==========================================================

Power Pivot Principles: Introducing the Function INTERSECT
==========================================================

21 January 2020

_Welcome back to the Power Pivot Principles blog. This week, we are going to learn one way of joining tables together in DAX._

The SQL language offers different types of **JOIN** such as **INNER JOIN** and **OUTER JOIN**_etc_. Similar to the SQL language, DAX offers some expressions producing a result equivalent to certain types of **JOIN**. This week, we are going to learn a new function to replicate the **JOIN** effect in DAX.

**INTERSECT** returns the row intersection of two tables, retaining duplicates. It has following syntax to operate:

**INTERSECT(<table\_expression1>, <table\_expression2>)**

where:

*   <**table\_expression1**\> and <**table\_expression2**\> are any expressions that result in a table.

Consider the data tables **EmployeeTable1** and **EmployeeTable2**:

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

The data tables contain the information for employee name and department. If we want to perform the inner join (_i.e._ find matching rows) on table **EmployeeTable2** by filtering the row context we use the measure:

**INTERSECT(EmployeeTable2, EmployeeTable1)**

The function **INTERSECT** here evaluates the two table expressions and returns a table containing all of the rows in **EmployeeTable2** that are also **EmployeeTable1** (_i.e._ there are matching rows). We use the method of evaluation introduced in my previous [blog](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-summarize-function)
 to return the result table in the workbook.

So far, we have pretty much always used the ‘New Measure’ dialog. Let’s do it another way this week. If I were to right-click on the second Table and select **Table -> Edit DAX…** from the shortcut menus , we can create the syntax as follows:

![](<Base64-Image-Removed>)

The result would be:

![](<Base64-Image-Removed>)

The result returns row for records with employee name **B** and **C**. If we choose to evaluate the result based on single column, the result would return error. For example, if we rewrite the measure as:

![](<Base64-Image-Removed>)

There would be error message indicating that the query could not be assessed since a single value is used in this case, not a table expression.

![](<Base64-Image-Removed>)

That’s it for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-introducing-the-function-intersect/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-introducing-the-function-intersect/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-introducing-the-function-intersect/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-introducing-the-function-intersect/#0)

[](https://sumproduct.com/blog/power-pivot-principles-introducing-the-function-intersect/#0 "close")

top