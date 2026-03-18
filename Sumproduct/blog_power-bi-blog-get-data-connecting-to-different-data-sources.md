# Power BI Blog: Get Data – Connecting to Different Data Sources

**Source:** https://sumproduct.com/blog/power-bi-blog-get-data-connecting-to-different-data-sources/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Get Data – Connecting to Different Data Sources

*   February 7, 2018

Power BI Blog: Get Data – Connecting to Different Data Sources
==============================================================

Power BI Blog: Get Data – Connecting to Different Data Sources
==============================================================

8 February 2018

Welcome back to Power BI Tips.

Let’s start using Power BI. Power BI is a **data** visualisation tool so the first and foremost thing that needs to be done is to get some data into Power BI. When Power BI loads, the following prompt will come up:

![](https://sumproduct.com/wp-content/uploads/2025/05/9dbed5e1ddf1f649fa972a9a1fb4f9d6.jpg)

One of the first things that immediately draws your eye is the “Get Data” on the left. Press it to bring up to the prompt to import data.

![](https://sumproduct.com/wp-content/uploads/2025/05/c49cb76bb789847418911739ca664387.jpg)

There are many diverse sources that Power BI can connect to! The left hand hand side shows the broad categories of where data can be taken from. Let’s explore through each category.

![](https://sumproduct.com/wp-content/uploads/2025/05/2ce9c36f9622bc8baf90565c11b69002.jpg)

**File** shows a few different options here.

*   **Excel**: File with extensions \*.xls\* which were saved for use in Microsoft Excel
*   **Text**: Files that are plain text. CSV files are a special version of plain text files where the **C**omma is used to **S**eparate **V**alues
*   **XML**: Stands for e**X**tensible **M**arkup **L**anguage. Similar to HTML, it is used in order to shape and identify data in a human readable format. **R**ich **S**ite **S**ummary (RSS) feeds transmit data in this format (for more information about XML click [here](https://www.w3schools.com/xml/xml_whatis.asp)
    )
*   **JSON**: **J**ava**S**cript **O**bject **N**otation is another minimal, readable format for structuring data as a similar alternative to XML. It is used primarily to transmit data between a server and web application (for more information about JSON click [here](https://www.w3schools.com/js/js_json_intro.asp)
    )
*   **Folder**: For multiple files in a single directory that need to be loaded
*   **SharePoint folder**: Like **Folder** above except accessing a user’s online storage in SharePoint instead

These are all **[flat file](https://en.wikipedia.org/wiki/Flat_file_database)
** types. The data has no structure for indexing and no relationships have been defined.

![](<Base64-Image-Removed>)

**Database** has a range of options for the larger scale databases one could use instead of storing it flat in files above. There are a few standard proprietary corporate ones like Oracle, IBM, SAP, it includes standard SQL database types, as well as cloud data warehouses like Amazon and Google.

![](https://sumproduct.com/wp-content/uploads/2025/05/20bf69d10980f542815cd350da765e17.jpg)

**[Azure](https://azure.microsoft.com/en-au/overview/what-is-azure/)
** is a Microsoft computing service for developing apps on the cloud. There are a range of dedicated connectors here that are unique to Azure that Microsoft has created for their Azure users.

![](https://sumproduct.com/wp-content/uploads/2025/05/d82504a7c121fb0f9e4e10a16fa12b94.jpg)

**Online services** include connectors to a number of common web-based applications. For example, one might use Salesforce for Customer Relationship Management and MailChimp for mailing newsletters. Instead of downloading a report from each program separately, one could connect directly to each service and do complementary analysis quickly and easily, such as seeing how many of our clients currently are subscribed to the newsletters.

![](https://sumproduct.com/wp-content/uploads/2025/05/5dba5d1df28a4a7d90adf84df41ab127.jpg)

Other contains a list of different types of connections that aren’t covered by the above categories. Here’s a few of the key ones we’d like to highlight:

*   **Web**: retrieving data from a basic web page which was first explored [here](https://www.sumproduct.com/blog/article/power-query-blogs/power-query-a-world-wide-web-of-possibilities)
    
*   **OData Feed**: **O**pen **Data** Protocol is a protocol to exchange data through the web. It uses standard HTTP technologies to allow different applications to talk to each other. A short video primer to OData can be found [here](https://www.youtube.com/watch?v=dPlFNsLTPJU)
    
*   **Microsoft Exchange**: This is the Microsoft email server software centralising emails into a single database. Connect directly to the server to access email, contact and calendar data
*   **Hadoop File (HDFS)**: [Apache Hadoop](http://hadoop.apache.org/)
     is an open source software framework for storing big datasets
*   **R script**: [R](https://www.r-project.org/about.html)
     is an open source language and environment for statistical computing and graphics. It is [most common language](http://www.oreilly.com/data/free/files/stratasurvey.pdf)
     used by statisticians, analysts and scientists. This is an alternative to cleaning and formatting data in PowerQuery, it can be prepared with R and imported directly
*   **ODBC**: is an interface for accessing database management systems acting as a driver to connect to the data source. If the DBMS doesn’t already have a direct connection listed in the Database category, then connecting to the ODBC for the database allows access.
*   **OLE DB**: [OLE DB](https://msdn.microsoft.com/en-us/library/ms722784(v=vs.85).aspx)
     interfaces provide applications with uniform access to data stored in diverse information sources, or data stores – so not just relational databases but also flat text files where necessary. Microsoft had originally intended for this to replace ODBC and provide higher functionality but shelved the project in 2012 and recently started work on it again in late 2017
*   **Blank Query**: An experienced Power Query user may want to create tables from scratch using M code (for example a date table) then this is where to start.

Get Data sends the data source after it has been selected into Power Query for transformation and clean up. Our [Power Query blog](https://www.sumproduct.com/thought/power-query-blog-series)
 has covered some of the above options.

*   CSV files were covered in [Power Query – Getting Started](https://www.sumproduct.com/blog/article/power-query-blogs/power-query-3-getting-started)
    
*   Folders were covered in Power Query – [One Folder, One Query](https://www.sumproduct.com/blog/article/power-query-blogs/power-query-5-one-folder-one-query)
    

There are so many ways to Get Data into Power BI. Microsoft is continually adding connectivity to new sources all the time so check the [news](https://www.sumproduct.com/news)
 regularly for the latest Power BI update announcements.

Tune in next week for more Power BI Tips.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-get-data-connecting-to-different-data-sources/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-get-data-connecting-to-different-data-sources/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-get-data-connecting-to-different-data-sources/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-get-data-connecting-to-different-data-sources/#0)

[](https://sumproduct.com/blog/power-bi-blog-get-data-connecting-to-different-data-sources/#0 "close")

top