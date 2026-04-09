# Free Excel Leave Tracker Template (Updated for 2026)

**Source:** https://trumpexcel.com/excel-leave-tracker

---

[Skip to content](https://trumpexcel.com/excel-leave-tracker/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-leave-tracker/#below-title)

One of my teammates has the responsibility of creating a leave tracker template in Excel for the entire team. This tracker template is then used to track vacations/holidays and planned leaves of the team members.

Till now, she used a [simple Gantt chart in Excel](https://trumpexcel.com/gantt-chart-in-excel/)
 but wanted something better with more functionalities.

So, I created this Excel Leave Tracker Template to make leaves management easy and track monthly and annual leaves by her team members.

You can also use this as a vacation tracker template or student attendance tracker if you want.

Excel Leave Tracker Template
----------------------------

This Excel Leave Tracker template can be used to record and monitor employee leaves for a year (of a financial year where you can choose the starting month of the year).

You can track 10 different leave codes for an employee  – vacation leaves, sick leaves, maternity/paternity leaves, casual leave tracking, leave in lieu of overtime, and half days, etc.

It also provides a monthly and yearly total of different types of leaves that can be helpful in project planning and leave management.

It uses a bit of [conditional formatting](https://trumpexcel.com/excel-conditional-formatting/)
, a few [DATE functions](https://trumpexcel.com/excel-networkdays-function/)
, array formulas, and a simple VBA code.

_**Download the Excel Leave Tracker Template (tracking for 20 employees/people)[![Download File](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://www.dropbox.com/s/d3rrclciqrfoni1/Excel%20Leave%20Tracker%202021%20-%20For%2020%20Employees.xlsm?dl=1)
**_

Looking for the Google Sheets version of this **[Leave Tracker Template? Click here!](https://productivityspot.com/leave-tracker/)
**

**How this Excel Leave Tracker Template Works?**

*   Use the triangle icons next to the month name to move to the next/previous month (the template updates itself to show the dates for the selected month). There is a short VBA code that runs in the background whenever you change the month. It shows you the selected month only and hides all the other months.![Excel Leave Tracker Template 2020 - select first month of the financial year](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20680%20216'%3E%3C/svg%3E)
*   This Excel template can be used to track leaves for over a year. You can select a start month and can track leaves for a year. For example, if you follow the April-March cycle, select April 2023 as the starting month.
    *   **Note:** The value in cell A1 is to change the time period of the leave tracker ONLY. **DO NOT use Cell A1 to move to the next month while recording leaves.** Use the triangle icons next to the month names to go to the next/previous month and mark leaves.![Excel Leave Tracker 2020 - Change the months using the arrows](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20680%20216'%3E%3C/svg%3E)
*   You can specify the working days and non-working days (Weekends). At the right of the leave tracker, there is functionality to specify the working days by selecting Yes from the drop-down. If you select No, that day is marked as a non-working day in the leave tracker.
    *   As soon as you specify the non-working days, those weekdays get highlighted in gray color in the leave tracker.

![Excel Leave Tracker Template - Select Working Days and Weekends](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20216%20192'%3E%3C/svg%3E)

*   You can update the holiday list in the worksheet named “Holiday List”. It will automatically be reflected in the tracker by highlighting those days in Orange color.
*   To enter the leave record for employees, use the relevant codes based on the leave type _(you can customize these leave codes). For example, in the case of sick leave, use S, in the case of Vacation, use V, as so on.![Excel Attendance Tracker Template 2020 - Holiday List](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20415%20360'%3E%3C/svg%3E)_
    *   There are two codes reserved for half-day leaves. you can enter H1 or H2 for a half-day leave.![Leave Codes You can use in the Leave tracker template in Excel Vacation Tracker Attendance](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20207%20260'%3E%3C/svg%3E)

*   As soon as you enter the leave code for any employee, it gets highlighted in red (in the case of half-day, it gets highlighted in yellow). If that day is a weekend or holiday, the color would not change.
    *   Column NJ (highlighted in green in the pic below) has the number of leaves of that employee in that month. It counts the leaves on working days only (those on weekends and/or holidays are not counted). Half-day leaves are counted as 0.5.
    *   UPDATED: Column NK (highlighted in light red in the pic below) has the number of annual leaves taken by an employee. It counts the leaves on working days only (those on weekends and/or holidays are not counted). Half-day leaves are counted as 0.5.![Leave planner in Excel - Free Template - number of Leaves Month Year](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20649%20237'%3E%3C/svg%3E)
    *   Columns NL to NU gives the leave break-up by leave code (for the entire year). This could be helpful to keep a track of the type of leave that has been availed. Note that while Half Leaves are counted as .5 leaves in the total count, in the leave break-up, it is counted as whole numbers. For example, 2 half leaves would lead to 1 leave count, but you’ll see two half leaves in the leave breakup.![Leave Tracker Template in Excel - Leave Breakup by Type](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20282%20361'%3E%3C/svg%3E)

I have created this leave/attendance tracker template for 20 employees. If you want to add more, just copy-paste the formatting and formulas for additional rows.

Also, since there is a VBA code involved, make sure you always save it with .xls or .xlsm extension.

_**Download the Leave Tracker Template[![Download File](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://www.dropbox.com/s/d3rrclciqrfoni1/Excel%20Leave%20Tracker%202021%20-%20For%2020%20Employees.xlsm?dl=1)
**_

_Note:_ To update this template for any year, simply change the year value in cell A2. For example, to make it for 2017, just change the value in A2 to 2017. Also, you need to update the [holiday list](https://trumpexcel.com/holiday-calendar-excel/)
 for the specified year.

The download file is completely unlocked so you can customize it to your needs.

Here is [**another version of the template**](https://www.dropbox.com/s/0vme0dxrtd4ivln/Excel%20Leave%20Tracker%202021%20-%20For%2050%20Employees.xlsm?dl=1)
 that can track leaves for **50 employees**.

Want to learn how to create awesome templates and dashboards? Check out the **[Excel Dashboard Course](https://trumpexcel.com/excel-dashboard-course/)
**

FAQs on using this Leave Tracker Template
-----------------------------------------

Since I created this vacation/leave tracker, I have been inundated with emails and comments. What you see now is a refined version that has been possible due to all the feedback that I have got.

Based on the questions I get repeatedly, I have created this FAQ section so that you can get an answer faster (instead of waiting for me to respond).

Here are the most common questions I get about the Leave tracker template:

Q: I tried downloading the file but it downloaded as a zip. How do I use it?
A: I have fixed this issue, and now you should be able to download the Excel file directly.

Q: When I change the month, the existing leaves are reflected in the changed month as well.
A: This happens when you use cell A1 to change the month. You need to use the arrow icons to change months. Cell A1 is to be used only to set the starting month of the calendar. For example, if you want the calendar to start from April, make cell A1 value 4. Now to move to March, use the triangle icons.

Q: I need to track multiple years of leaves. Do I need to create a new worksheet for each year (financial year)?
A: Yes! This leave tracker can only track leaves for a 12 month period. You need to create a copy for each year.

Q: Can I use my own leave codes?
A: Yes! You can change the leave code in cells NX8:NX17. You also need to specify the same code in cells NL5:NU5. For example, if you change the Work from Home leave code to X, you also need to change it in NR5.

I hope you find this leave/vacation tracker helpful.

Are there any other areas where you think an [Excel template](https://trumpexcel.com/free-excel-templates/)
 could be helpful? I am hungry for ideas and you are my gold mine. Do share your thoughts in the comments section 🙂

**Related Excel Project Management Tutorials and Templates:**

*   [Holiday Calendar Template in Excel](https://trumpexcel.com/holiday-calendar-excel/)
    .
*   [Employee Timesheet Calculator Template](https://trumpexcel.com/excel-timesheet-calculator-template/)
    .
*   [Milestone Chart in Excel](https://trumpexcel.com/milestone-chart-in-excel/)
    .
*   [Making a Pareto Chart in Excel](https://trumpexcel.com/dynamic-pareto-chart-in-excel/)
    .
*   [Making a Histogram in Excel](https://trumpexcel.com/histogram-in-excel/)
    .
*   [Task Matrix Productivity Template](https://trumpexcel.com/free-excel-templates-excel-list/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

1,198 thoughts on “Free Excel Leave Tracker Template”
-----------------------------------------------------

1.  How can I customize this or can you please update this tracker to include two columns to the right of the Name and add a date range (date away then return) to then populate the data by leave type?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-45155)
    
2.  Is it possible to replace the monthly bar (to change months) and do a drop down menu instead listing all 12 months? With the bar, it is a bit laggy/unresponsive.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-41473)
    
3.  Hi,
    
    May I know how to sum up the leaves of certain types (like for example P, H1 and H2) for this month and this year but not all as types of leaves as in now? Please kindly advise. Thanks.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-38052)
    
4.  It’s great!, this template really useful. Thank you so much for your sharing.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-37821)
    
5.  Dear Sumit,  
    Thank you very much for this which is very helpful. I work in a hospital and want to use this to create an Excel sheet where all the different types of leaves taken by 10 different staff members can be recorded.  
    Everything works fine with your sheet. However, I need to upload this in a shared drive where many people can see it but not edit it as it will become unsafe if there is not a single editor.  
    However, when I password protect the sheet, the viewers are unable to scroll through the different months. How can I resolve this issue?  
    My viewers should be unable to edit the document but at the same time be able to view the whole year.  
    Thanks in advance.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-35480)
    
6.  Hello. This is perfect apart from ONE thing.
    
    I want to specify non/working days for each individual employee but the option only lets you do it for every employee.
    
    I want to do it per employee as we have part time members of staff.
    
    How do you do this, or can you amend it to reflect this?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-33753)
    
7.  I find the tool quite useful, but I encountered an issue with the week numbers formula not working in the file. It’s located in row 7, hidden below the name & employees rows.
    
    Could you please provide me with the formula or share an updated version of the template where the week numbers function properly?
    
    Thank you for your assistance.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-33250)
    
8.  Hi,
    
    Great Tracker!  
    Q:Is there a way to import the entire workbook to Google Sheets?
    
    Thank you!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-18458)
    
    *   Hello Christi.. You can upload the Sheet to Google Drive and then start using it in Google Sheets. It may need some adjustment in formulas though
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-18917)
        
9.  It would be great if there was a column for days available or accrued and days remaining. The days available could be a number entered, like 30, or it could be based on a formula of x days per month. The days remaining column should subtract either total days out or a selected subset. For example, I don’t get charged for my companies newly formed refresh/recharge days (covid inspired) but I am still out those days and added it as a code R above the half days.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-14903)
    
10.  Hi, How can I share the file only allowing the users to navigate from month to month using the arrows while keeping the data protected? I tried different ways of protecting the sheet, but was not able to make it work. Please advise
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-14902)
    
11.  Is it possible to copy the sheet and update it to a new year. I tried that by changing the year, the months change but 2020 stayed. When you try using the arrow to go from month to month, it get a VBA Debug error. Please get back to me at your convenience. Would be happy to pay for a 2021 template if that is an option.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-14898)
    
12.  This is a really great tracker. One thing I would like to be able to do is when I add a new employee, I would like it to not include that employee in previous months; and obviously i would like to be able to delete an employee without affecting their previous months. I know it is possible to do this, just looking for the best method to do so. Thanks in advance!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-14890)
    
13.  Hello, this has been helpful.  
    Question: I have been asked to create an extra column for “the number of days taken” after each month and I have tried several formulas but I am not getting it can you please help with a formula?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-14889)
    
14.  There should be another sheet where it has to give summary like employee name, jan leaves, Feb leaves and finally total leaves used for that month. Do you think is possible?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-14857)
    
15.  Thank you for this. I would like the sheet to count certain types of leave on holidays, such as comp time earned. If they work a holiday, they receive one comp day to use at a later time. Is it possible to formulate so only these 2 types of leave (full comp day and half comp day) are counted on holidays and/or weekends? Thank you again for sharing this, it has been very helpful!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-14831)
    
16.  Hi I love the template. I do have an issue. Having filled everything in and revamped some items to suit I have to password protect so that the staff members viewing it cannot edit, delete cells or make entries. they file a request based on the availability in the holiday window and I unprotect then make entries and then protect.  
    The problem is that due to the macro that changes the view from month to the next month they cannot view the months as the macro does not work whilst the sheet is protected? Any fix?? thanks  
    Steve
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-14816)
    
17.  I love this tracker! Thank you for sharing. Since we track FMLA on a rolling calendar, I’d like to track one person per tab. I tried duplicating the Leave Tracker Tab but the Starting Month function did not operate properly on duplicated tabs. Can this be done?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-14811)
    
18.  Any chance to have a 2021 version too? I love this file and would like to keep using it for next year.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-14805)
    
19.  I cant click the triangle icon . it shows like macros is missing
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-14762)
    
20.  Thank you very much for sharing this, it is phenomenal! I am looking to extend this to include multiple balances of different leave types (vacation, sick). I would like to include the accrual in real-time for each month in addition to deducting any time taken. If they accrue 13.33 vacation hours the last day of month, with no probationary period, how can I have the beginning balance minus used time plus the accrual in real-time? Example, John has 120 hours vacation in March, used 20 hours in May and accrues 13.33 at the end of each month. I need the balance automatically populated for the date I open the workbook. Any guidance is truly appreciated! Thanks again!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-14754)
    
21.  Thanks allot… for sharing your efforts here. Really very useful.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-14733)
    
22.  If the working days are different for different employees could we customize working days for each employee?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-14606)
    
23.  Thanks for this excellent stuff…really helped me a lot.  
    But i have small concern about it that when i mark for vacation it doesn’t add up the holidays which falls in between..i want that to be added..this is how calculation goes here in my country..any solution to this?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-14604)
    
24.  Hi,  
    I just want to know that I dont want to count Work from home in leaves monthly and annually. How can i change it?
    
    Regards,  
    Ajinkya
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-14561)
    
25.  Great file. Thank you. Any ideas on how I can add this into the existing document?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-14537)
    
26.  i want the vacation count only in leave this month and leave this year column. I have to change the formula in leave this month and leave this year. please help.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-14531)
    
27.  Hello Summit, Thanks for the template. Really excellent and it solves my purpose. My project resources are based on multiple locations and can you help me with the below additional requirement
    
    To create one dropdown attribute named Country and based on the country selection for that particular employee, the respective public holiday needs to be applied for that particular resource.
    
    Please help.
    
    Best Regards  
    Raghav
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-14440)
    
28.  Is there a way to pull reports or trends (graphs) for all employee leave taken during a month?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-14432)
    
29.  I would like to be able to enter hours per day (9 sick) and also total hours for each code (sick 23). This is already great, tracking hours would make it FANTASTIC!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-14404)
    
30.  Hi… this spreadsheet is really great and has helped me tremendously… I just have one question please. Is there anyway made the cells different colours for each leave code please? Ive tried to suss it out but can’t find how to do it. Thank you.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-14400)
    
31.  This is amazing! 🙂 I copied the tab and changed the arrow macros to ActiveSheet which worked but the month stays as ‘January 2020’ in the text box. How do I get it to automatically change to the next date? The formula is =Sheet3!G2 but doesn’t make sense to me 🙁
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-14331)
    
    *   Hey Sophie, not sure when you asked this but have you tried changing Column A, Cell 1 from 1 in the drop down options to the month you want it to start from? Worked for me when I changed it to 4 & now starts at April .
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-14455)
        
32.  Thank you for this – its truly amazing – I really like the way you can scroll through the months with the arrows, rather than navigating a long sheet – how do you set this up?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-14302)
    
33.  Hi the tracker is excellent and has saved me a lot of time.  
    I have some colleagues who work part time, is there a way to mark the days of for those people so it doesn’t show as a work day?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-14273)
    
34.  Hi,
    
    The tracker is superb but I need one more help on it. I would like to track the leave balance too. It is doable?
    
    Hope to hear from you soon.
    
    Thanks
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-14249)
    
35.  Hi , i want to remove Work from category from leave. When i removing from column all others cell being red. Pls help
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-14227)
    
    *   Its work from Home\*
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-14228)
        
36.  can a rolling year be added for the sickness? Also can you create tabs to add additional trackers for multiple years or does it need to be a new document each time
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-14218)
    
37.  Hi – I love this leave tracker, it’s great! Just one question, I like to protect the spreadsheet to avoid people make changes or overwriting formula – the problem is when I protect the formula area (the 2 red triangles either side of the month /year) I am unable to change the month and an error is issued saying that I need to unprotect the sheet. Can you help?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-14112)
    
    *   Don’t worry … finally figured out…..
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-14113)
        
38.  This has been SUPER helpful for me! Thank you!  
    Question: I know that we can only use the leave sheet for one year. However, is there a way to duplicate the leave sheet and the reference sheet within the same workbook and just change the year??
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-14103)
    
39.  How can I do only half year? means separate Jan – Jun & Jul – Dec? Thank you
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-14100)
    
40.  Super useful, thank you so so much for your work
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-14077)
    
41.  Hello Sumit,
    
    Your Leave Tracker is amazing and has really opened my eyes even wider to what Excel can do. I am trying to use this tracker for my employees but instead of tabulating the days and half days can this be modified to tabulate hours instead?
    
    Thank you so much!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-14064)
    
42.  Can it be customized to include different work days per employee? For example, not all employees have the same days on or days off. The ‘Select Work days” to be customized per employee?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13990)
    
43.  Hi. Its a great solution. I could use it to track leaves across multiple projects in separate sheets. Can a dashboard be added to it that will pull the total leave information of individual employees month wise for each project and colour code the individuals record if it exceeds a certain number of leaves for a month?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13958)
    
44.  Hi There, Thank you it’s helps, just a question, I have teams in different country and the public holiday is not same across all country, next to name can you include a column to add country?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13804)
    
45.  Can i use other colors for each leave code, like Green for Vacation, Red for Sick, Yellow for Maternity and so on.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13675)
    
46.  I want to include weekends for the sick leave only. How do I do that?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13644)
    
47.  This template is the best. I’d like to change the fill color for the Sat & Sun columns. Can I do that? Thank you.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13521)
    
48.  Is there a way to assign points to this spreadsheet to automatically calculate your company’s assigned point system based upon absence, tardy, etc?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13518)
    
49.  Love this sheet, thank you! How do you recommend using time carried over from a previous year?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13512)
    
50.  Very useful! Thank you!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13502)
    
51.  I am only over five employees, how do I take off the extra Employee’s.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13483)
    
52.  How do I change the color for each Code? How can I put in by hours instead of days?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13482)
    
53.  I need a 12 month rolling for sick leave, but each employee has different allowances depending on length of service, so I need to be shown a total of amount used and what’s left each month…can you help?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13473)
    
54.  How can we change the color for the code we enter, for example i want to change color of P code from red to other color?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13464)
    
55.  Is it possible to have the Working Days only Grey out Non Working Days, but still include counts in the totals?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13458)
    
56.  hi  
    when using the arrow buttons to change the month – it still reflects as January 2020
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13456)
    
57.  I absolutely love this and has been a great help for my team, I have a challenge though:-
    
    We all work with different start dates so for example my leave year runs 1st May until 30th April.  
    My colleagues may run 1st June – 31st May.
    
    Thank you though as it’s brilliant.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13450)
    
58.  I would like to have the leave count not consider W (Work From Home) – how do i do that?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13433)
    
59.  Thank you for the Leave Tracker. Can we calculate the leave hours instead of days? Sometimes employes take vacation hours not full days The sheet calculate by days. How can I change to hours?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13428)
    
    *   I like having the leave codes but need to do this by hours, too.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13481)
        
60.  Thank you for the Leave Tracker. Can we calculate the leave hours instead of days? Sometimes employees take 2 hours for an errand or a Dr.’s Appointment. The sheet calculate by days. How can I change to hours?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13426)
    
61.  This is fantastic! Exactly what I’m looking for. However I’d like to be able to track work from home days, over time days, sick days etc without it counting as leave in columns NJ & NK? Whats the best way to amend this formula?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13412)
    
62.  I am unable to download the file. Following error occurs. Please help  
    This site can’t be reacheduc654e21be693a433fe40dd5fd40.dl.dropboxusercontent.com’s server IP address could not be found.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13402)
    
63.  Hello! I have added 21 columns before all calculation (changed in VBA module new ranges), but facing issue with macros while moving months, as currently I see half JAN, full FEB and rest months of half starting in the middle of 31 columns. Could you advise what needs to be changed?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13391)
    
    *   Hi can you help me knowing if I need to change Vacation from V to AL. How do I do that ?
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13404)
        
64.  Would also like some additional Half Day Leave Types/Columns. I can’t figure out how to change the formula to accommodate when I replace other existing categories. Help please!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13382)
    
65.  Hi there, is it possible to add more Half Day Leave Types/Columns?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13368)
    
66.  Hi, I would like to additional enter personnel number to the column before the name. Is this possible? I tried to enter it but it messes up the dates of the month.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13325)
    
    *   Did you get an answer on how to do this?
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13791)
        
67.  Why on each month do I get random days coloured in orange?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13312)
    
68.  A person take leave from 8th Feb to 10th Feb i.e sat, sun & mon. After entering leaves on 8,9 & 10th Feb, excel formula only count leaves of 8th & 10th Feb. It should count all three days right? can you help me for that formula for the leave tracker template given in this page for all the months?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13309)
    
69.  how can i change on of the h2 to count as a quarter day holiday? I have changed the code, but the formula is the same and it still counts quarter day as half day.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13299)
    
70.  Could you advise how to use this fantastic template as a session worked for e.g. I have GP’s who work just the am and on another day a full day. I can do the half day which is great but I don’t know how to change the leave (vacation) to two sessions worked as it is not calculating the true amount of leave taken
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13296)
    
71.  Hi  
    I want the leave total column to add the leave days .
    
    Ex : If an employee is on vacation continuously for 30 Days. It should also consider the other (off) days as annual leave. Currently if vacation is marked on the leave days/off days, it is not capturing they. How would I make count the leavs uncluding the off dasy.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13254)
    
    *   I have the same concern. Kindly please advise how can I make the holiday and off day counted on leaves. Thank you.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13287)
        
    *   I have the same question.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13290)
        
72.  Hi….just downloaded but the triangle icon is not working.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13242)
    
73.  Can you help me please I need to add column before column A but when add any column reflect to the days of the month 🙁
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13239)
    
74.  This is fantastic! Exactly what I’m looking for. However I’d like to be able to track work from home days without it counting as leave in columns NJ & NK? Whats the best way to amend this formula?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13234)
    
    *   How can i remove H1 and H2? When i do so the formula is changing
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-35923)
        
75.  I want to lock the past date cells to prevent to edit because if some one took the leave and record it in the template it should not be edited after leave date passed , can you modify this and share the template on below email
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13222)
    
76.  How do i add more employees to the sheet
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13221)
    
77.  Hi,
    
    I have downloaded the excel template and it is very good to use and I have a query can we update the template based upon location for holidays.
    
    Ex: If suppose in a team there are total 12 members and 4 are from Banglore, 2 from Pune, 2 from Gurgaon, 4 from Hyd so the holidays differ from location to locaion so how can we distinguish the holidays among the team members.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13212)
    
78.  HOW CAN I ADD COLUMN TO THE RIGHT AND LEFT OF NAME COLUMN I.E. EMPLOYEE CODE AND EMPLOYEE DESIGNATION. KINDLY HELP ME I NEED IT BADLY
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13211)
    
    *   I also need the same solution, can someone help
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-14013)
        
79.  The excel spreadsheet for tracking leaves of 50 Employee’s isnt working properly. I am unable to move to the next month. Is there any way the spreadsheet can be reviewed by your website?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13203)
    
80.  there is no column showing leave available? How would I incorporate that?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13185)
    
81.  How to create this in excel. can you send the vedio?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13184)
    
82.  Thank you so much for this. You save me so much time!
    
    Regards,  
    M
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13178)
    
83.  I would like to use your tracker but I am trying to modify it. I would like to add a functionality wherein, I will put only the range of date leave on a separate sheet, example Jan. 15, 2020 until, feb. 1, 2020. I should not be manually plotting the dates one by one. Instead, after clicking an approve button, it will automatically be plotted.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13168)
    
84.  “The file is corrupt and cannot be opened”.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13153)
    
85.  Hi,  
    I have downloaded the 50 employees version and have changed the year for 2020, however in the process the macro to change month has become defective.When I saw to debug code, it highlights this part – Range(“A3”).Value = Range(“A3”).Value + 1 Could you please advise how I fix this so that I can continue to use.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13151)
    
    *   Please ignore my post. I found a workmate had protected the sheet and therefore it had restricted the access. Thankyou.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13152)
        
86.  Hello! Love the template. Thank you for making it available!
    
    I’m trying to tweak it some to add additional tracking capability. When I add the columns and codes for what I want to check it is working just fine, but I would like to exclude 3 codes of the 9 being used from being tallied in the ‘Leaves this Month’ and ‘Leaves this Year’ sum cells. I’m not having luck modifying the formula as I don’t have a lot of experience with so many layers of nesting.
    
    Could you point me in the right direction? Thanks!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13139)
    
87.  Is it possible to import it to gmail/google account so my co-employees can edit it and view it.?  
    Actually, I tried to import it and send the link to them to access, but some details missing like the month with ‘arrow left’ and ‘arrow right’. Also the holidays marked are missing.  
    And the ‘click here’ to copy the leave tracker is not accessible.  
    Hope you could help me with these.  
    Thank you so much.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13136)
    
88.  Hi, I also want to track the number of times a person is late within the month. Is there a formula for that?
    
    TIA
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13134)
    
89.  My company allows leave to be taken in hourly increments, is there a way to create codes such as V1(0.125) V2 (.25) V3 (.375) V5 (.625) V6 (.75)& V7 (.875) into the leaves formula’s? The complexity of the formula is beyond my scope I cant figure out how to edit it myself help!!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13108)
    
90.  may i asked how you did the formula or total leaves
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13101)
    
91.  Is it possible to make an entry for 1/4 DAY worked?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13094)
    
92.  Hi, I have uploaded the excel sheet in SharePoint but the triangle icon is not working. When I tried to use the filter, it’s not going to any month. Please advise how this gonna work? Thank you
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13093)
    
93.  I have DL the 50 Employee template, i have selected the full 7 days as working days in my industry. Within the tracker there are orange columns which when you edit with any of the Leave Names it does not collate this in the totals, why is this and can it be rectified?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13083)
    
94.  I downloaded the excel sheet but the red arrows aren’t working. What can I do?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13075)
    
    *   Click on the second worksheet titled HOLIDAY a yellow icon will pop up just above the sheet requesting you to enable, just click enable, then return to the first worksheet, the arrows would now be able to work. I hope this is helpful to u.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13111)
        
95.  i have been using this tracker for over a year now as we have over 250 employees in our department. it is working well so far. thank you. I have a question, what if an employee gets separated from the company for example in October but i have data in previous months, I don’t want to delete the record, i want to keep the data for record keeping, how & what can i do ???
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13070)
    
96.  Is it possible to have 3 Half Day Codes and have those half day included in other codes? i.e: Vacation Half Day also gets added to regular Vacation code, etc.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13055)
    
97.  Amazing spreadsheet!!  
    Would it be possible to implement half-day Holidays on the holiday list? Thank would be very convenient!  
    THANKS!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13048)
    
98.  I admire the spreadsheet created. However I have tried copying and pasting for the next year in the same sheet without it working – no doubt because of the referencing of the formulas. Is there a way to have multiple years shown here?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13046)
    
99.  Hello, I have downloaded the spreadsheet but everytime i open it up it asks for the start date of the year repeatedly and I cannot go past the pop up box constantly coming back up. I have to force quite excel. Could you please tell me how to get round this?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13042)
    
100.  Hi, we have different working days for different employees- Sunday to Thursday, Monday to Friday and Tuesday to Saturday. Is there any way we can configure the working days for each employee?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13040)
    
    *   I’d like to do the same.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13238)
        
