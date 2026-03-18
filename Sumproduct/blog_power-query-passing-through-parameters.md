# Power Query: Passing Through Parameters

**Source:** https://sumproduct.com/blog/power-query-passing-through-parameters/

---

[Home](https://sumproduct.com/)

\> Power Query: Passing Through Parameters

*   August 8, 2017

Power Query: Passing Through Parameters
=======================================

Power Query: Passing Through Parameters
=======================================

9 August 2017

_Welcome to our Power Query blog. Today I look at filtering for parameters._

Last week, in [In Terms of Conditional Columns](https://sumproduct.com/blog/power-query-in-terms-of-conditional-columns/)
, I looked at how parameters were a possible source when defining conditional columns. This week, I take a closer look at parameter creation by using a parameter in a filter.

Parameters allow me to enter limits into a calculation or query. If I choose to only show data where the value in my date column matches a parameter, then only data corresponding to the parameter value will be shown. I can then change the parameter to alter the filter.

I am going to show how to create a parameter using the menu options in the Power Query editor. I begin by entering a new parameter and investigating my options. I can do this from the query editor by choosing the ‘Home’ tab and picking ‘New Parameter’ from the ‘Manage Parameters’ dropdown in the ‘Parameters’ section.

![](<Base64-Image-Removed>)

Sticking with my date theme, I choose to create a parameter that I can use as a date filter. I specify ‘Date/Time’ to match the data in my **_Date_** column. The other data types available are shown in the dropdown in the screen below:

![](<Base64-Image-Removed>)

The ‘Required’ box determines if this parameter must always be populated: if it is ticked then the ‘Current Value’ must be specified. The next box, ‘Suggested Values’, defines what can be entered into my parameter. The first option, ‘Any value’, is obvious enough; the other options need a little more explanation.

![](<Base64-Image-Removed>)

If I choose to only allow a parameter selected from a list (‘List of values’), I can limit the options that can be entered into my parameter by creating a list as shown below:

![](<Base64-Image-Removed>)

This could help to prevent me from entering a value that wouldn’t link to any rows. I can also use a query to determine my subset of dates, but it must have been created prior to me creating my parameter.

In order to have something available in this ‘Query’ option, I need to enter a list query, _i.e._ a query that will return a list of values, in this case dates. I could create a list using **M** code, but since I want to create a list of the dates that have data from my query associated with them, I will create the list from my Excel data here.

I create a new query from the Excel data and delete everything except the date column. On the ‘Transform’ tab, there is an option in the ‘Any Column’ section to convert a column to a list, called ‘Convert to List’, as shown below:

![](<Base64-Image-Removed>)

When I click on ‘Convert to List’, the view changes and the icon for my query changes to a list _viz._

![](<Base64-Image-Removed>)

My list is not yet finished: I have dates appearing multiple times in random order. I can tidy up my list by applying a sort and removing duplicates as shown below:

![](<Base64-Image-Removed>)

My list query is now available for me to select when creating or editing my parameter.

![](<Base64-Image-Removed>)

Therefore, I can either create a parameter that accepts any value or have a parameter that will only allow values on a list, whether that is a manually created list in my ‘Parameters’ screen or via a list query. To see how the parameter can be used in a filter, I begin with the first ‘Suggested Values’ option, the ‘Any value’ option:

![](<Base64-Image-Removed>)

In order to use my parameter to filter my data, I need to go to the filter icon next to my **_Date_** column, where I find a ‘Date/Time Filters’ dropdown and pick the ‘Custom Filter’ option at the bottom.

![](<Base64-Image-Removed>)

This allows me to filter based on my new parameter by clicking on the datatype icon between the values.

![](<Base64-Image-Removed>)

I think it is useful that I can also enter new parameters from here. However, this is not an option to enter the _first_ parameter in the workbook, as the datatype icon is not available if there are no parameters. I choose my parameter and click OK.

![](<Base64-Image-Removed>)

My current value has immediately been applied to the filter. In order to change my parameter, I can see it in the left-hand pane along with the current value. Another nice feature is that if I hover over my parameter, the description I entered appears so I can be sure I have the right one. I click on my date parameter. Since I have chosen to allow any value, I change it to another date:

![](<Base64-Image-Removed>)

If I return to my **_Parameters_** query, my parameter change has been picked up by the filter and it remains in the same step ‘Filtered Rows’, since the step refers to my parameter:

\= Table.SelectRows(#”Changed Type”, each \[Date\] = #”Date Parameter”)

![](<Base64-Image-Removed>)

However, as I mentioned earlier, since I have allowed any value, I can pick dates which will return no data. To prevent this happening, I can use a list.

I return to my parameter screen by choosing the option ‘Manage Parameter’, and choose one of the list options, ‘List of values’. I can enter a series of dates to create my list. Power Query will only allow me to add valid dates (Date/Time datatype) to this list:

![](<Base64-Image-Removed>)

I check how the parameter entry works now.

![](<Base64-Image-Removed>)

This time I can only pick from the dropdown, which means that I will always select at least one row when I change the parameter used in the filter.

Want to read more about Power Query? A complete list of all our Power Query blogs can be found here. Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-passing-through-parameters/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-passing-through-parameters/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-passing-through-parameters/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-passing-through-parameters/#0)

[](https://sumproduct.com/blog/power-query-passing-through-parameters/#0 "close")

top