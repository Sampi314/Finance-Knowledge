# Power Query: It’s Good to Share(Point) Part 1

**Source:** https://sumproduct.com/blog/power-query-its-good-to-sharepoint-part-1/

---

[Home](https://sumproduct.com/)

\> Power Query: It’s Good to Share(Point) Part 1

*   September 24, 2024

Power Query: It’s Good to Share(Point) Part 1
=============================================

Power Query: It’s Good to Share(Point) Part 1
=============================================

25 September 2024

_Welcome to our Power Query blog. This week, I look at how to access data on SharePoint._

In this series, I am considering how to access data on SharePoint. SharePoint is used by many companies to store organised data which may then be accessed and shared throughout the organisation. I will be starting with a single file and then move on to consider combining data in a SharePoint folder.

The data for this series will come from the following SharePoint folder:

![](https://sumproduct.com/wp-content/uploads/2025/05/fe448b61482a6daa334003fc5899c5d0-1.jpg)

Regular readers will be familiar with the expense data in the form of CSV files, I’m sure!

The first challenge is how to access this data from Power Query. I open a new Excel workbook and navigate to the Data tab, where I may access the File option on the ‘Get Data’ dropdown.

![](https://sumproduct.com/wp-content/uploads/2025/05/448e24a90d936a9f47a87cc9d95392d6-1.jpg)

Choosing this option presents me with the ‘Import Data’ dialog, where I am able to locate the data since I have mapped the SharePoint site to a local folder.

![](https://sumproduct.com/wp-content/uploads/2025/05/35c5d5b51d4248320017046441a18eb7-1.jpg)

It’s possible to encounter issues. For example, if I were to continue with this method of accessing my data:

![](https://sumproduct.com/wp-content/uploads/2025/05/b60d6d4580408169db8050e94deb5d41-1.jpg)

When the data is imported, the path used means that if I were to share this workbook with another user in my company, they would need to change the path:

![](https://sumproduct.com/wp-content/uploads/2025/05/358650092fc0c873e398d21e5fc77eee-1.jpg)

I would like to create a solution that can be shared more easily. There is another option in the File section of the ‘Get Data’ dropdown:

![](https://sumproduct.com/wp-content/uploads/2025/05/c8e98ce9788850814bea4a78fc6937df-1.jpg)

If I click on the ‘From SharePoint Folder’ option, I see the following dialog:

![](https://sumproduct.com/wp-content/uploads/2025/05/902fe2ee15ab9718c9831783e37a7a34-1.jpg)

This prompts me for a URL for the SharePoint site. However, this is for a folder, not a single file. I will look at extracting data from a SharePoint folder in Part 3.

This does however make it clear that I will need a URL to access my CSV file in SharePoint. On the ‘Get Data’ dropdown, there is also a ‘From Web’ option in the ‘From Other Sources’ section:

![](<Base64-Image-Removed>)

This prompts me for the URL for a webpage, which in my case will be the CSV I wish to access:

![](<Base64-Image-Removed>)

Next time, I will look at how I can find the URL I need.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-its-good-to-sharepoint-part-1/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-its-good-to-sharepoint-part-1/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-its-good-to-sharepoint-part-1/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-its-good-to-sharepoint-part-1/#0)

[](https://sumproduct.com/blog/power-query-its-good-to-sharepoint-part-1/#0 "close")

top