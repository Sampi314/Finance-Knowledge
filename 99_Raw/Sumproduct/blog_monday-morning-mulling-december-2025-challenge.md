# Monday Morning Mulling: December 2025 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-december-2025-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: December 2025 Challenge

*   December 29, 2025

Monday Morning Mulling: December 2025 Challenge
===============================================

_On the final Friday of each month, we set an Excel / Power Pivot / Power Query / Power BI problem for you to puzzle over for the weekend.  On the Monday, we publish a solution.  If you think there is an alternative answer, feel free to email us.  We’ll feel free to ignore you._

**_The Challenge_**

Hands up if you “clocked” this puzzle?  [Last time](https://sumproduct.com/blog/final-friday-fix-november-2025-challenge/)
, we challenged you to build an analogue clock in Excel complete with rotating hands. This month’s challenge was to create a fully working, self-updating digital clock in Excel similar to the following:

![](<Base64-Image-Removed>)

Your clock must:

*   show the current system time in HH:MM format.

You were able to use **Dynamic Arrays**, [**LET**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-let-function/)
, **TEXT**, [**NOW**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-now-function/)
 and any other Excel worksheet functions, but no event triggers and no hidden code were allowed.

You can download the original question file [here](https://sumproduct.com/wp-content/uploads/2025/12/SP-Excel-Digital-Clock-Challenge.xlsx)
.

As always, there were some requirements:

*   you had to ensure the solution was dynamic so that it updated when new placeholders or replacement values were added
*   no VBA or Power Query was allowed; this was purely a formula challenge.

**_Suggested Solution_**

You can find our Excel file [here](https://sumproduct.com/wp-content/uploads/2025/12/SP-Excel-Digital-Clock-Solution.xlsx)
, which shows our suggested solution.  The steps are detailed below.

**1.  TIME INPUT**

In this case, the time input is stored in cell **F11**, showing the current time. You can also change it to be a manual input, which allows users to test any time they wish.

![](<Base64-Image-Removed>)

**2.  CREATE NUMBERS AND NAMED RANGES**

The foundation of the clock is a set of named ranges representing digits zero \[0\] to nine \[9\] and the colon separator. Each digit is stored as a **5 × 3 grid**, where:

*   **“X”** marks a lit segment
*   Blank cells mark an unlit segment

![](<Base64-Image-Removed>)

Each digit is saved as a named range:

![](<Base64-Image-Removed>)

These named ranges allow us to “draw” digits dynamically using formulae—no VBA required.

**3.  CHANGE THE FORMAT OF THE TIME INPUT**

The time input is stored in **cell F11**:

**\=NOW()**

As [**NOW**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-now-function/)
 returns a serial number (_e.g_. 45999.5881…), we must convert it into a consistent text format:

**H27:** **\=TEXT(F11,”HH:MM”)**

Benefits of using **TEXT()**:

*   preserves leading zeros (_e.g_. “09:05”)
*   always returns a five-character string
*   ensures fixed positions for hours, colon and minutes.

This makes it easy to extract each individual character.

**4.  PARSE INDIVIDUAL CHARACTERS**

Next, we break the formatted time into separate elements in cell **H32**:

**\=IFERROR(VALUE(MID(H27,SEQUENCE(,5),1)),MID(H27,SEQUENCE(,5),1))**

In effect:

*   [**SEQUENCE**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-sequence-function/)
    **(,5)** produces {1,2,3,4,5}
*   **MID()** extracts each character
*   **VALUE()** converts digits into numbers
*   **IFERROR()** preserves the colon, which cannot be converted.

For “14:25”, the output is:

**{1, 4, “:”, 2, 5}**

This spills across **H32:L32**.

![](<Base64-Image-Removed>)

**5.  ASSEMBLE THE DISPLAY**

This is where the magic happens. In cell **H39**, we build the clock using one elegant dynamic array formula:

**\=DROP(REDUCE(0,H32#,LAMBDA(x,y,  
HSTACK(x,  
CHOOSE(IF(y=0,10,IF(y=”:”,11,y)),N\_1,N\_2,N\_3,N\_4,N\_5,N\_6,N\_7,N\_8,N\_9,N\_0,N\_Colon),  
N\_Padding  
))),,1)**

It works as follows:

*   [**REDUCE**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-reduce-function/)
     iterates through each digit
*   [**LAMBDA**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-lambda-function/)
     stacks the previously built section with the new digit
*   [**CHOOSE**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-choose-function/)
     selects the correct named range
*   **[HSTACK](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-hstack-function/)
    ** stacks digits horizontally with padding
*   [**DROP**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-drop-function/)
     removes the initial column.

The result is a spill range representing the digital clock layout.

**6.  APPLY CONDITIONAL FORMATTING**

The formula produces “X” for lit segments and blank cells for unlit ones.  Conditional formatting turns this into a visual LED-style display.

![](<Base64-Image-Removed>)

**_Conclusion_**

This dynamic digital clock demonstrates how powerful modern Excel has become.  By combining

*   structured named ranges
*   flexible dynamic array formulae
*   reusable **[LAMBDA](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-lambda-function/)
    ** logic
*   smart conditional formatting

We can create visual elements that once required macros or specialist tools.  This approach opens the door to dashboards, timers, counters and other creative spreadsheet designs.

![](<Base64-Image-Removed>)

**_Word to the Wise_**

The digital clock project looks complex at first, but every part builds logically on the previous step. Once you understand **REDUCE**, **LAMBDA** and named ranges, you unlock a world of dynamic visual tools inside Excel.  Use these techniques to surprise your audience and elevate your dashboard designs.

___The Final Friday Fix will return on Friday 30 January 2026 with a new Excel Challenge.  In the meantime, please look out for the Daily Excel Tip on our home page and watch out for a new blog every business working day.___

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-december-2025-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-december-2025-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-december-2025-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-december-2025-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-december-2025-challenge/#0 "close")

top