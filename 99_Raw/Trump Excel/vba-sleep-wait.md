# Make VBA Code Pause or Delay (Using Sleep / Wait Commands)

**Source:** https://trumpexcel.com/vba-sleep-wait

---

[Skip to content](https://trumpexcel.com/vba-sleep-wait/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/vba-sleep-wait/#below-title)

![Make VBA deliver pause the code using sleep and Wait](https://trumpexcel.com/wp-content/uploads/2023/01/Make-VBA-Code-Pause-or-Delay-Using-Sleep-Wait-Commands.png)

Sometimes, when working with a VBA code, you may want to put a pause on the code execution or delay the code running for a few seconds or tell a specific time.

For example, if I’m using my VBA code to open a .exe file or any other format file (such as Word or PowerPoint), and I want a delay in my code so that I can see that the file has opened correctly.

This can easily be done using the inbuilt SLEEP and WAIT commands in Excel VBA.

Let’s look at a couple of examples you can use to delay or pause your VB code in Excel.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/vba-sleep-wait/#)

Using VBA WAIT Command to Delay or Pause the Code
-------------------------------------------------

Using the WAIT method in Excel VBA, you can stop the code execution for a specific amount of seconds, minutes, and hours, all up to the specified time (say 3 PM or 9 AM)

Below is the VBA code that would use the wait command to delay the code execution by 5 seconds and then shows the message box with the text “Let’s Go”

    Sub Wait5Sec()
    If Application.Wait(Now + TimeValue("00:00:05")) Then
     MsgBox "Let's Go"
    End If
    End Sub

I have used the Application.Wait method within an [IF Then condition](https://trumpexcel.com/if-then-else-vba/)
, which only shows us the [message box](https://trumpexcel.com/vba-msgbox/)
 once the wait time is over.

![Message box after the code has been delayed](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20127%20133'%3E%3C/svg%3E)

Note that the Application.Wait method needs a time input so that it knows what time it needs to wait before moving to the next line of code.

In this example code, I have used Now + TimeValue(“00:00:05”) – where Now is the time when the code is executed (which is automatically picked up from your system setting), and then a 5-second delay is added to it.

**Caution**: When you use the WAIT command in VBA, while the delay is in progress, you will not be able to do anything in your Excel file. It would be as if your Excel has frozen, and it would only unfreeze once the wait time is over.

Below is how my cursor changes when the code is running, and I can’t select anything in the worksheet.

![Excel freezes when code is running](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20701%20212'%3E%3C/svg%3E)

You can also use the WAIT method to delay your code execution till a specific time.

For example, below is the VB code that would keep code execution on hold till the time on your system is 11:30 AM

    Sub WaitTill11AM()
    If Application.Wait "11:30:0" Then
     MsgBox "It's Time"
    End If
    End Sub

_I strongly recommend you create a backup copy when working with the Wait or the Sleep command in Excel VBA._

Using VBA SLEEP Command to Delay or Pause the Code
--------------------------------------------------

Another way to pause a delay of the VBA code is by using the SLEEP command.

Sleep is a Windows function and not a VBA method.

Therefore, if you want to use the SLEEP method in your code, you will first have to reference the Windows DLL that has the SLEEP command so that we can use it in our VBA code.

This is pretty straightforward. All you have to do is add a standard line of code above your actual VBA code that you want to run (see the code below, you can copy it from my code)

Below is the VBA code that would use the sleep command to pause the code for 10 seconds

    #If VBA7 Then
    
    'For 64-Bit MS Office
        Public Declare PtrSafe Sub Sleep Lib "kernel32" (ByVal Milliseconds As LongPtr)
    #Else
    'For 32-Bit MS Office
        Public Declare PtrSafe Sub Sleep Lib "kernel32" (ByVal Milliseconds As Long) 
    #End If
    
    Sub Sleep10Sec()
         Sleep (5000)
         MsgBox "It's Time"
         'Your Code can go here
    End Sub

In the above code, the first seven lines _#If VBA7….#End If_ is the declaration that refers to kernel32 DLL file of Windows.

Only after we have made this declaration can be used the SLEEP function in our VBA code (else it won’t work)

Unlike the WAIT function, where you need to specify the time value till you want the code to be delayed, the SLEEP function takes the delay value in milliseconds. In our code, I have used Sleep (5000), this would pause my code for 5 seconds.

If you want to pause your code for one second, you can use Sleep (5000)

Just like with the WAIT function, when you pause the code using the SLEEP function, Excel would freeze, and you won’t be able to do anything while the delay is in progress.

WAIT and SLEEP commands in Excel can have a few milliseconds of variation in the delay. So if you want to delay your VBA code for 1 second, it may be a little over or under that (it can be off by a few milliseconds). This hasn’t been an issue in any projects I worked with.

In this tutorial, I showed you how to pause or delay your VBA code in Excel by using the WAIT or SLEEP commands.

With the WAIT command, you need to specify the time till which you want to delay the code execution, and with SLEEP, you need to specify the time period itself for which you want to pause the code execution.

**Other Excel articles you may also like:**

*   [How to Create a Stopwatch in Excel (Basic + ToastMasters Style)](https://trumpexcel.com/stopwatch-in-excel/)
    
*   [Excel VBA Events – An Easy (and Complete) Guide](https://trumpexcel.com/vba-events/)
    
*   [Matrix Falling Numbers Effect in Excel using VBA](https://trumpexcel.com/matrix-falling-numbers-effect-in-excel-using-vba/)
    .
*   [How to Automatically Insert Date and Time Stamp in Excel](https://trumpexcel.com/date-timestamp-excel/)
    .
*   [Using Loops in Excel VBA](https://trumpexcel.com/vba-loops/)
    .
*   [How to Open Excel Files Using VBA (Examples)](https://trumpexcel.com/open-excel-files-using-vba/)
    
*   [Using VBA FileSystemObject (FSO) in Excel](https://trumpexcel.com/vba-filesystemobject/)
    
*   [Excel VBA Exit Sub Statement](https://trumpexcel.com/excel-vba/exit-sub/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/vba-sleep-wait/#respond)

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