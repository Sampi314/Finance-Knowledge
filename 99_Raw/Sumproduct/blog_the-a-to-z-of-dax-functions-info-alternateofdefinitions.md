# The A to Z of DAX Functions – INFO.ALTERNATEOFDEFINITIONS

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-alternateofdefinitions/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – INFO.ALTERNATEOFDEFINITIONS

*   April 30, 2024

The A to Z of DAX Functions – INFO.ALTERNATEOFDEFINITIONS
=========================================================

Power Pivot Principles: The A to Z of DAX Functions – INFO.ALTERNATEOFDEFINITIONS
=================================================================================

30 April 2024

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **INFO.ALTERNATEOFDEFINITIONS**._

**_The_** _**INFO.ALTERNATEOFDEFINITIONS**_ **_function_**

![](<Base64-Image-Removed>)

**Dynamic Management Views** (**DMVs**) are specialised queries provided by **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** that offer an administrative view into the internal state of these systems. **DMVs** are used to retrieve metadata, monitor health and performance, and diagnose problems within the database or data model. They serve as a powerful tool for administrators and developers to gain insights into the workings of the database engine and the tabular data model, covering aspects like performance metrics, configuration settings, and the structure of database objects.

The **$System** schema **DMVs** in **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** are categorised into four \[4\] types, each serving specific purposes:

*   **DISCOVER**: requires admin privileges and provides information about the model, including details on connected sessions and environment configuration
*   **DMSCHEMA**: focused on data mining, offering insights for predictive analytics and pattern recognition, mainly used in **SSAS/AAS**
*   **MDSCHEMA**: targets multidimensional models, delivering metadata and structure from an **MDX** perspective, relevant for **OLAP** cubes and dimensions
*   **TMSCHEMA**: designed for tabular models, it provides detailed metadata about tables, columns, measures, _etc._, using **Tabular Model Scripting Language** (**TMSL**) information, crucial for **Power BI** and tabular **SSAS/AAS** models.

In the past, if we want to query those **$System** schema **DMVs** weuse external tool like **Tabular Editors** or **DAX Studio** to query them:

![](<Base64-Image-Removed>)

Now, we just need to write a simple **DAX** syntax to query those **TMSCHEMA** directly in DAX query View. In this instance, we are using _**INFO.ALTERNATEOFDEFINITIONS**_ function to query the **TMSCHEMA\_ALTERNATE\_OF\_DEFINITIONS**.

The _**INFO.ALTERNATEOFDEFINITIONS**_ function is one of the system functions. It employs the following syntax:

_**INFO.ALTERNATEOFDEFINITION**_**S()**

This function has no parameters.

Here are a few remarks about function come with **INFO** prefix:

*   it is used for querying the **DMV** (Dynamic Management Views) from the **$System schema** called **TMSCHEMA** where **TM** stands for ‘Tabular model’ and **TMSCHEMA** provides information from the tabular model
*   sometimes querying **DMVs** may fail if we do not have the appropriate permission.

We can write this **INFO.ALTERNATEOFDEFINITION****S** function on **DAX Query View** to getinformation on the **TMSCHEMA\_ALTERNATE\_OF\_DEFINITIONS**:

![](<Base64-Image-Removed>)

Itwill query the **$SYSTEM.TMSCHEMA\_ALTERNATE\_OF\_DEFINITIONS** and return an entire table with five \[5\] columns:

*   **ID**
*   **ColumnID**
*   **BaseColumnID**
*   **BaseTableID**
*   **Summarization**.

![](<Base64-Image-Removed>)

Currently, there appears to neither be documentation for this **TMSCHEMA\_ALTERNATE\_OF\_DEFINITIONS** nor**INFO.ALTERNATEOFDEFINITION****S**.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-alternateofdefinitions/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-alternateofdefinitions/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-alternateofdefinitions/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-alternateofdefinitions/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-alternateofdefinitions/#0 "close")

top