101.  I wish there was a way to have some leave codes not add to the monthly/yearly totals. Not all our leave is chargeable. I tried to edit the code but it is way above my skill level. Even if I don’t edit the monthly/yearly cell and only select it and hit enter it gives the #VALUE error.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13023)
    
    *   This would be very helpful! I would like to track employees who work from home but that isn’t technically a “leave”.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13054)
        
102.  How can I have the calendar reflect holidays where the day before is a half day for all employees, i.e. Christmas Eve and New Years Eve? My company doesn’t normally give these as holidays but this year we are closing a half day. I want to make sure the employees are given only a half day for this day if they choose to take PTO during this time.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13011)
    
    *   They could just use the half day code.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13024)
        
103.  How can i change the “Leave This Month” and “Leave this year” formulas, so that only “Vacation” is counted as 1 and H1 and H2 as half but all else ignored?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13005)
    
104.  Very good guidance !
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12983)
    
105.  My company allows for time to be taken in hourly increments, not just half or full days. it this template able to handle this or will I need to look for a different solution?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12932)
    
106.  This is an awesome template. The only thing I am wondering if it’s possible is whether we can designate certain Holiday’s for certain employees. I work for President of an International Team so we have folks in Canada, Australia, Mexico and we are expanding into more countries. It would be great if I could somehow designate the different holiday’s by region for each person.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12902)
    
107.  Hello – i have downloaded your Leave Tracker template and customised for x 33 employees for 2020. How do i print the document so that all x 12 months print please – in one go ? thank you.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12900)
    
108.  Hi, can you create a template tracker for capital expenditures? Like monthly we will input the actual capital expenditure spent for the month, then we will do a re-forecast for the remaining months. Also, different sites with different list of capital expenditure projects (additional new projects may be added to the list as time goes by) also add complexity for monthly report use.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12897)
    
109.  I need to count the text entered in Sunday’s & Holiday’s for Leaves. Please modify.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12885)
    
110.  Hi this is a great tracker unfortunately my business has disabled the ability for macros to use – any ideas on how to use the template without the macros?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12884)
    
111.  I’m having trouble with the Holidays. Some of the holidays are not off days for our company. But even when I remove those holidays on page 2, they still remain as days off on the tracker.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12877)
    
    *   I have this same question. Did you manage to figure it out?
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12951)
        
        *   I deleted the row and it worked for me.
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13025)
            
112.  Very good guidance
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12864)
    
113.  In a seperate sheet, can I get the summary of leaves month wise for all the employees.
    
    Here it shows month wise. I need the detail of leaves one year at one place.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12861)
    
114.  How do I add additional Holiday’s. I tried to insert a sheet row but that didn’t work.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12860)
    
115.  Hi can i add working on Saturday and my employee will get time in lieu for this
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12793)
    
116.  This is very helpful. Can you add a column after the “Leaves This Year” to count the total of Leaves they took on a holiday. Thank you!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12792)
    
117.  I want to make the 2nd and 4th Saturday ass weekoffs.  
    Kindly suggest how to do that.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12780)
    
118.  Hi! Great spreadsheet! How can I change the holiday year? Instead of starting from January to start from April. I have done it in Sheet3 but once I change it then the days are offset.  
    Thank you!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12770)
    
119.  Hi! I absolutely LOVE what you’ve created! I’ve been playing around with this and think it’s amazing! I did have one question. I’m wanting to be able to track hours and not just half or full days off. I’ve been playing with the formulas and can’t seem to get it to work. Is there a way that you can have 0.1, 0.2, 0.3, 0.5, 0.6, 0.7 as codes for 1 to 7 hours off and have it calculate just like you did with the H1 and H2?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12738)
    
120.  Can I change color codes for example annual leave green, sick leave not paid red, sick leave paid blue and maternity pink
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12723)
    
    *   You have to do that in the conditional formatting area.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13026)
        
121.  how to mak all the full function can you provide video on that exel leave tracker
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12721)
    
122.  Hi,
    
    Thank you very much for this.
    
    I want to include “IN” and “OFF” on the days that employees are working and have off days but I do not want these to be counted when entered into the cells? How to exclude these so they are not counted in the leave totals? Thanks very much.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12702)
    
123.  Hi I have 80 employees, please suggest how can i add more to track leaves template of 50 employees?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12678)
    
124.  How do you add employees to the list? We have over 100 people on staff.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12671)
    
125.  i really love and like your “Leave Tracker Template”, for now i create for custom but still used your template 95%, but mostly i would like to ask about how to make change Leave tracker into attendance mean i would like make your leave as attendance in a month, put NJ8 = NL8, but formula NJ8 same as NL8, so every month change will keep as many leave track/”as leave code” for now leave track count in a year! i wish i can send my file to you…
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12611)
    
126.  I want to remove half day leave from the excel sheet. How to modify the formula.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12569)
    
127.  hi,  
    pls tell me how to update if any only one Sunday or Saturday working allotment
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12555)
    
128.  This works really well, except how do i edit the formula so that it does not deduct sickness and home working from your leave? If an employee gets 22 days holiday, I do not want the formula deducting leave when they work from home as this template seems to do that? I simply only want it to look at certain codes and deduct those eg vacation and half days.
    
    Is it possible to do this?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12551)
    
    *   I had a very similar question. Please let me know if you have an answer.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13027)
        
129.  When I saved the tracker and then reopened it, the macros would not work. I tried resaving enabling macros and it still would not work. Suggestions?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12514)
    
130.  Great Tool. Is there a way to create a summary of the tracking so you can see the whole year at once?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12505)
    
131.  Hello,
    
    This is very nice, but I am using SharePoint. It doesn’t allow for macros. You don’t have a version without the VB macro to move from month to month or ideas on how to create one without VB macro?
    
    Regards,
    
    Peter
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12499)
    
    *   macros work on our sharepoint
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13028)
        
132.  Thank you for the helpful leave tracker. One simple thing that can be done to faciliate customization is to use cell references in rows NL5:NU5, rather than hard-wired codes. Just have cell NL5, for example, =NX8; NL6 = NX9, etc.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12471)
    
133.  Hey creator! i love this solution. however how can i only count leave labelled “V” and “H” whereas the rest are just indicating they are on “S” without adding to the total monthly and yearly leave?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12447)
    
    *   I have this same question. Did you manage to figure it out?
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12552)
        
134.  How can I make the H1(half-day) column as 0.5 as well instead of 1?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12446)
    
135.  This spreadsheet is awesome!!! I’ve made few tweaks to match our organization’s attendance policy. However, I now need to be able to see a detailed listing of missed days (and the type of missed days) for one individual at a time….a report of some type that can be printed and placed in an employee’s personnel file.
    
    How can I do this?? I’ll be more than happy to share the current sheet I’m using.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12444)
    
136.  Are you able to add a rolling total of holiday taken month on month so that you can see how many remaining days the employee has left, I’m not sure how to add this into a workbook that has macros (so what I need is annual entitlement, leave taken this month, leave remaining, so that it carriers across the entire year. If you have any advise it would be appreciated. Thank you
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12422)
    
    *   I got the same problem as well. Also, I would like to add one more column of the carry forward vacation days plus the total annual entitlement. Please advise.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12462)
        
137.  how can i change the color when i enter codes into the cells. for instance i’d want Vacation cells to turn green and sick days red
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12415)
    
138.  Hi. how can I add 4 more columns after “Name” without messing up the formula?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12400)
    
139.  Fabulous work. We just started using this. Hope it works for us well. Was simple to use but will know more once folks start to use it.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12396)
    
140.  Hey this template is amazing. but i need further help. In our organisation, employee fiscal year is from the date of starting.. how do i do that for every employee. please help
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12384)
    
141.  Thank you so much ! I am loving it. Will you do a new one for 2020 ? please say yes 🙂
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12371)
    
142.  This is awesome! I created it on excel but was trying to convert it to Google Sheets. It doesn’t copy all the formats..etc. Any tips on how to get it to google Sheets?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12361)
    
    *   Hello Ashley,  
        Did you get an answer to this?
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12549)
        
143.  The Excel Leave Tracker Template is wonderful, but One question – how do I change some of the values from 1/2 day to full day. I’m looking at the formula and have not yet figured it out. Any suggestions?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12341)
    
144.  This is really useful, thanks. How do I change the colour so that each type of leave is a different colour?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12288)
    
145.  How can I restrict access to view only when sharing with others
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12280)
    
    *   I would like to know this as well.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-14764)
        
146.  wow, thank you very much!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12273)
    
147.  how can we insert one more column for emp ID with no changes in the code  
    ?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12257)
    
148.  Thank you for sharing this tracker, I want to share this information with all our staff. How can I protect it so others have access to view only?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12255)
    
149.  I want to add more type of leave, how to make it automatically counted either as 1 day or 0.5 day? I tried to copy to formulas but it does not work, and the new leave I added in is not marked as highlight as well.  
    Thank you.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12241)
    
150.  Yes, its so helpful and make my job in tracking annual leave for each individual so much easier~ thanks!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12239)
    
151.  how to set working days for specific employees,because their non working days are different.  
    Also what can I do if the time frame of employees allowed vacation are not the same ??  
    I tried to duplicate the sheet to change years but wasnt working
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12227)
    
152.  Hi this is a very good tool that helps managing the team capacity.  
    Here some input for improvement:  
    – Add the Indicator of team capacity (target) and a rule to automatically check the target with availability? for instant my if my expected capacity of a team is 8 people and i have a rule of only 2 planned absence in the team i would like to get an alert when the absences exceed the rule.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12209)
    
153.  Hi. This template is very useful and serves a very god purpose. However, what if I don’t want to include work from home as part of leave? I want to exclude work from home from monthly as well yearly leaves. I tried to change the formulas a couple of places, but didn’t work. Appreciate your help on this.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12199)
    
154.  Thank you very much for sharing this you have just saved me hours of creating my own version i am truly grateful.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12188)
    
155.  I don’t need that many holiday types, just want to keep it simple for Leave and the half days. But when I delete the rest leave types the conditional formatting to show the red and yellow colours disappears. What should I do to keep the conditional formatting?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12152)
    
156.  This is very helpful to tack leave for all employees, but how can I download this excel file directly.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12125)
    
157.  This is very helpful. Anyway, i have one question. If employee take half day of sick leave, how could we track it? Because from your template, we cannot track half day leave by specific type of leave.
    
    I’m looking forward to hearing from you and many thanks in advance.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12121)
    
158.  It would be nice to have a spreadsheet to track hours, OT and calculate PTO. If it could be attached to this one, you would have a winner.
    
    Thanks for the help. I needed this.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12118)
    
159.  HOW TO PRINT THE FILE SHOWING EVERY EMPLOYEES LEAVE DATES?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12108)
    
160.  HOW TO ADD ANOTHER TWO HALF DAY FOR LEAVE TYPES? I NEED HALF DAY VL WITH PAY, HALF DAY SL W/ PAY, HALF DAY SL W/O PAY AND HALF DAY VL W/O PAY?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12102)
    
161.  Very neat tracker. Thanks so much. & My question is how can this be made so that when an employee put their details on an input bar or a different sheet, their data will automatically entered into the “group” sheet? This is in order to get data from individuals without them seeing others’ input that they can accidentally mock up.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12066)
    
162.  Awesome
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12065)
    
163.  Hi,
    
    Does this template has the capability to handle multiple region public holiday calendar. For e.g. employee in America have 4th July as public holiday but employee in Europe will be working on that day.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12056)
    
    *   I have same issue. Is there a solution?
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-14765)
        
164.  hi, how to input our total annual leave ?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11947)
    
165.  This is a very awesome Leave Tracker, Thank you so much! Been using it for a while now. Was wondering if you can maybe make a google sheets version that has months from Feb 2019-Jan 2020. Our company renews their leave every year on the 1st of Feb.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11878)
    
166.  The Leave Tracker works great! I do have one suggestion. I have employees whose working days, are not the typical Monday – Friday with Saturday and Sunday off. I have employees that have different schedules. I was hoping you will be able to modify the “Select Working Days” function towards individual employees that way the formula can calculate Leave Name and code on each employee on any day of the week.
    
    For example: Monday – Sunday cells on calendar for each employee should have an option that designates working day a “Yes” or No” selection.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11875)
    
167.  Hi,  
    I like the tracker and would like to use it also. However, I would like to add designation and date of joining to the tracker next to employee name. Whenever I insert a column, it shifts the date ahead. Please help.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11869)
    
168.  I want alternative Saturday as a working day. How to do same changes in Leave tracker excel sheet?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11833)
    
169.  Dears, how can I introduce/modify a leave reason weight so that, for instance, remote working is not counted as “leave” ?  
    Tried modifying the Leave formula but can’t get it to work … Thanks !
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11785)
    
170.  I have entered a Leave Name for Provisional Leave and I do not want it to add a day to the leave taken sum. How do I format the code I enter to have a zero effect on leave taken?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11760)
    
    *   Hi, did you get it working? I’m trying to obtain the same but the formula is quite complex…
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11786)
        
        *   Hi no sorry I have not received feedback yet.
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11787)
            
171.  Your Excel sheet id quite excellent. I have few doubt to ask..!
    
    1\. i’m working in a company, my job is daily updation of leaves. So we use multiple sheets for working. now i need to work using your excel sheet, but i can’t copy the sheet to another. some problem occur during copying.  
    2\. Using your sheet for a year. one employee is joined in January, their details remains till the end of that year. if we delete when the resigned, whole data would goes with it.  
    we want the month changing system, but in data should enclose with that month only, is that possible.  
    please give me a solution. i’m waiting for your concern.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11711)
    
172.  What if we follow alternate saturdays working ?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11684)
    
173.  Attan: Dara Pettinelli. Never trust Abby Perlman because she was planing to lock up Dara Pettinelli using CBS anchor Otis Livingston!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11681)
    
174.  fantastic sheet… was wondering if i only wanted may and june, how do i do that?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11619)
    
175.  Hi, we are trying to use this but someone has noted that if you enter ‘W’ eg Work from Home day – it is counted as holiday. This logic is wrong. How can I edit this? Thanks.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11607)
    
176.  hello… liked the tool. i just want to enables multiple employees can open the sheet at a time.. it shows error “cannot be shared because has Maps or HML … ) how to fix it
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11595)
    
177.  hi, i was wondering if i can modify one of the codes for certain period of time less than a half day, lets say 3 hours. Thanks!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11574)
    
178.  Hi this is great thank you. I’m wondering if you can tell me how to add employees as we have 70?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11570)
    
    *   Insert a row and copy the formatting using the format painter tool.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11761)
        
179.  can we add the annual leave in clumen
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11566)
    
180.  Hi,
    
    How come I can note Enter V-(vacation) on a Holiday.  
    How can I do this with another code?
    
    Looking forward to your soonest response.
    
    Regards,
    
    Prec
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11545)
    
181.  Hi I need to calculate comp days for when an employee works on a weekend due to work travel. I still want to leave the sat/sunday as non-work days but I can’t get the excel doc to calculate any annotation (OT) on the weekends. Any ideas on how I can add this into the existing document?
    
    Thanks
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11537)
    
182.  Hi, the sheet is fantastic, however I would want to add time for employees for each day. When, say if I add 10:03 to employee 1, leaves increase by 1. How can I mitigate this issue?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11509)
    
183.  Great spreadsheet!
    
    How can I make it to where an absence will drop off after 90 days?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11504)
    
184.  I want to keep track of total SICK days taken, but they are not to be counted against (deducted) from leaves remaining. How to make this change?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11486)
    
185.  I really like the look of your template and would like to use it. Do you have a leave template that includes part-time workers whose holidays are set in hours, not days?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11479)
    
186.  Hi! Your template is greatly useful. However, there is one thing you haven’t mentioned. It’s the compensation day. For example, we have a holiday from Friday to Tuesday and the next Saturday we will go to work to make up for Monday (this day isn’t a holiday but we’re off to have full holiday). How can I mark up only that Saturday as working day. I think there may be a similar table as holiday sheet.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11447)
    
187.  How can I change the leave codes to reflect different colors? I wante Maternity to be different color than regular vacation.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11445)
    
188.  Hi! Thank you for this. However, I am unable to use is as the triangle icons do not work. The pop reads : Macros in this document have been disabled by your enterprise administrator for security reason. How can I fix this?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11440)
    
189.  Thank you for this! Saved me a ton of time. Two small comments:  
    1 – Macros are worrying. I inspected them before I allowed them to run. They are safe but you might want to mention them in your blurb.  
    2 – Give some instruction about how to create new conditional formatting rules for custom coloured leave codes.
    
    Thanks again!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11436)
    
190.  I want to add one more leave type that is short leave and assign it value 0.25, can anyone help me for that?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11376)
    
191.  Hi. Thank you. This is very helpful template. Do you happen to have one for timesheets for employees?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11374)
    
192.  i am not able to share the workbook
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11370)
    
193.  It would be great if you could actually track numbers of hours of leave taken per day for each category (so rather the “A,” It’s “A8” for a full day’s annual leave; or “A5” for five hours annual leave on a day). For instance, if someone goes to the doctor and it takes three hours, it would be great to log three hours of sick leave on the specific day.
    
    Also, it would be great to test the number of days leave taken against the maximum allowed (for example; a maximum of 10 day’s annual leave per year; or 30 day’s sick leave per three year cycle).
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11364)
    
194.  This is amazing! I cannot see the triangles where you change from month to month but they are there as I can click on them and change the month – how do you make them visible?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11363)
    
195.  Hello,  
    how can I change the colour for highlighting the noted spots??  
    For example, once I add s, v or h1, I Would like to have green, light green, blue and yellow instead. And I would like to have a few different colours for highlighting.
    
    Can you please help me with this?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11338)
    
    *   I just adapted the sheet for this very thing. It’s not too tough as it’s done with conditional formatting.
        
        For example: Create a new conditional formatting rule using Classic and Formula =B8=$NX$10 applying to ‘Leave Tracker’!$B$8:$NI$27 and give it some custom colours. You will need to remove the NX line from the rule that currently turns it red. Good luck!
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11435)
        
196.  thank you  
    it is fantastic  
    I have 2 questions  
    1.how to reduce the employees number  
    2\. in some countries the holidays are more than one day, even up to 7 days how to adjust it
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11334)
    
    *   Hi there, I have the same two questions – did you manage to find anything out about these? Thanks
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-12999)
        
197.  Hello, this document is amazing. However, I would like to add a column between the employees name and the first day of the month and I can’t seem to find how to do that without impacting everything. Any thoughts?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11321)
    
198.  This is amazing! Thank you.  
    How do you do the triangle things?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11318)
    
199.  i wanted to know how i can remove employee 3 from February month. i want this employee only in January. From Feb onwards i dont want this employee in the leave track as he is resigned.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11316)
    
200.  hi, since we have different week offs for employees how can i mark week ends for each employee seperately?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11314)
    
201.  Hi Instead of H2 which is Half Day Leave 2, I want to create a new code altogether as Unplanned Leave but still the value shows as 0.5 whereas it should get changed to 1 ideally. Could someone please tell me how to alter this change?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11290)
    
202.  This leave tracker template is the best I’ve seen. Thank you.
    
    Just wondering if it’s difficult to add a section where you can enter the number of leave days that are allowed and so the days left over can be tracked.
    
    Thank you again and looking forward to a possible solution.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11270)
    
    *   Hi Marc,
        
        It’s not difficult. I just inserted some columns at the end and added in the formulas.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11319)
        
203.  Hi! Thanks for the amazing tool! Any idea how I can print a document showing all months at the same time?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11269)
    
204.  Hi! Thanks for the amazing tool! Any idea how I can print a document showing all monts at the same time?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11268)
    
205.  Hello.
    
    This is a great tool to track the annual leave for the workers in the company. I am a big fan of the different reason for leave. However, there is something that I think will be useful and maybe someone can help me with. For example: If we have a worker who works in some of the holidays, later need to be compensated with an extra day. How we can track the extra days for the workers who work on holidays?
    
    Thanks for your help!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11248)
    
206.  Hi, this is a great tool for leave tracking, thank you!! Is it possible to change the colour of each leave type? For example all codes highlights the cell in red, is it possible to have different colours for each different code?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11241)
    
207.  Hi, this is a very nice leave tracker, but i have employees from multiple locations and their holidays are different; is there any way we can set that up?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11213)
    
208.  Hi This Leave tracker is fantastic. Thanks for sharing. However my HR is running on monthly cycle of 16th – 15th every month. First month 16Dec18-15Jan19, Second month 16Jan19-15Feb19.. and so on. Can the dashboard and vba formula be adjusted to achieve this?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11210)
    
209.  Hi,
    
    This is an excellent leave tracker.  
    I have few questions:
    
    1- We do not half days leaves so how can i remove it from formula and instead use my own codes for full day. I tried removing 0.5 with 1 in formula but it didn’t work.
    
    2- How can week ends be included in tracker calculation if someone is assigned to work on weekends?
    
    Thanks
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11203)
    
210.  This Leave Tracker Template works very well. The one addition I would like is ability to assign points to each leave type instead of just counting 1 occurrence or the half day. Attempted change but could not get to work. Any change to yearly or monthly column generates InValid error.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11199)
    
211.  How I can upload this to work in Google sheets?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11197)
    
212.  This tracker is really cool , just what I need. I have one query though, if I want to change the leave codes and delete few of them , the formula for the color coding does not work can you please help me with that
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11188)
    
213.  Thank you very much for this. It’s simple, works on a complex level and is EXACTLY what I need. Thank you for making it available.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11182)
    
214.  hi
    
    i am not able to change the month to feb in leave tracker.  
    i get a message that macros disabled  
    can u help
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11181)
    
    *   Hi Ritu,  
        You need to change the spreadsheet type to a “macro enabled” Excel Workbook.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11320)
        
215.  This is tracker is great!!! i have a question though. we have limited leaves at work and no overtime pay but we have “offsets” which are excess work hours that we can use in place of leaves at certain cases. how can I count cumulative offsets and offsets used apart from the leaves in one spreadsheet?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11178)
    
216.  fantastic work  
    i really thank you for this  
    but i have question, how can I print all the months in on paper?  
    i tried and all i can print is one month, the rest months does not appear to be able to be printed,
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11157)
    
217.  I am trying to add a few codes in the table and cannot figure out how to get them to calculate correctly in the leaves this month and leaves this year columns. Can you assist?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11148)
    
218.  I know this was created a few years ago but I am hoping you can still help. The spreadsheet is perfect for me except the holidays listed are not part of our holidays. I was able to make the change to the list but it doesn’t include the column in the calculations. Can you help me? For example, my employees work on MLK and President’s day.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11138)
    
    *   Just delete those days your employees work off the holiday list. For holidays you have but are not on the list, simply type in the name and the date. They will populate.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11183)
        
219.  Great work. I am loving it. Please if i want another column (between NJ and NK) that displays the amount of half days taken per month so as i go to the next month it resets; so that at a glance i can know how many half days an employee took per month…id be really grateful.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11119)
    
220.  This spreadsheet is excellent, exactly what I was looking for to track leave. Thank you 🙂 Is there a way to change the colour coding of vacation leave so you can see the difference immediately between sick and vacation
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11106)
    
221.  how do i capture the remaining number of leave days the employees has in a year
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11098)
    
222.  Hello! Thank you so much for sharing this resource, it is amazing. Is there anyway you could please guide me through changing the dates? Our pay period isn’t based on the month, it’s from the 20th to the 20th (for example, 1/20/19 – 2/20/19 counts as one pay period). Any help you could provide would be greatly appreciated!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11095)
    
223.  This is superb !!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11093)
    
224.  This excel is very nice. But how can I add minutes of late in the tracker so that it will add the leaves and lates. Thank you
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11091)
    
225.  Do I have a control on this tracker once downloaded? im afraid it will be corrupted since this is my tracker for my company’s leave/s
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11086)
    
226.  Is there a way to assign a different color to each leave code?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11073)
    
227.  Please check the week number – its not working “#N/A” this is what I see in the box….  
    I have both of your versions – 10 and 20 employees. . . .
    
    Thanks so much for your amazing work.
    
    Kind Regards,
    
    Newman
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11065)
    
228.  To the Hayley Bama and Bircbox. Ex editor from More magazine Abby Perlman recently got involved in dirty coraption business with crazy CBS anchor Otis Livingston to steal money from Bircbox employees bank accounts. Never deal with Abby Perlman and Otis Livingston they belong in prison!!!!!!!!!!!!!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11063)
    
229.  How do I create a column after the employee name . I need 4 columns. but when I add the date changes.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11048)
    
230.  Is there any way to have multiple sheets of these work on one file? When attempting to use it for multiple departments it gives an error “Runtime error “1004” Method ‘Range’ of object’\_Worksheet’failed
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11033)
    
231.  Good day! I have loved using your leave tracker this past year for 2018, I modified it for my vacation schedule in Canada 😉  
    Will you be providing a 2019 leave tracking soon?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11017)
    
232.  helo this leave tracker is very helpful, just having a problem on changing the working day example in this program SAT and SUN is considered day off but in my case our day off is Friday how can I edit the codes. Please kindly help me because I am not really good in these. Thank you!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11016)
    
233.  i love the template, but would you be able to share how did you create the top portion where you click the arrows for the months to change, as i would love to use that for some other of my sheets. Thanks
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11008)
    
234.  Hi. Can you protect the Leave Tracker worksheet so the cells cannot be manipulated except the scroll bar – moving month to month, brining up the data for each month?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11006)
    
235.  This is a great sheet !!!! Thanks so much.  
    The only issue I am having that if I put a password on the sheet so users are only able to change the month and edit the cells, the arrows gives me an error when going through the months
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11002)
    
236.  Hi,
    
    This is awesome tool! We have employees with different work week. I would like to add all the names in the same spreadsheet rather than copying the same workbook for different work week. Is this possible? Looking forward to your reply. Thanks.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11001)
    
237.  Hi,
    
    Thanks for the tracker. I would like to customize the tracker to run with our financial year from July to June. could you kindly assist with the codes for that. in addition, i’d like the leave to only count vacation days and half days.
    
    how do i change the code to that?
    
    Regards.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11000)
    
238.  I have changed some of the info on the holiday calendar…adding some more lines and they did not change to orange on the spreadsheet indicating they are statutory holidays. How do I correct that?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10997)
    
239.  Hello there! This spreadsheet is awesome! However, the only problem that I see relates to the counting of holidays.
    
    Per the US Department of Labor’s Employer’s Guide to The Family and Medical Leave Act (WH-1421): Calculating FMLA Leave…
    
    Time that an employee is not scheduled to report for work may not be counted as FMLA leave. Only the amount of leave actually taken may be counted against the employee’s leave entitlement.
    
    When a holiday falls during a week in which an employee is taking the full week of FMLA leave, the entire week is counted as FMLA leave. However, when a holiday falls during a week when an employee is taking  
    less than the full week of FMLA leave, the holiday is not counted as FMLA leave, unless the employee was scheduled and expected to work on the holiday and used FMLA leave for that day.
    
    An employee does not accrue FMLA leave at any particular hourly rate.
    
    Would you be able to address how to correct the leave count?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10987)
    
240.  Hello, how to add holiday and day off in the total?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10982)
    
241.  I am with Sharon Williams & Laura. I really need to be able to change the color of the codes so they are more distinguishable for my upper management team. Please advise ASAP
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10972)
    
242.  Can I change colours of a code. For example, I may want casual to be a different colour from vacation
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10967)
    
243.  This is exactly what I’ve been looking for. However, I changed the list of holidays to reflect the holidays that we offer. How do I remove the orange highlight on the column for holiday that is a workday for my employees and not a day off?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10966)
    
244.  Hi, this is very useful in my end.  
    \-I want to know what is the formula if I am going to breakdown the Leaves per month.
    
    Thanks,
    
    Alma
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10962)
    
245.  Hi this is great and super useful. I want to ask if I can do the following:  
    – Assign certain Holidays to employees (example certain holidays only apply to certain employees located off-shore etc)  
    – How can I add a “Late” or “Tardy” counter?  
    – I want to change Work from Home as a valid working day therefore will not count as a leave
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10960)
    
246.  Hello, this is exactly I need, just it would be nice to have the month, days and some other words translated into slovenian, how xould I do this?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10956)
    
247.  wow. its awesome leave tracker. how to change holiday for 2019? Plz guide me
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10950)
    
    *   Change it in the “Holidays” tab
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10961)
        
248.  Hello, How do I add more employees? I have 100 employees
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10930)
    
249.  I love your tracker. If there is option to mark 2nd & 4th Saturdays as Non Working day, it will be more use full. I know there is option to mark as leave days, but i need it show as non working day. Please look in to it and add this if possible.  
    Thank you.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10929)
    
250.  why is showing orange color on some colom and can i chose my on color based on type of leave ??
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10925)
    
251.  How can I reduce the list from 20 employees to 5 employees
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10916)
    
252.  Hello, please advise how I could add two columns for back-up persons within the view for each month. How should I edit the formula? Many thanks for the help!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10907)
    
253.  I love your tracker, but is there any way to track using hours instead of days? A few employees work 10 hour days instead of 8, and we are also allowed to take a few hours of vacation or sick time. Thank you.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10895)
    
254.  Hi,  
    I’m trying to add the Team manger, however, got error with the date and is there is any way to get over view of each month team manger wise and month wise.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10879)
    
255.  Hi, want to ask if there’s a way to summary into another sheet the balance of leave taken from leave tracker sheet? I have main menu to show all the balance used but got error when I link formula to the “Leaves this year”. Anybody can help? thx
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10869)
    
256.  Is there a way you can assign each employee a total number of leaves alloted through the year so the they can be deducted. For example, employee 1 gets 10 “leaves” a year and as she/he uses a vacation day/personal day then it gets deducted from the total number? thank you!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10863)
    
257.  Hi I need 2019 Leave tracker template
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10860)
    
    *   Just change 2019 in cell A2
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10870)
        
        *   So you’re saying that dates will fall on the same days in 2019?
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10910)
            
258.  The leave tracker sums W worked from home, it is quite cool idea to track this but it is not counted as holiday so how can I amend the sumproduct formula?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10847)
    
    *   I have the same question. I would like to track but do not want to count it as leave.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10893)
        
259.  I’d love to have a way to specify the working days for each employee. In my organization, we don’t all have the same workweek. That said, what a fantastic resource this tracker is (especially for nonprofits like us) — thank you!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10839)
    
260.  Wondering if it is possible to add another column next to Employee name. The additional column would be group/reporting manager.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10825)
    
261.  Hi Sumit,
    
    Excellent tracker, thank you so much. Would like to check if I can delete the leave codes as I do not need so many in my tracker.
    
    Your reply will be highly appreciated.
    
    Thank you!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10809)
    
262.  If I want to add more leave name and code can I do it? I tired doing it it works however when I put the code in tracker it wont give me the red color.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10801)
    
263.  Do you have a 2019 one yet? I tried changing the cells and it does not work. it will not add days of leave.  
    Thanks
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10771)
    
    *   2019 is working you just need to change the year A2 to 2019
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10802)
        
264.  Just wanted to ask for the 2019 template. I have tried changing the year but it did not work correctly.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10769)
    
265.  is there a way to log days worked in Lieu (eg. code L day worked in Lieu reduces the total days taken)? great spreadsheet by the way!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10752)
    
266.  Can you create a 2019 spreadsheet. Would like to be ready for the new year.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10749)
    
    *   explains above how to change to 2019 just edit the date then add the holidays
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10753)
        
        *   Hello I did change the date and edit the holidays but is does not change the leaves per year column. How do I change that?
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10770)
            
            *   you should only change 2018 to 2019 then it auto populates with the dates, the leaves per year auto populates when you add holidays, maybe you have lost some formatting, download and try with a fresh sheet
                
                [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10773)
                
267.  When I add in leave the cell does not fill with colour as you said it would. Why would this be?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10739)
    
268.  Hello. I would like to add one more half day as H3. how do I do that
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10735)
    
    *   Hi did you get any reply on this as I want to do something same.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10803)
        
        *   No I havent
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10804)
            
    *   Add another row, then you need to amend the conditional formatting.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10872)
        
269.  Can you please update for 2019? I like this spreadsheet but cannot seem to edit correctly for 2019.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10732)
    
270.  This is awesome!! Nice skills! I’ve tweaked the layout a little and added a team column next to the name column. I’ve adjusted to macros to show the first 2 columns (A&B) when the month skip arrow is pressed. The only thing I’m having an issue with is now January 1st is now the last entry on the calendar (NJ5 is Jan 1 every year, should now be in C5). This is clearly because I’ve added a column and its making reference to the wrong cell to start on, but not sure which of you formulas to adjust. Its not even an issue as all the dates are there but, my OCD in overdrive!! Please help…
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10718)
    
    *   hey do you know how to amend the formula so it excludes when summing the total holidays for the month and for the year please?
        
        thanks
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10848)
        
        *   Edit in conditional formating.
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10873)
            
271.  Pretty please for 2019!! Thank you!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10715)
    
272.  Can you fix your formula for “Week #”? You have it as a hidden row. It’s row 7. It won’t work since it references Sheet3 when of course there is no Sheet3.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10712)
    
    *   Sheet 3 is hidden, you can show it.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13137)
        
273.  Is there a way to log days where they may have only had to take off a couple hours?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10698)
    
274.  This is fantastic and has helped me so much with my employee’s leave. Can you please do one for 2019? pretty pretty please!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10648)
    
275.  I like the leave report but I need more information – Each one of my associates accumulates time/hours on their anniversary. I want the tracker to track time used as well as time remaining for the year. How can I do that without messing up the sheet?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10647)
    
276.  How to add columns without disturbing the formulas. need extra colum for department and id #.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10646)
    
277.  What if there is no set day off?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10645)
    
    *   In “working days table” select “yes” means all day is working.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10874)
        
278.  When an employee leaves and want to delete the row in the middle of the leave tracker spreadsheet. The leave tracker does not work when leave code is entered for other employees how do you delete the row??
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10633)
    
279.  Hi  
    If I want to see two months data together then what changes I should do in the file. like I want to see October’18 and November’18 at once on sheet.
    
    Please let me know what changes should I do in macro and date formula.
    
    It will be huge help.
    
    Regards  
    Sachin Sharma
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10630)
    
280.  Good day, i hope that there is some help that i need with the following problem, i have a sheet, kolom A has the name APG with all kind of codes.  
    and on row 1 starting from kolom B there are 30 cels with code AA AB AE enz. the problem is that i need an formula to get the result of the APG and the code AB or something like it to give as a result for example 50%, is this posible with a formula.  
    Hope that you are able to help me with this problem.  
    Best regards Teet.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10558)
    
281.  Hi hope you can help me, there’s an error on my leave registre it says ‘ unable to set the Hidden property of the range class” . What is this means?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10544)
    
282.  There’a alway an error “UNABLE TO SET THE HIDDEN PROPERTY OF THE RANGE CLASS”
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10543)
    
283.  Is there a way to delete some of the leave codes completely from the form? For example, I only need 4 codes, when I delete the extras I disturb majority of the form.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10493)
    
284.  So help full, but I cant add more column after the name, for gender or sth els. Please help!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10434)
    
285.  Dear all,
    
    first of all, thank you very much. the excel to count annual leave is very helpful.
    
    is it possible to insert an extra cell or column for starting date of each employee my leave, let say, 12 days per year, and “as of today”, how many days he or she is entitled? Then, there’ll be the balance of each staff.
    
    Also, just in case, use the financial year Apr 2018 to Mar 2019 instead of Jan 2018 to Dec 2018, will it be difficult to modify the excel?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10423)
    
286.  Hi, do you have a 2019 version?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10412)
    
287.  HI HALLO, IS IT POSSIBLE TO INSERT AN EXTRA COLUMN FOR STARTING DATE OF EMPLOYER MY LEAVE GOES FROM STARTING DATE TO ONE YEAR AFTER THAT.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10400)
    
288.  Hi Sumit, this tracker is very useful! I would like to know if there is anyway we can record in one day, an employee took 1/2 day annual leave and another 1/2 day unpaid leave?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10370)
    
289.  Thank you LOVE this!! Is there any way to get this to track hours down to 15 min. 1/4 of an hour? We do time in hours and down to 15 min. of Personal Time. Thank you again for this it is AWESOME!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10365)
    
290.  nice
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10355)
    
291.  Can I use this with Mac??
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10345)
    
292.  I love this tracker! Thank you so much for making my life easier during 2017 and 2018 🙂 Is there a chance for 2019 one?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10344)
    
293.  Great Job!  
    Can you please help me how to add additional columns to set Total annual leave for each employee and to display total leave taken and remaining for each employees.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10327)
    
294.  How do I add a column for employee ID left to name
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10292)
    
295.  This is a great tracker. How can you assign your own colors for each type of leave?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10275)
    
    *   Hey Lisa, You can do that using conditional formatting. Select the entire leave area section, go to Condition Formatting (in Home tab) and click on manage rules. There you can create your own rule
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10276)
        
        *   That worked…thank you!
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10277)
            
        *   So, I have to do this for each month? Is there a way to apply this once for all months/years?
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10280)
            
        *   Hello Sumit, I love this tracker but I need to use it to track points that my companies drivers get for certain driving violations. That being said, I was wondering if you could let me know how to change the values for the different codes? For example I would be changing Sick to Preventable accident and would need to change the 1 to a 2. Any help would be greatly appreciated!
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10899)
            
296.  How to change Saturday and Sunday holidays to Friday
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10273)
    
297.  Hi
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10272)
    
298.  hi. is it possible to exclude some leave type in the calculation of the leaves?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10269)
    
299.  How do you use the triangle icons next to the month names to go to the next/previous month? so that it shows you the selected month only and hides all the other months. can you plz share the method?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10260)
    
300.  Hi Sumit. The leave tracker is good. I have one query though. When I select Work from Home, it gets added as a leave in the “leaves this month” and “leaves this year” column. I don’t want it to be counted under the “Leaves this Month” and “Leaves this Year” column. How can I enter WFH without increasing the leave count?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10188)
    
301.  Awesome Work, Sumit. Thanks a lot for your great efforts… It helps!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10185)
    
302.  Hi, Many Thanks for the template. However, even though the boxes change color when I enter staff leave codes, there are no changes at all from column NJ to column NV. Please assist.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10186)
    
303.  Hey Sumit, you have done awesome work with this excel sheet. One request, if you can also break up monthly leaves instead of just giving total for the month would be very helpful. I tired playing with it with countif formula but once i change the month count of monthly leaves don’t change as columns gets changed for that month. Can you please email me if I am not asking too much. Thanks
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10189)
    
304.  Can you track the hours they took on the day they took the designated leave
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10191)
    
305.  hi, if an employee is already separated and supposedly not included let say in december..how do you arrange the employee column? thanks!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10193)
    
306.  Hi Sumit,  
    Thank you for sharing this spreadsheet. I am trying to add something that would show the number of PTO/Vacation/Leave days each individual employee had and then as they used them and they were inputted in the tracker, it would minus them from the individual employees “bank” of days. Can you please help?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10197)
    
307.  Is a 2019 version available?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10204)
    
308.  May i know how can we change the leave break up code for half days as well. If i want it to be reflected as .5 and not 1 in the leave break up of half day. Thank you
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10244)
    
309.  HI Sumit, thank you for this very helpful tracker.. Quick question, how to add more leave code?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10209)
    
310.  I can’t Find the working days and non-working days to change it
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10228)
    
311.  Is there a way to show each staff’s remaining holidays as well as holidays taken? Thanks
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10225)
    
312.  Hi, I’m not able to change the month by clicking the triangle icon.
    
    It says “The macro may not be available in this workbook or all macros may be disabled”
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10216)
    
313.  Hi, I’m not able to change the month by clicking the triangle icon.
    
    It says “The macro may not be available in this workbook or all macros may be disabled”
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10237)
    
314.  Hi Sir,  
    Your Leave Tracker templet design is wonderful If it possible for you, a humble request from my end please make a tutorial video on this.
    
    Thanks,  
    Rajib Das
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10226)
    
315.  Hi! First, your work is just great! Thank you that you share it, making my life easier 🙂 I have one question regarding the leve types. I would like to remove possibility of half day leave. When I do it however, the table becomes marked with gold (yellow). How can I get rid off those options (H1 and H2) and still keep the functionality of the table?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10229)
    
316.  Hello Summit,  
    Thank you for this excel sheet – I am trying to change the colors to the different leave codes, can you tell he how to do that?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10221)
    
317.  Thank you so much for this! Actually, our employees have different days off… Is there a way to reflect this?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10247)
    
318.  What should i do if individual staff a have a different off date? How do i indicate in the excel sheet?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10251)
    
319.  hello – thanks for this great spreadsheet. Is it possible to assign a different color to the different leave types.  
    thanks
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10108)
    
    *   Hey Tracey .. You can do that by changing the conditional formatting rules. In the current tracker I have kept only 2 colors – red for full day and yellow for halfday
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10123)
        
        *   Hey Sumit I need you help. in your summary of leave. It shows the total of leaves continued from previous months . for eg.  
            june I added Sicksheet 2 and annual leave 3 and while again going to enter in july month it gives the same total + adding the july sickksheet and annual leave.
            
            Isnt there anyway where it shows the summary for only july aug sept n so on..please do let me know.  
            If possible please reply me on my email.
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10464)
            
320.  Great tool!! Some of the holidays you have listed are not holidays for us. I deleted that row from the Holiday table but it did not change in the leave tracker. What am I doing wrong?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10107)
    
    *   Hey Michelle.. instead of deleting the row, simply delete the data and enter the one you want to be considered as a holiday.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10124)
        
321.  can you make one for shift workers, 7 working days and 2 off then 7 working days and 2 off then 7 working days and 3 off
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10100)
    
322.  Hi Sumit, I love your template thank you!! Question though, I need to add another category, Leave upcoming approved. Are you able to assist in how I would add this and the formula I need to use? Thanks Faye
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10093)
    
323.  Hello, is there a way to copy this sheet multiple times? I tried to do this to separate groups of people to track, and the month arrows give me an error when I try to change it. the debug highlighted this:  
    “LeaveTracker.Range(Columns(Range(“A3”).Value \* 31 – 29), Columns(Range(“A3″).Value \* 31 + 1)).Hidden = False”  
    I’m not sure why it wont work, the first sheet works just fine.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10092)
    
    *   I’m having the exact same issue. Were you able to find a solution?
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11019)
        
324.  This is awesome Sumit! Is there a way to break up the holidays between off-shore and on-shore?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10089)
    
325.  Hi, there is possible to add multiple Holidays for 2 or more different country??
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10088)
    
326.  Only my Sunday is highlighted in Grey, How can I get back the Saturday one? I used last years and made the changes to the year as discussed above
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10087)
    
327.  Hi, My team members are located in some different countries. Is it possible to add Location , and according to the location – National Holidays, and accociate the location to a team member?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10085)
    
328.  Hi, first I want to say how handy and easy and amazing this leave tracker is; however when I shared it with my boss via excel online it does not allow you to click to the next month. Why?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10079)
    
329.  can’t upload onto google drive coz of the macros…
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10076)
    
330.  Where can I put the monthly leave. For ex. 1.7 days per month, as well as the leave brought forward from previous months?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10071)
    
331.  It would be nice to be able to have different colours for different leave. i.e Sick Leave red with white text, Vacation Leave green with white text so you can easily see what leave is taken
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10070)
    
332.  Great template – amazing what Excel can do. There seems to be a typo in the formula for Leaves this Year – the IF statement is checking if H1 or H2 are used for calculating 1/2 days, but the second part of the formula repeats $NX$16 instead of $NX$17. For some reason, any change I make to a formula results in a #VALUE error and not sure why.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10069)
    
    *   I’m having exactly the same issue. Need to include a H2 value and it’s subtotalling correctly in the leave for that month but not for the year total. Anybody have any suggestions please?
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10072)
        
333.  How will I add additional column for the name/
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10068)
    
334.  Hi Sumit. great thank you.  
    Could you please add the following.  
    I need to be alerted if there is an employee who took more than 2 leave days in a 8 week cycle. And if an employee takes more than 1 consecutive leave days.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10067)
    
335.  Can I delete every code but vacation days? we do not need it broken up. Also, how do I go about putting our company header on it?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10066)
    
336.  Hi! Thanks so much for this template. It works very well. I was wondering though if it would be possible to customise the ‘weekend’ days for each employee, as where I work we take different days off. Or maybe you could give me some tips on how to do that. 🙂
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10065)
    
337.  this is a great template
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10064)
    
338.  hello. i have altered the holiday list,but i cant get the automatic change in color on the tracker
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10063)
    
339.  this is great.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10061)
    
340.  Is there a way to track hours instead of whole days or half days…. for example we had an employee leave to bring his child to the doctor and was gone for two hours.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10056)
    
341.  @ Sumit Bansal :  
    Hi, I found this tracker very helpful and easy to handle in the single sheet for various months. I was trying to change the leave categories and add new one as some are not applicable in my working context. Could you please help me in getting to know how to change the categories/Delete Categories. my email id [anoopjuesi@gmail.com](mailto:anoopjuesi@gmail.com)
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10055)
    
342.  This spreadsheet is great! How do I change the colours of the different types of leave please? I need to be able to see standard vacation leave in a different colour to compassionate leave, paternity leave, etc.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10054)
    
343.  Very nice template Sumit, thank you!  
    Is there an easy way to modify the template to show 2 or more month at the same time? I would like to use it to log vacation that usually span either jul-aug or dec-jan.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10053)
    
344.  Hello,  
    I only need certain leave name, code, and leave breakup information. Once I delete certain columns and information, the dates are automatically filled. Please assist.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10047)
    
345.  Hello,  
    I have employee working different days of the week, how I allocate the working days to each employee, thank you
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10046)
    
346.  hELLO,
    
    How I add new employee/
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10045)
    
347.  Excellent sheet… one question… is it possible to insert leave by the hour… we allow staff to take single or multiple hours of leave that do not necessarily fall under the bracket of a half or full day. Was wondering if this sheet could be edited to incorporate this.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10043)
    
348.  Hi This is a great software but I’m having trouble with the month scroll arrows. When I start at January, 2018, and click the orange arrow next to January to go to February, there is only a blank page with the columns and rows but no info in them. I had already done a couple of people in January and wanted to see February. So I filled in the columns for February then went back to January and the names are there but the columns are empty but the days off that I filled in are there.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10041)
    
349.  hi i have a question how did you link those arrows to the next month ive tried everything. please help btw very inspiring template well done
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10038)
    
    *   Hi Steven:
        
        DId you ever figure out how to go to the next month? I’m still having problems with those scroll arrows. Thanks  
        Melody
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10081)
        
350.  Hi Summit, in my case I have to select different weekly off days for each employee. How to execute it.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10037)
    
351.  That somebody can do this and leave it for us for free is quite very commendable.
    
    Whao! May God bless you real good.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10035)
    
352.  Thanks ,very good nice Excel Leave Tracker Template
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10032)
    
353.  Amazing ~ Thank you very much.  
    Could I insert more row for over 50 employees like 130? I am try to insert the employees code and number column before employees name. But the sheet does not work. How can I fix it?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10031)
    
354.  Hello, Well done for the planner. Is it possible to deduct two days for a Public holiday instead?  
    Thanks
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10030)
    
355.  Was wondering if there is a way to enter a code for unpaid leave days that would allow for there to still be a count of paid leave days used/left
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10027)
    
356.  i would really like the spreadsheet for Excel vacation tracker. I would like to have a sheet with 50 plus employee and one that i can copy and paste to another sheet within the same workbook. We have 3 shifts with different departments. I would like to set this up so that each department in on a different tab.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10025)
    
357.  can i copy and paste the vacation tracker to another spreadsheet within the same workbook?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10024)
    
358.  I tried removing some of the unwanted leave codes.. it changes the cell color. Also, I don’t want Work from Home to be marked as red…please help
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10020)
    
359.  Its really helpful thanx, my issue is a little different although. Can we set a limit for the no. of leaves that each employee can avail for eg: Annual Leaves should be less than or equal to 15 and also that the no. of leaves available to each employee can be set differently as per their allotted leaves.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10018)
    
360.  Hi Sumit,  
    I enjoyed using 2017 tracker. Will you be going to release 2018 tracker soon?  
    Thanks,
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10004)
    
361.  Hi, is there a way to set it to keep track of hours taken and not days? I believe right now it is set to days only.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10003)
    
362.  How to use Use the triangle icons next to the month name to move to the next/previous month (the template updates itself to show the dates for the selected month). There is a short VBA code that runs in the background whenever you change the month. It shows you the selected month only and hides all the other months.
    
    Let me know how to select it.  
    .
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9996)
    
363.  Hi. Need to add “P” (Number of days present) to the list which needs to be highlighted in green. How to do it?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9985)
    
364.  How to add another column without affecting the other column? Is that possible
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9978)
    
365.  When you be releasing 2018 Vacation Tracker?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9977)
    
366.  Hi Sumit,  
    First of all a big thanks to you. Great work Dude !!
    
    I need to include “Comp-Off” in my leave type which should not be considered as leave. Please let me know if there is a way to accomplish that?
    
    Thanks in advance
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9973)
    
367.  Hi Sumit! Thanks so much for this! I was trying to add two identifier columns in addition to employee name but i was unable to do so without making the sheet incorrect. Could you please inform me how to complete this?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9972)
    
368.  Hey , the zip file does not have any excel,pls help
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9969)
    
369.  Great work Sumit! If an employee takes a 1/2 day sick how do I get it to reflect on the sheet as a half day sick?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9963)
    
    *   Also if I have to keep track of historical data e.g. 2017-2020, would I be required to develop a new sheet for each year?
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9964)
        
370.  Hi Sumit, So glad to see this really i was in need of this.Thank you so much. Please teach me more because want to learn more from you.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9962)
    
371.  Hello, I downloaded this template and it come in a zip folder. And I do not see any xl sheet there. Can you please guide me ? Thank you
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9961)
    
372.  I downloaded the zip file… how do I open the template?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9956)
    
373.  Hi Do you have template for 70 people
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9948)
    
374.  Hi Sumit, I’d like to add 2 more rows from A sections, please advise how do i do that? 🙂
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9940)
    
375.  Hello. This is awesome. But how can I make it for atleast 100 people?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9939)
    
376.  Hi Summit is it possible to add Summary Sheet for easy checking of Employee? and showing Employee and all the date of the leaves they taken for whole year?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9936)
    
377.  when can you update the leave tracker template for 2018 🙂
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9931)
    
378.  Hi Sumit. Thanks a lot for sharing this Leave Tracker. Really good. Please how can I move the Scroll Bar from the bottom of the sheet to the top? Thanks. Abraham
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9928)
    
379.  Hi Sumit, I need your help on this. How can I change the colour of the leave record for employees? and am I able to create A1 to select for different department? Please assist me on this. Many Thanks
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9910)
    
380.  This there any way to return the dates from which the S,C,V,H,M (types) are applied to the calendar, and output them to a cell via I’m guessing what would need to be an INDEX by type?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9906)
    
381.  Hi – I have downloaded the zip and did the extraction. I am not seeing the executable file to launch the spreadsheet. I’m not sure if I’m doing something wrong, so would appreciate help in opening the spreadsheet. Thank you!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9905)
    
    *   Hey Brenda.. You can download the leave tracker now and it will be saved as an Excel file (not a zip).
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9992)
        
        *   hey Sumit need your help in doing AHT and other call center Dashboard .
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9993)
            
        *   Sumit, I made tons of changes in December to prepare for 2018….and just saw your revised version… 🙂  
            I just want to add more half days – the new version has 2 half days and I tried adding other codes but counldn’t get them to count as 1/2 day. How is that done?
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10021)
            
382.  Hi I love this spreadsheet thank you for sharing. Is there a possibility of editing the employee’s? So say we have some employees who work full time and part time. So It calculates the leave of their individual hours?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9904)
    
383.  The VBA for the scroll bar needs an edit but I can’t determine what that is…when clicking on the right arrow of the scroll bar it jumps from February to December.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9900)
    
384.  Hi- Is there a way to change the highlighted colour for leave code? Process is for the TL to enter the leave type, and then once confirmed in Pulse update that particular leave to another colour – this will help to track any non updated leave for Payroll purposes.  
    Thanks in advance!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9899)
    
385.  Trying to leave a blank column before A1 but it seem not working. How can I insert an addition column without affecting the formula?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9895)
    
386.  can i add another leave type for which it counts it as 0.5 day like it does for half day??  
    i want to bifurcate planned half day and unplanned half day.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9888)
    
387.  Hi Sumit, thank you for the amazing piece of work.. i want to have a link of updates sheet .. which include summary of the leaves as well as employee ID and position.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9874)
    
    *   Also whenever i try to create a copy it always show error of Debug .. s
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9875)
        
388.  This is the best format out there for leave trackers, as it deals with the whole team not just individual employees. But I’m running into 2 issues. (1) I change the number in A1 and use the scroll bar to switch months. But while it’s in one month, say November, and I click on the right arrow on the scroll bar, it doesn’t go to Dec. It’ll go straight to Feb of the next year or some other random month. It skips, it never just goes to next month. (2) I want to add more employees. So I copy the data and formulas and insert a new row. Everything works, formula-wise, but then now the scroll bar is covering the bottom most row, since the scroll bar doesn’t move even if you add rows.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9867)
    
389.  can anyone guide me how to calculate the leave balance, considering leave balance is different every year  
    Mr. ABC joined 01 Jan 2014- what should be his leave entitlement until December 2018  
    everyone is entitled for a leave balance as per below  
    2014 – 34 days  
    2015 – 34 days  
    2016 – 30 days  
    until 08 July 2017- 30 days  
    after 9 July 2017 – 34 days  
    2018 – 34 days
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9865)
    
    *   same worry for me .. how to calculate the leave balances with reference to the joining date
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9876)
        
390.  Hi,
    
    Is there any way I can add additional sheets as tabs at the bottom of the spread sheet? When i try copy the tab and use the scroll bar i receive a run time error 🙁
    
    Brilliant other than this Sumit… top marks sir!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9864)
    
391.  Hiya, This is great, would you be able to release a 2018 version please?
    
    Thanks!
    
    Emily
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9860)
    
392.  the file only downloads as a XML am I doing something wrong? I’ve also tried your direct link
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9849)
    
393.  Hi Sumit – I desperately need to use the leave tracker but we track based on anniversary date rather than calendar year. Can the Tracker be tweaked to accommodate me? Thanks! This tracker is the best on the internet!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9841)
    
394.  Hi Sumit, is there anyway to make this template based on a bi-weekly (2weeks) schedule? With teh first bi-week defined by the template user?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9821)
    
395.  Hi, maybe a silly question but where must I download it too for it to work? It looks great
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9816)
    
396.  HI. Please assist.. I am not to sure how to create a leave cycle on the leave tracking template you created  
    [admin1@cloetetransport.co.za](mailto:admin1@cloetetransport.co.za)
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9813)
    
397.  Hello, is there a way to change the color? i mean, i would like it to be green instead of red, how could be it done? Thanks
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9812)
    
398.  I just downloaded the tracker, but not able to find how to open the xls, where it’s located in the downloaded folder
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9801)
    
399.  your holiday tracker is excellent with one issue. the scroll bar doesnt work and doesnt advance by a month, it just goes to the end of the year. I cannot see a fix for this. Do you have any suggestions?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9793)
    
400.  Hi Sumit, How to change the year..im looking for 2018 version
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9787)
    
    *   Hey Siti, you can change the value in cell A2 to change the year. Note that if you already have one for 2017, you need to create a copy, delete all leave already marked in the tracker, and change the value in cell A2 to 2018.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9788)
        
        *   OK.. another matter for me is how i can add listing for the leave break up? because we have half day unpaid leave and half day for annual leave
            
            btw, thank you so much for sharing this excel leave tracker..
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9789)
            
