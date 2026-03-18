# Power Query: It’s Good to Share(Point) Part 2

**Source:** https://sumproduct.com/blog/power-query-its-good-to-sharepoint-part-2/

---

[Home](https://sumproduct.com/)

\> Power Query: It’s Good to Share(Point) Part 2

*   October 1, 2024

Power Query: It’s Good to Share(Point) Part 2
=============================================

Power Query: It’s Good to Share(Point) Part 2
=============================================

2 October 2024

_Welcome to our Power Query blog. This week, I look at how to find the URL I need to access a CSV file on SharePoint._

In this series, I am considering how to access data on SharePoint. SharePoint is used by many companies to store organised data which may then be accessed and shared throughout the organisation. I will be starting with a single file and then move on to consider combining data in a SharePoint folder.

The data for this series will come from the following SharePoint folder:

![](https://sumproduct.com/wp-content/uploads/2025/05/1c2711cb86c6d965b3f5194768048a9a-1.jpg)

Regular readers will be familiar with the expense data in the form of CSV files, I’m sure!

[Last time](https://sumproduct.com/blog/power-query-its-good-to-sharepoint-part-1/)
, I worked out how to access this data from Power Query. I realised that if I used the drive mapped to the SharePoint site, and then shared this workbook with another user in my company, they would need to change the path:

![](https://sumproduct.com/wp-content/uploads/2025/05/b58a7757fa9fb76067eedc0803c6450e-1.jpg)

To create a solution that can be shared more easily, I need to use the ‘From Web’ option in the ‘From Other Sources’ section of the ‘Get Data’ dropdown:

![](https://sumproduct.com/wp-content/uploads/2025/05/2f1d9957ca6b569a4e6ecd831797cf03-1.jpg)

This prompts me for the URL for a webpage, which in my case will be the CSV I wish to access:

![](https://sumproduct.com/wp-content/uploads/2025/05/df4fc9198f015e64294e819aeaa40f7d-1.jpg)

This week, I will begin by showing a way that will successfully find this. Then, I will show what happens if I try a different way. Let’s go back to SharePoint, and open the CSV file in Excel Online:

![](https://sumproduct.com/wp-content/uploads/2025/05/598be9d0eed9a329e7909d66f72bb608-1.jpg)

When I access the File tab, the Info allows me to ‘Open in Desktop App’:

![](https://sumproduct.com/wp-content/uploads/2025/05/829d1490ed1f5400963219da19e0faf9-1.jpg)

A confirmation dialog is displayed:

![](https://sumproduct.com/wp-content/uploads/2025/05/794e8130813717801c3d19a8500101bb-1.jpg)

In the Desktop App, I may now access the File tab. In the Info section, I see the path, and I may use the ‘Copy Path’ option to save this information.

![](<Base64-Image-Removed>)

I may now use this information in the dialog in my blank Excel workbook, using the shortcut **CTRL** + **V**:

![](<Base64-Image-Removed>)

Since this is the first time I am accessing the SharePoint website, I am prompted with further dialogs:

![](<Base64-Image-Removed>)

There are a variety of ways to access the website to import data. Typically in these blogs, I use websites that may be accessed by any user. Therefore, I have used Anonymous credentials. Since this example uses SharePoint data, I will be using my ‘Organizational account’. Let’s first look at the other options:

![](<Base64-Image-Removed>)

Some webpages require Windows credentials to access them. If the website requires this authentication, then the ‘Select which level to apply these settings to’ will determine at which level to apply the check. On some sites, subfolders may have different access credentials. The ‘Use my current credentials’ and ‘User alternate credentials’ will allow the use of datasets accessible to different users in the same workbook.

![](<Base64-Image-Removed>)

If a webpage needs a username and password to access it, data may be imported using the Basic credentials.

![](<Base64-Image-Removed>)

Some web resources require an API (Application Programming Interface) key to be entered, which may be entered on the ‘Web API’ tab.

![](<Base64-Image-Removed>)

Finally, the information we need for this example will be entered on the ‘Organizational account’ tab. The user is prompted to ‘Sign in’ to SharePoint.

Next time, I will sign in and try the URL that I have copied.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-its-good-to-sharepoint-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-its-good-to-sharepoint-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-its-good-to-sharepoint-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-its-good-to-sharepoint-part-2/#0)

[](https://sumproduct.com/blog/power-query-its-good-to-sharepoint-part-2/#0 "close")

top