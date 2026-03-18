# Power Query: New Year, New Approach

**Source:** https://sumproduct.com/blog/power-query-new-year-new-approach/

---

[Home](https://sumproduct.com/)

\> Power Query: New Year, New Approach

*   December 31, 2024

Power Query: New Year, New Approach
===================================

Power Query: New Year, New Approach
===================================

1 January 2025

_Welcome to our Power Query blog. This week, I extend the break from all things fuzzy to see how Copilot would solve last week’s challenge._

[Last week](https://sumproduct.com/blog/power-query-merry-christmas/)
, I was Santa’s not-so-little helper when I transformed this:

![](<Base64-Image-Removed>)

into this:

![](<Base64-Image-Removed>)

The **M** code I used was:

**\=  
List.Union({Source\[Dasher\], Source\[Prancer\], Source\[Dancer\], Source\[Vixen\],  
Source\[Donner\], Source\[Blitzen\], Source\[Cupid\], Source\[Comet\],Source\[Rudolf\]})**

However, since there are other methods I could have used to achieve my goal, I am curious to see what approach Copilot would suggest. If you would like to know more about Copilot in Excel, please see our [news article](https://www.sumproduct.com/news/article/copilot-in-excel-now-generally-available)
 here. I need to be specific about using Power Query and I need to describe the challenge succinctly. Let’s see how it goes!

To access Copilot, I need to activate AutoSave, and select the Copilot pane from the Home tab:

![](<Base64-Image-Removed>)

The prompt I will use is:

_“Using Power Query, create a single column containing all the data.”_

![](<Base64-Image-Removed>)

I have my answer, and here are the steps:

1.  Select any cell within your data range
2.  Go to the Data tab on the ribbon and click on ‘From Table/Range’ to load the data into Power Query
3.  In the Power Query Editor, select all the columns you want to combine
4.  Right-click on the selected columns and choose ‘Unpivot Columns’
5.  This will create two columns: **Attribute** and **Value**. The **Value** column contains all the data from the original columns
6.  You can remove the **Attribute** column if you only need the single column of data
7.  Click ‘Close & Load’ to load the transformed data back into Excel.

Let’s see how this works. I already have my **SC\_List** query from [last week](https://sumproduct.com/blog/power-query-merry-christmas/)
, which means I may skip the first two \[2\] steps.

![](<Base64-Image-Removed>)

I select all the steps I want to combine by clicking in any header and using **CTRL** + **A** to select all the columns. Next, I right-click an choose to ‘Unpivot Columns’:

![](<Base64-Image-Removed>)

This will give me the **Attribute** and **Value** columns:

![](<Base64-Image-Removed>)

Whilst this would give me the reindeer who created the list item, it does mean that I have the duplicate entries. I tried adding “with no duplicates” to the to the Copilot prompt, and the only difference in the method is that Copilot added an extra step to remove the duplicates.

I delete the **Attribute** column and right-click to ‘Remove Duplicates’:

![](<Base64-Image-Removed>)

This gives me the data in one column, albeit in more steps than my method:

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

It is interesting to see the method suggested by the algorithms. Copilot may be used as a starting point or, as I have done in this case, to consider alternative approaches. It may help more users to discover the benefits of Power Query but (as with all AI) the results should be checked carefully!

I couldn’t resist entering a more complex prompt, which demonstrates how Power Query knowledge is so important when using AI to help create queries:

_“Using Power Query and List.Union, create a list containing all the data with no duplicates.”_

![](<Base64-Image-Removed>)

This time, I have **M** code, which I copy.

**let**

    **Source =  
Excel.CurrentWorkbook(){\[Name=”SC\_List”\]}\[Content\],**

    **ColumnsToList =  
List.Union(List.Transform(Table.ToColumns(Source), each List.Distinct(\_))),**

    **RemoveDuplicates =  
List.Distinct(ColumnsToList),**

    **Result = Table.FromList(RemoveDuplicates,  
Splitter.SplitByNothing(), {“UniqueValues”})**

**in**

    **Result**

In the Power Query Editor, I create a new blank query by right-clicking in the Queries pane, and choosing the option from the ‘Other Sources’ tab. I access the ‘Advanced Editor’ from the Home tab, and paste the **M** code:

![](<Base64-Image-Removed>)

Let’s see what I get:

![](<Base64-Image-Removed>)

Don’t be fooled by the complexity of the code. Whilst the ColumnsToList step is an elegant way of getting the data into a list without using any column names:

![](<Base64-Image-Removed>)

where the **M** code is:

**\= List.Union(List.Transform(Table.ToColumns(Source), each  
List.Distinct(\_)))**

The subsequent steps are actually superfluous: we have our result, and there are no duplicates since **List.Union()** has been used! We don’t need to convert the list to a table either. This is another example of how Power Query knowledge is needed to assess the results.

I’ll let Copilot have the last word:

![](<Base64-Image-Removed>)

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-new-year-new-approach/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-new-year-new-approach/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-new-year-new-approach/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-new-year-new-approach/#0)

[](https://sumproduct.com/blog/power-query-new-year-new-approach/#0 "close")

top