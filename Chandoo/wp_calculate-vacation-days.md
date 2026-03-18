# Can you calculate vacation days in a period? [Homework] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/calculate-vacation-days

---

Can you calculate vacation days in a period? \[Homework\]
=========================================================

[Excel Challenges](https://chandoo.org/wp/category/excel-challenges/)
 - 67 comments

  

Its Friday, that means time for another [Excel challenge](http://chandoo.org/wp/tag/homework/)
 for you.

This is based on yesterday’s [employee vacation dashboard](http://chandoo.org/wp/2013/01/24/employee-vacations-tracker-dashboard/ "Designing a dashboard to track Employee vacations [case study]")
.

### Calculate vacation days in a period:

![Calculate vacation days using Excel formulas - formula challenge & homework](https://img.chandoo.org/hw/calculate-vacation-days-excel-formula-homework.png)Your mission, if you choose to accept it,

**Step 1: [Download this workbook](https://img.chandoo.org/hw/vacation-calculations.xlsx)
.**

**Step 2: Calculate number of vacations taken in a period.** Specifically,

1.  How many vacations are taken between start & end dates, _assuming complete vacation should be inside the start & end date period?_
2.  How many vacations are taken such that at least one day of vacation is between start & end dates?
3.  How many people took vacations? (if same person took multiple vacations, then count it as 1)

**You are free to,**

*   Use helper columns
*   Any formula
*   Play Mission Impossible music in background
*   Drink no more than 2 cups of coffee

### How to post your answers?

Simple, just post them in comments. Include explanation of your logic too _if possible._ **[Click here to post your answers](http://chandoo.org/wp/2013/01/25/calculate-vacation-days/#respond)
.**

### Need some clues?

We have them. See these links:

*   [SUMIFS formula](http://chandoo.org/wp/2010/04/20/introduction-to-excel-sumifs-formula/)
    
*   [SUMPRODUCT formula](http://chandoo.org/wp/2009/11/10/excel-sumproduct-formula/)
    
*   [Range Lookup](http://chandoo.org/wp/2010/06/30/range-lookup-excel/)
     & [Date overlap problems](http://chandoo.org/wp/2010/06/01/date-overlap-formulas/)
    

_**GO!!!**_

### Added later: Solution for this problem

here were quite a few interesting solutions in the comments.

Today, let me explain how to solve these problems using Excel formulas.

### Watch below video:

### Download solution workbook

[Click here to download the solution work book & see the formulas](https://img.chandoo.org/hw/vacation-calculations-sol.xlsx)
.

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
| Written by Chandoo  <br>Tags: [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)<br>, [array formulas](https://chandoo.org/wp/tag/array-formulas/)<br>, [challenge](https://chandoo.org/wp/tag/challenge/)<br>, [countifs](https://chandoo.org/wp/tag/countifs/)<br>, [date and time](https://chandoo.org/wp/tag/date-and-time/)<br>, [downloads](https://chandoo.org/wp/tag/downloads/)<br>, [homework](https://chandoo.org/wp/tag/homework/)<br>, [Learn Excel](https://chandoo.org/wp/tag/excel/)<br>, [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)<br>, [videos](https://chandoo.org/wp/tag/videos/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 67 Responses to “Can you calculate vacation days in a period? \[Homework\]”

1.  ![](https://secure.gravatar.com/avatar/b3b4be10492adf5b38e569234355addeda41b24d897c72178d52a371c15513f7?s=64&d=mm&r=g) K. NARAYAN says:
    
    [January 25, 2013 at 9:59 am](https://chandoo.org/wp/calculate-vacation-days/#comment-408461)
    
    Hi ,  
    I think this time , your challenges are quite simple ; I would like to add some more challenges :  
    How many of the vacations overlapped with each other ?  
    How many vacations did not overlap with each other ?  
    What is the maximum number of people who were on vacation at any point of time ?  
    What is the maximum period when at least one person was on vacation ?  
    What is the maximum / minimum period when no one was on vacation ?  
    Probably each of these can be taken up for a forensic post , assuming that each of them can be solved using formulae.
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-408461)
    
    *   ![](https://secure.gravatar.com/avatar/4391468e624ce070687d7944269e53cb5afee9bef631509733210f7b76a8c8c4?s=64&d=mm&r=g) Sayantan Kar says:
        
        [October 14, 2022 at 3:31 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-2102092)
        
        Please Provide the Answers
        
        [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-2102092)
        
2.  ![](https://secure.gravatar.com/avatar/dba2fe58ce811a00579305025fc1bd7747105b028d05c37ed3e4e08e3c5516b2?s=64&d=mm&r=g) [ChrisByham](http://www.about.me/chrisbyham)
     says:
    
    [January 25, 2013 at 10:03 am](https://chandoo.org/wp/calculate-vacation-days/#comment-408466)
    
    OK,  
       
    I've tackled 1) and 2) in similar ways, using COUNTIFS as follows:  
       
    1) =COUNTIFS(vacations\[Start Date\],">=" & start,vacations\[End Date\],"<=" & end)  
    Counts number of vacations where Start Date is on or later than 01-Feb and End Date is earlier than or on 31-Mar - so entire vacation is within period.  
    2) =COUNTIFS(vacations\[Start Date\],">=" & start,vacations\[Start Date\],"<=" & end) + COUNTIFS(vacations\[Start Date\],"<=" & start,vacations\[End Date\],">=" & start)  
    Similar to 1st question, but looking for vacations where Start Date is later than 01-Feb and start date is earlier than 31-Mar - this captures all vacations that start in the period. Only vacations that are missing are those that start earlier than period and end once the period has started, which is captured by the  
    \+ COUNTIFS(vacations\[Start Date\],"<=" & start,vacations\[End Date\],">=" & start)  
    counting all records where start date is earlier than period start, and end date is later than period start.  
    3) There's probably a nice array formula for this, which I'm going to try and work out. In the meantime, I added a new column, with the formula against the first row as:  
    \=IF(AND(\[@\[Start Date\]\]>=start,\[@\[End Date\]\]<=end,SUMIF($B$3:B3,\[@\[Employee Name\]\],$E$3:E3)=0),1,0)  
    So record a 1 if the vacation is fully within the period (start date is later than 01-Feb AND end date is earlier than 31-Mar) AND if the Employee concerned doesn't already have a 1 against them.  
    I hadn't used SUMIFS until I spotted it on Chandoo a few days ago - such a simple and powerful formula, and I took a guess that a COUNT version would also exist - I'm going to be using these a lot - thanks Chandoo!!
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-408466)
    
    *   ![](https://secure.gravatar.com/avatar/c692798a234d757e0f62473f9b392b2cd534d37506f5f7341407a193a7f79973?s=64&d=mm&r=g) tadovn says:
        
        [January 25, 2013 at 10:41 am](https://chandoo.org/wp/calculate-vacation-days/#comment-408483)
        
        Interesting!
        
        [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-408483)
        
    *   ![](https://secure.gravatar.com/avatar/8a54d1a3e159b618104d81325ae07919e4d7e6c1ee53181266aad5cf74d2c37c?s=64&d=mm&r=g) Abdelrahman says:
        
        [January 28, 2013 at 5:25 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-409569)
        
        Hi ..  
        I tried to use your formulas which is really interesting but it doesn't work with me 🙁
        
        [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-409569)
        
3.  ![](https://secure.gravatar.com/avatar/c692798a234d757e0f62473f9b392b2cd534d37506f5f7341407a193a7f79973?s=64&d=mm&r=g) tadovn says:
    
    [January 25, 2013 at 10:25 am](https://chandoo.org/wp/calculate-vacation-days/#comment-408479)
    
    [https://dl.dropbox.com/u/69797926/vacation-calculations\_tadovn.xlsx](https://dl.dropbox.com/u/69797926/vacation-calculations_tadovn.xlsx)
      
       
    Dear,  
    I sent the answer for this.  
    I use helper column to calculate.  
    The formular i used is IF, COUNTIFS, SUM, SUMIFS.  
    Thanks,
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-408479)
    
4.  ![](https://secure.gravatar.com/avatar/0a7e7527cc17f66e66c71e3d4be572deed308c07a0d64467e164176b65261014?s=64&d=mm&r=g) A. Ramanan says:
    
    [January 25, 2013 at 12:10 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-408517)
    
    Hi,  
    I have converted the Table as normal cells & also additional column (Col E).
    
    Employee Name -   
    B4
    
    Start Date -   
    C4
    
    End Date -   
    D4
    
    \# of days -   
    E4
    
       
    1\. E4 to E123 - =SUMPRODUCT(--(ISNUMBER(MATCH(ROW(INDIRECT(C4&":"&D4)),ROW(INDIRECT(start&":"&end)),0))))  
    Q1 - =SUMPRODUCT(($C$4:$C$123>=start)\*($D$4:$D$123<=end))  
    Q2 - =SUMPRODUCT(--($E$4:$E$123<>0))  
    Q3 -=SUM(IF(FREQUENCY(IF($B$4:$B$123<>"",IF($E$4:$E$123<>0,MATCH($E$4:$E$123,$E$4:$E$123,0))),ROW($E$4:$E$123)-ROW($E$4)+1),2))
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-408517)
    
    *   ![](https://secure.gravatar.com/avatar/8a54d1a3e159b618104d81325ae07919e4d7e6c1ee53181266aad5cf74d2c37c?s=64&d=mm&r=g) Abdelrahman says:
        
        [January 31, 2013 at 7:06 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-410422)
        
        @A. Ramanan  
          
        Hi..  
        Nice work but I wanna see Q3 form because it is not clear..
        
        [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-410422)
        
5.  ![](https://secure.gravatar.com/avatar/0a7e7527cc17f66e66c71e3d4be572deed308c07a0d64467e164176b65261014?s=64&d=mm&r=g) A. Ramanan says:
    
    [January 25, 2013 at 1:30 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-408548)
    
    The answer for Q3 requires Ctrl + Shift + Enter  
     
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-408548)
    
6.  ![](https://secure.gravatar.com/avatar/b3b4be10492adf5b38e569234355addeda41b24d897c72178d52a371c15513f7?s=64&d=mm&r=g) K. NARAYAN says:
    
    [January 25, 2013 at 2:00 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-408560)
    
    Some more challenges :  
    Who took the longest / shortest vacation , and for how many days ?  
    Who was on vacation for the maximum number of days ( this is different from the earlier question , since this includes more than 1 vacation by the same person ) ?  
     
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-408560)
    
7.  ![](https://secure.gravatar.com/avatar/286279e64c2c622ab96bf1f5e23294e8d6f4fc42d420b8b01dcad9b75a56b63c?s=64&d=mm&r=g) Juan Carlos Etayo says:
    
    [January 25, 2013 at 5:58 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-408648)
    
    I need help
    
    Problems running macros in Excel 2010 on Macintosh computers. How I can fix this?  
       
    Thx.
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-408648)
    
8.  ![](https://secure.gravatar.com/avatar/5a2752a18062d8735f1f7ae2b72982d0a4202574727eca9e4dc1308c001c0279?s=64&d=mm&r=g) Mayur Naik says:
    
    [January 25, 2013 at 7:33 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-408690)
    
    Below are the my solutions :  
       
    Q 1>  =IF(C4>start,IF(D4<end,"YES","NO"),"NOO") & Then =COUNTIF($I$4:$I$123,S3)  
    Q 2> =IF(AND(start<C4,C4<end),"YES",IF(AND(start<D4,D4<end),"YES","NO")) & then =COUNTIF($G$4:$G$123,S3)  
    Q3> Remove duplicates from Q 1
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-408690)
    
9.  ![](https://secure.gravatar.com/avatar/605aa0a5ed60566d559c6e247d6ce08efb9fb73560b36c518462fc3811df0158?s=64&d=mm&r=g) Saleh Saeed says:
    
    [January 25, 2013 at 10:22 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-408760)
    
    Hello everybody  
    Q1:   
    \=SUMPRODUCT(--(vacations\[Start Date\]>=start),--(vacations\[End Date\]<=end))  
    Q2:  
    \=SUMIFS(vacations\[Column1\],vacations\[Start Date\],"<="&end,vacations\[End Date\],">="&start)  
    Column1= typed 1 in all cells parallel with other columns  
    Q3:  
    \=IF(OR(C5<=start,D5>=end),IF(COUNTIF($B$4:B7,B7)=1,O4+1,O4),O4)  
    I get by this formula 13 people  
       
    Thank you
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-408760)
    
10.  ![](https://secure.gravatar.com/avatar/8182f2b7edd1a801707d99c2443bcdb4257df24763dc9bba329dcc78a43ea56e?s=64&d=mm&r=g) Sufal says:
    
    [January 25, 2013 at 10:34 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-408764)
    
    I am facing some kind of this problem.  
    My table is like this  
    "Start" column should have the same value as the "End" of Previous Row if the ID is same.  
    For example in the 1st row ID is 1 start and end is 0 and 20 respectively.  
    In the second row ID is 1. So the Start should be 20. But in table its 18. I need to find out the IDs that have this problem.  
    In third row ID is still 1 and "start" is equal to the End of Previous Row having ID 1. So its OK. Can any one give me idea? Thanks  
     
    
    ID  
    Start  
    End
    
    1  
    0  
    20
    
    1  
    18  
    40
    
    1  
    40  
    230
    
    2  
    0  
    250
    
    2  
    250  
    1500
    
    2  
    1500  
    1530
    
    3  
    0  
    15
    
    3  
    15  
    30
    
    3  
    28  
    40
    
    3  
    40
    
    50
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-408764)
    
    *   ![](https://secure.gravatar.com/avatar/c692798a234d757e0f62473f9b392b2cd534d37506f5f7341407a193a7f79973?s=64&d=mm&r=g) tadovn says:
        
        [January 26, 2013 at 2:56 am](https://chandoo.org/wp/calculate-vacation-days/#comment-408855)
        
        Could you upload excel file, pls?
        
        [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-408855)
        
11.  ![](https://secure.gravatar.com/avatar/f907534c8010f5652c25fb6c3b2555e5678589bd3adb7eb2306032a06d9b41e4?s=64&d=mm&r=g) [Mohammed Mustafa](http://www.myexcelacademy.com/)
     says:
    
    [January 26, 2013 at 7:56 am](https://chandoo.org/wp/calculate-vacation-days/#comment-408953)
    
    Ans 1. COUNTIFS(vacations\[Start Date\],">="&start,vacations\[End Date\],"<="&end)  
    Ans 2. Using a helper column with the number 1 in all rows, i used the formula: SUMIFS(vacations\[Column1\],vacations\[Start Date\],"<="&end,vacations\[End Date\],">="&start)  
    Ans 3. I first removed the unique names and used the formula to find the dates using only unique names. Then i used the formula  
     Formula 1. COUNTIFS(vacations\[Employee Name\],O4,vacations\[Start Date\],">="&start,vacations\[End Date\],"<="&end)  
    Formula 2. COUNTIFS(P4:P29,">0") to get 14 as the answer.  
    Thanks,  
    Mustafa
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-408953)
    
12.  ![](https://secure.gravatar.com/avatar/864bc03c0d303d01fee370b4f8d7869525c15c8862db8ddda339c4761bc0ffd7?s=64&d=mm&r=g) Raj Kumar Kothari says:
    
    [January 26, 2013 at 6:11 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-409068)
    
    Hi the following are my answers:  
    **Q1: =SUM((--((vacations\[Start Date\])>=start))\*(--((vacations\[End Date\])<=end)))**  \[CSE\]  
       
    **Q2: =SUM((--((vacations\[Start Date\])<=end))\*(--((vacations\[End Date\])>=start)))**  \[CSE\]  
       
    Q3: This one was little tricky to do it in a single cell (without using helper column), so I copies all the names to a new column N, and removed duplicates (I found 26 unique names in this case) and in the next column I applied the following formula and dragged it down to the last row:  
    **\=IF(SUM(--(N4=vacations\[Employee Name\])\*(--((vacations\[Start Date\])>=start))\*(--((vacations\[End Date\])<=end)))>0,1,0)**  \[CSE\]  
    **And, took a sum of all the velues which was equal to 14.**  
       
    \*CSE = Control+Shift+Enter  
    **Thanks,**  
    **Raj Kumar Kothari**
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-409068)
    
13.  ![](https://secure.gravatar.com/avatar/f08c33d1d73fa954d9c520cb983a06afde390bc5124875aa6606c7ea46909b19?s=64&d=mm&r=g) Mitch says:
    
    [January 26, 2013 at 11:22 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-409122)
    
    So the first two aren't that hard but the third one was quite a pain to do in one cell. Since most people have already answered the first 2, I won't bother answering those. But I will post an answer to the third one:  
    Enter this as an array formula:  
    \=SUMPRODUCT(IFERROR(1/COUNTIFS(vacations\[Employee Name\],vacations\[Employee Name\],vacations\[Start Date\],">" & start,vacations\[End Date\],"<" & end),0),--(vacations\[Start Date\]>start),--(vacations\[End Date\]<end))  
       
    The inspiration for this formula comes from a formula chandoo posted a while back on how to count the number of unique items in a list.  
       
    Thanks for the great challenge Chandoo!
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-409122)
    
    *   ![](https://secure.gravatar.com/avatar/864bc03c0d303d01fee370b4f8d7869525c15c8862db8ddda339c4761bc0ffd7?s=64&d=mm&r=g) Raj Kumar Kothari says:
        
        [January 27, 2013 at 8:23 am](https://chandoo.org/wp/calculate-vacation-days/#comment-409212)
        
        Hi Mitch,  
        I copy pastes this formula but didn't work.  
        –(vacations\[Start Date\]>start),–(vacations\[End Date\]<end) part of the formula yields an error,  
           
        Thanks,  
        Raj
        
        [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-409212)
        
14.  ![](https://secure.gravatar.com/avatar/f08c33d1d73fa954d9c520cb983a06afde390bc5124875aa6606c7ea46909b19?s=64&d=mm&r=g) Mitch says:
    
    [January 27, 2013 at 3:28 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-409283)
    
    The "-" should be doubled as in below (I copy/pasted it from excel before but it seems to have changed to single "-" by itself. I'm using excel 2007 (don't know if that could cause the error)  
       
    \=SUMPRODUCT(IFERROR(1/COUNTIFS(vacations\[Employee Name\],vacations\[Employee Name\],vacations\[Start Date\],">" & start,vacations\[End Date\],"<" & end),0),--(vacations\[Start Date\]>start),--(vacations\[End Date\]<end))
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-409283)
    
15.  ![](https://secure.gravatar.com/avatar/f08c33d1d73fa954d9c520cb983a06afde390bc5124875aa6606c7ea46909b19?s=64&d=mm&r=g) Mitch says:
    
    [January 27, 2013 at 3:29 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-409284)
    
    Turns out it's not my excel copying but the website that, for some reason, is autocorrecting it to not double the "-".  
    You should have two "-" whenever you see them. Let me know if that works.
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-409284)
    
    *   ![](https://secure.gravatar.com/avatar/864bc03c0d303d01fee370b4f8d7869525c15c8862db8ddda339c4761bc0ffd7?s=64&d=mm&r=g) Raj Kumar Kothari says:
        
        [January 27, 2013 at 4:58 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-409295)
        
        Hey Mitch, I tried using the double negative, but didn't work.  
           
        Thanks, Raj
        
        [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-409295)
        
16.  ![](https://secure.gravatar.com/avatar/f08c33d1d73fa954d9c520cb983a06afde390bc5124875aa6606c7ea46909b19?s=64&d=mm&r=g) Mitch says:
    
    [January 27, 2013 at 5:17 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-409299)
    
    Try this. It has the spreadsheet.  
       
    [http://www.excelforum.com/excel-formulas-and-functions/894788-unique-count-with-criteria.html?p=3100520#post3100520](http://www.excelforum.com/excel-formulas-and-functions/894788-unique-count-with-criteria.html?p=3100520#post3100520)
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-409299)
    
    *   ![](https://secure.gravatar.com/avatar/864bc03c0d303d01fee370b4f8d7869525c15c8862db8ddda339c4761bc0ffd7?s=64&d=mm&r=g) Raj Kumar Kothari says:
        
        [January 27, 2013 at 6:20 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-409320)
        
        Hi Mitch, Thanks for your efforts for sharing the link. I really appreciate your help. And yes, this your formula is working fine. Great trick.  
           
        Thanks , Raj
        
        [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-409320)
        
    *   ![](https://secure.gravatar.com/avatar/9994992d27dce0c91f8e4a7fb0d9abb617c99d95b60b9924fe5e633cd0be3df3?s=64&d=mm&r=g) Mahaz says:
        
        [January 28, 2013 at 7:39 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-409595)
        
        Hi Mitch,  
        Thanks for the solution. A question why we have two dash in front "--"  
        in the formula.  
        \=SUMPRODUCT(--(vacations\[Start Date\]>start),--(vacations\[End Date\]<end))  
           
        Thanks  
         
        
        [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-409595)
        
        *   ![](https://secure.gravatar.com/avatar/8831a54b3547afd593350025198bccb32fc03ddbf2e9fd377ce0667820b17286?s=64&d=mm&r=g) gaurav says:
            
            [January 31, 2013 at 6:50 am](https://chandoo.org/wp/calculate-vacation-days/#comment-410272)
            
            [http://www.k2e.com/tech-update/tips/143-using-two-minus-signs-in-excel](http://www.k2e.com/tech-update/tips/143-using-two-minus-signs-in-excel)
              
               
            to understand usage of double minus signs
            
            [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-410272)
            
17.  ![](https://secure.gravatar.com/avatar/4f789dbb41f59ff74bb00435308f7be7549b75310141450d1add63f41a956c95?s=64&d=mm&r=g) Kiran says:
    
    [January 28, 2013 at 9:03 am](https://chandoo.org/wp/calculate-vacation-days/#comment-409481)
    
    Hi,  
    I have tried the below formule for the 3 questions.  
    1\. How many vacations are taken in this period?  
    A: =SUMPRODUCT((vacations\[Start Date\]>=start)\*(vacations\[End Date\]<=end))  
    2\. How many vacations are taken in this period?  
    A: =SUMPRODUCT((vacations\[Start Date\]<end)\*(vacations\[End Date\]>start))  
    3\. How many distinct people took vacation in this period?  
    A: For this, i got some error when written in single cell. So i have taken one helper column. (Column E)  
    Filled the column E with '=IF((\[Start Date\]>=start)\*(\[End Date\]<=end),\[Employee Name\],"0")'  
    Used the below formula to get the answer for the question.  
    \=SUMPRODUCT(1/COUNTIF(vacations\[Column1\],vacations\[Column1\]))-1   
     
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-409481)
    
18.  ![](https://secure.gravatar.com/avatar/1423ba45a1a0f06bef3faa0dbcad9de60708856a6a9517f143edf6e1f5abab3f?s=64&d=mm&r=g) Smarty says:
    
    [January 29, 2013 at 7:41 am](https://chandoo.org/wp/calculate-vacation-days/#comment-409722)
    
    Q-1 Actule Result will be 25 from 1st Jan.12 to 31st Mar.12 with below formula  
    \=SUMPRODUCT(--(C4:C123>=start)\*(D4:D123<=end))  
       
    @-2 & Q-3  Pls clear what result u want  
       
    Smarty
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-409722)
    
19.  ![](https://secure.gravatar.com/avatar/1423ba45a1a0f06bef3faa0dbcad9de60708856a6a9517f143edf6e1f5abab3f?s=64&d=mm&r=g) Smarty says:
    
    [January 29, 2013 at 7:53 am](https://chandoo.org/wp/calculate-vacation-days/#comment-409726)
    
    How can i join this group to get & give the Solutions  
       
    Smarty
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-409726)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui](http://chandoo.org/wp/about-hui/)
         says:
        
        [January 29, 2013 at 2:10 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-409801)
        
        @Smarty  
        Start here: [http://chandoo.org/wp/welcome/](http://chandoo.org/wp/welcome/)
          
         
        
        [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-409801)
        
20.  ![](https://secure.gravatar.com/avatar/282835da5dae12b1f01e922d4a3d6f7f19bf9cc459e18a69a6064cc13cd83be6?s=64&d=mm&r=g) Naina says:
    
    [January 29, 2013 at 7:38 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-409856)
    
    1\. =COUNTIFS(vacations\[Start Date\],">="&start,vacations\[End Date\],"<="&end)  
    2\. =COUNTIFS(vacations\[Start Date\],"<="&end,vacations\[End Date\],">="&start)  
    3\. This isnt working, what am I missing? First of all, its giving me an extra ;0 in the 3rd array, and secondly, my formula isn't correct, in the sense that the match range should correspond correctly.  
    \=SUMPRODUCT(--(vacations\[Start Date\]>start),--(vacations\[End Date\]<end),IF(FREQUENCY(MATCH(vacations\[Employee Name\],vacations\[Employee Name\],0),MATCH(vacations\[Employee Name\],vacations\[Employee Name\],0))>0,1,0))  
    I guess an array would work..
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-409856)
    
21.  ![](https://secure.gravatar.com/avatar/251b8706f4cd1cd12bc6f10e61d1d730f3e1592f8533197a8d6645bbede97a9d?s=64&d=mm&r=g) [Paulo Cesar Semblano da Costa](http://www.excelvbagraficos.com.br/)
     says:
    
    [January 30, 2013 at 1:56 am](https://chandoo.org/wp/calculate-vacation-days/#comment-409924)
    
    Q3:  
    Column C in ascending order.  
    1) Column C even year:  
    M16: {=CORRESP(MÊS(start);MÊS($C$4:$C$123);0)+3}  
    M17: {=CORRESP(MÊS(end);MÊS($C$4:$C$123);1)+3}  
    M18: {=SOMA(1/CONT.SES(INDIRETO("B" & M16 & ":B" & M17);INDIRETO("B" & M16 & ":B" & M17)))}  
    2) Column C different years:  
       
    N16: {=CORRESP(DATA(ANO(start);MÊS(start);1);DATA(ANO($C$4:$C$123);MÊS($C$4:$C$123);1);0)+3}  
    N17: {=CORRESP(DATA(ANO(end);MÊS(end);1);DATA(ANO($C$4:$C$123);MÊS($C$4:$C$123);1);1)+3}  
    N18: {=SOMA(1/CONT.SES(INDIRETO("B" & N16 & ":B" & N17);INDIRETO("B" & N16 & ":B" & N17)))}  
     
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-409924)
    
22.  [Details about online Power Pivot Course | Chandoo.org - Learn Microsoft Excel Online](http://chandoo.org/wp/2013/01/30/power-pivot-course-details/)
     says:
    
    [January 30, 2013 at 8:46 am](https://chandoo.org/wp/calculate-vacation-days/#comment-409993)
    
    \[...\] Friday, we posted a home work problem for you – Calculate vacation days using formulas. There were quite a few interesting solutions in the \[...\]
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-409993)
    
23.  ![](https://secure.gravatar.com/avatar/ecf803bf2f64f9bd0f92b16e28727d39f6c9b8f4cbf5a8834a639c96c0e2465c?s=64&d=mm&r=g) [William Solera](http://no/)
     says:
    
    [January 30, 2013 at 3:16 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-410066)
    
    Question:  
    Suppose we have this 2 dates into the excel vacations file:  
    David: Start day: 25/01/2013 & End Day: 4/02/2013.  
    In this case David enjoyed 7 job days of his vacations. But also in my report i need to track how many vacations belongs to each month.   
    In this case the answer is 5 days for January and 2 days for February. But I cant figure out how  to get this with any formula.  
     Thx for the help..
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-410066)
    
24.  ![](https://secure.gravatar.com/avatar/9e746ac1bbfda8df2ecc12d220951075686cbb29d6cff973e78899983550fa15?s=64&d=mm&r=g) Manoj Choudhary says:
    
    [January 30, 2013 at 9:51 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-410150)
    
    ERROR IN THE SOLUTION XLS  
       
    Well.. i noticed this for the question2 : how many vacations are taken in this period. With the current solution, any vacation starting before 'start' and ending after 'end' is calculated twice. An alternative approach to fix this is to subtract vacations starting after the period and vacations ending before the period from the total number of vacations. Here is the formula i used :   
    \=COUNTA(vacations\[Employee Name\])-COUNTIF(vacations\[End Date\],"<"&start)-COUNTIF(vacations\[Start Date\],">"&end)
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-410150)
    
25.  ![](https://secure.gravatar.com/avatar/251b8706f4cd1cd12bc6f10e61d1d730f3e1592f8533197a8d6645bbede97a9d?s=64&d=mm&r=g) [Paulo Cesar Semblano da Costa](http://www.excelvbagraficos.com.br/)
     says:
    
    [January 31, 2013 at 9:48 am](https://chandoo.org/wp/calculate-vacation-days/#comment-410313)
    
    Q1:  
    \=CONT.SES(C4:C123;">=" & start;D4:D123;"<=" & end)  
    Q2:  
    \=CONT.SES(C4:C123;">=" & start;C4:C123;"<=" & end) + CONT.SES(C4:C123;"<" & start;D4:D123;">=" & start;D4:D123;"<=" & end)
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-410313)
    
26.  ![](https://secure.gravatar.com/avatar/d632a001b59a61782f88bee3153bbf6ed424668f82da1a7d16da8637cc12651b?s=64&d=mm&r=g) Naveen says:
    
    [February 10, 2013 at 2:07 am](https://chandoo.org/wp/calculate-vacation-days/#comment-412777)
    
    Dear Friends,  
    i need someones help to over come the issue i am facing that is i need to remove first orlast letters from the content in a cell  
    Ex.  
    HEPLANDCCRDDSUA  
    last 2 digits, UA needs to be removed  
    HOw can i do this as i need to do this for more than thousand  
    Thank you,  
    Naveen  
     
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-412777)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [February 10, 2013 at 12:52 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-412878)
        
        @Naveen  
        If it is always 2 characters  
        \=Left(A1,Len(A1)-2)
        
        Otherwise what are the rules for determining how many characters it is you want to keep
        
        [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-412878)
        
27.  ![](https://secure.gravatar.com/avatar/864bc03c0d303d01fee370b4f8d7869525c15c8862db8ddda339c4761bc0ffd7?s=64&d=mm&r=g) Raj Kumar Kothari says:
    
    [February 10, 2013 at 9:55 am](https://chandoo.org/wp/calculate-vacation-days/#comment-412853)
    
    @Navin:  
       
    You can use the following formula and drag it down till the desired amount of cells: (Please change the referencing according to your data)  
       
    **\=MID(A1,1,LEN(A1)-2)**  
    Thanks, Raj
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-412853)
    
28.  ![](https://secure.gravatar.com/avatar/4ace46bd7dcab7618f1fca2bbe414e8eda307d10ca91143f50ea94822a33a780?s=64&d=mm&r=g) benishiryo says:
    
    [February 20, 2013 at 9:57 am](https://chandoo.org/wp/calculate-vacation-days/#comment-415057)
    
    hi Chandoo.  i spotted a discrepancy in Q2's answer.  if you change C4's date to be before the Start Date & D4 to be after the End Date, the formula double counts that cell.    
    hence, maybe:  
    **\=SUMPRODUCT((vacations\[Start Date\]<start)\*(vacations\[End Date\]>=start)+(vacations\[Start Date\]>=start)\*(vacations\[Start Date\]<=end)\*(vacations\[End Date\]>end))**  
    or:  
    **\=COUNTIFS(vacations\[Start Date\],"<"&start,vacations\[End Date\],">="&start)+COUNTIFS(vacations\[Start Date\],">="&start,vacations\[Start Date\],"<="&end,vacations\[End Date\],">"&end)**  
    i love your dashboards by the way
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-415057)
    
    *   ![](https://secure.gravatar.com/avatar/5c760f7cae33e110afed3e80e7318bf2c291dc204f52ba5a9199497d4dc19d5c?s=64&d=mm&r=g) Rics says:
        
        [October 10, 2013 at 12:07 am](https://chandoo.org/wp/calculate-vacation-days/#comment-448579)
        
        Hi Benishiryo, Even I am getting incorrect answer with both the solutions provided by you. Please try below:
        
        \=J8+COUNTIFS(vacations\[Start Date\],"greater than"&start,vacations\[End Date\],"greater than equal to"&start)+COUNTIFS(vacations\[Start Date\],"less than equal to"&end,vacations\[End Date\],"greater than"&end)
        
        [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-448579)
        
    *   ![](https://secure.gravatar.com/avatar/c9ef0e94f2ceb8aaf85c613f42f31d2a65d8542df29fc36a51e37dc3fe315a40?s=64&d=mm&r=g) Bharathi says:
        
        [July 2, 2024 at 11:46 am](https://chandoo.org/wp/calculate-vacation-days/#comment-2227178)
        
        \=COUNTIFS(vacations\[Start Date\],">="&start,vacations\[Start Date\],"="&start,vacations\[End Date\],"="&start,vacations\[End Date\],"<="&end)
        
        My answer for q2
        
        [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-2227178)
        
29.  ![](https://secure.gravatar.com/avatar/5c760f7cae33e110afed3e80e7318bf2c291dc204f52ba5a9199497d4dc19d5c?s=64&d=mm&r=g) Rics says:
    
    [October 9, 2013 at 11:54 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-448576)
    
    Reg the video.. I am getting incorrect answers for the second question. if there are vacations that are on the exact start date and end date as specified as start and end.
    
    Even if one day of the vacation is between start and end dates, you should count it
    
    I am getting correct answer with following:  
    \=J8+COUNTIFS(vacations\[Start Date\],"="&start)+COUNTIFS(vacations\[Start Date\],""&end)
    
    In the video it was mentioned as following, which seems to be incorrect.  
    \=J8+COUNTIFS(vacations\[Start Date\],"="&start)+COUNTIFS(vacations\[Start Date\],"="&end)
    
    Please correct me if I am wrong.
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-448576)
    
30.  ![](https://secure.gravatar.com/avatar/db08bfe318fa21d025916eff867b3377439d8eda7ab526a46b8c5aa94e16865f?s=64&d=mm&r=g) Elkhan says:
    
    [April 8, 2014 at 8:43 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-477762)
    
    probably not the most sussinct ones, especially for the Q3:
    
    Q1==SUMPRODUCT((vacations\[Start Date\]>=start)\*(vacations\[End Date\]<=end))
    
    Q2=SUMPRODUCT((IF(((start<=vacations\[Start Date\])\*(vacations\[Start Date\]<=end))+(start<=vacations\[End Date\])\*(vacations\[End Date\]0,1,0))) CSE
    
    Q3=SUMPRODUCT(1/(COUNTIF(INDEX(vacations\[Employee Name\],MATCH(1,(vacations\[Start Date\]>=start)\*(vacations\[End Date\]=start)\*(vacations\[End Date\]=start)\*(vacations\[End Date\]=start)\*(vacations\[End Date\]<=end),0)),G8-1,0)))) CSE
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-477762)
    
31.  ![](https://secure.gravatar.com/avatar/db08bfe318fa21d025916eff867b3377439d8eda7ab526a46b8c5aa94e16865f?s=64&d=mm&r=g) Elkhan says:
    
    [April 9, 2014 at 1:53 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-477825)
    
    some rearrangements for Q3 to avoid constant referrence (1) in the MATCH function. it may be useful in case of the same task with Q2 conditions
    
    Q3=SUMPRODUCT(1/(COUNTIF(INDEX(vacations\[Employee Name\],ROWS(C4:INDEX(vacations\[Start Date\],MATCH(TRUE,vacations\[Start Date\]>=start,0))-ROW(C4)+1)):OFFSET(INDEX(vacations\[Employee Name\],ROWS(C4:INDEX(vacations\[Start Date\],MATCH(TRUE,vacations\[Start Date\]>=start,0))-ROW(C4)+1)),G8-1,0),INDEX(vacations\[Employee Name\],ROWS(C4:INDEX(vacations\[Start Date\],MATCH(TRUE,vacations\[Start Date\]>=start,0))-ROW(C4)+1)):OFFSET(INDEX(vacations\[Employee Name\],ROWS(C4:INDEX(vacations\[Start Date\],MATCH(TRUE,vacations\[Start Date\]>=start,0))-ROW(C4)+1)),G8-1,0)))) CSE
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-477825)
    
32.  ![](https://secure.gravatar.com/avatar/e768900f95173568b30c158deccb58d5974d7b9628cc9cec24ca1f8bb3fd3c94?s=64&d=mm&r=g) Daniel says:
    
    [May 22, 2014 at 10:36 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-539811)
    
    For the first two parts I had a slightly different answer, which seemed a little simplier than the given answers (they are both array formulas, and so require control-shift-enter):  
    Part 1:  
    \=SUM(IF(vacations\[Start Date\]>=start,IF(vacations\[End Date\]=start,IF(vacations\[Start Date\]<=end,1,0),0))
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-539811)
    
33.  ![](https://secure.gravatar.com/avatar/e768900f95173568b30c158deccb58d5974d7b9628cc9cec24ca1f8bb3fd3c94?s=64&d=mm&r=g) Daniel says:
    
    [May 23, 2014 at 3:57 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-540482)
    
    What is posted above is not my formula. Somehow it was muddled in the posting process. I will try again:
    
    Part1:  
    \=SUM(IF(vacations\[Start Date\]>=start,IF(vacations\[End Date\]=start,IF(vacations\[Start Date\]<=end,1,0),0))
    
    Both array formulas, use with control-shift-enter.
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-540482)
    
34.  ![](https://secure.gravatar.com/avatar/e768900f95173568b30c158deccb58d5974d7b9628cc9cec24ca1f8bb3fd3c94?s=64&d=mm&r=g) Daniel says:
    
    [May 23, 2014 at 3:59 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-540486)
    
    Muddled again. I give up.
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-540486)
    
35.  ![](https://secure.gravatar.com/avatar/6977d5b8fb31861470db30ff7e94956f9498b4c3f5acc101334453e5b41c660d?s=64&d=mm&r=g) [Bigger Don](http://bigdon-in-vbaland.blogspot.com/)
     says:
    
    [October 10, 2014 at 1:37 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-804791)
    
    hmmm...I got two out of three, and when I check the third mine result coincides with the data  
    How many vacations are taken in this period?  
    \=COUNTIFS(vacations\[Start Date\],">="&start,vacations\[End Date\],"="&start,vacations\[End Date\],"<="&end)  
    +COUNTIFS(vacations\[Start Date\],"<="&start,vacations\[End Date\],"="&start)  
    +COUNTIFS(vacations\[Start Date\],">="&start,vacations\[Start Date\],"="&end)
    
    How many distinct people took vacation in this period?  
    For this I inserted a column in the table, starting in the first row, then copying this down  
    \=IF(AND(OR(AND(\[@\[Start Date\]\]>=start,\[@\[End Date\]\]<=end),AND(\[@\[Start Date\]\]<=start,\[@\[End Date\]\]=start),AND(\[@\[Start Date\]\]>=start,\[@\[Start Date\]\]=end)),COUNTIFS(C$3:C3,"=1",B$3:B3,"=" &\[@\[Employee Name\]\])<1),1,0)
    
    Then in H19 (the answer cell) =SUM(vacations\[Column1\])
    
    That gave me 15...even hand-counted and sorted for dupes...maybe corrupted my file with a wrong date?  
    Name Start Date End Date  
    David 1 26-Jan-12 2-Feb-12  
    Lance 1 5-Feb-12 14-Feb-12  
    Vincent 1 6-Feb-12 12-Feb-12  
    Thomas 1 9-Feb-12 15-Feb-12  
    Xinhua 1 14-Feb-12 20-Feb-12  
    Mindy 1 16-Feb-12 19-Feb-12  
    Cindy 1 18-Feb-12 21-Feb-12  
    Albert 1 19-Feb-12 22-Feb-12  
    Jackie 1 24-Feb-12 4-Mar-12  
    Zack 1 29-Feb-12 3-Mar-12  
    Ganesh 1 1-Mar-12 7-Mar-12  
    Queen 1 3-Mar-12 5-Mar-12  
    Barry 1 7-Mar-12 9-Mar-12  
    Wendy 1 13-Mar-12 17-Mar-12  
    Steve 1 17-Mar-12 21-Mar-12
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-804791)
    
36.  ![](https://secure.gravatar.com/avatar/e2713ee4c7c6197e5917a8c4f6508c6bd78e7325cbb7245c9995bca4922f04d8?s=64&d=mm&r=g) Jasen says:
    
    [March 9, 2015 at 7:47 am](https://chandoo.org/wp/calculate-vacation-days/#comment-926634)
    
    Not a fan of array formulas but the task was fairly small so no impact.  
    \={SUM(1/COUNTIF(INDIRECT(ADDRESS(MATCH(start,vacations\[Start Date\])+4,2,1,1)&":"&ADDRESS(MATCH(end,vacations\[End Date\])+3,2,1,1)),INDIRECT(ADDRESS(MATCH(start,vacations\[Start Date\])+4,2,1,1)&":"&ADDRESS(MATCH(end,vacations\[End Date\])+3,2,1,1))))}
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-926634)
    
37.  ![](https://secure.gravatar.com/avatar/ffc701a3c1060e6b93a400ff058c7e34b0818044748120eed3f261a8ca8be969?s=64&d=mm&r=g) The Imposter says:
    
    [May 7, 2015 at 3:28 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-967755)
    
    1\. Answer=COUNTIFS(vacations\[Start Date\],">="&start,vacations\[End Date\],"<="&end)  
    2\. Answer=COUNTIFS(vacations\[Start Date\],"="&start)  
    3\. I used 2 helper columns - one to test the vacation dates and enter the name of employee and the other to count the employee if it was unique and ignore blank space and duplicate employee names.
    
    column1=IF(AND(\[@\[Start Date\]\]>=start,\[@\[End Date\]\]<=end),\[@\[Employee Name\]\],"")  
    column2 =IF(\[@Column1\]="",0,IF(COUNTIF($E$1:E3,\[@Column1\])=0,1,0))  
    Answer=SUM(vacations\[Column2\])
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-967755)
    
38.  ![](https://secure.gravatar.com/avatar/f1ee325a009224245d63b3b665115072610d8d1f4ca784ead62e979236cfc328?s=64&d=mm&r=g) Anouk says:
    
    [August 14, 2015 at 8:29 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-1023741)
    
    I am not sure if this has already been addressed but here goes:
    
    I am tracking vacation taken by employees. I want to be able to tell if there is a vacation conflict between two people from the same departement.  
    Also, since they are not required to take all their days at once, I have set up 4 vacation periods per person.
    
    John -- Acct 7/1 - 7/20  
    Bob -- Sales 7/5 - 7/25  
    Evan -- Acct 7/5 - 7/25  
    I would like for John and Bob's names and vacation days get highlighted to show conflict.
    
    Thank you in advance
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-1023741)
    
39.  ![](https://secure.gravatar.com/avatar/895397eac998e35a25c52718f7feed266ef98d7ebf87d0c6d51673baa6749485?s=64&d=mm&r=g) Mokshi says:
    
    [October 1, 2015 at 5:59 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-1054841)
    
    Took a long time to figure out 3. These are the formulas I have used.  
    1\. =COUNTIFS(vacations\[Start Date\],">="&start,vacations\[End Date\],"<="&end)  
    2\. =COUNTA(vacations\[Employee Name\])-COUNTIFS(vacations\[End Date\],""&end)  
    3\. Used a helper column (column E) which populates with a "N" if the start and end dates of vacations do not fall within the specified date range. It populates the first within-range instance of a recurring person with a "Y". Any subsequent vacation occurences by the same person are populated with a "N".
    
    Formula in helper:  
    \=IF(AND(COUNTIFS($B$3:B3,\[@\[Employee Name\]\],$E$3:E3,"="&"Y")=0,\[@\[Start Date\]\]>=start,\[@\[End Date\]\]<=end),"Y","N")
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-1054841)
    
40.  ![](https://secure.gravatar.com/avatar/7a80d88df8b0ff8c5361bb6bf4c2baa17b55d53089ab60cbe1b138e96d8ba468?s=64&d=mm&r=g) Chander says:
    
    [October 3, 2016 at 9:17 am](https://chandoo.org/wp/calculate-vacation-days/#comment-1302480)
    
    Don't you think, the below formula works for the question no. 2  
    \=COUNTIFS(vacations\[End Date\],">="&start,vacations\[Start Date\],"<="&end)
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-1302480)
    
41.  ![](https://secure.gravatar.com/avatar/22eb483a2e0cfe6363342a7dcd1a471bf947d5dfe2b9440e3b883479f2c4366e?s=64&d=mm&r=g) Rojo Loco says:
    
    [February 26, 2017 at 6:25 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-1413816)
    
    Counting Unique Values is a very, very useful skill. I use a countif with a fixed and non-fixed array then use the "1" values to determine which are "new unique values."
    
    \=IF(\[@\[Vacation Name\]\]="","",(COUNTIF($K$4:K4,K4)))
    
    the sample output is:
    
    Vacation Name Unique Count?
    
    Lance 1  
    Vincent 1  
    Thomas 1  
    Vincent 2  
    Xinhua 1  
    Mindy 1  
    Cindy 1  
    Albert 1  
    Jackie 1  
    Zack 1  
    Ganesh 1  
    Queen 1  
    Barry 1  
    Queen 2  
    Jackie 2  
    Xinhua 2  
    Wendy 1  
    Albert 2  
    Thomas 2  
    Steve 1
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-1413816)
    
42.  ![](https://secure.gravatar.com/avatar/5de9ebf4b9c5b50fa4f3202f6ab3d28c593584b78f77aa075b41513d1fcad9df?s=64&d=mm&r=g) licwill says:
    
    [May 29, 2017 at 6:23 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-1454381)
    
    Greetings.
    
    For Q1 I use Column M to set this formula  
    \=IF(AND(C4>=$K$3,D4=$K$3,C4=$K$3,D4<=$K$4)),1,0)  
    Then I just autoSum the Column
    
    For Q3 I use the results from Column M and I just extracted the name values with this formula =IF(M4=0,"",B4) in Column O. With just the names of the people who took a vacation during that period, I just copy, special paste, and applied Data tools-Remove duplicates. This allowed me to count the people on vacation during that period.
    
    Thanks. Good Challenge.
    
    My way just showed you all that there are at least 100 ways to evaluate something in Excel, you just need the proper logic.
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-1454381)
    
43.  ![](https://secure.gravatar.com/avatar/9dc7ff6ddbdfa23a5304c6b278e705fe3636ed03071e5fba15db335a91bf4da8?s=64&d=mm&r=g) Yves S says:
    
    [November 30, 2017 at 3:37 am](https://chandoo.org/wp/calculate-vacation-days/#comment-1525335)
    
    Q1: there are several ways to display the response. all have been posted before:  
    A1-1=COUNTIFS(vacations\[Start Date\],">="&start,vacations\[End Date\],"=start)\*(vacations\[End Date\]=start),--(vacations\[End Date\]<=end))
    
    Q2: same answer by simply changing start and end around.  
    A2-1 =COUNTIFS(vacations\[Start Date\],"="&start)  
    A2-2 and A2-3 follow above
    
    Q3: I really like Mitch's solution. I came to the same after a few iterations.  
    A3 ={SUMPRODUCT(IFERROR(1/COUNTIFS(vacations\[Employee Name\],vacations\[Employee Name\],vacations\[Start Date\],">="&start,vacations\[End Date\],"=start)\*(vacations\[End Date\]<=end))}
    
    theory: if an event is counted more than once in a sample, then SUM(1/COUNT(events)) = 1. For example, an event counted 3 times will post as 1/3; 1/3; 1/3 with SUM(1/3,1/3,1/3) = 1
    
    Note on SUMPRODUCT: One can replace the "\*" multiplier by comma "," and using the double negative "--".  
    The "--" replaces TRUE and FALSE by 1 and 0. Use "\*" to "multiply" arrays when performing SUMPRODUCT on TRUE and FALSE; use "," array separator when performing SUMPRODUCT on 1s and 0s.
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-1525335)
    
44.  ![](https://secure.gravatar.com/avatar/2c4958fddfef5f4263082bcac054d349409f1007e17e77dea286373e3992052f?s=64&d=mm&r=g) camel says:
    
    [June 5, 2018 at 12:19 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-1551300)
    
    Alternative Solution:
    
    1\. =SUMPRODUCT(--($C:$C>start),--($D:$D<end))
    
    2\. = SUMPRODUCT(--($C:$Cstart))
    
    3\. I hate helper columns. I have yet to figure it out how.
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-1551300)
    
45.  ![](https://secure.gravatar.com/avatar/ae62de078836c5ddd0554928a57f1b6903c05da4cc7df7fcce0bf362e396ea91?s=64&d=mm&r=g) David says:
    
    [August 28, 2018 at 5:00 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-1570846)
    
    Hi there, I think you have an error on the "How Many vacations are taken in this period.  
    If the holiday start date is pre the range and the holiday end date is post the range the formula calculates this as 2 holidays. If you do have a correct formula for this calculation I would be grateful as I have exactly the same issue. Many Thanks
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-1570846)
    
46.  ![](https://secure.gravatar.com/avatar/0832a1379aa9c50a257d82264ef57094d63303e734665b41b24bbf35cf7ec269?s=64&d=mm&r=g) Cleber Marrara says:
    
    [October 23, 2018 at 11:14 am](https://chandoo.org/wp/calculate-vacation-days/#comment-1583220)
    
    I did it in a simple way and it worked.  
    Note: My excel is in portuguese pt-br  
    Q1: =CONT.SES(C:C;">="&start;D:D;"<="&end)  
    Q2: =CONT.SES(C:C;"="&start)  
    Q3: I've just copied the answer. I confess I would've never thought about the solution given.
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-1583220)
    
47.  ![](https://secure.gravatar.com/avatar/b2f22c373ec32da576d708a2e1a86a357791a24ebc85fad9994d17cc0e5bd9f9?s=64&d=mm&r=g) christie says:
    
    [June 16, 2019 at 3:46 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-1659033)
    
    Hello
    
    Could someone tell me how to solve Q2 in below workbook
    
    [https://chandoo.org/wp/calculate-vacation-days/](https://chandoo.org/wp/calculate-vacation-days/)
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-1659033)
    
48.  ![](https://secure.gravatar.com/avatar/f8e0f5f65bd0b97469853fac9bb1303733c5486e9fdb7268241978091aa38d43?s=64&d=mm&r=g) VPSD says:
    
    [May 10, 2022 at 7:07 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-2076894)
    
    I am a beginner so, I assume my solution is simpler and understandable by all. I used helper columns and some basic formulas like: counta, if(), unique() ect...
    
    Here is the link:  
    [https://docs.google.com/spreadsheets/d/1gTfTYeLI5b6IBgApZRS0seB4A6qCvFdg/edit?usp=sharing&ouid=104412430299715464739&rtpof=true&sd=true](https://docs.google.com/spreadsheets/d/1gTfTYeLI5b6IBgApZRS0seB4A6qCvFdg/edit?usp=sharing&ouid=104412430299715464739&rtpof=true&sd=true)
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-2076894)
    
49.  ![](https://secure.gravatar.com/avatar/37bff848bbd4a4b659b727247f27b928cb0027d767394bb0e02d1b538a4b769a?s=64&d=mm&r=g) Max says:
    
    [December 7, 2023 at 6:17 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-2155818)
    
    I think I did well for the most part. Last question was a bit of a hassle but it works and it's adaptable.
    
    Q1: =COUNTIFS(vacations\[Start Date\],">=1-Feb-12",vacations\[End Date\],"=1-Feb-12",vacations\[Start Date\],"=start)\*(vacations\[End Date\]<=end)  
    Column F's Formula: =IF(E9=0," ",vacations\[@\[Employee Name\]\])  
    Column G's Formula:=UNIQUE(F9:F28)  
    Column H's Formula:=COUNTIF(G9#,"\*")
    
    Make the 1's and 0's array, use the if to print each name with a 1, use the unique function to get each unique name, and countif with wildcard to count the number of unique names
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-2155818)
    
50.  ![](https://secure.gravatar.com/avatar/683325fc3a15164fedf72314ccb5442f643a2a8b936a910b59dc9012d7b9e469?s=64&d=mm&r=g) Jurijs says:
    
    [January 3, 2024 at 8:15 am](https://chandoo.org/wp/calculate-vacation-days/#comment-2161747)
    
    Nice solution, but it will make some errors!!!
    
    Try start date in the table vacations end date.
    
    I've tried with Thomas: strart date 23-JAN end date 27-JAN, just change end date to 27-MAY so the answers are:  
    q1 - without changes - however it shoud be so, becauses vacation didn't start in required time frame.  
    q2 - ansewr is 24 - and that is wrong.  
    q3 - without changes - it's correct, but should be aware, key word here is "took vacation", and if you are interested in how many people were in vacation it will not give you correct answer!
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-2161747)
    
51.  ![](https://secure.gravatar.com/avatar/9661aa320d3f98a86ae0022c52eee8bd0b19c40c66cdecb9193c473163f04f79?s=64&d=mm&r=g) YOKESWARAN S says:
    
    [May 30, 2024 at 3:00 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-2216575)
    
    q1:=COUNTIFS(vacations\[Start Date\],">=01-02-2012",vacations\[End Date\],"=01-02-2012",vacations\[Start Date\],"  
    \=IF(AND(B4>=DATE(2012,2,1),B4 =COUNTIFS($D$4:D4,D4,$D$4:D4,"NA")
    
    q3:=COUNTIF(vacations\[dummy 2\],1)
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-2216575)
    
52.  ![](https://secure.gravatar.com/avatar/3c99caac920672f98fed3ead24b439974143a343ddb03a32eda5807d8999510b?s=64&d=mm&r=g) Sebastian says:
    
    [March 5, 2025 at 9:04 am](https://chandoo.org/wp/calculate-vacation-days/#comment-2369433)
    
    Q1: =COUNTIFS(vacations\[Start Date\], ">="&start, vacations\[End Date\], "="&start, vacations\[End Date\], "=start)\*(vacations\[End Date\]<=end))))
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-2369433)
    
53.  ![](https://secure.gravatar.com/avatar/bf25d23864cd52b34adb34a9beb4d270e880b188ae163ed5a3b9e384442f9bc0?s=64&d=mm&r=g) William says:
    
    [June 25, 2025 at 2:59 pm](https://chandoo.org/wp/calculate-vacation-days/#comment-2410561)
    
    Q1: =COUNTA(FILTER(B:B,(C:C>$K$3)\*(D:D=" & start,C:C,"<=" & end)+COUNTIFS(D:D,"=" & start)-COUNTIFS(C:C,">=" & start,D:D,"$K$3)\*(D:D<$K$4))))
    
    [Reply](https://chandoo.org/wp/calculate-vacation-days/#comment-2410561)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/calculate-vacation-days/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Designing a dashboard to track Employee vacations \[case study\]](https://chandoo.org/wp/employee-vacations-tracker-dashboard/) | [Introduction to DAX Formulas & Measures for Power Pivot](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)