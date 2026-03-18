# Convert Number to Words in Excel (2 Easy Ways)

**Source:** https://trumpexcel.com/number-to-words-excel

---

[Skip to content](https://trumpexcel.com/number-to-words-excel/#content "Skip to content")

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/number-to-words-excel/#below-title)

Excel doesn’t have a built-in function to convert numbers into words.

But there are a couple of reliable ways to do it, and I’ll walk you through both in this article.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/number-to-words-excel/#)

Method 1: Using VBA Macro to Create Custom Function (Recommended)
-----------------------------------------------------------------

This is the most widely used and reliable method.

To use this method, I will use a VBA code to create a custom function (say _NumbertoWords_), and then use this function in the worksheet to take the number as an input and give us the number in words.

It works in all Excel versions, and once it’s set up, using it is as simple as typing _\=NumbertoWords(A2)_

![Formula to convert number to words](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20862%20212'%3E%3C/svg%3E)

Here are the steps to set up the _NumbertoWords_ macro:

1.  Open your Excel workbook.
2.  Press **Alt + F11** to open the Visual Basic Editor.
3.  In the menu, click on the _Insert_ option and then click on _Module_. This will add a new module.
4.  Copy and paste the VBA code (provided below) into the Module code window.

![Code added to the VBA module](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201920%201080'%3E%3C/svg%3E)

5.  Close the VBA Editor.

Now I will give you different VBA codes for three scenarios:

*   Convert a number to words without any currency
*   Convert a number to words for the USD currency
*   Convert a number to words for the INR currency

_You can also customize these VBA codes for other currencies, such as Euros, Pounds, or Pesos._

### VBA code for Number to Words Only

Here is the VBA code to convert a number to words:

Option Explicit

' Main function: takes a number and returns it as words (no currency)
Function NumbertoWords(ByVal MyNumber)
    Dim WholeNumber As String, DecimalPart As String, Temp
    Dim DecimalPlace, Count
    ReDim Place(9) As String

    ' Scale labels for each 3-digit group
    Place(2) = " Thousand "
    Place(3) = " Million "
    Place(4) = " Billion "
    Place(5) = " Trillion "

    ' Convert number to a clean string for processing
    MyNumber = Trim(Str(MyNumber))

    ' Check if there's a decimal point
    DecimalPlace = InStr(MyNumber, ".")

    ' If decimal exists, split into whole and decimal portions
    If DecimalPlace > 0 Then
        DecimalPart = Mid(MyNumber, DecimalPlace + 1)
        MyNumber = Trim(Left(MyNumber, DecimalPlace - 1))
    End If

    ' Process the number in 3-digit chunks from right to left
    Count = 1
    Do While MyNumber <> ""
        Temp = GetHundreds(Right(MyNumber, 3))
        If Temp <> "" Then WholeNumber = Temp & Place(Count) & WholeNumber
        If Len(MyNumber) > 3 Then
            MyNumber = Left(MyNumber, Len(MyNumber) - 3)
        Else
            MyNumber = ""
        End If
        Count = Count + 1
    Loop

    ' Handle zero case
    If WholeNumber = "" Then WholeNumber = "Zero"

    ' If there's a decimal part, read each digit after "Point"
    If DecimalPart <> "" Then
        Dim i As Integer
        WholeNumber = WholeNumber & " Point"
        For i = 1 To Len(DecimalPart)
            WholeNumber = WholeNumber & " " & GetDigit(Mid(DecimalPart, i, 1))
        Next i
    End If

    NumbertoWords = WholeNumber
End Function

' Converts a 3-digit number (0-999) to words
Function GetHundreds(ByVal MyNumber)
    Dim Result As String
    If Val(MyNumber) = 0 Then Exit Function

    ' Pad to exactly 3 digits so positions are consistent
    MyNumber = Right("000" & MyNumber, 3)

    ' First digit = hundreds place
    If Mid(MyNumber, 1, 1) <> "0" Then
        Result = GetDigit(Mid(MyNumber, 1, 1)) & " Hundred "
    End If

    ' Second digit determines if we use teens (10-19) or tens + ones
    If Mid(MyNumber, 2, 1) <> "0" Then
        Result = Result & GetTens(Mid(MyNumber, 2))
    Else
        Result = Result & GetDigit(Mid(MyNumber, 3))
    End If

    GetHundreds = Result
End Function

' Converts a 2-digit number (10-99) to words
Function GetTens(TensText)
    Dim Result As String
    Result = ""

    ' Special case: teens (10-19) have unique names
    If Val(Left(TensText, 1)) = 1 Then
        Select Case Val(TensText)
            Case 10: Result = "Ten"
            Case 11: Result = "Eleven"
            Case 12: Result = "Twelve"
            Case 13: Result = "Thirteen"
            Case 14: Result = "Fourteen"
            Case 15: Result = "Fifteen"
            Case 16: Result = "Sixteen"
            Case 17: Result = "Seventeen"
            Case 18: Result = "Eighteen"
            Case 19: Result = "Nineteen"
        End Select
    Else
        ' For 20-99, combine the tens word with the ones word
        Select Case Val(Left(TensText, 1))
            Case 2: Result = "Twenty "
            Case 3: Result = "Thirty "
            Case 4: Result = "Forty "
            Case 5: Result = "Fifty "
            Case 6: Result = "Sixty "
            Case 7: Result = "Seventy "
            Case 8: Result = "Eighty "
            Case 9: Result = "Ninety "
        End Select
        Result = Result & GetDigit(Right(TensText, 1))
    End If

    GetTens = Result
End Function

' Converts a single digit (1-9) to its word. Returns empty for 0
Function GetDigit(Digit)
    Select Case Val(Digit)
        Case 1: GetDigit = "One"
        Case 2: GetDigit = "Two"
        Case 3: GetDigit = "Three"
        Case 4: GetDigit = "Four"
        Case 5: GetDigit = "Five"
        Case 6: GetDigit = "Six"
        Case 7: GetDigit = "Seven"
        Case 8: GetDigit = "Eight"
        Case 9: GetDigit = "Nine"
        Case Else: GetDigit = ""
    End Select
End Function

    Option Explicit
    
    ' Main function: takes a number and returns it as words (no currency)
    Function NumbertoWords(ByVal MyNumber)
        Dim WholeNumber As String, DecimalPart As String, Temp
        Dim DecimalPlace, Count
        ReDim Place(9) As String
    
        ' Scale labels for each 3-digit group
        Place(2) = " Thousand "
        Place(3) = " Million "
        Place(4) = " Billion "
        Place(5) = " Trillion "
    
        ' Convert number to a clean string for processing
        MyNumber = Trim(Str(MyNumber))
    
        ' Check if there's a decimal point
        DecimalPlace = InStr(MyNumber, ".")
    
        ' If decimal exists, split into whole and decimal portions
        If DecimalPlace > 0 Then
            DecimalPart = Mid(MyNumber, DecimalPlace + 1)
            MyNumber = Trim(Left(MyNumber, DecimalPlace - 1))
        End If
    
        ' Process the number in 3-digit chunks from right to left
        Count = 1
        Do While MyNumber <> ""
            Temp = GetHundreds(Right(MyNumber, 3))
            If Temp <> "" Then WholeNumber = Temp & Place(Count) & WholeNumber
            If Len(MyNumber) > 3 Then
                MyNumber = Left(MyNumber, Len(MyNumber) - 3)
            Else
                MyNumber = ""
            End If
            Count = Count + 1
        Loop
    
        ' Handle zero case
        If WholeNumber = "" Then WholeNumber = "Zero"
    
        ' If there's a decimal part, read each digit after "Point"
        If DecimalPart <> "" Then
            Dim i As Integer
            WholeNumber = WholeNumber & " Point"
            For i = 1 To Len(DecimalPart)
                WholeNumber = WholeNumber & " " & GetDigit(Mid(DecimalPart, i, 1))
            Next i
        End If
    
        NumbertoWords = WholeNumber
    End Function
    
    ' Converts a 3-digit number (0-999) to words
    Function GetHundreds(ByVal MyNumber)
        Dim Result As String
        If Val(MyNumber) = 0 Then Exit Function
    
        ' Pad to exactly 3 digits so positions are consistent
        MyNumber = Right("000" & MyNumber, 3)
    
        ' First digit = hundreds place
        If Mid(MyNumber, 1, 1) <> "0" Then
            Result = GetDigit(Mid(MyNumber, 1, 1)) & " Hundred "
        End If
    
        ' Second digit determines if we use teens (10-19) or tens + ones
        If Mid(MyNumber, 2, 1) <> "0" Then
            Result = Result & GetTens(Mid(MyNumber, 2))
        Else
            Result = Result & GetDigit(Mid(MyNumber, 3))
        End If
    
        GetHundreds = Result
    End Function
    
    ' Converts a 2-digit number (10-99) to words
    Function GetTens(TensText)
        Dim Result As String
        Result = ""
    
        ' Special case: teens (10-19) have unique names
        If Val(Left(TensText, 1)) = 1 Then
            Select Case Val(TensText)
                Case 10: Result = "Ten"
                Case 11: Result = "Eleven"
                Case 12: Result = "Twelve"
                Case 13: Result = "Thirteen"
                Case 14: Result = "Fourteen"
                Case 15: Result = "Fifteen"
                Case 16: Result = "Sixteen"
                Case 17: Result = "Seventeen"
                Case 18: Result = "Eighteen"
                Case 19: Result = "Nineteen"
            End Select
        Else
            ' For 20-99, combine the tens word with the ones word
            Select Case Val(Left(TensText, 1))
                Case 2: Result = "Twenty "
                Case 3: Result = "Thirty "
                Case 4: Result = "Forty "
                Case 5: Result = "Fifty "
                Case 6: Result = "Sixty "
                Case 7: Result = "Seventy "
                Case 8: Result = "Eighty "
                Case 9: Result = "Ninety "
            End Select
            Result = Result & GetDigit(Right(TensText, 1))
        End If
    
        GetTens = Result
    End Function
    
    ' Converts a single digit (1-9) to its word. Returns empty for 0
    Function GetDigit(Digit)
        Select Case Val(Digit)
            Case 1: GetDigit = "One"
            Case 2: GetDigit = "Two"
            Case 3: GetDigit = "Three"
            Case 4: GetDigit = "Four"
            Case 5: GetDigit = "Five"
            Case 6: GetDigit = "Six"
            Case 7: GetDigit = "Seven"
            Case 8: GetDigit = "Eight"
            Case 9: GetDigit = "Nine"
            Case Else: GetDigit = ""
        End Select
    End Function

Once you’ve set up the VBA code, you can use this newly created function (_NumbertoWords_) like any other regular worksheet function.

![Formula to convert number to words](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20862%20212'%3E%3C/svg%3E)

### VBA code for Numbers to Words for USD Currency

Option Explicit

' Main function: takes a number and returns it as words in currency format
Function NumbertoWordsUSD(ByVal MyNumber)
    Dim Dollars, Cents, Temp
    Dim DecimalPlace, Count
    ReDim Place(9) As String

    ' Scale labels for each 3-digit group
    Place(2) = " Thousand "
    Place(3) = " Million "
    Place(4) = " Billion "
    Place(5) = " Trillion "

    ' Convert number to a clean string for processing
    MyNumber = Trim(Str(MyNumber))

    ' Check if there's a decimal point
    DecimalPlace = InStr(MyNumber, ".")

    ' If decimal exists, split into whole and cents portions
    If DecimalPlace > 0 Then
        Cents = GetTensUSD(Left(Mid(MyNumber, DecimalPlace + 1) & "00", 2))
        MyNumber = Trim(Left(MyNumber, DecimalPlace - 1))
    End If

    ' Process the number in 3-digit chunks from right to left
    Count = 1
    Do While MyNumber <> ""
        Temp = GetHundredsUSD(Right(MyNumber, 3))
        If Temp <> "" Then Dollars = Temp & Place(Count) & Dollars
        If Len(MyNumber) > 3 Then
            MyNumber = Left(MyNumber, Len(MyNumber) - 3)
        Else
            MyNumber = ""
        End If
        Count = Count + 1
    Loop

    ' Handle singular/plural/zero for dollars
    Select Case Dollars
        Case "": Dollars = "No Dollars"
        Case "One": Dollars = "One Dollar"
        Case Else: Dollars = Dollars & " Dollars"
    End Select

    ' Handle singular/plural/zero for cents
    Select Case Cents
        Case "": Cents = " and No Cents"
        Case "One": Cents = " and One Cent"
        Case Else: Cents = " and " & Cents & " Cents"
    End Select

    NumbertoWordsUSD = Dollars & Cents
End Function

' Converts a 3-digit number (0-999) to words
Function GetHundredsUSD(ByVal MyNumber)
    Dim Result As String
    If Val(MyNumber) = 0 Then Exit Function

    ' Pad to exactly 3 digits so positions are consistent
    MyNumber = Right("000" & MyNumber, 3)

    ' First digit = hundreds place
    If Mid(MyNumber, 1, 1) <> "0" Then
        Result = GetDigitUSD(Mid(MyNumber, 1, 1)) & " Hundred "
    End If

    ' Second digit determines if we use teens (10-19) or tens + ones
    If Mid(MyNumber, 2, 1) <> "0" Then
        Result = Result & GetTensUSD(Mid(MyNumber, 2))
    Else
        Result = Result & GetDigitUSD(Mid(MyNumber, 3))
    End If

    GetHundredsUSD = Result
End Function

' Converts a 2-digit number (10-99) to words
Function GetTensUSD(TensText)
    Dim Result As String
    Result = ""

    ' Special case: teens (10-19) have unique names
    If Val(Left(TensText, 1)) = 1 Then
        Select Case Val(TensText)
            Case 10: Result = "Ten"
            Case 11: Result = "Eleven"
            Case 12: Result = "Twelve"
            Case 13: Result = "Thirteen"
            Case 14: Result = "Fourteen"
            Case 15: Result = "Fifteen"
            Case 16: Result = "Sixteen"
            Case 17: Result = "Seventeen"
            Case 18: Result = "Eighteen"
            Case 19: Result = "Nineteen"
        End Select
    Else
        ' For 20-99, combine the tens word with the ones word
        Select Case Val(Left(TensText, 1))
            Case 2: Result = "Twenty "
            Case 3: Result = "Thirty "
            Case 4: Result = "Forty "
            Case 5: Result = "Fifty "
            Case 6: Result = "Sixty "
            Case 7: Result = "Seventy "
            Case 8: Result = "Eighty "
            Case 9: Result = "Ninety "
        End Select
        Result = Result & GetDigitUSD(Right(TensText, 1))
    End If

    GetTensUSD = Result
End Function

' Converts a single digit (1-9) to its word. Returns empty for 0
Function GetDigitUSD(Digit)
    Select Case Val(Digit)
        Case 1: GetDigitUSD = "One"
        Case 2: GetDigitUSD = "Two"
        Case 3: GetDigitUSD = "Three"
        Case 4: GetDigitUSD = "Four"
        Case 5: GetDigitUSD = "Five"
        Case 6: GetDigitUSD = "Six"
        Case 7: GetDigitUSD = "Seven"
        Case 8: GetDigitUSD = "Eight"
        Case 9: GetDigitUSD = "Nine"
        Case Else: GetDigitUSD = ""
    End Select
End Function

    Option Explicit
    
    ' Main function: takes a number and returns it as words in currency format
    Function NumbertoWordsUSD(ByVal MyNumber)
        Dim Dollars, Cents, Temp
        Dim DecimalPlace, Count
        ReDim Place(9) As String
    
        ' Scale labels for each 3-digit group
        Place(2) = " Thousand "
        Place(3) = " Million "
        Place(4) = " Billion "
        Place(5) = " Trillion "
    
        ' Convert number to a clean string for processing
        MyNumber = Trim(Str(MyNumber))
    
        ' Check if there's a decimal point
        DecimalPlace = InStr(MyNumber, ".")
    
        ' If decimal exists, split into whole and cents portions
        If DecimalPlace > 0 Then
            Cents = GetTensUSD(Left(Mid(MyNumber, DecimalPlace + 1) & "00", 2))
            MyNumber = Trim(Left(MyNumber, DecimalPlace - 1))
        End If
    
        ' Process the number in 3-digit chunks from right to left
        Count = 1
        Do While MyNumber <> ""
            Temp = GetHundredsUSD(Right(MyNumber, 3))
            If Temp <> "" Then Dollars = Temp & Place(Count) & Dollars
            If Len(MyNumber) > 3 Then
                MyNumber = Left(MyNumber, Len(MyNumber) - 3)
            Else
                MyNumber = ""
            End If
            Count = Count + 1
        Loop
    
        ' Handle singular/plural/zero for dollars
        Select Case Dollars
            Case "": Dollars = "No Dollars"
            Case "One": Dollars = "One Dollar"
            Case Else: Dollars = Dollars & " Dollars"
        End Select
    
        ' Handle singular/plural/zero for cents
        Select Case Cents
            Case "": Cents = " and No Cents"
            Case "One": Cents = " and One Cent"
            Case Else: Cents = " and " & Cents & " Cents"
        End Select
    
        NumbertoWordsUSD = Dollars & Cents
    End Function
    
    ' Converts a 3-digit number (0-999) to words
    Function GetHundredsUSD(ByVal MyNumber)
        Dim Result As String
        If Val(MyNumber) = 0 Then Exit Function
    
        ' Pad to exactly 3 digits so positions are consistent
        MyNumber = Right("000" & MyNumber, 3)
    
        ' First digit = hundreds place
        If Mid(MyNumber, 1, 1) <> "0" Then
            Result = GetDigitUSD(Mid(MyNumber, 1, 1)) & " Hundred "
        End If
    
        ' Second digit determines if we use teens (10-19) or tens + ones
        If Mid(MyNumber, 2, 1) <> "0" Then
            Result = Result & GetTensUSD(Mid(MyNumber, 2))
        Else
            Result = Result & GetDigitUSD(Mid(MyNumber, 3))
        End If
    
        GetHundredsUSD = Result
    End Function
    
    ' Converts a 2-digit number (10-99) to words
    Function GetTensUSD(TensText)
        Dim Result As String
        Result = ""
    
        ' Special case: teens (10-19) have unique names
        If Val(Left(TensText, 1)) = 1 Then
            Select Case Val(TensText)
                Case 10: Result = "Ten"
                Case 11: Result = "Eleven"
                Case 12: Result = "Twelve"
                Case 13: Result = "Thirteen"
                Case 14: Result = "Fourteen"
                Case 15: Result = "Fifteen"
                Case 16: Result = "Sixteen"
                Case 17: Result = "Seventeen"
                Case 18: Result = "Eighteen"
                Case 19: Result = "Nineteen"
            End Select
        Else
            ' For 20-99, combine the tens word with the ones word
            Select Case Val(Left(TensText, 1))
                Case 2: Result = "Twenty "
                Case 3: Result = "Thirty "
                Case 4: Result = "Forty "
                Case 5: Result = "Fifty "
                Case 6: Result = "Sixty "
                Case 7: Result = "Seventy "
                Case 8: Result = "Eighty "
                Case 9: Result = "Ninety "
            End Select
            Result = Result & GetDigitUSD(Right(TensText, 1))
        End If
    
        GetTensUSD = Result
    End Function
    
    ' Converts a single digit (1-9) to its word. Returns empty for 0
    Function GetDigitUSD(Digit)
        Select Case Val(Digit)
            Case 1: GetDigitUSD = "One"
            Case 2: GetDigitUSD = "Two"
            Case 3: GetDigitUSD = "Three"
            Case 4: GetDigitUSD = "Four"
            Case 5: GetDigitUSD = "Five"
            Case 6: GetDigitUSD = "Six"
            Case 7: GetDigitUSD = "Seven"
            Case 8: GetDigitUSD = "Eight"
            Case 9: GetDigitUSD = "Nine"
            Case Else: GetDigitUSD = ""
        End Select
    End Function

Once you’ve set up the VBA code, you can use this newly created function (_NumbertoWordsUSD_) like any other regular worksheet function.

![Convert Number to Words USD](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20876%20240'%3E%3C/svg%3E)

**Pro Tip:** If you just need to change the currency label (e.g., to Euros and Cents or Pounds and Pence), you don’t need separate code. Just find and replace “Dollars” with “Euros” and “Dollar” with “Euro” in above code.

### VBA code for Number to Words for the Indian System

If you want to convert numbers to words for an Indian system (or other similar systems), you can use the VBA code below.

Option Explicit

Function NumberToWordsINR(ByVal MyNumber)
    Dim Rupees As String, Paise As String
    Dim DecimalPlace As Integer

    MyNumber = Trim(Str(MyNumber))
    DecimalPlace = InStr(MyNumber, ".")

    ' Handle Paise (decimal part)
    If DecimalPlace > 0 Then
        Dim PaiseStr As String
        PaiseStr = Left(Mid(MyNumber, DecimalPlace + 1) & "00", 2)
        If Val(PaiseStr) > 0 Then
            Paise = GetTensINR(PaiseStr)
        End If
        MyNumber = Trim(Left(MyNumber, DecimalPlace - 1))
    End If

    Dim NumVal As Double
    NumVal = Val(MyNumber)

    If NumVal = 0 Then
        Rupees = "Zero"
    Else
        Dim Cr As Long, Lk As Long, Th As Long, Hd As Long
        Dim Remainder As Double

        Cr = Int(NumVal / 10000000)
        Remainder = NumVal - (CDbl(Cr) \* 10000000)
        Lk = Int(Remainder / 100000)
        Remainder = Remainder - (CDbl(Lk) \* 100000)
        Th = Int(Remainder / 1000)
        Hd = Int(Remainder - (CDbl(Th) \* 1000))

        Rupees = ""

        ' Crores (split further for large values)
        If Cr > 0 Then
            Dim CrTh As Long, CrRem As Long
            Dim CrText As String
            CrTh = Int(Cr / 1000)
            CrRem = Cr Mod 1000
            CrText = ""
            If CrTh > 0 Then CrText = GetHundredsINR(CStr(CrTh)) & " Thousand "
            If CrRem > 0 Then CrText = CrText & GetHundredsINR(CStr(CrRem))
            Rupees = Trim(CrText) & " Crore "
        End If

        ' Lakhs
        If Lk > 0 Then
            Rupees = Rupees & GetTensINR(Right("00" & CStr(Lk), 2)) & " Lakh "
        End If

        ' Thousands
        If Th > 0 Then
            Rupees = Rupees & GetTensINR(Right("00" & CStr(Th), 2)) & " Thousand "
        End If

        ' Hundreds and below
        If Hd > 0 Then
            Rupees = Rupees & GetHundredsINR(CStr(Hd))
        End If

        Rupees = Trim(Rupees)
    End If

    ' Add Rupees label
    Select Case Rupees
        Case "Zero": Rupees = "Zero Rupees"
        Case "One": Rupees = "One Rupee"
        Case Else: Rupees = Rupees & " Rupees"
    End Select

    ' Add Paise label
    If Paise <> "" Then
        Select Case Paise
            Case "One": Paise = " and One Paisa"
            Case Else: Paise = " and " & Paise & " Paise"
        End Select
    Else
        Paise = ""
    End If

    NumberToWordsINR = Rupees & Paise
End Function

Function GetHundredsINR(ByVal MyNumber)
    Dim Result As String
    If Val(MyNumber) = 0 Then Exit Function
    MyNumber = Right("000" & MyNumber, 3)
    If Mid(MyNumber, 1, 1) <> "0" Then
        Result = GetDigitINR(Mid(MyNumber, 1, 1)) & " Hundred "
    End If
    If Mid(MyNumber, 2, 1) <> "0" Then
        Result = Result & GetTensINR(Mid(MyNumber, 2))
    Else
        Result = Result & GetDigitINR(Mid(MyNumber, 3))
    End If
    GetHundredsINR = Trim(Result)
End Function

Function GetTensINR(TensText)
    Dim Result As String
    Result = ""
    If Val(Left(TensText, 1)) = 1 Then
        Select Case Val(TensText)
            Case 10: Result = "Ten"
            Case 11: Result = "Eleven"
            Case 12: Result = "Twelve"
            Case 13: Result = "Thirteen"
            Case 14: Result = "Fourteen"
            Case 15: Result = "Fifteen"
            Case 16: Result = "Sixteen"
            Case 17: Result = "Seventeen"
            Case 18: Result = "Eighteen"
            Case 19: Result = "Nineteen"
        End Select
    Else
        Select Case Val(Left(TensText, 1))
            Case 2: Result = "Twenty "
            Case 3: Result = "Thirty "
            Case 4: Result = "Forty "
            Case 5: Result = "Fifty "
            Case 6: Result = "Sixty "
            Case 7: Result = "Seventy "
            Case 8: Result = "Eighty "
            Case 9: Result = "Ninety "
        End Select
        Result = Result & GetDigitINR(Right(TensText, 1))
    End If
    GetTensINR = Trim(Result)
End Function

Function GetDigitINR(Digit)
    Select Case Val(Digit)
        Case 1: GetDigitINR = "One"
        Case 2: GetDigitINR = "Two"
        Case 3: GetDigitINR = "Three"
        Case 4: GetDigitINR = "Four"
        Case 5: GetDigitINR = "Five"
        Case 6: GetDigitINR = "Six"
        Case 7: GetDigitINR = "Seven"
        Case 8: GetDigitINR = "Eight"
        Case 9: GetDigitINR = "Nine"
        Case Else: GetDigitINR = ""
    End Select
End Function

    Option Explicit
    
    Function NumberToWordsINR(ByVal MyNumber)
        Dim Rupees As String, Paise As String
        Dim DecimalPlace As Integer
    
        MyNumber = Trim(Str(MyNumber))
        DecimalPlace = InStr(MyNumber, ".")
    
        ' Handle Paise (decimal part)
        If DecimalPlace > 0 Then
            Dim PaiseStr As String
            PaiseStr = Left(Mid(MyNumber, DecimalPlace + 1) & "00", 2)
            If Val(PaiseStr) > 0 Then
                Paise = GetTensINR(PaiseStr)
            End If
            MyNumber = Trim(Left(MyNumber, DecimalPlace - 1))
        End If
    
        Dim NumVal As Double
        NumVal = Val(MyNumber)
    
        If NumVal = 0 Then
            Rupees = "Zero"
        Else
            Dim Cr As Long, Lk As Long, Th As Long, Hd As Long
            Dim Remainder As Double
    
            Cr = Int(NumVal / 10000000)
            Remainder = NumVal - (CDbl(Cr) * 10000000)
            Lk = Int(Remainder / 100000)
            Remainder = Remainder - (CDbl(Lk) * 100000)
            Th = Int(Remainder / 1000)
            Hd = Int(Remainder - (CDbl(Th) * 1000))
    
            Rupees = ""
    
            ' Crores (split further for large values)
            If Cr > 0 Then
                Dim CrTh As Long, CrRem As Long
                Dim CrText As String
                CrTh = Int(Cr / 1000)
                CrRem = Cr Mod 1000
                CrText = ""
                If CrTh > 0 Then CrText = GetHundredsINR(CStr(CrTh)) & " Thousand "
                If CrRem > 0 Then CrText = CrText & GetHundredsINR(CStr(CrRem))
                Rupees = Trim(CrText) & " Crore "
            End If
    
            ' Lakhs
            If Lk > 0 Then
                Rupees = Rupees & GetTensINR(Right("00" & CStr(Lk), 2)) & " Lakh "
            End If
    
            ' Thousands
            If Th > 0 Then
                Rupees = Rupees & GetTensINR(Right("00" & CStr(Th), 2)) & " Thousand "
            End If
    
            ' Hundreds and below
            If Hd > 0 Then
                Rupees = Rupees & GetHundredsINR(CStr(Hd))
            End If
    
            Rupees = Trim(Rupees)
        End If
    
        ' Add Rupees label
        Select Case Rupees
            Case "Zero": Rupees = "Zero Rupees"
            Case "One": Rupees = "One Rupee"
            Case Else: Rupees = Rupees & " Rupees"
        End Select
    
        ' Add Paise label
        If Paise <> "" Then
            Select Case Paise
                Case "One": Paise = " and One Paisa"
                Case Else: Paise = " and " & Paise & " Paise"
            End Select
        Else
            Paise = ""
        End If
    
        NumberToWordsINR = Rupees & Paise
    End Function
    
    Function GetHundredsINR(ByVal MyNumber)
        Dim Result As String
        If Val(MyNumber) = 0 Then Exit Function
        MyNumber = Right("000" & MyNumber, 3)
        If Mid(MyNumber, 1, 1) <> "0" Then
            Result = GetDigitINR(Mid(MyNumber, 1, 1)) & " Hundred "
        End If
        If Mid(MyNumber, 2, 1) <> "0" Then
            Result = Result & GetTensINR(Mid(MyNumber, 2))
        Else
            Result = Result & GetDigitINR(Mid(MyNumber, 3))
        End If
        GetHundredsINR = Trim(Result)
    End Function
    
    Function GetTensINR(TensText)
        Dim Result As String
        Result = ""
        If Val(Left(TensText, 1)) = 1 Then
            Select Case Val(TensText)
                Case 10: Result = "Ten"
                Case 11: Result = "Eleven"
                Case 12: Result = "Twelve"
                Case 13: Result = "Thirteen"
                Case 14: Result = "Fourteen"
                Case 15: Result = "Fifteen"
                Case 16: Result = "Sixteen"
                Case 17: Result = "Seventeen"
                Case 18: Result = "Eighteen"
                Case 19: Result = "Nineteen"
            End Select
        Else
            Select Case Val(Left(TensText, 1))
                Case 2: Result = "Twenty "
                Case 3: Result = "Thirty "
                Case 4: Result = "Forty "
                Case 5: Result = "Fifty "
                Case 6: Result = "Sixty "
                Case 7: Result = "Seventy "
                Case 8: Result = "Eighty "
                Case 9: Result = "Ninety "
            End Select
            Result = Result & GetDigitINR(Right(TensText, 1))
        End If
        GetTensINR = Trim(Result)
    End Function
    
    Function GetDigitINR(Digit)
        Select Case Val(Digit)
            Case 1: GetDigitINR = "One"
            Case 2: GetDigitINR = "Two"
            Case 3: GetDigitINR = "Three"
            Case 4: GetDigitINR = "Four"
            Case 5: GetDigitINR = "Five"
            Case 6: GetDigitINR = "Six"
            Case 7: GetDigitINR = "Seven"
            Case 8: GetDigitINR = "Eight"
            Case 9: GetDigitINR = "Nine"
            Case Else: GetDigitINR = ""
        End Select
    End Function

The above code uses words such as lakhs and crores instead of millions and billions.

Once you’ve set up the VBA code, you can use this newly created function (_NumbertoWordsINR_) like any other regular worksheet function.

![Convert Number to words INR VBA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20821%20242'%3E%3C/svg%3E)

**Important:** If you want to reuse this function later, you need to save the Excel file as a macro-enabled file with the .xlsm extension. Doing this will preserve the macro, and you can use this function the next time you open the file. If you save the file as a regular .xlsx file, the macro code would be lost.

Method 2: Using a Formula
-------------------------

If, for any reason, you cannot use the VBA code method, there is a formula way to do this (but it’s long and complicated).

Note: Since these formulas use the newly released [LET](https://trumpexcel.com/excel-functions/let-function/)
 and [LAMBDA functions](https://trumpexcel.com/excel-functions/lambda/)
, these would only work in Excel 2024, Excel with Microsoft 365, and Excel on the web.

### Formula for Number to Words Only (No Currency)

Here is the formula that will convert the number to words irrespective of the currency.

\=LET(
 val, A2,
 n, ABS(val), d, INT(n), c, ROUND((n-d)\*100,0),
 \_s, LAMBDA(n, LET(
 h,INT(n/100), r,MOD(n,100), t,INT(r/10), o,MOD(r,10),
 hT, IF(h>0,CHOOSE(h,"One","Two","Three","Four","Five",
 "Six","Seven","Eight","Nine")&" Hundred",""),
 rT, IF(r=0,"",IF(r<20,
 CHOOSE(r,"One","Two","Three","Four","Five","Six",
 "Seven","Eight","Nine","Ten","Eleven","Twelve",
 "Thirteen","Fourteen","Fifteen","Sixteen",
 "Seventeen","Eighteen","Nineteen"),
 CHOOSE(t-1,"Twenty","Thirty","Forty","Fifty",
 "Sixty","Seventy","Eighty","Ninety")
 &IF(o>0," "&CHOOSE(o,"One","Two","Three","Four",
 "Five","Six","Seven","Eight","Nine"),""))),
 TRIM(hT&" "&rT))),
 tri,INT(d/10^12), bil,INT(MOD(d,10^12)/10^9),
 mil,INT(MOD(d,10^9)/10^6), thou,INT(MOD(d,10^6)/1000),
 ones,INT(MOD(d,1000)),
 txt, TRIM(
 IF(tri>0, \_s(tri)&" Trillion ","") &
 IF(bil>0, \_s(bil)&" Billion ","") &
 IF(mil>0, \_s(mil)&" Million ","") &
 IF(thou>0, \_s(thou)&" Thousand ","") &
 IF(ones>0, \_s(ones),"")),
 IF(val=0,"Zero",
 IF(val<0,"Negative ","") &
 IF(d=0,"Zero",txt) &
 IF(c>0," Point " & IF(c<10,"Zero ","") & \_s(c),""))
)

    =LET(
     val, A2,
     n, ABS(val), d, INT(n), c, ROUND((n-d)*100,0),
     _s, LAMBDA(n, LET(
     h,INT(n/100), r,MOD(n,100), t,INT(r/10), o,MOD(r,10),
     hT, IF(h>0,CHOOSE(h,"One","Two","Three","Four","Five",
     "Six","Seven","Eight","Nine")&" Hundred",""),
     rT, IF(r=0,"",IF(r<20,
     CHOOSE(r,"One","Two","Three","Four","Five","Six",
     "Seven","Eight","Nine","Ten","Eleven","Twelve",
     "Thirteen","Fourteen","Fifteen","Sixteen",
     "Seventeen","Eighteen","Nineteen"),
     CHOOSE(t-1,"Twenty","Thirty","Forty","Fifty",
     "Sixty","Seventy","Eighty","Ninety")
     &IF(o>0," "&CHOOSE(o,"One","Two","Three","Four",
     "Five","Six","Seven","Eight","Nine"),""))),
     TRIM(hT&" "&rT))),
     tri,INT(d/10^12), bil,INT(MOD(d,10^12)/10^9),
     mil,INT(MOD(d,10^9)/10^6), thou,INT(MOD(d,10^6)/1000),
     ones,INT(MOD(d,1000)),
     txt, TRIM(
     IF(tri>0, _s(tri)&" Trillion ","") &
     IF(bil>0, _s(bil)&" Billion ","") &
     IF(mil>0, _s(mil)&" Million ","") &
     IF(thou>0, _s(thou)&" Thousand ","") &
     IF(ones>0, _s(ones),"")),
     IF(val=0,"Zero",
     IF(val<0,"Negative ","") &
     IF(d=0,"Zero",txt) &
     IF(c>0," Point " & IF(c<10,"Zero ","") & _s(c),""))
    )

![LET Formula to convert number to words](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201095%20303'%3E%3C/svg%3E)

### Formula for Number to Words for Dollar Currency

Below is the formula that will convert numbers to words for a dollar amount, so it would automatically put the terms such as dollars and cents in the result.

\=LET(
  val, A2,
  n, ABS(val), d, INT(n), c, ROUND((n-d)\*100,0),
  \_s, LAMBDA(n, LET(
    h,INT(n/100), r,MOD(n,100), t,INT(r/10), o,MOD(r,10),
    hT, IF(h>0,CHOOSE(h,"One","Two","Three","Four","Five",
      "Six","Seven","Eight","Nine")&" Hundred",""),
    rT, IF(r=0,"",IF(r<20,
      CHOOSE(r,"One","Two","Three","Four","Five","Six",
        "Seven","Eight","Nine","Ten","Eleven","Twelve",
        "Thirteen","Fourteen","Fifteen","Sixteen",
        "Seventeen","Eighteen","Nineteen"),
      CHOOSE(t-1,"Twenty","Thirty","Forty","Fifty",
        "Sixty","Seventy","Eighty","Ninety")
      &IF(o>0," "&CHOOSE(o,"One","Two","Three","Four",
        "Five","Six","Seven","Eight","Nine"),""))),
    TRIM(hT&" "&rT))),
  tri,INT(d/10^12), bil,INT(MOD(d,10^12)/10^9),
  mil,INT(MOD(d,10^9)/10^6), thou,INT(MOD(d,10^6)/1000),
  ones,INT(MOD(d,1000)),
  txt, TRIM(
    IF(tri>0, \_s(tri)&" Trillion ","") &
    IF(bil>0, \_s(bil)&" Billion ","") &
    IF(mil>0, \_s(mil)&" Million ","") &
    IF(thou>0, \_s(thou)&" Thousand ","") &
    IF(ones>0, \_s(ones),"")),
  IF(val=0,"Zero Dollars Only",
    IF(val<0,"Negative ","") &
    IF(d=0,"Zero",txt) &
    IF(d=1," Dollar"," Dollars") &
    IF(c>0," and " & \_s(c) & IF(c=1," Cent"," Cents"),
      " Only"))
)

    =LET(
      val, A2,
      n, ABS(val), d, INT(n), c, ROUND((n-d)*100,0),
      _s, LAMBDA(n, LET(
        h,INT(n/100), r,MOD(n,100), t,INT(r/10), o,MOD(r,10),
        hT, IF(h>0,CHOOSE(h,"One","Two","Three","Four","Five",
          "Six","Seven","Eight","Nine")&" Hundred",""),
        rT, IF(r=0,"",IF(r<20,
          CHOOSE(r,"One","Two","Three","Four","Five","Six",
            "Seven","Eight","Nine","Ten","Eleven","Twelve",
            "Thirteen","Fourteen","Fifteen","Sixteen",
            "Seventeen","Eighteen","Nineteen"),
          CHOOSE(t-1,"Twenty","Thirty","Forty","Fifty",
            "Sixty","Seventy","Eighty","Ninety")
          &IF(o>0," "&CHOOSE(o,"One","Two","Three","Four",
            "Five","Six","Seven","Eight","Nine"),""))),
        TRIM(hT&" "&rT))),
      tri,INT(d/10^12), bil,INT(MOD(d,10^12)/10^9),
      mil,INT(MOD(d,10^9)/10^6), thou,INT(MOD(d,10^6)/1000),
      ones,INT(MOD(d,1000)),
      txt, TRIM(
        IF(tri>0, _s(tri)&" Trillion ","") &
        IF(bil>0, _s(bil)&" Billion ","") &
        IF(mil>0, _s(mil)&" Million ","") &
        IF(thou>0, _s(thou)&" Thousand ","") &
        IF(ones>0, _s(ones),"")),
      IF(val=0,"Zero Dollars Only",
        IF(val<0,"Negative ","") &
        IF(d=0,"Zero",txt) &
        IF(d=1," Dollar"," Dollars") &
        IF(c>0," and " & _s(c) & IF(c=1," Cent"," Cents"),
          " Only"))
    )

![Formula to convert number to words USD](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201100%20332'%3E%3C/svg%3E)

### Formula for Number to Words for Rupee Currency

\=LET(
  val, A2,
  n, ABS(val), d, INT(n), c, ROUND((n-d)\*100,0),
  \_s, LAMBDA(n, LET(
    h,INT(n/100), r,MOD(n,100), t,INT(r/10), o,MOD(r,10),
    hT, IF(h>0,CHOOSE(h,"One","Two","Three","Four","Five",
      "Six","Seven","Eight","Nine")&" Hundred",""),
    rT, IF(r=0,"",IF(r<20,
      CHOOSE(r,"One","Two","Three","Four","Five","Six",
        "Seven","Eight","Nine","Ten","Eleven","Twelve",
        "Thirteen","Fourteen","Fifteen","Sixteen",
        "Seventeen","Eighteen","Nineteen"),
      CHOOSE(t-1,"Twenty","Thirty","Forty","Fifty",
        "Sixty","Seventy","Eighty","Ninety")
      &IF(o>0," "&CHOOSE(o,"One","Two","Three","Four",
        "Five","Six","Seven","Eight","Nine"),""))),
    TRIM(hT&" "&rT))),
  cro\_total,INT(d/10^7),
  cro\_th,INT(cro\_total/1000),
  cro\_rem,MOD(cro\_total,1000),
  lak,INT(MOD(d,10^7)/10^5),
  thou,INT(MOD(d,10^5)/1000),
  ones,INT(MOD(d,1000)),
  txt, TRIM(
    IF(cro\_total>0, TRIM(IF(cro\_th>0, \_s(cro\_th)&" Thousand ","") &
      IF(cro\_rem>0, \_s(cro\_rem),"")) & " Crore ","") &
    IF(lak>0, \_s(lak)&" Lakh ","") &
    IF(thou>0, \_s(thou)&" Thousand ","") &
    IF(ones>0, \_s(ones),"")),
  IF(val=0,"Zero Rupees Only",
    IF(val<0,"Negative ","") &
    IF(d=0,"Zero",txt) &
    IF(d=1," Rupee"," Rupees") &
    IF(c>0," and " & \_s(c) & IF(c=1," Paisa"," Paise"),
      " Only"))
)

    =LET(
      val, A2,
      n, ABS(val), d, INT(n), c, ROUND((n-d)*100,0),
      _s, LAMBDA(n, LET(
        h,INT(n/100), r,MOD(n,100), t,INT(r/10), o,MOD(r,10),
        hT, IF(h>0,CHOOSE(h,"One","Two","Three","Four","Five",
          "Six","Seven","Eight","Nine")&" Hundred",""),
        rT, IF(r=0,"",IF(r<20,
          CHOOSE(r,"One","Two","Three","Four","Five","Six",
            "Seven","Eight","Nine","Ten","Eleven","Twelve",
            "Thirteen","Fourteen","Fifteen","Sixteen",
            "Seventeen","Eighteen","Nineteen"),
          CHOOSE(t-1,"Twenty","Thirty","Forty","Fifty",
            "Sixty","Seventy","Eighty","Ninety")
          &IF(o>0," "&CHOOSE(o,"One","Two","Three","Four",
            "Five","Six","Seven","Eight","Nine"),""))),
        TRIM(hT&" "&rT))),
      cro_total,INT(d/10^7),
      cro_th,INT(cro_total/1000),
      cro_rem,MOD(cro_total,1000),
      lak,INT(MOD(d,10^7)/10^5),
      thou,INT(MOD(d,10^5)/1000),
      ones,INT(MOD(d,1000)),
      txt, TRIM(
        IF(cro_total>0, TRIM(IF(cro_th>0, _s(cro_th)&" Thousand ","") &
          IF(cro_rem>0, _s(cro_rem),"")) & " Crore ","") &
        IF(lak>0, _s(lak)&" Lakh ","") &
        IF(thou>0, _s(thou)&" Thousand ","") &
        IF(ones>0, _s(ones),"")),
      IF(val=0,"Zero Rupees Only",
        IF(val<0,"Negative ","") &
        IF(d=0,"Zero",txt) &
        IF(d=1," Rupee"," Rupees") &
        IF(c>0," and " & _s(c) & IF(c=1," Paisa"," Paise"),
          " Only"))
    )

![Formula to convert number to words INR](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201110%20339'%3E%3C/svg%3E)

These are really long formulas, so if you want to use them regularly, it would be a good idea to convert them into a LAMBDA and give a name to that function. That way, instead of using this long formula, you can use something like _NumbertoWords_ or _NumbertoWordsDollar_. Later in the article, I have covered how to convert these formulas into a LAMBDA.

**What these formulas can handle:**

*   Single cell reference change: Currently, the formula references cell A2, but if you want to change that, you can change it in the beginning (where it says _val, A2,_). If you want to run this formula on a range, you can do that as well. For example, if you want to run it on A2 to A10, you can change it to _val,A2:A10,_
*   Numbers up to Trillions (for non-currency and USD versions) or up to 999 Thousand Crore (for INR version).
*   Decimals up to 2 places, rendered as “Point” + words in the plain formula, or as Paise/Cents in the currency formulas
*   It can handle negative numbers. Negative numbers are prefixed with “Negative” automatically
*   Zero returns “Zero” in plain mode, or “Zero Rupees Only” / “Zero Dollars Only” in currency mode
*   Singular and plural currency is handled correctly: “One Dollar” vs “Two Dollars”, “One Rupee” vs “Two Rupees”, “One Cent” vs “Two Cents”, and “One Paisa” vs “Two Paise”
*   Teen numbers (11–19) are correctly output as “Eleven”, “Twelve”, etc. instead of “Ten One”, “Ten Two”
*   Single-digit decimals like 0.05 correctly show “Zero Five” (plain) or “Five Cents/Paise” (currency), not just “Five”

**Limitations of these formulas**:

*   More than 2 decimal places are ignored: a value like 45.6789 is treated as 45.68 (rounded to 2 decimal places). This is fine for currency but may not suit scientific or accounting scenarios requiring more precision
*   No error handling for non-numeric input: if the cell contains text, a blank, or an error like #N/A, the formula will return an error. You’d need to wrap it in an IFERROR or IF(ISNUMBER()) check
*   Excel’s 15-digit precision limit: Excel only stores 15 significant digits. Numbers beyond that (e.g., 1,234,567,890,123,456) will have their last digits rounded by Excel itself before the formula even sees them, so the words may not match the original number
*   No “and” before the final group: these formulas produce “One Hundred Twenty Three” (American style), not “One Hundred and Twenty Three” (British/Indian style).
*   Currency is hardcoded: each formula is built for one specific currency. If you need Euros, Pounds, or another currency, you’ll need to manually change the currency words in the formula

### Converting these formulas into a Lambda Named Function

The formulas covered above work great, but they’re long and hard to maintain.

By converting them into named LAMBDAs, you can turn the entire formula into a simple call like _\=NumbertoWords(A2)_.

Let me show you how to convert these formulas into a named lambda.

For this example, I am going to use the formula that converts a number or amount to words (no currency)

**Step 1:** Go to the _Formulas_ tab in the ribbon

**Step 2:** Click on Defined Names and then click on _Name Manager_ (or press _Ctrl + F3_ as a [shortcut](https://trumpexcel.com/excel-keyboard-shortcuts/)
)

![Click on Name Manager](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20901%20415'%3E%3C/svg%3E)

**Step 3:** In the _Name Manager_ dialog box, click the _New_ button. This will open the _New Name_ dialog box.

**Step 4:** In the _Name_ field, type your function name: _N2W_

![Enter the Lambda name in the name manager](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20454%20347'%3E%3C/svg%3E)

**Step 5:** Leave the _Scope_ set to _Workbook_ (this makes it available across all sheets)

**Step 6**: Copy and paste the formula below into the _Refers to_ field:

\=LAMBDA(val, LET(
  n, ABS(val), d, INT(n), c, ROUND((n-d)\*100,0),
  \_s, LAMBDA(n, LET(
    h,INT(n/100), r,MOD(n,100), t,INT(r/10), o,MOD(r,10),
    hT, IF(h>0,CHOOSE(h,"One","Two","Three","Four","Five",
      "Six","Seven","Eight","Nine")&" Hundred",""),
    rT, IF(r=0,"",IF(r<20,
      CHOOSE(r,"One","Two","Three","Four","Five","Six",
        "Seven","Eight","Nine","Ten","Eleven","Twelve",
        "Thirteen","Fourteen","Fifteen","Sixteen",
        "Seventeen","Eighteen","Nineteen"),
      CHOOSE(t-1,"Twenty","Thirty","Forty","Fifty",
        "Sixty","Seventy","Eighty","Ninety")
      &IF(o>0," "&CHOOSE(o,"One","Two","Three","Four",
        "Five","Six","Seven","Eight","Nine"),""))),
    TRIM(hT&" "&rT))),
  tri,INT(d/10^12), bil,INT(MOD(d,10^12)/10^9),
  mil,INT(MOD(d,10^9)/10^6), thou,INT(MOD(d,10^6)/1000),
  ones,INT(MOD(d,1000)),
  txt, TRIM(
    IF(tri>0, \_s(tri)&" Trillion ","") &
    IF(bil>0, \_s(bil)&" Billion ","") &
    IF(mil>0, \_s(mil)&" Million ","") &
    IF(thou>0, \_s(thou)&" Thousand ","") &
    IF(ones>0, \_s(ones),"")),
  IF(val=0,"Zero",
    IF(val<0,"Negative ","") &
    IF(d=0,"Zero",txt) &
    IF(c>0," Point " & IF(c<10,"Zero ","") & \_s(c),""))
))

    =LAMBDA(val, LET(
      n, ABS(val), d, INT(n), c, ROUND((n-d)*100,0),
      _s, LAMBDA(n, LET(
        h,INT(n/100), r,MOD(n,100), t,INT(r/10), o,MOD(r,10),
        hT, IF(h>0,CHOOSE(h,"One","Two","Three","Four","Five",
          "Six","Seven","Eight","Nine")&" Hundred",""),
        rT, IF(r=0,"",IF(r<20,
          CHOOSE(r,"One","Two","Three","Four","Five","Six",
            "Seven","Eight","Nine","Ten","Eleven","Twelve",
            "Thirteen","Fourteen","Fifteen","Sixteen",
            "Seventeen","Eighteen","Nineteen"),
          CHOOSE(t-1,"Twenty","Thirty","Forty","Fifty",
            "Sixty","Seventy","Eighty","Ninety")
          &IF(o>0," "&CHOOSE(o,"One","Two","Three","Four",
            "Five","Six","Seven","Eight","Nine"),""))),
        TRIM(hT&" "&rT))),
      tri,INT(d/10^12), bil,INT(MOD(d,10^12)/10^9),
      mil,INT(MOD(d,10^9)/10^6), thou,INT(MOD(d,10^6)/1000),
      ones,INT(MOD(d,1000)),
      txt, TRIM(
        IF(tri>0, _s(tri)&" Trillion ","") &
        IF(bil>0, _s(bil)&" Billion ","") &
        IF(mil>0, _s(mil)&" Million ","") &
        IF(thou>0, _s(thou)&" Thousand ","") &
        IF(ones>0, _s(ones),"")),
      IF(val=0,"Zero",
        IF(val<0,"Negative ","") &
        IF(d=0,"Zero",txt) &
        IF(c>0," Point " & IF(c<10,"Zero ","") & _s(c),""))
    ))

Note: To convert our regular formula into a lambda, I have added _\=LAMBDA(val,_ in the beginning, then removed _val, A2,_ from the formula and added a closing _)_

![Enter the formula in refers to field](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20454%20347'%3E%3C/svg%3E)

**Step 7**: Click _OK_ to save

**Step 8**: Close the Name Manager

Now you can use the formula below just like any other worksheet function:

\=N2W(A2)

    =N2W(A2)

![Using the named lambda function to convert number to text](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20880%20249'%3E%3C/svg%3E)

By converting it into a named lambda, you can see that the full formula is now a single, readable function that works across every sheet in the workbook.

You can follow the same steps to convert any of the above formulas into a named LAMBDA.

Name manager has a limitation of 2000 characters, so you need to ensure that the formulas you use to create the LAMBDA are less than 2000 characters.

VBA Macro vs Formula — Which Method Should You Use?
---------------------------------------------------

Both methods convert numbers to words, but they differ in setup, compatibility, and flexibility. Here’s how they compare.

Side-by-Side Comparison Help Me Decide

VBA Macro

~90

lines of code, one-time setup

Formula (LET + LAMBDA)

~30

lines in a single formula

Recommendation: VBA Macro for most users

The VBA method is easier to set up, works in all Excel versions, and is endorsed by Microsoft. Use the formula method only if macros are restricted in your environment or you need to stay on the web version of Excel.

So these are two methods you can use to convert a number to words in Excel.

Using a VBA method is recommended as it is more maintainable and easier to use, but if, for some reason, you cannot use a VBA code, you can try the formula methods.

If you do not want to get into the hassle of setting up a spreadsheet, you can also use this [free online number-to-words converter](https://trumpexcel.com/tools/number-to-words-converter/)
.

I hope you found this article helpful.

**Other Excel articles you may also like:**

*   [Convert Numbers to Text in Excel](https://trumpexcel.com/convert-numbers-to-text-excel/)
    
*   [Convert Text to Numbers in Excel](https://trumpexcel.com/convert-text-to-numbers-excel/)
    
*   [Extract Numbers from a String in Excel (Using Formulas or VBA)](https://trumpexcel.com/extract-numbers-from-string-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/number-to-words-excel/#respond)

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