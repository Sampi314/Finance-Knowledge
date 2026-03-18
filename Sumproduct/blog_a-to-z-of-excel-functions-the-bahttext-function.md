# A to Z of Excel Functions: The BAHTTEXT Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-bahttext-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The BAHTTEXT Function

*   October 16, 2016

A to Z of Excel Functions: The BAHTTEXT Function
================================================

A to Z of Excel Functions: The BAHTTEXT Function
================================================

17 October 2016

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **BAHTTEXT** function._

**The BAHTTEXT function**

Every now and then we unveil a pearl of a function, one that will rock your world and make you wonder how you ever lived without it. Today’s function is probably not going to be on that list for those outside of Thailand.

This function converts a number to Thai text and adds a suffix of “Baht”. You can change the Baht format to a different style in the Excel desktop application by using Regional and Language Options (Windows Start menu, Control Panel).

The **BAHTTEXT** function employs the following syntax to operate:

**BAHTTEXT(number)**

The **BAHTTEXT** function has the following argument only:

*   **number:** this is required and represents a number you want to convert to text, or a reference to a cell containing a number, or a formula that evaluates to a number.

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

I have to be honest, I am not quite sure why Microsoft has singled out Thai for this special treatment – especially as there is no equivalent to do this in English.

For the record (and probably of more relevance than the above for many), back in **Newsletter 33** (August 2015), we did actually enlighten readers how VBA code could be used to convert numbers to text by using the user defined function **_SpellNumber_**. To create this function, open the Visual Basic Editor in Excel (**ALT + F11**) and paste in the following code:

Option Explicit  
‘Main Function  
Function SpellNumber(ByVal MyNumber)  
    Dim Dollars, Cents, Temp  
    Dim DecimalPlace, Count  
    ReDim Place(9) As String  
    Place(2) = ” Thousand “  
    Place(3) = ” Million “  
    Place(4) = ” Billion “  
    Place(5) = ” Trillion “  
    ‘ String representation of amount.  
    MyNumber = Trim(Str(MyNumber))  
    ‘ Position of decimal place 0 if none.  
    DecimalPlace = InStr(MyNumber, “.”)  
    ‘ Convert cents and set MyNumber to dollar amount.  
    If DecimalPlace > 0 Then  
        Cents = GetTens(Left(Mid(MyNumber, DecimalPlace + 1) & \_  
                  “00”, 2))  
        MyNumber = Trim(Left(MyNumber, DecimalPlace – 1))  
    End If  
    Count = 1  
    Do While MyNumber <> “”  
        Temp = GetHundreds(Right(MyNumber, 3))  
        If Temp <> “” Then Dollars = Temp & Place(Count) & Dollars  
        If Len(MyNumber) > 3 Then  
            MyNumber = Left(MyNumber, Len(MyNumber) – 3)  
        Else  
            MyNumber = “”  
        End If  
        Count = Count + 1  
    Loop  
    Select Case Dollars  
        Case “”  
            Dollars = “No Dollars”  
        Case “One”  
            Dollars = “One Dollar”  
         Case Else  
            Dollars = Dollars & ” Dollars”  
    End Select  
    Select Case Cents  
        Case “”  
            Cents = ” and No Cents”  
        Case “One”  
            Cents = ” and One Cent”  
              Case Else  
            Cents = ” and ” & Cents & ” Cents”  
    End Select  
    SpellNumber = Dollars & Cents  
End Function

‘ Converts a number from 100-999 into text  
Function GetHundreds(ByVal MyNumber)  
    Dim Result As String  
    If Val(MyNumber) = 0 Then Exit Function  
    MyNumber = Right(“000” & MyNumber, 3)  
    ‘ Convert the hundreds place.  
    If Mid(MyNumber, 1, 1) <> “0” Then  
        Result = GetDigit(Mid(MyNumber, 1, 1)) & ” Hundred “  
    End If  
    ‘ Convert the tens and ones place.  
    If Mid(MyNumber, 2, 1) <> “0” Then  
        Result = Result & GetTens(Mid(MyNumber, 2))  
    Else  
        Result = Result & GetDigit(Mid(MyNumber, 3))  
    End If  
    GetHundreds = Result  
End Function

‘ Converts a number from 10 to 99 into text.  
Function GetTens(TensText)  
    Dim Result As String  
    Result = “”           ‘ Null out the temporary function value.  
    If Val(Left(TensText, 1)) = 1 Then   ‘ If value between 10-19…  
        Select Case Val(TensText)  
            Case 10: Result = “Ten”  
            Case 11: Result = “Eleven”  
            Case 12: Result = “Twelve”  
            Case 13: Result = “Thirteen”  
            Case 14: Result = “Fourteen”  
            Case 15: Result = “Fifteen”  
            Case 16: Result = “Sixteen”  
            Case 17: Result = “Seventeen”  
            Case 18: Result = “Eighteen”  
            Case 19: Result = “Nineteen”  
            Case Else  
        End Select  
    Else                                 ‘ If value between 20-99…  
        Select Case Val(Left(TensText, 1))  
            Case 2: Result = “Twenty “  
            Case 3: Result = “Thirty “  
            Case 4: Result = “Forty “  
            Case 5: Result = “Fifty “  
            Case 6: Result = “Sixty “  
            Case 7: Result = “Seventy “  
            Case 8: Result = “Eighty “  
            Case 9: Result = “Ninety “  
            Case Else  
        End Select  
        Result = Result & GetDigit \_  
            (Right(TensText, 1))  ‘ Retrieve ones place.  
    End If  
    GetTens = Result  
End Function

‘ Converts a number from 1 to 9 into text.  
Function GetDigit(Digit)  
    Select Case Val(Digit)  
        Case 1: GetDigit = “One”  
        Case 2: GetDigit = “Two”  
        Case 3: GetDigit = “Three”  
        Case 4: GetDigit = “Four”  
        Case 5: GetDigit = “Five”  
        Case 6: GetDigit = “Six”  
        Case 7: GetDigit = “Seven”  
        Case 8: GetDigit = “Eight”  
        Case 9: GetDigit = “Nine”  
        Case Else: GetDigit = “”  
    End Select  
End Function

You can subscribe to our monthly newsletter at the bottom of any SumProduct webpage.

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-bahttext-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-bahttext-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-bahttext-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-bahttext-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-bahttext-function/#0 "close")

top