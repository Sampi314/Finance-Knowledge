# Is there a secret code in this data? [Excel Homework] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/secret-code-problem

---

Is there a secret code in this data? \[Excel Homework\]
=======================================================

[Excel Challenges](https://chandoo.org/wp/category/excel-challenges/)
 - 33 comments

  

Are you ready for a fun Excel challenge? Read on then…

![](https://chandoo.org/wp/wp-content/uploads/2020/03/secret-code-challenge.jpg)

You are a nautical transport manifest analyst at New Donk city harbor. But **you also have a secret identity**. You are a spy for Global Intelligence Organization. As part of routine inspection of cargo details, you came across a list of shipping codes that look suspicious.

![](https://chandoo.org/wp/wp-content/uploads/2020/03/secret-code-challenge-data.png)

Your mission – Find the secret codes
------------------------------------

Step 1: [Download the sample data](https://chandoo.org/wp/wp-content/uploads/2020/03/shipping-secret-codes.xlsx)
.

Step 2: **The secret code is 007**. If you find it anywhere in the shipping number, then it is a Yes.

**For example:** the shipment number 123**0**45**07**89 has the code since you can spot 007 when reading from left to right. The code can be separated by other numbers, but as long as it is present in whole, the answer is Yes.

Step 3: You can use formulas, Power Query, VBA or rugged good looks to solve this.

**Go ahead and post your solutions in the comments area.**

Note: when posting your formula answers, just assume B4 has the shipment number.

Want more problems to solve?
----------------------------

As a transport manifest analyst life can be a bit drab. Worry not, I have several more challenges for you. Solve these problems (click on title or image).

### [Job title matching problem](https://chandoo.org/wp/job-title-matching-problem/)

[![Can you match the job titles?](https://chandoo.org/wp/wp-content/uploads/2019/08/job-title-matching-problem.png)](https://chandoo.org/wp/job-title-matching-problem/)

Can you match the job titles?

### [Any repetitions in the number?](https://chandoo.org/wp/number-has-repetitive-digits-formula/)

[![repetitive digits in the number...](https://chandoo.org/wp/wp-content/uploads/2017/10/number-has-repetitive-digits.png)](https://chandoo.org/wp/number-has-repetitive-digits-formula/)

One of them has too many fives

### [Elevator problem](https://chandoo.org/wp/elevator-problem/)

[![Elevator problem - excel formula homework](https://chandoo.org/wp/wp-content/uploads/2018/12/elevator-problem.png)](https://chandoo.org/wp/elevator-problem/)

Can the elevator go?

### [IF blood pressure problem](https://chandoo.org/wp/bp-category-problem/)

[![BP - have it or not?](https://chandoo.org/wp/wp-content/uploads/2016/11/bp-category-problem.png)](https://chandoo.org/wp/bp-category-problem/)

BP – Have it or not?

[Click me for more Excel Homework Problems & Puzzles](https://chandoo.org/wp/tag/homework/)

![Chandoo](https://chandoo.org/wp/wp-content/uploads/2018/05/chandoo-profile-pic.png)

**Hello Awesome...**

My name is Chandoo. Thanks for dropping by. My mission is to make you awesome in Excel & your work. I live in Wellington, New Zealand. When I am not F9ing my formulas, I cycle, cook or play lego with my kids. Know more [about me](https://chandoo.org/wp/about/)
.

I hope you enjoyed this article. Visit [Excel for Beginner](https://chandoo.org/wp/excel-basics/)
 or [Advanced Excel](https://chandoo.org/wp/advanced-excel-skills/)
 pages to learn more or join my [online video class to master Excel](https://chandoo.org/wp/excel-school-program/)
.

Thank you and see you around.

### Related articles:

|     |     |
| --- | --- |
| Written by Chandoo  <br>Tags: [homework](https://chandoo.org/wp/tag/homework/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 33 Responses to “Is there a secret code in this data? \[Excel Homework\]”

1.  ![](https://secure.gravatar.com/avatar/fdc8796dc22faa7287a2f49c81ecd6999d34e243f6b8ae7302248deee9587a98?s=64&d=mm&r=g) Charles Smith says:
    
    [March 27, 2020 at 9:19 am](https://chandoo.org/wp/secret-code-problem/#comment-1768610)
    
    \=IF(NOT(ISERR(FIND("0",B4)+FIND("0",B4,FIND("0",B4)+1)+FIND("7",B4,FIND("0",B4,FIND("0",B4)+1)))),"Yes","No")
    
    [Reply](https://chandoo.org/wp/secret-code-problem/#comment-1768610)
    
2.  ![](https://secure.gravatar.com/avatar/bcb526d24ca8bd9c69fc990c1c3ae6e1dadbb92dc9a4e71a6dfbc855e116d5c9?s=64&d=mm&r=g) Shiv says:
    
    [March 27, 2020 at 9:29 am](https://chandoo.org/wp/secret-code-problem/#comment-1768618)
    
    Make 4 columns. Find position of first 0 in First column using Find/Search Function, position of 2nd 0 using same function but string should be limited to after First 0. This can be achieved by using Len function and removing number of Characters in first column. In third, use Find to search 7 but string should be limited to after 2nd 0. That can be done by adding characters in 1st & 2nd column. Suitably insert IFERROR with some text if in case of error. In the fourth one, with the help of AND & ISNUMBER, find out True values, there you have your answer-Shipping Numbers with 007 in it! Sigh! pretty long solution though..
    
    [Reply](https://chandoo.org/wp/secret-code-problem/#comment-1768618)
    
3.  ![](https://secure.gravatar.com/avatar/390e89ce769ba80dd18c773f485c678a648a67d0b31a9f092f24f6baeaf2529f?s=64&d=mm&r=g) p45cal says:
    
    [March 27, 2020 at 12:41 pm](https://chandoo.org/wp/secret-code-problem/#comment-1768762)
    
    In D4 copied down:  
    \=IF(ISNUMBER(SEARCH("\*0\*0\*7\*",B4)),"Yes","No")
    
    VBA:  
    Sub blah()  
    For Each cll In Range("B4:B23").Cells  
    If cll.Value Like "\*0\*0\*7\*" Then cll.Offset(, 3) = "Yes" Else cll.Offset(, 3) = "No"  
    Next cll  
    End Sub
    
    VBA if you've got an awful lot:  
    Sub blah2()  
    With Range("B4:B23")  
    x = .Value  
    For rw = 1 To UBound(x)  
    If x(rw, 1) Like "\*0\*0\*7\*" Then x(rw, 1) = "Yes" Else x(rw, 1) = "No"  
    Next rw  
    .Offset(, 3).Value = x  
    End With  
    End Sub
    
    [Reply](https://chandoo.org/wp/secret-code-problem/#comment-1768762)
    
    *   ![](https://secure.gravatar.com/avatar/bbe5488709e9753f4c9c56b9807c3dd1aed314b77c3f756d54c4a26e75aa4b2b?s=64&d=mm&r=g) JasonW says:
        
        [March 29, 2020 at 11:40 am](https://chandoo.org/wp/secret-code-problem/#comment-1769536)
        
        This formula is beautiful! Very elegant!
        
        [Reply](https://chandoo.org/wp/secret-code-problem/#comment-1769536)
        
    *   ![](https://secure.gravatar.com/avatar/8faaa1631defbb25100fb61878fe5303affb2954b894529c2b56c2b463673163?s=64&d=mm&r=g) Ankur Sharma says:
        
        [April 8, 2020 at 3:20 pm](https://chandoo.org/wp/secret-code-problem/#comment-1774410)
        
        Liked Your Formula!
        
        [Reply](https://chandoo.org/wp/secret-code-problem/#comment-1774410)
        
4.  ![](https://secure.gravatar.com/avatar/feaa65776123654eb2d16552da8968a10a5537a49648eaa435b247fd13760a21?s=64&d=mm&r=g) Patrick Reagan says:
    
    [March 27, 2020 at 2:14 pm](https://chandoo.org/wp/secret-code-problem/#comment-1768833)
    
    That could simply be:  
    \=IFERROR(IF(SEARCH("\*0\*0\*7\*",B4)=1,"Yes"),"No")
    
    [Reply](https://chandoo.org/wp/secret-code-problem/#comment-1768833)
    
    *   ![](https://secure.gravatar.com/avatar/3cadfe58db2042c21f0cd397fb361481860cfb564046f4404ff72e0e43122799?s=64&d=mm&r=g) neil R Auty says:
        
        [March 28, 2020 at 11:39 am](https://chandoo.org/wp/secret-code-problem/#comment-1769264)
        
        You could leave out the =1 bit and still gives the correct answer.  
        I went the long way about this, totally forgot wildcard search so did a long walking nested find solution...  
        Nicely done
        
        [Reply](https://chandoo.org/wp/secret-code-problem/#comment-1769264)
        
5.  ![](https://secure.gravatar.com/avatar/65bec3eab87b735a2b5c637107afcf08f25c1975ec932ddd8d65a2d597b37949?s=64&d=mm&r=g) Cratze says:
    
    [March 27, 2020 at 3:35 pm](https://chandoo.org/wp/secret-code-problem/#comment-1768889)
    
    \=IFERROR(IF(FIND(7,B4,FIND(0,B4,FIND(0,B4)+1))>0,"Yes"),"No")
    
    [Reply](https://chandoo.org/wp/secret-code-problem/#comment-1768889)
    
6.  ![](https://secure.gravatar.com/avatar/1598c78c3a3c055e277b9b072ffbf6783713a7ea48a92490a1085987194058b3?s=64&d=mm&r=g) [Daniel Ferry](http://excelhero.com/)
     says:
    
    [March 27, 2020 at 5:57 pm](https://chandoo.org/wp/secret-code-problem/#comment-1768992)
    
    {=IF(ISERR(SEARCH("\*0\*0\*7\*",B4)),"No","Yes")}
    
    [Reply](https://chandoo.org/wp/secret-code-problem/#comment-1768992)
    
    *   ![](https://secure.gravatar.com/avatar/1d0554e77132128be0f059e11fbed771cd0a1372b32a6a62259185a31ea78a8a?s=64&d=mm&r=g) Vineet Sharma says:
        
        [March 27, 2020 at 7:40 pm](https://chandoo.org/wp/secret-code-problem/#comment-1769059)
        
        I found some good content on your web also.
        
        [Reply](https://chandoo.org/wp/secret-code-problem/#comment-1769059)
        
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [March 27, 2020 at 9:15 pm](https://chandoo.org/wp/secret-code-problem/#comment-1769106)
        
        Welcome back to the comments hero.
        
        [Reply](https://chandoo.org/wp/secret-code-problem/#comment-1769106)
        
7.  ![](https://secure.gravatar.com/avatar/5e5dc3c67241034178eea2079b8aa8ffd31cac0204b3d23487efb359dee8966d?s=64&d=mm&r=g) Esakki Rajesh M says:
    
    [March 27, 2020 at 5:57 pm](https://chandoo.org/wp/secret-code-problem/#comment-1768993)
    
    \=IF(ISERROR(FIND(7,MID(MID(B4,FIND(0,B4)+1,LEN(B4)),FIND(0,MID(B4,FIND(0,B4),LEN(B4)))+1,LEN(MID(B4,FIND(0,B4),LEN(B4)))))),"No","Yes")
    
    [Reply](https://chandoo.org/wp/secret-code-problem/#comment-1768993)
    
8.  ![](https://secure.gravatar.com/avatar/9955e6f8bc06bf52999acce65be64b1a7f8c1e86629144538e654f4cea903229?s=64&d=mm&r=g) Latiff says:
    
    [March 27, 2020 at 6:09 pm](https://chandoo.org/wp/secret-code-problem/#comment-1769004)
    
    Multiple helper columns:  
    Position of 1st 0: =IFERROR(FIND(B$2,$A3,1),"")  
    Position of 2nd 0: =IFERROR(IF($B3"",FIND(C$2,$A3,$B3+1),""),"")  
    Position of 7 after second 0: =IFERROR(FIND(D$2,$A3,$C3+1),"")  
    3 digit code check: =IF(LEN(TEXTJOIN("",TRUE,B3:D3))=3,1,"")  
    Code Sequence Check: =IF(AND(B3<C3,C3<D3),"YES","NO")  
    Code present: =IF(E3=1,F3,"NO")
    
    convoluted but works.
    
    [Reply](https://chandoo.org/wp/secret-code-problem/#comment-1769004)
    
9.  ![](https://secure.gravatar.com/avatar/1d0554e77132128be0f059e11fbed771cd0a1372b32a6a62259185a31ea78a8a?s=64&d=mm&r=g) Vineet says:
    
    [March 27, 2020 at 7:35 pm](https://chandoo.org/wp/secret-code-problem/#comment-1769053)
    
    Thanks, guys. Recalled my Linux programming days. I can't imagine that \*x\* could also be used here.
    
    [Reply](https://chandoo.org/wp/secret-code-problem/#comment-1769053)
    
10.  ![](https://secure.gravatar.com/avatar/9e746ac1bbfda8df2ecc12d220951075686cbb29d6cff973e78899983550fa15?s=64&d=mm&r=g) Manoj Choudhary says:
    
    [March 27, 2020 at 10:09 pm](https://chandoo.org/wp/secret-code-problem/#comment-1769125)
    
    \=IF(ISERROR(SEARCH(7,B4,SEARCH(0,B4,SEARCH(0,B4,1)+1)+1)),"No","Yes")
    
    [Reply](https://chandoo.org/wp/secret-code-problem/#comment-1769125)
    
11.  ![](https://secure.gravatar.com/avatar/3cadfe58db2042c21f0cd397fb361481860cfb564046f4404ff72e0e43122799?s=64&d=mm&r=g) neil R Auty says:
    
    [March 28, 2020 at 11:41 am](https://chandoo.org/wp/secret-code-problem/#comment-1769265)
    
    \=IFERROR(IF(FIND(7,B4,(FIND(0,B4,(FIND(0,B4))+1))+1),"Yes"),"No")
    
    [Reply](https://chandoo.org/wp/secret-code-problem/#comment-1769265)
    
12.  ![](https://secure.gravatar.com/avatar/dcb6d1617b2e5590a94eeb14b03943b2ea54629c593099d393f85d9a91eec268?s=64&d=mm&r=g) Alexander says:
    
    [March 28, 2020 at 3:51 pm](https://chandoo.org/wp/secret-code-problem/#comment-1769319)
    
    \=IF(IFERROR(FIND("007";SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(B4;1;"");2;"");3;"");4;"");5;"");6;"");8;"");9;""));0)>0;"Yes";"No")
    
    [Reply](https://chandoo.org/wp/secret-code-problem/#comment-1769319)
    
13.  ![](https://secure.gravatar.com/avatar/390e89ce769ba80dd18c773f485c678a648a67d0b31a9f092f24f6baeaf2529f?s=64&d=mm&r=g) p45cal says:
    
    [March 28, 2020 at 4:18 pm](https://chandoo.org/wp/secret-code-problem/#comment-1769326)
    
    I put together a Power Query solution to this a few days ago, but didn't post it because I'm new to Power Query and I don't know the full range of functions available within it, but since no-one has posted one I'll link to my rooky efforts here:  
    [https://app.box.com/s/f7rxwlg0g4etvk9ziweu7ztj8gz0qrbz](https://app.box.com/s/f7rxwlg0g4etvk9ziweu7ztj8gz0qrbz)
      
    where there's a couple of macros too (not related to the Power Query offering).
    
    [Reply](https://chandoo.org/wp/secret-code-problem/#comment-1769326)
    
14.  ![](https://secure.gravatar.com/avatar/bbe5488709e9753f4c9c56b9807c3dd1aed314b77c3f756d54c4a26e75aa4b2b?s=64&d=mm&r=g) JasonW says:
    
    [March 29, 2020 at 11:42 am](https://chandoo.org/wp/secret-code-problem/#comment-1769537)
    
    Having look at the other solutions, I see I used a long way around:
    
    \=IF(  
    IFERROR(SMALL(UNIQUE(IFERROR(SEARCH(0,B4,SEQUENCE(LEN(B4))),"")),2),"")<  
    IFERROR(MAX(UNIQUE(IFERROR(SEARCH(7,B4,SEQUENCE(LEN(B4))),""))),""),  
    "Yes","No")
    
    Using wildcards is brilliant!
    
    [Reply](https://chandoo.org/wp/secret-code-problem/#comment-1769537)
    
15.  ![](https://secure.gravatar.com/avatar/34fd573417aa331391293d4f65b2a93354b63f684501e97f96f4358aed8ee132?s=64&d=mm&r=g) Lee T says:
    
    [March 29, 2020 at 10:17 pm](https://chandoo.org/wp/secret-code-problem/#comment-1769659)
    
    \=IF(IFERROR(SEARCH(7,B4),"No")="No","No",IF(ISERROR(SEARCH(7,B4,SEARCH(0,B4,SUM(SEARCH(0,B4)+1)))),"No","Yes"))  
    1st time i have had some time to do the homework (wonder why that it is!), thought my solution was good until i saw the other posts, some really efficient coding. Room for me to improve!
    
    [Reply](https://chandoo.org/wp/secret-code-problem/#comment-1769659)
    
16.  ![](https://secure.gravatar.com/avatar/120651dab1a25525bbf7cbf786e40429b7bf1aa61b55c2479d62844eb2ff5afd?s=64&d=mm&r=g) Matt Brook says:
    
    [March 30, 2020 at 3:38 pm](https://chandoo.org/wp/secret-code-problem/#comment-1769888)
    
    Option Explicit
    
    Public Const HIDDEN\_MESSAGE As String = "007"
    
    Public Function IsSecretCodePresent(ByVal cellContents As Range) As String
    
    Dim secret() As String  
    Dim message() As String  
    Dim functionResult As String
    
    functionResult = ""
    
    secret() = SplitStringIntoStringArray(HIDDEN\_MESSAGE)  
    message() = SplitStringIntoStringArray(cellContents.Value)
    
    If IsCodeEmbedded(secret(), message()) Then  
    functionResult = "Yes"  
    Else  
    functionResult = "No"  
    End If
    
    IsSecretCodePresent = functionResult
    
    End Function
    
    Private Function SplitStringIntoStringArray(ByVal stringIn As String) As String()
    
    Dim temp() As String  
    Dim i As Integer
    
    ReDim temp(Len(stringIn) - 1)
    
    For i = 1 To Len(stringIn)  
    temp(i - 1) = Mid$(stringIn, i, 1)  
    Next
    
    SplitStringIntoStringArray = temp()
    
    End Function
    
    Private Function IsCodeEmbedded(ByRef codeIn() As String, ByRef messageIn() As String) As Boolean
    
    Dim functionResult As Boolean  
    Dim codeCounter As Integer  
    Dim messageCounter As Integer  
    Dim lastCounterValue As Integer  
    Dim codeCount As Integer  
    Dim checkArray() As Integer  
    Dim checkCounter As Integer  
    Dim currentCodeItem As String  
    Dim currentMessageItem As String  
    Dim individualCodesFound As Integer  
    Dim messageLBoundValue As Integer  
    Dim forceLoopJump As Boolean  
    Dim forceLoopStop As Boolean
    
    functionResult = False  
    lastCounterValue = 0  
    forceLoopJump = False  
    forceLoopStop = False
    
    ' Get the First Item in the message array  
    messageLBoundValue = LBound(messageIn)
    
    ' Get number of items in the Seret Code  
    codeCount = UBound(codeIn) - LBound(codeIn) + 1
    
    ' Create Array to keep Checks on each item in the Secret Code are present  
    ReDim checkArray(0 To codeCount - 1)  
    For checkCounter = LBound(checkArray) To UBound(checkArray)  
    checkArray(checkCounter) = 0  
    Next checkCounter
    
    ' Loop through items in Secret Code  
    For codeCounter = LBound(codeIn) To UBound(codeIn)
    
    currentCodeItem = codeIn(codeCounter)
    
    ' Loop through message  
    For messageCounter = messageLBoundValue To UBound(messageIn)
    
    currentMessageItem = messageIn(messageCounter)
    
    ' If there is a match, record position in message  
    ' so in next item in Code can start in last  
    ' position in message checked  
    If currentMessageItem = currentCodeItem Then
    
    checkArray(codeCounter) = 1  
    lastCounterValue = messageCounter  
    forceLoopJump = True
    
    Exit For
    
    End If
    
    Next messageCounter
    
    If forceLoopJump = True Then  
    messageLBoundValue = lastCounterValue + 1  
    Else  
    ' If we have cycled through message and haven't found  
    ' the code, then exit function returning false  
    If checkArray(codeCounter) = 0 Then  
    forceLoopStop = True  
    End If  
    End If
    
    If forceLoopStop = True Then  
    Exit For  
    End If
    
    Next codeCounter
    
    ' Find out how many items of the Secret Code were found  
    For checkCounter = LBound(checkArray) To UBound(checkArray)  
    individualCodesFound = individualCodesFound + checkArray(checkCounter)  
    Next checkCounter
    
    functionResult = (individualCodesFound = codeCount)
    
    IsCodeEmbedded = functionResult
    
    End Function
    
    [Reply](https://chandoo.org/wp/secret-code-problem/#comment-1769888)
    
    *   ![](https://secure.gravatar.com/avatar/1598c78c3a3c055e277b9b072ffbf6783713a7ea48a92490a1085987194058b3?s=64&d=mm&r=g) [Daniel Ferry](http://excelhero.com/)
         says:
        
        [March 30, 2020 at 5:59 pm](https://chandoo.org/wp/secret-code-problem/#comment-1769927)
        
        Matt, try this:
        
        Function CodeFound(d$, k$)  
        Dim i&, j&  
        For i = 1 To Len(d)  
        If Mid(d, i, 1) = Mid(k, j + 1, 1) Then j = j + 1  
        Next  
        CodeFound = "No"  
        If j = Len(k) Then CodeFound = "Yes"  
        End Function
        
        [Reply](https://chandoo.org/wp/secret-code-problem/#comment-1769927)
        
    *   ![](https://secure.gravatar.com/avatar/b00cb1ccc8b0f9e459e083299d7f8569c99a562e06ede9844630e2b21bf4ba0c?s=64&d=mm&r=g) Jeremy says:
        
        [March 31, 2020 at 10:15 pm](https://chandoo.org/wp/secret-code-problem/#comment-1770170)
        
        Longest answer ever, I love it 🙂
        
        [Reply](https://chandoo.org/wp/secret-code-problem/#comment-1770170)
        
17.  ![](https://secure.gravatar.com/avatar/b00cb1ccc8b0f9e459e083299d7f8569c99a562e06ede9844630e2b21bf4ba0c?s=64&d=mm&r=g) Jeremy says:
    
    [March 31, 2020 at 10:17 pm](https://chandoo.org/wp/secret-code-problem/#comment-1770171)
    
    Simplest solution I found
    
    \=IF(ISNUMBER(SEARCH("0\*0\*7",B4,1)),"Yes","No")
    
    [Reply](https://chandoo.org/wp/secret-code-problem/#comment-1770171)
    
18.  ![](https://secure.gravatar.com/avatar/ff9057b90b9209d63d104c8a489826d80fa5c02d826f0704774e182bc994fc95?s=64&d=mm&r=g) Mark Williams says:
    
    [April 1, 2020 at 5:24 am](https://chandoo.org/wp/secret-code-problem/#comment-1770226)
    
    This was the first challenge I've tried...happy to find a solution but very impressed with the other solutions here...
    
    \=IF(IFERROR(FIND("7",B4,FIND("0",B4,FIND("0",B4)+1)+1),-1)>0,"Yes","No")
    
    [Reply](https://chandoo.org/wp/secret-code-problem/#comment-1770226)
    
19.  ![](https://secure.gravatar.com/avatar/f8eca86882ee63558ecde075557c57afeb162e275cad88487c6bd5f65816a3b4?s=64&d=mm&r=g) Jim says:
    
    [April 2, 2020 at 1:43 pm](https://chandoo.org/wp/secret-code-problem/#comment-1770629)
    
    Another (and longer) version is this:  
    \=ISNUMBER(FIND("007",SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(B4,2,""),3,""),4,""),5,""),6,""),8,""),9,""),1))
    
    [Reply](https://chandoo.org/wp/secret-code-problem/#comment-1770629)
    
20.  ![](https://secure.gravatar.com/avatar/7ef7b54c5d60458bbe6e6a654994b746f1178f025451e1c1456711c212a5c9c0?s=64&d=mm&r=g) MichaelCH says:
    
    [April 6, 2020 at 8:26 am](https://chandoo.org/wp/secret-code-problem/#comment-1772499)
    
    \=IF(ISNUMBER(SEARCH("0\*0\*7",B4)),"Yes","No")  
    \=IF(ISERR(SEARCH("0\*0\*7",B4)),"No","Yes")  
    \=MID("YesNo",ISERR(SEARCH("0\*0\*7",B4))\*3+1,3)
    
    UDF:  
    Function Is\_007(s As String) As String  
    If s Like "\*0\*0\*7\*" Then Is\_007 = "Yes" Else Is\_007 = "No"  
    End Function
    
    [Reply](https://chandoo.org/wp/secret-code-problem/#comment-1772499)
    
21.  ![](https://secure.gravatar.com/avatar/7ef7b54c5d60458bbe6e6a654994b746f1178f025451e1c1456711c212a5c9c0?s=64&d=mm&r=g) MichaelCH says:
    
    [April 6, 2020 at 8:44 am](https://chandoo.org/wp/secret-code-problem/#comment-1772515)
    
    \=CHOOSE(ISERR(SEARCH("0\*0\*7",B4))+1,"Yes","No")  
    \=IF(COUNT(SEARCH("0\*0\*7",B4)),"Yes","No")  
    \=MID("YesNo",4^ISERR(SEARCH("0\*0\*7",B4)),3)
    
    [Reply](https://chandoo.org/wp/secret-code-problem/#comment-1772515)
    
22.  ![](https://secure.gravatar.com/avatar/7ef7b54c5d60458bbe6e6a654994b746f1178f025451e1c1456711c212a5c9c0?s=64&d=mm&r=g) MichaelCH says:
    
    [April 6, 2020 at 8:55 am](https://chandoo.org/wp/secret-code-problem/#comment-1772530)
    
    \=IFERROR(IF(SEARCH("0\*0\*7",B4),"Yes"),"No")
    
    [Reply](https://chandoo.org/wp/secret-code-problem/#comment-1772530)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [April 6, 2020 at 9:30 am](https://chandoo.org/wp/secret-code-problem/#comment-1772563)
        
        Those are some very interesting formulas. I liked the MID versions especially 🙂
        
        [Reply](https://chandoo.org/wp/secret-code-problem/#comment-1772563)
        
23.  ![](https://secure.gravatar.com/avatar/985b05d24811dd2f1e9f611dfff406e6b225215081e6c969e2ceaffc7784c62c?s=64&d=mm&r=g) ELIENAY JUNIOR says:
    
    [September 23, 2020 at 5:29 pm](https://chandoo.org/wp/secret-code-problem/#comment-1884070)
    
    I used a matrix formula to solve this. I only know how to use matrix formulas to solve kkkk problems.
    
    \=IF(SUM(IFERROR(IF((MID(LEFT(B4,MAX(IF(MID(B4,ROW(INDIRECT("1:"&LEN(B4))),1)+0=7,ROW(INDIRECT("1:"&LEN(B4))),""))),ROW(INDIRECT("1:"&LEN(B4))),1)+0)=0,1,""),""))>1,1,"")
    
    [Reply](https://chandoo.org/wp/secret-code-problem/#comment-1884070)
    
24.  ![](https://secure.gravatar.com/avatar/457dc7c8ab50238c6c9a83c2b8b3ba05c038094f6749409e1bbb130842d276e8?s=64&d=mm&r=g) Irvine Russell says:
    
    [October 2, 2020 at 1:40 pm](https://chandoo.org/wp/secret-code-problem/#comment-1892769)
    
    I used the RegEx pack in VBA to create a UDF:
    
    Function simpleCellRegex(Myrange As Range, strPattern As String) As String  
    Dim regEx As New RegExp  
    Dim strInput As String  
    Dim strReplace As String  
    Dim strOutput As String
    
    If strPattern "" Then  
    strInput = Myrange.Value  
    strReplace = ""
    
    With regEx  
    .Global = True  
    .MultiLine = True  
    .IgnoreCase = False  
    .pattern = strPattern  
    End With
    
    If regEx.test(strInput) Then  
    simpleCellRegex = regEx.Replace(strInput, strReplace)  
    Else  
    simpleCellRegex = "Not matched"  
    End If  
    End If  
    End Function
    
    and then used the following formula to test:  
    \=IF(simpleCellRegex(B4,"\\d\*0\\d\*0\\d\*7\\d\*")"Not Matched","Yes","No")
    
    [Reply](https://chandoo.org/wp/secret-code-problem/#comment-1892769)
    
25.  ![](https://secure.gravatar.com/avatar/f11beb7d93eb45e646f02f6f8f7b715f28eab4e47945849db1e807635c1bdbc6?s=64&d=mm&r=g) Tony says:
    
    [April 24, 2023 at 4:33 pm](https://chandoo.org/wp/secret-code-problem/#comment-2125996)
    
    \=LET( a, FIND("0",B4), b, FIND("0",B4,a+1), c, FIND("7",B4,b+1), IF(ISNUMBER(a + b + c),"Yes","No"))
    
    [Reply](https://chandoo.org/wp/secret-code-problem/#comment-2125996)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/secret-code-problem/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Number to Words – Excel Formula](https://chandoo.org/wp/number-to-words-formula/) | [There are 20 Easter Eggs in this Workbook](https://chandoo.org/wp/easter-eggs-2020/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)