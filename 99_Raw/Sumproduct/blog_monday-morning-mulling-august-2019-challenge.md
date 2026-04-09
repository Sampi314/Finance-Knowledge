# Monday Morning Mulling: August 2019 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-august-2019-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: August 2019 Challenge

*   September 1, 2019

Monday Morning Mulling: August 2019 Challenge
=============================================

Monday Morning Mulling: August 2019 Challenge
=============================================

2 September 2019

_On the final Friday of each month, we set a Power BI or Excel problem for you to puzzle over for the weekend. On the Monday, we publish a solution. If you think there is an alternative answer, feel free to email us. We’ll feel free to ignore you._

To recap, the problem we presented last week was to challenge you to create multiple worksheets from a data list. The intention is to dynamically create the worksheets without manual intervention.

Essentially, we want to generate multiple worksheets with the names from the data list shown below:

![](<Base64-Image-Removed>)

**_Suggested Solution_**

One simple way here is to use VBA to look through the value of each cell in the data list and assign the value to each worksheet created after the **Summary** worksheet.

The first step is to set up a named range as shown below. We define the cell range **A2** to **A13** as the data list and assign a name tag **Source** to this range as shown below.

![](<Base64-Image-Removed>)

The next step is to declare the relevant variables.

Dim wksht As Worksheet

Dim rng As Range

Dim sName As String

Then, we set the variable **wksht** as the active worksheet and turn off the **ScreenUpdating** application. If **ScreenUpdating** property were set to false, it will speed up the macro operation.

Set wksht =ActiveSheet

Application.ScreenUpdating = False

Next, we used an ‘For Loop’ to look up each value in the named range and assign the range value to the string variable **sName**. Then, we use an ‘If’ statement to determine the length of the variable **sName.** If the length is greater than zero, then we add a new worksheet after the last page and set the worksheet name equal to the value stored in variable **sName**, _viz._

For Each rng In Range(“Source”)

sName = rng.Value

If Len(sName) > 0 Then

Worksheets.Add after:=Worksheets(Worksheets.Count)

ActiveSheet.Name = sName

End If

Next rng

Next, we go back to the summary worksheet and turn on the **ScreenUpdating** application once more.

Worksheets(“Summary”).Select

Application.ScreenUpdating = True

Combing all the lines of code together, we get this:

Sub AddWorksheetsFromSelection()

Dim wksht As Worksheet

Dim rng As Range

Dim sName As String

Set wksht = ActiveSheet

Application.ScreenUpdating = False

For Each rng In Range(“Source”)

sName = rng.Value

If Len(sName) > 0 Then

Worksheets.Add after:=Worksheets(Worksheets.Count)

ActiveSheet.Name = sName

End If

Next rng

Worksheets(“Summary”).Select

Application.ScreenUpdating = True

End Sub

By using this method, we could create multiple worksheets from the named range without repetitive manual intervention.

_The Final Friday Fix will return on 27th September with a new Challenge. In the meantime, please look out for the Daily Excel Tip on our home page and watch out for a new blog every business workday._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-august-2019-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-august-2019-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-august-2019-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-august-2019-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-august-2019-challenge/#0 "close")

top