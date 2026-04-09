# The A to Z of DAX Functions – INFO.STORAGETABLECOLUMNSEGMENTS

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-storagetablecolumnsegments/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – INFO.STORAGETABLECOLUMNSEGMENTS

*   May 13, 2025

The A to Z of DAX Functions – INFO.STORAGETABLECOLUMNSEGMENTS
=============================================================

Power Pivot Principles: The A to Z of DAX Functions – INFO.STORAGETABLECOLUMNSEGMENTS
=====================================================================================

13 May 2025

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **INFO.STORAGETABLECOLUMNSEGMENTS**._

**_The_** _**INFO.STORAGETABLECOLUMNSEGMENTS**_ **_function_**

![](https://sumproduct.com/wp-content/uploads/2025/06/dfb6fe4c8fa5cb422f78f626c0b3b79a.jpg)

**Dynamic Management Views** (**DMVs**) are specialised queries provided by **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** that offer an administrative view into the internal state of these systems. **DMVs** are used to retrieve metadata, monitor health and performance, and diagnose problems within the database or data model. They serve as a powerful tool for administrators and developers to gain insights into the workings of the database engine and the tabular data model, covering aspects like performance metrics, configuration settings and the structure of database objects.

The **$System** schema **DMVs** in **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** are categorised into four \[4\] types, each serving specific purposes:

*   **DISCOVER**: requires admin privileges and provides information about the model, including details on connected sessions and environment configuration
*   **DMSCHEMA**: focused on data mining, offering insights for predictive analytics and pattern recognition, mainly used in **SSAS/AAS**
*   **MDSCHEMA**: targets multidimensional models, delivering metadata and structure from an **MDX** perspective, relevant for **OLAP** cubes and dimensions
*   **TMSCHEMA**: designed for tabular models, it provides detailed metadata about tables, columns, measures, _etc._, using **Tabular Model Scripting Language** (**TMSL**) information, crucial for **Power BI** and tabular **SSAS/AAS** models.

In the past, if we wanted to query those **$System** schema **DMVs** weused external tools like **Tabular Editors** or **DAX Studio** to query them:

![](<Base64-Image-Removed>)

The _**INFO.STORAGETABLECOLUMNSEGMENTS**_ function is one of the system functions. It employs the following syntax:

**INFO.STORAGETABLECOLUMNSEGMENTS  
(\[RestrictionName1\], \[RestrictionValue1\], …)**

There are two \[2\] main arguments in this function (excluding numbering):

*   **RestrictionName:** this argument is optional and repeatable this represents the restriction name
*   **RestrictionValue:** this argument is optional and repeatable this represents the restriction value.

Based upon the _‘\[MS-SSAS\]: SQL Server Analysis Services Tabular Protocol’_ from Microsoft (which you may access [**here**](https://learn.microsoft.com/en-us/openspecs/sql_server_protocols/ms-ssas/854a72f2-d637-4be3-b60f-6a44422e80c9)
), this schema rowset returns information about the column segments used for storing data for in-memory tables.

We can write this _**INFO.STORAGETABLECOLUMNSEGMENTS**_ function in DAX query viewto get the sameinformation on the **DISCOVER\_STORAGE\_TABLE\_COLUMN\_SEGMENTS**:

![](https://sumproduct.com/wp-content/uploads/2025/06/fa2c4b95d3183bc3ef3706bd169365e6.jpg)

Itwill query the **$SYSTEM.****DISCOVER\_STORAGE\_TABLE\_COLUMN\_SEGMENTS** and return an entire table with 20 columns:

![](https://sumproduct.com/wp-content/uploads/2025/06/01812054b7bee5de13c7ebc7e52ad055.jpg)

*   **DATABASE\_NAME:** this is the name of the database
*   **CUBE\_NAME:** the name of the cube
*   **MEASURE\_GROUP\_NAME:** this is the name of the measure group
*   **PARTITION\_NAME:** this is not mentioned in the documents
*   **DIMENSION\_NAME:** this is the name of the dimension
*   **TABLE\_ID:** this the ID of the table
*   **COLUMN\_ID:** this the ID of the column
*   **SEGMENT\_NUMBER:** this is the numeric value of the segment
*   **TABLE\_PARTITION\_NUMBER:** this is the numeric value of the partition table
*   **RECORDS\_COUNT:** this represents the number of records
*   **ALLOCATED\_SIZE:** this is the size of allocated data
*   **USED\_SIZE:** this is the size of the data used
*   **COMPRESSION\_TYPE:** this is the type of compression. Currently, this value is always “NOSPLIT”. The compression value is intended for internal server use only
*   **BITS\_COUNT:** this is the count of bits required to store the Data IDs
*   **BOOKMARK\_BITS\_COUNT:** this is the bookmark count of BITS
*   **VERTIPAQ\_STATE:** this is the state of the VertiPaq compression for this column segment. The value is one of the following:
    *   COMPLETED: this is the VertiPaq compression completed successfully
    *   TIMEBOXED: this is he VertiPaq compression was timeboxed
    *   SKIPPED: this is the VertiPaq compression was skipped
*   **ISPAGEABLE:** when true, MAY indicate that the segment is pageable; otherwise, false. If the paging feature is not supported on the server, the value is NULL
*   **ISRESIDENT:** when true, MAY indicate that the segment is resident; otherwise, false. If the paging feature is not supported on the server, the value is NULL
*   **TEMPERATURE:** when the segment is pageable and is resident, MAY indicate the scaled numeric value of the frequency of segment access considering the last access time and usage; otherwise, NULL
*   **LAST\_ACCESSED:** For a pageable segment, MAY indicate the last access time of a segment if it has been paged in at least once; otherwise, NULL. For a non-pageable segment, the value is always NULL.

It should be noted that:

*   it is used for querying the **DMV** (Dynamic Management Views) from the **$System schema** called **TMSCHEMA** where **TM** stands for ‘Tabular model’ and **TMSCHEMA** provides information from the tabular model
*   sometimes querying **DMVs** may fail if we do not have the appropriate permission.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-storagetablecolumnsegments/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-storagetablecolumnsegments/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-storagetablecolumnsegments/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-storagetablecolumnsegments/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-storagetablecolumnsegments/#0 "close")

top