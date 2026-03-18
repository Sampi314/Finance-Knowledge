# Extract the 10 digit number [formula homework] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/extract-the-10-digit-number-formula-homework

---

Extract the 10 digit number \[formula homework\]
================================================

[Excel Challenges](https://chandoo.org/wp/category/excel-challenges/)
 - 106 comments

  

Okay, time for another challenge.

Imagine you have some data like this. Each cell contains 3 numbers separated by line break  – CHAR(10) and you need to extract the number that is 10 digits long.

![extract-10-digits](https://chandoo.org/wp/wp-content/uploads/2016/05/extract-10-digits.png)

Go ahead and solve this riddle.

**[Click here to download sample data workbook](https://chandoo.org/wp/wp-content/uploads/2016/05/extract-10-digit-data.xlsx)
.**

Post your answers in comments. Although the title says _formula homework_ you are welcome to post VBA, Power Query and RegEx (thru VBA) solutions too.

**Want to extract more?**

If you derive pleasure extracting good data from junk, you are going to love below challenges.

*   [Extract numbers from text](http://chandoo.org/wp/2015/10/30/extract-numbers-from-text-hw/)
    
*   [Extract first & last names from email addresses](http://chandoo.org/wp/2014/02/27/extract-first-name-last-name-from-email/)
    
*   [Extract file name from full path](http://chandoo.org/wp/2012/10/23/extract-file-name-from-full-path-using-formulas/)
    
*   [Extract dates from text](http://chandoo.org/wp/2012/08/17/extract-dates-from-text/)
    
*   [Extract hourly rate by looking up a pattern](http://chandoo.org/wp/2012/12/14/find-text-pattern/)
    

A note: These challenges are very interesting and can take up a lot of your time (thus make you a whole lot smarter).

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
| Written by Chandoo  <br>Tags: [array formulas](https://chandoo.org/wp/tag/array-formulas/)<br>, [homework](https://chandoo.org/wp/tag/homework/)<br>, [Learn Excel](https://chandoo.org/wp/tag/excel/)<br>, [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)<br>, [text processing](https://chandoo.org/wp/tag/text-processing/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 106 Responses to “Extract the 10 digit number \[formula homework\]”

1.  ![](https://secure.gravatar.com/avatar/028d37308327c214a626cd36939a66ce94ee7410dde285bd46f6a22b08102ce6?s=64&d=mm&r=g) Abhay says:
    
    [May 6, 2016 at 8:38 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181009)
    
    Power Query Script
    
    let  
    Source = Excel.CurrentWorkbook(){\[Name="Table1"\]}\[Content\],  
    Replaced\_Carraige = Table.ReplaceValue(Source,"#(lf)","|",Replacer.ReplaceText,{"Data"}),  
    Split\_Column = Table.SplitColumn(Replaced\_Carraige,"Data",Splitter.SplitTextByDelimiter("|", QuoteStyle.Csv),{"Data.1", "Data.2", "Data.3"}),  
    Final\_Column\_Added = Table.AddColumn(Split\_Column, "Length", each if Text.Length(\[Data.1\]) >= 10 then \[Data.1\]  
    else if Text.Length(\[Data.2\]) >= 10 then \[Data.2\]  
    else if Text.Length(\[Data.3\]) >= 10 then \[Data.3\]  
    else "NA")  
    in  
    Final\_Column\_Added
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181009)
    
    *   ![](https://secure.gravatar.com/avatar/028d37308327c214a626cd36939a66ce94ee7410dde285bd46f6a22b08102ce6?s=64&d=mm&r=g) Abhay says:
        
        [May 6, 2016 at 8:41 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181012)
        
        Step 1 - Replace Value "#(If)" with "|"  
        Step 2 - Split columns by "|"  
        Step 3 - Add column with IF function in power query identifying column with 10 digits and taking first column having 10 digits as result.
        
        [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181012)
        
    *   ![](https://secure.gravatar.com/avatar/d8824c8a465b5cda167c467729811719ba92c9767744642abd5f1a70f307ee6a?s=64&d=mm&r=g) PL Chan says:
        
        [May 7, 2016 at 2:18 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181470)
        
        \=RIGHT(SUBSTITUTE(B3,CHAR(10),""),10)\*1
        
        [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181470)
        
        *   ![](https://secure.gravatar.com/avatar/d8824c8a465b5cda167c467729811719ba92c9767744642abd5f1a70f307ee6a?s=64&d=mm&r=g) PL Chan says:
            
            [May 7, 2016 at 2:31 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181475)
            
            Oops, the first formula is wrong as I have make the wrong assumption.  
            Below is the modified formula to pull the 10 digits whether is the 1st row, 2nd row or the 3rd row.
            
            \=IF(FIND(CHAR(10),B3)=11,LEFT(B3,10),IF(FIND(CHAR(10),B3,FIND(CHAR(10),B3)+1)-FIND(CHAR(10),B3)<10,RIGHT(B3,10),MID(B3,FIND(CHAR(10),B3)+1,10)))
            
            [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181475)
            
    *   ![](https://secure.gravatar.com/avatar/6a70435d993cc4f41eceb077e0eed46211a34d27717315d1406920ef3ff9fada?s=64&d=mm&r=g) Donald Parish says:
        
        [May 7, 2016 at 1:19 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181721)
        
        Newer version of Power Query can split by Special Characters including Line feeds. See my post from 5/7/2016.
        
        [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181721)
        
2.  ![](https://secure.gravatar.com/avatar/3e70a753ed9ed4f312b1d3f707d2d0e71efe19e75770c1e61fb03e4250d2f0e5?s=64&d=mm&r=g) Jorge says:
    
    [May 6, 2016 at 9:18 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181036)
    
    \=IF(FIND(CHAR(10);B3)-1=10;LEFT(B3;10);IF(FIND(CHAR(10);B3;FIND(CHAR(10);B3)+1)-FIND(CHAR(10);B3)-1=10;MID(B3;FIND(CHAR(10);B3)+1;10);RIGHT(B3;10)))
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181036)
    
3.  ![](https://secure.gravatar.com/avatar/e55fa99e494443221e7bc9e481b4a9d4f5de82c81feb3ec9b4c94f1798c15d11?s=64&d=mm&r=g) Worm says:
    
    [May 6, 2016 at 9:45 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181055)
    
    Not exactly neat, wouldn't scale, and there's no example with the ten digit number first, but it seems to work 🙂
    
    \=IF(FIND(CHAR(10),B3)=10,LEFT(B3,10),IF((FIND(CHAR(10),B3,FIND(CHAR(10),B3)+1)-FIND(CHAR(10),B3))=11,MID(B3,FIND(CHAR(10),B3)+1,10),RIGHT(B3,10)))
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181055)
    
    *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
        
        [May 6, 2016 at 11:55 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181103)
        
        @Worm,  
        I'm sure you meant: =IF(FIND(CHAR(10),B3)=10,LEFT(...
        
        [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181103)
        
        *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
            
            [May 6, 2016 at 11:56 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181104)
            
            Ooooopsssss,  
            Just saw the length correction...
            
            [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181104)
            
4.  ![](https://secure.gravatar.com/avatar/aa7e3254f7dfc4575583b9793f4896f20efb5f9726e93b57a1d8e8a65dec6b92?s=64&d=mm&r=g) [Vaibhav](http://excelvbalab.com/)
     says:
    
    [May 6, 2016 at 10:04 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181066)
    
    If data is in cell A1 then use =IF(FIND(CHAR(10),A1)=11,LEFT(A1,10),IF(FIND(CHAR(10),A1,FIND(CHAR(10),A1)+1)-FIND(CHAR(10),A1)=11,MID(A1:A1,FIND(CHAR(10),A1)+1,10),RIGHT(A1,10)))
    
    Cheers!!
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181066)
    
    *   ![](https://secure.gravatar.com/avatar/e55fa99e494443221e7bc9e481b4a9d4f5de82c81feb3ec9b4c94f1798c15d11?s=64&d=mm&r=g) Worm says:
        
        [May 6, 2016 at 10:10 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181069)
        
        Same answer, but at least you got the first length right, unlike me 🙂
        
        [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181069)
        
    *   ![](https://secure.gravatar.com/avatar/28e5cabdf461d20ff045b3300404e8e5bf0402780db0d3dc548eb10444ca4952?s=64&d=mm&r=g) Vasanth says:
        
        [June 10, 2019 at 6:27 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1656230)
        
        WOW.............!!!! Lovely Bro, Love You 🙂
        
        [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1656230)
        
5.  ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
    
    [May 6, 2016 at 10:05 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181067)
    
    User Defined Function (UDF)  
    \-----------------------------------------------------  
    Function Extract\_10(Str As String)  
    Arr = Split(Str, Chr(10))  
    For CL = 0 To UBound(Arr)  
    If Len(Arr(CL)) = 10 Then Extract\_10 = Arr(CL)  
    Next  
    End Function  
    \-------------------  
    In cell C3 type: =Extract\_10(B3) and copy down.  
    \=========================  
    Michael Avidan  
    ISRAEL
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181067)
    
    *   ![](https://secure.gravatar.com/avatar/ab9407ca70da02336509af28b16347f83c70c8e3c593fcf02656a5362759ec5a?s=64&d=mm&r=g) Calvin says:
        
        [May 6, 2016 at 4:30 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181272)
        
        HI Micky,
        
        it is giving me #Name? error
        
        [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181272)
        
    *   ![](https://secure.gravatar.com/avatar/7172db04de729c130c11ae51bd08f28faea7ec5cfd74ffe8368e7b96fa34ffe3?s=64&d=mm&r=g) Denys Calvin says:
        
        [May 8, 2016 at 1:45 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1182318)
        
        This is genius! And easily generalized to extract a substring of length N (assuming there is only one) set off by a particular non-numeric separator character. Hat's off to you!
        
        [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1182318)
        
    *   ![](https://secure.gravatar.com/avatar/616e79633c417a50d356e09298f5f31106f0a916c43eb33ed73360cd52b9f636?s=64&d=mm&r=g) hbillions says:
        
        [May 8, 2016 at 3:26 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1183123)
        
        Hello Micky,
        
        I like your solution. Was wondering if it can be modified to target any 10 character starting with first 3 characters being one of 20 specific 3-characters i.e. I want any 10-character number but starting with any of the following 802,803,805,806,808,809,810 then 702,703,705...and 902,903,905...910.
        
        Thank you.
        
        [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1183123)
        
        *   ![](https://secure.gravatar.com/avatar/aa7e3254f7dfc4575583b9793f4896f20efb5f9726e93b57a1d8e8a65dec6b92?s=64&d=mm&r=g) [Vaibhav](http://excelvbalab.com/)
             says:
            
            [May 10, 2016 at 9:10 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1184751)
            
            @hbillions you can try below UDF:
            
            Function Extract\_10(Str As String, rng As Range)  
            Dim c As Range  
            Arr = Split(Str, Chr(10))
            
            For CL = 0 To UBound(Arr)  
            If Len(Arr(CL)) = 10 Then
            
            For Each c In rng  
            If c.Value "" Then  
            If Val(Left(Arr(CL), Len(c.Value))) = c.Value Then  
            Extract\_10 = Arr(CL)  
            Exit Function  
            End If  
            End If  
            Next c
            
            End If  
            Next  
            End Function
            
            syntax is
            
            \=Extract\_10(B3, E1:E10)
            
            here b3 contains value & E1 to E10 contains criterion for which you want to match conditions like 802,803,805,806,808,809,810 then 702,703,705...and 902,903,905...910
            
            Cheers!!
            
            [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1184751)
            
6.  ![](https://secure.gravatar.com/avatar/aa7e3254f7dfc4575583b9793f4896f20efb5f9726e93b57a1d8e8a65dec6b92?s=64&d=mm&r=g) [Vaibhav](http://excelvbalab.com/)
     says:
    
    [May 6, 2016 at 10:21 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181077)
    
    The most complicated one, if value in cell A1:
    
    \=LOOKUP(10,LEN(TRIM(MID(SUBSTITUTE(A1,CHAR(10),REPT(" ",99)),(ROW(OFFSET($A$1,,,LEN(A1)-LEN(SUBSTITUTE(A1,CHAR(10),""))+1))-1)\*99+((ROW(OFFSET($A$1,,,LEN(A1)-LEN(SUBSTITUTE(A1,CHAR(10),""))+1)))=1),99))),TRIM(MID(SUBSTITUTE(A1,CHAR(10),REPT(" ",99)),(ROW(OFFSET($A$1,,,LEN(A1)-LEN(SUBSTITUTE(A1,CHAR(10),""))+1))-1)\*99+((ROW(OFFSET($A$1,,,LEN(A1)-LEN(SUBSTITUTE(A1,CHAR(10),""))+1)))=1),99)))
    
    Cheers!!
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181077)
    
7.  ![](https://secure.gravatar.com/avatar/aa7e3254f7dfc4575583b9793f4896f20efb5f9726e93b57a1d8e8a65dec6b92?s=64&d=mm&r=g) [Vaibhav](http://excelvbalab.com/)
     says:
    
    [May 6, 2016 at 10:49 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181086)
    
    Last one from my side (probably :p), its lesser complex than last one by me
    
    \=LOOKUP(10,LEN(TRIM(MID(SUBSTITUTE(CHAR(10)&A1,CHAR(10),REPT(" ",255)),{1,2,3}\*255,255))),TRIM(MID(SUBSTITUTE(CHAR(10)&A1,CHAR(10),REPT(" ",255)),{1,2,3}\*255,255)))
    
    Cheers!!
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181086)
    
    *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
        
        [May 6, 2016 at 11:09 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181092)
        
        @Vaibhav  
        Check:  
        1234568790  
        299004  
        99004
        
        [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181092)
        
        *   ![](https://secure.gravatar.com/avatar/aa7e3254f7dfc4575583b9793f4896f20efb5f9726e93b57a1d8e8a65dec6b92?s=64&d=mm&r=g) [Vaibhav](http://excelvbalab.com/)
             says:
            
            [May 6, 2016 at 11:48 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181101)
            
            My bad, i did not check for exception.
            
            [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181101)
            
            *   ![](https://secure.gravatar.com/avatar/aa7e3254f7dfc4575583b9793f4896f20efb5f9726e93b57a1d8e8a65dec6b92?s=64&d=mm&r=g) [Vaibhav](http://excelvbalab.com/)
                 says:
                
                [May 6, 2016 at 11:53 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181102)
                
                This one is updated
                
                \=INDEX(TRIM(MID(SUBSTITUTE(CHAR(10)&$A7,CHAR(10),REPT(" ",255)),{1,2,3}\*255,255)),1,MATCH(10,LEN(TRIM(MID(SUBSTITUTE(CHAR(10)&A7,CHAR(10),REPT(" ",255)),{1,2,3}\*255,255))),0))
                
                Cheers!!
                
                [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181102)
                
8.  ![](https://secure.gravatar.com/avatar/9c8add29f4aa9c7adf28f9e766cb0109f2bc4411de38a4b8c85626dab9a791ca?s=64&d=mm&r=g) Rudra Sharma says:
    
    [May 6, 2016 at 11:38 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181098)
    
    First of all I split the data into three columns with the help of Text To Columns tool. My delimiter was char(10) or Ctrl + J. Then in another column I used formula as
    
    \=IF(LEN(D3)=10,D3,IF(LEN(E3)=10,E3,F3))
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181098)
    
    *   ![](https://secure.gravatar.com/avatar/4f5ac4884ef996471c99a034bbfa3f3bf9e8355f0ec7bb5024b0935d58256242?s=64&d=mm&r=g) Jeff S says:
        
        [May 6, 2016 at 4:39 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181276)
        
        I like your approach - much easier to debug and to understand months later. Even if the situation called for a single formula solution, this is a good way to get a known good result for validation.
        
        [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181276)
        
    *   ![](https://secure.gravatar.com/avatar/ca996958df7184f43221f7b0b9ae97e0bb03268442b303bf1306f5701d1017cd?s=64&d=mm&r=g) PJ says:
        
        [May 6, 2016 at 5:07 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181290)
        
        Hi Rudra,
        
        Text to Columns only has Tab, Semicolon, Comma, Space, Other (which supports only one character). How you split the data?
        
        Thanks in advance for sharing..
        
        [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181290)
        
        *   ![](https://secure.gravatar.com/avatar/9c8add29f4aa9c7adf28f9e766cb0109f2bc4411de38a4b8c85626dab9a791ca?s=64&d=mm&r=g) Rudra Sharma says:
            
            [May 11, 2016 at 6:52 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1185642)
            
            Hey PJ  
            Hadn't expected that my comment will get a reply.
            
            Once you clicked on 'Other Character' box, hit Ctrl + J, it forces excel to use char(10) as delimiter. I learned this trick in Chandoo's forum only but don't have the link. Thanks.
            
            [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1185642)
            
    *   ![](https://secure.gravatar.com/avatar/a99fde22ba553e95374b55cf95b4330a73402730a0061854eac75bb90c31242d?s=64&d=mm&r=g) Chandra Mohan says:
        
        [July 4, 2016 at 11:32 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1226277)
        
        I suggest this formula after splitting column =LOOKUP(10,LEN(D2:F2),D2:F2)
        
        [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1226277)
        
9.  ![](https://secure.gravatar.com/avatar/d1c5834140d6e6cb54eddbf0d261c8e1d6c1a6d2da686158c3f97de7c66e5aa5?s=64&d=mm&r=g) [Kapil Marwaha](https://www.truedata.in/)
     says:
    
    [May 6, 2016 at 12:32 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181148)
    
    Ok, I have the correct answer and it works for 10 digits in all lines;-
    
    \=IF((FIND(CHAR(10),B3)-1)=10,LEFT(B3,10),IF(FIND(CHAR(10),B3,(FIND(CHAR(10),B3)+1))-(FIND(CHAR(10),B3)+1)=10,MID(B3,FIND(CHAR(10),B3)+1,10),RIGHT(B3,10)))
    
    Thank you Chandoo for this lovely homework !! I just love this.
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181148)
    
10.  ![](https://secure.gravatar.com/avatar/460be5157a8ff55b9ffdf755dce4658a7d42130b5bda58c43f07368eb6088d00?s=64&d=mm&r=g) Daniel H says:
    
    [May 6, 2016 at 12:35 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181153)
    
    Very short, but limited to the sample:
    
    \=MID(B3,IF(FIND(CHAR(10),B3,8)=18,8,14),10)
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181153)
    
    *   ![](https://secure.gravatar.com/avatar/4dd750916a9ada60351e061eb94759569e284a134136746007641b1d84bb5e6c?s=64&d=mm&r=g) [XLarium](https://plus.google.com/b/111273925303719415801/)
         says:
        
        [May 6, 2016 at 2:07 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181219)
        
        Hello Daniel, your solution gives #VALUE! if then 10 digit number is the first number.  
        My solution is:  
        \=MID(B3,SEARCH(CHAR(10)&"??????????"&CHAR(10),CHAR(10)&B3&CHAR(10)),10)
        
        [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181219)
        
        *   ![](https://secure.gravatar.com/avatar/aee5f5b568c6f3d309e4d5d53b9a98535fd42577d69f12c7476579f35d62842a?s=64&d=mm&r=g) David N says:
            
            [May 11, 2016 at 6:58 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1186181)
            
            This MID-SEARCH approach works with the seeming consistency of the sample values but could fail if the two shorter numbers are ever consecutive with a total of nine digits because the ? wildcard would match the CHAR(10) in between them as a valid tenth character. For example, the following input would give 223923908 as a result.
            
            2239  
            23908  
            1518028737
            
            [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1186181)
            
11.  ![](https://secure.gravatar.com/avatar/7c2af25faf15519b3499790815be8053c20fec771e60cadc30865b94a37b150c?s=64&d=mm&r=g) [Andres Rojas Moncada (Excel Hecho Facil)](http://excelhechofacil.blogspot.com.co/)
     says:
    
    [May 6, 2016 at 1:23 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181188)
    
    La función de Michael (Micky) Avidan utilizando "the function Split in VBA" es una salida fenomenal...
    
    Yo realicé una mucho más larga "very large"
    
    Aquí esta:
    
    Public Function Extrae10Caracteres(Celda As Range) As Long  
    If Celda.Count = 1 Then  
    Dim Texto As String, Caracter10 As String  
    Dim LargoTexto As Long, ValorCaracter As Long  
    Dim i As Long
    
    Texto = VBA.CStr(Celda.Value)  
    LargoTexto = VBA.Len(Texto)
    
    For i = 1 To LargoTexto  
    ValorCaracter = VBA.Asc(VBA.Mid(Texto, i, 1))  
    If (ValorCaracter = 10) And (VBA.Len(Caracter10) < 10) Then  
    Caracter10 = Empty  
    End If
    
    If (ValorCaracter 10) And (VBA.Len(Caracter10) < 10) Then  
    Caracter10 = Caracter10 & VBA.Mid(Texto, i, 1)  
    End If  
    Next i  
    Extrae10Caracteres = VBA.CLng(Caracter10)  
    End If  
    End Function
    
    \----------------------------------------  
    In Cell C3 type: =Extrae10Caracteres(B3) and copy down.  
    \====================  
    Regards, Andres Rojas Moncada, Colombia
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181188)
    
    *   ![](https://secure.gravatar.com/avatar/7c2af25faf15519b3499790815be8053c20fec771e60cadc30865b94a37b150c?s=64&d=mm&r=g) [Andres Rojas Moncada (Excel Hecho Facil)](http://excelhechofacil.blogspot.com.co/)
         says:
        
        [May 6, 2016 at 1:35 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181205)
        
        I'm Sorry, the line code:
        
        If (ValorCaracter 10) And (VBA.Len(Caracter10) < 10) Then
        
        Replace:
        
        If (ValorCaracter"  
        different operator"10) And (VBA.Len(Caracter10) < 10) Then
        
        Regards
        
        [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181205)
        
12.  ![](https://secure.gravatar.com/avatar/e4708a1733e67db9ed0b12630b9ea8830233d7f5deac23fd32be2ee0301d5d90?s=64&d=mm&r=g) Brian says:
    
    [May 6, 2016 at 4:19 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181262)
    
    In Power Query assuming the original data is in a table called Table1
    
    let  
    Source = Excel.CurrentWorkbook(){\[Name="Table1"\]}\[Content\],  
    #"Added Index1" = Table.AddIndexColumn(Source, "Index", 1, 1),  
    #"Changed Type" = Table.TransformColumnTypes(#"Added Index1",{{"Data", type text}, {"Extract", Int64.Type}}),  
    #"Split Column by Delimiter" = Table.SplitColumn(#"Changed Type","Data",Splitter.SplitTextByDelimiter("#(lf)", QuoteStyle.Csv),{"Data.1", "Data.2" , "Data.3"}),  
    #"Changed Type1" = Table.TransformColumnTypes(#"Split Column by Delimiter",{{"Data.1", type text}, {"Data.2", type text}}),  
    #"Removed Columns" = Table.RemoveColumns(#"Changed Type1",{"Extract"}),  
    #"Unpivoted Other Columns" = Table.UnpivotOtherColumns(#"Removed Columns", {"Index"}, "Attribute", "Value"),  
    #"Added Custom" = Table.AddColumn(#"Unpivoted Other Columns", "Custom", each Text.Length(\[Value\])),  
    #"Filtered Rows" = Table.SelectRows(#"Added Custom", each (\[Custom\] = 10)),  
    #"Removed Columns1" = Table.RemoveColumns(#"Filtered Rows",{"Attribute", "Custom"}),  
    #"Renamed Columns" = Table.RenameColumns(#"Removed Columns1",{{"Index", "Row"}, {"Value", "Extract"}})  
    in  
    #"Renamed Columns"
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181262)
    
    *   ![](https://secure.gravatar.com/avatar/6a70435d993cc4f41eceb077e0eed46211a34d27717315d1406920ef3ff9fada?s=64&d=mm&r=g) Donald Parish says:
        
        [May 7, 2016 at 1:22 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181726)
        
        Good approach. See my 5/7 post for similar solution. I added an Index column before the unpivot, so I could tie the split rows to the original row
        
        [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181726)
        
13.  ![](https://secure.gravatar.com/avatar/d78941caa580c869ec5b5c50e5924366b45b6af5bbbade8d3a254e6a32b5cbf6?s=64&d=mm&r=g) Karthik. G says:
    
    [May 6, 2016 at 5:04 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181289)
    
    How about this  
    \=LOOKUP(10^10,MID(B3,ROW(INDIRECT("1:"&LEN(B3)-9)),10)+0)
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181289)
    
    *   ![](https://secure.gravatar.com/avatar/aee5f5b568c6f3d309e4d5d53b9a98535fd42577d69f12c7476579f35d62842a?s=64&d=mm&r=g) David N says:
        
        [May 11, 2016 at 7:24 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1186209)
        
        This solution is perfect for the consistency of the given samples and gets my vote being both short and creative. However, it won't work if the third number is more than 10 digits. The following example would give 9004123456 as the result.
        
        299004  
        1760481410  
        99004123456
        
        [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1186209)
        
14.  ![](https://secure.gravatar.com/avatar/25a9730846fc4b01d9c7fcb5e99efcd5ad98d0bbbd1e122049dee411b37690d2?s=64&d=mm&r=g) cllach says:
    
    [May 6, 2016 at 5:11 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181292)
    
    \=MID(B3,IF(FIND(CHAR(10),B3)=11,1,IF(FIND(CHAR(10),B3,FIND(CHAR(10),B3)+1)-FIND(CHAR(10),B3)=11,FIND(CHAR(10),B3)+1,FIND(CHAR(10),B3,FIND(CHAR(10),B3)+1)+1)),10)
    
    Almost the same ....
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181292)
    
15.  ![](https://secure.gravatar.com/avatar/aa7e3254f7dfc4575583b9793f4896f20efb5f9726e93b57a1d8e8a65dec6b92?s=64&d=mm&r=g) [Vaibhav](http://excelvbalab.com/)
     says:
    
    [May 6, 2016 at 5:20 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181296)
    
    ok this seems to be shorter than last one of mine
    
    \=LOOKUP(9E+307, --MID(A1,ROW(INDIRECT("1:" & LEN(A1) - 9)), 10))
    
    Cheers!!  
    blog.ExcelVbaLab.Com
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181296)
    
    *   ![](https://secure.gravatar.com/avatar/aee5f5b568c6f3d309e4d5d53b9a98535fd42577d69f12c7476579f35d62842a?s=64&d=mm&r=g) David N says:
        
        [May 11, 2016 at 7:29 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1186215)
        
        Since this solution follows the same premise as the one from Karthik G, it also gets my vote. However, it too is susceptible to the example I showed in my reply to Karthik's post.
        
        [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1186215)
        
16.  ![](https://secure.gravatar.com/avatar/abf2b00fef3fca0fdf9d31013cc370e8cf96993f1ba4aa5b4d81d02c65f9fbcf?s=64&d=mm&r=g) Gary Ferguson says:
    
    [May 6, 2016 at 6:13 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181312)
    
    VBA Method (with flexible number length)
    
    Public Function GetNumWithLen(strValue As String, numLength As Integer)  
    Dim strnum As Variant  
    Dim i As Integer  
    strnum = Split(strValue, Chr(10), , vbBinaryCompare)  
    For i = 0 To 2  
    If Len(strnum(i)) = numLength Then  
    GetNumWithLen = strnum(i)  
    Exit Function  
    End If  
    Next  
    GetNumWithLen = "N/A"  
    End Function
    
    then have a formula in the cell of  
    \=GetNumWithLen(B3,10)
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181312)
    
17.  ![](https://secure.gravatar.com/avatar/aa7e3254f7dfc4575583b9793f4896f20efb5f9726e93b57a1d8e8a65dec6b92?s=64&d=mm&r=g) [Vaibhav](http://excelvbalab.com/)
     says:
    
    [May 6, 2016 at 6:22 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181316)
    
    Here goes Regex solution:
    
    Function ExtNum(cll As String, nDig As Single, cnt As Single) As String  
    Dim regex As Object  
    Set regex = CreateObject("VBScript.RegExp")  
    With regex  
    .Pattern = "\\b\\d{" & nDig & "}\\b"  
    .IgnoreCase = True  
    .Global = True  
    End With
    
    If regex.Test(cll) Then  
    Set matches = regex.Execute(cll)  
    For Each Match In matches  
    i = i + 1  
    If i = cnt Then  
    ExtNum = Match.Value  
    Exit For  
    End If  
    Next Match  
    Else  
    ExtNum = ""  
    End If  
    Set regex = Nothing  
    End Function
    
    Cheers!!  
    blog.ExcelVbaLab.Com
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181316)
    
    *   ![](https://secure.gravatar.com/avatar/aa7e3254f7dfc4575583b9793f4896f20efb5f9726e93b57a1d8e8a65dec6b92?s=64&d=mm&r=g) [Vaibhav](http://excelvbalab.com/)
         says:
        
        [May 6, 2016 at 6:24 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181317)
        
        syntax is =ExtNum(A1,10,1)
        
        here A1 is cell with value,  
        10 for number of matching digits,  
        1 is to get number of occurrence, i.e. 1st, 2nd, 3rd & so on
        
        Cheers!!
        
        [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181317)
        
18.  ![](https://secure.gravatar.com/avatar/3d59f57da241ec5207f04f5df6ca5eb519a6bc98a18650c89e3c07dbbef68b64?s=64&d=mm&r=g) Brian says:
    
    [May 6, 2016 at 7:15 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181333)
    
    \=VALUE(CHOOSE(IF(FIND(CHAR(10),B4)=11,1,IF(FIND(CHAR(10),B4,FIND(CHAR(10),B4)+1)-FIND(CHAR(10),B4)=11,2,3)),LEFT(B4,10),LEFT(RIGHT(B4,LEN(B4)-FIND(CHAR(10),B4)),10),RIGHT(B4,10)))
    
    Scalable, works for 10-digit number in all positions (as long as it's a 3-number set). Lose the VALUE() function if you don't care about a text value being returned.
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181333)
    
19.  ![](https://secure.gravatar.com/avatar/03ed5d6b2d43548500f2499295d6f2fe3a399218f245f25a51254f2c0e35e783?s=64&d=mm&r=g) dolllar says:
    
    [May 6, 2016 at 8:00 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181355)
    
    Can't you just divide the number by 1,000,000 and if the result is greater than 0 and less than 1 display it?
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181355)
    
20.  ![](https://secure.gravatar.com/avatar/75ac277d75e2ce7ed36c265b2ae975f258c23915dc061894328acde34e14aa53?s=64&d=mm&r=g) Modeste Geedee says:
    
    [May 6, 2016 at 10:49 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181411)
    
    Hi, folks...  
    my formula :  
    \=IF(FIND(CHAR(10),A1)>10,LEFT(A1,10),IF(CODE(RIGHT(A1,11))=10,RIGHT(A1,10),MID(A1,FIND(CHAR(10),A1)+1,10)))
    
    assuming Each cell contains 3 numbers separated by line break – CHAR(10) and max number is 10-digit
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181411)
    
21.  ![](https://secure.gravatar.com/avatar/036392219fa42f7d54e74786f1e7bc769c17f67a3361e3ddb8a77d92c3db9647?s=64&d=mm&r=g) SunnyKow says:
    
    [May 6, 2016 at 11:40 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181427)
    
    Since all the 10 digit numbers begin with 1 and no others contain 1, I would use =MID(B3,FIND("1",B3),10). Will only work for the sample data given.
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181427)
    
    *   ![](https://secure.gravatar.com/avatar/036392219fa42f7d54e74786f1e7bc769c17f67a3361e3ddb8a77d92c3db9647?s=64&d=mm&r=g) SunnyKow says:
        
        [May 6, 2016 at 11:43 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181430)
        
        Can also use VALUE(MID(B3,FIND(1,B3),10)) if need it to convert to a value
        
        [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181430)
        
22.  ![](https://secure.gravatar.com/avatar/b58f660d8fbf6dba9c536b1fda39c88cf9aa3dd0c8e84ba298f0dea21cae2414?s=64&d=mm&r=g) [Prem Singh](http://na/)
     says:
    
    [May 7, 2016 at 3:42 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181500)
    
    \=INDEX(MID(B3,ROW(INDIRECT("1:"&LEN(B3))),10),MATCH(TRUE,LEN(ABS(1\*(MID(B3,ROW(INDIRECT("1:"&LEN(B3))),10))))=10,0),1)
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181500)
    
23.  ![](https://secure.gravatar.com/avatar/4f18bdb2a90f34d148cca974273f1386f8536eee8652b7679b3f23df3822d5ac?s=64&d=mm&r=g) Hirapara says:
    
    [May 7, 2016 at 5:02 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181525)
    
    Sub Extract10()  
    Dim RawData As Variant  
    Dim StrgVal As String  
    Dim i, j As Integer
    
    For i = 3 To 8  
    StrgVal = Sheet1.Cells(i, 2).Value  
    RawData = Split(StrgVal, Chr(10))  
    For j = 0 To UBound(RawData)  
    If Len(RawData(j)) = 10 Then  
    Sheet1.Cells(i, 3).Value = RawData(j)  
    End If  
    Next j  
    Next i  
    End Sub
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181525)
    
24.  ![](https://secure.gravatar.com/avatar/cb5303d3578e4ae8119b8ce9df2c9b5c932d90575de7898e0a0d95bbc6798544?s=64&d=mm&r=g) Sabeesh says:
    
    [May 7, 2016 at 5:15 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181527)
    
    1\. Select range and click Text to Column  
    2\. Check Others on Step 2 type in ALT+0010 and click finish  
    3\. In the next empty Column type the formula INDEX(A1:C1,MATCH(10,LEN(A1:C1),0)) and CTRL + Enter and fill down  
    (Assuming data is in column A)
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181527)
    
25.  ![](https://secure.gravatar.com/avatar/384f7e1fad91b1e90ce2f79dc014b35f72d3d1d88cab22be283fe73808a8a9ef?s=64&d=mm&r=g) Asheesh says:
    
    [May 7, 2016 at 5:41 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181542)
    
    Hi,
    
    Here is my go...!! non array solution..
    
    MID(B3,SEARCH(CHAR(10)&REPT("?",10)&CHAR(10),CHAR(10)&B3&CHAR(10)),10)
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181542)
    
    *   ![](https://secure.gravatar.com/avatar/aa7e3254f7dfc4575583b9793f4896f20efb5f9726e93b57a1d8e8a65dec6b92?s=64&d=mm&r=g) [Vaibhav](http://excelvbalab.com/)
         says:
        
        [May 7, 2016 at 6:22 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181558)
        
        This one is cool!!
        
        [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181558)
        
        *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
            
            [May 7, 2016 at 5:48 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181804)
            
            @Vaibhav,  
            I still think your formula (with a minor change):  
            \=LOOKUP(9^99,--MID(B3,ROW(INDIRECT("1:"&LEN(B3)-9)),10))  
            is the coolest (so far...)
            
            [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181804)
            
            *   ![](https://secure.gravatar.com/avatar/384f7e1fad91b1e90ce2f79dc014b35f72d3d1d88cab22be283fe73808a8a9ef?s=64&d=mm&r=g) Asheesh says:
                
                [May 9, 2016 at 5:02 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1183986)
                
                Exactly...so do I
                
                But if I were you I would not use Indirect function to generate the sequence of numbers..I would rather use ROW($A$1:INDEX(A:A,len(B3)-9))
                
                [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1183986)
                
                *   ![](https://secure.gravatar.com/avatar/aa7e3254f7dfc4575583b9793f4896f20efb5f9726e93b57a1d8e8a65dec6b92?s=64&d=mm&r=g) [Vaibhav](http://excelvbalab.com/)
                     says:
                    
                    [May 10, 2016 at 8:56 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1184741)
                    
                    even though this will fetch result, but i like to keep a number of functions as less as possible.
                    
        *   ![](https://secure.gravatar.com/avatar/7a013f2fa6b8808ca5dae786753bc8a2610b67c9441012ee788be1093e59b7b1?s=64&d=mm&r=g) Elias says:
            
            [May 7, 2016 at 8:51 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181873)
            
            @Vaibhav I think yours is cool too, but I prefer Asheesh's because is not volatile.
            
            [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181873)
            
    *   ![](https://secure.gravatar.com/avatar/aee5f5b568c6f3d309e4d5d53b9a98535fd42577d69f12c7476579f35d62842a?s=64&d=mm&r=g) David N says:
        
        [May 11, 2016 at 7:11 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1186189)
        
        This is a good solution, and it works for the given samples. But it won't work for others. Daniel H offered an identical solution except for the REPT; see my reply to his post for one such case.
        
        [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1186189)
        
26.  ![](https://secure.gravatar.com/avatar/7287f28430d7fcf98054efe7f10b04d704aa75b97a2fea7aaac950c1899fa8d1?s=64&d=mm&r=g) [Sunil Pandey](http://www.dynamiclevels.com/)
     says:
    
    [May 7, 2016 at 5:43 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181543)
    
    \=IF(FIND(CHAR(10),B3)=11,LEFT(B3,10),  
    IF(FIND(CHAR(10),RIGHT(B3,LEN(B3)-(FIND(",",SUBSTITUTE(B3,CHAR(10),",",1)))))=11,LEFT(RIGHT(B3,LEN(B3)-(FIND(",",SUBSTITUTE(B3,CHAR(10),",",1)))),10),  
    RIGHT(B3,LEN(B3)-(FIND(CHAR(10),SUBSTITUTE(B3,CHAR(10),",",1),1)))))
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181543)
    
27.  ![](https://secure.gravatar.com/avatar/aa7e3254f7dfc4575583b9793f4896f20efb5f9726e93b57a1d8e8a65dec6b92?s=64&d=mm&r=g) [Vaibhav](http://excelvbalab.com/)
     says:
    
    [May 7, 2016 at 6:15 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181555)
    
    so many grey areas & combination of solutions!!
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181555)
    
28.  ![](https://secure.gravatar.com/avatar/6a70435d993cc4f41eceb077e0eed46211a34d27717315d1406920ef3ff9fada?s=64&d=mm&r=g) Donald Parish says:
    
    [May 7, 2016 at 1:16 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181718)
    
    Used GUI to build, then modified code by hand to Merge the final step with and earlier step in the query to avoid having and extra table.
    
    The key was to use a newer Split By feature that let's you split by Special Character of Line Feed. But first add an Index column, so when we unpivot the Split rows, we can tie each Line within a cell to the original Row number. We than add the Length of each line as a Custom Column, filter to only keep the rows with Length 10. Finally, I join it back to original data, and add a test column to match sure I match the expected value.
    
    let  
    Source = Excel.CurrentWorkbook(){\[Name="Table1"\]}\[Content\],  
    #"Added Index" = Table.AddIndexColumn(Source, "Index", 0, 1),  
    Base = Table.TransformColumnTypes(#"Added Index",{{"Extract", type text}}),  
    #"Split Column by Delimiter" = Table.SplitColumn(Base,"Data",Splitter.SplitTextByDelimiter("#(lf)", QuoteStyle.Csv),{"Data.1", "Data.2", "Data.3"}),  
    #"Removed Columns" = Table.RemoveColumns(#"Split Column by Delimiter",{"Extract"}),  
    #"Reordered Columns" = Table.ReorderColumns(#"Removed Columns",{"Index", "Data.1", "Data.2", "Data.3"}),  
    #"Unpivoted Other Columns" = Table.UnpivotOtherColumns(#"Reordered Columns", {"Index"}, "Attribute", "Value"),  
    #"Split Column by Delimiter1" = Table.SplitColumn(#"Unpivoted Other Columns","Attribute",Splitter.SplitTextByDelimiter("Data.", QuoteStyle.Csv),{"Attribute.1", "Attribute.2"}),  
    #"Removed Columns1" = Table.RemoveColumns(#"Split Column by Delimiter1",{"Attribute.1"}),  
    #"Renamed Columns" = Table.RenameColumns(#"Removed Columns1",{{"Attribute.2", "Column"}}),  
    #"Inserted Text Length" = Table.AddColumn(#"Renamed Columns", "Length", each Text.Length(\[Value\]), type number),  
    #"Filtered Rows" = Table.SelectRows(#"Inserted Text Length", each (\[Length\] = 10)),  
    #"Removed Columns2" = Table.RemoveColumns(#"Filtered Rows",{"Length"}),  
    #"Merged Queries" = Table.NestedJoin(#"Removed Columns2",{"Index"},Base,{"Index"},"NewColumn",JoinKind.LeftOuter),  
    #"Expanded NewColumn" = Table.ExpandTableColumn(#"Merged Queries", "NewColumn", {"Data", "Extract"}, {"Data", "Extract"}),  
    #"Removed Columns3" = Table.RemoveColumns(#"Expanded NewColumn",{"Index"}),  
    #"Reordered Columns1" = Table.ReorderColumns(#"Removed Columns3",{"Data", "Extract", "Value", "Column"}),  
    #"Renamed Columns1" = Table.RenameColumns(#"Reordered Columns1",{{"Column", "Line"}}),  
    #"Added Custom" = Table.AddColumn(#"Renamed Columns1", "Match?", each \[Extract\] =\[Value\])  
    in  
    #"Added Custom"
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181718)
    
29.  ![](https://secure.gravatar.com/avatar/7a013f2fa6b8808ca5dae786753bc8a2610b67c9441012ee788be1093e59b7b1?s=64&d=mm&r=g) Elias says:
    
    [May 7, 2016 at 9:46 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181910)
    
    One more with Power Query  
    let  
    Source = Excel.CurrentWorkbook(){\[Name="Table1"\]}\[Content\],  
    DupCol = Table.DuplicateColumn(Source, "Data", "DC"),  
    Split = Table.SplitColumn(DupCol,"DC",Splitter.SplitTextByDelimiter("#(lf)", QuoteStyle.None),{"D1", "D2", "D3"}),  
    AddCol = Table.AddColumn(Split, "Extract", each if Text.Length(\[D1\]) = 10 then \[D1\] else if Text.Length(\[D2\]) = 10 then \[D2\] else \[D3\]),  
    Final = Table.RemoveColumns(AddCol,{"D1", "D2", "D3"})  
    in  
    Final
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1181910)
    
30.  ![](https://secure.gravatar.com/avatar/7172db04de729c130c11ae51bd08f28faea7ec5cfd74ffe8368e7b96fa34ffe3?s=64&d=mm&r=g) Denys Calvin says:
    
    [May 8, 2016 at 1:33 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1182288)
    
    Here's a generalized solution to search in a string ("Str") for a substring of a particular length ("Length") that is set off from other substrings by a particular character ("Char"). I conceive it as recursive calls of a user-defined function I'll call "ExtractStr" that in the example given we use as follows:
    
    \=ExtractStr(ExtractStr(Str,Length,Char),Length,Char)
    
    where  
    Str = the value in the "Data" column of the example  
    Length = 10  
    Char = Char(10)  
    and the UDF is nested once because there are 3 substrings. If there were n substrings, the UDF would be nested n-2 times.
    
    The UDF is:
    
    Public Function ExtractStr(Str As String, Length As Integer, Char As String) As String  
    Dim Result As String  
    Dim Pos As Integer  
    Pos = InStr(Str, Char)  
    If Pos < Length + 1 Then  
    Result = Replace(Str, Left(Str, Pos), "")  
    Else  
    Result = Left(Str, Length)  
    End If  
    ExtractStr = Result  
    End Function
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1182288)
    
31.  ![](https://secure.gravatar.com/avatar/2c7d8e68af4e8fb478b36b7507a0d2638fa3fdee9a5b273172df962595fbe701?s=64&d=mm&r=g) Ernesto says:
    
    [May 8, 2016 at 2:46 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1182402)
    
    Its VERY simple. The formula needed is the following:
    
    \=MID(B3,FIND(1,B3,1),10)
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1182402)
    
    *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
        
        [May 8, 2016 at 12:24 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1182904)
        
        @Ernesto,  
        Although I am not Chandoo's spokesman - he wrote VERY CLEARLY (and I quote): "you need to extract the number that is 10 digits long".  
        He never mentioned a thing about the first digit of the 10 digits number being "1".
        
        [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1182904)
        
32.  ![](https://secure.gravatar.com/avatar/f465fc81ee0a121e1aed877450d396403d4477a7e346b2eaa0b0823af89e395f?s=64&d=mm&r=g) Target says:
    
    [May 9, 2016 at 1:35 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1183521)
    
    \=if(mid(b3,11,1)=char(10), left(b3,10),if(mid(b3,len(b3)-10,1)=char(10),right(b3,10)mid(b3,search(char(10),b3,1)+1,10)))
    
    obviously assumes only 3 sub strings, and assumes there actually is a 10 digit string (ie if there are 3 6 character strings the answer would be incorrect)
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1183521)
    
33.  ![](https://secure.gravatar.com/avatar/8b875c9820cb7b0be4f327283b40e70cf5d3cfcb0e612d17996ef90694e81067?s=64&d=mm&r=g) DJP says:
    
    [May 9, 2016 at 9:45 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1183712)
    
    Hi everyone,  
    An array formula (Ctrl+Shift+Enter)  
    Assuming that Len of col B content always = 23 (case here) and that the 10 digits no cannot be in 1st position (according to the displayed pattern), I built:  
    {=IF(MAX((MID(B3,ROW(A1:A23),1)=CHAR(10))\*ROW(A1:A23))=13,RIGHT(B3,10),MID(B3,FIND(CHAR(10),B3)+1,10))}  
    Cheers 🙂
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1183712)
    
34.  ![](https://secure.gravatar.com/avatar/8b875c9820cb7b0be4f327283b40e70cf5d3cfcb0e612d17996ef90694e81067?s=64&d=mm&r=g) DJP says:
    
    [May 9, 2016 at 11:28 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1183747)
    
    Hi again,  
    Now, the 10 digits no can be in the 1st position !  
    \=IF(FIND(CHAR(10),B3)=11,LEFT(B3,10),IF(MAX((MID(B3,ROW(A1:A23),1)=CHAR(10))\*ROW(A1:A23))=13,RIGHT(B3,10),MID(B3,FIND(CHAR(10),B3)+1,10)))  
    Don't forget C+S+E
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1183747)
    
35.  ![](https://secure.gravatar.com/avatar/7301d599671545ca183da76efe0e3153ea1a6f073471883c1671e019774720ef?s=64&d=mm&r=g) Micah Dail says:
    
    [May 9, 2016 at 1:31 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1183860)
    
    Here's my ham-handed solution. Array entered formula. Uses ROW(INDIRECT()) to loop through the string and incrementally extract out 10 characters. Then checks if characters are number, and then returns the maximum (which should be the only) number that is 10 characters long.
    
    {=MAX(IFERROR(1\*MID(SUBSTITUTE(B3,CHAR(10),"|"),ROW(INDIRECT("1:"&LEN(B3)-9)), 10), ""))}
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1183860)
    
    *   ![](https://secure.gravatar.com/avatar/37126bca5b2d642974940c98f7a8241b321d0f5c21e32fb204d414d88c874564?s=64&d=mm&r=g) Leonid says:
        
        [May 9, 2016 at 8:22 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1184106)
        
        @Micah  
        Not sure why you need SUBSTITUTE(B3,CHAR(10),"|").  
        \=MAX(IFERROR(1\*MID($B3,ROW($A$1:INDEX(A:A,LEN($B3)-9)), 10), "")) works for me without SUBSTITUTE.  
        I like your solution, but it's based on an assumption that there are no numbers there that are lengthier than 10 digits.
        
        [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1184106)
        
36.  ![](https://secure.gravatar.com/avatar/966b77fa9f25eacf0db9921410abc6cd8a3b3585055ae4f85a33a48f738c7873?s=64&d=mm&r=g) Nanna says:
    
    [May 9, 2016 at 2:33 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1183896)
    
    I would use Text to Column to get three seperate columns. Then the following formula will extra the number that is 10 characters long.
    
    \=IF(LEN(B3)=10,B3,IF(LEN(C3)=10,C3,D3))
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1183896)
    
37.  ![](https://secure.gravatar.com/avatar/8a404cdf7424548f4f75d050e1886bde8dea5d6a37477344d7903e5a6cfa6afd?s=64&d=mm&r=g) Malvinder Virdi says:
    
    [May 10, 2016 at 7:35 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1184690)
    
    \=IF(LEN(LEFT(B3,SEARCH(CHAR(10),B3,1)-1))=10,LEFT(B3,SEARCH(CHAR(10),B3,1)-1),IF(LEN(MID(B3,SEARCH(CHAR(10),B3,1)-1+2,FIND(CHAR(10),B3,FIND(CHAR(10),B3)+1)-(SEARCH(CHAR(10),B3,1)-1+2)))=10,MID(B3,SEARCH(CHAR(10),B3,1)-1+2,FIND(CHAR(10),B3,FIND(CHAR(10),B3)+1)-(SEARCH(CHAR(10),B3,1)-1+2)),IF(LEN(RIGHT(B3,LEN(B3)-FIND(CHAR(10),B3,FIND(CHAR(10),B3)+1)))=10,RIGHT(B3,LEN(B3)-FIND(CHAR(10),B3,FIND(CHAR(10),B3)+1)))))
    
    Note : First time have posted some solution on your site. But have taken lot more from your website in my regular work.
    
    Explanation :
    
    Number of Character in a Cell = =LEN(B3)  
    Finding First Enter Char (10) position = SEARCH(CHAR(10),B3,1)-1  
    Finding 2nd Enter Char (10) position =FIND(CHAR(10),B3,FIND(CHAR(10),B3)+1)  
    Finding Left Number =LEFT(B3,SEARCH(CHAR(10),B3,1)-1)  
    Finding Mid Number =MID(B3,SEARCH(CHAR(10),B3,1)-1+2,FIND(CHAR(10),B3,FIND(CHAR(10),B3)+1)-(SEARCH(CHAR(10),B3,1)-1+2))  
    Finding Right Number =RIGHT(B3,LEN(B3)-FIND(CHAR(10),B3,FIND(CHAR(10),B3)+1))
    
    Then if Loop to Check the count of Character in left, Mid, Center and where ever the count is 10 show it.
    
    Hope it is the easy solution.
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1184690)
    
    *   ![](https://secure.gravatar.com/avatar/aa7e3254f7dfc4575583b9793f4896f20efb5f9726e93b57a1d8e8a65dec6b92?s=64&d=mm&r=g) [Vaibhav](http://excelvbalab.com/)
         says:
        
        [May 10, 2016 at 8:53 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1184740)
        
        very good explanation.
        
        [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1184740)
        
        *   ![](https://secure.gravatar.com/avatar/8a404cdf7424548f4f75d050e1886bde8dea5d6a37477344d7903e5a6cfa6afd?s=64&d=mm&r=g) Malvinder Virdi says:
            
            [May 10, 2016 at 9:12 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1184753)
            
            Thanks
            
            [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1184753)
            
38.  ![](https://secure.gravatar.com/avatar/58c24a17970395d1d1164b4d1407b8896d5948183740d626a4cc213b6a3b9678?s=64&d=mm&r=g) nitin Verma says:
    
    [May 10, 2016 at 8:25 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1184722)
    
    Use with control +shift+ ENter
    
    \=MAX(IFERROR(VALUE(MID(B3,ROW(INDIRECT("a1:a"&LEN(B3))),10)),0))
    
    Regards  
    Nitin Verma
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1184722)
    
    *   ![](https://secure.gravatar.com/avatar/aa7e3254f7dfc4575583b9793f4896f20efb5f9726e93b57a1d8e8a65dec6b92?s=64&d=mm&r=g) [Vaibhav](http://excelvbalab.com/)
         says:
        
        [May 10, 2016 at 8:52 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1184739)
        
        Formula not working when there is number with more than 10 digit.
        
        [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1184739)
        
39.  ![](https://secure.gravatar.com/avatar/90d6e5a60dc393ba190b6fec95456b4f5bc058ee95919583b8fed4e65c32043c?s=64&d=mm&r=g) sam says:
    
    [May 10, 2016 at 11:55 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1184832)
    
    \=MID(CHAR(10)&B3&CHAR(10),SEARCH(CHAR(10)&"??????????"&CHAR(10),CHAR(10)&B3&CHAR(10))+1,10)
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1184832)
    
    *   ![](https://secure.gravatar.com/avatar/aee5f5b568c6f3d309e4d5d53b9a98535fd42577d69f12c7476579f35d62842a?s=64&d=mm&r=g) David N says:
        
        [May 11, 2016 at 7:15 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1186198)
        
        Although this solution was my first thought as well, see my replies to Daniel H and Asheesh for an example case where it won't work.
        
        [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1186198)
        
40.  ![](https://secure.gravatar.com/avatar/038d408c149f36ab4275ec8a8c58c24b69d06a6ea84828c367616f47d3ae1ac1?s=64&d=mm&r=g) tim says:
    
    [May 10, 2016 at 1:38 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1184933)
    
    shame on me ... i went the cheap route and used flash fill.
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1184933)
    
41.  ![](https://secure.gravatar.com/avatar/39deb32cf19ef92c7c7eb12364ba114d47a21ff6f34272b2f09e8460e0cfbac9?s=64&d=mm&r=g) Kuldeep Mishra says:
    
    [May 10, 2016 at 5:40 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1185094)
    
    \=IF(LEN(LEFT(B3,FIND(CHAR(10),B3)-1))=10,LEFT(B3,FIND(CHAR(10),B3)-1),IF(LEN(RIGHT(B3,LEN(B3)-FIND(CHAR(10),B3,FIND(CHAR(10),B3)+1)))=10,RIGHT(B3,LEN(B3)-FIND(CHAR(10),B3,FIND(CHAR(10),B3)+1)),MID(B3,FIND(CHAR(10),B3)+1,10)))
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1185094)
    
42.  ![](https://secure.gravatar.com/avatar/37126bca5b2d642974940c98f7a8241b321d0f5c21e32fb204d414d88c874564?s=64&d=mm&r=g) Leonid says:
    
    [May 10, 2016 at 7:39 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1185200)
    
    I like Sam's formula:
    
    \-not obscure, directly looks for what was asked  
    \-short  
    \-non array  
    \-works with both digits and alpha characters  
    \-easy to adjust for other length.  
    I'd suggest slightly shortened version:  
    \=MID(B3,SEARCH(CHAR(10)&REPT("?",10)&CHAR(10),CHAR(10)&B3&CHAR(10)),10)  
    If we want to extract numbers only then  
    \=IFERROR(--MID(B3,SEARCH(CHAR(10)&REPT("?",10)&CHAR(10),CHAR(10)&B3&CHAR(10)),10),"")
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1185200)
    
43.  ![](https://secure.gravatar.com/avatar/aee5f5b568c6f3d309e4d5d53b9a98535fd42577d69f12c7476579f35d62842a?s=64&d=mm&r=g) David N says:
    
    [May 11, 2016 at 8:27 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1186258)
    
    This is a reapplication of the awesome technique Roberto Mensa contributed for the Winning Streak problem Chandoo offered in a previous post. It could be shortened a little with things like --MID(...) instead of VALUE(MID(...)) or $A$1 instead of INDEX(A:A,1), but the core of the solution would remain the same.
    
    Note that it is a CSE array. As far as I can tell it works no matter where the 10 digit number is located and appropriately fails if there is no 10 digit number.
    
    \=MID(B3,MATCH(10,FREQUENCY(IF(ISNUMBER(VALUE(MID(B3,ROW(INDEX(A:A,1):INDEX(A:A,LEN(B3))),1))),ROW(INDEX(A:A,1):INDEX(A:A,LEN(B3)))),IF(ISNUMBER(VALUE(MID(B3,ROW(INDEX(A:A,1):INDEX(A:A,LEN(B3))),1))),,ROW(INDEX(A:A,1):INDEX(A:A,LEN(B3))))),0)-10,10)
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1186258)
    
44.  ![](https://secure.gravatar.com/avatar/e8681dec180dd2788ff94c042c77f0b1434acd021e496dfec043316b00149cd0?s=64&d=mm&r=g) Paul S says:
    
    [May 16, 2016 at 3:39 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1190221)
    
    Not the prettiest of formulas but....
    
    \=IF(FIND(CHAR(10),B3)=11,LEFT(B3,10),IF(FIND(CHAR(10),B3,FIND(CHAR(10),B3)+1)-FIND(CHAR(10),B3)=11,RIGHT(LEFT(B3,FIND(CHAR(10),B3,FIND(CHAR(10),B3)+1)),11),RIGHT(B3,10)))
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1190221)
    
45.  ![](https://secure.gravatar.com/avatar/749b79c2ec7afe93f7443be290b9caf9ee41bdf733f0b5b087a68999d92f3f49?s=64&d=mm&r=g) Rushabh Gala says:
    
    [May 22, 2016 at 5:44 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1195210)
    
    \=TEXT(MAX(IFERROR(VALUE(MID(B5,14,10)),0),IFERROR(VALUE(MID(B5,7,10)),0),IFERROR(VALUE(MID(B5,8,10)),0)),"0000000000")
    
    This gave perfect answer.
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1195210)
    
46.  ![](https://secure.gravatar.com/avatar/7ef7b54c5d60458bbe6e6a654994b746f1178f025451e1c1456711c212a5c9c0?s=64&d=mm&r=g) MichaelCH says:
    
    [May 28, 2016 at 10:20 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1199015)
    
    \=MID(A1,MATCH(11,FREQUENCY(ROW($1:$99),ISERR(-MID(A1&-10^9,ROW($1:$99),1))\*ROW($1:$99)),)-10,10)
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1199015)
    
47.  ![](https://secure.gravatar.com/avatar/8de0f37951b19489700a0902e29b2228cc5e051c2fe4ccc8c62f44eebf3588de?s=64&d=mm&r=g) Gala says:
    
    [May 29, 2016 at 9:23 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1199997)
    
    Here's my answer
    
    \=IF(LEN(TEXT(A7,"0"))=10,A7,"")
    
    A7 is my initial cell. then just drag down the cell
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1199997)
    
48.  ![](https://secure.gravatar.com/avatar/75c334365ff4885a44651a26505d1dad31307eafc37667131ab9089d8594d1ff?s=64&d=mm&r=g) Haz says:
    
    [June 2, 2016 at 9:39 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1203404)
    
    \=INDEX(TRIM(MID(REPLACE(B8,CHAR(10),REPT(" ",100)),{1,100,200},100)), MATCH(10,LEN(TRIM(MID(REPLACE(B8,CHAR(10),REPT(" ",100)),{1,100,200},100))),0))
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1203404)
    
    *   ![](https://secure.gravatar.com/avatar/75c334365ff4885a44651a26505d1dad31307eafc37667131ab9089d8594d1ff?s=64&d=mm&r=g) Haz says:
        
        [June 8, 2016 at 7:05 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1209650)
        
        With CSE:  
        {=MID(B3,MATCH(10,LEN(REPLACE(MID(B3,ROW(OFFSET($A$1,,,LEN(B3))),10),CHAR(10),)),0),10)}
        
        [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1209650)
        
49.  ![](https://secure.gravatar.com/avatar/8d98b803cefca7ae4681a69d3e620110628ca9ce6cf2473403a79926a8a4b456?s=64&d=mm&r=g) Sridhar Belide says:
    
    [June 3, 2016 at 1:02 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1203573)
    
    When this will be answered by Chandoo?
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1203573)
    
50.  ![](https://secure.gravatar.com/avatar/4369a2e04fdf877fec41d1102d6ad08d94eeb5555e15b04f1be4b7b4808fe41c?s=64&d=mm&r=g) CC says:
    
    [October 4, 2016 at 10:10 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1303811)
    
    \=IF(FIND(CHAR(10),B3)=11,LEFT(B3,10),IF(ISERROR(FIND(CHAR(10),RIGHT(B3,10))),RIGHT(B3,10),MID(B3,FIND(CHAR(10),B3)+1,10)))
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1303811)
    
51.  ![](https://secure.gravatar.com/avatar/821b56d18d0c3e92ad60d759faa6f457e2e942484f6b2764dfed28311907ee4a?s=64&d=mm&r=g) Yogendra C says:
    
    [October 27, 2016 at 9:08 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1323972)
    
    IF(LEN(LEFT(B3,FIND(CHAR(10),B3,1)))=10,LEFT(B3,FIND(CHAR(10),B3,1)),IF(LEN(MID(B3,FIND(CHAR(10),B3,1)+1,(FIND(CHAR(10),B3,(FIND(CHAR(10),B3,1))+1))-FIND(CHAR(10),B3,1)-1))=10,MID(B3,FIND(CHAR(10),B3,1)+1,(FIND(CHAR(10),B3,(FIND(CHAR(10),B3,1))+1))-FIND(CHAR(10),B3,1)-1),IF(LEN(MID(B3,(FIND(CHAR(10),B3,FIND(CHAR(10),B3,1)+1))+1,LEN(B3)-(FIND(CHAR(10),B3,FIND(CHAR(10),B3,1)+1))+1))=10,MID(B3,(FIND(CHAR(10),B3,FIND(CHAR(10),B3,1)+1))+1,LEN(B3)-(FIND(CHAR(10),B3,FIND(CHAR(10),B3,1)+1))+1),"No Ten Numbers Exists")))
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1323972)
    
52.  ![](https://secure.gravatar.com/avatar/b3557456060addb51588b874aae05655384cf08a8751df5f6c1f2ff718371f73?s=64&d=mm&r=g) Ashish kumar says:
    
    [January 27, 2017 at 6:16 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1399363)
    
    Dear All,
    
    One Problems  
    I have one data of date type like this
    
    Date  
    Feb 15 2016  
    Oct 17 2016  
    Jul 15 2016  
    Jun 16 2016  
    Apr 30 2017  
    Mar 19 2017  
    Jan 10 2017
    
    And i want to get the data in this Format
    
    Desired Output in Date Format  
    15-Feb-16  
    17-Oct-16  
    15-Jul-16  
    16-Jun-16  
    30-Apr-17  
    19-Mar-17  
    10-Jan-17
    
    So please help on this
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1399363)
    
    *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
        
        [January 27, 2017 at 9:32 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1399399)
        
        @Ashish kumar,  
        Select the 7 cells range > goto 'DATA' > 'TEXT TO COLUMNS' > mark 'SEPERATED' > NEXT > NEXT > mark date format 'MDY' > 'FINISH'.  
        \-----------------  
        Michael Avidan  
        ISRAEL
        
        [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1399399)
        
        *   ![](https://secure.gravatar.com/avatar/b3557456060addb51588b874aae05655384cf08a8751df5f6c1f2ff718371f73?s=64&d=mm&r=g) Ashish kumar says:
            
            [January 27, 2017 at 10:22 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1399406)
            
            Sir  
            By formula
            
            [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1399406)
            
            *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
                
                [January 27, 2017 at 11:05 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1399423)
                
                @Ashish kumar,  
                Try the suggested formula in the lonked picture:  
                [https://postimg.org/image/q549uhuel/](https://postimg.org/image/q549uhuel/)
                  
                \-----------------  
                Michael Avidan  
                ISRAEL
                
                [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1399423)
                
53.  ![](https://secure.gravatar.com/avatar/a96812162ecaadcfd666346bace7214aac1bfd61457d2a56e38510a4a005560d?s=64&d=mm&r=g) Rishi Kumar says:
    
    [August 16, 2017 at 10:12 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1497316)
    
    \=IF(FIND("",B4)=11,LEFT(B4,10),IF(FIND("",B4,FIND("",B4)+1)-FIND("",B4)<10,RIGHT(B4,10),MID(B4,FIND("",B4)+1,10)))
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1497316)
    
54.  ![](https://secure.gravatar.com/avatar/961dfe204e2035fa2b67100785726233138bc8dc8c392326f8149f11f7ca4a3c?s=64&d=mm&r=g) Nyakno-Abasi Obott says:
    
    [November 28, 2017 at 4:16 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1525046)
    
    \=RIGHT(SUBSTITUTE(B3,CHAR(10),"-"),LEN(SUBSTITUTE(B3,CHAR(10),"-"))-FIND("-",SUBSTITUTE(B3,CHAR(10),"-"),FIND("-",SUBSTITUTE(B3,CHAR(10),"-"))+1))
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1525046)
    
55.  ![](https://secure.gravatar.com/avatar/961dfe204e2035fa2b67100785726233138bc8dc8c392326f8149f11f7ca4a3c?s=64&d=mm&r=g) Nyakno-Abasi Obott says:
    
    [November 28, 2017 at 4:28 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1525048)
    
    Here's my solution:
    
    \=RIGHT(SUBSTITUTE(B3,CHAR(10),"-"),LEN(SUBSTITUTE(B3,CHAR(10),"-"))-FIND("-",SUBSTITUTE(B3,CHAR(10),"-"),FIND("-",SUBSTITUTE(B3,CHAR(10),"-"))+1))
    
    Nyakno-Abasi Obott  
    NIGERIA
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1525048)
    
56.  ![](https://secure.gravatar.com/avatar/4d73edac775b34e130e65ab9ac830579c5eafc54539d415bbc4f610e065f890e?s=64&d=mm&r=g) Gayane says:
    
    [June 5, 2018 at 8:46 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1551193)
    
    \=IF(FIND(CHAR(10),B3,FIND(CHAR(10),B3,1)+1)-FIND(CHAR(10),B3,1)<10,MID(B3,FIND(CHAR(10),B3,FIND(CHAR(10),B3,1)+1)+1,10),MID(B3,FIND(CHAR(10),B3,1),FIND(CHAR(10),B3,FIND(CHAR(10),B3,1)+1)-FIND(CHAR(10),B3,1)))
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1551193)
    
57.  ![](https://secure.gravatar.com/avatar/961dfe204e2035fa2b67100785726233138bc8dc8c392326f8149f11f7ca4a3c?s=64&d=mm&r=g) Nyakno-Abasi Obott says:
    
    [June 28, 2018 at 8:11 am](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1555450)
    
    My Solution:
    
    \=IF(LEN(LEFT(B5,FIND(CHAR(10),B5)-1))=10,LEFT(B5,FIND(CHAR(10),B5)-1),"")&IF(LEN(MID(B5,FIND(CHAR(10),B5)+1,FIND(CHAR(10),B5,FIND(CHAR(10),B5)+1)-FIND(CHAR(10),B5)-1))=10,MID(B5,FIND(CHAR(10),B5)+1,FIND(CHAR(10),B5,FIND(CHAR(10),B5)+1)-FIND(CHAR(10),B5)-1),"")&IF(LEN(RIGHT(B5,LEN(B5)-FIND(CHAR(10),B5,FIND(CHAR(10),B5)+1)))=10,RIGHT(B5,LEN(B5)-FIND(CHAR(10),B5,FIND(CHAR(10),B5)+1)),"")
    
    Nyakno-Abasi Obott  
    NIGERIA
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1555450)
    
58.  ![](https://secure.gravatar.com/avatar/df1c03e03a5aaebff204c0b4a5ff3e776f363f8e9f11cafe5db70dbb2b92c329?s=64&d=mm&r=g) Avi Kohanim says:
    
    [December 17, 2019 at 2:06 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1722189)
    
    \=IF(FIND(CHAR(10),B3)=11,LEFT(B3,10),IF(FIND(CHAR(10),MID(B3,FIND(CHAR(10),B3)+1,100))=11,MID(B3,FIND(CHAR(10),B3)+1,10),RIGHT(B3,10)))
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1722189)
    
59.  ![](https://secure.gravatar.com/avatar/cd199417aa19c98d733372350b58902dbf79315925b52ebd6b75a4c64ee4fe18?s=64&d=mm&r=g) Sunil says:
    
    [December 14, 2020 at 2:06 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1946490)
    
    In excel ceii have number: 94873/777812345ram bahadur.  
    in another cell lpc777812346  
    need only started 7778 belong 5 digit.  
    Like 77781234 and 777812346
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1946490)
    
60.  ![](https://secure.gravatar.com/avatar/a4c20fc20d1d588b62c4bd6470108179769a27a459223fac89080c77c89bea73?s=64&d=mm&r=g) Mayukh Bhattacharya says:
    
    [April 23, 2021 at 1:23 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1995447)
    
    \=FILTERXML("~" & SUBSTITUTE(A2,CHAR(10),"~~")&"~","//s\[string-length()=10\]")
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1995447)
    
    *   ![](https://secure.gravatar.com/avatar/a4c20fc20d1d588b62c4bd6470108179769a27a459223fac89080c77c89bea73?s=64&d=mm&r=g) Mayukh Bhattacharya says:
        
        [April 23, 2021 at 1:26 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1995448)
        
        \=FILTERXML("~" & SUBSTITUTE(BF3,CHAR(10),"~~")&"~","//s\[string-length()=10\]")
        
        [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-1995448)
        
61.  ![](https://secure.gravatar.com/avatar/fa25acb03d028e383515e45ee05a538925d009596a2c761cccbec0ea560a8095?s=64&d=mm&r=g) Vijay Dhangar says:
    
    [January 26, 2024 at 7:15 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-2167986)
    
    Just copy 10 digits number in the next column and press Ctrl+E (Flash fill)  
    It worked in my computer.
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-2167986)
    
62.  ![](https://secure.gravatar.com/avatar/6ddb4aad4bd3f636e7895c6048287a211130412f56657b48b579d056f1db6e5a?s=64&d=mm&r=g) Cad says:
    
    [November 5, 2025 at 9:34 pm](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-2496965)
    
    \=LET(a,TEXTSPLIT(B3,CHAR(10)),b,LEN(a)=10, FILTER(a,b))
    
    \=CONCAT(BYCOL(TEXTSPLIT(B3,CHAR(10)),LAMBDA(a,IF(LEN(a)=10,a,""))))
    
    \=SUM((LEN(TEXTSPLIT(B3,CHAR(10)))=10)\*(TEXTSPLIT(B3,CHAR(10))))
    
    [Reply](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#comment-2496965)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Excel Tips, Tricks, Cheats & Hacks – Notable Excel Websites (Non-MVP) Edition](https://chandoo.org/wp/excel-tips-tricks-cheats-hacks-notable-excel-websites-non-mvp-edition/) | [Apply Conditional Formatting using Slicers](https://chandoo.org/wp/apply-conditional-formatting-using-slicers/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)