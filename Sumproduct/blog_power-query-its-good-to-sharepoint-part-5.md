# Power Query: It’s Good to Share(Point) Part 5

**Source:** https://sumproduct.com/blog/power-query-its-good-to-sharepoint-part-5/

---

[Home](https://sumproduct.com/)

\> Power Query: It’s Good to Share(Point) Part 5

*   October 22, 2024

Power Query: It’s Good to Share(Point) Part 5
=============================================

Power Query: It’s Good to Share(Point) Part 5
=============================================

23 October 2024

_Welcome to our Power Query blog. This week, I complete the extraction of data from a folder on SharePoint._

In this series, I am considering how to access data on SharePoint. SharePoint is used by many companies to store organised data which may then be accessed and shared throughout the organisation. I will be starting with a single file and then move on to consider combining data in a SharePoint folder.

The data for this series will come from the following SharePoint folder:

![](https://sumproduct.com/wp-content/uploads/2025/05/9e33b2e79d47d5204877f243a5f9cad3-1.jpg)

Regular readers will be familiar with the expense data in the form of CSV files, I’m sure!

In [Part 3](https://sumproduct.com/blog/power-query-its-good-to-sharepoint-part-3/)
, I completed the task of extracting a single CSV file from SharePoint into Power Query.

![](https://sumproduct.com/wp-content/uploads/2025/05/7d55bdd998da3d33d515c7077554a0d7-1.jpg)

[Last time](https://sumproduct.com/blog/power-query-its-good-to-sharepoint-part-4/)
, I used the ‘From SharePoint Folder’ option to combine all the CSVs in the SharePoint folder

![](https://sumproduct.com/wp-content/uploads/2025/05/611afcda09a8048aca4798c1bb716ac9-1.jpg)

I filtered **Folder Path** to select only the data in the required folder:

![](https://sumproduct.com/wp-content/uploads/2025/05/395299fd0044b192db33470cef457263-1.jpg)

These are the files in my folder, and I may now make the solution robust by selecting the **Extension** column and transforming it to UPPERCASE in the Transform section of the right-click menu:

![](https://sumproduct.com/wp-content/uploads/2025/05/9e314e1ad23babdf40398585a0277c25-1.jpg)

Next, I add to ‘Text Filters’ from the filter button dropdown:

![](https://sumproduct.com/wp-content/uploads/2025/05/c775b8f7f3544d164248fe84ff09d212-1.jpg)

I select only those files with **Extension ‘**.CSV’.

![](https://sumproduct.com/wp-content/uploads/2025/05/ac1fae89c9371cbaabefe8a57755a841-1.jpg)

I may now select the **Content** column and choose to remove the other columns:

![](https://sumproduct.com/wp-content/uploads/2025/05/861de2b81f2b3e40ac2f7bcc7b08e263-1.jpg)

Finally, I use the ‘Combine Files’ icon next to the column heading to combine the data. Whilst this takes longer than combining local files, as Power Query accesses the SharePoint folder, the process is the same. The ‘Combine Files’ dialog appears:

![](<Base64-Image-Removed>)

When I click ‘OK’, the helper queries are created and the data is combined in the original query:

![](<Base64-Image-Removed>)

The data may then be transformed in the usual way.

Accessing data in SharePoint is simple once the method to access the data has been carried out correctly. The process may be slower, depending upon the SharePoint site being used, but using the URL to access the data means that the same current data may be accessed by other users in the organisation when using the same workbook. I was also able to access the data whilst I had one of the CSV files open in Excel, but this may vary depending upon how the SharePoint site has been set up.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-its-good-to-sharepoint-part-5/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-its-good-to-sharepoint-part-5/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-its-good-to-sharepoint-part-5/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-its-good-to-sharepoint-part-5/#0)

[](https://sumproduct.com/blog/power-query-its-good-to-sharepoint-part-5/#0 "close")

top