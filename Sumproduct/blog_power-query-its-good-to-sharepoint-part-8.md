# Power Query: It’s Good to Share(Point) Part 8

**Source:** https://sumproduct.com/blog/power-query-its-good-to-sharepoint-part-8/

---

[Home](https://sumproduct.com/)

\> Power Query: It’s Good to Share(Point) Part 8

*   November 12, 2024

Power Query: It’s Good to Share(Point) Part 8
=============================================

Power Query: It’s Good to Share(Point) Part 8
=============================================

13 November 2024

_Welcome to our Power Query blog. This week, I transform the data from a SharePoint list._

In this series, I am considering how to access data on SharePoint. SharePoint is used by many companies to store organised data which may then be accessed and shared throughout the organisation. I started with a single file and then moved on to consider combining data in a SharePoint folder.

[Last time](https://sumproduct.com/blog/power-query-its-good-to-sharepoint-part-7/)
, instead of a folder, I looked at a SharePoint list:

![](<Base64-Image-Removed>)

Along with the flattering pictures, the salespeople are responsible for creating expense files and these are linked as attachments. I would like to extract a table with the attached expenses and the responsible salesperson. Regular readers will not be surprised to discover that the expense files are CSV files, I’m sure!

I accessed the SharePoint site, and selected my list:

![](<Base64-Image-Removed>)

I chose to ‘Transform Data’ and selected the columns I wanted to keep:

![](<Base64-Image-Removed>)

Next, I need to extract the expense data from the tables. Before I extract any data, I click in the space next to a table to see what is in the columns:

![](<Base64-Image-Removed>)

Now I can see which data I need; I begin by using the expand icon next to the heading of the **AttachmentFiles** column:

![](<Base64-Image-Removed>)

I know from looking at the data in the ‘Table’ in the **AttachmentFiles** column that I need the data in **FileName**:

![](<Base64-Image-Removed>)

I see that I have different data types here. I only want the CSV files. I begin by extracting the data after the full stop, or period, to a new column. On the ‘Add Column’ tab, I choose to Extract ‘Text After Delimiter’:

![](<Base64-Image-Removed>)

I choose the full stop or period (.) as the delimiter:

![](<Base64-Image-Removed>)

This gives me a new column with the extension,. To ensure I pick up any files with extension csv or CSV, I transform this column to UPPERCASE:

![](<Base64-Image-Removed>)

I may now filter to select the CSV files:

![](<Base64-Image-Removed>)

I could add further filters to ensure that I only had the expense data if I had other CSV files attached, but this is sufficient for now. I remove the **Text After Delimiter** column that I have created:

![](<Base64-Image-Removed>)

I have the data I wanted, and I may use this to merge with other expense queries.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-its-good-to-sharepoint-part-8/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-its-good-to-sharepoint-part-8/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-its-good-to-sharepoint-part-8/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-its-good-to-sharepoint-part-8/#0)

[](https://sumproduct.com/blog/power-query-its-good-to-sharepoint-part-8/#0 "close")

top