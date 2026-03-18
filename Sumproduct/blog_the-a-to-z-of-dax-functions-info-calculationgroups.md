# The A to Z of DAX Functions – INFO.CALCULATIONGROUPS

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-calculationgroups/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – INFO.CALCULATIONGROUPS

*   May 28, 2024

The A to Z of DAX Functions – INFO.CALCULATIONGROUPS
====================================================

Power Pivot Principles: The A to Z of DAX Functions – INFO.CALCULATIONGROUPS
============================================================================

28 May 2024

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **INFO.CALCULATIONGROUPS**._

**_The_** _**INFO.CALCULATIONGROUPS**_ **_function_**

**Dynamic Management Views** (**DMVs**) are specialised queries provided by **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** that offer an administrative view into the internal state of these systems. **DMVs** are used to retrieve metadata, monitor health and performance, and diagnose problems within the database or data model. They serve as a powerful tool for administrators and developers to gain insights into the workings of the database engine and the tabular data model, covering aspects like performance metrics, configuration settings and the structure of database objects.

The **$System** schema **DMVs** in **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** are categorised into four \[4\] types, each serving specific purposes:

*   **DISCOVER**: requires admin privileges and provides information about the model, including details on connected sessions and environment configuration
*   **DMSCHEMA**: focused on data mining, offering insights for predictive analytics and pattern recognition, mainly used in **SSAS/AAS**
*   **MDSCHEMA**: targets multidimensional models, delivering metadata and structure from an **MDX** perspective, relevant for **OLAP** cubes and dimensions
*   **TMSCHEMA**: designed for tabular models, it provides detailed metadata about tables, columns, measures, _etc._, using **Tabular Model Scripting Language** (**TMSL**) information, crucial for **Power BI** and tabular **SSAS/AAS** models.

In the past, if we wanted to query those **$System** schema **DMVs** weused external tools like **Tabular Editors** or **DAX Studio** to query them:

![](https://sumproduct.com/wp-content/uploads/2025/06/712a93bac329c03047c75d7f8f54eca5.jpg)

Now, we just need to write a simple **DAX** based syntax to query those **TMSCHEMA** directly in DAX query view. In this instance, we are using **INFO.CALCULATIONGROUPS** function to query the **TMSCHEMA\_CALCULATION\_GROUPS**.

The **INFO.CALCULATIONGROUPS** function is one of the system functions. It employs the following syntax:

**INFO.CALCULATIONGROUPS****()**

This function has no parameters.

Based upon the _‘\[MS-SSAS-T\]: SQL Server Analysis Services Tabular Protocol’_ from Microsoft (which you may access [**here**](https://learn.microsoft.com/en-us/openspecs/sql_server_protocols/ms-ssas-t/f85cd3b9-690c-4bc7-a1f0-a854d7daecd8)
), the **CalculationGroup** object represents a collection of **CalculationItems**. It is a child of a **Table** object and requires compatibility level 1500 or higher.

We can write this **INFO.CALCULATIONGROUPS** function on DAX query viewto get the sameinformation on the **TMSCHEMA\_CALCULATION\_GROUPS**:

![](https://sumproduct.com/wp-content/uploads/2025/06/d225660e7815b4424467d3a0ba5fc9d4.jpg)

Itwill query the **$SYSTEM.****TMSCHEMA\_CALCULATION\_GROUPS** and return an entire table with five \[5\] columns:

![](https://sumproduct.com/wp-content/uploads/2025/06/f684c9cdc4bc2d229daab279c3735118.jpg)

*   **ID:** thisrepresents a reference to the object
*   **TableID:** this represents an ID-based reference to a **Table** object
*   **Description:** this is the description of the object
*   **ModifiedTime:** this represents the time that the object was last modified
*   **Precedence:** this defines an evaluation order of **CalculationGroup** objects.

It should be noted that:

*   it is used for querying the **DMV** (Dynamic Management Views) from the **$System schema** called **TMSCHEMA** where **TM** stands for ‘Tabular model’ and **TMSCHEMA** provides information from the tabular model
*   sometimes querying **DMVs** may fail if we do not have the appropriate permission.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-calculationgroups/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-calculationgroups/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-calculationgroups/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-calculationgroups/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-calculationgroups/#0 "close")

top