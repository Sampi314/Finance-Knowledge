# Monday Morning Mulling: January 2021 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-january-2021-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: January 2021 Challenge

*   January 31, 2021

Monday Morning Mulling: January 2021 Challenge
==============================================

Monday Morning Mulling: January 2021 Challenge
==============================================

1 February 2021

_On the final Friday of each month, we set an Excel / Power Pivot / Power Query / Power BI problem for you to puzzle over for the weekend. On the Monday, we publish a solution. If you think there is an alternative answer, feel free to email us. We’ll feel free to ignore you._

The first Final Friday Fix challenge of the year is to generate the list of the five most recent items using Excel formulae.

**_The Challenge_**

There is an **Order\_Database** data set which contains details of **Customer Name**, **Order Date** and **Order Volume** over the time as shown below.

![](https://sumproduct.com/wp-content/uploads/2025/05/5edbf87fdf5b18abe93119749766ff75.jpg)

To facilitate the conversation with customers upon placing an order, the operator wants to view the five most recent orders from a given customer. Specifically, when a customer is selected from the list in cell **F140** _(see image below)_, their last five order dates will appear in cells **F146:F150** in descending order, together with the related order volumes.

Can you get the list in cells **F146:F150** in just **_two_** steps?

![](https://sumproduct.com/wp-content/uploads/2025/05/d6c5b844475107950b54584415920352.jpg)

**_Suggested Solution_**

**_Step 1: Create a [Dynamic Range Name](https://www.sumproduct.com/thought/dynamic-range-names)
_****_using a formula_**

Navigate to the Formulas tab on the Ribbon and select ‘Define Name’. In the ‘New Name’ dialog, the **List\_Last\_Five\_Orders** range name should be created using the formula below:

**\=SORT(UNIQUE(FILTER(Order\_Database\[Order Date\],Order\_Database\[Customer Name\]=’The Challenge’!$F$140)),,-1)**

![](https://sumproduct.com/wp-content/uploads/2025/05/13fe089efb3fae6fd3600399592bb8e0.jpg)

Yes, we are using the [\>dynamic array formulae](https://www.sumproduct.com/thought/getting-arrays-spilling-the-beans-on-seven-new-functions)
 to make it work, so we understand this is a solution for Office 365. However, we should avail ourselves of all the features available in modern Excel.

Let’s break the formula into digestible pieces to understand how it works:

*   the **FILTER** function will get the list of all dates related to the customer selected in cell **F140**
*   a customer may make multiple orders in a day, so the **UNIQUE** function will return no duplicates in the list of dates
*   therefore, the **SORT** function will arrange this list based upon descending order (as seeing the most recent order first probably makes the most sense).

![](<Base64-Image-Removed>)

**_Step 2: Get the list of last five order dates using the [\>INDEX](https://www.sumproduct.com/thought/index-match)
_****_function_**

Given the **List\_Order\_Date**, the cells **F14****6:F150** may be filled using the **INDEX** function. In case the list of historical order date related to the customer is less than five (5), the formula should return a blank, _viz._

**\=IFERROR(INDEX(List\_Order\_Date,E146),””)**

![](<Base64-Image-Removed>)

Hence, the order volume can be calculated using the **SUMIFS** function.

You can take a look at our solution using the [attached file](https://sumproduct.com/assets/blog-pictures/2021/fff-mmm/jan/fff-jan-2021-end-v1.xlsm)
. Please share with us if you have a better solution. We won’t let anyone know, but we will steal it for the future 🙂

_The Final Friday Fix will return on Friday 26 February 2021 with a new Excel Challenge. In the meantime, have a great new year and please look out for the Daily Excel Tip on our home page and watch out for a new blog every business workday._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-january-2021-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-january-2021-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-january-2021-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-january-2021-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-january-2021-challenge/#0 "close")

top