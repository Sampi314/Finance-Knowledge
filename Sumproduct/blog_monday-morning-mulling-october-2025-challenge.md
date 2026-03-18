# Monday Morning Mulling: October 2025 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-october-2025-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: October 2025 Challenge

*   November 3, 2025

Monday Morning Mulling: October 2025 Challenge
==============================================

_On the final Friday of each month, we set an Excel / Power Pivot / Power Query / Power BI problem for you to puzzle over for the weekend.  On the Monday, we publish a solution.  If you think there is an alternative answer, feel free to email us.  We’ll feel free to ignore you._

**_The Challenge_**

This month’s challenge was to create a working Excel clock that shows the current time using two \[2\] concentric circles of numbers:

*   Inner circle: the 12-hour dial
*   The outer circle represents the minutes (1 to 60, corresponding to 5-minute intervals).

You might imagine it should look like this:

![](<Base64-Image-Removed>)

However, as this was the first part of a three-part challenge (Parts 2 and 3 will be provided as our _Final Friday Fix_ in November and December), our clock face in Excel was a little more basic:

![](<Base64-Image-Removed>)

To assist, we provided an original question file [here](https://sumproduct.com/wp-content/uploads/2025/10/SP-Excel-Clock-Challenge.xlsx)
.

The cells should automatically highlight the correct hour and minute based upon the current time in your system, _i.e._ Excel should show the clock “hands” through cell colour, updating dynamically whenever the time changes.

You were to assume the following setup:

*   the **Data** area included two \[2\] categories: **Hours** (1 to 12) and **Minutes** (1 to 60)
*   the **Time** cell was an input and was formatted as dd/mm/yyyy hh:mm (as this is the date format for our regional setting – you were free to modify this if you needed to).

![](<Base64-Image-Removed>)

As always, there were some requirements:

*   the formula needed to be within just one \[1\] column (no “helper” cells)
*   you were to ensure the solution was dynamic so that it updated when new placeholders or replacement values were added
*   no VBA or Power Query was allowed; this was purely a formula challenge.

**_Suggested Solution_**

You can find our Excel file [here](https://sumproduct.com/wp-content/uploads/2025/10/SP-Excel-Clock-Suggested-Solution.xlsx)
, which shows our suggested solution. The steps are detailed below:

**1.  INPUTS AND NAMED RANGES**

In this case, the time input is stored in cell **F14**.  It is a manual input, which allows users to evaluate any time they want (it will be easy to use the **\=NOW()** formula later to ensure it is the current time in your system later).

![](<Base64-Image-Removed>)

Two named ranges are defined in the Model Parameters worksheet to make the structure more flexible: **Minutes\_Interval,** set to five \[5\] and **Hours\_in\_Clock**, set to 12.  These parameters allow for easy customisation if someone wishes to experiment with different clock types or intervals.

![](<Base64-Image-Removed>)

**2.  CONDITIONAL FORMATTING RULES**

There are two \[2\] sets of conditional formatting rules for this challenge:

![](<Base64-Image-Removed>)

The formula used to calculate Rounded Time is:

**\=MINUTE(MROUND($F$14,TIME(0,Minutes\_Interval,0)))**

This step is important because:  
  

![](<Base64-Image-Removed>)

In our model, the calculation is performed in cell **E20**.

![](<Base64-Image-Removed>)

The hour numbers (one \[1\] to 12) are placed in a circular layout on the worksheet and one of these numbers should be highlighted to represent where the hour hand points.

The conditional formatting formula used is:

**\=J28=MOD(HOUR(MROUND($F$14, TIME(0, Minutes\_Interval, 0)))  
\+ Hours\_in\_Clock – 1, Hours\_in\_Clock) + 1**

This formula:

*   extracts hour from the rounded time
*   converts zero \[0\] to 24 to a 12-hour clock (one \[1\] to 12)
*   ensures that after 12, the value wraps back to one \[1\], while adding one corrects the offset so that midnight or noon (hour zero in Excel’s system) is displayed as 12 instead of zero \[0\]
*   Carries forward minutes properly (_e.g_. 09:58 becomes 10:00).

This is applied to all inner ring cells (continuous range **J28:V40**).

![](<Base64-Image-Removed>)

The comparison to the cell reference **J28** makes the formatting dynamic, matching the cell’s printed number to the corresponding hour.  When the logical test evaluates as TRUE, that cell is filled red, visually representing the hour hand on the clock.

So now for the minutes.  Since our outer ring labels are one \[1\] to 60, the formula used is:

**\=IF(MINUTE(MROUND($F$14, TIME(0, Minutes\_Interval, 0))) = 0, 60,  
MINUTE(MROUND($F$14, TIME(0, Minutes\_Interval, 0))))**

![](<Base64-Image-Removed>)

This formula retrieves the minute from the rounded time, coverts zero \[0\] to 60 so that 10:00 highlights the “60” position.  For the applied range, the outer ring represents the minutes, which requires a slightly different approach because it cannot be selected as a single rectangular block, which would overlap the inner circle.  Instead, we manually select each cell representing a minute position, resulting in a non-contiguous range:

![](<Base64-Image-Removed>)

The formatting colours are chosen to make the clock visually intuitive, red for the inner (hour) ring and blue for the outer (minute) ring.  A yellow-filled cell is used at the centre to represent the pivot point of the hands.  When the user changes the time in **F14**, the conditional formatting automatically updates, and the red and blue highlights move accordingly, showing the current hour and minute positions instantly.

![](<Base64-Image-Removed>)

**_Word to the Wise_**

This challenge really shows how flexible conditional formatting can be.  It is not only for highlighting errors or setting limits, but also for building creative, moving visuals directly inside the worksheet.  By carefully combining functions like **HOUR**, **MINUTE**, **MOD** and **MROUND**, we can recreate the behaviour of a real clock purely through formulas.  It is quite amazing to see how Excel’s calculation logic and visual tools can work together.

If you have tried building your own version, perhaps with a different layout or colour theme, congratulations — exploring new ideas is always part of the joy of Excel!

Now, if you thought this was a rather simple conditional formatting challenge, don’t despair.  We revisit this problem again next time…

_The Final Friday Fix will return on Friday 28 November 2025 with a new Excel Challenge.  In the meantime, please look out for the Daily Excel Tip on our home page and watch out for a new blog every business working day._

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-october-2025-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-october-2025-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-october-2025-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-october-2025-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-october-2025-challenge/#0 "close")

top