# The A to Z of DAX Functions – INFO.KPIS

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-kpis/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – INFO.KPIS

*   October 29, 2024

The A to Z of DAX Functions – INFO.KPIS
=======================================

Power Pivot Principles: The A to Z of DAX Functions – INFO.KPIS
===============================================================

29 October 2024

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **INFO.KPIS**._

**_The_** _**INFO.KPIS**_ **_function_**

![](<Base64-Image-Removed>)

**Dynamic Management Views** (**DMVs**) are specialised queries provided by **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** that offer an administrative view into the internal state of these systems. **DMVs** are used to retrieve metadata, monitor health and performance, and diagnose problems within the database or data model. They serve as a powerful tool for administrators and developers to gain insights into the workings of the database engine and the tabular data model, covering aspects like performance metrics, configuration settings and the structure of database objects.

The **$System** schema **DMVs** in **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** are categorised into four \[4\] types, each serving specific purposes:

*   **DISCOVER**: requires admin privileges and provides information about the model, including details on connected sessions and environment configuration
*   **DMSCHEMA**: focused on data mining, offering insights for predictive analytics and pattern recognition, mainly used in **SSAS/AAS**
*   **MDSCHEMA**: targets multidimensional models, delivering metadata and structure from an **MDX** perspective, relevant for **OLAP** cubes and dimensions
*   **TMSCHEMA**: designed for tabular models, it provides detailed metadata about tables, columns, measures, _etc._, using **Tabular Model Scripting Language** (**TMSL**) information, crucial for **Power BI** and tabular **SSAS/AAS** models.

In the past, if we wanted to query those **$System** schema **DMVs** weused external tools like **Tabular Editors** or **DAX Studio** to query them:

![](<Base64-Image-Removed>)

The **INFO.KPIS** function is one of the system functions. It employs the following syntax:

**INFO.KPIS()**

This function has no parameters.

Based upon the _‘\[MS-SSAS-T\]: SQL Server Analysis Services Tabular Protocol’_ from Microsoft (which you may access [**here**](https://learn.microsoft.com/en-us/openspecs/sql_server_protocols/ms-ssas-t/f85cd3b9-690c-4bc7-a1f0-a854d7daecd8)
), the **KPI** object represents a **key performance indicator (KPI)** object. It is a child of a **Measure** object.

We can write this **INFO.KPIS** function on DAX query viewto get the sameinformation on the **TMSCHEMA\_KPIS**:

![](<Base64-Image-Removed>)

Itwill query the **$SYSTEM.****TMSCHEMA\_KPIS** and return an entire table with 13 columns:

![](<Base64-Image-Removed>)

*   **ID:** this is a reference to the object
*   **MeasureID:** this isan ID-based reference to a Measure object
*   **Description:** this is the description of the object
*   **TargetDescription:** this isthe description of the target value of the KPI
*   **TargetExpression:** this is an expression that evaluates to a number and indicates the goal for the KPI
*   **TargetFormatString:** this is the format string to be used when presenting the target value for the KPI
*   **StatusGraphic:** this is a string that identifies the recommended graphic to represent the status of the KPI
*   **StatusDescription:** this is a description of the Status value for the KPI
*   **StatusExpression:** this is an expression that is used to calculate the status of the KPI
*   **TrendGraphic:** this is a string that identifies the graphic to show for the trend of the KPI
*   **TrendDescription:** this is a description of the trend value of the KPI
*   **TrendExpression:** this is an expression representing the trend of the KPI
*   **ModifiedTime:** this is the time that the object was last modified.

It should be noted that:

*   it is used for querying the **DMV** (Dynamic Management Views) from the **$System schema** called **TMSCHEMA** where **TM** stand for ‘Tabular model’ and **TMSCHEMA** provides information from the tabular model
*   sometimes querying **DMVs** may fail if we do not have the appropriate permission
*   there is also a **MDSCHEMA** for **KPIS** call **MDSCHEMA\_KPIS** but its output is not the same as **TMSCHEMA\_KPIS** and **INFO.KPIS.**

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-kpis/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-kpis/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-kpis/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-kpis/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-kpis/#0 "close")

top