401.  can i mark time also if employee leaves early in the same sheet?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9783)
    
402.  hello, thank you as this is a very very fantastic template,i am wondering how do I add more employees as I have 160 employees. it would be great if you can advise me how to do that.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9776)
    
403.  I love this template. I’m not good at Excel, but this doesn’t require me to be. How would I change the casual leave, which we don’t use, to something that we do use, comp time? I would love to have this box allow me to put in, for example, C2, which would equal two hours of comp time and have that reflected in the month and year totals. I figure the values would be based on .125 per hour, i.e. C8 would equal 1 day. Is this possible? I already added columns for the fluctuation in comp time off to the right and did a sum formula for the columns to reflect adding and subtracting comp hours. It would just be nice to look back on the month and see how much and when comp time was taken. As of now though if I put anything in a day box it equals one and I have to go back and change the total, which really doesn’t work because the template is not set up for three decimals and it rounds up.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9773)
    
404.  I have employees with different days off on a regular basis, how can it be customized for each employees days off? When I try to change each days off, it is applied to all employees. We work shift works and have schedule through the week with employees having different days off. thank you
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9768)
    
405.  Hi Mr. Sumit, awesome work, I just stuck with one, you didn’t add Time off In Lieu (TOIL) here
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9759)
    
406.  Dear Sumit whenever i add new rows the scroll down bar comes in the middle of the sheet please tell me the solution for it so that can manage the template accordingly. and by the way uve done an awsome job. kindly do reply its very urgent
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9731)
    
    *   First right click and drag the scroll bar down and then keep adding the rows
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9879)
        
407.  Hi Sumit,  
    I love this tracker, I was wondering if its possible to add .25 hours to it?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9721)
    
408.  how to add another row of employee.. our employee are more then 10
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9709)
    
409.  Hello, no matter how many times I’ve tried, the zip file doesn’t open to an excel spreadsheet. I do get a variety of folders but couldn’t find a spreadsheet within it. Is there a different way of downloading and accessing this template?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9703)
    
    *   Hello Dana, Try this drop link: [https://www.dropbox.com/s/omkx619gctco0ot/Excel-Leave-Tracker-2017%20%284%29.xlsm?dl=0](https://www.dropbox.com/s/omkx619gctco0ot/Excel-Leave-Tracker-2017%20%284%29.xlsm?dl=0)
        
        You can download the file using the Download button at the top-right.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9704)
        
        *   [https://uploads.disquscdn.com/images/3686c879d37abd0e2e14a266ec3df44b559735bbef8a1168c123c50c4a4296ad.jpg](https://uploads.disquscdn.com/images/3686c879d37abd0e2e14a266ec3df44b559735bbef8a1168c123c50c4a4296ad.jpg)
             Thank you. That worked. Can you help me with how I can alter the formula for the total days off per month/year to reflect half day? I have written down the codes “M” and “A” for either a morning half day or afternoon day. I’d like for both to reflect 0.5 in the totals
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9705)
            
            *   Hi there, may I know how do you change the colour of the leave record and how to you add more column into the leave record? please assist me. Thank you.
                
                [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9911)
                
410.  This is really great! Thanks Sumit!  
    I have one question, how can I add a field after the Employee Name? I’d like to add more like ID, Team, etc. Thank you!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9695)
    
411.  Hi I’m downloading the file but there’s no excel file? Is this still available?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9663)
    
    *   I had the same problem. I was using Microsoft Edge. Use Google Chrome and it should download the excel file instead of a zip folder that Edge did.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9697)
        
412.  hi , this leave template is so amazing.  
    can we add training leave without adding to the total in leave column?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9655)
    
    *   Hey Serena.. You can use a code for training leaves (for example, replace C with T) and the leave breakup section will show the total for that leave code for all months.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9680)
        
        *   Thanks Sumit. I tried to do that but it’s adding up to the leave total. How to exclude the training leaves from the total ?
            
            Thanks a lot. Love your templates  
            Sereba
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9687)
            
            *   Hey Serena.. The easiest way would be to use a separate column (may be column NQ) and subtract the training leaves from total leaves.
                
                [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9688)
                
                *   Oh i tried to do that too on Column NJ and NK to subtract the training leaves but maybe i did it wrongly, its not getting a value after that
                    
                *   Did you try and do this column NJ or NK? If yes, it wouldn’t work as it will break the formulas in it. You can do this in a separate column that doesn’t have any formula in it. For example column NT or NU
                    
                *   oh ok thanks. I got what you mean but then it will stay put when i change the month, Hem its ok then thanks. i figure out something else.
                    
        *   Hi Sumit,  
            I tried deleting few leave codes but after that I do not see the color code. Please advise.
            
            Regards,  
            Vijeta
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11189)
            
413.  Hi this is amazing. i love it. im just trying to add to the leave training days without having to add to the total number of leaves. is that possible?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9654)
    
414.  Hello Sumit!
    
    First of all, thanks for the awesome excel spreadsheet! It is definitely efficient, clean, and pretty easy to use.
    
    I’ve added some changes to the excel, I’ve added additional years since we’re halfway into 2017 and modify some of the codes to be in alignment with our policy. With that being said, the modifications took place, I’ve crossed path with issues with the additional years.
    
    As I was scrolling through next year 2018, the excel spreadsheet did not clear all data from the current year. What codes that was already plugged in this current year carried over to 2018. How can I go about clearing the codes for next calendar year?
    
    Also, I would like to update the Holidays page for the year of 2018. How can I go about updating next years holidays chart and so forth? If I am able to update the holidays sheet, will the holidays carry over in the leave tracker sheet for the year of 2018?
    
    Thanks a bunch!!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9642)
    
415.  Thanks a lot for this template. I have one question: How can I count friday as half day?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9621)
    
416.  Splendid work Sumit !!  
    I want to add one more column as “comp-off” in Leave break up as well as in absence code mentioning comp-off as “Comp”. But the thing is Comp-off code should not get calculated or added to Leaves This Month and Leaves This Year but should get calculated or added only in Leave Break up.  
    Please let me know how to do this ?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9614)
    
417.  I cannot run macros due to restrictions in work area. How can i use this template without macros
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9613)
    
418.  Hi, I would like to add more Employees however please can someone help as to how you move the scroll bar down in the document once employees are add?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9612)
    
419.  Thanks Sumit for the tracker, however the half day leave is not summed up with the corresponding types of leave like Vacation or Sick. For example since half day is not a separate types of leave but if I need mark half day vacation or sick leave it should be summed up with vacation or Sick leave instead of separate H list.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9610)
    
420.  When you create the leave tracker for 2018, can you add a column after the employee name. I’d like to add information for each employees without having to scroll all the way to the right of the spreadsheet. Thank you
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9608)
    
421.  How can you change the scroll bar to advance by one month?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9607)
    
422.  superb!! Thanks 🙂
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9591)
    
423.  I love this tracker so much; well done — thank you for the share! We use all time off (sick, personal, vacation, etc.) as PTO (Paid Time Off) which is accrued on bi-monthly pay periods (26 per year). Do you have any spreadsheets to calculate accrual PTO for salaried and non-salaried employees?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9585)
    
424.  Hi Sumit. Love this template. I was wondering if you could explain how you set up H/h to equal .5 and all other values to equal 1. I was hoping to adjust this leave tracker to focus only on one type of leave, and then break it down by the amount of time, in quarters of hour, taken in one day: W=1.0, H=0.5, Q=0.25, HQ=0.75…  
    Not sure if that’s possible. Any thoughts?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9567)
    
425.  Hello Sumit,
    
    Can you add three more columns on the right like Back Up Resource, Approved By Client and other? I need that for 30 employees
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9559)
    
426.  hi, can i use this template of year 2017 & 2018 in one sheet?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9556)
    
427.  Is there a way to add a second half day or change one of the existing days to a half day as well?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9539)
    
428.  What if I want to deduct the half day from the available leave types (EL,CL or SL)?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9538)
    
429.  Hi.. the leave tracker is one time saving workbook specially for the startups. Thank you for this creation. But I am facing an issue with the sheet. When I mark half day for an employee the leave breakup counts it as 1 and not as 0.5. Please help me in resolving this.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9536)
    
430.  Hi Sumit!
    
    I am trying to add Employee ID & Location in the beginning of the sheet but I am not able to move the formulas. Is there a way to fix this please?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9512)
    
431.  I really like this tracker, but would like to do some customizations. The first one is a bit of color coding. Right now a half day shows up as yellow & all other absences are red. I am hoping that I can custom color it to have vacation days as green. Can you tell me how to do this?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9500)
    
432.  Hi  
    On all saturdays my employees work half day. Is there a logic that I can input such that if i put in unpaid leave/urgent leave, it will become 0.5?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9483)
    
433.  Hi, I have just downloaded this template. It’s fantastic, but i’m not sure if it will work for me. At my organisation we all work different hours, so our leave entitlement is recorded as hours and not days. I am no good with formula’s or VBA’s. Does anyone know how I change the formula from daily annual leave to hours? Any help would be appreciated. Thanks
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9476)
    
434.  hello Summit, thanks a lot for this template. saved my day. keep up with the good job.  
    is it possible to move the scroll bar down to add more employees on the list?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9463)
    
435.  Hi. I am using the 50+Employee excel and its great!  
    But I need to add 200 names….so I though copy and paste formulas down……however the scroll bar starts doing weird things. Instead of scrolling per month on the right, it scroll all the way to the end of the year on one click.  
    I looked at the VBA code and couldn’t figure out why it is doing this….
    
    Any ideas?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9423)
    
436.  once download it was a zip file.. how to use?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9408)
    
437.  hello sumit thanks for this file, i’m getting error when i select 1st month it is displaying as march 2017….what may be the error. can you please help me the get this resolved. thanks in advance
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9403)
    
438.  Hello, I am unable to unzip the file, does it still work? thanks!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9402)
    
439.  Hi Sumit, is there a way to add two half days one for vacation and one for sick day?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9391)
    
440.  This seems to work great. My company CEO uses it. I have a question/problem though. After he has entered 12 months of data, is there any way to add months, or do you have to start a fresh, blank template? He would like to have a continuous, single spreadsheet that keeps adding months to the end, or has 60 months or more. Otherwise, when a new sheet is created, the previous few months of data will be on a different sheet.  
    In other words, is there any way to have a sheet which was started in May of 2016 have data through December of 2018 or longer?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9380)
    
441.  Dear Mr. Sumit Bansal  
    Thank you very much. This template is useful and simplified. I’ve solved all the problems.again thank you very much i really appreciate .
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9378)
    
442.  Hi Sumit,
    
    This is a great spreadsheet, thanks for sharing.
    
    I’m trying to adapt it to use it to track all hours worked by my employees for the month, quarter, and year.
    
    So in each day on the calendar, I enter the hours worked by the employee. Can you advise how I can create columns that total the hours worked for the current month, current quarter, and the entire year? I’m trying to learn how you set up your {sumproduct:offset} forumula, but don’t quite understand them as of yet.
    
    Thanks again,  
    Shawn
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9373)
    
443.  Is it possible to calculate monthly absent and present in this template?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9371)
    
    *   hey Yogesh, did you find the way to do this?
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10184)
        
444.  Hi Sumit, Thanks for the template. However, I am unable to open the worksheet. Its downloads a zip file in all kinds of xml and other formats which are not accessible. can this be shared on email – [sjaveed85@gmail.com](mailto:sjaveed85@gmail.com)
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9364)
    
445.  Hi Sumit thanks for the great work. I am trying to add more employees in the list but the scroll button is not moving down when I am trying to add more rows can you help me on this please.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9363)
    
    *   Hey, where you able to access the excel file?  
        I am not able to. can you please share it with me – [sjaveed85@gmail.com](mailto:sjaveed85@gmail.com)
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9365)
        
446.  HI SUmit,
    
    I would like to add to column with repsect to leave breakup like “L” for Late and “P” for permission. But I do not want to add this in Leaves this month and Leaves this Year column
    
    How do I proceed for this
    
    Regards  
    Visu.V
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9345)
    
447.  Thanks a lot
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9341)
    
448.  This is a total useful …. Thanks
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9340)
    
449.  Hi Sumit, I tried, the months are not changing properly and once i try switiching from Jan to Feb the leaves entered are wiped out or stay there.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9336)
    
450.  Hi Sumit, I just downloaded. I am not sure how to get to the template. I see al XML files. Could you assist please. Do I need to open those XML files with any application?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9334)
    
451.  I need to add additional leave codes, both full day and half day. Can you send instructions? My email is [suzettemarino1@gmail.com](mailto:suzettemarino1@gmail.com)
    .
    
    Thanks for the help!!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9328)
    
452.  Excellent program and I use it regularly. However, can I have it amended to not subtract Sick, Personal Days etc. I just need to add these days, not subtract from any other entitlements. Since our company has no benefits, I use sick days/personal days as 1 day and I need to add these up through out the year….Thanks. John
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9306)
    
453.  Wow… what a great post! That helped me a lot. I would like to share with you a great service to fill a form online. If you ever need to fill out a form, here is `https://goo.gl/76rzxp`
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9303)
    
454.  Hi Sumit  
    I have added an overview sheet that uses a drop down to select the employee and then show the annual leave.  
    Not as colourful as your original so far. Thanks for the template. Column AI is the starting point for each month assuming no changes have been made to layout.  
    [https://uploads.disquscdn.com/images/b1929dd3a6c1ffec104313a6a44e7d23172692086e11dbb6ce0de8a5abaaab8a.png](https://uploads.disquscdn.com/images/b1929dd3a6c1ffec104313a6a44e7d23172692086e11dbb6ce0de8a5abaaab8a.png)
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9292)
    
    *   Hi Paul, can you share this spreadsheet you made? I would like to use it
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10200)
        
    *   Cool! Thanks for sharing!
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11322)
        
455.  I like this tracker, but how do add time to it. It only goes to March 2018?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9280)
    
456.  could you please do a tutorial of this leave tracker
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9272)
    
457.  I have 80 employees to be added but not able to add employees in the sheet.If I insert new Rows then all formula gets disturbed. Please suggest me how Can I add new employees?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9182)
    
458.  I download the sheet and start working, but i move to the next month all the leave history in the previous month are shown, and pop macro may not be available in the w.b or all macros may be disabled.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9181)
    
459.  Hi, thanks for this amazing template.  
    However, can the same template be used as a year calendar, where I can have a year overview of absences.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9179)
    
460.  Hello sir, this is very useful template for me. i would like to know how did you do the scroll bar. it scrolls the column labels with it. could you please do a tutorial of it?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9173)
    
461.  Hey, I tried using the excel in office online through sharepoint, but seems the scroll bar to change the months is not working at all. Could you kindly assist how the scroll bar can be enabled in the online version so that your excel sheet can be used. Its very urgent, would appreciate if you could respond asap. Thanks
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9159)
    
462.  This tracker is great. Except for one thing. I updated the list of holidays, but some of them are not highlighted orange for some reason. Anybody knows why? How can it be fixed?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9157)
    
463.  When I want to add different employees in other month the employee also delete from first moth what is the solution? can anyone help.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9152)
    
464.  This is awesome!
    
    How can I move the scroll bar down if I insert additional rows?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9138)
    
    *   right click on scroll bar and then cut , past where you want.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9150)
        
465.  I really like this Leave Tracker, but have one question about it. Is there a way to add a couple more columns next to the “Name” column?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9129)
    
    *   You can add column after NQ not anywhere else
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9151)
        
466.  Hello Sumit, Thanks for your template it is great , can you please help me how to add additional column fjor ID and position in template 2017 I could not use the template you added additional column in version  
    2016.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9121)
    
467.  Hello Sumit, thanks for your template it is great 🙂  
    Can you please help me how to add additional column for ID and position in template of 2017 I could not use the template you added for 2016 ?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9120)
    
468.  When I click on the scroll bar; it says; “Run Time Error: 1004 – Application defined or object define error”
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9117)
    
469.  Need help.  
    I download the zip file, but unsure of how to set up the file in excel.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9103)
    
    *   Hi  
        I had the same issue, rename the .ZIP file extension to .XLSM and the file will open in Excel.  
        HTH
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9110)
        
        *   Thanks!  
            I will make the name change.
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9115)
            
470.  Hi Sumit,
    
    Would it be possible to add extra columns next to name, such as team,…?  
    Because every time I add a column, the first day of the month January disapears
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9094)
    
    *   ı have same ıssue can anyone help?
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9123)
        
471.  HI Sumit  
    I can download the 2016 version fine and runs in Excel.  
    However Excel-leave-tracker-2017.zip when extracted produces several folders with XML content and not an Excel workbook .XLSM.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9091)
    
472.  I’m probably being really dim but I downloaded and unzipped the file but cannot find an excel spreadsheet to open?  
    Which file in what directory opens the tracker?  
    [pete@computertechnix.co.uk](mailto:pete@computertechnix.co.uk)
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8990)
    
473.  Hi, I am in need of an excel sheet which can record attendance with exact time of login and log out automatically. When the employee opens this excel sheet he/she shouldn’t be entering anything. Excel should record the time of login and cannot be changed in any case. Should have a button, when pressed excel should record the log out time. This will show how much time has he/she worked. No manual intervention.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8889)
    
474.  Thanks for sharing this. It’s very helpful. I wonder if you would be able to customize some parts of it for me. Some of my staff have weekends as work days. How do I make weekends work days for selected staff. Also, some staff have some public holidays as work days. How can I make some public holidays work days for selected staff? I’m happy to pay for customization to achieve these outcomes.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8828)
    
475.  This is the most important thing i have so far got from the internet this year
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8778)
    
476.  Thanks for the template!!! If we also want to track WFH (Work from Home) count of employees, how should we do it? It should not add up to holidays, but should have two similar columns to WFH per month and per year. Can you please update it to track WFH also?  
    Thanks in advance!!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8770)
    
477.  The Leave Tracker is awesome. I need to track 2017,2018,2019 and so on in one excel sheet.  
    When i copy worksheet from one to another the scroll bar doesnot work. Please help
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8759)
    
478.  Hi, this is an absolutely amazing tool but I have one question for the 2017 version. When I downloaded it and opened on my desktop everything worked perfectly. But when I wanted to open it in my drive google docs it started to change the dates – now January 2017 is not starting with day 01 (Sunday) but starts on 31st (Sunday) and the month of January does not end with 31st Tuesday as it should, but Tuesday 30. Does anybody has an idea why?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8749)
    
    *   You need to set the starting month from the A1 cell for once and use the scroll bar to change the months. If you change the months from A1 cell the dates would be mapped randomly to show some different value but exact.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9162)
        
479.  hi there. This is going to sound a little weird, but what program does this use and what file do I open? I downloaded the above and tried to open it in Excel but nothing…. please help?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8747)
    
    *   I have the same issue. Please advise!
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8779)
        
480.  @sumitbansal23:disqus ,  
    First let me say thank you for this awesome template, I am having a little bit of trouble getting it or any other schedule to accomplish what is needed and would love to talk to you about it and see if you can help.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8744)
    
481.  Hi, in the our office set up, people instead of getting paid double for working on holidays, they earn an extra VL that they can use for some other day. How do I incorporate this? Awesome template btw, thanks!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8737)
    
482.  This is awesome! Do you plan on doing a Google Sheets version?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8725)
    
483.  Hello Sumit,
    
    Your Leave Tracker is amazing, and I am trying my best to use it. However, I will like to upload it on Google Sheets so that I can share it with my entire team, but I do not want them to be able to make changes, just to view the sheet. Anytime I upload it, it changes the last day of the month to the first day, is there anything you can do to help. This is going to be a life saver for me if this works. Thanks a lot and I do hope to hear from you soon.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8724)
    
484.  Hello Sumit, It is a very nice excel sheet which you have prepared & completely puts me at ease. I just wanted know from you how to add shift details. My team works in 24\*5 form hence I am require to collect their login details. How can I create a LIST to record the same & then use other codes highlighting leaves.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8719)
    
485.  HI Sumith- Is there a 2017 version for this?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8716)
    
486.  Hi Sumit! Please help me remove the 0.5 value and make it to 1. How do I do that? Thank you so much.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8693)
    
487.  Our holidays are February to end January .. how can I amend the dates for the year
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8688)
    
488.  Thank you. It is really helpful. I just have 1 questtion.  
    If I don’t want to count U, M as 1 in “Leaves this year” column, what should I do?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8678)
    
489.  Tracker is good, but i am facing some issues. For example if i enter two days as vacation for the month on January and i change the month from the dropdown on the left hand corner then the vacation days which i entered in the month of January are reflecting in other months too. Also if i click the scroll bar, it is taking to the end of the month for the year instead of the next month.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8673)
    
490.  This is really is a brilliant template, thank you,  
    I have added additional “leave codes”. Some of these additional “leave codes” I would like to have counted as 0.5, however, they are all being counted as 1.0. How do I change that?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8664)
    
491.  Thanks for sharing however the issue with tracker is that if you fill in one of the cell for any leave type, then the cell remains filled even if you change the month. Ideally, the data from the cell should remain restricted to that month only.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8663)
    
492.  This spreadsheet is great however when I tried plotting the leaves for January, the leaves for that month still shows up on the rest of the months. If you delete the code, it will remove everything. How do you fix this?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8648)
    
    *   As per sumit, you need to use the scroll bar for changing the months 🙂
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8651)
        
        *   But using the scroll bar, the month is not changing to the immediate next month. Instead it is taking to the last month of the year and some times to the middle month of the year
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8674)
            
493.  Is it possible to change one of the other categories, for example the Personal Day to a 0.5 day as well?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8644)
    
494.  Hi Sumit,
    
    Hope that you have a template for this for Google Docs 🙂
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8637)
    
495.  Awesome leave tracker, thank you. How can I add in columns to reflect the employee surname, employee code, and job description please?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8633)
    
496.  This tracker is exactly what I’ve been looking for! Question though, I’ve updated the year to 2017, but the days of the week don’t match up properly. How do I update the day of the week row to be accurate?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8622)
    
497.  Hi! The leave tracker is extremely helpful. Just a small question. I want to upload it as Google Spreadsheet and share it with the management. However, when I upload it, the scroll bar doesnt show in Google Spreadsheet. Any suggestions on how to do it? Thanks.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8621)
    
    *   Same problem here 🙂 As per Sumit, he’s currently working on another file for Google Spreadsheet
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8636)
        
498.  Hi Sumit,  
    Would it be possible to amend the tracker so it was date specific, eg if a worker started working on the 20th of the month, the tracker would then show 12 months based on the 20th being the first day of the month?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8612)
    
499.  What a beautiful spreadsheet. Is there perhaps a video on how to start it from scratch?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8609)
    
500.  Great template, one question/problem:  
    – if I modify the formula in NJ8 (trying to change the 0.5 to 1 so that all leave types will be counted as a full day) then I end up with a #VALUE error in the cell, not sure how to fix this
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8596)
    
    *   I am also trying to do this. Did you find out how to make all leave types count as full days?
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10196)
        
501.  Hello There,  
    The leave tracker one of the best..!Love the Tool..!  
    One que i am not able to find same format and formula in next month Exp-if i scroll jan to Feb found the that the micro may not be available in this workbook or all macros may be disable..can you suggest me for the same  
    thanks.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8595)
    
502.  Hi there.  
    Love the tool – so useful!!!!!
    
    Are you aware of a way that will stack 3 months at a time and show the month prior and after the selected month? So a manager can see 3 months of planned leave at a time?
    
    I have thought about linking multiple macros but I did find it difficult and kept getting errors.
    
    For example, if we have 3 employees and instead of viewing 3 months horizontally, we want to see vertically. Using what we would like to see for feb as an example I have listed it below…
    
    January 1 2 3 4 5 6 7 8 9 10 11 12 etc
    
    Employee 1
    
    Employee 2
    
    Employee 3
    
    Feb 1 2 3 4 5 6 7 8 9 10 11 12 etc
    
    Employee 1
    
    Employee 2
    
    Employee 3
    
    March 1 2 3 4 5 6 7 8 9 10 11 12 etc
    
    Employee 1
    
    Employee 2
    
    Employee 3
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8581)
    
    *   Hello Matthew.. That would have to be a completely new tracker.. Stacking these months would mean a complete overhaul of formula and VBA
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8582)
        
503.  This is excellent! Thank you for the tracker but i have one doubt if i enter SL on Jan 5th its taking automatically next month also ???
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8578)
    
    *   Hello Vinoth, You need to use the scroll bar to change the months, and not cell A1
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8583)
        
504.  This is excellent! Thank you for the tracker. I’m customizing it for my team, however I’m having trouble adding more employees. Need help. I tried copy-pasting the formula to add more members but the scroll bar is overlapping.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8577)
    
    *   Hello Ashwini, Right-click on the scroll bar and then you can move it.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8584)
        
505.  Hi Sumit, where can I input a staff’s leave entitlement for the year?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8576)
    
    *   Hello Jan, you can put these at the end of the tracker. Next to the leave count
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8585)
        
506.  Sumit, you have made my life easier creating this. I love it. I am having difficulty tweaking it just a little, I’d like to know if you can help. I want to add 3 columns after the name column, to enter the employees hire date/accrual time/ days left. I’ve been trying, but all the formulas get mixed up one way or another. I’m still a beginner so I have no idea what I’m doing (clearly).
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8574)
    
    *   Hello Leslie.. You can insert details about the employees after the tracker ends (from column NQ onward). That ways it will not mess with the formulas and VBA
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8586)
        
        *   Hi Sumit!  
            Thanks so much! It worked perfectly. Really appreciate you sharing 🙂
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8638)
            
507.  This is AMAZING! I can not wait to use this for a portion of our company. Your making me look good Sumit.  
    I was wondering, could i get your email or a way to reach out regarding how we do the remaining of our employees to see if you could help. We track our staff (no managers) by hours. IS there anyway to do that with this excel sheet? Really look forward to hearing from you
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8486)
    
    *   Hello Shannon. Glad you found the template useful. You can reach out to me at [sumitbansal@trumpexcel.com](mailto:sumitbansal@trumpexcel.com)
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8492)
        
    *   Shannon, did Sumit ever solve this issue for you? We have the same request.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10896)
        
508.  the scroll bar simply skips few months
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8480)
    
    *   It happens if you have a slow system or too many applications open. To handle this, click on the tip of the scroll bar and then move away the cursor.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8496)
        
        *   Hey thanks for the reply. Appreciate it.
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8505)
            
509.  Once we move to next month, then the leaves tracked for previous month are reflecting. This makes it unusable.  
    Please help.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8478)
    
    *   Use the scroll bar to change months, and not cell A1
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8495)
        
510.  When I save to google drive the scroll bar disappears (all the other functions appear available). How do I create/copy the scroll bar?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8475)
    
    *   Hey Jenene.. You can’t save this is Google Sheets as it does not have a scroll bar feature and does not use VBA. I am working on creating a leave tracker in Google Sheets. Will share soon.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8497)
        
511.  This looks great but the month changer scroll bar either moves one month or scrolls all the way to the end of the year?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8472)
    
    *   Hey Jonathan.. It happens if you have a slow system or too many applications open. To handle this, click on the tip of the scroll bar and then move away the cursor. Hope this helps!
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8500)
        
512.  awesome! Thank you Sumit!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8470)
    
    *   Thanks for commenting Jan.. Glad you liked it!
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8501)
        
513.  Hi,
    
    I tried to mark Feb 7, 2016 as VL for 2016, but when I changed the year to 2017, Feb 7, 2017 was automatically VL. Do we have fix to delete the entries for another year if you moved to the next year?
    
    Also, what if I want to add a “Half Day SL” in the leave breakup? How to do this one?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8469)
    
    *   Hello Paul.. This tracker works for one financial year only. So If you want to have one for multiple years, you need to create a copy of the workbook. There is already a Half Day leave in the tracker (use the code H)
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8502)
        
