# Power Query: In the Zone

**Source:** https://sumproduct.com/blog/power-query-in-the-zone/

---

[Home](https://sumproduct.com/)

\> Power Query: In the Zone

*   February 5, 2019

Power Query: In the Zone
========================

Power Query: In the Zone
========================

6 February 2019

_Welcome to our Power Query blog. This week, I look at some issues when dealing with extracted dates._

John, my reliable imaginary salesperson has provided some expense information. However, John was a bit confused by his recent trip to the US East Coast. John has decided that putting the dates in US format will be enough to sort out the time differences. The times he has entered are UK times.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-490.jpg)

Using ‘From Table’ on the ‘Get & Transform’ section on the ‘Data’ tab, I upload the data:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-508.jpg)

Since my locale is in the UK, the time has been converted to UK format (dd/mm/yyyy). I want to show the date in US format (mm/dd/yyyy).

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-479.jpg)

The option to ‘Add Column from Examples’ is on the ‘Add Columns’ tab. I want to see how Power Query will convert my format:

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-442.jpg)

Power Query is reorganising my date data into the correct format using **M**‘s **Text** functionality.

**\= Text.Combine({Text.Middle(Text.From(\[Date\], “en-GB”), 3, 3), Text.Start(Text.From(\[Date\], “en-GB”), 3), Text.Middle(Text.From(\[Date\], “en-GB”), 8)})**

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-368.jpg)

However, my new date column is a text column, and it should be a date column. I convert the column datatype by right-clicking on the column.

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-318.jpg)

This looks better, but I have another problem. The times are correct for the **_UK Date and Time_**, but not the **_US Date and Time_**. I need to correct the time on the US column. I could do this by simply subtracting five hours since I know that the US column is set to EST. However, I want to use the **M** function **DateTime.AddZone()**:

DateTime.AddZone(**datetime** as nullable datetime, **timezonehours** as number, optional **timezoneminutes** as nullable number) as nullable datetimezone

This adds the **timezonehours** (and minutes if specified) as an offset to the input **datetime** value and returns a new datetimezone value.

I create a new column for the US date and time using ‘Custom Column’ option on the ‘Add Column’ tab.

![](<Base64-Image-Removed>)

I enter the **M** code:

**\= DateTime.AddZone(\[Date\], 5)**

![](<Base64-Image-Removed>)

But the time is the same! I need one more step – I right-click on **_Correct US Date and Time_**, and convert it to a Date/Time column.

![](<Base64-Image-Removed>)

The column has now been converted to show the US time (which is five hours behind GMT).

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-in-the-zone/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-in-the-zone/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-in-the-zone/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-in-the-zone/#0)

[](https://sumproduct.com/blog/power-query-in-the-zone/#0 "close")

top