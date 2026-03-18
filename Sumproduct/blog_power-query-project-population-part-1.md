# Power Query: Project Population – Part 1

**Source:** https://sumproduct.com/blog/power-query-project-population-part-1/

---

[Home](https://sumproduct.com/)

\> Power Query: Project Population – Part 1

*   April 18, 2023

Power Query: Project Population – Part 1
========================================

Power Query: Project Population – Part 1
========================================

19 April 2023

_Welcome to our Power Query blog. This week, we transform selected data from a public source._

I have found some information on population growth provided by The World Bank, which I am going to use as an example of how to transform real-life data.

![](https://sumproduct.com/wp-content/uploads/2025/05/85c0ca52048614788f328509b7e1b017.jpg)

I have downloaded the Excel file, and I am ready to analyse the data. In a new Excel file, I use ‘Get Data’ in the ‘Get & Transform Data’ section of the Data tab to navigate to ‘From Excel Workbook’:

![](https://sumproduct.com/wp-content/uploads/2025/05/ec2744a1539e416a6345094b93a2e533.jpg)

I select the workbook I want to use, and in the Navigator dialog I can choose which sheets I want to upload. I check the ‘Select multiple items’ box, which will allow me to create several queries at once:

![](https://sumproduct.com/wp-content/uploads/2025/05/f00ecf4e2b5490d4ffe21cb78805776e.jpg)

I choose to ‘Transform Data’:

![](https://sumproduct.com/wp-content/uploads/2025/05/8d4252513daf40655b53e1730329db82.jpg)

Not only has Power Query created three \[3\] queries, but for **Country**, four \[4\] steps have been created automatically. The ‘Source’ step points at the Excel file, Navigation chooses the correct sheet, ‘Promoted Headers’ makes the first row the headings, and ‘Changed Type’ has decided the type based on the data in the first 200 rows. The information at the bottom-left of the screen tells me how much data I have:

![](https://sumproduct.com/wp-content/uploads/2025/05/4fedae3880a360dd237b7a95349a78ef.jpg)

I currently have 30 columns and 265 rows. The ‘Column profiling’ is the line underneath the headings:

![](https://sumproduct.com/wp-content/uploads/2025/05/0a7a2abb4c4296bebc74fe25861ee0ee.jpg)

The amount of grey indicates the proportion of _null_ values in the column. This can help me decide whether to keep a column. **Alternative conversion factor** and **PPP survey year** are entirely populated by _null_ values. This is further indicated by the ‘Any’ data type. It is important to reduce the size of the data set by removing unnecessary columns as early as possible in the query so that the remaining steps are applied to less data. Since I have 30 columns to choose from, I will use the ‘Choose Columns’ option on the Home tab.

![](<Base64-Image-Removed>)

I need to keep any data I want to see, and data that will help me link to other tables, such as the **Country Code** and the **Currency Unit**:

![](<Base64-Image-Removed>)

I click OK to see the columns I have kept:

![](<Base64-Image-Removed>)

Power Query creates a ‘Removed Other Columns’ step. There is an important distinction between this step and the ‘Removed Columns’ step that is generated if I choose to remove a column. If more columns were to be added to the data source, then it could interfere with later steps in my query. By choosing which columns to keep, I will not pick up any additional columns.

I notice that **2-alpha code** and **WB-2 code** have the same data, so I want to delete the latter. If I delete **WB-2 code** by selecting it and pressing the **delete** key, Power Query will create a ‘Removed Columns’ step.

![](<Base64-Image-Removed>)

This step is not necessary. Instead, I delete this step and click on the cog icon next to ‘Removed Other Columns’:

![](<Base64-Image-Removed>)

I can uncheck the box for **WB-2 code** and click OK, and I have amended the step.

![](<Base64-Image-Removed>)

Next time, I will identify and remove any unnecessary rows and continue to transform the data.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-project-population-part-1/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-project-population-part-1/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-project-population-part-1/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-project-population-part-1/#0)

[](https://sumproduct.com/blog/power-query-project-population-part-1/#0 "close")

top