514.  Its a very very useful tracker..kudos… however , it doens’t allow for designations, locations, DOJ etc. to be added
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8466)
    
    *   Hello Rachna.. You can add these additional details at the end of the tracker in the same row. That ways it wouldn’t break the tracker but still allow you to have the details
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8503)
        
515.  Thank you for this wonderful tracker! It is very useful. I would like to track the “Leave this Year” for the period 1 July 2016 to 30 June 2017 (instead of the calendar year.) Can you please advise how I can do this?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8465)
    
    *   Hello Angie.. You can do that by selecting 7 from the drop down in cell A1.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8504)
        
516.  CAN U UNDERSTAND ME DEEP TO ATTENDANCE SHEET OF EMPLOYEE
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8463)
    
517.  how to add coverage: if any one is on leave some one is assigned to cover. How to add name of person covering to cell where type of leave entered
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8101)
    
    *   The easy way would be to add the name in the same row after the tracker ends.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8515)
        
        *   When using the spreadsheet the leave calculator only show formulas but no numbers/
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10963)
            
518.  the formula you entered in NJ AND NK DOES NOT COUNT THE LEAVES PROPERLY. CRATEFUL IF YOU COULS SEE TO THE MATTER. THANKS
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-7961)
    
519.  Hi! May I know how would I be able to change the value of casual leave to 0.5? Thanks!!!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-7960)
    
520.  Hi Sumit. I need to add 2 columns to the right of Name and before the first date. but when I do it shifts the days. How can I add a column for Employee ID and DoH?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-7959)
    
    *   Hello Fran.. while the tracker breaks if you try and insert columns, it would work fine if you have these details in column NT or to the right of it.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8520)
        
        *   Hi sir thanks alots for this helpful sheet that’s what I’m looking for from long time but really you would help me to add some colume after the name if you can share the sheet with extra colume after the name coz ineed around 7 colume to add all staff details
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10481)
            
521.  Hi Sumit. Excellent work. I really like the excel leave planner. However I have to include weekends as well in the leave breakup columns. Right now it gives the leave count for week days only but if we need to consider weekends as well, then the leave breakup column is not considering the weekends days.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-7941)
    
    *   In the select working days options, just make all the days as working days (select yes for all)
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8528)
        
522.  Fantastic spreadsheet, thanks. I need to add more rows for employees but the scroll bar stays in the same place. If I move it it doesn’t work properly. How can I do this?  
    Denise
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-7940)
    
523.  Dear Sir, how to add more types in leave breakup and also to add present column which counts the present number for everymonth or entire year.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-7937)
    
524.  do you have tracker for 2017
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-7920)
    
525.  hi how do you add no of employees to the tracker
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-7919)
    
526.  Hi, thanks for an awesome spreadsheet.
    
    1\. How do I add more leave options – I want to add a leave option for “unpaid leave” and a few others.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-7915)
    
527.  Hi Sumit. The leave planner is fantastic. Quick question though, I need to add in TOIL in half days. I’ve tried copying and pasting the half day formula but it doesn’t work. Please could you tell me how I can add another leave type that counts half days.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-7904)
    
528.  Thank you for the great template you created.  
    I am looking to create a copy of the “leave tracker” sheet, within the same workbook so that I can track year 1, year 2 etc. all in one document rather than creating a new one for each year.  
    The only block I can see to this is the VB logic to show the calendar. As soon as I copy the sheet and start moving the scrolling bar the VB crashes to debug. Any idea on how to fix this. I expect it would be changing the VB logic / macro to apply to a sheet rather than workbook but cannot work it out.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-7894)
    
529.  Hi Sumit, this is really helpful however when i am trying to add more rows the scroll bar is reflecting in between, i try to hide but it is not working can u help
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-7788)
    
    *   ALSO IF I UPDATE ONE MONTH THEN IT REFLECTS IN OTHER MONTH TOO
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-7791)
        
        *   To change month, don’t use cell A1. Use Scroll bar only
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8540)
            
    *   Hello Nivedita.. Right click on the scroll bar and drag it wherever you want it!
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8529)
        
530.  Hi Sumit…
    
    I downloaded your excellent Leave Tracker and I’ve added some other functionality to it. Great spreadsheet – love the slider changing to the relevant month. I’ve since added 4 sheets to it showing an Individual Calendar (showing all annual absences of all types), a group summary and a Management summary dashboard along with a Master data spreadsheet controlling some new functionality. Couldn’t have done it with your starting sheet though.
    
    As an idea for a future spreadsheet what about and ‘Issues / Risk Log Tracker’. This should ideally include the following:
    
    The same log should be able to track Issues or Risks.  
    Each record must include  
    ‘Unique Reference’ e.g. I-001 or R-001,  
    ‘Raised By’ (Creator Name)  
    ‘Date Logged’,  
    ‘Issue Name’ (or ‘Customer Name’),  
    ‘Description of Issue / Risk’ field (free text),  
    ‘Current Owner’ (Owner name)  
    ‘Priority’ (High, Medium, Low),  
    ‘Age’ field (Age of issue in days)  
    ‘Last Updated on’ (Date / Time field – flagged and highlighted if not updated in X days),  
    ‘Status’ (Open, Closed, On Hold (with a triggered ‘Off Hold’ date),  
    an associated ‘Audit’ record and, most importantly… Each record must be able to accommodate multiple Actions with each Action having a Time / Date stamp.
    
    A Log Dashboard would be useful e.g. X Records over Y days, XX Records over YY days, had XX records open, etc., etc.
    
    There are lots of Templates out there but all a little basic and importantly they don’t accommodate multiple actions (most Issues / rRsks are resolved with a series of actions which need to be recorded and tracked). The ability to produce a formatted history / report for an individual record would be nice – especially if it can be emailed to the person / persons responsible for the next action.
    
    What do you think? I developed a spreadsheet that does all the above but it is a little clumsy and probably not that efficient – I’m sure it can be improved on.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-7304)
    
531.  Hey Sumit, love the holiday tracker. I created a similar one, also free to download, check it out here [http://www.excel-macros.co.uk/free-excel-tool-for-recording-and-tracking-employee-vacations/](http://www.excel-macros.co.uk/free-excel-tool-for-recording-and-tracking-employee-vacations/)
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-7303)
    
532.  Hi, I have 2 questions as below:
    
    1)0.5day can be sick leave, annual leave or unpaid leave. How can I do to count this particular 0.5day at the respective breakup column as 0.5 instead of counting as 1?
    
    2)Some employee are 5 working day, some is 6 working day and some is 5.5 day within departments. Can I record altogether in this template?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-7153)
    
533.  hii.. first thanks for your amazing template.  
    when i add a column before the name column. the january shows only 30 days while it should be 31 days. i tried adding an extra column but when i scroll to the february and came back it is again 30 days. what should I do?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-7139)
    
534.  need to ask how could I make H code for day off full day not half day
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-7036)
    
535.  Hello, Is there a possibility to add the holidays too during vacation?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-7034)
    
536.  Hi Sumit, I am trying to scroll through to the next month but it keeps jumping all the way to the last month.. the scroll bar moves automatically even when I click just once on the forward arrow, all the way to the last month. I am using Microsoft Excel 2016.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-5396)
    
537.  Exactly what I was looking for! I want to modify the name of the leave types and have a different color for each one. Is there a simple way to do this?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-5165)
    
    *   I also would like to modify the names of the leave types?? I am NOT familiar with Excel formulas and would greatly appreciate step by step instructions, especially for changing the colors. Thanks!
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-5171)
        
538.  Further to my post below, Sumit, One more question, Sometimes a staff may work on a weekend. Normally this is added back on from the leave days (effectively increasing the eligible leave days by one). How would that be done?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-4300)
    
539.  Hi Sumit, Just downloaded the template and am trying to learn to work it. So far it seems like it will make life a lot easier for me. Maybe an extra day or two of vacations for me. On question though, our staff all have different working years and not necessarily 1st Jan to 31st Dec. How would that account for in this system?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-4299)
    
540.  Hi Sumit – great chart. I’ve been looking for something like this for a while. You say we can add more employees by copying and pasting additional rows – and that works well. However, I need to print the chart so staff know who is on leave when – we have 150 staff and only a certain number can be off at any time 🙂 When I add more rows, the scroll bar for the months is also printed. I tried moving it – but somehow that interferes with the VBA code and I have no idea how to alter that. Can you assist and/or tell me what I need to do to make this alteration. Generally there would only be 40 staff listed on one chart as I have created a different worksheet for each category of staff. Thanks again.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-4205)
    
    *   Hi Sumit  
        I think I found the answer. I had copied the worksheet so I could have different categories on staff on separate worksheets in the one workbook. That created a bug in the VBA code somehow – which was why I couldn’t move the scroll bar. Is there a way to duplicate the worksheet so I can have four categories of staff on different worksheets in the one workbook? I don’t really want to have to save it as four separate files. Will be a little tedious for the staff inputting the data if I do that?  
        The question about the highlighting the cells without the “V” showing in the cell is still relevant if you can answer that as well please. Thanks
        
        Sue
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-4301)
        
541.  Hi Sumit, how do we change the color for those holidays that fall on a weekend (Sat/ Sun) to the ORANGE highlight.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-4201)
    
542.  Wow!! It’s exactly what I was looking for. Thank you.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-4193)
    
543.  Hello! I would like to ask why every time i am adding columns, the 1-31 dates is changing. when i add one column, the date one number will be removed, and so on. How can i add columns without changing the dates? Please help! Thanks ahead 🙂
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-4056)
    
544.  hi, with the newest version available, how do add more employees? at least 40 for example, but with the version that we can edit the working days and sums up the whole year leaves too.? @sumitbansal23:disqus
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-4048)
    
545.  Hi Sumit,
    
    You are god sent! The excel is god’s gift!  
    However, i have added 2 more leave codes and how do i color code them using conditional formatting?  
    Thanks! Ivy
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-4045)
    
546.  Can someone please tell me how you add Bank Holidays into the spreadsheet?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-4028)
    
    *   If you look on the second tab on the workbook, the US bank holidays are all listed, just change the date and the description and it automatically updates on the main spreadsheet 🙂
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-4029)
        
547.  hi sumit i like your template very much but how can i change the calendar i mean i need to use Ethiopian calendar we have 13 months each contains 30 days except the last one which contains 5 days and the year is 2008 can you help me please?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-4019)
    
548.  Hi, i have some staff that work different hours and there leave is calculated in hours rather than days – anyone know how i can work this into the formula? Also i need to add a column next to the employee name, but when i do this the 1st day of the month disappears – can any one help?
    
    Great piece of work by the way – works really well!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-4016)
    
549.  Hello Sumit,  
    You have the best tracker I have been able to find so far! There are a couple tweaks I have been trying to do specifically for my job and I was wondering if you could assist me? I could email you the changes I have made and what my goals are in each area that I’m having issues with. Thank for your help!  
    Matthew
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3990)
    
550.  Hello Sumit, first of all great file, im learning a lot with all your posts.
    
    I have been playing with this file trying to make it show me the weeks per year, and also im trying to make it show me the leaves not only the total of the month but for the week. (first week this many leaves, second week this many…)
    
    Hope you can help me and once again Thanks for sharing your knowledge.
    
    Regards from Mexico!! Amigo.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3988)
    
551.  Hi Sumit Am I doing something wrong? When I add any type of leave into a month it copies over into all the subsequent months,
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3979)
    
552.  Hi there, I really love this excel. Simple and beauty.  
    Then I’m trying to convert this excel to google spreadsheet. So me and my friend could collaborate when using it. By simply do import from excel on G spreadsheet, basic function are working well . And i love it, until I realized, the day the date are not correct. 1st Jan 2016 should be on Friday. In fact it show Sat on google spreadsheet.
    
    Anyone could help ?  
    Many thanks.
    
    – Alex
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3915)
    
    *   Hello Alex.. This can be converted into Google Sheets as it uses VBA. I am working on a Google Sheet leave tracker and will share it soon.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-4007)
        
553.  I’d love to see this tracker calculate the amount of PTO hours used (and how many hours are remaining) not just the amount of occurrences. Otherwise it’s great!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3911)
    
    *   Is there any way you can upload a formula for that? I can’t seem to figure it out :o/
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3912)
        
554.  Hi Sumit, just awesome to track leave. Here by us sick leave must be calculated even over NON working days, the other leave types only on workings days. I can make the complete week a working week, but then my cell shading is gone making it more difficult to enter data. Please tell me where I must change the formula to include NON working days for my SICK leave count. Thanks again, Chris
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3906)
    
555.  Hi – thank you so much for this leave tracker.. it helped me a lot. However, I have one slight problem. Whenever I place a leave on a specific date for example on March 2016, what happens is its duplicated on all months. For example I placed an Emergency leave for March 15 2016.. all months every 15th has an Emergency leave on it. Please teach me how I can fix it. Thank You. 🙂
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3899)
    
    *   Hello Renee.. Please use the scroll bar to change months (and not cell A1).
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-4006)
        
556.  Hi Admin, How can this template be used for over 100 staff of a restaurants business that has many outlets. something . This question is because you have only 10 staff on the template . kindly send a private mail if possible. [seyibabatunde01@gmail.com](mailto:seyibabatunde01@gmail.com)
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3895)
    
557.  Hi Sumit, I need to change the value of the Casual leave to be 0.5 instead of 1. Another user mentioned he used the array formula. It would be great if you could suggest how I can change this. Loving your spreadsheet 🙂
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3894)
    
    *   Hello Venessa. Use this formula in cell NJ8 (and copy for all cells): =SUMPRODUCT((OFFSET($A8,0,31\*($A$3-1)+1,1,31)””)\*(IF(OR(OFFSET($A8,0,31\*($A$3-1)+1,1,31)=$NS$6,OFFSET($A8,0,31\*($A$3-1)+1,1,31)=$NS$5),0.5,1)\*(OFFSET($A$4,0,31\*($A$3-1)+1,1,31))))
        
        Use this one for NK8 (and copy for all cells): =SUMPRODUCT((OFFSET($A8,0,1,1,372)””)\*(IF(OR(OFFSET($A8,0,1,1,372)=$NS$6,OFFSET($A8,0,1,1,372)=$NS$5),0.5,1)\*(OFFSET($A$3,0,1,1,372))))
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-4005)
        
        *   Hi Sumit, I tried to copy and paste this formula but it’s not working.
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-7967)
            
            *   You will need to use Control + Shift + Enter instead of just Enter.
                
                [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8518)
                
558.  Hi Sumit. This is amazing. However, there is a slight glitch on the sheet. Data populated on a particular month is also showing on other months. Can you help me with that please?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3892)
    
    *   Hello Mirasol.. Please use the scroll bar to change the months. Don’t use cell A1 to do this.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-4004)
        
559.  How do you print this template?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3880)
    
    *   You can print it but it may not fit into the print area. Have a look at this to set the print area: [http://trumpexcel.com/2015/12/how-to-set-the-print-area-in-excel/](http://trumpexcel.com/2015/12/how-to-set-the-print-area-in-excel/)
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-4003)
        
560.  Hi, This is amazing and just what I’ve been looking for, but when i download, the scroll bar isn’t working, any idea on what may be wrong or how I fix it?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3878)
    
    *   Hello.. When you open the workbook, it might prompt yo enable macros. You need to click on that prompt button so that macros can work.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-4002)
        
561.  HI,
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3877)
    
562.  Hi, thanks for this! however I am having trouble when entering annual leave in January it maps to all the other months. how can i stop this? … thank you
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3876)
    
    *   Hello Ella.. Please use the scroll bar to change the months. Don’t use cell A1 to do this.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-4001)
        
563.  Sumit ..this tracker is really neat. Do you have a suggestion on how to enter actual times instead of using codes? I am needing to enter leave time used in increments as small as 15 minutes up to 12 hours depending on what individual employees use on any given day. I was hoping I could modify this wonderful layout if there was a way..thank you so much
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3874)
    
564.  Hi, looking to add a additional sheet to the tracker called Comp Offs, I work for an AUS client so we take Australian holidays, if I work o the list of AUS holidays im eligible for a Comp Off, how do I add that to the tracker so that after I update the holiday list and it shows as orange in the tracker now if I mark as Present (P) it should showup as a comp off  
    Secondly need to track the comp off’s each person is eligible for and if utilized or not  
    Please help  
    Not forgetting that the tracker is awesome
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3841)
    
565.  Hello, I would like to delete everything but vacation. When I try, I delete all the hard work that you put into this so is there a way I can only track vacation only?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3832)
    
    *   Hi Megan. I would suggest, when you type “V” into the cells the person takes their vacation, this will put in “V” for vacation – just ignore all other types of leave and do not use those codes. I need the same and that is what I am doing.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-4209)
        
566.  Hi, this template is super! However, I’d appreciate if you could help me out with my scenario – I’ve selected the year Jan’16-Dec’16, and updated the leave plans for my team. However, if I now change the A2 as 2017 (in order to plan for 2017 leaves starting Jan), the 2016 highlighted leave plans reflect in 2017 months, and are all messed up. I was expecting the cells to be reset as soon as I select another fiscal year! Is there a fix?
    
    Thanks
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3786)
    
    *   Hello Amrit, You can use this planner only for one financial year. In you want to use it for multiple years, you need to create a copy of this, so one for 2016 and a different one for 2017.
        
        Also, to change months, use the scroll bar and not cell A1.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3790)
        
        *   Hi, to use this for more than one year, I have moved the holiday list on the year sheet and then made copies of that sheet. I then added another sheet to give me totals for all the years. But to do this you need a little bit about Formula and VBA skills
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3907)
            
567.  i want to add one more code for leaves but don’t want to count it in total leaves of a year.. how i can make changes?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3782)
    
    *   In that case, a better way would be to apply a backgroud color to the cell. That way, it will be highlighted but not get counted.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3791)
        
568.  Hello,  
    We want to maintain 2016 and 2017 in one excel, can you please help us
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3765)
    
    *   You need to create separate copies (preferably separate workbooks) for this. This leave tracker only covers one year,
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3792)
        
569.  hi! amazing sheet thanks a lot! how to count as well over time?  
    eg: my staff working on weekends or during national days, i need to count so that i replace their over time by holidays  
    thanks
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3760)
    
570.  thanks sumit …. its awesome but kindly help me all the month sheet are of same holidays after using scroll bar.also how it is possible to change holidays for a particular month.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3750)
    
571.  Any way to add vacation accrual based on hire date to calculate time remaining for each employee?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3743)
    
572.  I would like to change the half day value. How do I change it from 0.5 to 1?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3741)
    
573.  Does anyone know if hours versus codes could be entered? Thanks
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3729)
    
574.  How can I copy the calender so that the vbn module works on more then one sheet in that workbook?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3717)
    
575.  Hi Sumit,
    
    This is Arikrishnan. So pleasure to get in touch with you. I need a favour from you regarding a Tracker you updated for Attendance ([http://trumpexcel.com/2015/03/](http://trumpexcel.com/2015/03/)
    ….  
    In this Tracker you have made the fields “Leave this Month (Cell NJ)”, “Leaves This Year (Cell NK)” till Cell NQ as constant and only cells allocated for every month changes.
    
    My requirement is that, I need those aforementioned fields needs to be changed as I would like to use those fields for monthly report. Can you assist me in this !!!!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3704)
    
    *   Hello.. Cell NL to NP are not constants. The value changes when you mark a leave for any month. However, these would show you the value for the entire year, and not monthly
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3736)
        
576.  Can the templete be altered to enter actual hours used for leave time? For instance, employees have 480 hours of FMLA, family medical leave, in a rolling calendar year. They can use in increments of 15 minutes. Would like to be able to see what they have used and how much is available. Any help would be appreciated! Thank you
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3703)
    
577.  hi! Sumit,  
    I have just downloaded the leave tracker. It looks really good but I just cant change the months.  
    Can you please advise.  
    Appreciate your help and great template.  
    Thanks,  
    Nilam
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3702)
    
578.  Hi – This is awesome, thanks! Could you tell me though how to modify the time off values (i.e. maternity leave – i don’t want this to show as days taken, because it doesn’t count towards their vacation, it’s protected time away). So, if I wanted to make mat leave = 0 days taken, how would I do that?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3683)
    
579.  Its amazing, thanks for the same. Can you please help assist how can we move the Scroll bar down while adding more employees
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3676)
    
    *   ahh.. I found the answer in the comments, thanks 🙂
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3677)
        
580.  Hi,
    
    Whenever I put a leave in a cell it reflects on the other months. Kindly help advise. Thanks. 🙂
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3617)
    
    *   Hello.. please use the scroll bar to change months and the value in cell A1
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3649)
        
    *   Hello.. please use the scroll bar to change months and the value in cell A1
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3650)
        
581.  Hi Sumit ! Thanks for this wonderful tracker, I have slightly tweaked the formulas to add the days present. these efforts wont be counted in no of leaves for the month and year [https://uploads.disquscdn.com/images/156a36b1d988100d97549cbca759b81ae5f2a17d700e17e1df6d5b173ec26456.png](https://uploads.disquscdn.com/images/156a36b1d988100d97549cbca759b81ae5f2a17d700e17e1df6d5b173ec26456.png)
     .leaves this month:=SUMPRODUCT((OFFSET($A8,0,31\*($A$3-1)+1,1,31)””)\*(IF(OFFSET($A8,0,31\*($A$3-1)+1,1,31)=$NS$6,0.5,1)\*(IF(OFFSET($A8,0,31\*($A$3-1)+1,1,31)=$NS$7,0,1)\*(IF(OFFSET($A8,0,31\*($A$3-1)+1,1,31)=$NS$8,0,1)\*(IF(OFFSET($A8,0,31\*($A$3-1)+1,1,31)=$NS$9,0,1)\*(IF(OFFSET($A8,0,31\*($A$3-1)+1,1,31)=$NS$10,0,1)\*(OFFSET($A$4,0,31\*($A$3-1)+1,1,31)))))))) leaves this year:=SUMPRODUCT((OFFSET($A8,0,1,1,372)””)\*(IF(OFFSET($A8,0,1,1,372)=$NS$6,0.5,1)\*(IF(OFFSET($A8,0,1,1,372)=$NS$7,0,1)\*(IF(OFFSET($A8,0,1,1,372)=$NS$8,0,1)\*(IF(OFFSET($A8,0,1,1,372)=$NS$9,0,1)\*(IF(OFFSET($A8,0,1,1,372)=$NS$10,0,1)\*(OFFSET($A$3,0,1,1,372)))))))) paste there use control +shift+enter
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3611)
    
    *   how could I edit .. can you send me yours  
        [Mohamed\_shaaban@outlook.com](mailto:Mohamed_shaaban@outlook.com)
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-7222)
        
582.  Any answer on this question pls guide me Some of the additional “leave codes” I would like to have counted as 0.5, however, they are all being counted as 1.0. How do I change that?  
    SUMPRODUCT((OFFSET($A10,0,31\*($A$3-1)+1,1,31)””)\*(IF(OFFSET($A10,0,31\*($A$3-1)+1,1,31)=$NS$6,0.5,1)\*(OFFSET($A$4,0,31\*($A$3-1)+1,1,31)))) here =$NS$6,0.5,1 similarly i want =$NS$5 also counted to be 0.5 thanks!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3608)
    
583.  Thx for this great spreadsheet. Can I ask for a version where You can also add two columns on the right from the employee which would include number of the employee group and current shifht. I need those informations to quickly manage shifts in the company. Those 3 columns wolud have to be visible all the time.  
    Pls right me back.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3604)
    
    *   Hello Lukas.. You can add new columns to the right of the tracker (column NT onwards). That would keep the tracker intact and also have the columns visible at all time
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3651)
        
    *   Hello Lukas.. You can add new columns to the right of the tracker (column NT onwards). That would keep the tracker intact and also have the columns visible at all time
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3652)
        
        *   Hi sumit  
            i need to add columns to the left, please help
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11542)
            
584.  Hi Sumit,
    
    I have figured out what I was doing wrong! I had the right formula but missed that the formula was an Array Formula so consequently I was getting the #VALUE! when I spotted the { } brackets at the start and end of the formula I did some research which suggested after entering the additional information I use the key combination  
    CTRL-SHIFT-ENTER rather than just Enter and it worked!
    
    Now have the spreadsheet working perfectly with 3 options for half-days and an additional column noting the lateness.
    
    Patrick
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3573)
    
    *   Great! Since there are so many variables, array formulas were the way to go. and they need Control + Shift + Enter
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3653)
        
        *   Thanks again!!
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3688)
            
585.  `Savvy piece , Apropos , others need a HI DoT BB-1 , my colleagues filled out a blank document here http://goo.gl/MFT7jp`
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3569)
    
586.  Can we use 1 tab for 2016 and 1 for 2017 in the same file with 1 tab for combined holidays?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3568)
    
    *   You can create a copy of this tracker and keep in the same workbook.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3654)
        
        *   I tried copying the sheet and changing the year to have 2 leave sheets in one workbook. I received a VBA debug error. Any help would be much appreciated. Love this leave sheet.
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-14108)
            
    *   You can create a copy of this tracker and keep in the same workbook.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3655)
        
587.  Can we use 1 tab for 2016 and 1 for 2017?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3567)
    
588.  Excuse me, how can I remove the Half day cell. I do not want two half day to change to one day leave. How can i Change it , please?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3560)
    
    *   You want to remove the half day leave? You can use other codes except H which is for half leave.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3656)
        
589.  Hi, I’ve recently start using this great spreadsheet as it really fulfills all my needs but unfortunately I’m not as good expert of excel as this sheet. So, would like to know few things:
    
    – How I can customize/add/remove the leave codes  
    – How can I update new code on leave break up section
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3559)
    
    *   Hello Shujat.. The tracker is a bit complicated so to add new codes, you will need to modify the formulas and make sure new codes are part of it. Alternatively, you can create a copy of the tracker and split the codes
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3657)
        
    *   Hello Shujat.. The tracker is a bit complicated so to add new codes, you will need to modify the formulas and make sure new codes are part of it. Alternatively, you can create a copy of the tracker and split the codes
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3658)
        
590.  Is there anyway to know the VBA Code that runs in the back to keep the month changing?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3550)
    
    *   Activate the worksheet and press Alt + F11. The only thing that VBA does in this is hide columns when you use the scrollbar
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3659)
        
    *   Activate the worksheet and press Alt + F11. The only thing that VBA does in this is hide columns when you use the scrollbar
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3660)
        
