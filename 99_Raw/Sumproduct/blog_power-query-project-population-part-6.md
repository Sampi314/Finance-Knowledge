# Power Query: Project Population – Part 6

**Source:** https://sumproduct.com/blog/power-query-project-population-part-6/

---

[Home](https://sumproduct.com/)

\> Power Query: Project Population – Part 6

*   May 30, 2023

Power Query: Project Population – Part 6
========================================

Power Query: Project Population – Part 6
========================================

31 May 2023

_Welcome to our Power Query blog. This week, I prepare my second query from a public data source._

I have found some information on population growth provided by The World Bank, which I am using as an example of how to transform real-life data.

![](<Base64-Image-Removed>)

I have been transforming the data, and in [Part 5](https://sumproduct.com/blog/power-query-project-population-part-5/)
, I finished tidying up the main query: **Country**:

![](<Base64-Image-Removed>)

Now that all the columns in this query have consistent data, I will look at the data that I can add from the other queries I imported. Today, I will look at the **Country-Series** query to see if there is any information that could be useful.

![](<Base64-Image-Removed>)

The first thing I notice is that the headers have not been promoted. This is because the algorithms have not detected a difference between the headings and the other data in the column since everything is of data type text. I can fix this by using the ‘Use First Row as Headers’ option on the Home tab.

![](<Base64-Image-Removed>)

However, since this will also generate a ‘Changed Type’ step, I will first delete the current ‘Changed Type’ step:

![](<Base64-Image-Removed>)

This query gives me information about the source of the population data in the **Data** query. I decide that I do not need the **SeriesCode** column, so I select the **CountryCode** and **DESCRIPTION**, and right-click to ‘Remove Other Columns’:

![](<Base64-Image-Removed>)

Ideally, I would like to have one description for each country. I start by selecting both columns and accessing the right-click menu, where I can ‘Remove Duplicates’:

![](<Base64-Image-Removed>)

However, there are still multiple descriptions for some countries. I can use a trick to combine the text. I can use ‘Group By’ which is available on the Home tab, and here, on the Transform tab:

![](<Base64-Image-Removed>)

I want to ‘Group By’ **CountryCode**, and concatenate the **DESCRIPTION** rows. However, since I have both columns selected, the dialog is in ‘Advanced’ mode, and prompting me to ‘Group By’ **CountryCode** and **DESCRIPTION**. I will sort this out later.

![](<Base64-Image-Removed>)

I want to create a new column which I call **Description**, where I will sum the **DESCRIPTION** rows:

![](<Base64-Image-Removed>)

Unsurprisingly, Power Query is not happy about summing a text value:

![](<Base64-Image-Removed>)

Next time, I will convert the **M** code into something more acceptable…

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-project-population-part-6/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-project-population-part-6/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-project-population-part-6/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-project-population-part-6/#0)

[](https://sumproduct.com/blog/power-query-project-population-part-6/#0 "close")

top