# The A to Z of DAX Functions – COLUMNSTATISTICS

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-columnstatistics/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – COLUMNSTATISTICS

*   October 18, 2022

The A to Z of DAX Functions – COLUMNSTATISTICS
==============================================

Power Pivot Principles: The A to Z of DAX Functions – COLUMNSTATISTICS
======================================================================

18 October 2022

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at_ **_COLUMNSTATISTICS_**_._

**_The COLUMNSTATISTICS function_**

![](<Base64-Image-Removed>)

The **COLUMNSTATISTICS** function is one of the information functions. It provides statistics regarding every column in every table in the model. This function does not have parameters in its syntax:

**COLUMNSTATISTICS()**

This function will return a table with six \[6\] columns in the following order **Table Name**, **Column Name**, **Min**, **Max**, **Cardinality** and **Max Length**. Each of these columns have different functionality:

*   **Table Name**: this is the column containing the name of the different tables within the model
*   **Column Name**: this is the column containing the name of the different columns in the different tables within the model
*   **Min**: this column shows the minimum values visible in the attribute
*   **Max**: this column shows the maximum values visible in the attribute
*   **Cardinality**: this column provides the number of unique values for each attribute in the data table
*   **Max Length**: this column shows the maximum lengths of strings visible in the attribute.

It should be further noted that:

*   the **COLUMNSTATISTICS** function returns the values and attributes to the user considering the security roles. Hence, different users can get different results querying the same model because of different security profiles
*   there will be an extra row named **RowNumber** in **Column Name** for each table which details the number of rows a table has
*   when used with a DirectQuery data source over SQL Server, it is compatible only with SQL Server 2019 or later version, because internally it uses **APPROX\_COUNT\_DISTINCT**
*   the **COLUMNSTATISTICS** function is not compatible with Excel and currently it is only compatible with Power BI, SSAS Tabular, Azure AS and SSDT.

Please have a look at the following example where we have a Power BI file that has four \[4\] different tables namely: **Sales**, **Customer**, **ProductCategory**, **ProductSubCategory**.

![](<Base64-Image-Removed>)

These tables have the following columns:

![](<Base64-Image-Removed>)

Since the output of the **COLUMNSTATISTICS** function is a table, we will write a DAX expression to create a new table with this function:

![](<Base64-Image-Removed>)

After writing the query and then hitting enter, we have the above error. This error occurred because our **COLUMNSTATISTICS** function tries to summarise itself along with other tables in the data model – just like the ouroboros eating its own tail here. In technical terms, we created a circular dependency. Thus, writing this DAX code in a new calculated table will not work out. We must find another way.

Instead of creating this as a physical table, what if we create it as a virtual table so that it is not looping back on itself in a circular dependency? Hence, we should create a measure here which I named it **COLUMNSTATISTICS\_Example**, _viz._

![](<Base64-Image-Removed>)

Don’t worry about the red squiggly line here since IntelliSense doesn’t recognise it but the function still works fine in Power BI. When we put this measure into a card visual, we will have the following figure:

![](<Base64-Image-Removed>)

This show that there are 40 lines in the column statistics table.

Now, the question is how can we extract the statistics data here? For the purposes of this example, we will use ‘DAX Studio’ to output this to a file. In ‘DAX Studio’. After we connect Power BI to ‘DAX Studio’, we can write the similar ‘DAX expression’ we wrote from the start:

![](<Base64-Image-Removed>)

But why are we having six \[6\] tables here? Aren’t we only inputting four \[4\] tables here? This is because Power BI will execute its ‘Auto date/time’ functionality which built a hidden Date table name **LocalDateTable** for the **Sales** table since only the **Sales** table has a column containing Date value. If we have more tables containing a column that contains date value Power BI will create more **LocalDateTable** tables. Whereas the **DateTableTemplate** table is just a dummy table that Power BI creates to store the Date and Time format. To avoid Power BI creating these tables we can untick the ‘Auto date/time for new files’ under Time intelligence in Settings:

![](<Base64-Image-Removed>)

After we press the Run button in the Query section it will give us the following result:

![](<Base64-Image-Removed>)

There are 40 rows returned here which matches our example using the **[COUNTROWS](https://www.sumproduct.com/blog/article/power-pivot-principles/the-a-to-z-of-dax-functions-countrows)
** function earlier. It would be fewer rows if we untick the ‘Auto date/time for new files’, but here in our example, we kept the box ticked. Now, to extract the statistics data in Excel here we simply choose **Home -> Output -> Results -> Static** then we press the Run button and save the files on the local drive. In the example here, I will save my file as **Query\_Example**. We will have the following Excel file that contains the statistics data we want to extract:

![](<Base64-Image-Removed>)

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-columnstatistics/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-columnstatistics/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-columnstatistics/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-columnstatistics/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-columnstatistics/#0 "close")

top