591.  Hi Sumit,  
    I am not sure where my last post went but we actually need 3 1/2 day options and to increase the Leave tracker to 6 categories rather than 5. I have managed to add the sixth category but cannot seem to get the other two 1/2 day formulas to work I keep getting #VALUE! error. Please can you help. For the record, our 1/2 day options are Half day holiday (HH), Half day sick (HS) and Half day other (HO).  
    Thank you in advance,
    
    Patrick
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3548)
    
    *   Hi Patrick! I am having the same issue as you! I need to change to change one of the leave options to account for a half day holiday! Would be awesome if you could share how you got around this! Thanks!
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3893)
        
        *   Hi Vanessa, Are you adding an extra row/ column or just amending one of the formulas?
            
            I had to add to add an extra row so firstly make sure you only move the rows directly below where you insert the formula so that the main spreadsheet is kept in its format. I copied one of the leave codes and then “Inserted Copied Cells” shifting the others down and changed the letters to the Code I wanted i.e. HS  
            When you add the extra column, Copy the whole cell range and again insert the copied cells, this will shift the whole lot to the right then again change the code to match the one you want.  
            Once you have completed the first two actions, you will then need to amend the formulas in the first cell you want to change, make the relevant changes directly into the cell then before exiting the line use the key combination  
            CTRL-SHIFT-ENTER (This is because the formula is an Array formula)  
            This will then save the amended formula for you. Once you have done this once, you can copy the cell and paste and this should work fine.  
            I hope this helps, let me know if I can help any more, good luck,  
            Patrick
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3896)
            
            *   Hi Patrick, thanks a bunch for your help. However, I need to change value of C to equal a half day instead of 1 full day. I don’t understand how to change the formula let alone find it. Any help or guidance would be greatly appreciated! Thank you again for being so kind!
                
                [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3897)
                
                *   Hi Vanessa,
                    
                    It is a bit complex but I think I can put something together to show you how to change C to show a 1/2 day. I am training staff today but will try to get an answer to you tomorrow.  
                    In the meantime, please can you let me know which cell the letter “C” sits in i.e. NP4 etc
                    
                    Thanks,
                    
                    Patrick
                    
                *   Hi Vanessa,
                    
                    Just wondering if you could let me know which Cell the letter C sits in on your spreadsheet.
                    
                    Thanks,
                    
                    Patrick
                    
                *   Hi Patrick,
                    
                    I managed to edit the formula and it worked! Thanks again for your help though!
                    
                    Do you happen to know how to create one for 2017? Do we change the dates and holidays manually?
                    
                    Thanks,  
                    Vanessa
                    
                *   Hi Vanessa,
                    
                    I am delighted that you have managed to make the changes!!! All you need to do is amend the Year on the spreadsheet to 2017 and it will do the rest for you. What we have done here is to copy the sheet and change the date and save it as 2017.
                    
                    I hope this helps best regards,
                    
                    Patrick
                    
                *   I also need to know how to change the formula to include 6 half day options. I have them changed on the right but they dont figure in as half. I understand the crtl, shift etc but where do I put that in the formula? The formula shows as
                    
                    \=SUMPRODUCT((OFFSET($A8,0,31\*($A$3-1)+1,1,31)””)\*(IF(OFFSET($A8,0,31\*($A$3-1)+1,1,31)=$NS$6,0.5,1)\*(OFFSET($A$4,0,31\*($A$3-1)+1,1,31))))
                    
                    I know I the NS is no longer correct and should be OS but when I add the range it adds them to the total even without any entries being made
                    
                *   Hello Kary,
                    
                    As you will see I have had to put in a new set of formula for each separate half day that I had to record.
                    
                    \=SUMPRODUCT((OFFSET($A70,0,1,1,372)””)\*(IF(OFFSET($A70,0,1,1,372)=$OG$8,0.5,1)\*(IF(OFFSET($A70,0,1,1,372)=$OG$5,0.5,1)\*(IF(OFFSET($A70,0,1,1,372)=$OG$9,0,1)\*(IF(OFFSET($A70,0,1,1,372)=$OG$3,0.5,1)\*(OFFSET($A$3,0,1,1,372)))))))
                    
                    Before I did this, I had to create the half day holiday reference cells so I added to the existing table pushing the Days of the week table down. (I hope this makes sense where you have “NS$6” I changed mine to “OG$” then the cell number this is because I moved the cells to the right when I created the extra columns to show the half days under the “Annual Leave Breakup” columns (I simply copied the Holiday Column, pasted copied cells, shifting to the right and renamed the column).
                    
                    I hope this helps,
                    
                    Patrick
                    
                *   Yes this does make sense. I’m pretty good at excel but this one was beating me. I could get it to show .5 but then nothing else I entered for that month would add in the monthly total, just the yearly total. Thank you
                    
                *   I hope that it is now working, I must admit it took me a few goes…. 🙂
                    
                *   Hi Vanessa,
                    
                    So sorry for my slow reply. I just copied the spreadsheet then amended the year to 2017 and it did the rest.
                    
                    Patrick
                    
592.  how to edit the formula & add some category of leave… I’ve been trying this for 2 days now, but everytime i change the formula even for the row number it shows error.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3537)
    
    *   Hi Casper,
        
        You can make the changes as normal but as the formula is an Array formula you have to shut it down differently, you cannot just select ENTER you have to use the key combination CTRL-SHIFT-ENTER – here is a link with more detail, which helped me:
        
        [http://www.excelforum.com/excel-formulas-and-functions/553799-what-do-brackets-mean-when-they-encompass-a-function.html](http://www.excelforum.com/excel-formulas-and-functions/553799-what-do-brackets-mean-when-they-encompass-a-function.html)
        
        Hope this helps, let me know if you want to know how I added in the additional codes etc
        
        Patrick
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3574)
        
593.  how can i add for the category or kinds of leave , we have halfday for sickleave and halfday for sickleave? how will i add it to the formula. thanks
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3534)
    
594.  Hi sumit
    
    Your leave tracker is very nice.thanks.i have modified the leave tracker to include onshore and offshore and hence have created two list in holidays.its working fine except the sum section in column NJ.I am just replacing the holiday list in formula with my one but its not working.its showing 1 only.also i am not able to understand the logic also.can you please help.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3530)
    
595.  HI Sumit,  
    Please help me with tab-wise employee sheet instead of month-wise view,  
    This will help to see annual details of a single employee on one sheet.  
    Can you please upload anything like that?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3519)
    
    *   Hello.. The tracker is made to have all employees in a single sheet. Currently I don’t have anything that shows each employee detail in a separate tab
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3661)
        
    *   Hello.. The tracker is made to have all employees in a single sheet. Currently I don’t have anything that shows each employee detail in a separate tab
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3662)
        
596.  Hi this looks superb,  
    i would like to have employee wise tabs instead of month wise,  
    so one sheet will have annual details for one employee.
    
    With months on the place of employee names and the heading will be the name of employee.  
    Please hep
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3518)
    
597.  Hi Sumit, thanking you kindly for making your hard work available for everyone to use!
    
    I need some assistance regarding protecting the sheet. I need my employees to have access to view the planner but no edit permissions. I have tried many avenues however I’m unable to make the scrollbar the only accessible function. Are you able to assist? Many thanks!!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3517)
    
598.  Hi Sumit,  
    how to add in-lieu leave, my team sometimes work during weekend or holiday… Thanks
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3495)
    
599.  how to change the colour in leave code there are only showing RED colour  
    any know body know please let me know please
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3470)
    
    *   You can use conditional formatting to change the color
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3663)
        
        *   Please let me know clearly
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3667)
            
        *   Please let me know clearly
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3668)
            
600.  Hi,when i update as S”Sick leave” for the month Jan 4th Example of employee 1,when i change the month to febrauary also, the 4th date Sickleave will remain same in the sheet,request you to do the needful.thanks
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3464)
    
    *   Hello.. You need to use the scroll bar to change the month and not the value in cell A1
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3664)
        
601.  Hi, i’m planning to do up a firefighter leave tracker. I need to tweak the excel sheet but i’m clueless. Can i get your email to discuss with you?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3431)
    
    *   Yes indeed. My email is [s.thomas@betterhomehealthcarega.com](mailto:s.thomas@betterhomehealthcarega.com)
        .
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3437)
        
        *   Muhud you would need to speak directly with Sumit as I’m not familiar with the chart to that extent. I believe you posted under my question and I thought it was Sumit needing more information for my specific chart needs. Sorry!
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3460)
            
602.  Hi Sumit, I have been using the awesome leave tracker and I find it very useful. I’m having problem with the scroll bar. When I scroll, it didn’t go to the month I wanted, instead it scroll to the end. Is there a way to adjust the scrolling?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3430)
    
    *   Hello Morni.. This happens as the file is a bit heavy. Here is the workaround. Click on the edge of the scroll bar and then remove the cursor from it. It will stop
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3665)
        
    *   Hello Morni.. This happens as the file is a bit heavy. Here is the workaround. Click on the edge of the scroll bar and then remove the cursor from it. It will stop
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3666)
        
603.  I LOVE this leave tracker and have tried to manipulate this form to track the services but can only enter 1 “letter” in a daily box.
    
    Do you have any type of excel form whereas you can still track the services each day but are able to add 2 or 3 codes in one box and it tallys it at the end based upon each client’s needs??
    
    For example, each client is given 100 units for Behavorial Health for either a 3, 6, 9 or 12 month period. As I enter the services daily, it will deduct from the available units till the next authorization period.
    
    Thanks,
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3429)
    
604.  Hi Submit, it is great to work with your template and my compliments for this tool! Only if I try to change the holiday list, as I am from Europe, I doesn’t succeed to change it. For instance, we don’t have the holiday 4th July. When I update the holiday list, it remains in the tracker. What am I doing wrong?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3413)
    
    *   Hey.. Since the holiday are in an excel table, you need to make sure you delete and replace the dates (and not delete the rows as that will delete the table as well)
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3452)
        
605.  HI Sumit, i want to use this for 100 employees, but i can not move the scroll bar down to add rows
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3411)
    
    *   To get the scroll bar down, right click on it and then drag it down. To add more employees, simply add employees and copy the formatting and formula.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3420)
        
    *   To get the scroll bar down, right click on it and then drag it down. To add more employees, simply add employees and copy the formatting and formula.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3448)
        
606.  Hello Sumit, great template!!! it is very useful! One question, I try to add a column to have the balance (deducting from the number of vacations they have for the year but the formula didn´t work. Could you help me with it?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3409)
    
    *   Hello Liza… Try this formula: =Total Leaves-SUM(NL8:NO8)-0.5\*NP8 (in cell NQ8 and copy for all the cells in NQ column).
        
        In the formula, replace ‘Total Leaves’ with the number of total leaves in your company.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3421)
        
    *   Hello Liza… Try this formula: =Total Leaves-SUM(NL8:NO8)-0.5\*NP8 (in cell NQ8 and copy for all the cells in NQ column).
        
        In the formula, replace ‘Total Leaves’ with the number of total leaves in your company.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3447)
        
607.  Hi Sumit. Love this especially as you can start the year anywhere. Great for us whose holiday year doesn’t run from Jan to Dec. One thing..Feb 29th doesn’t seem to show up for 2016
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3406)
    
    *   Hey Russ.. Glad you liked the template. I just tried and 29 Feb is showing in the template when 2016 is selected.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3422)
        
    *   Hey Russ.. Glad you liked the template. I just tried and 29 Feb is showing in the template when 2016 is selected.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3446)
        
608.  For some reason the days seem to be out by 1 (Jan 1st is showing as a Saturday when in fact is was a Friday – at least for me in the UK). How would I go about changing this?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3402)
    
    *   This only seems to be an issue when opening in Google Sheets (Dates are fine when opening in excel). The whole document however is not setup to work in Google Sheets.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3403)
        
        *   Hello Adam.. This won’t work in Google Sheet since this uses VBA as well
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3426)
            
        *   Hello Adam.. This won’t work in Google Sheet since this uses VBA as well. Also, for me it’s showing Friday on Jan 1.
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3444)
            
    *   Hello Adam.. For me it’s showing Friday on Jan 1.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3423)
        
609.  Hi, I also wanted to calculate shrinkage of the month for a team and also set a shrinkage limit. How do i do that?  
    Please explain.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3391)
    
610.  Hello Summit! Please can you reply to my email….please please…
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3389)
    
611.  Is there a way to set the Year to run from June to May instead of Calendar year
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3387)
    
    *   Hi Aaron. I’ve just done this. Just put June and the year in the boxes on the top left and it calculates 12 months from there.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3405)
        
612.  Hi Sumit.  
    The leave tracker is not working for me.  
    I have to maintain leave record of about 100 employees  
    As I had one column the other column will hide automatically and also the scroll bar will remain in middle of the page
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3384)
    
    *   Hello Shilpa.. To get the scroll bar down, right click on it and then drag it down. Also, when you insert a column, you need to make sure the formulas are intact. You can however, easily add more employees by adding more rows and copy paste the formulas and formatting.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3442)
        
        *   Thank You
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3457)
            
613.  Hi Sumit! So far you have assisted us with a most impressive and useful excel leave sheet and I have been searching for one for months now! Thank you for this!  
    I have managed to figured out how to move the scroll bar in the sheet. Unfortunatley on a few occasions it has completely messed up my leave sheet wtih the error message “run time error message 1004” and I have had to start from scratch…..I have no idea how to fix it.  
    Please can you assist me by;  
    Inserting colums with NAME/SURNAME/ SITE/ EMPLOYEE #/START DATE  
    Vacation leave – after each month have the vacation balance (this will make it easier to see what vacation leave balance they have at that month (however still leave the total vacation days as you have it too)  
    Is there a way to have a column with a leave amount that the staffmember has like at end June 2016 Mr x has 8days owing to him and so continue is this manner?
    
    I also need for the CASUAL LEAVE to be changed to CAME LATE (THIS SHOULD BE HIGHLIGHTED IN RED) BUT NO DEDUCTIONS SHOULD BE MADE
    
    ALSO, SOME STAFF WORK ON A SUNDAY AND GET A DAY OFF (CAN YOU INSERT A COLUMN FOR “O” OFF DAY?
    
    I also tried to update the calendar with our Holidays and it give me the run time error also.
    
    Friday 1 January 2016 – New Years Day  
    Mon 21 March 2016 – Human Rights Day  
    Friday 25 March 2016 – Good Friday  
    Monday 28 March 2016 – Family Day  
    Wed 27 April 2016 – Freedom Day  
    Sunday 1 May 2016 – Workers Day  
    Monday 2 May 2016 – “Public Holiday”  
    Thursday 16 June 2016 – Youth Day  
    Tuesday 9 August 2016 – National Women’s Day  
    Sat 24 September 2016 – Heritage Day  
    Friday 16 December 2016 – Day of Reconciliation  
    Sunday 25 December 2016 – Christmas Day  
    Monday 26 December 2016 – Day Of Goodwill  
    (if you add all these dates in, then I can just update it next year without any problem)
    
    Your assistance is much appreciated!!!!!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3380)
    
    *   Hello, adding columns to the tracker will mess with the formulas. If you need to add columns, I suggest you do it to the right of the tracker area. You can mark casual leaves by simply coloring the cell and not entering anything in it. Also, to change the holidays, simply delete the data in the holidays tab and add the days you want to show up as holidays. Make sure you don’t delete the rows, only the data.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3454)
        
614.  Is there a way to lounch filtering mode in the “Name” heading, I would like to filter just one employee at a time. Great template by the way.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3375)
    
615.  i want to join your class if you offer any classes plz let me know e-mail [sheikh\_imranz@yahoo.com](mailto:sheikh_imranz@yahoo.com)
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3373)
    
616.  super like bansal
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3372)
    
617.  Hi Mr. Sumit,  
    How can I remove half and causal day without damaging the formal in total leave for the month and year?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3371)
    
    *   Also, sir, is there a way that if i type “x” into the calendar then it wont count it towards a leave? (all of my employees have a different off days, therefore I am putting an “x” for there off days. The formula thinks it’s a leave).
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3374)
        
618.  hi all how to mark present
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3369)
    
619.  Hi sir in my company alternate saturday is OFF. How is possible to change that with your template
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3368)
    
620.  i want to add more employees in the sheet, but the scroll bar at the bottom to change the month does not move down, hence hindering my view of additional employees. how do i move the scroll bar further down the page?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3367)
    
621.  hi how do i change the year cycle from april 2016 to march 2017.?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3366)
    
622.  Hi Sumit, thank you for the awesome template. Just a qns, I would like to add in AM / PM half day leave into the templates so the sheet will reflect either a half day leave taken during the AM session of the day or half day leave taken in the afternoon session of the day.
    
    Can you guide me thru how to edit the formulas in the excel sheet? Thanks alot in advance for your reply !
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3359)
    
623.  Hello, is it possible to get 2 half leaves? Example – if Maternity leave is not needed can we replace by VAC Half day and still keep the other Half day as Personal Half day? I tried to copy the formula but it just links both cells. Thank you!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3348)
    
624.  Hi Sumit, Thank you for this excellent tool. But I have a tricky situation. I have added two more codes W(Work from home) and F(Comp Off). I dont want these to add up to the leaves for the month or the year. However I just need a count of the number of Work from Home and the Comp offs availed separatly for audit purposes. Can you help me here? Thanks in advance- Vasanth
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3345)
    
625.  Hi there, I have been looking for something like this for a very long time!! thank you” will the excel sheet still work if the employee holiday year starts at different months? they do not all start on the same month.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3337)
    
626.  Hi,  
    Sumit I love the excel leave tracker. But i need some changes in it so would u plese healp me for the same.  
    I want to change the colours of the Assigned leave for example consider as vacation(V) should be in dark green insted of red. And i also need the working days to split according from employee to employees as if now if we select the working days it applys to all employees so it should be split working days.Also its should show persent of absent days. Please help.  
    Thanks once again.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3331)
    
627.  Hi, This is so close to what I am looking for and tweaked it to add more number of employees. My organization has comp offs that I would like to capture too but they need to be counted as 0 (similar to H being counted as 0.5). How do I tweak to accomodate this.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3323)
    
628.  This was excellent! Thank you. Is there a way to change the colors of the time off. Sick day have own color, vacation own color etc?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3321)
    
629.  Hi, Is there any way to amend the formula so sick days and maternity days do not calculate as leave but can be recorded?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3318)
    
630.  Hi Sumit Bansal… i would like to modify your tracker but i have hard time understanding it.. hehehe
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3314)
    
631.  This is a great template! However there is a little glitch such that if i take leave on 1 Jan 2016, the same leave would appear every year for 1 Jan, please help 🙂
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3313)
    
632.  Hello 🙂 There is a little problem in the excel sheet. If i take sick leave on 2 Jan 2016, the same leave will appear in 2 Jan 2017 🙁 But anyway thanks for this excel sheet! It’s great!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3311)
    
633.  Dear Sumit,  
    its a great work,  
    but how can i add another columns, it change the date ?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3310)
    
634.  Dear Sumit,  
    I already key in in excel attendance but when i key in january why in february leave symbol still there
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3308)
    
635.  the tracker is amazing you did a great job!!!! I was wondereong if how can i change the years , I plan holidays following the uk financial year (from april to april) and need to ad 2017 months!!! will be possible show me how this can be done!!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3302)
    
636.  In addition to days taken, some employees take a couple of hours here and there and I would like to be able to track those hours. How can I change it to show hours taken as well?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3282)
    
637.  Another random bug I just discovered. I added a new column after Column A to allow for First Name and Last Name Columns of employees. This new column removes the first day of the first month in the calendar. Everything else seems to be fine (I did adjust the slider macro format control to leave that column from moving but that seems to be unrelated). All other cells, formulas, and conditional formatting adjust when I insert that new column except for January 1 or June 1 or whatever the first month is set at. Any ideas?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3278)
    
    *   (Did I mention how much a truly LOVE this workbook! Amazing job and thank you so much for making it and sharing it! Has REALLY helped my job)
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3279)
        
638.  I LOVE this tracker so much. So adaptable to my needs. Thanks for making it and thanks for having it unlocked and open. I have discovered one small bug that I cannot figure out how to fix. I changed the start month to June to coincide with our fiscal year (using the dropdown menu in A1) and the the year to 2015 so it goes June 2015-May 2016. It does not account for the leap year in February of this year. But when I have it set to the calendar year of 2016 (Jan-Dec) the leap year is there. I have been able to simply type “29” in the box where it should be and everything seems to work fine, but was wondering if that is causing any unseen issues that I haven’t noticed. Thanks again for such an amazing workbook template! Amazing!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3277)
    
639.  I LOVE this tracker so much. So adaptable to my needs. Thanks for making it and thanks for having it unlocked and open. I have discovered one small bug that I cannot figure out how to fix. I changed the start month to June to coincide with our fiscal year (using the dropdown menu in A1) and the the year to 2015 so it goes June 2015-May 2016. It does not account for the leap year in February of this year. But when I have it set to the calendar year of 2016 (Jan-Dec) the leap year is there. I have been able to simply type “29” in the box where it should be and everything seems to work fine, but was wondering if that is causing any unseen issues that I haven’t noticed. Thanks again for such an amazing workbook template! Amazing!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3276)
    
640.  Hi Sumit. Awesome work with the tracker. You have a breakup for the year, can you please advise how can I break up the leaves taken per month the same way. Secondly, how can I assign a different colour for different leave types?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3271)
    
    *   Changing the colors is super simple (I literally just did that to mine 5 mins ago). Go to Conditional Formatting > Manage Rules. Notice the rule for the Red and Yellow (those are the ones to pay attention to).For yellow (for example) it is only the half day. It looks at B8(don’t put $ in this piece) and compares that (or whatever date cell you are on) to $NT$6 (use the $ here) which is the code ‘H’ for half day listed in the small area on the top right of the worksheet listing codes. You can add more codes like this. Conditional Formatting > Manage Rules > ‘+’ > Style = ‘Classic’, Next drop down menu = ‘Use formula to determine which cells to format’. formula would look like ‘=B8=$NT$2. Custom Format – whatever color(s)/Fill(s) you want. Click OK. Change ‘Applies to’ to “‘Leave Tracker’!$B$8:$NI$25” which is the entire calendar piece. Make sure you then edit the current “Red” formula to remove the $NT$2 code in that formula (“=OR(B8=$NT$2, B8=$NT$3, etc). If you have one color for each code, you will remove that entire formula and just have one that looks like “=B8=$NT$x” for each code. Hope this isn’t too confusing.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3280)
        
641.  Hi Sumit! I’m having an issue with my template, when ever I highlight a cell in March 2016 as a Half Day (H) for example, it duplicates it in the other years (March 2015), and when we erase the duplicate, the original cell highlight disappears as well. Not sure how to fix this, any ideas?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3254)
    
642.  Hi, it seems problem when I edit the file and when I move the scroll bar, it show the table of mistake and say that “mircrosoft visual basic, run-time error”1004″, application defined or object defined error”” I have tried to download the file again to PC and again the same problem happened? How can I fix it? please help.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3253)
    
643.  can the half days be converted to hours?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3246)
    
644.  I locked A1 and A3 Cells and made it invisible so you cannot change. Now I use tracker to move between the months and it works so much better. Vacations are not copied to the other months. I could not post the new tweaked spreadsheet here unfortunately. Please help us add the department besides the employee name and then it would work like a charm. If anybody need my tweaked spreadsheet please send me an email.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3244)
    
    *   Hii Chavi,
        
        Please share your spreadsheet to [alikhansiraj1@gmail.com](mailto:alikhansiraj1@gmail.com)
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3245)
        
645.  Please add another column for department besides employee name (Sales, Marketing etc) and allow us to Filter by department or show by all department. It will be very useful. appreciate in advance.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3243)
    
646.  Hello Sir, could you please assist me with how to modify the Half Day calculation from 0.5 Day to 1 Day
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3240)
    
647.  Hello Sir, could you please assist me with how to modify the Half Day calculation from 0.5 Day to 1 Day
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3239)
    
648.  Dear Sumit, It’s been a while, How are you? Please i would like to know if i can i use this leave tracker template to track other hr functions? If yes, please how do i go about it?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3230)
    
649.  Hey Sumit! Thank for this amazing template. Is it possible to tweak this template to count weekends when it comes to vacation?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3226)
    
650.  Hi – I have 2 additional codes like half day which need to be 0.5 and then once it had added them up in total leaves this month and total leaves this year I need it to add 0.5 into these columns and not add 1 like it currently is. Can you help please.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3223)
    
651.  the leave tracker is great but i have an issue with this sheet.When you use S code or M Code or any other code for instant, on 15 of April was a sick leave the sheet records in all other months same date as sick leave instead on each month to be blank for you to input your records
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3221)
    
652.  Hi Sumit,
    
    Its a great template. Thanks. I need 2 different section with Half Casual and Half Sick leave. I could not formulate the template. Would appreciate it if you could help me. I need four different options : Annual Leave, Sick Leave, Half Sick, Casual Leave,Half Casual. I was not able to add formula to account another half day leave.
    
    Would be great if you could help.
    
    Thanks
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3217)
    
653.  The leave tracker is fantastic – many thanks. However, the horizontal scroll doesn’t appear to work very well. When I try to toggle from month to month, it starts off well, then slides to the end by itself, makin git hard to see specific months. Anybody else having this challenge?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3213)
    
654.  How can I add a quarter day. Any help would be appreciated
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3212)
    
655.  Hi Summit, that’s one of the best tracker i have seen so far, CONGRATS. but plss if i want to copy the template from one sheet to another in the same workbook, how do i do that please? i tried with some VBA code and it works but the scroll bar was unable to select the months. can you help please. it gives some runtime error
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3210)
    
656.  Hi Sumit, Wonderful progress !  
    I rebuild the leave tracker to learn but when it comes to the macro code it’s not working.
    
    B12: where the month number appears using a scroll bar
    
    H:NO is the year days columns range
    
    showcalendar()  
    SCHEDULE.Range(Columns(Range(“B12”).Value \* 37 – 35), Columns(Range(“B12”).Value \* 37 + 1)).Hidden = False  
    End Sub
    
    I’m trying to change the equation numbers but it’s not working .. Don’t hide columns or the correct ones .. can you give a hand !?
    
    Appreciate your help !
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3206)
    
    *   I can you help and let me know I change the years I need to add january 2017 and foward
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3303)
        
657.  Hello Sumit!
    
    I have downloaded the template, thank you very much for allowing free access to it, very helpful.
    
    However, when I try to move the scroll bar to change the month, it shows the Runtime error 1004 : application defined or object defined error. Why could it be so and can I do something to fix it? Thank you in advance!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3203)
    
658.  Hi Sumit, I think your template is excellent. I have some questions about some of the formulas, though, as I am far from an expert. I have been able to add extra holiday types, etc, but am struggling with the part where a sick day is added to the number of leave days per month and year. I have added a holiday entitlement column, also, which then works out how much leave is still available. However, I am struggling to workout for leave which taken in hours rather than a full day. Do you have any advice, please? Thanks, Deb
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3195)
    
659.  Thank you for your sharing! But i experienced one issue regarding entry leave code. The leave code wont change when i want to key another month. For example, employee one took annual leave on first April so i typed A on first April. However, the A will exist on first May when i change to another month. Do you have any advice about this? Appreciate if you can give me the solution. Thank.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3190)
    
660.  Hello, This excel template has the potential to be absolutely fantastic – thank you very much!
    
    I am just stuck on one thing though. I need to enter retroactive leave for the years of 2014 and 2015 to accurately check leave balances for staff in the present. I added in all of the relevant Holidays for 2014/2015/2016 into the \[Holidays\] worksheet.  
    I then changed the value in A2 to read ‘2014’. I then scrolled through the months and entered in the leave. However, when I change the A2 value to read ‘2015’ and then I scroll through the months to add leave for 2015, the leave I added for 2014 is still associated to those days.  
    Is there a way I can add in leave days for multiple years without it affecting each year’s data?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3186)
    
661.  Thanks a lot Sumit.. A great help.. 🙂 easy and helpful..
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3180)
    
662.  Thanks for sharing this! It’s sooooooooooooooooooooo helpful. God bless you.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3160)
    
663.  How do you create additional leave codes for full and half days?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3156)
    
664.  Thank you for the perfect leave tracker! I do have a question however. If i wanted to include a column next to “leaves this year” titled “vacation days taken”. How would I code that? Essential i want that total to include only vacation, half flex day and full flex day(i included the last one). Also, what formula would I use if I wanted to log only a half sick day taken?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3151)
    
665.  Hi Submit,
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3146)
    
    *   Is it possible to have have multiple leave types that are half day-0.5. For instance,i would like to include Sick-S as half day leave as well.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3147)
        
666.  Hi Sumit, the leave tracker is so awesome!. Could you please help me on counting the leave breakup every month beside the yearly summary?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3123)
    
    *   Hello Jade.. Glad you liked the tracker. If you want monthly breakup (instead of yearly), use the following formula in cell NL8 and copy paste in all the cell (NL8:NP17)
        
        \=SUMPRODUCT((OFFSET($A8,0,31\*($A$3-1)+1,1,31)””)\*((OFFSET($A$4,0,31\*($A$3-1)+1,1,31)))\*((OFFSET($A8,0,31\*($A$3-1)+1,1,31)””)))
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3140)
        
