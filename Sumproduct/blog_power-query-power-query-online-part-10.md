# Power Query: Power Query Online – Part 10

**Source:** https://sumproduct.com/blog/power-query-power-query-online-part-10/

---

[Home](https://sumproduct.com/)

\> Power Query: Power Query Online – Part 10

*   October 10, 2023

Power Query: Power Query Online – Part 10
=========================================

Power Query: Power Query Online – Part 10
=========================================

11 October 2023

_Welcome to our Power Query blog. Today, I look at the query folding features in the diagram view in Power Query Online._

In the current series, I am looking at Power Query Online, which I have accessed from Power Apps:

![](<Base64-Image-Removed>)

[Last week](https://sumproduct.com/blog/power-query-power-query-online-part-9/)
, I looked at the effect of marking a column used in a merge as a key.

I marked the column **2-alpha code** as a key in both tables I planned to merge:

![](<Base64-Image-Removed>)

Then, I went back to the data view, and refreshed the query **Merge** again:

![](<Base64-Image-Removed>)

I found that the time had improved:

![](<Base64-Image-Removed>)

This week, I am going to look at a different dataflow. I have some data that I have imported from an Azure SQL database:

![](<Base64-Image-Removed>)

For this table, although I only have one ‘Marked Key’ step, I have two separate keys indicated:

![](<Base64-Image-Removed>)

**AddressID** was already marked as a key in the database, and in Power Query Online, I am now able to see this information easily. The icon is the same as the icon on **City**, which I have marked as a key myself.

Note also the query folding indicators in the ‘Applied steps’ section:

![](<Base64-Image-Removed>)

The query folding starts at step ‘Source’ and ends at step ‘Inserted Text Between Delimiters’. If these icons do not appear, the setting can be adjusted from ‘Options’ on the Home tab:

![](<Base64-Image-Removed>)

The setting ‘Enable query folding indicators’ can be enabled from this dialog.

If I select the diagram view, I can see more information about what the query folding indicators mean. I select the ‘Navigation 1’ step and right-click.

![](<Base64-Image-Removed>)

On the right-click menu, I have the option to ‘View data source query’:

![](<Base64-Image-Removed>)

This is showing me the SQL code which is used to extract the data from the database for this step. This makes query folding easier to understand: folding a query means that the steps so far can be expressed as an SQL statement. If I move onto the ‘Choose columns’ step, and ‘View data source query again’, I get the SQL statement up to and including that step:

![](<Base64-Image-Removed>)

This time the SQL statement is shorter, because I have reduced the number of columns that I am extracting from the table. If I try to view the data source query by right clicking on the step ‘Inserted Text Between Delimiter’:

![](<Base64-Image-Removed>)

The option is greyed out because this step cannot be incorporated into the SQL statement, as shown by the query folding indicator next to the step:

![](<Base64-Image-Removed>)

The **M** code in this step could be expressed in SQL, but not in the same statement as the previous steps, therefore the query folding has been terminated at this point:

**Table.AddColumn(#”Choose  
columns”,** **“Street”****,****each****Text.BetweenDelimiters(\[AddressLine1\],** **” “****,** **” “****),** **type****text****)**

These new features help to demystify query folding, especially for new users of Power Query.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-power-query-online-part-10/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-power-query-online-part-10/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-power-query-online-part-10/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-power-query-online-part-10/#0)

[](https://sumproduct.com/blog/power-query-power-query-online-part-10/#0 "close")

top