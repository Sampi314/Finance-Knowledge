# The A to Z of DAX Functions – INFO.VIEW.RELATIONSHIPS

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-view-relationships/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – INFO.VIEW.RELATIONSHIPS

*   July 8, 2025

The A to Z of DAX Functions – INFO.VIEW.RELATIONSHIPS
=====================================================

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions.  This week, we look at **INFO.VIEW.RELATIONSHIPS**._

**_The_** _**INFO.VIEW.RELATIONSHIPS**_ **_function_**

![](https://sumproduct.com/wp-content/uploads/2025/06/InfoViewRelationships.jpg)

The **INFO.VIEW.RELATIONSHIPS** function is one of the information functions.  It returns a table with information about each relationship in the current model.  It operates using the following syntax:

> **INFO.VIEW.RELATIONSHIPS()**

The **INFO.VIEW.RELATIONSHIPS** function does not take any arguments.

Here are a few remarks about the **INFO.VIEW.RELATIONSHIPS** function:

*   the **INFO.VIEW** functions can be run in calculated tables, columns, measures and **DAX** queries
*   it can only be run by users with write permission on the semantic model and not when live connected to the semantic model in Power BI Desktop
*   it can be used in calculated tables, columns and measures of a semantic model
*   it will update when the model is refreshed
*   in DAX Studio, the user can join different DMV tables to get the same table produced by **INFO.VIEW.RELATIONSHIPS.**

We can write this **INFO.VIEW.RELATIONSHIPS** function in the DAX query view to get the information of the table:

![](<Base64-Image-Removed>)

It will return an entire table with 15 columns:

![](https://sumproduct.com/wp-content/uploads/2025/06/InfoViewRelationships2-1024x378.jpg)

The function of each column is as follows:

*   **ID:** this is the unique ID for each column in this semantic model as an integer
*   **Name:** this is the name of each column in this semantic model as a string, sometimes a GUID
*   **Relationship:** this is the descriptive relationship name of each relationship in this semantic model as a string.  Includes from table and column to table and column, with cardinality and cross filter direction
*   **Model:** this is the relationship’s semantic model ID, usually a GUID
*   **IsActive:** this is the is active property of each relationship in this semantic model as True or False
*   **CrossFilteringBehavior:** this is the cross-filter behaviour or direction of each relationship in this semantic model as a string
*   **RelyOnReferentialIntegrity:** this is the rely on referential integrity property of each relationship in this semantic model as a string.  Also called assume referential integrity in the relationship editor, as it assumes all rows in the column in the many tables have a match to a row in the one side table
*   **FromTable:** this is the from table name of each relationship in this semantic model as a string
*   **FromColumn:** this is the from column name of each relationship in this semantic model as a string
*   **FromCardinality:** this is the from column cardinality of each relationship in this semantic model as a string
*   **ToTable:** this is the to table name of each relationship in this semantic model as a string
*   **ToColumn:** this is the to column name of each relationship in this semantic model as a string
*   **ToCardinality:** this is the to column cardinality of each relationship in this semantic model as a string
*   **State:** this is the state of each relationship in this semantic model as a string
*   **SecurityFilteringBehavior:** this is the security filtering behaviour of each relationship in this semantic model as a string.  This is important for row-level security roles.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section.  In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_.  If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-view-relationships/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-view-relationships/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-view-relationships/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-view-relationships/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-view-relationships/#0 "close")

top