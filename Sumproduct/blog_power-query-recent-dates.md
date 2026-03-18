# Power Query: Recent Dates

**Source:** https://sumproduct.com/blog/power-query-recent-dates/

---

[Home](https://sumproduct.com/)

\> Power Query: Recent Dates

*   November 17, 2020

Power Query: Recent Dates
=========================

Power Query: Recent Dates
=========================

18 November 2020

_Welcome to our Power Query blog. This week, I show how to only extract the dataset for the last two years, say._

I have some accounting data:

![](<Base64-Image-Removed>)

I only want to work with the data for the last two (2) years. I begin by extracting my data to Power Query using the ‘From Table’ option on the ‘Get & Transform’ section of the Data tab.

![](<Base64-Image-Removed>)

Once I have my data, I change the datatype of my **Date** column to ‘Date’. I can do this from several places; here, I have used the ‘Data Type’ dropdown on the Transform tab:

![](<Base64-Image-Removed>)

Since this change type step comes directly after the automatically generated change type step, I am invited to make the amendment to the existing step, which I accept.

![](<Base64-Image-Removed>)

I can then filter my column by using the down arrow next to the column title.

![](<Base64-Image-Removed>)

I have a dropdown from the ‘Date Filter’ option with a selection of different ways to filter my data. I choose ‘Custom Filter’:

![](<Base64-Image-Removed>)

I want to choose the ‘Advanced’ options, so I select that box.

![](<Base64-Image-Removed>)

I change ‘Operator’ from ‘equals’ to ‘is in year’ and then look at my ‘Value’ dropdown.

![](<Base64-Image-Removed>)

I select ‘Last Year’ and then move onto the next line. I want to pick data from two years, so I change ‘And’ to ‘Or’.

![](<Base64-Image-Removed>)

I have a choice here: I can either pick ‘This Year’ or ‘Year to Date’. This will depend upon my needs, but for accounting purposes, I will usually pick ‘Year to Date’.

![](<Base64-Image-Removed>)

I can now apply this to my data. I started off with 999+ rows.

![](<Base64-Image-Removed>)

I now have 680 rows, and I can see that the earliest row is from last year. Since I haven’t specified any dates in my filter, this is a dynamic way to see the last two years.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-recent-dates/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-recent-dates/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-recent-dates/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-recent-dates/#0)

[](https://sumproduct.com/blog/power-query-recent-dates/#0 "close")

top