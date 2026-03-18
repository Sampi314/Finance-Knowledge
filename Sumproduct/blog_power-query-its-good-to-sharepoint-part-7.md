# Power Query: It’s Good to Share(Point) Part 7

**Source:** https://sumproduct.com/blog/power-query-its-good-to-sharepoint-part-7/

---

[Home](https://sumproduct.com/)

\> Power Query: It’s Good to Share(Point) Part 7

*   November 5, 2024

Power Query: It’s Good to Share(Point) Part 7
=============================================

Power Query: It’s Good to Share(Point) Part 7
=============================================

6 November 2024

_Welcome to our Power Query blog. This week, I look at extracting data from a SharePoint list._

In this series, I am considering how to access data on SharePoint. SharePoint is used by many companies to store organised data which may then be accessed and shared throughout the organisation. I started with a single file and then moved on to consider combining data in a SharePoint folder.

This time, instead of a folder, I am looking at a SharePoint list:

![](https://sumproduct.com/wp-content/uploads/2025/05/fdd8aff572a7bf5c338aaef8b8373935-1.jpg)

Along with the flattering pictures, the salespeople are responsible for creating expense files and these are linked as attachments. I would like to extract a table with the attached expenses and the responsible salesperson. Regular readers will not be surprised to discover that the expense files are CSV files, I’m sure!

I start in my Excel workbook, where I access the option I need from the ‘From Other Sources’ tab of the ‘Get Data’ dropdown:

![](https://sumproduct.com/wp-content/uploads/2025/05/dd57be3afd0fcf1f4feceafa15305b4a-1.jpg)

In this series on SharePoint data, it’s no surprise to see that we need to enter the URL of the SharePoint site:

![](https://sumproduct.com/wp-content/uploads/2025/05/c194247488253d2359a320042f7d8f68-1.jpg)

As we discovered in [Part 4](https://sumproduct.com/blog/power-query-its-good-to-sharepoint-part-4/)
, this is:

**https://sumproduct0.sharepoint.com/sites/SumProductTeam**

I enter this and click ‘OK’. If necessary, I follow the same process to log in, and choose to Connect:

![](https://sumproduct.com/wp-content/uploads/2025/05/6d171677ac970d87078b3e7c3788654e-1.jpg)

I could select multiple lists if I wish, but I only need ‘Power Query List’:

![](https://sumproduct.com/wp-content/uploads/2025/05/ddf88725a7c4cc1a98979098e76a65b0-1.jpg)

There are numerous columns I don’t need. I choose to ‘Transform Data’:

![](https://sumproduct.com/wp-content/uploads/2025/05/e932093714a47c084652f1297823aa86-1.jpg)

I have the Source step and the Navigation step that I would expect, but the third generated step is ‘Renamed Columns’. This behaviour appears to be prompted by this particular source type. Let’s start by looking at the Source step:

![](<Base64-Image-Removed>)

I use the URL and the **Sharepoint.Tables()** function that I discovered [last week](https://sumproduct.com/blog/power-query-its-good-to-sharepoint-part-6/)
. This has produced a table containing an identifier **Id**, the **Title**, and a table of data.

The Navigation step then expands the table for ‘Power Query List’.

![](<Base64-Image-Removed>)

This gives me two \[2\] columns with the same name, **Id** and **ID**.

The ‘Renamed Columns’ step renames **ID** to **ID.1** and is generated to avoid any confusion.

**\= Table.RenameColumns(#”bb59a983-0cde-417a-91a0-d806d1a8d020″,{{“ID”,  
“ID.1”}})**

I use ‘Choose Columns’ from the Home tab to decide which columns I need:

![](<Base64-Image-Removed>)

I can see I need to keep the **Title** column, as that is the salesperson responsible for the expenses. I also need **AttachmentFiles**:

![](<Base64-Image-Removed>)

I click OK, and the other columns are removed:

![](<Base64-Image-Removed>)

Next time, I will continue transforming this data.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-its-good-to-sharepoint-part-7/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-its-good-to-sharepoint-part-7/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-its-good-to-sharepoint-part-7/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-its-good-to-sharepoint-part-7/#0)

[](https://sumproduct.com/blog/power-query-its-good-to-sharepoint-part-7/#0 "close")

top