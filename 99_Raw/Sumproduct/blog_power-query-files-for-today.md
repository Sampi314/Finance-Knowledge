# Power Query: Files for Today

**Source:** https://sumproduct.com/blog/power-query-files-for-today/

---

[Home](https://sumproduct.com/)

\> Power Query: Files for Today

*   April 16, 2019

Power Query: Files for Today
============================

Power Query: Files for Today
============================

17 April 2019

_Welcome to our Power Query blog. Today, I am going to select files using the date embedded in the file name._

I have a group of files created by my almost-legendary imaginary salespeople. I only need to upload those files that match today’s date.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-450.jpg)

I am going to import from a folder, which I first visited way back in [Power Query: One Folder, One Query](https://sumproduct.com/blog/power-query-one-folder-one-query/)
. In Excel, I first select the ‘Get & Transform’ section of the ‘Data’ tab. Here, I can choose to create a new query, and I select the ‘From Folder’ option on the dropdown from the ‘From File’ option:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-464.jpg)

I am prompted to enter or browse for my folder.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-435.jpg)

Having selected my folder, I click ‘OK’.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-403.jpg)

I can see a number of files in this folder, some of which apply to today (guess when I wrote this – 26/03/2019). There are a number of ways to get just those files that correspond to today’s date, and I will explore one of them. To start, I choose to transform my data using the ‘Transform Data’ tab (formerly known as ‘Edit’).

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-343.jpg)

I am only interested in the first two columns: **_Content_** and **_Name_**, so I select these two columns whilst holding down the **CTRL** key and right-click to ‘Remove Other Columns’.

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-299.jpg)

There are a number of ways I could use to extract the date; I am going to use the ‘Column From Examples’ functionality on the ‘Add Column’ tab:

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-253.jpg)

After the first example, Power Query has filled in the transformation:

**\= Text.BetweenDelimiters(\[Name\], “\_”, “\_”, 1, 0)**

(for more on using **Text.BetweenDelimiters** please refer to [Power Query: Sub Texting](https://sumproduct.com/blog/power-query-sub-texting/)
.)

![](<Base64-Image-Removed>)

My next step will be to transform this into a date. To do this, first I will need to get it into a format that Power Query will recognise. This time, I add a column using ‘Custom Column’ and provide the **M** code.

![](<Base64-Image-Removed>)

The **M** I have used is:

**\= #date(Number.FromText(Text.Range(\[Text Between Delimiters\],4,4)),Number.FromText( Text.Range(\[Text Between Delimiters\],2,2)),Number.FromText(Text.Range(\[Text Between Delimiters\],0,2)))**

This essentially gets the portions of text that represent year, month and day using **Text.Range**, converts each portion to a number using **Number.FromText**, and then uses **#date** to convert the year, month and day to date format.

![](<Base64-Image-Removed>)

Now I need to create the filter. I am going to use an existing filter option to get the format of the **M** code, and make a tweak.

![](<Base64-Image-Removed>)

I have the option ‘In the Previous’, but not ‘In the Current’, so I will start off with ‘In the Previous’.

![](<Base64-Image-Removed>)

I choose dates ‘in the previous 1 day’.

![](<Base64-Image-Removed>)

This gives me yesterday’s file, but I can change the **M** code. The code I have now is:

**\= Table.SelectRows(#”Added Custom”, each Date.IsInPreviousNDays(\[Date\], 1))**

I am going to change this to use **Date.IsInCurrentDay** (which I think should be a standard filter option for dates!):

**\= Table.SelectRows(#”Added Custom”, each Date.IsInCurrentDay(\[Date\]))**

(For more on **Date.IsIn()** functionality, please refer to [Power Query: Currently Dating](https://www.sumproduct.com/blog/article/power-query-blogs/power-query-currently-dating)
.

![](<Base64-Image-Removed>)

This gives me the files that have today’s date on them, and I can then expand the available data should I wish. I rename my current **_Date_** column to **_File Date_** to avoid confusion.

![](<Base64-Image-Removed>)

When I use the icon next to the **_Content title_**, I am prompted to specify how to combine the files. I will use the defaults.

![](<Base64-Image-Removed>)

The data from the files that had today’s date in the title have been combined, and I can transform them as I wish.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-files-for-today/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-files-for-today/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-files-for-today/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-files-for-today/#0)

[](https://sumproduct.com/blog/power-query-files-for-today/#0 "close")

top