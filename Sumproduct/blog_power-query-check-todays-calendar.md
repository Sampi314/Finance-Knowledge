# Power Query: Check Today’s Calendar

**Source:** https://sumproduct.com/blog/power-query-check-todays-calendar/

---

[Home](https://sumproduct.com/)

\> Power Query: Check Today’s Calendar

*   May 28, 2019

Power Query: Check Today’s Calendar
===================================

Power Query: Check Today’s Calendar
===================================

29 May 2019

_Welcome to our Power Query blog. Today, I am going to look at an example which uses a Calendar table to filter on today’s date._

[Last week](https://sumproduct.com/blog/power-query-todays-calendar/)
, I looked at how to add a column to the Calendar table which held the relationship between the current date and the calendar date:

![](<Base64-Image-Removed>)

I am going to use this calendar in an example which selects data based on a date. I have some expense data, which I only want to upload if the file name matches today’s date.

![](<Base64-Image-Removed>)

This is similar to the issue I encountered in [Power Query: Files for Today](https://sumproduct.com/blog/power-query-files-for-today/)
, but this time I am going to use my Calendar table.

I begin in the same way as previously: I choose to extract my data ‘From Folder’:

![](<Base64-Image-Removed>)

I choose to ‘Transform Data’, so that I can select which files I want to combine.

![](<Base64-Image-Removed>)

Before I can link this data to the Calendar table, I need to extract the dates from the file names. I am only interested in the first two columns: **_Content_** and **_Name_**, so I select these two columns whilst holding down the **CTRL** key and right click to ‘Remove Other Columns’.

![](<Base64-Image-Removed>)

As shown above, using the ‘Column From Examples’ option, I create a new column with the date and time.

![](<Base64-Image-Removed>)

I rename my new column. I need to change the data type of **_File Date_** so that I can link to my Calendar table. I can do this on the ‘Transform’ tab where the current data type is set to text.

![](<Base64-Image-Removed>)

I choose the ‘Merge Queries’ option on the ‘Home’ tab. I choose to simply merge queries as I don’t need to create a new one.

![](<Base64-Image-Removed>)

I choose to merge with the ‘Calendar’ query. I need to specify how to link; I will link **_Date_** on the Calendar query to **_File Date_** on my current query. I can take the default left join as I only want those Calendar rows that match dates in my query.

![](<Base64-Image-Removed>)

The Calendar table appears as a column, and I can expand it to choose what columns I want in my query.

![](<Base64-Image-Removed>)

I am only interested in ‘Days from Today’ so I choose that option (without the prefix!).

![](<Base64-Image-Removed>)

I can see that the only files I need to upload are the ones with zero (0) in **_Days from Today_**.

![](<Base64-Image-Removed>)

This gives me the files which I want to extract and combine together.

![](<Base64-Image-Removed>)

I can delete everything apart from the **_Content_** column and expand my data.

![](<Base64-Image-Removed>)

The data looks fine so I continue.

![](<Base64-Image-Removed>)

The correct files have been extracted, and I can transform my data into the required format.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-check-todays-calendar/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-check-todays-calendar/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-check-todays-calendar/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-check-todays-calendar/#0)

[](https://sumproduct.com/blog/power-query-check-todays-calendar/#0 "close")

top