667.  Hi Sumit..can you help me to do this excel spreadsheet  
    in google excel? my company is using google excel.. Please assist thanks.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3112)
    
    *   Hello.. I am afraid I won’t be able to replicate it in Google Spreadsheets. While the formulas are almost the same in Excel and Google Sheets, VBA is exclusive to Excel.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3133)
        
668.  Hi I am still having problem with this excel work sheet when I put in  
    the V under dates and then switch to next month why am I seeing the V  
    for previous month, please help.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3108)
    
    *   Hi Tony, You have to use the left and right arrows on the scroll bar to move to the next month or the previous month.
        
        The month number is cell A1 is to give the user the flexibility to  
        change the lave year. For example, to have the year as Jan-Dec, make A1  
        value 1, for Apr-Mar, make it 4. . Once you have set leave year, you  
        need to use the scroll bar only to go to next/previous month.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3109)
        
669.  There is a bug in the month selection. A1 and A3 are both being used to determine the month, but they change independently. For example, if I scroll forward to March, A1 will stay static. If I then select the third month using A1, I am taken to June instead of March.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3106)
    
    *   Hello Andre.. The month number is cell A1 is to give the user the flexibility to change the lave year. For example, to have the year as Jan-Dec, make A1 value 1, for Apr-Mar, make it 4. . Once you have set leave year, you need to use the scroll bar only to go to next/previous month.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3107)
        
670.  Thank you Sumit, loved this tracker… it is very much user friendly. Since am very new to excel formulas, can we edit this sheet?  
    What we are looking for is like need to add something in the leave description section, Half Day (forenoon and afternoon) and also add some shift codes to use this leave tracker and as a shift tracker as well like (Morning(M), After noon(A) and Night (N). Really appreciate your help in this
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3081)
    
    *   Hello Austin.. The leave tracker only tracks the Half leave using the code H, but you can add comments if you like. However, you’ll need to stick to H as the leave code for half day
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3091)
        
        *   Thank you for the quick reply Sumit, as asked in earlier question can I add some codes for the shift as Morning(M), After noon(A) and Night (N) and these should not count as leave. Currently the formula is set like if hit any character, it counts as one day leave.
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3098)
            
            *   Hey Austin.. You can highlight the cells by filling it with a background color. That would not make it count as a leave and you can still make out the shift based on a color code.
                
                [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3101)
                
                *   Thanks a lot Sumit, that was a quick fix!!!
                    
671.  Hi Suimt, Thanks for the great tool, Is if possible for you to add Work From Home option and highlight with different color and give the total counts separately for the whole year.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3079)
    
    *   Hello Dinesh, as of now there is a provision for five types of leaves (sick, vacation, maternity, casual, and half leaves). You can change any of these with the leave code you want. For example, if you want W for work from home, replace the S with W in NL5 and NS2
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3090)
        
        *   Hello Sumit..I added additional column for Work from home this year(W) however i dont want work from home to be counted on Leaves this month and Leaves this year.could you please give me the formula for that.
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3102)
            
            *   If you want to highlight Work from home but don’t want to count it, a quick fix is to highlight the cell by filling it with a background color. That way’s it will be marked but not counted
                
                [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3130)
                
672.  Hi this is such a good and user friendly template. Thank you for creating it. Only problem I am having is when I book a holiday off for an employee, it comes up in the future years too. I only want it for that one year. How do we do that?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3078)
    
    *   Hello Krupa.. This tracker is made for one year only. If you want to have multiple years, you can create copies of it
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3089)
        
673.  Do need to add additional columns (need 3 before Name) without breaking the dates please.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3077)
    
    *   Managed to add the additional columns, using the dropbox link below in the comments.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3083)
        
        *   Hey Vivian.. Glad it worked.. I just saw your comments, but I guess you managed it before I could jump in 🙂
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3088)
            
        *   Hi Vivian !  
            Could you please help me with how to add more columns before Name using dropbox as you have already succeeded in the same.
            
            thanks.
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3242)
            
        *   Hi Vivian…..please help on the addition of more columns.
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8951)
            
674.  Hello, When I add a vacation day let’s say January 10th 2016 and then I want to change the month on the upper A1 case the vacation day (january 10th) appears on february 10th, march 10th and so on. How can I have the vacation day ony highlighted on january and not o the rest of the months? becasue it work when I change the month on the scrolling bar but not on the A1 (select month) case. thank you
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3075)
    
675.  Hi Sumit, One question when I add for example a vacation day for one employee let’s say January 2nd 2016 and I go on the top to select february or any month of the following year 2016 you can see the V from vacation on the 2nd of each months 2016. This happens only when I choose the month in cell A1 but when I scroll the moths it doesn’t happend how can I fix this?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3074)
    
    *   Hello Janine.. To change the months in a specified interval, only use the scroll bar. Cell A1 is to be used only when you want to change the year (let’s say from Jan- Dec to Apr-Mar). Once you have the desired year range, scroll bar should be used to go to next/previous months
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3087)
        
676.  Thanks for the amazing template Sumit. I saw that you have added an additional column and helped with the template, but it is very difficult to add extra columns I think. If there was some instructions to add columns to the template, it would make it so much easier. As, I wanted to add 3 columns before the Name column and adding them spoils the date formula. However, I appreciate your efforts in this and thank you for sharing the template. Please do consider making the adding of columns a little easier.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3073)
    
677.  Question: when I add employees, the months scroll bar remains in the same place. How to move the scroll bar down, or how to properly insert additional employees?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3069)
    
    *   Hello Gordana, Hold the Control key and left click on the scorll bar. Now you’ll be able to move it.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3086)
        
678.  awesome template!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3068)
    
679.  Still no response from you,,.Sumit……When protecting the sheet …scrollbar doesn’t work and also I have not locked or protected the cell link to scrollbar….pls help on this..
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3049)
    
    *   Please see my response in your comment above.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3055)
        
680.  Please advise how I can add further UK holidays to the table.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3048)
    
    *   You can add holidays in the table in the holidays tab
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3054)
        
681.  When I make an entry in one month why does those entries show up when I change months.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3047)
    
    *   Hello Tony.. You need to use the scroll bar to change the month. I believe you are using cell A1 as of now.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3053)
        
682.  Hello Sumit, really nice work! one comment. If I want add different holiday (for two countries) with different color to be displayed it is possible?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3027)
    
    *   Hello Jaro, you can do that. First you need to have the list of holidays somewhere in the workbook. A similar table as the one in the holidays tab. Then you need to add a conditional formatting formula to all the cells in the leave tracker.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3052)
        
        *   Thanks for reply Sumit. In conditional formatting I can see “HolidayListNamedRange” and worksheet with bank holiday are called Holiday  
            What exactly in code mean “HolidayListNamedRange” ?
            
            I want add couple holiday workseets (holiday\_US, holiday\_UK..) For all of new add new formatting with different colors.
            
            but where define different worksheets name?
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3070)
            
683.  Hello Sumit, First, I would like to say that the leave tracker which you have made is superb and very easy to use!
    
    I’m trying to customized base on requirement, and trying to use the same sheet as a shift tracker.  
    As part of this I need your support:  
    1) I’ve to put the log-in time of each employees when they are present. So, in column NJ (Leaves This Months) & in NK (Leaves This Year) should pull the total no. of days and ignore the cell were the log-in time is mentioned  
    .currently if we put the login time then it is getting added as leaves.  
    2) I’ve added three more column, which in NU, NV & NW this column will count the no. days he/she had login in particular region so that in end of the month it will be easy to calculate the shift allowance. for eg. if a person log-in at 12:15 3 days, then column NU (UK Login i.e 11:15 am to 8:30 PM) will show as 3 days.  
    It will be really helpful if you can help me in putting the formula to get the desire results,
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3025)
    
684.  When protecting the sheet …scrollbar doesn’t work and also I have not locked or protected the cell link to scrollbar….pls help on this..
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3019)
    
    *   Hi Sumit,  
        Awaiting your response…pls help on query.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3037)
        
        *   You need to make sure the cells that are dependent on the scroll bar are not protected. Simply protecting the entire sheet wont work
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3051)
            
685.  This is such a awesome tool! I tried to follow the thread below as I am trying enter additional leave codes for half days for vacation, sick and personal. Any idea on how I can accmplish this?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3010)
    
    *   Hello.. As of now I have made this for five leave codes. If you want to use more leave codes for full day leaves, you can simply enter the code in the leave tracker and it will count it as a leave. It would however not highlight it. As of now, you can only use h/H for half day leave.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3011)
        
        *   I understand but I was trying to get the half days to apply to the appropriate leave breakup, hence SH, VH, etc. Where is the tutorial I can download an updated version from?
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3012)
            
            *   You can download the updated version from the tutorial above. There is no video tutorial on this, just the template
                
                [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3050)
                
686.  why is it that when i select a day in one month it gets selected in all other months?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3007)
    
    *   Hello Henry.. I believe you are using the value in cell A1 to change the month. Instead use the scroll bar at the bottom.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3008)
        
687.  wonderful template.Please assist me with one issue.suppose i sel;ected Jan Month and entered the leave in the columns of the respective employees.and when i scroll for the next month i.e feb and try to add the leaves for the month,the leave balance for the Jan month is affected.whatever changes i try to make it happens for previous month too
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2992)
    
    *   Hello Neha.. When you use the scroll bar and change the month, column NJ shows leaves only for the selected month. So if you have 2 leaves in January, and you use the scroll bar to come to february, column NJ would show leaves of Feb only. However, Colunm NK tracks all the leaves in that year.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3002)
        
688.  Thanks Sumith, it realy works
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2991)
    
    *   Thanks Nilaksha 🙂
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3001)
        
689.  Thank you for this goog job. Seems there is an error in the sheet as when I enter the vacations for example in January then I move to Feb to enter another vacations, The vaction which I entered in Jan coming to Fenruary automatically! Can you please find whats the problem?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2989)
    
    *   Hello Abeer,, I believe you are changing the month value in cell A1. Instead, use the scroll bar to change the month.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3000)
        
690.  does the tracker only track fr one year i want to save the leaves for one year nd continue wth the nxt year is it possibble
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2986)
    
    *   Hello.. The tracker is made for 1 year for now. If you want to make it for multiple years, you can have create multiple copied for different years.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2999)
        
        *   thank you
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3015)
            
        *   Is it possible to do this within the same workbook?
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8824)
            
691.  Thanks for good tracker!
    
    When leaves are updated for Feb month ie 25 Feb, same leave codes are copied for other months as well which duplicates the work and same case for previous months ie Feb 2016 data is reflecting in Jan 2016.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2956)
    
    *   Hello Mahe.. Just want to make sure you are using the scroll bar to change the month (and not the month value in cell A1).
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2959)
        
        *   Yes, I was changing the month value….thanks will scroll to change the month…whether I can display the scroll bar vertically?
            
            Also in holiday list whether I can name it as public holiday and optional holiday for each month with color code to view in main.sheet?
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2981)
            
            *   You can make the scroll bar vertical. Hold the Control key and left click on the scroll bar. You will see an outline on the scrollbar. Then you can resize and make it vertical.
                
                As of now, there is no way to classify holidays in the tracker
                
                [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2998)
                
692.  After finishing the tracker for a month, when I change the month in column A1 the holidays do not wipe out. If I delete them, then the entire spreadsheet becomes zero. Is there a fix?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2953)
    
    *   Hello Kathryn.. To change the month, use the scroll bar at the bottom. As you click on the scroll bar, the months would change and the leave record would remain intact.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2958)
        
        *   The holiday cells are staying highlighted no matter what the month is. I’ve saved the doc as a xlms – but it’s still not working properly 🙁
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2976)
            
            *   If you don’t want the holidays to get highlighted, you can remove these by deleting the holidays data from the Holidays Tab.
                
                [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2977)
                
693.  When I change the month ont he column A1 after finishing the tracker for a month. The holidays do not wipe out, if I delete them then the entire thing becomes zero. Is there a fix?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2952)
    
694.  I am so happy that I found this template and downloaded it immediately. But, when I marked “C” casual leave for one of the employees on a date, let say 10th of February. All other months are marked with C on the 10th! I am very confused here, please help!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2939)
    
    *   That’s what happened with mine! I am hoping I will get a response soon as it is a really helpful template other than that small glitch!
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2944)
        
        *   Hello Heather.. To change the month in the leave tracker, you need to use the scroll bar. Don’t use the value in cell A1 to change months (it’s just to specify the time period for the leave tracker)
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2961)
            
    *   Hello Sharon.. To change the month in the leave tracker, you need to use the scroll bar. Don’t use the value in cell A1 to change months (it’s just to specify the time period for the leave tracker)
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2960)
        
        *   The control bar is not going to the next month, hard to control. Is there a way to make it more responsive? And, sometimes the entire spreadsheet was highlighted and hang there. Hoping for your help soon.
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3067)
            
            *   Hey Sharon.. A lot also depends on the computers configuration. Scroll Bar tend to just keep scrolling if you are using a machine is less memory. It seems to work fine a multiple machines I tried
                
                [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3085)
                
695.  Is there a way to create more than one half days, say for sick leave or casual leave
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2935)
    
696.  For some reason, every time I enter a day in april it reflects on all the other days. How can I change that? For example I put a V day in april, and when I went to the next month it showed up on that as well.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2930)
    
    *   Hello Sahar.. To change the month in the leave tracker, you need to use the scroll bar. Don’t use the value in cell A1 to change months (it’s just to specify the time period for the leave tracker)
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2962)
        
697.  This is very wonderful. My question is about the maximum number of leaves allowed.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2928)
    
698.  Hi, great tracker although I am a little confused – when i put in a day off / vacation / sick leave etc. and I change the month it then has it on every single month not just the one I placed it in!? Help would be great!  
    Thanks
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2920)
    
    *   Hello Heather.. Kindly use the scroll bar to change the month value. I believe you are changing the value in A1.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2963)
        
699.  Hi Sumit This is Great Thank you. 🙂
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2891)
    
    *   Having started to use it, I have a suggestion for you.  
        It would be nice if the working days changes as per employee as I manage a company with staff working on different days. Wondering if that is a possible tweak?
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2892)
        
        *   Hello Ramya.. If you have different employees working on different days, You can create different versions of this tracker. To have it all in the same tracker will complicate it a lot.
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2907)
            
        *   Thanks for commenting Ramya.. Glad you liked it.  
            If you have different employees working on different days, You can create different versions of this tracker. To have it all in the same tracker might complicate it a lot.
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2908)
            
700.  This tracker is impressive, I can see a lot of use in the future. I do have a little request for you.  
    Is there some way to easily change the totals at the end of the row to equal hours instead of days?  
    Example:  
    Sick Leave = 8 hours  
    Vacation = 8 hours  
    Half Day = 4 hours  
    (or if someone happens to leave for an appointment)  
    Appointment = 2 hours  
    and in the final column have a calculation that would take those hours and give a total amount of days?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2890)
    
    *   Hello Kris.. You can achieve that by multiplying the leave count with the number of working hours in a day. For example, if the total leaves for a month is 2, then hours could be 2\*8 (considering an eight hour work day)
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2909)
        
        *   Hello Sumit, First of all, your tracker is amazing. I have been trying to modify the formula by multiplying the leave count by 8 and I keep getting an error message. Any suggestions
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3184)
            
701.  Is there a way to account for Lieu days? I am trying to insert a formula but it is counting as a day away.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2889)
    
    *   Hello Jewels.. Currently there is no way to account for lieu days. You can have the Lieu days in a separate cell for each employee and add it to the total leave count if you want
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2910)
        
        *   Thank-you very much Sumit, I love the tracker. It is extremely user friendly.
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2957)
            
702.  Hi, Would it be possible to edit this so standard year is 01/04 to 31/03?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2887)
    
    *   I have updated the tracker and now you can select the starting month (for example Apr 2016-Mar 2017). You can download the new tracker from the link in the tutorial.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2911)
        
703.  hi, could you help me with this the same format yet the month will be Jul to dec only and it be starting on column 2
    
    this is a great help.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2886)
    
    *   Hello faye.. I have updated the tracker and now you can select the starting month (for example July 2016-June 2017). You can download the new tracker from the link in the tutorial.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2912)
        
704.  hi.. loved it…….. want to know if there is a way to get total of the codes at month end.. like total number of sick days…. or V days…
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2882)
    
    *   Hello Elizabeth.. I have updated the tracker and now you can get the leave break-up by leave type. You can download the updated tracker from the link in the tutorial.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2913)
        
705.  Hello Sumit, how have you been? Have a thing or two l would like you to help me out with. In my company, we do not take out sick leave from a staff leave schedule. would like to know how l can use the (S) sick leave with out it being deducted from the staff leave
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2856)
    
    *   Hello Liz.. I’ve been good.. Nice to see you again. For marking sick leave but not counting it, a better way would be to simply highlight the cell with a background color, but not enter anything in it. That way it will be marked and wouldn’t be counted in the total leave count.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2860)
        
    *   Hello Liz.. An easy way would be highlight the sick days (using fill cell), but not enter any leave code. That way, it will not count it in total leave count
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2914)
        
706.  Hi Sumit, this template really helped me. I need a small change would you be able to show the leaves separately.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2854)
    
    *   Hello Malsha.. I have updated the tracker and now you can get the leave break-up by leave type. You can download the updated tracker from the link in the tutorial.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2915)
        
        *   Thanks a bunch 🙂
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2917)
            
        *   Thanks a bunch 🙂
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2918)
            
        *   Thanks a bunch 🙂
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2919)
            
707.  Wow! fantastic.Thank you for this template .Can you create an Excel sheet whereby sheet one is able to update other sheets in the same work book .If so please let us get in touch through skype
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2852)
    
    *   Hello Sebastian.. It can be done but by interlinking cells across sheets. Kindly let me know what you are looking for, and I’ll try my best to guide you
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2861)
        
708.  The leave tracker is the closest I’ve seen to what I am looking for. I am trying to create an employee time tracker spreadsheet that will record working hours, calculate overtime hours based on a 40 hour work week, sick time, and vacation time. I want this spreadsheet by pay period with the ability to record a portion of day vacation/sick and portion of day working. This is where I am running into difficulty. Ideally this spreadsheet would provide a pay period summary for each employee for the following; hours worked, vacation hours taken, sick hours, and overtime hours, as well as a yearly summary for managers showing total sick time taken/remaining, vacation time taken/remaining, etc.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2846)
    
    *   Hello Lori.. Have a look at the Timesheet calculator template here: [http://trumpexcel.com/2015/07/employee-timesheet-calculator-template/](http://trumpexcel.com/2015/07/employee-timesheet-calculator-template/)
        
        Hope this helps
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2862)
        
709.  Is it possible to have the total separately? like annual paid leave is separated from sick leave on the calculation?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2831)
    
    *   Hello Mar, if you don’t want the total count to include sick leaves, it would be best to highlight sick leaves with a background color, but not insert any alphabet code in it. That way the total leave count wouldn’t have the sick leave count in it.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2863)
        
    *   Hello Mar.. One easy way to do this would be to highlight sick leaves with a background color, but not enter any code in the cell. That ways, it wouldn’t be counted in the total
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2869)
        
710.  Hi Sumit, I have a few specific changes that I am trying to make to the sheet. Would it be possible for me to send this to you over email so that i can explain it well. I can then post a summary on the comments section for everyone else.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2827)
    
    *   Hello Krutika.. You can send me via email and I’ll try my best to help
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2864)
        
711.  I really like this tracker, any ideas on how I would go about setting up an automated system for personal and sick time accrual so i dont have to go in each month and do it manually?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2826)
    
712.  How could you change this to be a jul 1 – jun 30 fiscal year?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2820)
    
    *   Hello Carolyn.. As of now I have created it for Jan-Dec.. Will soon create one for custom periods and share here with you
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2865)
        
713.  I would like to amend the sumproduct formula in NJ to exclude a all leave codes except annual leave and half days so they do not get counted. All other leave is recorded but does not need to be counted. I have tried to get to grips with this formula, but am finding it difficult. Also if I click on any cell in NJ, click in the formula bar and hit enter, it comes up with #value! even though I have made no changes. Can you please break your formula down so I can try to amend it. I have never used sumproduct before.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2818)
    
    *   I had a Eureka moment. I changed the “” to =$nn$3 and it has worked. However, if I needed to include other leave types, I would not know how to accomplish that.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2819)
        
        *   Hello Dawn.. there are five types of leave codes already.. if you need to have more, simply use any alphabet code. As soon as you enter any code, it will be counted as one.
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2866)
            
    *   Hi Dawn,
        
        I have the same question. I don’t want Sick day to count as Annual Leave. How did you figure it out? Thanks
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-11175)
        
714.  Hello Sumit, can’t tell you how grateful l am, l have downloaded it through the link and l have gotten what l wanted. Thank you so much 🙂
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2811)
    
    *   Welcome Liz.. Glad I could help 🙂
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2812)
        
715.  For instance, an employee takes two days in January and five days in February, l don’t get to see the total seven days when am on February, l only see the 5day in february and when l go to January l see the 2day.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2809)
    
716.  Hi Sumit, l have downloaded the template again and it still calculates how many days taken per month, it still does not summarize the whole days being taken as the months go by.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2808)
    
    *   Hey Liz.. Maybe it’s the cache issue in your browser.. Here is the direct download link – [https://www.dropbox.com/s/8tv8rgeyrna70pg/Excel-Leave-Tracker-2016-TrumpExcel\_v3.xlsm?dl=0](https://www.dropbox.com/s/8tv8rgeyrna70pg/Excel-Leave-Tracker-2016-TrumpExcel_v3.xlsm?dl=0)
        
        This would show you monthly as well as total leaves taken so far.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2810)
        
717.  Hello. Does this allow one input the total number of leave days allowable and also track the number of leave days outstanding for an employee?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2787)
    
    *   Hello Chido.. I have updated the template so now it will also show the leaves availed in the entire year. This would be helpful in knowing how many leaves can still be availed by each employee
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2791)
        
        *   Thanks so much. This is so nice.
            
            If you could include 2 more columns to show “Allowable Leave Days” and “Leave days balance”, it would be great.
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2814)
            
        *   Thanks Sumit.  
            Kindly make provisions for total leave days allowable as well and leave days balance if its possible.
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2816)
            
718.  Hello Sumit, thanks for leave tracker, l have figured out how to change the holidays to the ones we observe but still wish l can get the leaves taken calculate totally as the months go by rather than the monthly calculations we already have
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2785)
    
    *   Hello Liz.. I have updated the template and now you can get total leaves as well (availed so far in all the months). Kindly download the template again
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2792)
        
719.  This is awesome, thanks! Is there a way to ‘select working days’ for each employee? Also, is there a way to change the “leave code” highlight color from red to a different color for each? I’d like to color code the leave days. Thanks again!!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2783)
    
    *   Hello Lynnae.. It wouldn’t be possible to have different working days for different employees.. You can however, change the color codes by changing the conditional formatting setting
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2793)
        
        *   Sumit could you please explain how? I’ve added a leave code and want to assign a colour to it but can’t and every leave code is coming up red. Your spreadsheet is amazing btw.
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3718)
            
720.  and by the way this is just awesome!!!!! You save me heaps of time
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2780)
    
    *   Glad it’s making a difference 🙂
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2795)
        
        *   You are just awesome! Thanks mate!
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2995)
            
721.  Hi Sumit,
    
    How can I have the total Leaves for the entire year?
    
    Thanks
    
    Jet
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2779)
    
    *   Hello Jet.. Thanks for dropping by and commenting.. I have updated the template so now you can get total leaves for the entire year as well. Kindly download the template again from the link in the article.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2794)
        
722.  Thanks for the Employee Leave Tracker Template – Can it be customised to include more leave variation like Working from Home but not calculate those days in the # of leaves column
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2778)
    
723.  Hello Sumit, l like the planner but here in Nigeria our holidays are different from yours so how do l cancel the holidays that we in Nigeria don’t have and also change the orange colour on those days so it can reflect as normal days?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2773)
    
    *   Hello Liz, you can change the holidays in the Holidays tab.. There is a table with dates. Just change it the ones that you follow. The tracker would automatically show the orange color for only the ones that you have specified as holidays
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2796)
        
724.  oh, I figured it out myself, its how you save it. clever me!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2771)
    
725.  Hi, when I use the slidebar to change the months, the dates are only showing for the first month January, not any other months- what am I doing wrong please- there is a pop up message about macros disabled, how to I enable them, I am a novice sorry.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2770)
    
726.  Hi, thanks for an awesome tool. Would it be at all possible to add a table where each employee’s types of leave are shown as a sub-total then also show a total? It will give an overview of all the leave taken.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2768)
    
    *   Hello Astroud.. I have updated the template so now you can get total leaves for the entire year as well. Kindly download the template again from the link in the article.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2797)
        
        *   Hi Sumit, thank you for that, much appreciated.
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2803)
            
727.  Hi There, Is there any chance I could change this from April 2016 – March 2017 as that is when our next leave year runs! Thanks!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2765)
    
728.  Hi Sumit. I would like to add the employee ID and department before the name but when i do so the formula eliminates the first 2 days of the month. Please help 🙂
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2748)
    
    *   Hello Farah.. You can download the file from this link., I have added an additional column for Employee id in it – [https://www.dropbox.com/s/qsubvcfounytzqn/Excel-Leave-Tracker-2016-TrumpExcel%20Additional%20Column.xlsm?dl=0](https://www.dropbox.com/s/qsubvcfounytzqn/Excel-Leave-Tracker-2016-TrumpExcel%20Additional%20Column.xlsm?dl=0)
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2750)
        
729.  hi when the same sheet is uploaded for spreadsheet the scrol bar and months are not visible any help on this matter
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2746)
    
    *   Hello Naveen.. What do you mean when you say “uploaded for spreadsheet”?
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2751)
        
730.  the issue I have with the half day is that it doesn’t seem to allow the user to input they type of leave that is being utilized…..just records that a half day of “leave” was taken. also, I would like to see a summary of each employees’ type of leave that has been used as opposed to the sum of all leave for example, 3 days sick, 1.5 days vacation, 2 days compensatory.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2742)
    
731.  Hello All,
    
    Our employees work one week in the whole, so I don’t record the PTO used until the week after it has been used. When I opened up the sheet today, the only dates in January showing were from the 11th (today’s date) through the end of the month). Is there a way for the entire sheet to show for the entire month and thereafter??
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2736)
    
    *   Hello Kelli.. The template shows the dates for the entire month. You can use the scrollbar to change the months.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2752)
        
732.  hi sumit. leave tracker updated is really great and helpful . please let me know how to add column before emp name .. i want to add emp id column however while doing so the whole sheet gets messed .. Please help
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2735)
    
    *   Hello Reenu.. You can download the file from the link below. I have added an additional column for employee id – [https://www.dropbox.com/s/qsubvcfounytzqn/Excel-Leave-Tracker-2016-TrumpExcel%20Additional%20Column.xlsm?dl=0](https://www.dropbox.com/s/qsubvcfounytzqn/Excel-Leave-Tracker-2016-TrumpExcel%20Additional%20Column.xlsm?dl=0)
        .
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2753)
        
733.  Great spreadsheet Sumit. Is there an easy way to use this sheet to track days my employees are late, be great to have that total in a separate total Column?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2727)
    
    *   Hello Jamie. You can use this formula in cell NK (and drag for all the remaining cells). =COUNTIF(B8:NI8,”L”)
        
        Now when you enter ‘L’ (for Late) in any of the cells, it will be counted.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2754)
        
734.  How could I put actual hours in here and have it add them up also I tried to add a column B for the employee id and it skews the January date to start with 2. I found where to change it to hide from C in the Macro.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2726)
    
    *   Hello Dale.. If you are looking to add an additional column, try the file from this link – [https://www.dropbox.com/s/qsubvcfounytzqn/Excel-Leave-Tracker-2016-TrumpExcel%20Additional%20Column.xlsm?dl=0](https://www.dropbox.com/s/qsubvcfounytzqn/Excel-Leave-Tracker-2016-TrumpExcel%20Additional%20Column.xlsm?dl=0)
        
        I have added a column for employee id
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2755)
        
        *   Thank You for the update.
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2764)
            
