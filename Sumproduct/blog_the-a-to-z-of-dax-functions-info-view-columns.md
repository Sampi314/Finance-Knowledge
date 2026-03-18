# The A to Z of DAX Functions – INFO.VIEW.COLUMNS

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-view-columns/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – INFO.VIEW.COLUMNS

*   June 24, 2025

The A to Z of DAX Functions – INFO.VIEW.COLUMNS
===============================================

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (**DAX**) functions.  This week, we look at **INFO.VIEW.COLUMNS**._

**_The_** _**INFO.VIEW.COLUMNS**_ **_function_**

![](https://sumproduct.com/wp-content/uploads/2025/06/InfoViewColumns.jpg)

The **INFO.VIEW.COLUMNS** function is one of the information functions.  It returns a list of all columns in the current model.  It operates using the following syntax:

> **INFO.VIEW.COLUMNS()**

The **INFO.VIEW.COLUMNS** function does not take any arguments.  Sounds like my wife.

Here are a few remarks about the **INFO.VIEW.COLUMNS** function:

*   the **INFO.VIEW** functions can be run in calculated tables, columns, measures and **DAX** queries
*   it can only be run by users with write permission on the semantic model and not when live connected to the semantic model in Power BI Desktop
*   it can be used in calculated tables, columns and measures of a semantic model
*   it will update when the model is refreshed
*   in DAX Studio, the user can join different DMV tables to get the same table produce by **INFO.VIEW.COLUMNS**.

We can write this **INFO.VIEW.COLUMNS** function in the DAX query view to get the information of the table:

![](<Base64-Image-Removed>)

It will return an entire table with 24 columns:

![](<Base64-Image-Removed>)

The function of each column is as follow:

*   **ID:** this is the unique ID for each column in this semantic model as an integer
*   **Name:** this is the name of each column in this semantic model as a string
*   **Table:** this is the table of each column in this semantic model as a string
*   **DataType:** this is the data type of each column in this semantic model as a string
*   **DataCategory:** this is the data category of each column in this semantic model as a string
*   **Description:** this is the description of each column in this semantic model as a string
*   **IsHidden:** this is the hidden state of each column in this semantic model as True or False
*   **IsUnique:** the is unique of each column in this semantic model as True of False
*   **IsKey:** the is key of each column in this semantic model as True or False
*   **IsNullable**: the is nullable of each column in this semantic model as True or False
*   **Alignment:** the alignment of each column in this semantic model as a string
*   **SummarizeBy:** the summarize by of each column in this semantic model as a string
*   **ColumnStorage:** the column storage of each column in this semantic model as a string combination of name and ID
*   **Type:** the type of each column in this semantic model as a string
*   **SourceColumn:** the source column of each column in this semantic model as a string
*   **Expression:** the **DAX** formula of calculated columns
*   **FormatString:** the format string of each column in this semantic model as a string
*   **IsAvailableInMDX:** this is available in the MDX of each column in this semantic model as True or False.  Analyse in Excel pivot tables will only show columns set to True
*   **SortByColumn:** the sort by column of each column in this semantic model as a string.  Shows as blank when sorting by itself
*   **GroupingBehaviour:** the grouping behaviour of each column in this semantic model as a string
*   **SourceProviderType:** the source provider type of each column in this semantic model as a string
*   **DisplayFolder:** the display folder of each column in this semantic model as a string.  Nested folders shown with / and multiple folders separated by
*   **AlternativeOf:** the alternate of property of each column in this semantic model as a string
*   **LineageTag:** the lineage tag of each column in this semantic model as a string.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section.  In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_.  If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-view-columns/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-view-columns/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-view-columns/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-view-columns/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-view-columns/#0 "close")

top