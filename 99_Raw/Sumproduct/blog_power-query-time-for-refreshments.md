# Power Query: Time for Refreshments

**Source:** https://sumproduct.com/blog/power-query-time-for-refreshments/

---

[Home](https://sumproduct.com/)

\> Power Query: Time for Refreshments

*   February 28, 2017

Power Query: Time for Refreshments
==================================

Power Query: Time for Refreshments
==================================

1 March 2017

_Welcome to our new Power Query blog. So far I have shown that a variety of data can be extracted and loaded into queries and worksheets. Today I look at how to keep that data current by triggering automatic refreshes._

The ability to refresh data easily is a useful feature of Power Query. To begin with users are happy to carry this out manually by right clicking on an existing query.

![](<Base64-Image-Removed>)

As queries are added to and the Excel model becomes more complex, automated refreshing is an attractive option. There are several trigger points for refreshes, which require different methods to instigate them. A query can be set to refresh when a workbook is opened or at a specified time interval, from the Excel menus. These triggers can be extended to refresh Power Pivot too, since the refresh controls are held within the main Excel menus rather than as part of the Power Query (or Power Pivot) add-in.

The refresh options for queries created in Power Query are found on the ‘Data’ tab in Excel – there is a ‘Connections’ section which features a ‘Connections’ icon, clicking this brings up the ‘Workbook Connections’ screen. The screen below shows the connections for the merged query I created in back in the [Two (Queries) Become One](https://sumproduct.com/blog/power-query-two-queries-become-one/)
 blog.

![](<Base64-Image-Removed>)

If a pick a query, I can look at the ‘Properties’ box, which includes a ‘Refresh Control’ section:

![](<Base64-Image-Removed>)

There are several checkboxes:

*   Background refresh takes longer, but allows me to work whilst it’s in progress. That’s why it is the default, and should only be taken off for specific reasons as it will lock out users until complete
*   Refreshing every **n** minutes only works while the workbook is open. It can be good for data that is frequently changing at source and can be used in conjunction with the background refresh setting
*   Refreshing when opening the file does exactly what it suggests and can also be used in conjunction with the background refresh setting. This comes with an extra option to remove data from the external data range before saving the workbook; this option can be taken in order to save the workbook with the query definition but without the external data
*   Refresh this connection on ‘Refresh All’ ought to be checked as a general principle otherwise end users may believer data is up to date when it is not.

If these options are not enough, then there are some VBA options, but only use these if the queries are not going to be ported to Power BI. A single connection or all connections can be refreshed on demand using VBA. To refresh all connections some specific VBA code is required and since this is not our VBA blog, I will keep it simple by looking at refreshing a single connection.

A macro can be constructed to refresh a single connection on the ‘Developer’ tab when the workbook is open. On the ‘Developer’ tab in the Excel Ribbon, there is an option to ‘Record Macro’. I’m going to call mine ‘refresh’. I also give my macro a description which tells me what is being refreshed:

![](<Base64-Image-Removed>)

Having set up the macro, I then perform the action I want to record, by refreshing the **_ACCT\_Order\_Charges\_with\_Group_** query from the ‘Connections’ option on the ‘Data’ tab:

![](<Base64-Image-Removed>)

I can then stop recording by going back to the ‘Developer’ tab and choosing to ‘Stop Recording’:

![](<Base64-Image-Removed>)

I can see my macro from the Developer tab under Macros, and editing shows the VBA behind it:

![](<Base64-Image-Removed>)

Whilst I can run the refresh from the macros section, it would be better to have a button. S till on the ‘Developer’ tab, in the ‘Control’ section I can choose to ‘Insert’ ‘Form Controls’ – hovering over the icons tells me what they are, and in this case I choose the button icon. Once selected, my cursor turns into a ‘+’ so I can place my button. Having selected a location, I am prompted for the macro that the button will run:

![](<Base64-Image-Removed>)

I can then give it an appropriate name. As long as I remember to save my workbook in xlsm or xlsb format (I will be warned if I try to save to xlsx format), my button will be saved with my workbook, allowing me to refresh my connection without using the menus.

![](<Base64-Image-Removed>)

These options will be enough to get started with managing how connections are refreshed, but for the adventurous, more can be achieved by using third party add-ins, which can allow solutions to be ported to the web.

Next time I will take a look at the code behind Power Query…

Want to read more about Power Query? A complete list of all our Power Query blogs can be found [here](https://www.sumproduct.com/thought/power-query-blog-series)
. Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-time-for-refreshments/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-time-for-refreshments/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-time-for-refreshments/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-time-for-refreshments/#0)

[](https://sumproduct.com/blog/power-query-time-for-refreshments/#0 "close")

top