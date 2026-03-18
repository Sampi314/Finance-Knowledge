# Power Query: Viewing Query Dependencies

**Source:** https://sumproduct.com/blog/power-query-viewing-query-dependencies/

---

[Home](https://sumproduct.com/)

\> Power Query: Viewing Query Dependencies

*   June 20, 2017

Power Query: Viewing Query Dependencies
=======================================

Power Query: Viewing Query Dependencies
=======================================

21 June 2017

_Welcome to our Power Query blog. Today, we look at the Power Query Dependencies Viewer._

Workbooks which are built using multiple queries can become complex, and the Power Query Dependencies Viewer is a tool which allows an overview of how each query has been built.

I will revisit the workbook I created for [Two (Queries) Become One](https://sumproduct.com/blog/power-query-two-queries-become-one/)
, where I merged some tables from my Access database:

![](https://sumproduct.com/wp-content/uploads/2025/05/a4780be6c72e7fec53bed1b096c84de8.jpg)

I double click on ‘**ACCT\_Order\_Charges\_with\_Group**‘ to edit my query. In fact, the Power Query Dependencies Viewer includes all dependencies in the workbook, so I could have used any query for this.

In the Query Editor, I choose the ‘View’ tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/3e74d2625ada9f70798f86a186143964.jpg)

On the right there is a section on ‘Dependencies’, where I can choose the ‘Query Dependencies’ button.

![](https://sumproduct.com/wp-content/uploads/2025/05/ee31a9b39825b37baa11fbecae9062c6.jpg)

Now admittedly, I haven’t chosen the most complicated model to use for my example, because I want to keep things simple. I have the option to expand the window to use the full screen, and at the bottom of the window is a scaling option, which is more useful for large complex models. There is also a ‘Layout’ dropdown.

![](https://sumproduct.com/wp-content/uploads/2025/05/9e5e92a184cc4da10b05124d38a77c05.jpg)

The ‘Layout’ default is ‘Top to Bottom’ which works well for my model. I can also try ‘Left to Right’:

![](https://sumproduct.com/wp-content/uploads/2025/05/570b7cf6723415ed3acf231bb378fefe.jpg)

The icon on the right also allows me to ‘Fit to Screen’, which is useful for complex models, particularly as there is no print option! If I want to concentrate on a particular component, right-clicking on that component allows me two more options:

![](https://sumproduct.com/wp-content/uploads/2025/05/8a797f9f0b99ab7778572dcfbf27e429.jpg)

I can make my component the centre of my window (‘Center to View’), or make the hierarchy associated with that component central to my view (‘Center Hierarchy to View’).

Many of these features have been added because I can’t do what I would intuitively like to do which is to click and drag parts of my model to display as I wish. I can click and drag, but the whole model moves as one intact unit.

One nice feature, again very useful in more complex models, is that when I click a component, the associated components are highlighted. In the screen below, I clicked on ‘**ACCT\_Order\_Charges**‘:

![](<Base64-Image-Removed>)

As there is no direct connection with ‘Items’, that component is greyed out. To show the different options that can appear for each component, I add an unrelated query which I will not load to my model.

![](<Base64-Image-Removed>)

When I view the ‘Power Query Dependencies’ now, I see the following:

![](<Base64-Image-Removed>)

So, my components are either ‘Loaded to Data Model’, ‘Loaded to worksheet’ or ‘Not loaded’. ‘Not Loaded’ means that when I created the query, I opted to make it ‘connection only’ and not load it into the data model. Note that since I have extracted the queries from different sources, the source paths are shown distinctly on the diagram.

However, ‘Not Loaded’ can be confusing. Consider the diagram below:

![](<Base64-Image-Removed>)

I have gone back to the query pane in the Excel worksheet and set the query ‘Items’ not to be loaded to the data model. It is still part of the ‘**ACCT\_Order\_Charges\_with\_Groups**‘ query, so it _is_ part of the data loaded to the worksheet.

In summary, the Power Query Dependencies Viewer is useful to get an overview of what is going on in a workbook that uses queries, but I recommend saving before removing any queries that may appear to be ‘redundant’!

Want to read more about Power Query? A complete list of all our Power Query blogs can be found [here](https://www.sumproduct.com/thought/power-query-blog-series)
. Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-viewing-query-dependencies/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-viewing-query-dependencies/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-viewing-query-dependencies/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-viewing-query-dependencies/#0)

[](https://sumproduct.com/blog/power-query-viewing-query-dependencies/#0 "close")

top