# Creating a Stopwatch in Excel (Basic + Toastmasters Style)

**Source:** https://trumpexcel.com/stopwatch-in-excel

---

[Skip to content](https://trumpexcel.com/stopwatch-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/stopwatch-in-excel/#below-title)

While working at IBM, I was a part of a [ToastMasters International](https://www.toastmasters.org/)
 club. It’s a place where you can improve your communication and leadership skills.

An interesting section in the weekly meetings was impromptu speaking. In this part of the meeting, a person was given a topic and he/she had to speak on it for 2 minutes. There was a designated person who used to time the speech and shows a green card at 1 minute, a yellow card at 1:30 minutes, and a red card after 2 minutes.

Usually, a smartphone or a watch is used to time the speech, and the time taken is recorded manually on a paper.

It often happens that the person forgets to show the colored cards or sometimes forgets to record the timing for the speakers (happened with me all the time). With these things in mind, I have created a stopwatch in Excel that would help time and record the speeches.

Let’s first learn how to create a basic stopwatch in Excel.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/stopwatch-in-excel/#)

How to Create a Stopwatch in Excel (Basic)
------------------------------------------

By a simple/basic stopwatch in Excel, I mean something that would start when we press the start button and stop when we press the stop button.

Something as shown below:

![StopWatch in Excel - Basic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20288%20140'%3E%3C/svg%3E)

**Download this Basic Stopwatch in Excel**[![Download File](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://www.dropbox.com/s/6jvltr0l0d323i1/StopWatch-Basic_v2.xlsm?dl=1)

To create this stopwatch in Excel, you need to know about the **Application**.**Ontime** method in VBA.

### Application.OnTime Method in VBA

Application.OnTime method can be used when you want to run a specified code in the future. For example, you may use it to show a message box to remind you to get up and stretch your legs after 1 hour or have medicines after 3 hours.

#### Syntax of Application.OnTime Method:

Application.OnTime(_EarliestTime_, _Procedure_, _LatestTime_, _Schedule_)

*   EarliestTime: The time when you want to run the procedure.
*   Procedure: The name of the procedure that should be run.
*   LatestTime (Optional): In case another code is running and your specified code can’t be run at the specified time, you can specify the LatestTime for which it should wait. For example, it could be EarliestTime + 45 (which means it will wait for 45 seconds for the other procedure to get completed). If even after 45 seconds the procedure it not able to run, it gets abandoned. If you don’t specify this, Excel would wait until the code can be run, and then run it.
*   Schedule (Optional): If set to True, it schedules new time procedure. If False, then it cancels the previously set procedure. By default, this is True.

#### An Example of Application.OnTime Method

Sub test()
Application.OnTime Now + TimeValue("00:00:05"), "ShowMessage"
End Sub

Sub ShowMessage()
MsgBox ("HELLO")
End Sub

The first part of the macro uses the Application.OnTime method and runs the procedure ShowMessage (in double quotes) after five seconds. The ShowMessage procedure simply shows the [message box](https://trumpexcel.com/vba-msgbox/)
 with the prompt HELLO.

You can use this format to run any procedure after a specified time from the current time.

Now using this concept, let’s look at the code for creating a simple stopwatch in Excel.

Dim NextTick As Date, t As Date
Sub StartStopWatch()
t = Time
Call StartTimer
End Sub

Sub StartTimer()
NextTick = Time + TimeValue("00:00:01")
Range("A1").Value = Format(NextTick - t - TimeValue("00:00:01"), "hh:mm:ss")
Application.OnTime NextTick, "StartTimer"
End Sub

Sub StopTimer()
On Error Resume Next
Application.OnTime EarliestTime:=NextTick, Procedure:="StartTimer", Schedule:=False
End Sub

This code has 3 parts:

*   The first part initializes the current time to the variable t. Then it calls another procedure StartTimer.
*   StartTimer procedure uses a variable NextTick which gets incremented by 1 with every passing second. In the worksheet, cell A1 has the running timer as we have specified NextTick – t -TimeValue(“00:00:01”), “hh:mm:ss”) to be the value in that cell. It then runs the StartTimer code again after every second.
*   StopTimer cancels the Application.Ontime procedure by making the schedule value False. This stops the timer.

Here is what you’ll get with the above code (I have assigned the macros to the start/stop buttons):

![StopWatch in Excel - Basic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20288%20140'%3E%3C/svg%3E)

This is a basic stopwatch in Excel.

I call it basic as you can not stop in middle and restart where you left. It will always restart from 1 when you press the start button.

Now that you have learned the basics of Application.OnTime method, you can easily tweak this to create whatever kind of stopwatch you want in Excel.

Also read: [Make VBA Code Pause or Delay (Using Sleep / Wait Commands)](https://trumpexcel.com/vba-sleep-wait/)

Stopwatch in Excel (For ToastMasters)
-------------------------------------

I have used the concept discussed above and created a Stopwatch in Excel that can be used in the Toastmasters meeting (which I mentioned at the beginning of this tutorial).

Here are the things that can be done using this stopwatch:

*   You can stop the timer and then restart again from the same time (recorded till then).
*   You can reset the timer. This sets the timer value to 0. As soon as you do that it automatically records the total time elapsed.
*   It changes the color of the timer box, depending on stopwatch value (this could be a good reminder to show the green/yellow/red cards).

Here is how it looks:

![Stopwatch in Excel - Demo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20588%20356'%3E%3C/svg%3E)

In this above demo, I have set the color change every five seconds. You can easily specify when you want the color to change (the green card at 1 min, yellow card at 1.5 minutes, and a red card at 2 minutes) by changing the values in the Calculation sheet.

As soon as you hit the reset button, the color of the timer would go back to white, the value of the timer would become 0, and it will record the time in column G.

_**Download the ToastMasters Style Stopwatch in Excel**_[![Download File](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://www.dropbox.com/s/849iyxwp8ntntr1/ToastMaster-StopWatch_TrumpExcel.xlsm?dl=1)

_Note: Since these files contain macro, you will have to [enable macros](https://trumpexcel.com/enable-macros-in-excel/)
 before using it. When you open the workbook, you’ll see a yellow button – Enable Content. Click on it to enable macros._

![Generate Military Alphabet Code in Excel - Enable Content](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20461%2034'%3E%3C/svg%3E)

If you create something cool using a timer, do share it with me.

**You May Also Like the Following Excel Tutorials:**

*   [Matrix Falling Numbers Effect in Excel using VBA](https://trumpexcel.com/matrix-falling-numbers-effect-in-excel-using-vba/)
    .
*   [How to Automatically Insert Date and Time Stamp in Excel](https://trumpexcel.com/date-timestamp-excel/)
    .
*   [Using Loops in Excel VBA](https://trumpexcel.com/vba-loops/)
    .
*   [How to Calculate Time in Excel](https://trumpexcel.com/calculate-time-in-excel/)
    
*   [Free Excel Templates](https://trumpexcel.com/free-excel-templates/)
    .
*   [Creating a Dashboard in Excel](https://trumpexcel.com/creating-excel-dashboard/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

18 thoughts on “How to Create a Stopwatch in Excel (Basic + ToastMasters Style)”
--------------------------------------------------------------------------------

1.  Hi. I find it very useful, but I need to record the time in hundreds of seconds. Please advise if the file can be changed to preform this.
    
    [Reply](https://trumpexcel.com/stopwatch-in-excel/#comment-12493)
    
2.  Excellent. Very useful
    
    [Reply](https://trumpexcel.com/stopwatch-in-excel/#comment-11830)
    
3.  Excellent Sir. Thank You Very Much.
    
    [Reply](https://trumpexcel.com/stopwatch-in-excel/#comment-10949)
    
4.  Great work…
    
    [Reply](https://trumpexcel.com/stopwatch-in-excel/#comment-10794)
    
5.  thanks for the article and the document.
    
    [Reply](https://trumpexcel.com/stopwatch-in-excel/#comment-10534)
    
6.  Hi,  
    this works great except now when I have another spreadsheet open and the clock is running the Undo button is unavailable. As soon as I Stop the clock undo is available again. Can anyone help me with this please?
    
    Option Explicit
    
    Dim NextTick As Date, t As Date, PreviousTimerValue As Date
    
    Private Sub StartTime()  
    PreviousTimerValue = Calculations.Range(“A1”).Value  
    t = Time  
    Call ExcelStopWatch  
    End Sub
    
    Private Sub ExcelStopWatch()  
    Calculations.Range(“A1”).Value = Format(Time – t + PreviousTimerValue, “hh:mm:ss”)  
    NextTick = Now + TimeValue(“00:00:01”)
    
    If Calculations.Range(“A1”).Value > Calculations.Range(“B3”) Then  
    With Sheet4.Shapes(“TimeBox”)  
    .Fill.ForeColor.RGB = RGB(0, 255, 0)  
    End With
    
    End If
    
    Application.OnTime NextTick, “ExcelStopWatch”  
    End Sub
    
    Sub StopClock()  
    On Error Resume Next  
    Application.OnTime earliesttime:=NextTick, procedure:=”ExcelStopWatch”, schedule:=False  
    With Sheet4.Shapes(“TimeBox”)  
    .Fill.ForeColor.RGB = RGB(255, 0, 0)  
    End With  
    End Sub
    
    [Reply](https://trumpexcel.com/stopwatch-in-excel/#comment-10325)
    
    *   I’ve found the problem but not the solution. If I don’t colour the shape it works. Has anyone a solution as to how to colour a shape not using vba.  
        Trying to use conditional formatting but can’t get it figured out.
        
        ‘If Calculations.Range(“A1”).Value > Calculations.Range(“B3”) Then
        
        ‘ With Sheet4.Shapes(“TimeBox”)  
        ‘ .Fill.ForeColor.RGB = RGB(0, 255, 0)  
        ‘ End With
        
        ‘End If
        
        [Reply](https://trumpexcel.com/stopwatch-in-excel/#comment-10326)
        
7.  Try XNote Stopwatch.
    
    [Reply](https://trumpexcel.com/stopwatch-in-excel/#comment-10029)
    
8.  Dear Mr Bansal,
    
    I’ve downloaded theToastMaster Stopwatch. I want to make it recording without clicking the reset button by using spesific criteria, for example Stopwatch.Range(“I11”).Value = 1. I’m not good at VBA. So sorry for this silly question.
    
    Hope you can help me here. I’m looking forward your reply. Thank you.
    
    [Reply](https://trumpexcel.com/stopwatch-in-excel/#comment-10009)
    
9.  Dear Mr Bansal,
    
    I’ve downloaded theToastMaster Stopwatch. I want to make it autorecording without clicking the reset button by using spesific criteria, for example Stopwatch.Range(“I11”).Value = 1. I’m not good in VBA. So sorry for this silly question.
    
    Hope you can help me here. I’m looking forward your reply. Thank you.
    
    [Reply](https://trumpexcel.com/stopwatch-in-excel/#comment-10008)
    
10.  The stopwatch is a great tool – thanks! Just one question: sometimes it simply stops, no pun intended. Is there any explanation or workaround? Thanks.
    
    [Reply](https://trumpexcel.com/stopwatch-in-excel/#comment-9507)
    
11.  Hello. It is very useful the toast masters stopwatch for me. I need to get over some rows without data inserted in them and continue to count. how can I do this? Thank you.
    
    [Reply](https://trumpexcel.com/stopwatch-in-excel/#comment-9069)
    
12.  Hello, I am working on a backup system for timing a 5K running event. How can I modify the code for the clock to continue run with the reset button. Thank you!
    
    [Reply](https://trumpexcel.com/stopwatch-in-excel/#comment-8980)
    
13.  If I needed this to show tenths of a second, what would I need to do?
    
    [Reply](https://trumpexcel.com/stopwatch-in-excel/#comment-7950)
    
    *   I am afraid VBA can’t show a tenth of a second
        
        [Reply](https://trumpexcel.com/stopwatch-in-excel/#comment-8524)
        
14.  StopWatch: starts at 1 not at 0.  
    ToastMaster-StopWatch: starts at 0, but you don’t need PreviousTimerValue, just delete it.
    
    [Reply](https://trumpexcel.com/stopwatch-in-excel/#comment-2821)
    
    *   Thanks for commenting Frank.. Good catch.. I have corrected the basic stopwatch. Now it start at 0.  
        In ToastMasters Stopwatch, I have used the PreviousTimerValue to make sure it doesn’t restart from 0 when we click on Start, rather It starts where we left. To reset it to 0, you need to press the reset button.
        
        [Reply](https://trumpexcel.com/stopwatch-in-excel/#comment-2822)
        
        *   If you want to be able to stop and restart (for whatever reason) PreviousTimerValue certainly makes sense.
            
            [Reply](https://trumpexcel.com/stopwatch-in-excel/#comment-2825)
            

### Leave a Comment [Cancel reply](https://trumpexcel.com/stopwatch-in-excel/#respond)

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