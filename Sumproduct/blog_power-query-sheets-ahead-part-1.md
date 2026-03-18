# Power Query: Sheets Ahead Part 1

**Source:** https://sumproduct.com/blog/power-query-sheets-ahead-part-1/

---

[Home](https://sumproduct.com/)

\> Power Query: Sheets Ahead Part 1

*   April 5, 2022

Power Query: Sheets Ahead Part 1
================================

Power Query: Sheets Ahead Part 1
================================

6 April 2022

_Welcome to our Power Query blog. This week, I look at uploading data from multiple sheets._

I have some simple monthly data:

![](<Base64-Image-Removed>)

This sheet is for January (apologies to any confused US readers!), and I have a similar sheet in the same workbook for February:

![](<Base64-Image-Removed>)

I want to create a query that not only concatenates this data, but will also include the sheets for other months as they appear if I refresh it.

I am going to create my query in another workbook. In the ‘Get & Transform’ section of the Data tab, I choose the ‘Get Data’ dropdown, where I can choose ‘Workbook’ in the File options:

![](<Base64-Image-Removed>)

I select this option and browse to the Workbook with the monthly sheets. The Navigator dialog appears, and I can view the data:

![](<Base64-Image-Removed>)

I start by selecting January, but it doesn’t matter which sheet I pick as I plan to amend the query to load all sheets. I opt, as ever, to ‘Transform Data’:

![](<Base64-Image-Removed>)

Power Query has helpfully created some steps for me, but I am only interested in the Source step:

![](<Base64-Image-Removed>)

If I click in the white space next to a ‘Table’ in **Data**, I can see the contents. Note that the headings are on the first row.

![](<Base64-Image-Removed>)

I only need the **Data** column (field), so I select this and choose to ‘Remove Other Columns’.

![](<Base64-Image-Removed>)

I choose to continue by inserting a step:

![](<Base64-Image-Removed>)

In the **Data** column, I can use the split arrows icon to expand the tables.

![](<Base64-Image-Removed>)

I have already seen that the headings are in the rows, so I choose to expand all columns. I do not need to keep any column names for prefixes.

![](<Base64-Image-Removed>)

Again, I am happy to insert a step:

![](<Base64-Image-Removed>)

My data appears. I can delete the ‘January\_Sheet’ step, since I am now looking at all the sheets:

![](<Base64-Image-Removed>)

The rest of the steps now work as before – well almost:

![](<Base64-Image-Removed>)

The red under the column names indicates one or more errors – next time I will solve this, complete my query and test it by adding more data to the workbook.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-sheets-ahead-part-1/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-sheets-ahead-part-1/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-sheets-ahead-part-1/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-sheets-ahead-part-1/#0)

[](https://sumproduct.com/blog/power-query-sheets-ahead-part-1/#0 "close")

top