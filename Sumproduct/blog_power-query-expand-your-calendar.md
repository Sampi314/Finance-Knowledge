# Power Query: Expand Your Calendar

**Source:** https://sumproduct.com/blog/power-query-expand-your-calendar/

---

[Home](https://sumproduct.com/)

\> Power Query: Expand Your Calendar

*   October 27, 2020

Power Query: Expand Your Calendar
=================================

Power Query: Expand Your Calendar
=================================

28 October 2020

_Welcome to our Power Query blog. This week, I finish my calendar creation._

It’s been a while since I looked at how to create a calendar, and Power Query has moved on since then. It’s time to bring my calendar creation up to date. This is the sequel (not SQL), and below is the state of my calendar so far:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-118-1.jpg)

The **M** code is currently:

**\= List.Dates(StartDate, Calendar\_Length, #duration(1, 0, 0, 0))**

From [last time](https://sumproduct.com/blog/power-query-update-your-calendar/)
, I promised to point out the deliberate mistake in the Calendar\_Length step. Currently, it will only reach yesterday – if I want today then I need to add one (1):

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-108-1.jpg)

The first thing I need now is to see my calendar when I open the query. I can do this by adding a step which points back to the ‘Changed Type’ step.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-99-1.jpg)

Now I can add more columns.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-89-1.jpg)

I can start with the year, which is easy to add from the ‘Add Column’ tab, where I have a number of options under Date, _viz._

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-78-1.jpg)

I can go on to add a few more date columns.

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-66-1.jpg)

There are of course many columns which I can add, depending upon my requirements. One column which can be useful is the financial year, but this is not available from the ‘Add Column’ menu. This varies by country, but in the UK, the financial year starts in April. For simplicity here, I will assume the financial year starts on April 1 (more fool me).

I can add a custom column to do this:

![](<Base64-Image-Removed>)

I have done this by amending the ‘Inserted Year’ step. Instead of

**\= Table.AddColumn(Custom1, “Year”, each Date.Year(\[Date\]), Int64.Type)**

I have used:

**\= Table.AddColumn(****_#”Inserted Month Name”, “Financial Year”, each Date.Year(\[Date\] + #duration(275,0,0,0)_ _)_****, Int64.Type)**

So, I am treating April 1st as if it is January 1st of the next year, by adding 275 days. Since February is not involved, leap years are not an issue.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-expand-your-calendar/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-expand-your-calendar/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-expand-your-calendar/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-expand-your-calendar/#0)

[](https://sumproduct.com/blog/power-query-expand-your-calendar/#0 "close")

top