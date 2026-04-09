# Power Query: Appending CSV files in Excel for the web Part 1

**Source:** https://sumproduct.com/blog/power-query-appending-csv-files-in-excel-for-the-web-part-1/

---

[Home](https://sumproduct.com/)

\> Power Query: Appending CSV files in Excel for the web Part 1

*   February 25, 2026

Power Query: Appending CSV files in Excel for the web Part 1
============================================================

_Welcome to our Power Query blog.  This week, we continue to look at some of the features of Power Query in Excel for the web by appending CSV files._

Recently, I welcomed the arrival of more Power Query functionality to Excel for the web and began a series of blogs looking at the functionality available.  So far, I have enlisted the help of my imaginary salesperson: Derek.

[Last week](https://sumproduct.com/blog/power-query-power-query-in-excel-for-the-web-part-5/)
, I completed extracting data from a CSV file called **PQ\_StandardExpense\_CSV\_1:**

![](https://sumproduct.com/wp-content/uploads/2026/02/image-105.png)

Now, I shall delete the **amount** column.  I would like to bring in the next CSV file **PQ\_StandardExpense\_CSV\_2.**  Ideally, I’d like to avoidrepeating the process I used to extract **PQ\_StandardExpense\_CSV\_1**.

On the Home tab in the Power Query Editor, there is an option called ‘Recent data (Preview)’.  Let’s see if this provides a quick way to get the next file.

![](https://sumproduct.com/wp-content/uploads/2026/02/image-107.png)

If I choose ‘More…’, I should be able to see other data sources I have connected to:

![](https://sumproduct.com/wp-content/uploads/2026/02/image-109.png)

This takes me to a ‘Recent data (Preview)’ dialog:

![](https://sumproduct.com/wp-content/uploads/2026/02/image-110.png)

I might expect that this would take me to another copy of **PQ\_StandardExpense\_CSV\_1**, but it is actually the ‘Table from Examples’ I created in [Power Query in Excel for the web Part 3](https://sumproduct.com/blog/power-query-power-query-in-excel-for-the-web-part-3/)
!

![](https://sumproduct.com/wp-content/uploads/2026/02/image-112.png)

This time it has a catchy new query name: **https://sumproduct0 sharepoint com/sites/SumProductTeam/Shared%20Documents/Gener**.

I quietly delete the query.  There is a way to check what the entry in ‘Recent Data (Preview)’ will create.  Hovering over the entry allows me to check the **M** code that will be applied:

![](<Base64-Image-Removed>)

Since this will not help me, I opt for copying the **PQ\_StandardExpense\_CSV\_1** instead.  I select the query in the Queries pane, right-click and choose to create a duplicate copy since I need to use a modified source step:

![](<Base64-Image-Removed>)

I change the name of the query to **PQ\_StandardExpense\_CSV\_2** and change the Source step from this:

> **Csv.Document(Web.Contents(“https://sumproduct0.sharepoint.com/sites/SumProductTeam/Shared%20Documents/General/Kathryn/PQ\_StandardExpenses/PQ\_StandardExpense\_CSV\_1.csv”), \[Delimiter = “,”, Columns = 4, QuoteStyle = QuoteStyle.None\])**

to this:

> **Csv.Document(Web.Contents(“https://sumproduct0.sharepoint.com/sites/SumProductTeam/Shared%20Documents/General/Kathryn/PQ\_StandardExpenses/PQ\_StandardExpense\_CSV\_2.csv”), \[Delimiter = “,”, Columns = 4, QuoteStyle = QuoteStyle.None\])**

My plan is held up by a credentials issue:

![](<Base64-Image-Removed>)

I choose to ‘Configure credentials’:

![](<Base64-Image-Removed>)

I change the ‘Authentication kind’ to ‘Organizational account’, which I am currently logged in to:

![](<Base64-Image-Removed>)

I choose to Connect:

![](<Base64-Image-Removed>)

Mary’s data has been successfully extracted and if I go to the last step in the query, I see that the steps are valid for Mary’s data too:

![](<Base64-Image-Removed>)

I am ready to append the data, which is where I will pick this up next time.

Come back next time for more ways to use Power Query!            

*   [Log in](https://sumproduct.com/blog/power-query-appending-csv-files-in-excel-for-the-web-part-1/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-appending-csv-files-in-excel-for-the-web-part-1/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-appending-csv-files-in-excel-for-the-web-part-1/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-appending-csv-files-in-excel-for-the-web-part-1/#0)

[](https://sumproduct.com/blog/power-query-appending-csv-files-in-excel-for-the-web-part-1/#0 "close")

top