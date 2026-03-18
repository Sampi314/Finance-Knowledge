# Monday Morning Mulling: November 2025 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-november-2025-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: November 2025 Challenge

*   December 1, 2025

Monday Morning Mulling: November 2025 Challenge
===============================================

_On the final Friday of each month, we set an Excel / Power Pivot / Power Query / Power BI problem for you to puzzle over for the weekend.  On the Monday, we publish a solution.  If you think there is an alternative answer, feel free to email us.  We’ll feel free to ignore you._

**_The Challenge_**

This month’s challenge was to create a working clock in Excel, similar to the following:

![](https://sumproduct.com/wp-content/uploads/2025/11/image-34.png)

Your clock had to:

*   display the input time using two hands
*   have the hour hand as the shorter of the two hands pointing to the hour between numbers similar to how a normal analogue clock would work
*   have the minute hand as the longer of the two hands pointing exactly to the minute position
*   have the hour and minute hands rotate just like a real clock
*   have the numbers 1 to 12 arranged in a circular clock face. 

The data area was to include a **Time** cell that was an input formatted as hh:mm:ss, _viz._

![](<Base64-Image-Removed>)

As always, there were some requirements:

*   the formula needed to be within just one \[1\] column (no “helper” cells)
*   you had to ensure the solution was dynamic so that it updated when new placeholders or replacement values were added
*   no VBA or Power Query was allowed; this was purely a formula challenge.

**_Suggested Solution_**

You can find our Excel file [here](https://sumproduct.com/wp-content/uploads/2025/11/SP-Excel-Clock-Solution.xlsx)
, which shows our suggested solution. The steps are detailed below:

**1.  TIME INPUT**

In this case, the time input is stored in cell **F11**.  It is a manual input, which allows users to test any time they wish. 

![](<Base64-Image-Removed>)

Excel stores the time as a fraction of the day (_e.g_. 6:00 AM = 0.25, 15:00 = 0.625).

**2.  CALCULATE HOUR PROPORTION**

The formula used to calculate the hour proportion of the input time is:

**\=MOD(F11\*2,1)**

Here, the computation **F11\*2** converts 24-hour time into a 12-hour rotation, and **MOD(…,1)** keeps only the fractional part, giving the position of the hour hand as a proportion of the clock.

**3.  BUILD THE HOUR HAND WITH PIE CHART LOGIC**

To draw a single hand using a Pie chart, we split the circle into three \[3\] parts that must sum to one \[1\]:

![](<Base64-Image-Removed>)

In this section:

*   **Before** is calculated by **MAX(E16 – E20/2, 0)**, identifying the space before the hour hand ensuring the pointer is centred
*   **Thickness** determines the width of the hour hand (_e.g_. 0.013; you can adjust to control how thick the hand looks)
*   **After** is calculated by **1 – SUM(E19:E20)**, filling the rest of the circle.  This ensures we have in effect a 100% Pie chart.

Then, select these three \[3\] cells and insert a Pie chart:

*   Only the **Thickness** slice is coloured (this becomes the hand), the **Before** and **After** slices are set to ‘No Fill’
*   Then go to **Format**, click **Shape Fill** and choose ‘No Fill’ and then click **Shape Outline** and select ‘No outline’ for **Before** and **After**

![](<Base64-Image-Removed>)

*   Next, uncheck the **Chart Title** and **Legend** for the chart.

![](<Base64-Image-Removed>)

**4.  BUILD THE MINUTE HAND**

The logic is similar to the hour hand, but here we divide by 60 minutes instead.

![](<Base64-Image-Removed>)

Minute proportion:

**\=MINUTE(F11) / 60**

Then calculate:

*   **Before**: =**MAX((MINUTE(F11)/60) – (E25/2), 0)**
*   **Thickness**: **\=E25** (_e.g_. 0.007 as it is usually thinner than hour hand)
*   **After**: =**1 – SUM(E24:E25)**

Here, we have similar visualisation rules to the hour hand and we create a new Pie chart with these three \[3\] values and colour only the **Thickness** slice.

**5.  CREATE THE CLOCK DIAL** We now need the circular clock face displaying numbers 1 to 12.  Here, we create a list of 12 cells, each with value one \[1\].  This ensures 12 equal segments

![](<Base64-Image-Removed>)

Then, we insert a Doughnut chart based on this range.  Inside this single Doughnut chart, we add three \[3\] series, with each one becomes one ring of the clock face. 

![](<Base64-Image-Removed>)

Then, we need to adjust the format of this Doughnut chart. 

![](<Base64-Image-Removed>)

Here are some steps to make it closer to a real clock:

*   Set **Angle of first slice** = 15°.  This is because the segments start from 0° (due north), with the labels at mi-point.  To get the 12 aligned at the top we need to displace by 360°/12 and then divide this by two \[2\], _i.e._ by 15°
*   Add hour numbers (either via data labels or manually typed)

![](<Base64-Image-Removed>)

*   Insert first Pie chart (hour hand)
*   Insert second Pie chart (minute hand)
*   Remove legends, borders and chart backgrounds
*   Align all charts to same centre point.

![](<Base64-Image-Removed>)

**_Word to the Wise_**

This challenge shows Excel is more than grids and **SUM** formulae.  With just a few logical tricks and using such functions as **MOD**, **HOUR**, **MINUTE** with some careful chart settings, you can make an Excel version of a clock.  It’s quite amazing to see how Excel’s calculation logic and visual tools can work together so beautifully.

If you have tried building your own version, perhaps with a different layout or colour theme, congratulations — exploring new ideas is always part of the joy of Excel!

Feel free to get more complex: perhaps you want a second hand or the hands to “centre” round the precise angle.  It’s up to you!

__The Final Friday Fix will return on Friday 26 December 2025 with a new Excel Challenge.  In the meantime, please look out for the Daily Excel Tip on our home page and watch out for a new blog every business working day.__

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-november-2025-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-november-2025-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-november-2025-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-november-2025-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-november-2025-challenge/#0 "close")

top