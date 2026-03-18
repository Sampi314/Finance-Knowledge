# Power Query: Querying Query Options

**Source:** https://sumproduct.com/blog/power-query-querying-query-options/

---

[Home](https://sumproduct.com/)

\> Power Query: Querying Query Options

*   January 9, 2018

Power Query: Querying Query Options
===================================

Power Query: Querying Query Options
===================================

10 January 2018

_Welcome to our Power Query blog. This week, I look at the ‘Query Options’ screen and what it can do for me._

The ‘Query Options’ screen is on the ‘Data’ tab and may be found at the bottom of the dropdown when selecting ‘New Query’.

![](https://sumproduct.com/wp-content/uploads/2025/05/3c198d1b01396cce9976b64fbc8275df.jpg)

The screen gives me control over how my queries are created, either globally or in my current workbook, depending which tab I choose. Taking it from the top, ‘Use standard load settings’ sets the default action for where to load queries to:

*   For single queries, the default is to load to a new worksheet
*   For multiple queries, the default is to load to the data model.

I can choose to specify the defaults instead, but in any case, I can override this when I am actually loading a query.

‘Fast Data Load’ can also be set for individual queries in the ‘Query Properties’ screen (for more on this, please refer to Power Query: Managing Many Queries. Microsoft describes the fast data load setting below, which means it depends how quickly I need the information from my query and whether I am happy to let Excel hang in the meantime!

The default behaviour is “Background Data Load”, but now users can instead choose the “Fast Data Load” mode in the Options dialog.  When loading a query using the “Fast Data Load” mode, your query will take less time to load, however, Excel may be unresponsive for long periods of time during the upload.

The ‘Data Cache Management Options’ basically show me the current size and limit of the cache and allows me to clear the cache and change the limit. Caches generally speed up retrieval and this is no exception: copies of query preview results may be held here for faster access. Whilst the maximum size can be controlled, it’s not recommended to go below 32 MB.

![](<Base64-Image-Removed>)

The ‘Query Options’ screen is mostly to do with how the Query Editor appears. The ‘Parameters’ section is interesting, and deserves more explanation. If I enable ‘Always allow parameterization…’, then I can use the functionality associated with parameters from my query without first creating a parameter. As a more experienced user, I switch this on, but someone who was going to stick to simple queries probably wouldn’t. For more on parameters, please see [Power Query: Passing Through Parameters](https://sumproduct.com/blog/power-query-passing-through-parameters/)
.

![](<Base64-Image-Removed>)

The next tabs are to do with protecting data. Requiring approval for new database queries is a sensible precaution, and warning users if they select a website that has not been approved as trusted or entered explicitly makes sense. I keep these default settings. I haven’t approved any ADFS authentication services, but if I did, they would appear here. Privacy levels are concerned with protecting my data sources, and require a complete explanation – for this reason I will not try to simplify it. Microsoft explain the levels and how to combine them [here](https://support.office.com/en-us/article/Privacy-levels-Power-Query-cc3ede4d-359e-4b28-bc72-9bee7900b540?CorrelationId=a4930b80-fee2-4c13-b370-1426e6c81363&ui=en-US&rs=en-US&ad=US&ocmsassetID=HA104009800)
 so that I don’t have to! I can choose to specify privacy settings globally and for my current workbook. I am not going to show the account tab, as that is part of my privacy settings…

![](<Base64-Image-Removed>)

Diagnostics can be used if serious problems are encountered in Excel. I have created a simple query just to show what is created in the trace file. Any open Excel session will write to trace files until the session that has enabled tracing is closed or tracing is disabled. The screen helpfully tells me where the trace files are kept by letting me access the folder. One of my trace files is shown below:

![](<Base64-Image-Removed>)

It is essentially a list of steps, but it’s used mainly to locate an error if there is a problem.

![](<Base64-Image-Removed>)

Finally, I can set the locale for my current workbook on the ‘Regional Settings’ tab. This influences how dates and times are interpreted as data is extracted and can be useful if I am dealing with data that has come in from the US. This only affects the query, not my Excel workbook.

![](<Base64-Image-Removed>)

In the screen above, I have imported from my US file with my locale set to English (United States), and Power Query recognises that I have dates, as shown by the assumed data type. I can now load my data.

![](<Base64-Image-Removed>)

As I have my location set as English (United Kingdom) in Excel, the date is now shown in the correct format for me.

![](<Base64-Image-Removed>)

On the screen above I have set my locale back to English (United Kingdom) and extracted my data again. This time, the date fields appear as data type text because Power Query has not recognised them as dates.

![](<Base64-Image-Removed>)

When I load to my spreadsheet, the dates are not shown correctly. So locale can be useful when I am using sources from other regions.

Want to read more about Power Query? A complete list of all our Power Query blogs can be found [here](https://www.sumproduct.com/thought/power-query-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-querying-query-options/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-querying-query-options/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-querying-query-options/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-querying-query-options/#0)

[](https://sumproduct.com/blog/power-query-querying-query-options/#0 "close")

top