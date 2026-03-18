# Random Group Generator Template [Free Download]

**Source:** https://trumpexcel.com/random-group-generator-template

---

[Skip to content](https://trumpexcel.com/random-group-generator-template/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/random-group-generator-template/#below-title)

If you’re a teacher or a trainer, creating groups of students/participants is a common task. For example, you may want to create groups to conduct a quiz or a team building activity.

And in most of the cases, you need these groups to be random.

Today, I am sharing a random group generator template that will make it super easy for you to create a group of students/participants.

All you need is the list of students or participants and specify how many groups you want to create.

![Random Group Generator Template - Cover](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20760%20250'%3E%3C/svg%3E)

Random Group Generator Template
-------------------------------

Here is a demo of how this random group generator (or random team generator) template works:

![Random Group Generator Template - Demo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20780%20379'%3E%3C/svg%3E)

The list of students/participants is in A2:A17. If you have a longer list, simply add the names in it.

Cell E2 has the number of groups that you want to create. Based on the number you enter, you would get the groups and the names in each group in columns G to P. As of now, I have created it this template for a maximum of 10 groups.

Once you have entered the number of groups you want in cell E2, click on the ‘Create Teams’ button to randomly generate the groups of names.

[**Download the Random Group Generator Template**](https://www.dropbox.com/s/jch89p4xxbigzxy/Random-Team-Generator-Template.xlsm?dl=1)

### How this Excel Template Works

There are a couple of cool Excel features and a few helper columns that make this random group generator template in Excel.

Here is how it is made:

*   A2:A17 contains the list of names that are to be grouped randomly.
    *   A1:C17 has been converted into an [Excel Table](https://trumpexcel.com/excel-table/)
        . This helps to keep the formulas intact when you add/remove names from the list.![Random Group Generator Template - Excel Table](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20777%20372'%3E%3C/svg%3E)
*   Column B has the [formula](https://trumpexcel.com/excel-functions/)
    : \=[RANDBETWEEN](https://trumpexcel.com/excel-randbetween-function/)
    (1,[COUNTA](https://trumpexcel.com/excel-functions/counta-function/)
    (\[Names\])) + [ROW](https://trumpexcel.com/excel-row-function/)
    ()/100
    *   The function returns a random number between 1 and the total number of names in the list (using the COUNTA function). To this, ROW()/100 is added to make it unique (as the RANDBETWEEN function can spit out duplicates as well).![Random Group Generator Template - unique](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20684%20407'%3E%3C/svg%3E)
*   Cell C2 has the formula: \=[RANK](https://trumpexcel.com/excel-rank-function/)
    (\[@Unique\],\[Unique\])
    *   This function gives the rank for each value in Column B. Since all the values in column B are unique, this formula gives a unique list of integers that vary from 1 to the total number of names in the list.![Random Group Generator Template - rank](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20680%20404'%3E%3C/svg%3E)
*   Cell G1 has the formula: \=[IF](https://trumpexcel.com/excel-if-function/)
    ([COLUMNS](https://trumpexcel.com/excel-columns-function/)
    ($G$1:G1)>$E$2,””,COLUMNS($G$1:G1))
    *   The same formula is copied in cells H1 to P1. It returns the number of columns between column G and the current column. Hence, G1 gets 1, H1 gets 2 and so on. It also checks whether the number is greater than the value in cell E2. If yes, then it returns a blank.![Random Group Generator Template - Group Number](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20692%20406'%3E%3C/svg%3E)
*   Cell G2 has the formula: \=IFERROR(IF(G$1<>””,[INDEX](https://trumpexcel.com/excel-index-function/)
    (Table1\[Names\],INDEX(Table1\[Rank\],G$1+$E$2\*(ROWS($F$2:F2)-1))),””),””)
    *   It is copied to all the cells in G2:P17.
        *   In cell G2, this formula will pick up the rank from C2 and return the name at that position in the list.
        *   In cell G3, it will pick the rank from C6 (which is 1 + 1\*4, where 4 is the number of groups to be formed).
        *   In cell G4, it will pick the rank from C10 (which is 1 + 2\*4, where 4 is the number of groups to be formed).
    *   If the cell in the first row is empty or the result of the formula is an error, it returns a blank.![Random Group Generator Template - Team Member](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20773%20308'%3E%3C/svg%3E)

Since RANDBETWEEN function is [volatile](https://trumpexcel.com/excel-volatile-formulas/)
, it will automatically refresh every time you make a change in the worksheet. This may be undesirable as it will change the grouping every time.

To avoid this:

*   Go to File Options.
*   In the Excel Options dialog box, select formulas in the pane on the left.
*   In the Calculation options, make Workbook Calculation Manual.![Random Group Generator Template - Manual](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20585%20304'%3E%3C/svg%3E)
*   Click OK.

Now the worksheet would not refresh until you force a refresh by hitting the F9 key.

But to make it look better, there is an orange button that does the refresh when you click it. There is a one-line [VBA code](https://trumpexcel.com/excel-vba/)
 at play here that gets executed whenever you click the button.

Here is how to insert this button:

*   Go to Developer –> Code –> Visual Basic. (You can also use the keyboard shortcut Alt + F11).![Random Group Generator Template - VB](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20632%20139'%3E%3C/svg%3E)
*   In the VB Editor right-click on any of the objects for the workbook and go to Insert –> Module.![Random Group Generator Template - Insert Module](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20430%20350'%3E%3C/svg%3E)
*   In the module code window, copy-paste the following code:
    
    Sub Refresh()
    Worksheets("Team Generator").Calculate
    End Sub
    
    *   Note that the name of the worksheet is in double-quotes. If your worksheet name is different, change it in the code.![Random Group Generator Template - Code](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20606%20222'%3E%3C/svg%3E)
*   Close the VB Editor.
*   Go to Insert –> Shapes and insert any shape that you want as the button.![Random Group Generator Template - Shape insert](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20455%20261'%3E%3C/svg%3E)
*   Right-click on the shape and click on Assign Macro.![Random Group Generator Template - Assign Macro](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20233%20245'%3E%3C/svg%3E)
*   In the Assign Macro dialog box, select the macro name and click on OK.![Random Group Generator Template - Select Macro](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20381%20371'%3E%3C/svg%3E)
*   Format the button the way you want.

Now when you click on the button, the worksheet would recalculate and you would get a new grouping based on the number of groups you have specified.

[**Download the Random Group Generator Template**](https://www.dropbox.com/s/jch89p4xxbigzxy/Random-Team-Generator-Template.xlsm?dl=1)

**Other Excel Templates You May Like:**

*   [Employee Leave/Vacation Tracker Template](https://trumpexcel.com/excel-leave-tracker/)
    .
*   [Employee Timesheet Calculator](https://trumpexcel.com/excel-timesheet-calculator-template/)
    .
*   [Excel To Do Lists Templates](https://trumpexcel.com/excel-to-do-list-template-download/)
    .
*   [A collection of FREE Excel Templates](https://trumpexcel.com/free-excel-templates/)
    .
*   [Random Group / Team Generator](https://trumpexcel.com/tools/random-team-generator/)
     (Free Tool)

**You may also like the following Excel tutorials:**

*   [How to Generate Unique Random Numbers in Excel](https://trumpexcel.com/generate-unique-random-numbers-in-excel/)
    .
*   [How to Run a Macro in Excel](https://trumpexcel.com/run-a-macro-excel/)
    .
*   [How to Create an Excel Dashboard](https://trumpexcel.com/creating-excel-dashboard/)
    .
*   [How to Rank within Groups in Excel](https://trumpexcel.com/rank-within-groups-excel/)
    
*   [How to Shuffle a List of Items/Names in Excel? 2 Easy Formulas!](https://trumpexcel.com/shuffle-list-excel/)
    
*   [Create All Possible Combinations from Lists in Excel](https://trumpexcel.com/create-all-combinations-from-lists-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

25 thoughts on “Random Group Generator Template \[FREE Download\]”
------------------------------------------------------------------

1.  I need to add columns like, Last name, email address, Gender, City, and two more columns. Can you please guide me on how to work on the VBA so that I can use your template?
    
    [Reply](https://trumpexcel.com/random-group-generator-template/#comment-14402)
    
2.  Is there any way to increase the max number of groups? I really need 15 groups! Please help… would be so great to use in my classroom.
    
    [Reply](https://trumpexcel.com/random-group-generator-template/#comment-13320)
    
3.  I am sorry but the random team generator isn’t working correctly. It will pull duplicates about every 8th run. Conditional format for dups and you will see. Can it be fixed? I have trying but to no avail. Please advise. M
    
    [Reply](https://trumpexcel.com/random-group-generator-template/#comment-12351)
    
4.  Thank you …i almost got here myself but couldn’t figure put how to add the names to the teams…awesome!
    
    [Reply](https://trumpexcel.com/random-group-generator-template/#comment-12134)
    
5.  Thanks for the template! Is there a way to specify that I would want to have my samples distributed randomly across three groups (A,B,C) but have e.g. 80% of them in group-A, 10% in group-B and 10% in group-C?
    
    [Reply](https://trumpexcel.com/random-group-generator-template/#comment-12086)
    
6.  Doesnt work, can anyone help. Why does the formual reference cell F if there is nothing in it?
    
    [Reply](https://trumpexcel.com/random-group-generator-template/#comment-11909)
    
7.  You can help me to create a specific random match, is for a sport team, 6 teams with 3 members i need matching with rival teams and similar weight for the member or very close weight , please i pay you
    
    [Reply](https://trumpexcel.com/random-group-generator-template/#comment-11839)
    
8.  This is a great tool. However I tried modifying it. But could’nt.
    
    I just need 1 Team where I need to mention the no of members in cell E2 and it creates a team with Random Names. I am confident its a piece of cake for you.
    
    [Reply](https://trumpexcel.com/random-group-generator-template/#comment-11167)
    
9.  Absolutely perfect but I need the absent function to work. I would love to this to randomly select 3 or 4 ball groups of golfers whilst we are on the tee. However we are never sure who is going to turn up hence the need to mark golfers absent from the master list and randomise the selection of the players who are there. Can anyone help???
    
    [Reply](https://trumpexcel.com/random-group-generator-template/#comment-10917)
    
10.  Sorry this does not work very well.  
    I have 40 teams and they have to be paired this goes no where needed for this program to work.
    
    [Reply](https://trumpexcel.com/random-group-generator-template/#comment-10833)
    
11.  Hey there,  
    Loved this!  
    i ended up making a few alterations of my own, namely, put the generating function into VBA so that it stopped updating all the time, I added some arrows to increase/decrease the number of groups with a single click and also made a ‘secret’ tab where you could specify two people you didn’t want in the same group. I’d be happy to share it if you’re interested.
    
    [Reply](https://trumpexcel.com/random-group-generator-template/#comment-9885)
    
    *   Hi Steve,  
        Please do share how you worked on “secret” tab.
        
        [Reply](https://trumpexcel.com/random-group-generator-template/#comment-13901)
        
12.  Is there a way to set group 1 to have 10 members, and the others to have like 7 ?
    
    [Reply](https://trumpexcel.com/random-group-generator-template/#comment-9305)
    
13.  Cool trick, but i have one scenario. let’s say i have names(2 or more) that cannot be teamed together,is there any way to solve it?
    
    [Reply](https://trumpexcel.com/random-group-generator-template/#comment-8947)
    
14.  Hi Sumit!  
    This is amazing for my classroom thanks so much!  
    Is there any way to increase the max number of groups? I really need 12 groups!
    
    [Reply](https://trumpexcel.com/random-group-generator-template/#comment-8705)
    
15.  Dear Sumit,
    
    I really enjoy using your random group generator for my classes (I created a tab for each class. It’s swift and easy to use.
    
    Sometimes, however someone in a class is absent (visit to the dentist, etc.).  
    If so, I have to alter the table, to remove the absent student.
    
    It would be nice if there could be a column next to the student names where I could mark the absent student(s) (for example with a zero) , so he/she won’t be displayed in the generated groups.
    
    Unfortunately I don’t have the programming skills to make that happen.
    
    Someone else perhaps?
    
    Greetings,  
    Willem  
    (Netherlands)
    
    [Reply](https://trumpexcel.com/random-group-generator-template/#comment-7535)
    
    *   Thanks Willem.. Glad you liked it.
        
        Here is a link to a new template that will allow you to mark a student as absent: [https://www.dropbox.com/s/ys1mmwmbdy7eeb5/Random-Team-Generator-Template%20Absent.xlsm?dl=0](https://www.dropbox.com/s/ys1mmwmbdy7eeb5/Random-Team-Generator-Template%20Absent.xlsm?dl=0)
        
        [Reply](https://trumpexcel.com/random-group-generator-template/#comment-8542)
        
        *   Hi Sumit!  
            This is amazing for my classroom thanks so much!  
            Is there any way to increase the max number of groups? I really need 12 groups!
            
            [Reply](https://trumpexcel.com/random-group-generator-template/#comment-8675)
            
        *   Hello… there is something wrong with the absent function in the worksheet…Even if I indicate that the student is absent, his name will still show in the generated teams list… Also, is there anyway to group 40 people into 2 groups… it seems that the template doesn’t support such a function… thanks and keep up the good work! 🙂
            
            [Reply](https://trumpexcel.com/random-group-generator-template/#comment-9575)
            
        *   Hello, I was searching for an excel template to create random 4 man teams when I happened upon your template. I downloaded it and tested what I am trying to accomplish, but was having trouble when I found the above link. It gets me a step closer to what I am wanting to do, however, I am trying to accomplish the opposite. I have a list of 71, but I only want to include those I identify as opposed to excluding those that are identified. And I want the teams to be in multiples of 4, but I think if I identify the total number of teams, the template will provide me with teams of 3 or 4. So, I am wondering if a template is available that would provide the capability to include vs exclude? Thanks in advance for your help. Andy.
            
            [Reply](https://trumpexcel.com/random-group-generator-template/#comment-11612)
            
16.  Thanks to both of you, Sumit and Rudra!  
    Sumit, I enjoy your formulabased random generator. I have my ovn VBA-generator that I will continue using,but I learned a lot from your reallønn Nice formulas.
    
    Rudra! I’ve never notised the easy way of changing calculation mode. I still miss a warning light when ExCeL is in manual mode. Forgetting to return to aut. Mode has caised me lot f extra work.
    
    [Reply](https://trumpexcel.com/random-group-generator-template/#comment-3382)
    
    *   From the Custom Quick Access Toolbaar, add “Manual” to the Quick Access Toolbaar and it will show when in Manual mode.
        
        [Reply](https://trumpexcel.com/random-group-generator-template/#comment-3399)
        
        *   Thanks Hennie, I’ve already adferd it to QAT.
            
            [Reply](https://trumpexcel.com/random-group-generator-template/#comment-3408)
            
17.  Cool trick Sumit. Thanks for sharing. However there is a short cut to change calculation from ribbon itself. Just go to formula ribbon and click on Calculation Option.
    
    [Reply](https://trumpexcel.com/random-group-generator-template/#comment-3378)
    
    *   Thanks for sharing Rudra.. That’s definitely the faster way to do this.
        
        [Reply](https://trumpexcel.com/random-group-generator-template/#comment-3379)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/random-group-generator-template/#respond)

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