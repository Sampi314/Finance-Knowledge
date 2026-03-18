# Best Excel Tip Ever?

**Source:** https://sumproduct.com/news/best-excel-tip-ever/

---

[Home](https://sumproduct.com/)

\> Best Excel Tip Ever?

*   July 30, 2024

Best Excel Tip Ever?
====================

Best Excel Tip Ever?
====================

30 July 2024

One of the most common questions we are ever asked is how to translate a number into words, _e.g._

![](https://sumproduct.com/wp-content/uploads/2025/05/2b7f9c5ad91e780dc6108830a5c33cbc.jpg)

You may even have encountered this problem for yourself. Microsoft suggests you write VBA code to create a user-defined function (let’s not assume they’d actually create a function!):

Option  
Explicit

‘Main  
Function

Function  
SpellNumber(ByVal MyNumber)

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

    DecimalPlace = InStr(MyNumber,  
“.”)

    ‘ Convert cents and set MyNumber to dollar  
amount.

    If DecimalPlace > 0 Then

        Cents = GetTens(Left(Mid(MyNumber,  
DecimalPlace + 1) & \_

                  “00”, 2))

        MyNumber = Trim(Left(MyNumber,  
DecimalPlace – 1))

    End If

    Count = 1

    Do While MyNumber <> “”

        Temp = GetHundreds(Right(MyNumber, 3))

        If Temp <> “” Then  
Dollars = Temp & Place(Count) & Dollars

        If Len(MyNumber) > 3 Then

            MyNumber = Left(MyNumber,  
Len(MyNumber) – 3)

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

            Dollars = Dollars & ”  
Dollars”

    End Select

    Select Case Cents

        Case “”

            Cents = ” and No Cents”

        Case “One”

            Cents = ” and One Cent”

              Case Else

            Cents = ” and ” &  
Cents & ” Cents”

    End Select

    SpellNumber = Dollars & Cents

End  
Function

‘ Converts  
a number from 100-999 into text

Function  
GetHundreds(ByVal MyNumber)

    Dim Result As String

    If Val(MyNumber) = 0 Then Exit Function

    MyNumber = Right(“000” &  
MyNumber, 3)

    ‘ Convert the hundreds place.

    If Mid(MyNumber, 1, 1) <>  
“0” Then

        Result = GetDigit(Mid(MyNumber, 1, 1))  
& ” Hundred “

    End If

    ‘ Convert the tens and ones place.

    If Mid(MyNumber, 2, 1) <>  
“0” Then

        Result = Result &  
GetTens(Mid(MyNumber, 2))

    Else

        Result = Result &  
GetDigit(Mid(MyNumber, 3))

    End If

    GetHundreds = Result

End  
Function

‘ Converts  
a number from 10 to 99 into text.

Function  
GetTens(TensText)

    Dim Result As String

    Result = “”           ‘ Null out the temporary function  
value.

    If Val(Left(TensText, 1)) = 1 Then   ‘ If value between 10-19…

        Select Case Val(TensText)

            Case 10: Result = “Ten”

            Case 11: Result =  
“Eleven”

            Case 12: Result =  
“Twelve”

            Case 13: Result =  
“Thirteen”

            Case 14: Result =  
“Fourteen”

            Case 15: Result =  
“Fifteen”

            Case 16: Result =  
“Sixteen”

            Case 17: Result =  
“Seventeen”

            Case 18: Result =  
“Eighteen”

            Case 19: Result =  
“Nineteen”

            Case Else

        End Select

    Else                                 ‘ If value  
between 20-99…

        Select Case Val(Left(TensText, 1))

            Case 2: Result = “Twenty  
“

            Case 3: Result = “Thirty  
“

            Case 4: Result = “Forty “

            Case 5: Result = “Fifty “

            Case 6: Result = “Sixty “

            Case 7: Result = “Seventy  
“

            Case 8: Result = “Eighty  
“

            Case 9: Result = “Ninety  
“

            Case Else

        End Select

        Result = Result & GetDigit \_

            (Right(TensText, 1))  ‘ Retrieve ones place.

    End If

    GetTens = Result

End  
Function

‘ Converts  
a number from 1 to 9 into text.

Function  
GetDigit(Digit)

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

End  
Function

Yuck.

Others on the internet will suggest you can use a recursive **LAMBDA** function, let’s call it **NUMBERTEXT**, which can do something similar up to a given value, _e.g._

**\=LAMBDA(num, LET(singleDigits, {“Zero”,”One”,”Two”,”Three”,”Four”,”Five”,”Six”,”Seven”,”Eight”,”Nine”},  
teens, {“Ten”,”Eleven”,”Twelve”,”Thirteen”,”Fourteen”,”Fifteen”,”Sixteen”,”Seventeen”,”Eighteen”,”Nineteen”},  
tens,  
{“”,””,”Twenty”,”Thirty”,”Forty”,”Fifty”,”Sixty”,”Seventy”,”Eighty”,”Ninety”},  
units, MOD(num, 10), tensPlace, MOD(INT(num / 10), 10), hundredsPlace,  
MOD(INT(num / 100), 10), thousandsPlace, MOD(INT(num / 1000), 1000),  
millionsPlace, INT(num / 1000000), words, IF(num < 10, INDEX(singleDigits,  
num + 1), IF(num < 20, INDEX(teens, num – 9), IF(num < 100, INDEX(tens,  
tensPlace + 1) & IF(units <> 0, “-” &  
INDEX(singleDigits, units + 1), “”), IF(num < 1000,  
INDEX(singleDigits, hundredsPlace + 1) & ” Hundred” &  
IF(MOD(num, 100) <> 0, ” ” & NUMBERTEXT(MOD(num, 100)),  
“”), IF(num < 1000000, NUMBERTEXT(INT(num / 1000)) & ”  
Thousand” & IF(MOD(num, 1000) <> 0, ” ” &  
NUMBERTEXT(MOD(num, 1000)), “”), IF(num < 10000000,  
NUMBERTEXT(millionsPlace) & ” Million” & IF(MOD(num, 1000000)  
<> 0, ” ” & NUMBERTEXT(MOD(num, 1000000)), “”),  
“Number out of range”)))))), words))**

Nice.

I have something much simpler and mine even remembers adding words such as “and”:

![](<Base64-Image-Removed>)

Assuming the formula is in cell **B2** (as above):

**\=SUBSTITUTE(TRANSLATE(BAHTTEXT(B2),”th”,”en”),”  
baht”,””)**

How cool is that?

**BAHTTEXT** is a truly random function in Excel that converts a number to Thai text and adds a suffix of “Baht”. You can change the Baht format to a different style in the Excel desktop application by using Regional and Language Options (Windows Start menu, Control Panel). It employs the following syntax to operate:

**BAHTTEXT(number)**

The **BAHTTEXT** function has the following argument only:

*   **number:** this is required and represents a number you want to convert to text, or a reference to a cell containing a number, or a formula that evaluates to a number.

![](<Base64-Image-Removed>)

So, I thought why not use the new **TRANSLATE** function to translate Thai to English (or any other language you wish)?

For those not familiar with this brand new function, suppose you have the following text in cell **A1**:

  “Hello, World!”  

and you want to translate it to Spanish. You can use the **TRANSLATE** function as follows:

**\=TRANSLATE(A1,  
“en”, “es”)**

In this example, the source language is English (en) and the target language is Spanish (es). The translated text, “Hola mundo!” will be displayed in the cell where you entered the formula.

Alternatively, you may just type the text in, _viz._

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

We can take this idea with **BAHTTEXT**:

![](<Base64-Image-Removed>)

Then, all you need to do is remove “baht” from the text at the end (I use the **SUBSTITUTE** function to do this).

![](<Base64-Image-Removed>)

Simple!

**_Word to the Wise_**

Before everyone starts cheering from the rooftops, there are some issues. Some numbers don’t seem to work (_e.g._ 10,014 and those with decimals) – but hey, it’s a start and greater minds will bulldoze these scenarios in time. Also, I should point out that **TRANSLATE** is not yet available in all versions of Excel. At the time of writing, this function is only available to Beta Channel users of Excel 365 running:

*   Windows: Version 2407 (Build 16.0.17808.20000) or later
*   Mac: 16.87 (Build 24062430) or later.

But it’s coming!!

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/news/best-excel-tip-ever/#0)
    
*   [Register](https://sumproduct.com/news/best-excel-tip-ever/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/news/best-excel-tip-ever/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/news/best-excel-tip-ever/#0)

[](https://sumproduct.com/news/best-excel-tip-ever/#0 "close")

top