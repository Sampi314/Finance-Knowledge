# Power BI Blog: Excel-sior – Part 1

**Source:** https://sumproduct.com/blog/power-bi-blog-excel-sior-part-1/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Excel-sior – Part 1

*   February 14, 2018

Power BI Blog: Excel-sior – Part 1
==================================

Power BI Blog: Excel-sior – Part 1
==================================

15 February 2018

Welcome back to Power BI Tips.

Last week’s we looked at the myriad of ways data can be import into Power BI, now it is time to bring some in for analysis. This blog series will be using case studies of real data and we’ll go through the steps from Get Data, cleaning data in the query editor, creating a measure wax DAX and then building a simple visualisation. We will be using free data that is available online for easy replication of the results.

Excel files are the format that most people use to store and analyse flat data. Simple formula calculations and the ability to visually format data. Today’s file comes from [NASA](https://catalog.data.gov/dataset/agency-data-on-user-facilities#topic=research_navigation)
 in the quest to go ever upward! First save [this file](https://sumproduct.com/assets/blog-pictures/2018/power-bi/02-february/nasa-labs-facilities.xlsx)
 in an easily accessible place on your computer (note we had to make slight adjustments to the original data, the errata is at the end of this post).

Choosing the “Excel” option from “Get Data”, a file dialog appears asking us to choose a file:

![](<Base64-Image-Removed>)

After clicking “Open”, the “Navigator” menu appears:

![](<Base64-Image-Removed>)

Notice that the worksheet appears, click on “Sheet1” to see the preview.

![](<Base64-Image-Removed>)

However, to bring the sheet into the dataset, the box next to the sheet in the menu must be checked.

![](<Base64-Image-Removed>)

Notice how the “Load” and “Edit” buttons are no longer greyed out. “Load” is highlighted in yellow as that is the default. Looking at the column headers, they have defaulted to numeric labelling because most of the first row of the Excel sheet is blank:

![](<Base64-Image-Removed>)

Click “Load” and let’s see how our data looks if we import it as is. You’ll notice on the right hand side, the “Fields” pane shows a **Sheet1** table with the numerically labelled columns:

![](<Base64-Image-Removed>)

On the left sidebar of the Power BI screen you can see three icons:

*   **Report**: where all your reports are and the space to create visualisations
*   **Data**: displays the current table
*   **Relationships**: displays the relationships between the tables in the dataset

Click on “Data” and our table will be displayed.

![](<Base64-Image-Removed>)

Note how the data is not ordered in the same way as it is in the file and the headers have moved. Normally in a database the order of the rows do not matter, but our table hasn’t been loaded correctly.

Next time we’ll be coming back to this dataset and going through the process of cleansing it in query editor.

See you next time for more Power BI Tips.

**Errata**

The following adjustment was made to the workbook provided by NASA:

Moved **Sheet1!$I$394:$Q$394 to Sheet1!$J$394:$R$394** and **Sheet1!$I$397:$Q$397** to **Sheet1!$J$397:$R$397**

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-excel-sior-part-1/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-excel-sior-part-1/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-excel-sior-part-1/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-excel-sior-part-1/#0)

[](https://sumproduct.com/blog/power-bi-blog-excel-sior-part-1/#0 "close")

top