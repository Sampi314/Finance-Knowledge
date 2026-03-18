# Power Query: Arranging a List

**Source:** https://sumproduct.com/blog/power-query-arranging-a-list/

---

[Home](https://sumproduct.com/)

\> Power Query: Arranging a List

*   April 27, 2021

Power Query: Arranging a List
=============================

Power Query: Arranging a List
=============================

28 April 2021

_Welcome to our Power Query blog. This week, I look at how to translate a range of data contained in one cell to a list of cells._

Yet again, I have some data from my imaginary salespeople:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-210.jpg)

I had asked for their diary of supplier contacts, but I have instead received a list of date ranges for each salesperson and supplier. I want to have a row for each date. I start by extracting my data to Power Query using ‘From Table / Range’ on the ‘Get & Transform Data’ section of the Data tab (as usual!).

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-269.jpg)

I take the default range provided in the ‘Create Table’ dialog and indicate that my data has headers.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-214.jpg)

Ultimately, I want to have a row for each date in the range. The steps I need to take in order to achieve this are:

1.  Create columns for the start and end date
2.  Ensure that the columns have data type date
3.  Create a list of all dates between the start and end date
4.  Ensure that this list is attached to the correct sales data.

In order to create the start and end date columns, I need to split **Date Range** by delimiter, which I can do from the Home tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-202.jpg)

The delimiter I want to use is the dash (‘-‘).

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-171.jpg)

This gives me two columns which I rename **Start Date** and **End Date** for clarity.

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-150.jpg)

The next step is to set these columns to data type ‘Date’. I can do this in several places; I choose to select both columns and then right-click, where I can ‘Change Type’ to Date.

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-138.jpg)

I’m hoping this copes with all the date formats used by my salespeople.

![](<Base64-Image-Removed>)

Unfortunately, this is not the case. Only the dates using a forward slash (‘**/**‘) have been correctly converted. As I did in [Power Query: Dating Options](https://sumproduct.com/blog/power-query-dating-options/)
, I need to convert the columns to the format that is not being correctly formatted. I need to remove the delimiters.

![](<Base64-Image-Removed>)

I delete the ‘Changed Type2’ step and remove all the delimiters. Next, I have to create a custom column from the ‘Add Column’ tab where I put the delimiters into each date. Although the year length varies, I am only concerned with putting a forward slash after the second and fourth characters.

![](<Base64-Image-Removed>)

The **M** code I have used is:

**\= Text.Combine({Text.Start(\[Start Date\],2),”/”,Text.Middle(\[Start Date\],2,2),”/”,Text.Middle(\[Start Date\],4)})**

This takes the first two characters, adds a forward slash, then adds the net two characters, adds another slash, and then adds the remaining text. Finally, the elements are combined into one text string.

![](<Base64-Image-Removed>)

I repeat the process for the end date. Note that if there is a space at the beginning of **End Date**, the positions will have to be adjusted accordingly. I can then delete my original date columns and rename my new columns **Start Date** and **End Date**.

![](<Base64-Image-Removed>)

I should now be able to change the data type to ‘Date’ on my new columns.

![](<Base64-Image-Removed>)

Step 2 is complete, now I need to create a new custom column which will contain all the dates in the range. For this, I am going back to basic list creation, where I can use the ellipsis (**..**) to fill in the missing dates. For more on creating lists, see [Power Query: Birthday Lists](https://sumproduct.com/blog/power-query-birthday-lists/)
.

Having checked my dates are valid, I need to convert the columns to be whole numbers. This will allow me to create the list, as the ellipsis will not currently work with dates. It’s important to add a new ‘Change Type’ step for this, as I wouldn’t have been able to create a whole number from the text value with forward slashes in it.

![](<Base64-Image-Removed>)

I can now add a new custom column to create the list.

![](<Base64-Image-Removed>)

The **M** code I have used is:

**\= {\[Start Date\]..\[End Date\]}**

This creates a list of numbers from **Start Date** to **End Date**, which I will be able to convert back to dates.

![](<Base64-Image-Removed>)

I can see that the list contains the values; now I can move to step 4, which is to expand my column.

![](<Base64-Image-Removed>)

I choose to ‘Expand to New Rows’.

![](<Base64-Image-Removed>)

I have a row for each day. Now, I need to delete **Start Date** and **End Date** and convert **Dates List** to a date.

![](<Base64-Image-Removed>)

I can see that I have a row for each date with all the relevant data.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-arranging-a-list/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-arranging-a-list/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-arranging-a-list/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-arranging-a-list/#0)

[](https://sumproduct.com/blog/power-query-arranging-a-list/#0 "close")

top