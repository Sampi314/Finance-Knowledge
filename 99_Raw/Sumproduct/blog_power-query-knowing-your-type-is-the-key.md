# Power Query: Knowing Your Type is the Key

**Source:** https://sumproduct.com/blog/power-query-knowing-your-type-is-the-key/

---

[Home](https://sumproduct.com/)

\> Power Query: Knowing Your Type is the Key

*   June 27, 2017

Power Query: Knowing Your Type is the Key
=========================================

Power Query: Knowing Your Type is the Key
=========================================

28 June 2017

_Welcome to our Power Query blog. Today I look at extracting data by using differences in data types._

When transforming data with Power Query, the most important skill is knowing where to start, and this week I look at one such scenario.

I have received a CSV file containing expense information for a number of employees. The creator of the file has included heading information, but it is embedded in the expense data. Starting from a fresh Excel workbook, I load my data using the same method I employed in [Getting Started](https://sumproduct.com/blog/power-query-getting-started/)
. To do this, I go to the Power Query tab, and choose ‘From File’. I select the ‘From Text/CSV’ option:

![](<Base64-Image-Removed>)

Having selected my file, I choose to edit prior to loading so that I access the Power Query Editor.

![](<Base64-Image-Removed>)

Note that because my top row contained text for each column, Power Query has correctly assumed that this is the title row and ‘Promoted Headers’ accordingly which saves me renaming my columns and deleting that row. However, now I can see the problem. Since the creator of the file has included the employee and department information between the expense rows, my **_Date_** column has some names in it, and my **_expense code_** column has some departments. I need to extract my name and department data from the other rows.

In these situations, I have to look for a way of distinguishing the data that I need to extract. My **_expense code_** column doesn’t help much, as departments and expense codes look fairly similar. In my **_Date_** column however, the names are a different format to the dates, and this is a reliable indicator, as I am not likely to have someone with a name that resembles a date!

I have two problems – I want to get rid of the rows that have an ‘irregular’ date, but I also need to extract my name data. The first step I will take, is to make a copy of my **_Date_** column. To do this, I right-click my **_Date_** column and choose ‘Duplicate Column’:

![](<Base64-Image-Removed>)

I complete this process and create a **_Date – Copy_** column which I can manipulate without losing data from the original column. I right-click my copied column and choose to change the type to ‘Date’, which means that my names are flagged as errors:

![](<Base64-Image-Removed>)

I can now reset the data in the ‘Error’ entries to null – I right click my copied column again and choose to ‘Replace Errors’ with null.

![](<Base64-Image-Removed>)

The reason that null is more useful to me than an error, is because I can use null in the conditional logic that I need to extract my name data.

I create a new column by choosing ‘Conditional Column’ from the ‘General’ section on the ‘Add Column’ tab. I want to create a column that is populated with the employee name.

![](<Base64-Image-Removed>)

Power Query builds the logic statement, so I just need to supply the location of the data.

**If _Date\_Copy_ equals null, Then _Date_, Otherwise null**

Note that the default for the **Value** and the **Output** is a value, and since my chosen output is a column, I need to select that from the icon under **Output**, otherwise I will be inserting the value ‘Date’ instead of the value in **_Date._** Choosing to output null when the condition is not met will help with the next step.

With this borne in mind, I click ‘OK’ to see my new column:

![](<Base64-Image-Removed>)

Since the value in my new column is either a name or null, I can populate the rest of the data. I right-click my new column and choose ‘Fill’ and then ‘Down’.

![](<Base64-Image-Removed>)

I have my names; I can now create another Conditional Column to get my department information – this time my output is the **_expense code_** column.

![](<Base64-Image-Removed>)

Since the value in my new column is either a department name or null, I can populate the rest of the data. I right-click my new column and choose ‘Fill’ and then ‘Down’ as before:

![](<Base64-Image-Removed>)

Now all I need is to get rid of my redundant columns and rows. There are a number of ways I could approach this, but since I still have nulls in **_Date – Copy_**, I use this column. Then, I use the filter icon next to the **_Date – Copy_** column to remove null values.

![](<Base64-Image-Removed>)

This gives me the rows I want.

![](<Base64-Image-Removed>)

I delete **_Date – Copy_** and set the data types on the columns I want to keep. I am now ready to ‘Close and Load’ my data to an Excel worksheet.

![](<Base64-Image-Removed>)

By spotting the differences in data types in my original **_Date_** column, I have been able to pull out the data I need and format it in a useful way.

Want to read more about Power Query? A complete list of all our Power Query blogs can be found [here](https://www.sumproduct.com/thought/power-query-blog-series)
. Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-knowing-your-type-is-the-key/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-knowing-your-type-is-the-key/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-knowing-your-type-is-the-key/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-knowing-your-type-is-the-key/#0)

[](https://sumproduct.com/blog/power-query-knowing-your-type-is-the-key/#0 "close")

top