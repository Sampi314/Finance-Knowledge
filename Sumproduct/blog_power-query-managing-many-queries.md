# Power Query: Managing Many Queries

**Source:** https://sumproduct.com/blog/power-query-managing-many-queries/

---

[Home](https://sumproduct.com/)

\> Power Query: Managing Many Queries

*   October 24, 2017

Power Query: Managing Many Queries
==================================

Power Query: Managing Many Queries
==================================

25 October 2017

_Welcome to our Power Query blog. This week I look at the options available to organise queries within a workbook._

When I have spent some time in a particular Excel workbook, transforming and loading my data using Power Query, I can find that I have created quite a few different queries. To avoid confusing anyone opening the workbook, whether that is my future self or another analyst, there are some techniques I can use. I already looked at how to get an overview of the connections between my queries in Viewing Query Dependencies, but there are other ways I can make it easier to get a quick overview of my queries.

![](https://sumproduct.com/wp-content/uploads/2025/05/fcc5dbbb73fdaa3aaf50976f85232be2.jpg)

Above, I have a workbook where I have created nine queries – this is obviously a small example, but there is a limit to how much admin anyone wants to see!

The first thing to notice is the ‘QUERY’ tab within the ‘TABLE TOOLS’ tab (this is a context specific tab that appears when you click on one or more cells in the loaded table). This only appears when the table has a linked query, and it gives access to a number of options. The ‘QUERY’ tab will not allow me to access queries that are not linked to my table. For example, if I need to access ‘**FormatExpenseType**‘, then I need to select my query and right click to see the options available.

![](https://sumproduct.com/wp-content/uploads/2025/05/ea58455092183a9c3a5b31952904c89b.jpg)

For those queries linked to my table I have access to the ‘QUERY TAB’ containing the main query options, which are grouped into ‘Edit’, ‘Load’, ‘Reuse’, ‘Combine’ and ‘Power BI’. For this example, I am interested in how I can make my queries easier to understand and use, so I want to look at the ‘Properties’ in the ‘Edit’ section:

![](https://sumproduct.com/wp-content/uploads/2025/05/e87784538415f3fd72741a83b997b3f2.jpg)

In this pop-up screen I can describe my query in more detail, and give it a better name if I wish. There is also a little checkbox for ‘Fast Data Load’ which is worth a look. This is for those queries that are a priority. As Microsoft puts it:

The default behaviour_(sic)_ is “Background Data Load,” but now users can instead choose the “Fast Data Load” mode in the Options dialog. When loading a query using the “Fast Data Load” mode, your query will take less time to load, however, Excel may be unresponsive for long periods of time during the upload.

So basically, it depends upon which is more important to me: running my query or continuing with other tasks. I am going to leave the queries in this particular workbook loading as a background task, but it’s good to know I have a choice.

Assuming I have given all my queries nice names and detailed descriptions, is there anything else I can

![](<Base64-Image-Removed>)

There are a number of options towards the bottom of the list that can help. I can move a query up or down the list, or I can keep my queries in groups, which are essentially folders of queries. As I currently have no groups set up in my workbook, my only option is to create a new one. Therefore, I will put ‘**Merge Expense Type**‘ into a new group called ‘**Expense Type Calculations**‘.

![](<Base64-Image-Removed>)

I click ‘OK’ to create my new group.

![](<Base64-Image-Removed>)

Not only has my ‘**Merge Expense Type**‘ been added to my newly created ‘**Expense Type Calculations**‘ group, but another group, ‘**Other Queries**‘, has been created to house the rest of my queries. Next, I want to add the ‘**FormatExpenseType**‘ function to my new group too:

![](<Base64-Image-Removed>)

This time the group appears for me to select; I continue creating groups for my other queries.

![](<Base64-Image-Removed>)

Now all my queries are in groups, and I still have my ‘**Other Queries**‘ group for new queries.

![](<Base64-Image-Removed>)

I also have options available when I select a group:

![](<Base64-Image-Removed>)

I can add my group to another group, either new or existing, which will create subfolders. To undo this, I can ‘Move to Top Level’ again. I can also ungroup the queries in the selected group. I have to be careful when I delete a group though, as it will also delete any queries in my group!

I can also control the order my groups appear in by moving up or down to alter their position in the queries pane.

![](<Base64-Image-Removed>)

Now my queries are much easier to follow when I come back to this workbook in a few months’ time!

Want to read more about Power Query? A complete list of all our Power Query blogs can be found [here](https://www.sumproduct.com/thought/power-query-blog-series)
.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-managing-many-queries/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-managing-many-queries/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-managing-many-queries/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-managing-many-queries/#0)

[](https://sumproduct.com/blog/power-query-managing-many-queries/#0 "close")

top