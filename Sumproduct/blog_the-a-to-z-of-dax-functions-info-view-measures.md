# The A to Z of DAX Functions – INFO.VIEW.MEASURES

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-view-measures/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – INFO.VIEW.MEASURES

*   July 1, 2025

The A to Z of DAX Functions – INFO.VIEW.MEASURES
================================================

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions.  This week, we look at **INFO.VIEW.MEASURES**._

**_The_** _**INFO.VIEW.MEASURES**_ **_function_**

![](https://sumproduct.com/wp-content/uploads/2025/06/InfoViewMeasures.png)

The **INFO.VIEW.MEASURES** function is one of the information functions.  It returns a table with information about each measure in the current model.  It operates using the following syntax:

> **INFO.VIEW.MEASURES()**

The **INFO.VIEW.MEASURES** function does not take any arguments.

Here are a few remarks about the **INFO.VIEW.MEASURES** function:

*   the **INFO.VIEW** functions can be run in calculated tables, columns, measures and **DAX** queries
*   it can only be run by users with write permission on the semantic model and not when live connected to the semantic model in Power BI Desktop
*   it can be used in calculated tables, columns and measures of a semantic model
*   it will update when the model is refreshed
*   in DAX Studio, the user can join different DMV tables to get the same table produced by **INFO.VIEW.MEASURES.**

We can write this **INFO.VIEW.MEASURES** function in the DAX query view to get the information of the table:

![](https://sumproduct.com/wp-content/uploads/2025/06/InfoViewMeasures1.jpg)

It will return an entire table with 16 columns:

![](https://sumproduct.com/wp-content/uploads/2025/06/InfoViewMeasures2.jpg)

The function of each column is as follows:

*   **ID**: this is the unique ID for each column in this semantic model as an integer
*   **Name**: this is the name of each column in this semantic model as a string
*   **Table**: this is the table of each column in this semantic model as a string
*   **Description**: this is the description of each measure in this semantic model as a string
*   **DataType**: this is the data type of each column in this semantic model as a string
*   **Expression**: this is the **DAX** formula of each measure in this semantic model
*   **FormatString**: this is the format string of each measure in this semantic model as a string
*   **IsHidden**: this is the hidden state of each column in this semantic model as True or False
*   **State**: the state (such as valid or error) of each measure in this semantic model as a string
*   **KPIID**: the KPI ID of each measure in this semantic model as an integer
*   **IsSimpleMeasure**: the simple measure flag of each measure in this semantic model as True or False
*   **DisplayFolder**: the display folder of each measure in this semantic model as a string.  Nested folders shown with / and multiple folders separated by “**;**”
*   **DetailRowsDefinition**: the details rows definition of each measure in this semantic model
*   **DataCategory**: the data category of each measure in this semantic model as a string
*   **FormatStringDefinition**: the dynamic format string of each measure in this semantic model
*   **LineageTag**:the lineage tag of each column in this semantic model as a string.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section.  In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_.  If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-view-measures/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-view-measures/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-view-measures/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-view-measures/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-view-measures/#0 "close")

top