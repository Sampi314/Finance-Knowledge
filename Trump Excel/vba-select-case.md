# Excel VBA Select Case Statement - Explained with Examples

**Source:** https://trumpexcel.com/vba-select-case

---

[Skip to content](https://trumpexcel.com/vba-select-case/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/vba-select-case/#below-title)

Excel VBA has the [IF Then Else](https://trumpexcel.com/if-then-else-vba/)
 construct that you can use to analyze multiple conditions and execute codes based on these conditions.

Another similar construct that allows you to check for multiple conditions is the **SELECT CASE** statement.

Select Case is useful when you have three or more conditions that you want to check. You can also use this with two conditions (but I feel If Then Else is easier to use in those cases).

A simple example where the Select Case statement is useful when you want to get the grade of a student based on the marks he/she has scored (covered as an example later in this tutorial).

Note: All the example codes covered in this tutorial are meant to be placed in a module in VBA.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/vba-select-case/#)

Select Case Syntax
------------------

Below is the syntax of Select Case in Excel VBA:

Select Case Test\_Expression

Case Value\_1
Code Block when Test\_Expression = Value\_1

Case Value\_2
Code Block when Test\_Expression = Value\_2

Case Value\_3
Code Block when Test\_Expression = Value\_3

Case Else
Code Block when none of the case conditions are met

End Select

*   Test\_Expression: This is the expression whose value we analyze by using different cases (explained better with the examples below).
*   Condition\_1, Condition\_2,…: These are the conditions on which the text expression is tested. If it meets the condition, then the code block for the given condition is executed.

For every Select Case statement that you use, you need to use the End Select statement.

**Note:** As soon as a condition is met, VBA exits the select case construct. So if you have five conditions, and the second condition is met, VBA would exit Select Case – and the rest of the conditions will not be tested.

Select Case Examples
--------------------

Now to better understand how to use Select Case statement in VBA, let’s go through a few examples.

Note that most of the examples in this tutorial are meant to explain the concept. These may or may not be the best way to get the work done.

Let’s start with a simple example of see how Select Case allows us to check for conditions.

### Example 1 – Check the Numbers

In the below example, the code asks the user to enter any number between 1 and 5, and then shows a message box with the number the user entered.

Sub CheckNumber()
Dim UserInput As Integer
UserInput = InputBox("Please enter a number between 1 and 5")

Select Case UserInput

Case 1
MsgBox "You entered 1"

Case 2
MsgBox "You entered 2"

Case 3
MsgBox "You entered 3"

Case 4
MsgBox "You entered 4"

Case 5
MsgBox "You entered 5"

End Select
End Sub

Note that this code is far from useful and is not even foolproof. For example, if you enter 6 or any string, it would do nothing. But as I mentioned, my intent here is to showcase how Select Case works.

### Example 2 – Using Select Case with IS Condition

You can use an IS condition with the Select Case construct to check for the value of numbers.

The below code checks whether the input number is greater than 100 or not.

Sub CheckNumber()
Dim UserInput As Integer
UserInput = InputBox("Please enter a number")

Select Case UserInput

Case Is < 100
MsgBox "You entered a number less than 100"

Case Is >= 100
MsgBox "You entered a number more than (or equal to) 100"

End Select
End Sub

### Example 3 – Using Case Else to Catch All

In the above example, I used two conditions (less than 100 or greater than or equal to 100).

Instead of the second case with a condition, you can also use Case Else.

Case Else acts as a catch-all and anything which doesn’t fall into any of the previous cases is treated by the Case Else.

Below is an example code where I have used Case Else:

Sub CheckNumber()
Dim UserInput As Integer
UserInput = InputBox("Please enter a number")

Select Case UserInput

Case Is < 100
MsgBox "You entered a number less than 100"

Case Else
MsgBox "You entered a number more than (or equal to) 100"

End Select
End Sub

### Example 4 – Using a Range of Numbers

In Select Case, you can also check for a range of numbers.

The below code asks for an [input and shows a message](https://trumpexcel.com/input-message-in-excel/)
 box based on the value.

Sub CheckNumber()
Dim UserInput As Integer
UserInput = InputBox("Please enter a number between 1 and 100")

Select Case UserInput

Case 1 To 25
MsgBox "You entered a number less than 25"

Case 26 To 50
MsgBox "You entered a number between 26 and 50"

Case 51 To 75
MsgBox "You entered a number between 51 and 75"

Case 75 To 100
MsgBox "You entered a number more than 75"

End Select
End Sub

### Example 5 – Get the Grade based on the Marks Scored

So far we have seen basic examples (which are not really useful in the practical world).

Here is an example which is closer to a real-world example where you can use Select Case in Excel VBA.

The following code will give you the grade a student gets based on the marks in an exam.

Sub Grade()
Dim StudentMarks As Integer
Dim FinalGrade As String
StudentMarks = InputBox("Enter Marks")

Select Case StudentMarks

Case Is < 33
FinalGrade = "F"

Case 33 To 50
FinalGrade = "E"

Case 51 To 60
FinalGrade = "D"

Case 60 To 70
FinalGrade = "C"

Case 70 To 90
FinalGrade = "B"

Case 90 To 100
FinalGrade = "A"

End Select
MsgBox "The Grade is " & FinalGrade

End Sub

The above code asks the user for the marks and based on it, shows a [message box](https://trumpexcel.com/vba-msgbox/)
 with the final grade.

In the above code, I have specified all the conditions – for marks 0 – 100.

Another way to use Select Case is to use a Case Else at the end. This is useful when you have accounted for all the conditions and then specify what to do when none of the conditions is met.

The below code is a variation of the Grade code with a minor change. In the end, it has a Case else statement, which will be executed when none of the above conditions are true.

Sub CheckOddEven()
Dim StudentMarks As Integer
Dim FinalGrade As String
StudentMarks = InputBox("Enter Marks")
Select Case StudentMarks
Case Is < 33
FinalGrade = "F"

Case 33 To 50
FinalGrade = "E"

Case 51 To 60
FinalGrade = "D"

Case 60 To 70
FinalGrade = "C"

Case 70 To 90
FinalGrade = "B"

Case Else
FinalGrade = "A"

End Select
MsgBox "The Grade is " & FinalGrade

End Sub

### Example 6 – Creating a Custom Function (UDF) using Select Case

In the above example, the code asked the user for the marks input.

You can also create a [custom function (User Defined Function)](https://trumpexcel.com/user-defined-function-vba/)
 that can be used just like any regular worksheet function, and which will return the grade of the students.

Below is the code that will create the custom formula:

Function GetGrade(StudentMarks As Integer)
Dim FinalGrade As String

Select Case StudentMarks

Case Is < 33
FinalGrade = "F"

Case 33 To 50
FinalGrade = "E"

Case 51 To 60
FinalGrade = "D"

Case 60 To 70
FinalGrade = "C"

Case 70 To 90
FinalGrade = "B"

Case Else
FinalGrade = "A"

End Select
GetGrade = FinalGrade

End Function

Once you have this code in the module, you can use the function GetGrade in the worksheet as shown below.

![Select Case Statement in Excel VBA - Get Grade Custom Function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20440%20295'%3E%3C/svg%3E)

### Example 7 – Check ODD / EVEN with Select Case

Below is an example code where I check whether the number in cell A1 is odd or even.

Sub CheckOddEven()
CheckValue = Range("A1").Value

Select Case (CheckValue Mod 2) = 0

Case True
MsgBox "The number is even"

Case False
MsgBox "The number is odd"

End Select
End Sub

### Example 8 – Checking for Weekday/Weekend (Multiple Conditions)

You can also use Select Case to check for multiple values in the same case.

For example, the below code uses the current date to show whether today is a weekday or weekend (where weekend days are Saturday and  Sunday)

Sub CheckWeekday()
Select Case Weekday(Now)

Case 1, 7
MsgBox "Today is a Weekend"

Case Else
MsgBox "Today is a Weekday"

End Select
End Sub

In the above code, we check for two conditions (1 and 7) in the same case.

Note: [Weekday function](https://trumpexcel.com/excel-weekday-function/)
 returns 1 for Sunday and 7 for Saturday.

### Example 9 – Nested Select Case Statements

You can also nest one Select Case statement within other.

Below is a code that checks whether a day is a weekday or a weekend, and if it’s a weekend, then it will display whether it’s a Saturday or a Sunday.

Sub CheckWeekday()
Select Case Weekday(Now)

Case 1, 7
   Select Case Weekday(Now)
   Case 1
      MsgBox "Today is Sunday"
   Case Else
      MsgBox "Today is Saturday"
  End Select

Case Else
MsgBox "Today is a Weekday"
End Select
End Sub

In the above code, I have nested the Select Case to check whether the weekend is a Saturday or a Sunday.

Note: The example shown above is to explain the concept. This is not the best or the most practical way to find out weekday/weekend.

### Example 10 – Checking Text String with Select Case

You can check specific strings using Select Case and then execute code based on it.

In the example code below, it asks the user to enter their department name and shows the name of the person they should connect with for onboarding.

Sub OnboardConnect()
Dim Department As String
Department = InputBox("Enter Your Department Name")

Select Case Department

Case "Marketing"
MsgBox "Please connect with Bob Raines for Onboarding"

Case "Finance"
MsgBox "Please connect with Patricia Cruz for Onboarding"

Case "HR"
MsgBox "Please connect with Oliver Rand for Onboarding"

Case "Admin"
MsgBox "Please connect with Helen Hume for Onboarding"

Case Else
MsgBox "Please connect with Tony Randall for Onboarding"

End Select
End Sub

Hope all the examples above were helpful in understanding the concept and application of Select Case in Excel VBA.

**You May Also Like the Following VBA Tutorials:**

*   [Excel VBA Loops – For Next, Do While, Do Until, For Each.](https://trumpexcel.com/vba-loops/)
    
*   [For Next Loop in Excel VBA.](https://trumpexcel.com/for-next-loop-excel-vba/)
    
*   [How to Record a Macro in Excel](https://trumpexcel.com/record-macro-vba/)
    .
*   [VBA Exit Sub Statement](https://trumpexcel.com/excel-vba/exit-sub/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/vba-select-case/#respond)

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