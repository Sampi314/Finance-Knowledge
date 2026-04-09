# The A to Z of DAX Functions – INFO.VIEW.TABLES

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-view-tables/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – INFO.VIEW.TABLES

*   July 15, 2025

The A to Z of DAX Functions – INFO.VIEW.TABLES
==============================================

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions.  This week, we look at **INFO.VIEW.TABLES**._

**_The_** _**INFO.VIEW.TABLES**_ **_function_**

![](https://sumproduct.com/wp-content/uploads/2025/06/InfoViewTables.png)

The **INFO.VIEW.TABLES** function is one of the information functions.  It returns a table with information about each table in the current model.  It operates using the following syntax:

> **INFO.VIEW.TABLES()**

The **INFO.VIEW.TABLES** function does not take any arguments.

Here are a few remarks about the **INFO.VIEW.TABLES** function:

*   the **INFO.VIEW** functions can be run in calculated tables, columns, measures and **DAX** queries
*   it can only be run by users with write permission on the semantic model and not when live connected to the semantic model in Power BI Desktop
*   it can be used in calculated tables, columns and measures of a semantic model
*   it will update when the model is refreshed
*   in DAX Studio, the user can join different DMV tables to get the same table produced by **INFO.VIEW.TABLES.**

We can write this **INFO.VIEW.TABLES** function in the DAX query view to get the information of the table:

![](<Base64-Image-Removed>)

It will return an entire table with 13 columns:

![](<Base64-Image-Removed>)

The function of each column is as follow:

*   **ID:** this is the unique ID for each column in this semantic model as an integer
*   **Name:** this is the name of each column in this semantic model as a string
*   **Model:** this is the relationship’s semantic model ID, usually a GUID
*   **DataCategory:** this is the data category of each table in this semantic model as a string
*   **Description:** this is the description of each table in this semantic model as a string
*   **IsHidden:** this is the hidden state of each table in this semantic model as True or False
*   **StorageMode:** this is the storage mode of each table in this semantic model as a string
*   **TableStorage:** this is the name and unique ID of each table in this semantic model as a string
*   **Expression:** this is the **DAX** formula of each table in this semantic model as a string.  Only applies to calculated tables
*   **ShowAsVariationOnly:**  this is the show as variation only state of each table in this semantic model as True or False
*   **IsPrivate:** this is the private state of each table in this semantic model as True or False
*   **CalculationGroupPrecedence:** this is the calculation group precedence of each table in this semantic model as an integer.  This only applies to calculation groups
*   **LineageTag:** this is the lineage tag of each table in this semantic model as a string.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section.  In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_.  If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-view-tables/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-view-tables/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-view-tables/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-view-tables/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-view-tables/#0 "close")

top