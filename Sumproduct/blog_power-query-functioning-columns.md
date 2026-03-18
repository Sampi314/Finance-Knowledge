# Power Query: Functioning Columns

**Source:** https://sumproduct.com/blog/power-query-functioning-columns/

---

[Home](https://sumproduct.com/)

\> Power Query: Functioning Columns

*   July 30, 2019

Power Query: Functioning Columns
================================

Power Query: Functioning Columns
================================

31 July 2019

_Welcome to our Power Query blog. Today, I create a function to add a column to a table._

_Back in [Power Query: Splitting Up is Not so Hard to Do](https://www.sumproduct.com/blog/article/power-query-blogs/power-query-splitting-up-is-not-so-hard-to-do)
_, I divided a column containing a full name into first and last name columns, _viz._

![](<Base64-Image-Removed>)

Since this is a common scenario, I want to create a function that I can apply whenever I have a full name column that I need to split up.

![](<Base64-Image-Removed>)

I need to convert the **M** code I used to split my column into a function. My original code looked like this:

**let**

    **Source = Excel.CurrentWorkbook(){\[Name=”Table8″\]}\[Content\],**

    **#”Changed Type” = Table.TransformColumnTypes(Source,{{“Employee”, type text}}),**

    **#”Split Column by Delimiter” = Table.SplitColumn(#”Changed Type”,”Employee”,Splitter.SplitTextByDelimiter(” “, QuoteStyle.None),{“Employee.1”, “Employee.2”}),**

    **#”Changed Type1″ = Table.TransformColumnTypes(#”Split Column by Delimiter”,{{“Employee.1”, type text}, {“Employee.2”, type text}})**

**in**

    **#”Changed Type1″**

To begin, I create a new blank query from the ‘From Other Sources’ option of the dropdown from ‘New Query’ on the ‘Get & Transform’ section of the Data tab.

![](<Base64-Image-Removed>)

I simplify the code and rename my function to **fnSplitName**.

![](<Base64-Image-Removed>)

The **M** code I have used is:

**\= (mytable as table,fullname as text, column1 as text, column2 as text) => Table.SplitColumn(mytable,fullname,Splitter.SplitTextByDelimiter(” “, QuoteStyle.None),{column1, column2})**

This code transforms a given column into two columns by splitting at the first space. I can now use it to transform my original data.

![](<Base64-Image-Removed>)

When I invoke, I get a new query with my results:

![](<Base64-Image-Removed>)

I could also use the function in my query:

![](<Base64-Image-Removed>)

When I execute this step, I get the following results:

![](<Base64-Image-Removed>)

I could tweak my function to create a copy of the column to be split if I wanted to keep it, and this function will work for any column that I want to split into two using a space. By adding more parameters, I could make it more flexible, but there is a risk of making the function too complex to be useful.

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-functioning-columns/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-functioning-columns/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-functioning-columns/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-functioning-columns/#0)

[](https://sumproduct.com/blog/power-query-functioning-columns/#0 "close")

top