735.  In the formula mention to Sheet 3 but there is no Sheet 3 or i was missing while i downloading, pls explain, it is very helpful for me
    
    Thx
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2723)
    
    *   Glad you are find this helpful.. Sheet 3 is hidden. You can make it visible by right clicking on any of the tabs and selecting unhide. It will show a box with Sheet 3 in it. Select it and click on OK
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2725)
        
        *   Hi Mr. Sumit  
            Thanks for the sheet 3 purpose but i have 3 more Questions  
            – What if i’d like to adjust date of the month start from 21.Dec.2015 to 20.Jan.2016 (For 1 month)  
            – Change Leave code  
            – Add Holiday
            
            is it able to adjust?
            
            Thank you 🙂
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2729)
            
            *   – Changing month start and end date would be difficult.  
                – You can change the leave codes in cells NN2 to NN6. The tracker, however can track any code you enter in it.  
                – You can easily add holidays in the table in the holidays tab.
                
                [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2756)
                
736.  Hi, wondering if there is a way to change the position of the scroll bar, after adding more employees?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2722)
    
    *   Hello Chelle.. You can right click on the scroll bar and then move it like any other object. In case you wish to add more employees, here is the same leave trackers for 100 employees – [https://www.dropbox.com/s/ydyl3nltqk08a6v/Excel-Leave-Tracker-2016-100Employees-TrumpExcel.xlsm?dl=0](https://www.dropbox.com/s/ydyl3nltqk08a6v/Excel-Leave-Tracker-2016-100Employees-TrumpExcel.xlsm?dl=0)
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2724)
        
737.  Love this leave tracker but having some issues. When I scroll to Feb, March, etc… all the calendar dates disappear. January is beautifully labeled 01, 02, 03, etc… However, when I choose a different month there is no data in row 5. There is a formula but the cells in row 5 are blank.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2717)
    
    *   Thanks for commenting Al.. Since this workbook contain a macro, you need to enable the macros in it. When you open the workbook, you would see a yellow button that says -‘enable content’. Once you click on it, the tracker should work. I just checked it on my system and seems to be working fine.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2718)
        
738.  hi! how do i add a column to the right of “employee” to say something like “title” or “time zone” without messing up the entire formula?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2711)
    
    *   Hello Rachel.. Here is a template where I have added an additional column to the right of Employee Name Column [https://www.dropbox.com/s/qsubvcfounytzqn/Excel-Leave-Tracker-2016-TrumpExcel%20Additional%20Column.xlsm?dl=0](https://www.dropbox.com/s/qsubvcfounytzqn/Excel-Leave-Tracker-2016-TrumpExcel%20Additional%20Column.xlsm?dl=0)
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2798)
        
739.  Hi, can you please help me creating a dashboard sheet where we can get total leaves of each employee
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2700)
    
    *   Hi Sumit,  
        Can you please help me in creating a dashboard where I can get total leaves of each employee. Please do need full help.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2713)
        
        *   Hello Suma.. I have updated the template and now you can get the total number of leaves as well. Kindly download the template again using the link in the tutorial.
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2799)
            
740.  Hi Sumit, when I tried making amendments to formula such as changing “=SUMPRODUCT((OFFSET($A8,0,31\*($A$3-1)+1,1,31)””)\*(IF(OFFSET($A8,0,31\*($A$3-1)+1,1,31)=$NN$6,0.5,1)\*(OFFSET($A$4,0,31\*($A$3-1)+1,1,31))))” to “=SUMPRODUCT((OFFSET($A8,0,31\*($A$3-1)+1,1,31)””)\*(IF(OFFSET($A8,0,31\*($A$3-1)+1,1,31)=$NN$5,0.5,1)\*(OFFSET($A$4,0,31\*($A$3-1)+1,1,31))))”  
    The $NN$5 causes the formual to display #Value . Urgently need help
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2698)
    
741.  Hi! Will it be possible to track the no. of SL and VL separately minus from SL and VL credits for a year?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2697)
    
742.  Couple of questions. Will the sheet keep a running total the time taken off for every employee (For example, so you can see in May how much time was taken?) If I revert the sheet to a google doc with the formulas transfer?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2696)
    
    *   Hi Please! How can I include Half day Vacation and Half Day Sick leave?
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2714)
        
        *   Hello Maria.. You can record half leaves by using the code H. Half day leaves are highlighted in yellow, while full day leaves are highlighted in red.
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2716)
            
    *   Hello Jennifer.. It keeps a track of all the leaves taken in the entire year for all the employees. So if you mark the leaves for May, it will show the total for May. If you then mark the leaves for June, it will show the total for June, however, if you go back to May, it will have the leaves for May as well.
        
        I haven’t checked this on Google Doc, but I feel this wont work in Google Docs.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2715)
        
743.  Sumit, I really like the lay out and ease of use of the spreadsheet, the only component that I am missing is the ability to see the yearly total of vacation days used and be able to subtract it from each employees yearly vacation accrual. This would then allow me to see what vacation total for the year has been used and what is remaining. Just curious if there is a way I can add these functions. If you have any tips on how it would be greatly appreciated.  
    Thanks
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2688)
    
    *   Hello Kacey.. I have updated the template and now you can get the total number of leaves as well. Kindly download the template again using the link in the tutorial.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2800)
        
744.  Amazing! So helpful
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2686)
    
    *   Thanks for commenting Kiran.. Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2801)
        
745.  This is great! I am trying to modify it to calculate the amount of PTO a given employee has remaining, as well as to count the number of days off that the employee takes without pay. Any suggestions??
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2684)
    
    *   Hello Kelli.. I have updated the template and now you can get the total number of leaves as well. Kindly download the template again using the link in the tutorial.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2802)
        
        *   Great! Thank you very much! this template is excellent!
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2813)
            
746.  Hi Sumit.  
    How can I make some of the leave types not countable? Or is there a way to get totals of each type of leave in a separate column? rather then counting all the leave together?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2683)
    
    *   It will be good and useful if Sumit can do this
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2701)
        
        *   hello Darren.. I have updated the template and now you can get the total number of leaves taken so far (along with the monthly leaves). Hope this helps
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2804)
            
747.  Hi Sumit,
    
    Thanks a ton for sharing the excel sheet. It has helped me in sorting out the employee leave details to a great extent.  
    Just one request: Can you please share the formula to include weekends (Saturday and Sunday) under “# of Leaves” column. In my company, we don’t have a weekend system in place and rather have weekly offs for employees.  
    Looking forward to a favorable response from your end.  
    Regards
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2654)
    
    *   Hello.. I have updated the template and now you can select the what days are working and what are not. Kindly download the template from the link in the tutorial.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2805)
        
748.  Hi Sumit
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2653)
    
749.  Is there a way to lock the worksheet but keep the scroll bar functionality? When I protect the sheet the scroll bar no longer works! I have Unlocked the scroll bar, as well as, the Cell A3. After I protect the sheet and try to use the scroll bar the debug note comes up.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2645)
    
750.  Hi, love this, is there a way to track the sick days annually? The way our company works employees get 3 per fiscal year. Also, this may be a stretch, is there a way once the employee reaches their three days that their row can be filled in a certain color? Thank you!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2643)
    
    *   Is there a way to lock the worksheet? When I lock the Worksheet the Scroll Bar stops working!
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2644)
        
751.  Great Leave Tracker… Quick question — how can I add 2016 in the same calendar?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2629)
    
    *   Hello Brian.. I have updated the tracker for 2016. You can download it from the tutorial above
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2679)
        
752.  Hi Sumit. How can I capture if an employee takes half day leave?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2616)
    
    *   I have updated the Template. now you can record half day leaves as well
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2678)
        
753.  Your Excel file is gorgeous. Only one thing is missing, could you give me a hint on how to sum all the leave DAY of the year ? we have 20 days each years, would be nice to undestand how many days are left month by month in a column near the day for each month
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2612)
    
    *   Hello Riccardo.. I have updated the template and now you can get the total number of leaves as well. Kindly download the template again using the link in the tutorial.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2806)
        
754.  hi sumit,  
    the leave tracker is great, however i would like to gray out fri and sat as the weekends as these are the weekends in UAE.  
    how can you help me with this ?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2605)
    
    *   Hello Amrita.. I have updated the Template. Now you can select weekends from the list. You can download the updated template from the tutorial above
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2677)
        
755.  Within my office, many of the employees have different start and end dates for their contracts (which roll-over 6 months at a time). Using this template, is there a way to calculate the number of days of annual leave they have taken only within their current contracted 6 months.  
    For example: For Person 1 – I would need to know how many days they had taken between January 28th and June 28th. But for someone else this might be March 28th – September 28th.  
    I understand I could calculate this by editing the formula =COUNTA($B8:$NI8), but I would have to allocate these for each employee. Is there a way to change the formula so that I could input Start & End dates for each persons contract somewhere else, and the COUNT formula would then use the information in these cells to count within the appropriate range of dates?
    
    From here I have no problem calculating remaining days. It’s just calculating individual contracts that is causing issues.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2578)
    
    *   Sorry! Also is it possible to add an option for a ‘half day’ of annual leave, rather than a full one.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2579)
        
        *   Hello Luke.. I have updated the template and now you can add half day leaves
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2676)
            
756.  Hi, do you know how to clear contents whenever you change the year? For instance January 2015 -December 2015 cell values will be remove when you plan your schedule for January 2016 -December 2016
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2577)
    
    *   Hello Desmond.. The easiest way would be to download this again and change the year. You can also do this manually by going to each month and deleting all the records,
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2675)
        
757.  Your Excel worksheet is great, but I need help on also including the weekends as part of the # of leaves total. How can I add the weekend as part of the total # of leaves?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2570)
    
    *   Hello Rod.. I have updated the template so you can select what days are working days and which ones are not. Kindly download using the link in the tutorial above.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2807)
        
758.  This is amazing – do you have a 2016 version too?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2561)
    
    *   Thanks for commenting Sandy. If you change the value in cell A2 to 2016, it will become the leave tracker for 2016. You will need to update the holidays for 2016 though.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2562)
        
        *   You legend – thank you!
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2563)
            
        *   how about if I need to add half day and sick leave and don’t want that to be counted in the last tab , what should I do to solve that issue . there is one more cant add any other column or row coz it shift everything , any help .
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2611)
            
759.  2016 Version Release soon?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2558)
    
    *   Hey Alan.. Just Enter 2016 in cell A2 and you will have it. You would have to add the holidays for 2016 though.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2559)
        
760.  I just discovered the leave tracker and it is great. planning ot use it for 2016. i need to do a bit of edit though. Appreciate your help. I need the value in NK8 to be updated every month. that is reduce the leaves taken
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2547)
    
761.  I am not in the winner list 🙁
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2546)
    
762.  Hi,
    
    How to move the scroll bar to next cell.. has employee are more than count 10
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2544)
    
    *   Thanks for commenting Rakesh.. To get the scroll bar down, right click on it and then drag it down. To add more employees, simply add employees and copy the formatting and formula. I did it for you here (can have up to 40 employees) – [https://www.dropbox.com/s/qsfyo70kyf1ugvh/Excel-Leave-Tracker-40Rows-TrumpExcel.xlsm?dl=0](https://www.dropbox.com/s/qsfyo70kyf1ugvh/Excel-Leave-Tracker-40Rows-TrumpExcel.xlsm?dl=0)
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2545)
        
        *   Hi Sumit! i would like to use this template for 100 employees where all days are working days… I also want to insert more columns where I can put the employees position, hire date, etc. Hope you could help me. Thank you so much.
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8695)
            
763.  How can we have half day leave recorded in the templet?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2543)
    
    *   I have updated the Template. Now you can enter Half Day leave by typing the code H. It will be counted as 0.5
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2674)
        
        *   hi sumit! where is the formula for 1 day leave? i would like to remove 0.5
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-8694)
            
764.  u made an excel template for time and matrix one, the entry in one excel automatically refelcted in time matrix page. i do have special requirements regarding that sort or type can make it
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2524)
    
765.  hi sumit  
    i watched ur videos found interesting  
    the stuff like this im being waiting let me check out  
    all tutorials are really short and effective
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2523)
    
766.  This is amazing – I am trying to edit it so that I can use it for 2016 – 2017 – I already have the holiday for both years applicable to the company. Any pointers to do this?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2522)
    
767.  Thanks a lot Sumit for this wonderful tool. !! Need your help with one customisation though. My team has members from different countries and their holiday calendars vary accordingly. Can I insert additional holiday sheets and with different colour codes? Your guidance will be much appreciated.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2507)
    
768.  I love this tracker and would like to use it however, although I can get by in excel I’m by no means an expert. I need this to run from April to March but although I can change the months easily enough, the days don’t correspond though. Does anyone know how to adjust this?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2490)
    
    *   Hi Nicole, there is a similar tool available here which allows you to vary the dates of the vacation year: [http://excel-macros.co.uk/free-excel-tool-for-recording-and-tracking-employee-vacations/](http://excel-macros.co.uk/free-excel-tool-for-recording-and-tracking-employee-vacations/)
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2514)
        
        *   Thanks Phil, think I’ll be using that one now. 🙂
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2541)
            
769.  Eres un Maestro. Agradezco tu tiempo y el que compartas tus trabajos.  
    Por favor,¿cómo pudiera generar desde Septiembre de 2015 a Agosto de 2016?  
    Lo intente de varias maneras pero me sale error, Gracias!!!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2429)
    
770.  can i change the weekend? cuz i still work on saturday
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2414)
    
    *   I have updated the Template. Now you can select weekends from the list. You can download the updated template from the tutorial above
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2673)
        
771.  how do you edit the weekends days? here in the middle east, we usually have fridays & saturdays as weekends.. thanks.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2413)
    
    *   Hello Marvin. I have updated the Template. Now you can select weekends from the list. You can download the updated template from the tutorial above
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2672)
        
772.  Its a fabulous software. Friends #Leave Monitor is also providing the same kind of software. Experience it really you will like it also. Click here: [https://www.leavemonitor.com/](https://www.leavemonitor.com/)
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2367)
    
773.  Could you please change the weekend days to be Sunday?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2357)
    
    *   Hello Anjali.. I have updated the leave tracker template. Now you can select the weekends
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2671)
        
774.  This was really helpful!! Thankyou!:)
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2302)
    
    *   Thanks for dropping by and commenting.. Glad you liked the template 🙂
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2305)
        
775.  Hi, great share. Is there a way where I could have an additional code to sum the total number of lets say “Sick Leave” for Employee 1 and etc?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2294)
    
    *   in addition, how do we adjust the weekdays? Since we have working days from Monday till Saturday. So the only day off is on a Sunday
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2295)
        
        *   Hello Asha.. I have updated the template. Now you can select what days are working and which ones are not
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2790)
            
776.  Nice one, Sumit.
    
    Thanks for this.
    
    I have one request, how can I add # of Leaves for a complete year
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2286)
    
    *   Hello Dilshad.. I have updated the tracker and now you can have the total number of leaves for the complete year. Kindly download the template again from the link in the tutorial
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2859)
        
777.  Hi Sumit, this is a really great tool! It’s a thousand times better than my super basic Excel. Thank you so much for sharing it. However I would like to add more columns “Role” and “Team” next to “\[Employee\] Name” but can’t work out how to do that. Please help.. 🙁
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2226)
    
778.  Great product. I would like to add more employees say 20 total and move the slider for the months down. How can i do this?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2173)
    
779.  Amazing. I have asked my team implement with immediate effect. Summary for whole year (employee wise & Type of leave in the columns) would be great
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2159)
    
    *   Thanks for commenting Pradeep. I am glad you find this template useful. I will soon update it with a summary
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2161)
        
        *   Hi did you get any chance to update it with the summary, i am so relief looking at this template and what to implement it in my company
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9873)
            
780.  Ur work is awesome. Additionally, I would like to do more with your template…
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2149)
    
    *   Thanks for commenting.. Glad you like the work here 🙂
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2150)
        
781.  How will i get balance of Annual Leave casual leave and sick leave separately
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2129)
    
782.  Hi, Would it be possible to edit this so standard year is 01/04 to 31/03?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2128)
    
    *   A free Excel vacation tracker tool available on [http://www.excel-macros.co.uk](http://www.excel-macros.co.uk/)
         allows you to do this.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2515)
        
783.  this is the Bestest excel i have used till date. its so helpful. thank you!!!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2063)
    
    *   Thanks for commenting Theresa.. To get the scroll bar down, right click on it and then drag it down. To add more employees, simply add employees and copy the formatting and formula. I did it for you here (up to 40 employees) – [https://www.dropbox.com/s/qsfyo70kyf1ugvh/Excel-Leave-Tracker-40Rows-TrumpExcel.xlsm?dl=0](https://www.dropbox.com/s/qsfyo70kyf1ugvh/Excel-Leave-Tracker-40Rows-TrumpExcel.xlsm?dl=0)
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2064)
        
        *   @sumitbansal23:disqus I need to do some edits on the same. please help? how should i contact you?
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3235)
            
784.  thank you for the leave template. 1 question, is there a way to change the weekends?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2061)
    
    *   Thanks for commenting..You can change the weekend by tweaking the Weekday formula in this template. More about weekday formula here – [http://trumpexcel.com/learn-excel/excel-formulas/WEEKDAY/](http://trumpexcel.com/learn-excel/excel-formulas/WEEKDAY/)
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2062)
        
        *   Thank you, I tried to figure out how but honestly I’m total noob in excel formulas. Your template is really really awesome! but can you please upload a version where the weekend is Friday and Saturday? it would be very much appreciated.
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2073)
            
            *   Hello Mohammad.. I have updated the template and now you can select the weekends.
                
                [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2670)
                
                *   Hi, Would there be a version which would allow me to upload to google sheets as I need something like this on the cloud
                    
785.  but there is no validation, suppose if five people apply on a same day then how we tackle. There should be validation where more than 3 or 4 people can not mark their leaves. a message box will prompt to select another day..
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-1978)
    
786.  Amazing piece of work! I want to extend the no of workers but I I fail how to remove the horizontal scroll bar in row 18, please some idea!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-1956)
    
    *   Right click on the HSB and drag down in this way you can add more Rows in between. Hope Sumit don’t mind, very good stuff well done Sumit 🙂
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-1957)
        
        *   Thanks Binaya.. glad you liked it 🙂
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-1958)
            
        *   Hi,how can move month scroll down?
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2584)
            
787.  Hi Sumit, Thanks very much for sharing your knowledge. One comment here, i tried to put a non-valid vacation Letter (like R for example). and it counted it as a day off in # of leaves column.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-1927)
    
    *   Hi Ammar.. Thanks for commenting.. I left it that way as I was not sure if people would want to add their own codes (or randomly key in anything just to mark a leave). But you have a valid point, and we can improve it by highlighting any cell that has something in it. Thanks for bringing this to my notice 🙂
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-1928)
        
788.  The leave tracker came in time that i require. And its a great program. Thank you. Are you able to add in the balance after deducting the nos. of leaves taken. I am more concern to track the balance of vacation leaves.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-1925)
    
    *   Thanks for commenting April.. To get the total number of leaves, use the formula in cell NK8 (and drag for all employees) =COUNTA($B8:$NI8)
        
        To get the leave balance, subtract this leave count from the total number of leaves. Hope this helps
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-1926)
        
        *   Sumit, this is an amazing spreadsheet. Similar to April, I need to track the balance of vacation leaves throughout the course of the calendar year. I cannot find a formula in cell NK8 that you reference above. I just downloaded the leave tracker this morning, so maybe it was an earlier version that contained a formula in NK8?
            
            Further, in order to track total vacation days taken for the entire year, how would I adjust the # of leaves formula?
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2708)
            
        *   Hi Sumit,Its wonderful & excellent tool. After searching many templates on website I found this useful. A question how can i amend count formula in cell NK8 to exclude holidays & weekends.(I know it can be manually done but not entering any value in this column, just curious to know it there is any formula)
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2733)
            
        *   This is really helpful. However, when I added that formula, it treated “h” as full days, giving me a total count of 4 instead of 3.5. Any recommendations? Thanks in advance.
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2740)
            
789.  Congrats to all winners !  
    Leave tracker is awesome and very useful !! – Yogirajoo
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-1919)
    
    *   Thanks for commenting Yogirajoo.. Glad you liked the leave tracker 🙂
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-1922)
        
790.  Thanks Sumit, nice.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-1918)
    
    *   Thanks for commenting Raja.. Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-1921)
        
791.  I changed the condition for highlighting the days for the leave code – I first defined the list of codes as ‘LeaveCodes’ and then changed the condition to – =IF(ISERROR(VLOOKUP(B8,LeaveCodes,1,FALSE)),FALSE,TRUE), this makes it easier to extend the table of leave codes as you only then need to ensure the name matches the longer list. It could also be used to apply ‘Data Validation’ to all the dates. It is also something that can be used to track other type of calendar events – a lot of work must have gone into this, well done.
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-1917)
    
    *   Thanks for commenting Andrew.. Great idea to create a named range for leave codes. It would make customizing it much easier 🙂
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-1920)
        
    *   Hi, Andrew. Killing myself here trying to follow your comment so I can  
        also extend the leave codes. Any chance you could email me a sample  
        file? I’d really appreciate it.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2499)
        
    *   Sorry. I am at [chelsea1424@rogers.com](mailto:chelsea1424@rogers.com)
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2500)
        
    *   Hi Andrew, I’m trying to follow your comment as I would like to extend the leave codes but I seem to be lost. Can you please email me the worksheet that you have? My email is [nisch24@gmail.com](mailto:nisch24@gmail.com)
         Thanks!
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3353)
        
    *   am trying to add the additional leave type for 0.5 value , can you help me please
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3830)
        
        *   I’m trying to do the same, did you get a response for this?
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9327)
            
792.  Congrats to all winners!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-1916)
    
793.  Super Stuff! Love the leave tracker.. This is so much better than what I use.. Thank You!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-1913)
    
    *   Thanks for commenting Mark.. Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-1914)
        
794.  Yayy!!! I won $25 Amazon Gift Card 🙂 Thank you Sumit….Look forward to learning more new interesting stuff on TrumpExcel
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-1910)
    
    *   Congratulations Mehar 🙂 Thanks for making this blog awesome!
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-1911)
        
795.  Could you please change the weekend days to be Friday and Saturday ?
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-1907)
    
    *   Thanks for commenting.. It can be done by tweaking the weekday() formula, where the second argument is 2. You can change it to 1 and it will work.
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-1909)
        
        *   i try t but the dates became amended for 1 day !!
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-1965)
            
            *   Hello Gehad..I have updates the template. Now you can select the weekends
                
                [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2669)
                
                *   Sumit,
                    
                    Thank you so much for a great template.
                    
                    A few questions:
                    
                    1.How can we keep track of total vacation time allowed for each employee and then track the remaining vacation?
                    
                    2\. Can you explain the formula a bit? I am trying to edit to accommodate for quarter day and half day vacations but it gives me error.
                    
                    Thank you,  
                    S
                    
796.  The leave tracker is one of the awesome-st thing i have seen! congratulations to the winners!
    
    [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-1906)
    
    *   Thanks Rose.. Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-1908)
        
        *   Hi Submit, Will you be releasing a 2016 version soon?
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2617)
            
            *   Hello Rodolfo.. I have updated the template for 2016. You can download it now
                
                [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-2668)
                
                *   Thanks for this template, I have a question. How would list the counts for vacation days and sick days separate instead of having just the total of all days?
                    
                *   Hi Sumit, i need to change the standard year to Jan-December year. Can you guide on how to do it?
                    
                *   I am also experiencing this issue – is there a fix?
                    
                *   Did you receive a recommendation for correction?
                    
                *   Same problem here. Everything drags over into the other months. If I mark April 3rd as a V for Vacation day then the 3rd of every month becomes a vacation day for that employee. If I delete one, they all delete.
                    
                *   Hello Megan.. I believe you are using the value in cell A1 to change the month. Cell A1 need to be set only once, and then use the scroll bar to change the month.
                    
                *   Hello Fam..To change the month, use the scroll bar and not the value in cell A1.
                    
                *   Thank you so much for the reply! I was unclear with my question. I actually have two. 1). I have added additional “leave codes”. Some of these additional “leave codes” I would like to have counted as 0.5, however, they are all being counted as 1.0. How do I change that?  
                    2). How can I view multiple months at a time? I need to see 6 months in advance all at once for schedule comparison. I can unhide the columns, however, I then lose the dates at the top.  
                    This is masterful! Thank you for the creation, as once I have it completely tweaked, it will make tracking so easy!!!
                    
                *   You will need to add or amend the formula to do so
                    
                *   is it also possible to link the A1 value to scrollbar? for easy access
                    
                *   A1 is not to be used to change the months. For that you need to use scroll bar. A1 is to be used to specify the calendar year. SO if you want the year from April-march, then you would have 4 in cell A1.
                    
                *   Hi Sumit I enjoy your Leave Tracker.. but I have a question. Is it possible to include a summary Sheet where in you can see all the Employee and the Date they tag as Leave in that summary for whole year?
                    
                *   The scroll bar is not user friendly as it changes at random. Also is there an easier way to view a single person’s vacation details?
                    
                *   Hello Ashesh.. To change the month, use the scroll bar and not the value in cell A1.
                    
                *   hello. after adjusting the holiday list, the tracker color has not changed
                    
                *   I am also facing this problem. Did u get a solution to this?
                    
                *   same here, is there any solution for this case?
                    
                *   Is there a possibility to add the holidays too during vacation?
                    
        *   Thanks so much for this wonderful template! 🙂
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3117)
            
            *   Thanks for commenting Prabhath.. Glad you found this useful 🙂
                
                [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-3135)
                
        *   Hello Sumit, Thanks for your template it is great , can you please help  
            me how to add additional column for ID and position in template 2017 I  
            could not use the template you added additional column in version  
            2016
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9122)
            
            *   Hi… did you by any chance find the way to add employee ID. Please share if you’ve got the solution
                
                [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9537)
                
        *   Hi, I’m trying to download the leave tracker, it just shows up downloaded like a zip file and when I open zip file, no spreadsheet. Not sure what I am doin wrong. Is it possible for the spreadsheet tracker to emailed to me
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9322)
            
            *   I’m having the same problem – what am I doing wrong?
                
                [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9664)
                
                *   Hey Anna.. Here is the direct link: [https://s3-ap-southeast-1.amazonaws.com/downloadexcelfiles/Excel-Leave-Tracker-2017.xlsm](https://s3-ap-southeast-1.amazonaws.com/downloadexcelfiles/Excel-Leave-Tracker-2017.xlsm)
                    
                    Hope this works for you.
                    
                *   HI Summit, thanks for the link but I’m having same issue as Kayla below- the files are in XML format and I can’t open the, PLEASE HELP!!! 🙂
                    
                *   I’m having the same problem – after extracting everything from the zip file, it’s all XML, VML, or BIN files, nothing that’s XLS
                    
        *   how to set working day for specific employee,because they non working day is not the same..hope u will help me
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-9454)
            
        *   hi i am wondering how i can do this template all by myself and it is  
            been very helpful without too much effort still i want to understand it  
            fully in spite of plenty try i could not understand it fully is there  
            are guide i have to be using to help me make one of my own.
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-10137)
            
        *   Hi,
            
            This template is amazing i currently do everything by pen and paper but this will help me loads. is there a way you can make this template run the uk work calendar year which is april to april so month 1 starts april then adds all the days used untill the following april. i currently have 15 employees and would happily pay you if this could be updated for the next say 10- years and save me having to download every year also i am more than happy to edit and add in the public holidays manually .
            
            [Reply](https://trumpexcel.com/excel-leave-tracker/#comment-13180)
            

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-leave-tracker/#respond)

Comment

Name Email Website

  

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

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