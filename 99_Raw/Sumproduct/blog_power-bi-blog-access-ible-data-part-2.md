# Power BI Blog: Access-ible Data – Part 2

**Source:** https://sumproduct.com/blog/power-bi-blog-access-ible-data-part-2/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Access-ible Data – Part 2

*   July 11, 2018

Power BI Blog: Access-ible Data – Part 2
========================================

Power BI Blog: Access-ible Data – Part 2
========================================

12 July 2018

Welcome back to Power BI Tips!

[Last week](https://www.sumproduct.com/blog/article/power-bi-tips/access-ible-data-part-1)
 we were just wrapping ourselves around the concept of databases. Now it’s time to use one! As indicated, we’re using the IPEDS 2016-2017 survey results.

Now before you do any work with data, you have to know what _kind_ of data you have in your database, in order to extract the necessary information. Let’s have a look at the readme document that came with this sruvey:

_Metadata Tables:_

_**Tables16** – This table lists each data table in the database by survey component. It includes table name, table title, brief description, and data year covered. It also identifies the data release (i.e., final data that has revised the provisional data or provisional, which has yet to be revised) and the date the table was released in the IPEDS “Use the data” website._

_**Vartable16** – This table lists each variable in the data table by survey component. It includes variable names, descriptions, source, data types and formats. Also, vartable16 identifies variables that were subject to revisions._

_**Valuesets16** – This table lists the value labels of each categorical variable in the database._

Ok Great! So let’s open in Access and see what we have.

Here’s a snapshot of Tables16:

![](https://sumproduct.com/wp-content/uploads/2025/05/2fd1e5c26e67a76d21e90e392dfd76e4.jpg)

Ok great! This table describes the other tables and tells us what the other tables represent.

Let’s quickly look at **Vartable16**:

![](https://sumproduct.com/wp-content/uploads/2025/05/6d8821dfbdec72727476ebc2fa06b6f1.jpg)

This table describes what the column headers mean in plain English.

From here, we can see that in table **HD2016,** column **INSTNM** is the “Institution (entity) name”.

Now to look at **Valuesets16**:

![](https://sumproduct.com/wp-content/uploads/2025/05/7897bf68a5604b85d0ee5a5ef9239b97.jpg)

This shows us what abbreviations are used where. For example, in table **HD2016**, in column 7 **STABBR** it uses letters to represent the state. The longform can be found in this table in column **valueLabel**.

Terrific! Now we know have an understanding of how this database is structured.

Let’s focus on the “Institutional Characteristics” survey. That means we’ll need to pull in tables:

*   **HD2016**
*   **CUSTOMCGIDS2016**
*   **FLAGS2016**
*   **IC2016**
*   **IC2016\_AY**
*   **IC2016\_PY**
*   **DRVIC2016**
*   **IC2016MISSION**

However, we will also need the metadata tables **Vartable16** to know what the headers are and **Valuesets16** to define any abbreviated data.

Next it is time to import the data. From the “Get Data” menu under “Databases,” select “Access database” and click “Connect”:

![](<Base64-Image-Removed>)

Select your file. This will then bring up the Navigator:

![](<Base64-Image-Removed>)

On the left, you can see all the tables in the database are represented in a check list on the left. Click on a table to preview, and click on a checkbox to select that table to be loaded in.

Scrolling through the list to try and find our tables could be very time consuming. Databases may have hundreds of tables. However, the Navigator gives us a nice filter feature. If I start typing in the search box over the table names, it will filter the table names down for easy selection.

![](<Base64-Image-Removed>)

After you’ve selected all your tables, just click Load and they should populate in your Fields pane on the right:

![](<Base64-Image-Removed>)

Pretty easy huh?

Next week we’ll start exploring how the relationships between the tables are represented in Power Bi.

_Tune in next time for more Power BI Tips!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-access-ible-data-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-access-ible-data-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-access-ible-data-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-access-ible-data-part-2/#0)

[](https://sumproduct.com/blog/power-bi-blog-access-ible-data-part-2/#0 "close")

top