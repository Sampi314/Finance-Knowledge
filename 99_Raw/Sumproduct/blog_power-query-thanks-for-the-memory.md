# Power Query: Thanks for the Memory

**Source:** https://sumproduct.com/blog/power-query-thanks-for-the-memory/

---

[Home](https://sumproduct.com/)

\> Power Query: Thanks for the Memory

*   May 1, 2018

Power Query: Thanks for the Memory
==================================

Power Query: Thanks for the Memory
==================================

2 May 2018

_Welcome to our Power Query blog. This week, I look at what to do if you are short of memory._

At the beginning of this series of blogs I described the versions of Excel required to be able to access Power Query (or Get and Transform). This was in [Power Query: Installing and Updating](https://sumproduct.com/blog/power-query-installing-and-updating/)
. In this blog, I mentioned choosing the right version of Power Query in Excel 2013 that matched the bit version of the installed Excel (which will either be 32-bit (x86) or 64-bit (x64)).

![](<Base64-Image-Removed>)

This information can be found on the ‘File’ menu from the any Excel spreadsheet. The ‘About Microsoft Excel’ is found in the ‘Account’ section. The Excel 2016 bit version can be found in the same menu location.

![](<Base64-Image-Removed>)

So why is this important? Well, if I am running a 32-bit version, then I might see this:

![](<Base64-Image-Removed>)

I happen to have complete control over the versions of Excel I am running, but if I were stuck with a 32-bit version, then I would need to turn to the settings in Power Query that allow me to limit the memory being used. I covered all the query settings available in [Power Query: Querying Query Options](https://sumproduct.com/blog/power-query-querying-query-options/)
, but I will revisit some of them here.

Whilst building a Power Query model, it’s not always necessary to load queries immediately to a worksheet – this can use a lot of memory. If I am happy just to see the preview rows then I can disable loading to the worksheet or to the Data Model. I can access the ‘Query Options’ screen from the ‘File’ tab in any query:

![](<Base64-Image-Removed>)

I can also access the ‘Query Options’ screen from the ‘Get and Transform’ section from the ‘New Query’ option dropdown. Whichever way I access the screen, the options will apply to loading all queries in my workbook or all the queries on my computer, depending upon whether I pick the ‘Current Workbook’ or ‘Global’ section.

![](<Base64-Image-Removed>)

The first option in both sections is all about data loading and I can choose to ‘Specify custom default load settings’:

![](<Base64-Image-Removed>)

If I remove the default action to load to worksheet, then my next query will show this. I create a new query from my Access database and choose to load it.

![](<Base64-Image-Removed>)

My data does not appear in the worksheet, it appears as ‘connection only’.

![](<Base64-Image-Removed>)

I can perform other options such as merging with queries and appending to queries (the options are shown in the screen below). When I am ready to load my data, I can right click on my query.

![](<Base64-Image-Removed>)

The ‘Load To’ option brings up the same sub-screen that I normally see when I choose the ‘Close and load to’ options from the Query Editor.

![](<Base64-Image-Removed>)

This shows the current default option – to create a connection and not to add the data to the data model. Once I choose to create a table or add the data to the data model, then I access the memory required for this task.

There is also the option to set and clear the cache from the Query Options screen. Whilst the maximum size can be controlled, it’s not recommended to go below 32 MB. Power Query itself has in-built limitations as defined by Microsoft in their help pages:

*   Soft limit of persistent cache. A soft limit can be exceeded for periods of time: 4GB
*   Individual entries in the cache: 1GB

However, if running the 32-bit version of Excel, then the 1GB is the cache limit. The recommendation would be to have the 64-bit version of Excel, but there are a few more settings that can help with memory issues, once loading is required.

![](<Base64-Image-Removed>)

Turning on the ‘Fast Data Load’ at Global level will concentrate memory on that task, although the rest of Excel will not be responsive.

![](<Base64-Image-Removed>)

At ‘Current Workbook’ level, unchecking the box to ‘allow data preview to download in the background’ will also concentrate memory on the main task.

![](<Base64-Image-Removed>)

Finally, choosing to ‘Ignore the Privacy Levels and potentially improve performance’ speaks for itself, though it does need to be used with caution in a corporate environment…

Want to read more about Power Query? A complete list of all our Power Query blogs can be found [here](https://www.sumproduct.com/thought/power-query-blog-series)
. Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-thanks-for-the-memory/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-thanks-for-the-memory/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-thanks-for-the-memory/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-thanks-for-the-memory/#0)

[](https://sumproduct.com/blog/power-query-thanks-for-the-memory/#0 "close")

top