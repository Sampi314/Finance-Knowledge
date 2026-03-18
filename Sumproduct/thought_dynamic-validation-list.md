# Dynamic Validation List

**Source:** https://sumproduct.com/thought/dynamic-validation-list/

---

[Home](https://sumproduct.com/)

\> Dynamic Validation List

*   September 20, 2019

Dynamic Validation List
=======================

VBA Blogs: Dynamic Validation List
==================================

20 September 2019

_Welcome back to the VBA blog. This week, we are going to learn how to use VBA to setup a dynamic validation list._

Today we are going to create VBA script to automatically setup a validation list with the worksheet name. It is a useful method to create what is known as a ‘catalogue’ from the worksheet names without manual operation.

Essentially, we would like to add the worksheet names to a validation list shown in the range **C3** below:

![](https://sumproduct.com/wp-content/uploads/2025/06/e774d10cbbb9450fc45efbe51abdf434-717.jpg)

The first step is to declare the relevant variables:

Dim i As Integer

Dim strList As String

Dim wrkSht As Worksheet

Then, we use a ‘For Loop’ to look through all the worksheets name in the current workbook and use an ‘If’ function to determine which worksheet name should be included in the validation list. In this instance, if the name of the worksheet is not equal to “Summary”, then we add the name to the string variable **strList** and use the character ‘,’ to separate different worksheet names as follows:

For Each wrkSht In Worksheets

        If wrkSht.Name <> “Summary” Then

            strList = strList & wrkSht.Name & “,”

        End If

Next wrkSht

The next step is to refer to the Summary worksheet. We located the range **C3** as the target cell for validation list. Firstly, we delete any existing data validation in this target cell and add a new validation list to range **C3**. The content of the validation list is then set to equal the string variable **strList** by using the parameter **Formula1**. Those of a nervous disposition may be pleased to learn that no Grands Prix were injured in the making of this procedure.

After assigning the data validation list, we set the worksheet variable **wrkSht** to nothing.

Set wrkSht = Nothing

Combing all the lines of code together, we get this:

Sub SheetsNameValidation()

    Dim i As Integer

    Dim strList As String

    Dim wrkSht As Worksheet

    For Each wrkSht In Worksheets

        If wrkSht.Name <> “Summary” Then

            strList = strList & wrkSht.Name & “,”

        End If

    Next wrkSht

    With Worksheets(“Summary”).Range(“C3”).Validation

        .Delete

        .Add Type:=xlValidateList, Formula1:=strList

    End With

    Set wrkSht = Nothing

End Sub

By using this method, we can dynamically add the worksheet name to the data validation list without manual operation.

See you next week for more VBA tips!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/dynamic-validation-list/#0)
    
*   [Register](https://sumproduct.com/thought/dynamic-validation-list/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/dynamic-validation-list/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/dynamic-validation-list/#0)

[](https://sumproduct.com/thought/dynamic-validation-list/#0 "close")

top