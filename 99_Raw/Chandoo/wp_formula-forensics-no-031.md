# Resource Allocation and Scheduling using Excel

**Source:** https://chandoo.org/wp/formula-forensics-no-031

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
    , [Posts by Sajan](https://chandoo.org/wp/category/posts-by-sajan/)
    

Formula Forensics No. 031 – Production Scheduling using Excel
=============================================================

*   Last updated on October 12, 2012

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

Recently, Bluetaurean asked in the [Chandoo.org Forums](http://chandoo.org/forums/topic/break-into-24-hour-schedules "http://chandoo.org/forums/topic/break-into-24-hour-schedules")
 about ways to allocate work durations for various product lines across 24 hour days to create a daily schedule.

Both formula-based and VBA-based solutions were offered.

Today at formula Forensics we will take a look at the formula-based approach.

As always at Formula Forensics you can follow along, [Download Here – Excel 2007-2013](https://chandoo.org/wp/wp-content/uploads/2012/10/FF-Production-Scheduling-the-Excel-way.xlsx "https://chandoo.org/wp/wp-content/uploads/2012/10/FF-Production-Scheduling-the-Excel-way.xlsx")
.

Set the Scene
-------------

Since one might encounter a similar need in a variety of contexts (manufacturing, engineering, project planning, etc.), we will look at a more general problem of allocating a set of tasks and corresponding durations to one or more days, as shown in the following diagram.

We will create two output views:

*   One that is a flat list that can then be manipulated further using Excel’s Pivot table feature, and
*   Another view that mimics a pivot-table (and is similar to a typical project Gantt view, but with actual values listed instead of a bar chart).

[![](https://chandoo.org/wp/wp-content/uploads/2012/10/FF-Production-Scheduling-the-Excel-way-Figure0.png "FF - Production Scheduling the Excel way -Figure0")](https://chandoo.org/wp/wp-content/uploads/2012/10/FF-Production-Scheduling-the-Excel-way-Figure0.png)

You can follow along using the attached Excel document. [Download here Excel 2007+](https://chandoo.org/wp/wp-content/uploads/2012/10/FF-Production-Scheduling-the-Excel-way.xlsx "https://chandoo.org/wp/wp-content/uploads/2012/10/FF-Production-Scheduling-the-Excel-way.xlsx")

Problem Specifics
-----------------

*   We have a list of tasks and their durations.
*   We need to distribute the tasks to different days, without exceeding the maximum available duration in a given day.
*   When the hours in a day are “used up”, we need to allocate the remaining task duration to the next day, and so on.
*   On the other hand, if a given task does not use up all of the hours in a given day, we will need to assign more than one task for that day, provided the combined durations do not exceed the available hours for that day.
*   In other words, we will need to split a task across one or more days, or combine one or more tasks into a single day, as needed, to maximize the work performed in a given day.

Developing the Approach
-----------------------

Before we tackle this problem in Excel, let us review how we might do this manually. Like most things, we might use the following three step process:

1.  Take the first task and assign its duration to Day 1. If the task’s duration exceeds the maximum hours available in a day, allocate the portion of the duration that does not fit into Day 1 into Day 2.
2.  Take the second task, and see whether it can fit into an existing day, or whether it needs to be distributed to multiple days
3.  Etc. (OK… so that three-step process was a stretch!)

Statistics show that most people think in terms of IF-THEN-ELSE statements. So here it is…

_For a given Day, and for a given Task,_

_If \[Hours Not Allocated For that Task\] > \[Hours Available for that Day\] Then_

_Set Duration for that Day as \[Hours Available for that Day\]_

_Else_

_Set Duration for that Day as \[Hours Not Allocated for that Task\]_

_End_  
_Continue the above evaluation until all tasks have been allocated to days._

Of course, the above IF() logic can be condensed as follows:

MIN( \[Hours Not Allocated For that Task\] ,  \[Hours Available for that Day\] )

Putting it All Together: Output Option 1: Gantt-like View
---------------------------------------------------------

Let us employ the above approach to create the Gantt-like view.

To make our approach more generic, we will use an Excel Name called “MaxHrsPerDay” to indicate the maximum available hours in a given day. (In the sample worksheet, it has been set to 24 hours.)

Our source data is setup as shown in the diagram below:

*   Tasks are in the range A2:A5
*   Durations are in the range B2:B5

[![](https://chandoo.org/wp/wp-content/uploads/2012/10/FF-Production-Scheduling-the-Excel-way-Figure1.png "FF - Production Scheduling the Excel way -Figure1")](https://chandoo.org/wp/wp-content/uploads/2012/10/FF-Production-Scheduling-the-Excel-way-Figure1.png)

We will create the output in a separate worksheet, in the range A1:E5 as shown below:

[![](https://chandoo.org/wp/wp-content/uploads/2012/10/FF-Production-Scheduling-the-Excel-way-Figure2.png "FF - Production Scheduling the Excel way -Figure2")](https://chandoo.org/wp/wp-content/uploads/2012/10/FF-Production-Scheduling-the-Excel-way-Figure2.png)

Put the following formula into cell A2 and copy down to A5:

\=SourceData!$A2

(This formula is merely referencing the values from the SourceData sheet. The sample workbook also includes an approach to make this reference more location independent.)

Put the following formula in cell B2, and copy it down and right:

\=MIN((SourceData!$B2-SUM($A2:A2)), (MaxHrsPerDay-SUM(B$1:B1)))

Setup the header row (B1:E1) as desired. (I have used text values for the header. You could also calculate the header text using formulas. Since that is straightforward, I will leave that as an exercise for the reader.)

Now let us look at what the formula in cell B2 is doing:

*   SUM($A2:A2) is calculating the sum of the allocated durations for TaskA. (Please note the use of absolute and relative references. The formula is anchored on column A, but the starting row, ending row and ending column are free to expand.) SUM($A2:A2) returns zero since SUM() ignores text values.

– If you look at cell C2, the reference changes to SUM($A2:B2).  
– In cell B3, the reference changes to SUM($A3:A3). You get the idea

*   (SourceData!$B2-SUM($A2:A2)) calculates the difference between the duration for TaskA (40 in the example) and the hours allocated as of that point (0), to return 40-0=40.
*   SUM(B$1:B1) is calculating the sum of the allocated hours for Day1. (Again, we are using a combination of absolute and relative references to keep the calculation anchored on column B.) In this case, the value is zero, since this is the first allocation for Day1.
*   (MaxHrsPerDay-SUM(B$1:B1)) calculates the hours remaining (i.e. available) for Day1. Since this is for cell B2, the calculation returns 24 – 0 = 24.

That is it!

We put those absolute and relative references to good use!

This approach was easy because all we had to do was calculate the duration for a given task for a given day.

On the other hand, if we had to figure out what the Task was, or which Day it was, the calculation gets a little more involved. Since this is “formula forensics”, we would not have it any other way! 🙂

Putting it All Together: Output Option 2: A Sequential List of Tasks and Durations for Each Day (i.e. a Flat List)
------------------------------------------------------------------------------------------------------------------

As before, we will use the Excel Name “MaxHrsPerDay” to refer to the maximum hours in a Day.

As shown in the following diagram, we will turn the source data into a flat list of Days, Tasks and Durations:

[![](https://chandoo.org/wp/wp-content/uploads/2012/10/FF-Production-Scheduling-the-Excel-way-Figure3.png "FF - Production Scheduling the Excel way -Figure3")](https://chandoo.org/wp/wp-content/uploads/2012/10/FF-Production-Scheduling-the-Excel-way-Figure3.png)

Unlike with VBA, since a formula cannot choose which row and column to write its output, we have to set the formula in every cell where we suspect there might be a value.

In the above sample diagram, we copy the formulas from row 2 to row 9. However, row 9 shows “…” indicating that the list was completed by row 8.

Let us look at how to determine the value for Day, Task and Allocated Duration.

For ease of description, I have created the following Excel Names:

**WorkList**: =A2:A5 in the source data.

**WorkDuration**: =B2:B5 in the source data

While creating the Gantt-like view earlier, we were able to take advantage of the static “Day” and “Task” values to determine the Remaining Duration, Available Duration, etc. Since we now have to determine all three values (Day, Task, Allocated Duration), we will need some “helper” data.

We will add a column alongside the source data that shows the cumulative duration (for reasons that will become clear shortly), as shown in the following diagram:

[![](https://chandoo.org/wp/wp-content/uploads/2012/10/FF-Production-Scheduling-the-Excel-way-Figure4.png "FF - Production Scheduling the Excel way -Figure4")](https://chandoo.org/wp/wp-content/uploads/2012/10/FF-Production-Scheduling-the-Excel-way-Figure4.png)

Cumulative Duration is calculated as the sum of all durations up to a given row.

*   For example, in cell C2, the Cumulative Duration is 40.
*   In cell C3, the Cumulative Duration is 40+20=60
*   And so on.

For ease of referencing, we will use an Excel Name called **CumulativeDuration** =C2:C5.

### Let us look at why we need the “CumulativeDuration” helper column:

### The circular logic problem

In order to determine the durations already allocated for a given day, we will need to know which Day it is.

We also need to know which Task we are trying to calculate the duration for.

So… do we calculate the Day or the Task or the Duration first?!! As you can imagine, that will soon land us in some circular logic.

Some helpful observations about the output:

*   In column C of the output (on worksheet FlatList), the sum of allocated durations adds up to the total duration for all tasks. (No surprise here!)
*   If every task had duration equal to the MaxHrsPerDay, you would have the same duration value for all days. (Not surprising, but interesting!)
*   In other words, you could think of the Allocated Duration column as the total duration for all tasks, allocated MaxHrsPerDay at a time.
*   Now we need a way to iterate through the duration values one at a time and account for the durations already processed. In other words, each value needs to contain all of the previous values. Welcome to an array of the cumulative durations!
*   For example, in the cumulative array “{40;60;65;80}”, the value 60 already includes the previous value 40 in it. This allows us to subtract all durations allocated up to a given row, to get the duration value that is remaining to be allocated.
*   Since Excel is good with numbers, we will base the calculation for AllocatedDuration and Tasks on the Duration values.
*   By calculating the two values separately, we avoid the circular logic.

Let’s now look at the formulas for **Day**, **WorkItem** and **AllocatedDuration**.

It would be easier if we looked at the formulas in reverse order, starting with **AllocatedDuration**, then **WorkItem**, and finally **Day**.

### Formula for “AllocatedDuration”

Enter the following formula into cell C2, ending with **Ctrl+Shift+Enter**, as shown in the following diagram:

\=IF(SUM(C$1:C1)>=SUMPRODUCT(WorkDuration), “…”,MIN(INDEX(WorkDuration, MATCH(TRUE, CumulativeDuration-SUM(C$1:C1) > 0, 0)) – SUMIFS(C$1:C1, B$1:B1,B2), MaxHrsPerDay-SUMPRODUCT((A$1:A1=A2)\* IF(ISNUMBER(C$1:C1), C$1:C1, 0)))) **Ctrl+Shift+Enter**

[![](https://chandoo.org/wp/wp-content/uploads/2012/10/FF-Production-Scheduling-the-Excel-way-Figure5.png "FF - Production Scheduling the Excel way -Figure5")](https://chandoo.org/wp/wp-content/uploads/2012/10/FF-Production-Scheduling-the-Excel-way-Figure5.png)

Let us look at the formula closely (using the formula in row 2):

*   SUMPRODUCT((A$1:A1=A2)\* IF(ISNUMBER(C$1:C1), C$1:C1, 0)) **\->** This calculates the sum of all allocated durations up to the previous row, where the Day = current row’s day. Please note the use of absolute and relative references. They allow us to expand the range as we go down the rows, while remaining anchored to the first row.

– Since this is the first data row, C$1:C1 returns “Allocated Duration” and the ISNUMBER() function returns FALSE, and consequently, the IF() function returns 0.  
– A$1:A1 returns “Day”, and the test A$1:A1=A2 returns FALSE. Please note that in this case, it does not matter whether A2 has a value in it, whether it has the value 1, etc.  
– SUMPRODUCT() provides the result of FALSE \* 0 = 0

*   **MaxHrsPerDay** – SUMPRODUCT((A$1:A1=A2)\* IF(ISNUMBER(C$1:C1), C$1:C1, 0)) **\->** This calculates the difference between maximum duration available for a day and the sum of durations allocated for the current day. In other words, it calculates the available duration for the current row’s day.

– In this example, the calculation results in MaxHrsPerDay (24 in our example) – 0 = 24

*   SUMIFS(C$1:C1, B$1:B1,B2) **\->** This calculates the sum of all allocated durations for the current row’s task. Since B$1:B1 is the text value “Work Item”, the SUMIFS() returns 0. Again, it does not matter if B2 is blank or has a value like “TaskA”, since Excel correctly evaluates the condition whether B$1:B1 equals B2.
*   SUM(C$1:C1) **\->** This calculates the sum of all allocated durations up to the previous row.
*   **CumulativeDuration** — SUM(C$1:C1) **\->** CumulativeDuration evaluates to {40;60;65;80}. SUM(C$1:C1) evaluates to zero. As such, the expression evaluates to {40;60;65;80} – 0, or {40;60;65;80}.

– If we look at the calculation for this expression in cell C3 (the expression would be “CumulativeDuration—SUM(C$1:C2)”), we would get the result of {40;60;65;80} – (0+24) = {16;36;41;56}. (As you know, subtracting a scalar value from an array results in an array with each value reduced by the scalar value.)

– If we look at the calculation for this expression in cell C4 (the expression would be “CumulativeDuration—SUM(C$1:C3)”) , we would get the result of {40;60;65;80} – (0+24+16) = {0;20;25;40}

– As you can see, each successive calculation reduces the CumulativeDuration array by the amount of hours already allocated. By reducing the CumulativeDuration array in this fashion, we ensure that we do not “double count” a duration.

– If a value in the array evaluates to zero, it means the corresponding duration has been fully allocated. (In cell C3, the first value in the array is zero, indicating that the original 40 hours has been fully allocated.) We will put this knowledge to good use in the next expression.

*   MATCH(TRUE, CumulativeDuration—SUM(C$1:C1) > 0, 0) **\->** The expression CumulativeDuration—SUM(C$1:C1) > 0 evaluates to \={TRUE;TRUE;TRUE;TRUE} because all values are greater than zero. By performing a MATCH() for TRUE, we are able to find the first location in the array that has a non-zero value.

– If we look at the result of this expression in cell C3, we get {16;36;41;56} > 0 = {TRUE;TRUE;TRUE;TRUE}

– If we look at the result of this expression in cell C4, we get {0;20;25;40} > 0 = {FALSE;TRUE;TRUE;TRUE}

– As you recall, the zero values (or FALSE) correspond to the durations that have been fully allocated, whereas, the non-zero values (or TRUE) correspond to the durations that have NOT been fully allocated.

– It is helpful to note that MATCH() returns the LOCATION of what it finds. As such, the returned location is that of the first duration value that has not been fully allocated! Since the CumulativeDuration array is the same size as the WorkDuration array, we will be able to put this returned location value to good use in the next expression.

*   INDEX(WorkDuration, MATCH(TRUE, CumulativeDuration — SUM(C$1:C1) > 0, 0)) **\->** By using the location value (of the first duration value that has not been fully allocated), we find the corresponding original duration value from the WorkDuration array.

– As we saw earlier, the expression “CumulativeDiration – SUM(C$1:C1)” reduces the CumulativeDuration by the duration values allocated to that point. However, the resulting array could have partial duration values as well. By referencing the corresponding duration value from the WorkDuration array, we ensure that we retrieve the original (full) duration value that was to be allocated.

*   MIN(…) -> This expression calculates the value of MIN(\[Hours Not Allocated For that Task\], \[Hours Available for that Day\])

– \[Hours Not Allocated For that Task\] is returned by INDEX(WorkDuration, MATCH(TRUE, CumulativeDuration—SUM(C$1:C1) > 0, 0)) – SUMIFS(C$1:C1, B$1:B1,B2)

– \[Hours Available for that Day\] is returned by second half of the MIN() expression: MaxHrsPerDay—SUMPRODUCT((A$1:A1=A2)\* IF(ISNUMBER(C$1:C1), C$1:C1, 0)).

– So, we essentially got back to the logic we started from, which is the same logic we used for creating the Gantt-like view as well.

*   The remaining portion of the formula (the IF() check) determines if all of the hours have been allocated. If all hours have been allocated, it returns “…”.

– SUMPRODUCT(WorkDuration) **\->** This expression calculates the total of all work duration values. In cell C2, it evaluates to SUMPRODUCT({40;20;5;15}) = 80

– SUM(C$1:C1)>=SUMPRODUCT(WorkDuration) **\->** Determines if the sum of durations allocated up to that point is greater than the total for all durations. (Since this is part of an array formula, you could also use the SUM function in place of SUMPRODUCT. But I am partial to the SUMPRODUCT function!! So, unless you are in a competition where the winner is determined by the shortest formula, feel free to use either one!

### Formula for “WorkItem”

Enter the following formula into cell B2, ending with **Ctrl+Shift+Enter**, as shown in the following diagram.

\=IF(SUM(C$1:C1)>=SUMPRODUCT(WorkDuration), “…”,INDEX(WorkList, MATCH(TRUE, (CumulativeDuration-SUM(C$1:C1)) > 0, 0))) **Ctrl+Shift+Enter**

[![](https://chandoo.org/wp/wp-content/uploads/2012/10/FF-Production-Scheduling-the-Excel-way-Figure6.png "FF - Production Scheduling the Excel way -Figure6")](https://chandoo.org/wp/wp-content/uploads/2012/10/FF-Production-Scheduling-the-Excel-way-Figure6.png)

You are already familiar with most of the formula components since you saw them in the formula for AllocatedDuration. The only difference is that in this formula, we are returning a value from WorkList. (i.e. we locate the position of the first non-zero duration in CumulativeDuration array, and since that array is the same size as the WorkList array, we are able to find the first Task that has not been fully allocated.)

### Formula for “Day”

Enter the following formula into cell A2, ending with **Ctrl+Shift+Enter**, as shown in the following diagram:

\=IF(SUM(C$1:C1)>=SUMPRODUCT(WorkDuration), “…”, MAX( N(A1) + (SUMIFS(C$1:C1, A$1:A1, A1)>=MaxHrsPerDay), 1)) **Ctrl+Shift+Enter**

[![](https://chandoo.org/wp/wp-content/uploads/2012/10/FF-Production-Scheduling-the-Excel-way-Figure7.png "FF - Production Scheduling the Excel way -Figure7")](https://chandoo.org/wp/wp-content/uploads/2012/10/FF-Production-Scheduling-the-Excel-way-Figure7.png)

Let us look at the formula in detail (using the formula in row 2):

*   SUMIFS(C$1:C1, A$1:A1, A1) **\->** This expression calculates the sum of all durations (in column C) where the Days (in column A) equal the previous day.

– In cell A2, this expression evaluates to “SUMIFS(“Allocated Duration”, “Day”, “Day”)” = 0. (Excel smartly ignores any non-numeric values in the first argument.)

– In cell A3, this expression evaluates to “SUMIFS({“Allocated Duration”;24}, {“Day”;1}, 1)” = 24.

*   SUMIFS(C$1:C1, A$1:A1, A1)>=MaxHrsPerDay **\->** This expression checks if the sum of all durations where the Days equal the previous day is greater than or equal to MaxHrsPerDay.

– In cell A2, this expression evaluates to FALSE

– In cell A3, this expression evaluates to TRUE

*   N(A1) **\->** This expression returns the numeric value for its argument. Since N() returns zero for any non-numeric arguments, we use this function to return zero for the heading (“Day”) in A1. (Any numeric values are returned as is.)
*   MAX( N(A1) + (SUMIFS(C$1:C1, A$1:A1, A1)>=MaxHrsPerDay), 1) **\->** The first argument of the MAX function “N(A1) + (SUMIFS(C$1:C1, A$1:A1, A1)>=MaxHrsPerDay)”returns the next increment for day, if the previous day has been fully allocated. Otherwise, it returns the same value as the previous day.

– In cell A2, this expression evaluates to MAX( N(“Day”) + (SUMIFS(“Allocated Duration”, “Day”, “Day”)>=24), 1), which evaluates to MAX( N(“Day”) + (0>=24), 1), which evaluates to MAX( 0 + (FALSE), 1), which finally evaluates to 1.

– In cell A3, this expression evaluates to MAX( N(1) + (SUMIFS({“Allocated Duration”;24}, {“Day”;1}, 1)>=24), which evaluates to MAX( N(1) + (24>=24), 1), which evaluates to MAX( 1+ (TRUE), 1), which finally evaluates to 2 since 1 + TRUE = 2.

Download
--------

You can download a copy of the above file and follow along, [Download Here – Excel 2007-2013](https://chandoo.org/wp/wp-content/uploads/2012/10/FF-Production-Scheduling-the-Excel-way.xlsx "https://chandoo.org/wp/wp-content/uploads/2012/10/FF-Production-Scheduling-the-Excel-way.xlsx")
.

Final Thoughts
--------------

While we used the same basic logic for both output options in this article, there are probably many other ways to tackle the age-old problem of production scheduling.

I would love to hear about some of your ideas, as well as ways to extend the concepts described here.

In the meantime, I wish you continued EXCELlence!

**_Sajan._**

Other Chandoo.org Posts related to Scheduling
---------------------------------------------

Here at Chandoo.org you can find the following related posts:

[http://www.chandoo.org/wp/2010/11/18/scheduling-variable-sources/](http://chandoo.org/wp/2010/11/18/scheduling-variable-sources/ "http://chandoo.org/wp/2010/11/18/scheduling-variable-sources/")

[http://chandoo.org/wp/2009/06/16/gantt-charts-project-management/](http://chandoo.org/wp/2009/06/16/gantt-charts-project-management/ "http://chandoo.org/wp/2009/06/16/gantt-charts-project-management/")

[http://chandoo.org/wp/project-management-templates/gantt-charts/](http://chandoo.org/wp/project-management-templates/gantt-charts/ "http://chandoo.org/wp/project-management-templates/gantt-charts/")

Thank You
---------

This was Sajan’s second post at Chandoo.org and so a special thank you to **Sajan** for putting pen to paper to describe the technique here.

You may want to read [Sajan’s first post here](http://chandoo.org/wp/2012/10/04/formula-forensics-no-030/ "Sajan's First Post")
 or thank him in the comments below:

[Formula Forensics “The Series”](http://chandoo.org/wp/category/formula-forensics/ "Formula Forensics Series")

---------------------------------------------------------------------------------------------------------------

This is the 31st post in the Formula Forensics series.

You can learn more about how to pull Excel Formulas apart in the following posts: [Formula Forensic Series](http://chandoo.org/wp/category/formula-forensics/ "Formula Forensics")

Formula Forensics Needs Your Help
---------------------------------

I need more ideas for future Formula Forensics posts and so I need your help.

If you have a neat formula that you would like to share like above, try putting pen to paper and draft up a Post like Sajan has done above or;

If you have a formula that you would like explained, but don’t want to write a post, send it to [Hui](http://chandoo.org/wp/about-hui/ "Contact Hui")
 or [Chandoo](http://chandoo.org/wp/contact/ "Contact Chandoo")
.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [30 Comments](https://chandoo.org/wp/formula-forensics-no-031/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/formula-forensics-no-031/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [circular references](https://chandoo.org/wp/tag/circular-references/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Formula Forensics](https://chandoo.org/wp/tag/formula-forensics/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [planning](https://chandoo.org/wp/tag/planning/)
    , [scheduling](https://chandoo.org/wp/tag/scheduling/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
    , [Posts by Sajan](https://chandoo.org/wp/category/posts-by-sajan/)
    

[PrevPreviousUse Indexed charts when understanding change \[Charting Techniques\]](https://chandoo.org/wp/indexed-charts-in-excel/)

[NextWrite a formula to check few cells have same value \[homework\]Next](https://chandoo.org/wp/check-cells-for-equality/)

![](https://chandoo.org/wp/wp-content/uploads/2018/07/chandoo-instructor.png)

### Welcome to Chandoo.org

Thank you so much for visiting. My aim is to make **you awesome in Excel & Power BI.** I do this by sharing videos, tips, examples and downloads on this website. There are more than 1,000 pages with all things Excel, Power BI, Dashboards & VBA here. Go ahead and spend few minutes to be AWESOME.  
  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel tips book](https://chandoo.org/wp/subscribe/)

[![](https://chandoo.org/wp/wp-content/uploads/2019/08/fast-track-excel-book-signup-v3-med.png)](https://chandoo.org/wp/subscribe/)

[Want an AWESOME  \
Excel Class?](https://chandoo.org/wp/excel-school-program/)

[![advanced-excel-dashboards-course-chandoo](https://chandoo.org/wp/wp-content/uploads/2019/08/advanced-excel-dashboards-course-chandoo.jpg)](https://chandoo.org/wp/excel-school-program/)

Overall I learned a lot and I thought you did a great job of explaining how to do things. This will definitely elevate my reporting in the future.

![](https://chandoo.org/wp/wp-content/uploads/2023/10/rebekah-spouser-1631059707542.jpeg)

Rebekah S

Reporting Analyst

[FREE Goodies for you...](https://chandoo.org/wp/excel-school-program/)

[![Excel formula list - 100+ examples and howto guide for you](https://chandoo.org/wp/wp-content/uploads/2018/06/100-formulas-excel-list.png)](https://chandoo.org/wp/excel-formula-list/)

[100 Excel Formulas List](https://chandoo.org/wp/excel-formula-list/)

From simple to complex, there is a formula for every occasion. Check out the list now.

[![](https://chandoo.org/wp/wp-content/uploads/2018/07/free-excel-templates-v1.png)](https://chandoo.org/wp/free-excel-templates-download/)

[20 Excel Templates](https://chandoo.org/wp/free-excel-templates-download/)

Calendars, invoices, trackers and much more. All free, fun and fantastic.

[![Advanced Pivot Table tricks](https://chandoo.org/wp/wp-content/uploads/2020/02/advanced-pivot-table-tricks.png)](https://chandoo.org/wp/advanced-pivot-tables)

[13 Advanced Pivot Table Skills](https://chandoo.org/wp/advanced-pivot-tables)

Power Query, Data model, DAX, Filters, Slicers, Conditional formats and beautiful charts. It's all here.

[![](https://chandoo.org/wp/wp-content/uploads/2019/08/introduction-to-powerbi-chandoo-thumb.jpg)](https://chandoo.org/wp/powerbi-introduction/)

[Get started with Power BI](https://chandoo.org/wp/powerbi-introduction/)

Still on fence about Power BI? In this getting started guide, learn what is Power BI, how to get it and how to create your first report from scratch.

Recent Articles on Chandoo.org

[![2026 calendar and planner Excel template - how to use](https://chandoo.org/wp/wp-content/uploads/2025/12/screenshot-0282.png)](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

### [FREE Calendar & Planner Excel Template for 2026](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

Here is a fabulous New Year gift to you. A free 2025 Calendar Excel Template with built-in Activity planner. This is a fully dynamic and 100% customizable Excel calendar for 2025.

[![Who is my boss's boss?](https://chandoo.org/wp/wp-content/uploads/2025/08/image.png)](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

### [Who is my boss’s boss? \[Data Analytics Challenge – 001\]](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

[![NZ GST Calculation - Excel Formula](https://chandoo.org/wp/wp-content/uploads/2025/07/nz-gst-calculation-excel-formula.png)](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/)

### [New Zealand GST Calculation with Excel \[Free Template\]](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/)

[![How to make a pivot from another pivot in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0157.png)](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/)

### [Make a Pivot from Another Pivot Table in Excel](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/)

[![How to use XLOOKUP with two sheets in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0152.png)](https://chandoo.org/wp/xlookup-with-two-sheets/)

### [How to use XLOOKUP with two sheets?](https://chandoo.org/wp/xlookup-with-two-sheets/)

Best of the lot

*   [Excel for beginners](https://chandoo.org/wp/excel-basics/)
    
*   [Advanced Excel Skills](https://chandoo.org/wp/advanced-excel-skills/)
    
*   [Excel Dashboards](https://chandoo.org/wp/excel-dashboards/)
    
*   [Complete guide to Pivot Tables](https://chandoo.org/wp/excel-pivot-tables/)
    
*   [Top 10 Excel Formulas](https://chandoo.org/wp/top-10-formulas-for-aspiring-analysts/)
    
*   [Excel Shortcuts](https://chandoo.org/wp/complete-list-of-excel-shortcuts/)
    
*   [#Awesome Budget vs. Actual Chart](https://chandoo.org/wp/budget-vs-actual-chart-free-template/)
    
*   [40+ VBA Examples](https://chandoo.org/wp/excel-vba/examples/)
    

Related Tips
------------

[![2026 calendar and planner Excel template - how to use](https://chandoo.org/wp/wp-content/uploads/2025/12/screenshot-0282.png)](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

Learn Excel

### [FREE Calendar & Planner Excel Template for 2026](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

[![Who is my boss's boss?](https://chandoo.org/wp/wp-content/uploads/2025/08/image.png)](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

Excel Challenges

### [Who is my boss’s boss? \[Data Analytics Challenge – 001\]](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

[![How to use XLOOKUP with two sheets in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0152.png)](https://chandoo.org/wp/xlookup-with-two-sheets/)

Excel Howtos

### [How to use XLOOKUP with two sheets?](https://chandoo.org/wp/xlookup-with-two-sheets/)

[![Excel IF Statement Two Conditions - Perfect Examples](https://chandoo.org/wp/wp-content/uploads/2025/05/screenshot-0121.png)](https://chandoo.org/wp/excel-if-statement-two-conditions/)

Excel Howtos

### [Excel IF Statement Two Conditions](https://chandoo.org/wp/excel-if-statement-two-conditions/)

[![How to insert dates automatically in Excel](https://chandoo.org/wp/wp-content/uploads/2025/05/2025-05-07_10-35-53.gif)](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/)

Excel Howtos

### [How to insert dates in Excel automatically](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/)

[![Lookup in any column - Excel formula trick](https://chandoo.org/wp/wp-content/uploads/2025/02/SNAG-0092.png)](https://chandoo.org/wp/how-to-lookup-in-any-column-excel/)

Excel Howtos

### [How to lookup in any column – Excel Formula Trick](https://chandoo.org/wp/how-to-lookup-in-any-column-excel/)

### 3 Responses to “Filter one table if the value is in another table (Formula Trick)”

1.  ![](https://secure.gravatar.com/avatar/009649ad2a9f58f64a563b208b196d4e78b4e506bf2eeb2ab4c84a820fd0aa0e?s=64&d=mm&r=g) Montu says:
    
    [November 18, 2022 at 5:19 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107616)
    
    What about the opposite? I want a list of products without sales or customers with no orders. So I would exclude the ones that are on the other table.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-031/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-031/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-031/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