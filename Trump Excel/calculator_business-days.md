# Business Days Calculator: Count Workdays Between Two Dates

**Source:** https://trumpexcel.com/calculator/business-days

---

[Skip to content](https://trumpexcel.com/calculator/business-days/#content "Skip to content")

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/calculator/business-days/#below-title)

Business Days Calculator
------------------------

Count working days between two dates

Start Date 

End Date 

Holidays to Exclude (Optional)

 Add Load US Holidays

Calculate

There are **–** between –.

Business Days

–

Total Calendar Days

–

Weekend Days

–

Holidays Excluded

–

Holidays Excluded from Count

| Date | Holiday |
| --- | --- |

Share This Calculator

Made by [TrumpExcel.com](https://trumpexcel.com/)

Share Calculator

Business Days Calculator — TrumpExcel.com

 Include my inputs in the link

[Facebook](https://trumpexcel.com/calculator/business-days/#)
 [X](https://trumpexcel.com/calculator/business-days/#)
 [LinkedIn](https://trumpexcel.com/calculator/business-days/#)

 Copy

The calculator above gives you the exact count of business days (working days) between any two dates.

Pick your start and end dates, optionally load US federal holidays (or add your own), and hit Calculate.

You'll get the business day count along with a breakdown of total calendar days, weekends, and holidays excluded.

Below, I'll walk through how the count works, what the numbers mean, and the mistakes people commonly make when counting business days by hand.

How Business Days Are Calculated
--------------------------------

The formula is:

**Business Days = Total Calendar Days - Weekend Days - Holidays (that fall on weekdays)**

Say you need to count business days from Monday, March 2, 2026 to Friday, March 20, 2026.

**Step 1:** Count total calendar days. March 2 to March 20 is 19 calendar days (both dates included).

**Step 2:** Identify the weekends in that range.

*   Week 1: Mar 2-6 (Mon-Fri) then Mar 7-8 (Sat-Sun)
*   Week 2: Mar 9-13 (Mon-Fri) then Mar 14-15 (Sat-Sun)
*   Week 3: Mar 16-20 (Mon-Fri)
*   That's 4 weekend days total (2 Saturdays + 2 Sundays)

**Step 3:** Check for holidays. No US federal holidays fall in this range, so holidays excluded = 0.

**Result:** 19 total days - 4 weekend days - 0 holidays = **15 business days**.

Now let's add holidays to the mix. If we extend the range to Monday, January 12 to Friday, January 30, 2026:

*   Total calendar days: 19
*   Weekend days: 4 (Jan 17-18, Jan 24-25)
*   US holidays in range: Martin Luther King Jr. Day (Monday, January 19, 2026)
*   Business days: 19 - 4 - 1 = **14 business days**

That one holiday on a Monday costs you a full business day from the count.

### How Observed Holidays Work

When a fixed-date holiday like Independence Day (July 4) or Christmas (December 25) falls on a weekend, the US federal government observes it on the nearest weekday:

*   **Saturday holiday** is observed on the preceding Friday
*   **Sunday holiday** is observed on the following Monday

For example, if July 4 falls on a Saturday, the observed holiday is Friday, July 3. This calculator handles observed dates automatically when you load US federal holidays.

How to Interpret the Result of this Business Days Calculator
------------------------------------------------------------

The calculator gives you four numbers.

Here's what each one means:

**Business Days** is the number you probably came here for. This is the count of weekdays (Monday through Friday) in your date range, minus any holidays you chose to exclude. Use this number for:

*   Contract deadlines ("deliver within X business days")
*   PTO and leave calculations
*   Project timeline estimates
*   Payroll processing periods
*   SLA and response time tracking

**Total Calendar Days** is the raw count from start date to end date, including both dates. This is useful as a sanity check. A 30-calendar-day period typically contains 20-22 business days, depending on where the weekends fall and how many holidays are in the range.

**Weekend Days** shows how many Saturdays and Sundays fall in your range. For every full week, you get 2 weekend days. A rough estimate: multiply the number of weeks by 2.

**Holidays Excluded** counts only the holidays that fell on weekdays. If Christmas falls on a Sunday, it doesn't add to this count because that Sunday is already excluded as a weekend day. You'll see a detailed table below the summary showing exactly which holidays were excluded and on what dates.

Some Questions You May Have
---------------------------

**How does this calculator handle date ranges that span multiple years?**  
It works the same way regardless of how long the range is. The calculator loops through every day from start to end, checking each one individually. If you load US holidays, it generates them for every year in your range. A 5-year range works just as accurately as a 2-week range.

**Can I enter the end date before the start date?**  
Yes. The calculator automatically detects when the end date comes before the start date and swaps them. You'll get the same result either way. The result sentence shows the dates in chronological order, so there's no confusion.

**What if I need to exclude holidays from a country other than the US?**  
Use the "Add" button to manually enter individual holiday dates for any country. The "Load US Holidays" button is a convenience shortcut for the 11 US federal holidays, but you're not limited to those. Add whatever dates your organization observes as holidays.

**Does this match Excel's NETWORKDAYS function?**  
Yes. This calculator uses the same logic as Excel's NETWORKDAYS function. Both count start and end dates as part of the range, both exclude Saturdays and Sundays, and both let you specify a list of holidays to exclude. If you enter the same dates and holidays here as you would in NETWORKDAYS, you'll get the same result.

**Can I use this for payroll calculations?**  
Yes. Select the pay period start and end dates, load the relevant holidays, and you'll get the exact number of working days for that period. This is useful for calculating daily rates, prorating salaries for partial months, or verifying timesheet submissions.

**Why does the calculator show 0 holidays excluded even though I added holidays?**  
The holidays you added might fall outside your selected date range, or they might fall on weekends. The "Holidays Excluded" count only includes holidays that are both within your date range and on a weekday (Monday through Friday). Check the dates of your added holidays against your selected range.

**Note:** If you want to do this calculation inside a spreadsheet, Excel has a built-in function called NETWORKDAYS that works exactly the same way. Check out our [NETWORKDAYS tutorial](https://trumpexcel.com/excel-networkdays-function/)
 for details.

**Other Related Calculators / Articles**:

*   [All Free Calculators](https://trumpexcel.com/calculator/)
    
*   [Days Between Dates Calculator](https://trumpexcel.com/calculator/days-between-dates/)
    
*   [Age Calculator](https://trumpexcel.com/calculator/age-years-months-days/)
    
*   [Get the Number of Days in a Month in Excel](https://trumpexcel.com/days-in-month-excel/)
    
*   [Add or Subtract Days to a Date in Excel](https://trumpexcel.com/add-days-to-date-in-excel/)
    
*   [Excel NETWORKDAYS.INTL Function](https://trumpexcel.com/excel-networkdays-intl-function/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free Excel Tips EBook Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK