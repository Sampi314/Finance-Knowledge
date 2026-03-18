# Check if 2 ranges have same values (set equality problem) » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem

---

Check if 2 ranges have same values (set equality problem)
=========================================================

[Excel Challenges](https://chandoo.org/wp/category/excel-challenges/)
 - 71 comments

  

Hello folks,

Time for another homework problem. **Assuming you have 2 ranges of values like below, how do you check if both of them have same set of values?**

![check-2-ranges-have-same-values](https://chandoo.org/wp/wp-content/uploads/2015/03/check-2-ranges-have-same-values.png)

You may assume that these ranges are named _range1_ & _range2._ 

**Please post your answers in the comments section.**

### A bonus question…

How do you find the first equal set of _source_ in the range _target?_ 

For example, for below scenario, **source = 2nd column of target**.

So the expected answer is 2 for this question.

![find-the-equal-set-from-a-range](https://chandoo.org/wp/wp-content/uploads/2015/03/find-the-equal-set-from-a-range.png)

Please assume the source & target ranges are named as _source_ and _target._

Go ahead and share your comments. I am very keen to see what kind of creative & elegant solutions we can come up to solve this problem.

**Want more homework or Excel challenges?**

Check out our [Excel challenges page](http://chandoo.org/wp/excel-problems-challenges/ "Excel Problems & Challenges")
 & [homework](http://chandoo.org/wp/tag/homework/)
 tag for more problems. Be warned though, serious workouts for your brain ahead. Your mind will have a six pack at the end of it all.

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
| Written by Chandoo  <br>Tags: [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)<br>, [duplicates](https://chandoo.org/wp/tag/duplicates/)<br>, [homework](https://chandoo.org/wp/tag/homework/)<br>, [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)<br>, [sets](https://chandoo.org/wp/tag/sets/)<br>, [unique items](https://chandoo.org/wp/tag/unique-items/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 71 Responses to “Check if 2 ranges have same values (set equality problem)”

1.  ![](https://secure.gravatar.com/avatar/50b582c4d1420c1f6f08e60024e99f5b8ec282f2f24aa7925cc2cd31a05acb8c?s=64&d=mm&r=g) Somendra Misra says:
    
    [March 10, 2015 at 8:34 am](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927322)
    
    Hi Chandoo,
    
    May be something like:
    
    For first problem:  
    \=IFERROR(SUMPRODUCT(--(MATCH(Range1,Range2,0)>0))=COUNTA(Range1),FALSE)
    
    For Bonus Question, WITH CSE:  
    \=MATCH(TRUE,MMULT(COUNTIF(Source,TRANSPOSE(Target)),{1;1;1;1;1})=COUNTA(Source),0)
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927322)
    
2.  ![](https://secure.gravatar.com/avatar/7e4971c3152778fde7ddedad4cb22034f624d5d198c7de681ed43fe2a1d3044f?s=64&d=mm&r=g) Desk Lamp says:
    
    [March 10, 2015 at 8:48 am](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927328)
    
    Problem1: =AND(range1=range2)  
    Ctrl+Shift+Enter
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927328)
    
    *   ![](https://secure.gravatar.com/avatar/4da90559efec9bdcf59678aabff82628d37fdcd92041807092e3bf213fe5759f?s=64&d=mm&r=g) Rob says:
        
        [March 11, 2015 at 10:12 am](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928016)
        
        This is great but only works if the items in each range are in the same order. Ranges 1 & 2 above are identical but in different orders
        
        [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928016)
        
3.  ![](https://secure.gravatar.com/avatar/50bf79d6f504e406a21d930a4ea90388f16dd95e9f04cbef9c2394b7fa2dad03?s=64&d=mm&r=g) Satish says:
    
    [March 10, 2015 at 10:23 am](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927373)
    
    For First Problem It May be Just Compare 2 Columns  
    \=Range1=Range2 --- Result will be "True" if column Data match  
    \---- Result will be "False" if Column Data Don't Match
    
    Second Question i not completely understand. what to do in That
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927373)
    
4.  ![](https://secure.gravatar.com/avatar/0d18958dd4886de3f23bbbd5cc75145332ce2e3ba0177031bf9ed33ff17484fe?s=64&d=mm&r=g) [Elchin Khalilov](http://excelchin.wordpress.com/)
     says:
    
    [March 10, 2015 at 10:53 am](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927396)
    
    First of all, I would put an additional column using VLOOKUP function to find whether a value in Range 1 exists in Range 2. And if so I will bring that value using the same VLOOKUP function.  
    Then using IF function will show me whether value in Range 1 corresponds to the value generated by VLOOKUP function.
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927396)
    
5.  ![](https://secure.gravatar.com/avatar/08946ae8163fb8b320bf10e520933033ff0d8223317ffdb665765ed3b8eefad0?s=64&d=mm&r=g) Dick Byrne says:
    
    [March 10, 2015 at 11:58 am](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927434)
    
    Main question:
    
    \=AND(NOT(ISNA(MATCH(Range1, Range2, 0))))
    
    Enter as an array formula (CSE)
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927434)
    
6.  ![](https://secure.gravatar.com/avatar/08946ae8163fb8b320bf10e520933033ff0d8223317ffdb665765ed3b8eefad0?s=64&d=mm&r=g) Dick Byrne says:
    
    [March 10, 2015 at 12:05 pm](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927439)
    
    Ah but what if the ranges are different sizes? Then you need a two way check ...
    
    \=AND(NOT(ISNA(MATCH(Range2, Range1, 0))), NOT(ISNA(MATCH(Range1, Range2, 0))))
    
    Entered as an array function (CSE)
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927439)
    
7.  ![](https://secure.gravatar.com/avatar/7bbd3375773d818af330ee8e3ea6b839409e5281c0b66372301352a10fff8ad6?s=64&d=mm&r=g) Jason Morin says:
    
    [March 10, 2015 at 2:35 pm](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927496)
    
    Assuming ranges are same dimensions as in the example:
    
    \=SUMPRODUCT(1\*ISNA(MATCH(range1,range2,0)))=0
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927496)
    
8.  ![](https://secure.gravatar.com/avatar/7612d271ebeed8274c9847cacb35276e2738a4128250cb5d0d600926ab256013?s=64&d=mm&r=g) Michael says:
    
    [March 10, 2015 at 2:42 pm](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927498)
    
    First problem (Array formula):
    
    \=AND(COUNTIF(range1,range2)=IF(range1=range1,1,0),COUNTIF(range2,range1)=IF(range2=range2,1,0))
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927498)
    
9.  ![](https://secure.gravatar.com/avatar/9e3113d4884dc7290dab0c7ad609fe3eb083382b6cd604e2c9de83c0461aafa2?s=64&d=mm&r=g) Ericson says:
    
    [March 10, 2015 at 7:34 pm](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927637)
    
    Problem #2
    
    \=(Geomean(source)^var.s(source))-(geomean(target2)^var.s(target2))
    
    A zero indicates same. A variety of math equations can be used this is just one. I could have chosen logs. The point is to make the range a unique value and compare the next range using same methodology. Only works for numbers and the probability of this failing falls well below an "I trust excel enough for the array to work"
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927637)
    
10.  ![](https://secure.gravatar.com/avatar/3cdf9fe7a585c56d99c879d6e062c94cd52587814f8098379acf39d946fd145b?s=64&d=mm&r=g) [XOR LX](http://excelxor.com/)
     says:
    
    [March 10, 2015 at 10:06 pm](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927689)
    
    Hi Chandoo.
    
    In all of your examples each of the values from a given range is unique within that range. Is it safe to assume that this will always be the case?
    
    Or could you have a case such as:
    
    range1: "DEF", "DEF", "GHI", "JKL", "MNO"  
    range2: "JKL", "GHI", "MNO", "DEF", "DEF"
    
    ?
    
    Regards
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927689)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [March 11, 2015 at 3:27 am](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927838)
        
        Hi XOR LX... you can assume that all values will be unique and ranges will have same size (number of cells).
        
        [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927838)
        
11.  ![](https://secure.gravatar.com/avatar/b8b93be3161caa7e8cc65a3ddb76c8cb8522cf1b99a3ea04af26af60bc08b88a?s=64&d=mm&r=g) Miguel says:
    
    [March 10, 2015 at 10:19 pm](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927695)
    
    I know is a easier way to do it and some one is going to clean this bit of code  
    Thanks a lot Chandoo  
    \========================================  
    Public Sub sameRange()  
    Dim setOne As Range  
    Dim setTwo As Range  
    Set setOne = Sheets("Sheet1").Range("range1")  
    Set setTwo = Sheets("Sheet1").Range("range2")
    
    'REMOVE THE COLOR FILL  
    setOne.Interior.ColorIndex = xlNone
    
    For Each cellitem In setOne  
    For Each cellItem2 In setTwo  
    If cellitem = cellItem2 Then  
    MsgBox "Found match at cell.." & cellitem.Address  
    Range("E2").Select
    
    ActiveCell.Value = cellitem  
    cellitem.Interior.ColorIndex = 50  
    End If  
    Next cellItem2  
    Next cellitem  
    End Sub  
    \======================  
    🙂
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927695)
    
    *   ![](https://secure.gravatar.com/avatar/46611bb84b2e659b0d14524bb6b6664949a4fd5d8a5103135dafdbbc6356baee?s=64&d=mm&r=g) Zak Naz says:
        
        [January 12, 2021 at 8:15 am](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-1961235)
        
        Great!  
        How to apply for non-equal contents for every named range in two workbooks with identical named ranges but different ranges?
        
        [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-1961235)
        
    *   ![](https://secure.gravatar.com/avatar/46611bb84b2e659b0d14524bb6b6664949a4fd5d8a5103135dafdbbc6356baee?s=64&d=mm&r=g) Zak Naz says:
        
        [January 12, 2021 at 10:23 am](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-1961257)
        
        Great!  
        How to use to highlight differences of cell contents of named ranges in two workbooks with identical named ranges and different range areas?
        
        [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-1961257)
        
12.  ![](https://secure.gravatar.com/avatar/64685707209622c7aca0e21921aa25e7f3b215b23ecbe9f124e32050540ac6bf?s=64&d=mm&r=g) [Maribeth EM](http://na/)
     says:
    
    [March 11, 2015 at 1:18 am](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927777)
    
    Use function EXACT. It compares two text strings and returns True if exactly the same and False if not. This function however is case-sensitive so if one is capitalized and the other is not, then it will return False.
    
    \=EXACT(A1,A2)
    
    assumption is that the text are in cells A1 and A2
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927777)
    
13.  ![](https://secure.gravatar.com/avatar/53171af15aafb76c22464531e8b8baf0559c159705f2d66e5f45546406e373ab?s=64&d=mm&r=g) [Linda Campbell](http://solvuconsulting.com.au/)
     says:
    
    [March 11, 2015 at 1:22 am](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927778)
    
    Problem 1:
    
    \=SUM((COUNTIFS(D3:D7,C3:C7))\*1)=COUNTA(C3:C7)  
    CTL ALT DLT
    
    Returns true if exact match, false otherwise
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927778)
    
    *   ![](https://secure.gravatar.com/avatar/e01e2c6ebc000b36efa6011b442f7f00f1d38cbfddcb0a95d0bb0a672444da13?s=64&d=mm&r=g) Nelson says:
        
        [March 11, 2015 at 6:07 pm](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928294)
        
        I think you mean Ctrl+Shift+Enter...
        
        [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928294)
        
        *   ![](https://secure.gravatar.com/avatar/53171af15aafb76c22464531e8b8baf0559c159705f2d66e5f45546406e373ab?s=64&d=mm&r=g) [Linda Campbell](http://solvuconsulting.com.au/)
             says:
            
            [March 16, 2015 at 1:24 am](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-931236)
            
            🙂 I think I do
            
            [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-931236)
            
14.  ![](https://secure.gravatar.com/avatar/ce59b0d8e22bf577f01d4211907632b05b396bfcf8c32699db707da405274298?s=64&d=mm&r=g) Steve S. says:
    
    [March 11, 2015 at 4:31 am](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927873)
    
    I would use conditional formatting for each range with the following formula in the conditional formatting :
    
    For Range 1:
    
    \=NOT(IFERROR(VLOOKUP(A2,Range\_2,1,0)=A2,0))
    
    For Range 2:
    
    \=NOT(IFERROR(VLOOKUP(C2,Range\_1,1,0)=C2,0))
    
    This gives me true/false for each cell and highlights any cells that are different.
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927873)
    
15.  ![](https://secure.gravatar.com/avatar/3574b2a697314dd916a135f893713a38ba917b60069044df49309acd96ce604f?s=64&d=mm&r=g) Ysahme says:
    
    [March 11, 2015 at 4:46 am](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927881)
    
    Hi Guys...  
    Good day!!!  
    Problem #1  
    I use IF Statement to another column and it return OK if same and blank if it is not...
    
    I also try match but it return me a Number meaning that range2 is in the number base on range1...
    
    That's what i answer....
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927881)
    
16.  ![](https://secure.gravatar.com/avatar/ebc2279778f6680cfec63abb39f60efbc63cb5df63b0bd176b9ebafb51aa58c2?s=64&d=mm&r=g) Harry S says:
    
    [March 11, 2015 at 5:03 am](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927893)
    
    ' got a bit if VBA instead  
    'use the data as at least 1 space around to use CurrentRegion
    
    TRUE Range 1 Range 2 Source Target
    
    ABC ABC 123 128 127 123 134 127 140  
    DEF GHI 124 129 123 126 135 123 141  
    GHI MNO 125 130 124 125 136 124 142  
    Not In Col 1 JKL JKL 126 131 126 124 137 125 143  
    In Col 2 MNO DEF 127 132 125 127 138 132 144  
    In Col 3 126  
    Not In Col 4  
    In Col 5  
    Not In Col 6
    
    '  
    Then code as
    
    \[code\]  
    Option Explicit  
    Function AllRaInRB(Ra As Range, Rb As Range) As Boolean  
    Dim CE As Range  
    For Each CE In Ra  
    If Rb.Find(CE) Is Nothing Then GoTo NotThere  
    ' see the Find ( Options .. ) like below if needed  
    ' If Rb.Find(CE, LookIn:=xlValues, lookat:=xlWhole, MatchCase:=False) Is Nothing Then GoTo NotThere  
    Next CE  
    AllRaInRB = True ' found them all  
    NotThere:  
    End Function  
    Private Sub CommandButton21\_Click()  
    Dim Ra As Range, Rb As Range, Rc%, Rot%  
    '  
    ' assuming Range header one space above the data and the range data is spaced from other data  
    ' the headers for the ranges can be whatever and anywhere in the active sheet  
    '  
    With ActiveSheet.UsedRange
    
    Set Ra = .Find("Range 1")(3, 1).CurrentRegion  
    Set Rb = .Find("Range 2")(3, 1).CurrentRegion
    
    \[b2\] = AllRaInRB(Ra, Rb) ' part A
    
    Set Ra = .Find("Source")(3, 1).CurrentRegion  
    Set Rb = .Find("Target")(3, 1).CurrentRegion  
    Rot = 6 ' row Out start  
    End With
    
    For Rc = 1 To Rb.Columns.Count ' finding all columns in Target  
    If AllRaInRB(Ra, Rb.Columns(Rc)) Then  
    Cells(Rot + Rc, 1) = " In Col " & Rc ' results down column A starting at Rot +1  
    Else  
    Cells(Rot + Rc, 1) = "Not In Col " & Rc  
    End If  
    Next Rc  
    End Sub  
    \[/code\]
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927893)
    
17.  ![](https://secure.gravatar.com/avatar/748b5ff4b26b20441021ea20ade031d6e958eda976172b9ce31017c91945e049?s=64&d=mm&r=g) Krishna says:
    
    [March 11, 2015 at 7:23 am](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927946)
    
    Hi all,
    
    Great answers. Please have a look at my  
    For first question:  
    {=(ISNUMBER(MATCH(Range1,Range2,0)))}  
    or as mentioned by Maribeth, we can use Exact function  
    {=EXACT(Range1, range2)}
    
    Use of CSE as we are dealing with ranges
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927946)
    
18.  ![](https://secure.gravatar.com/avatar/e314189b7e4697aefd49bde89e9354fc8c654f23b65214a3bef48ac9cc619e9c?s=64&d=mm&r=g) VISHAL says:
    
    [March 11, 2015 at 8:18 am](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927966)
    
    For First Problem  
    \=IF(A2=B2,TRUE,FALSE)
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927966)
    
19.  ![](https://secure.gravatar.com/avatar/3cdf9fe7a585c56d99c879d6e062c94cd52587814f8098379acf39d946fd145b?s=64&d=mm&r=g) [XOR LX](http://excelxor.com/)
     says:
    
    [March 11, 2015 at 8:30 am](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927971)
    
    Since Chandoo confirmed that the values in each range are unique within that range, CSE:
    
    \=AND(COUNTIF(range1,range2))
    
    Bonus Question, non-array:
    
    \=MATCH(5,MMULT({1,1,1,1,1},COUNTIF(source,target)),0)
    
    if the number of rows is fixed at 5, or, CSE:
    
    \=MATCH(COUNTA(source),MMULT(TRANSPOSE(ROW(source))^0,COUNTIF(source,target)),0)
    
    if the number of rows is dynamic.
    
    Regards
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927971)
    
    *   ![](https://secure.gravatar.com/avatar/16ee71d7bb19fb0945e3c63d50fe570a95e76be0a5d33b32cfe648c3163506a8?s=64&d=mm&r=g) [Oscar](http://www.get-digital-help.com/)
         says:
        
        [March 11, 2015 at 10:03 am](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928010)
        
        XOR LX
        
        Congratulations, your two first formulas are exactly the same formulas I was about to post here but you were faster.
        
        [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928010)
        
    *   ![](https://secure.gravatar.com/avatar/50b582c4d1420c1f6f08e60024e99f5b8ec282f2f24aa7925cc2cd31a05acb8c?s=64&d=mm&r=g) Somendra Misra says:
        
        [March 11, 2015 at 3:54 pm](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928181)
        
        XOR,
        
        Clever way of changing array1 with array2. 🙂
        
        See my formula in comment #1.
        
        Regards,
        
        [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928181)
        
        *   ![](https://secure.gravatar.com/avatar/3cdf9fe7a585c56d99c879d6e062c94cd52587814f8098379acf39d946fd145b?s=64&d=mm&r=g) [XOR LX](http://excelxor.com/)
             says:
            
            [March 12, 2015 at 7:57 am](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928879)
            
            @Somendra
            
            Yes - yours was of course the first post I saw, and a very good one as well.
            
            I just saw the opportunity to tweak your MMULT construction so that we donn't require the TRANSPOSE. 🙂
            
            Cheers
            
            [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928879)
            
20.  ![](https://secure.gravatar.com/avatar/d4605560751fc80b4ce7a9d0d69dfa8ee70962caae042e3d248dc9b8d793a423?s=64&d=mm&r=g) Gabriel says:
    
    [March 11, 2015 at 9:18 am](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927984)
    
    \=AND(SUM(SUM(--(vector\_2=vector\_1)))=COUNTA(vector\_1),COUNTA(vector\_1)=COUNTA(vector\_2))  
    Control+Shift + Enter. ( Array Formula )  
    example:( for ture)  
    vector 2 vector 1  
    abc abc  
    dei dei  
    copy copy  
    try try  
    bug bug  
    loop loop  
    example for False:  
    vector 2 vector 1  
    abc abc  
    bei dei  
    sopi copy  
    try try  
    bug bug  
    loop loop
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-927984)
    
21.  ![](https://secure.gravatar.com/avatar/3cdf9fe7a585c56d99c879d6e062c94cd52587814f8098379acf39d946fd145b?s=64&d=mm&r=g) [XOR LX](http://excelxor.com/)
     says:
    
    [March 11, 2015 at 10:33 am](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928025)
    
    @Oscar
    
    Cheers! And sorry! 🙂
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928025)
    
    *   ![](https://secure.gravatar.com/avatar/16ee71d7bb19fb0945e3c63d50fe570a95e76be0a5d33b32cfe648c3163506a8?s=64&d=mm&r=g) [Oscar](http://www.get-digital-help.com/)
         says:
        
        [March 11, 2015 at 12:10 pm](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928061)
        
        @XOR LX
        
        I wouldn´t have made the bonus question formula without learning the MMULT function from your blog.
        
        [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928061)
        
22.  ![](https://secure.gravatar.com/avatar/064e03fce862939ea2c6aee0a4ff917942ef32355fbc26b5ae8356a8d626a31b?s=64&d=mm&r=g) Ilyas says:
    
    [March 11, 2015 at 12:11 pm](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928062)
    
    For problem 1 i tried the following formula:  
    {=ISNUMBER(SUM(MATCH(Range2,Range1,0)))}
    
    For problem 2 i used the following formula in conditional formatting so that the matching column gets highlighted:
    
    \=ISNUMBER(SUM(MATCH(source,OFFSET(target,1,C$9-1,5,1),0)))
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928062)
    
23.  ![](https://secure.gravatar.com/avatar/250afddfe22885243d797cc10f9194ef2f8dbfcab4bba7714d0fa6360c7b10e7?s=64&d=mm&r=g) Bhavesh Soni says:
    
    [March 11, 2015 at 2:27 pm](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928120)
    
    Sum(match(range1)=(match(range2) will show true if all items are there. Note enter this as Array formula.
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928120)
    
24.  ![](https://secure.gravatar.com/avatar/250afddfe22885243d797cc10f9194ef2f8dbfcab4bba7714d0fa6360c7b10e7?s=64&d=mm&r=g) Bhavesh Soni says:
    
    [March 11, 2015 at 2:27 pm](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928122)
    
    Sum(match(range1)=(match(range2) will show true if all items are there. Note enter this as Array formula
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928122)
    
25.  ![](https://secure.gravatar.com/avatar/6fae93bd37cdb5f417443df81fbdaabda6c8fa867f3f340f4d727a589283dd9b?s=64&d=mm&r=g) cllach says:
    
    [March 11, 2015 at 2:32 pm](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928123)
    
    For first one:
    
    \=NOT(ISERROR(PRODUCT(MATCH(IF(Range1="""",""""&COUNTBLANK(Range1),Range1 & COUNTIF(Range1,Range1)),IF(Range2="""",""""&COUNTBLANK(Range2),Range2& COUNTIF(Range2,Range2)),0))))
    
    I think that works returning True for vertical ranges even if values are not unique (must appear same number of times), or empty or numeric, if ranges are diferent size it returns False.
    
    Easy to adapt to second one.
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928123)
    
    *   ![](https://secure.gravatar.com/avatar/25a9730846fc4b01d9c7fcb5e99efcd5ad98d0bbbd1e122049dee411b37690d2?s=64&d=mm&r=g) cllach says:
        
        [March 11, 2015 at 2:35 pm](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928127)
        
        Sorry, pasting doubled quotes...  
        \=NOT(ISERROR(PRODUCT(MATCH(IF(Range1="",""&COUNTBLANK(Range1),Range1 & COUNTIF(Range1,Range1)),IF(Range2="",""&COUNTBLANK(Range2),Range2& COUNTIF(Range2,Range2)),0))))  
        \============================================
        
        [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928127)
        
        *   ![](https://secure.gravatar.com/avatar/25a9730846fc4b01d9c7fcb5e99efcd5ad98d0bbbd1e122049dee411b37690d2?s=64&d=mm&r=g) cllach says:
            
            [March 11, 2015 at 2:40 pm](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928129)
            
            Think that works for unique or not, values, returns True if found same number of times, numeric or text and return False if ranges are diferent size. Easy to adapt to second problem.
            
            [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928129)
            
26.  ![](https://secure.gravatar.com/avatar/c90ca6d0f89a4a6deb2cd99343265649d582fb9e4528d2514435a773b7f24b21?s=64&d=mm&r=g) Lokesh says:
    
    [March 11, 2015 at 3:45 pm](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928170)
    
    For the main question.
    
    \=VLOOKUP(\[@\[Range 2\]\],Table1\[Range 1\],1,0)=\[@\[Range 2\]\]
    
    If all values are true than the values in both range match
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928170)
    
27.  ![](https://secure.gravatar.com/avatar/261be5464e1f906335ed499834f21899e20599489b1b600cb9b310a3d087bbb7?s=64&d=mm&r=g) [Vad](http://vppc.wordpress.com/)
     says:
    
    [March 11, 2015 at 5:34 pm](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928270)
    
    \=IFERROR(SUM(MATCH(C3:C7,E3:E7,0)),"No Match")  
    Array Formula
    
    I am expecting it work irrespective of number of items in both the lists,,
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928270)
    
28.  ![](https://secure.gravatar.com/avatar/e01e2c6ebc000b36efa6011b442f7f00f1d38cbfddcb0a95d0bb0a672444da13?s=64&d=mm&r=g) Nelson says:
    
    [March 11, 2015 at 6:00 pm](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928284)
    
    How about a simple:
    
    "=IF(NOT(ISERROR(VLOOKUP(C1,Range2,1,0))),"True","False")"
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928284)
    
29.  ![](https://secure.gravatar.com/avatar/c4c641038f0ff946745e3fb851c640ea875ed7f90723ef9a0af6818105920d74?s=64&d=mm&r=g) Fern says:
    
    [March 11, 2015 at 7:33 pm](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928352)
    
    Highlight the 2 ranges  
    Under Conditional Formatting, Select "Highlight Cell Rules", select "Duplicate Values"  
    The values that match in each range will be highlighted.
    
    You can also choose to highlight only Unique value in each range
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928352)
    
30.  ![](https://secure.gravatar.com/avatar/ad793f73a77e0640f8b1c9ec8bedadb989b1dcdb15e2c2034c0c65c3d9855048?s=64&d=mm&r=g) CraigM says:
    
    [March 12, 2015 at 12:01 am](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928514)
    
    use {=OR(Exact(A1,range2))}
    
    where:  
    the cells in range1 are A1 to A5  
    the cells in range2 are B1 to B5
    
    Enter the formula in cell C1. This will check to see if the value in A1 exists in range2. Copy down for the rest of the values.
    
    To check if each of the values in range1 exist in range2, use:  
    {=OR(Exact(B1,range1))} in D1 & then copy down for the rest.
    
    This is useful for lists that aren't too large. If they are, then resources/performance becomes an issue.
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928514)
    
31.  ![](https://secure.gravatar.com/avatar/85c32ec4d3dfbced8a4bdf79ed19679f4255a5bb56fd8bf2c9bd4539d1451122?s=64&d=mm&r=g) Dev says:
    
    [March 12, 2015 at 12:42 am](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928536)
    
    Use Conditional Formatting and use formula:  
    \=COUNTIF(A1,Range 2)=0 \[Colour Highlight Blue if not found\]  
    where A1 is the first cell in Range 1 i.e. ABC
    
    So, if ABC is not listed in Range 2, ABC will be highlighted in Blue
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928536)
    
32.  ![](https://secure.gravatar.com/avatar/250afddfe22885243d797cc10f9194ef2f8dbfcab4bba7714d0fa6360c7b10e7?s=64&d=mm&r=g) Bhavesh Soni says:
    
    [March 12, 2015 at 3:08 am](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928663)
    
    \=SUM(MATCH(RANGE1,RANGE1,0))=(SUM(MATCH(RANGE2,RANGE2,0)))  
    Enter this as array formula.
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928663)
    
33.  ![](https://secure.gravatar.com/avatar/6204fc9cd8e8aa51121b1b0a41c879b735394009642e7fb0e657d87ef5ac81b0?s=64&d=mm&r=g) shanmugam says:
    
    [March 12, 2015 at 3:50 am](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928711)
    
    Assumtion Range1 A1 to A6, Range 2 B1 to B6
    
    Answer  
    \=Vlookup(A2,$A$2:$A$6,2,0)
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928711)
    
34.  ![](https://secure.gravatar.com/avatar/58b001eca0431554f67348ec6c37b710b843fcee5ff2824993f6fe81ec131d4a?s=64&d=mm&r=g) Shaji says:
    
    [March 12, 2015 at 4:44 am](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928751)
    
    first one is so simple...  
    {=if(COUNTIF(Range1,Range2)=1,"True","false")}
    
    2nd one to find out...
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928751)
    
    *   ![](https://secure.gravatar.com/avatar/58b001eca0431554f67348ec6c37b710b843fcee5ff2824993f6fe81ec131d4a?s=64&d=mm&r=g) Shaji says:
        
        [March 12, 2015 at 10:17 am](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-929001)
        
        Sorry,  
        this one is correct for the first question...  
        {=SUM(COUNTIF(Range2,Range1))=ROWS(Range1)}
        
        [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-929001)
        
35.  ![](https://secure.gravatar.com/avatar/a66cc35c23f02aac1cd4f2bb067a6b533fc8b8232f4462feba18dca29e728ae4?s=64&d=mm&r=g) Aravind says:
    
    [March 12, 2015 at 5:01 am](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928765)
    
    Hai,Good Morning
    
    In the first one even though the values are same but the cells are different know so,I will make the criteria with cell numbers and find the answer
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928765)
    
36.  ![](https://secure.gravatar.com/avatar/bd344dfa84d32ae6cd63c29c6873b2af87481d11f4f767ebe9a686806f20645f?s=64&d=mm&r=g) [Ian](http://www.repxl.com/)
     says:
    
    [March 12, 2015 at 5:38 am](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928786)
    
    \=IF(IFERROR(MATCH(A1,B:B,0),0)=0,"No Match","Matched")
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928786)
    
37.  ![](https://secure.gravatar.com/avatar/0c46888cc0e25c78439081a1bad750cc7e24405972237e9685cdd262af521acc?s=64&d=mm&r=g) Anand says:
    
    [March 12, 2015 at 7:09 am](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928853)
    
    I simply use conditional formatting feature.
    
    Select both range and use conditional formatting to see duplicate/unique values.
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-928853)
    
38.  ![](https://secure.gravatar.com/avatar/c22a516b754f5c55085bb2a68810096d3836e7702db07b0b441fc39db8f3e950?s=64&d=mm&r=g) Belle-Isle says:
    
    [March 12, 2015 at 11:12 am](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-929025)
    
    For first problem :
    
    CSE : =AND(COUNT(Range1)=COUNT(Range2), COUNTIF(Range2, Range1)=1, COUNTIF(Range1, Range2)=1)
    
    This returns true in the wanted situation (identical arrays of unique values, whatever their order), but returns false if the arrays are of different sizes or if there are any duplicates in any one array. All in a single formula.
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-929025)
    
39.  ![](https://secure.gravatar.com/avatar/ed7ea023a22875fb13cd9e9af9861903508eee3d29f79bd1ddb20ee9e605f2f5?s=64&d=mm&r=g) Abhijeet says:
    
    [March 12, 2015 at 12:13 pm](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-929050)
    
    My source data: A3:A7  
    Target Ranges: C3:F7  
    Select Target Range and use conditional formatting formula "=COUNTIF($A$3:$A$7,C3)" with some colour to highlight cells matching criteria. If all cells in a column are colored, it's a match target range.
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-929050)
    
40.  ![](https://secure.gravatar.com/avatar/8b875c9820cb7b0be4f327283b40e70cf5d3cfcb0e612d17996ef90694e81067?s=64&d=mm&r=g) DJP says:
    
    [March 12, 2015 at 3:32 pm](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-929126)
    
    Good morning / Good afternoon,
    
    May I suggest this formula:  
    SUM(--(Range1=TRANSPOSE(Range2)))=COUNTA(Range1)  
    As an array formula, Ctrl+Shift+Enter is required
    
    For Frenchies, it gives:  
    SOMME(--(Range1=TRANSPOSE(Range2)))=NBVAL(Range1)  
    Ctrl+Shift+Enter needed too 😉
    
    Cheers
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-929126)
    
41.  ![](https://secure.gravatar.com/avatar/90d6e5a60dc393ba190b6fec95456b4f5bc058ee95919583b8fed4e65c32043c?s=64&d=mm&r=g) sam says:
    
    [March 12, 2015 at 3:48 pm](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-929144)
    
    Problem 1  
    \=AND(COUNTIF(Rng1,Rng2))  
    Array Entered  
    True if both are the same, False if they are different
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-929144)
    
42.  ![](https://secure.gravatar.com/avatar/4eb1537713ee7374222451ef268b4dc3a324f11fab9e03ed6fbb7086063051b9?s=64&d=mm&r=g) Jorge Eduardo (brazil) says:
    
    [March 12, 2015 at 7:45 pm](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-929276)
    
    \=contREP(O3:S7;H3:L17)  
    vai informar a quantidade de valores repetidos entre 2 range
    
    funciona para mim e uso muito dentro de macros
    
    Dim reg1() As Variant, reg2() As Variant, ttl As Long  
    Dim lc1 As Long, cc1 As Long, lc2 As Long, cc2 As Long
    
    Function ContREP(ByVal rag1 As Range, ByVal rag2 As Range) As Long
    
    ttl = 0  
    reg1 = rag1.Value2  
    reg2 = rag2.Value2  
    lc1 = UBound(reg1, 1)  
    cc1 = UBound(reg1, 2)  
    lc2 = UBound(reg2, 1)  
    cc2 = UBound(reg2, 2)
    
    For l1 = 1 To lc1  
    For c1 = 1 To cc1  
    If reg1(l1, c1) "" Then GoSub lk  
    Next  
    Next  
    ContREP = ttl  
    Exit Function  
    lk:  
    For l2 = 1 To lc2  
    For c2 = 1 To cc2  
    If reg1(l1, c1) = reg2(l2, c2) Then ttl = ttl + 1: Return  
    Next  
    Next  
    Return
    
    End Function
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-929276)
    
    *   ![](https://secure.gravatar.com/avatar/4eb1537713ee7374222451ef268b4dc3a324f11fab9e03ed6fbb7086063051b9?s=64&d=mm&r=g) Jorge Eduardo (brazil) says:
        
        [March 12, 2015 at 8:28 pm](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-929298)
        
        [https://www.sendspace.com/file/fsr0k5](https://www.sendspace.com/file/fsr0k5)
          
        planilha com a função aplicada
        
        [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-929298)
        
43.  ![](https://secure.gravatar.com/avatar/b474635bede0a7762c762ac11c9f1feb23856ac452225cdefc465a04165ad051?s=64&d=mm&r=g) [Abbott Katz](http://www.spreadsheetjournalism.com/)
     says:
    
    [March 12, 2015 at 10:39 pm](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-929359)
    
    Assuming the two ranges are in B8:B12 and C8:C12 respectively:
    
    {=IF(ISNA(SUM(MATCH(B8:B12,C8:C12,0))),"Incomplete match","Complete match")}
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-929359)
    
44.  ![](https://secure.gravatar.com/avatar/4dc639faaf6e67531cbb830d58ec2858c1e27bb6551e34c6234661e1b7165a57?s=64&d=mm&r=g) QL says:
    
    [March 13, 2015 at 7:04 am](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-929617)
    
    My approach to the first question:
    
    Assume range\_1 and range\_2 are arranged as vertical column range with same size, and there might be duplicate values in the range.
    
    The array formula  
    \=SUM(--(MMULT(--(TRANSPOSE(Range\_1)=Range\_1),--(ROW(Range\_1)=ROW(Range\_1)))=MMULT(--(TRANSPOSE(Range\_1)=Range\_2),--(ROW(Range\_1)=ROW(Range\_1))))) = ROWS(Range\_1)
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-929617)
    
45.  ![](https://secure.gravatar.com/avatar/be6c8d5ac992e887333dad6d2cd61f56667eaad08e4faa71e92d7b5fdd4861d7?s=64&d=mm&r=g) Katie Grimes says:
    
    [March 13, 2015 at 1:34 pm](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-929848)
    
    Assuming the two ranges are in A2:A6 and B2:B6, I created a row beneath the two ranges to tell me how many values are MISSING from Range 1 in Range 2 and vice versa. If they are a perfect match, there would be 0 missing values in each column. (I decided to do missing values instead of matching values so that I wouldn't have to know HOW MANY values were in the range to begin with.)
    
    My array formula for A7 = SUM(IF(ISNA(MATCH(A2:A6, B2:B6, 0)), 1, 0)), Ctrl + Shift + Enter. This would give 0 if every value in Range 1 could be found in Range 2.
    
    Similarly, for B7 = SUM(IF(ISNA(MATCH(B2:B6, A2:A6, 0)), 1, 0)). If both A7 and B7 = 0, then you have a perfect match.
    
    In addition, I wanted to be able to tell which values WERE missing if they did not match perfectly. So I created a conditional formatting in cells A2:A6 using the formula = ISNA(MATCH(A2, $B$2:$B$6,0)). This would highlight any cells in Range 1 that could not be found in Range 2. I then repeated the formatting for B2:B6 using the formula condition = ISNA(MATCH(B2, $A$2:$A$6, 0)).
    
    For question 2:
    
    Assume the Source Range is in K3:K7, and the Target Table has headers in M2:R2, and the data is in M3:R7.
    
    Beneath each of the ranges in the Target table, I inserted a row with the same array formula used above to compare it to the Source Range:  
    M8 = SUM(IF(ISNA(MATCH(M3:M7, $K$3:$K$7, 0)), 1, 0)), Ctrl + Shift + Enter.  
    N8 = SUM(IF(ISNA(MATCH(N3:N7, $K$3:$K$7, 0)), 1, 0)), Ctrl + Shift + Enter.  
    O8 = SUM(IF(ISNA(MATCH(O3:O7, $K$3:$K$7, 0)), 1, 0)), Ctrl + Shift + Enter.  
    P8 = SUM(IF(ISNA(MATCH(P3:P7, $K$3:$K$7, 0)), 1, 0)), Ctrl + Shift + Enter.  
    Q8 = SUM(IF(ISNA(MATCH(Q3:Q7, $K$3:$K$7, 0)), 1, 0)), Ctrl + Shift + Enter.  
    R8 = SUM(IF(ISNA(MATCH(R3:R7, $K$3:$K$7, 0)), 1, 0)), Ctrl + Shift + Enter.
    
    Then, in cell K10 (where I wanted to pull the Range that matched, i.e. where I wanted my answer to appear), I used a Match formula to find the range with 0 missing values.
    
    K10 = MATCH(0, M8:R8, 0). This returned 2, our given range.
    
    I also decided that I wanted to be able to return the Range Name, even if it wasn't 1-6. Changing Range 2 to be called "Apple" (no reason, just the word I picked), in cell K11, I used an Index-Match formula.
    
    K11 = INDEX(M2:R2, ,MATCH(0,M8:R8,0)) This then returned "Apple" instead of "2".
    
    The only thing I realize now as I am typing this is that I didn't do a back check: I didn't check that the Source range had all the values in the Target Range 2. Given they had the same number of values, this isn't a big deal, but ideally, I would have added that as well.
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-929848)
    
46.  ![](https://secure.gravatar.com/avatar/955f35dd7b87da5636855ca6ae837ac6ca16cff8a7f016554514f8a09ab2e72b?s=64&d=mm&r=g) David says:
    
    [March 13, 2015 at 2:21 pm](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-929870)
    
    Problem 1:  
    {=AND(COUNTIF(RANGE1,RANGE2)\*COUNTIF(RANGE2,RANGE1))}
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-929870)
    
47.  ![](https://secure.gravatar.com/avatar/2f4e95a68e884deb9d0a72c72c2805aa72bbf22247d7cfaf544ebb3bdcae4402?s=64&d=mm&r=g) Alex Groberman says:
    
    [March 13, 2015 at 10:09 pm](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-930112)
    
    If there can be duplicate values and/or a different number of rows in each set:
    
    {=IFERROR(AND(SMALL(MATCH(range1,range2,0),ROW(INDIRECT("1:"&ROWS(range1))))=ROW(INDIRECT("1:"&ROWS(range2)))),FALSE)}
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-930112)
    
48.  ![](https://secure.gravatar.com/avatar/f0fd57995198e15c5c7ab417a80eca763c287c5743605e2bbb74cc4b9ca89d6b?s=64&d=mm&r=g) [Ramakrishnan C](http://ie/)
     says:
    
    [March 16, 2015 at 2:22 am](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-931268)
    
    Hi sir,  
    for Q1  
    two option I tried correct me if I am wrong  
    a) conditional formatting- cell value(range 1) (giving colour) stop if true  
    b) match function - by which range1 order is matched with range 2  
    showing a result like  
    Rang1 Range2 Order  
    ABC ABC 1  
    DEF GHI 3  
    GHI MNO 5  
    JKL JKL 4  
    MNO DEF 2
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-931268)
    
49.  ![](https://secure.gravatar.com/avatar/15d97c9f955b75ede2d20a543037e2b62191749c7d380bfef36ad51ef30c32d1?s=64&d=mm&r=g) Neil says:
    
    [March 16, 2015 at 5:01 pm](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-931618)
    
    For question two here is my starter for ten that has not been tidied up but should provide some food for thought:
    
    CSE enter:  
    {=MATCH(MAX(MMULT(COUNTIF(CHK\_RNG,TRANSPOSE(CHOOSE(COLUMN(A1:F1),TEST1,TEST2,TEST3,TEST4,TEST5,TEST6))),ROW(A1:A5)^0)),  
    MMULT(COUNTIF(CHK\_RNG,TRANSPOSE(CHOOSE(COLUMN(A1:F1),TEST1,TEST2,TEST3,TEST4,TEST5,TEST6))),ROW(A1:A5)^0),0)}
    
    I set up a range called CHK\_RNG in cells B4:B8 for the data to be checked against. And six ranges for the guesses called TEST1 (D4:D8), TEST2 (E4:E8), ...TEST6 (I4:I8)
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-931618)
    
50.  ![](https://secure.gravatar.com/avatar/7301d599671545ca183da76efe0e3153ea1a6f073471883c1671e019774720ef?s=64&d=mm&r=g) Micah Dail says:
    
    [March 17, 2015 at 10:26 pm](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-932644)
    
    First problem is pretty straighforward.
    
    {=AND(ISNUMBER(MATCH(range1, range2, 0)))}
    
    Second one is rather tricky. Haven't figured it out yet.
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-932644)
    
51.  ![](https://secure.gravatar.com/avatar/882b0f3216239e25bb7bde4bc90c4415e65aa7133fd21fb5c9de557af8cf77d1?s=64&d=mm&r=g) [parveen](http://none/)
     says:
    
    [March 19, 2015 at 9:48 pm](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-934437)
    
    Hello Chandoo,  
    As per me exact function should be used.
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-934437)
    
52.  ![](https://secure.gravatar.com/avatar/6541252afc5ad0cff6ea6b7cd863fd627ba35812181fc7a14376465777b5a629?s=64&d=mm&r=g) Ale says:
    
    [March 27, 2015 at 4:12 pm](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-940640)
    
    My solution to the first question:
    
    \=AND(MATCH(INDEX(Range1,1),Range2,0),MATCH(INDEX(Range1,2),Range2,0),MATCH(INDEX(Range1,3),Range2,0),MATCH(INDEX(Range1,4),Range2,0),MATCH(INDEX(Range1,5),Range2,0))
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-940640)
    
53.  ![](https://secure.gravatar.com/avatar/6541252afc5ad0cff6ea6b7cd863fd627ba35812181fc7a14376465777b5a629?s=64&d=mm&r=g) Ale says:
    
    [April 1, 2015 at 3:33 pm](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-944043)
    
    And this is my solution for the bonus question:
    
    IF(NOT(ISERROR(AND(MATCH(INDEX(Source,1),Target1,0),MATCH(INDEX(Source,2),Target1,0),MATCH(INDEX(Source,3),Target1,0),MATCH(INDEX(Source,4),Target1,0),MATCH(INDEX(Source,5),Target1,0)))),D15,IF(NOT(ISERROR(AND(MATCH(INDEX(Source,1),Target2,0),MATCH(INDEX(Source,2),Target2,0),MATCH(INDEX(Source,3),Target2,0),MATCH(INDEX(Source,4),Target2,0),MATCH(INDEX(Source,5),Target2,0)))),E15,IF(NOT(ISERROR(AND(MATCH(INDEX(Source,1),Target3,0),MATCH(INDEX(Source,2),Target3,0),MATCH(INDEX(Source,3),Target3,0),MATCH(INDEX(Source,4),Target3,0),MATCH(INDEX(Source,5),Target3,0)))),F15,IF(NOT(ISERROR(AND(MATCH(INDEX(Source,1),Target4,0),MATCH(INDEX(Source,2),Target4,0),MATCH(INDEX(Source,3),Target4,0),MATCH(INDEX(Source,4),Target4,0),MATCH(INDEX(Source,5),Target4,0)))),G15,IF(NOT(ISERROR(AND(MATCH(INDEX(Source,1),Target5,0),MATCH(INDEX(Source,2),Target5,0),MATCH(INDEX(Source,3),Target5,0),MATCH(INDEX(Source,4),Target5,0),MATCH(INDEX(Source,5),Target5,0)))),H15,IF(NOT(ISERROR(AND(MATCH(INDEX(Source,1),Target6,0),MATCH(INDEX(Source,2),Target6,0),MATCH(INDEX(Source,3),Target6,0),MATCH(INDEX(Source,4),Target6,0),MATCH(INDEX(Source,5),Target6,0)))),I15,"no match"))))))
    
    Tip: any idea on how to make it shorter?
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-944043)
    
54.  ![](https://secure.gravatar.com/avatar/af327b45480d0b0df193c12b96d9f01f48f1cd020c8e8411f4383a10ec06ab6b?s=64&d=mm&r=g) Eric Lind says:
    
    [April 30, 2015 at 10:01 pm](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-962765)
    
    Count if makes the most sense to me.
    
    The basic formula would be:
    
    \=COUNTIF(Range2,A2)
    
    which is nice because you can count how many instances of a value in the range.
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-962765)
    
55.  ![](https://secure.gravatar.com/avatar/8f7cb591de843062c02cda7a04c91cd3ca032153523410c9e54ce37a5f3a8841?s=64&d=mm&r=g) [Ryan Wells](http://wellsr.com/vba/)
     says:
    
    [May 14, 2015 at 11:25 pm](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-973873)
    
    I know you can do this with formulae, but I'm partial to VBA. Since I have to compare strings regularly for nuclear engineering design verification, I created a VBA code that doesn't stop at simply comparing the ranges. It will tell you where in Range 2 the value in Range 1 appears and it will highlight the cells not found in both ranges. If you're interested: [http://wellsr.com/vba/2015/excel/examples/excel-compare-two-columns-for-differences/](http://wellsr.com/vba/2015/excel/examples/excel-compare-two-columns-for-differences/)
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-973873)
    
56.  ![](https://secure.gravatar.com/avatar/07bbb9ac7e9b81366af3a34fce256be1d7454ad3ac7ecdc938bb84e6e372277f?s=64&d=mm&r=g) Ramesh Deo says:
    
    [June 22, 2015 at 8:46 pm](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-998672)
    
    (=OR(range1=range2)}
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-998672)
    
57.  ![](https://secure.gravatar.com/avatar/07bbb9ac7e9b81366af3a34fce256be1d7454ad3ac7ecdc938bb84e6e372277f?s=64&d=mm&r=g) Ramesh Deo says:
    
    [June 22, 2015 at 8:49 pm](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-998673)
    
    {=OR(range1=range2)}
    
    [Reply](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#comment-998673)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/check-if-2-ranges-have-same-values-set-equality-problem/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Celebrate Holi with this colorful Excel file](https://chandoo.org/wp/celebrate-holi-with-this-colorful-excel-file/) | [Share your favorite Excel tip & you could win Beats Headphones \[Podcast Anniversary Celebrations\]](https://chandoo.org/wp/podcast-first-anniversary-contest/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)