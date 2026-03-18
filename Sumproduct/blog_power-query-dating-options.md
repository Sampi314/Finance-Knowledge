# Power Query: Dating Options

**Source:** https://sumproduct.com/blog/power-query-dating-options/

---

[Home](https://sumproduct.com/)

\> Power Query: Dating Options

*   April 20, 2021

Power Query: Dating Options
===========================

Power Query: Dating Options
===========================

21 April 2021

_Welcome to our Power Query blog. This week I look at how to deal with dates in a variety of formats._

I have some dates in various formats in Excel that I am going to upload to Power Query.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-214.jpg)

I upload the data to Power Query using ‘From Table / Range’ in the ‘Get & Transform Data’ section of the Data tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-274.jpg)

I choose ‘My table has headers’ and upload my data.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-217.jpg)

The Power Query engine has tried to make sense of the dates. The **M** code applied to change the types of the columns is:

**\= Table.TransformColumnTypes(Source,{{“UK(Day/Month/Year)”, type date}, {“US(Month/Day/Year)”, type text}, {“Year/Month/Day”, type date}, {“DayMonthYear”, Int64.Type}, {“Day?Month?Year”, type text}})**

This means that it has recognised **UK(Day/Month/Year)** and **Year/Month/Day** as dates, but has left **US(Month/Day/Year)** and **Day?Month?Year** as type text. This makes sense because I am based in the UK and that is my locale. Interestingly, **DayMonthYear** has been treated as a whole number (Int64.Type).

I would like all the date columns to be transformed as dates, so I will look at each column in turn.

I will start by seeing what happens if I set the data type of date for **US(Month/Day/Year).**

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-205.jpg)

I can do this on the Transform tab where there is a dropdown for ‘Data Type’

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-173.jpg)

Since all that has happened so far is that Power Query has determined data types, I am invited to add this change to the existing step, which I do.

![](<Base64-Image-Removed>)

This is not what I want and could be confusing if I didn’t have days larger than 12. I need to help Power Query understand the format of this date. Since the date format is associated with a different locale, I can change the locale for this column.

![](<Base64-Image-Removed>)

If I click on the date icon next to the column name, I can access a dropdown list. Right at the bottom is an option to specify ‘Using Locale’. I choose this option.

![](<Base64-Image-Removed>)

I choose Data Type Date and Locale ‘English (United States)’.

![](<Base64-Image-Removed>)

The data type and the display are now correct, and there are no errors. Next, I repeat the process for **DayMonthYear,** which is currently a whole number.

![](<Base64-Image-Removed>)

Changing to type Date gives me errors. Since this is not in a recognised locale format, I need to reformat it using some **M** code. I create a custom column from the ‘Add Column’ tab.

![](<Base64-Image-Removed>)

The **M** code I have used is:

**\= Text.Start(Text.From(\[DayMonthYear\]),2) & “/”**

    **& Text.Middle(Text.From(\[DayMonthYear\]),2,2)**

    **& “/” & Text.End(Text.From(\[DayMonthYear\]),4)**

This means I am converting the column to text and then taking the first two characters (the day), adding a “/”, then taking the next two characters (the month) and adding another “/”, and finally adding the last four characters (the year).

![](<Base64-Image-Removed>)

I can now convert this to a date.

![](<Base64-Image-Removed>)

My final column is **Day?Month?Year**, which is a mixture of properly formatted dates and dates missing the separator. The rule of thumb here is that I have to cater for the most difficult case, so I need to remove the separators. I can do this by right clicking and using ‘Replace Values’.

![](<Base64-Image-Removed>)

This will leave me with all the data in the same format and I can use the same **M** code as before. If I had a lot of dates in this format, I would create a function to do this.

![](<Base64-Image-Removed>)

The **M** code this time is:

**\= Text.Start(Text.From(\[#”Day?Month?Year”\]),2) & “/”**

    **& Text.Middle(Text.From(\[#”Day?Month?Year”\]),2,2)**

    **& “/” & Text.End(Text.From(\[#”Day?Month?Year”\]),4)**

Note that this time I have to use **“#”** and put the column name in quote marks (**“”**) so that the question mark (**“?”**) is not treated like a special character.

I change the new column to a date and rename the custom columns. My dates are now all formatted correctly.

![](<Base64-Image-Removed>)

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-dating-options/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-dating-options/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-dating-options/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-dating-options/#0)

[](https://sumproduct.com/blog/power-query-dating-options/#0 "close")

top