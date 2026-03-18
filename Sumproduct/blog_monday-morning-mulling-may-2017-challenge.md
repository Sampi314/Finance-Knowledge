# Monday Morning Mulling: May 2017 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-may-2017-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: May 2017 Challenge

*   May 28, 2017

Monday Morning Mulling: May 2017 Challenge
==========================================

Monday Morning Mulling: May 2017 Challenge
==========================================

29 May 2017

_On the final Friday of each month, set an Excel for you to puzzle over for the weekend. On the Monday, we publish one suggested solution. No-one is stating this is the best approach, it’s just the one we selected. If you don’t like it, lump it – or contact us with your preferred solution._

**_Final Friday Fix: May Challenge Recap_**

First appearing in Excel 2013, slicers are a visual filter that can be used to interact with PivotTables, PivotCharts or Tables. They are very popular with end users as they are highly intuitive requiring little more than a quick point and click.

The problem was that although are great for selecting one or more elements to filter, if there are many records to scroll through, searching is cumbersome. _There appears to be no search facility._

![](https://sumproduct.com/wp-content/uploads/2025/05/bfbd28fbae308e18c5a08dd7223ab13e.jpg)

In the example above, wouldn’t it be good if you could search for, say, everyone whose surname was “Smith”?

![](https://sumproduct.com/wp-content/uploads/2025/05/ced2391e60b07d2e78007e1ae11eb7a9.jpg)

Clearly from the screenshot I appear to have achieved it. But that’s exactly my point. I _appear_ to have achieved it. Perception is nine-tenths of the game sometimes. So how did I do it?

It’s easy – just follow these steps, assuming you are creating a slicer for a PivotTable:

*   Create a PivotTable in the usual way
*   Insert a slicer on the worksheet (click inside the PivotTable and then from the context tab ‘PivotTable Tools, Analyze’ tab on the Ribbon, select the slicer you require. You will note there is no search facility
*   Make a copy of the PivotTable and paste it close to the original PivotTable. Note that the slicer is connected to both of these summary tables
*   Remove all of the fields from the new PivotTable. If this causes an error, you have the two PivotTables too close together and you will need to separate them further apart
*   In the Field list of the second (now empty) PivotTable, add the slicer field to the ‘Filters’ area of the PivotTable
*   Now comes the clever part. Line up the slicer / adjust column widths so that it covers the filter button of the second PivotTable – except for the drop-down arrow. This gives the impression that the drop-down arrow ‘belongs’ to the slicer
*   Turn off the Autofit column widths option on both PivotTables (simply right-click on the PivotTable and select ‘PivotTable Options…’):

![](<Base64-Image-Removed>)

*   Right-click on the slicer and select ‘Size and Properties…’ from the shortcut menu. In the ‘Properties’ section, choose ‘Don’t move or size with cells’

![](<Base64-Image-Removed>)

*   These two setting changes will ensure the slicer continues to cover the second PivotTable
*   Optionally, you can hide the column that contains the field name in the ‘Filters’ area of the new PivotTable.

That’s it! You can check out our example Excel file [here](https://sumproduct.com/assets/blog-pictures/2017/monday-morning-mulling/sp-searching-slicers-example.xlsm)
.

For more tricks and tips, check out our many examples at [www.sumproduct.com/thought.](https://www.sumproduct.com/thought)

_The Final Friday Fix will return on Friday 30 June with a new Excel Challenge. In the meantime, please look out for the Daily Excel Tip on our [home page](https://www.sumproduct.com/blog)
 and watch out for a new blog every other business workday._

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-may-2017-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-may-2017-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-may-2017-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-may-2017-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-may-2017-challenge/#0 "close")

top