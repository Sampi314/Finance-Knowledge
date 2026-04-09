# How many people used their entire sick leave entitlement? [Power Query / Excel homework] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/sick-leave-usage-problem

---

How many people used their entire sick leave entitlement? \[Power Query / Excel homework\]
==========================================================================================

[Excel Challenges](https://chandoo.org/wp/category/excel-challenges/)
 - 18 comments

  

I have a big day tomorrow. We are celebrating our kids (Nishanth & Nakshatra) 9th birthday this weekend. We (Jo & I) must have been possessed by demons, for we are hosting the party at our home. 12 kids (half of each kind) will be invading our house for a couple of hours. There will be balloons to blow, cakes to bake, decorations to dangle, meals to make, children to cheer, guests to greet, dishes to wash, carpets to clean, walls to varnish, furniture to fix and Chandoo to calm.

So let’s keep this quick and simple. I want you to figure out an elegant and simple way to answer below questions.

![Sick leave entitlement vs usage - Excel problem](https://chandoo.org/wp/wp-content/uploads/2018/09/sick-leave-problem-pq.png)

Imagine you are the HR analyst at BigLargeCompany. You need to find out whether staff at BLC (BigLargeCompany you silly) use up their full sick leave entitlement.

You have two tables – emps & leaves as illustrated below.

![sample data - sick leave entitlement vs. usage](https://chandoo.org/wp/wp-content/uploads/2018/09/sick-leave-usage-problem-sample-data.png)

Your mission is to find out answers to below questions.

*   How many employees used **exactly** 100% of their entitled sick leave?
*   How many employees did not take any sick leaves?
*   Listing of all employees who used 100% of their entitlement

Use either Power Query, Excel formulas or any other technique to answer the questions.

[**Please download sample data for this exercise here**](https://chandoo.org/wp/wp-content/uploads/2018/09/sick-leave-problem.xlsx)
.

Once you have answers, post them in comments section.

**Want more problems?** Check out [Excel homework section](https://chandoo.org/wp/tag/homework/)
 for some very tricky, interesting challenges.

Talk to you soon. If you need me, I will be scraping ketch up off carpets.

Update: Solution is here
------------------------

If you want to learn how to solve problems like this, check out the [**Entitlement vs. usage analysis – solution**](https://chandoo.org/wp/entitlement-vs-usage-power-query/)
 page.

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
| Written by Chandoo  <br>Tags: [Excel for HR](https://chandoo.org/wp/tag/excel-for-hr/)<br>, [homework](https://chandoo.org/wp/tag/homework/)<br>, [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)<br>, [power query](https://chandoo.org/wp/tag/power-query/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 18 Responses to “How many people used their entire sick leave entitlement? \[Power Query / Excel homework\]”

1.  ![](https://secure.gravatar.com/avatar/d4a39a29ba251034f960a5e17b104a974f23ec9d9afdf2dc5ae6b92b3081e062?s=64&d=mm&r=g) Chihiro says:
    
    [September 21, 2018 at 4:57 pm](https://chandoo.org/wp/sick-leave-usage-problem/#comment-1576701)
    
    PQ - On leaves, Group by \[Emp ID\] and aggregate \[Days used\] by sum.  
    Left Join to emps.  
    Add custom column.  
    \= try \[Days used\]/\[Entitlement\] otherwise 0
    
    Then use pivot table(s) to summarize (using slicers). Alternately use custom functions to aggregate data to return single value (Table.SelectRows, Table.RowCount).
    
    If you have PowerPivot (DAX) available. There are number of ways to set up model for this data. 1 & 2 are preferable over 3.  
    1\. Create single flat table as above. Use DAX measures and cube functions to summarize.  
    2\. Create 2 separate dimension from emps, 1 for unlimited entitlement and another for limited entitlement. Report using multiple visual/pivottable.  
    3\. Load both to model after Group by operation. Add calculated columns to leave table to handle unlimited entitlement.
    
    [Reply](https://chandoo.org/wp/sick-leave-usage-problem/#comment-1576701)
    
    *   ![](https://secure.gravatar.com/avatar/d4a39a29ba251034f960a5e17b104a974f23ec9d9afdf2dc5ae6b92b3081e062?s=64&d=mm&r=g) Chihiro says:
        
        [September 21, 2018 at 8:11 pm](https://chandoo.org/wp/sick-leave-usage-problem/#comment-1576723)
        
        Here's DAX solutions using model based on option 2.
        
        No absence:  
        No Abs:=COUNTROWS(Unlimited)+COUNTROWS(Limited)-COUNTROWS('leaves')
        
        Exactly 100%:  
        Count Exact:=COUNTX(FILTER('leaves',RELATED(Limited\[Emp ID\])BLANK()),IF(\[Days used\]/RELATED(Limited\[Entitlement\])=1,1,Blank()))
        
        100% & Over Count:  
        Count 100% and Over:=COUNTX(FILTER('leaves',RELATED(Limited\[Emp ID\])BLANK()),IF(\[Days used\]/RELATED(Limited\[Entitlement\])>=1,1,Blank()))
        
        For the list, used Pivot Table (you can use CONCATENATEX... but that'd make it hard to read).
        
        [Reply](https://chandoo.org/wp/sick-leave-usage-problem/#comment-1576723)
        
        *   ![](https://secure.gravatar.com/avatar/d4a39a29ba251034f960a5e17b104a974f23ec9d9afdf2dc5ae6b92b3081e062?s=64&d=mm&r=g) Chihiro says:
            
            [September 21, 2018 at 8:14 pm](https://chandoo.org/wp/sick-leave-usage-problem/#comment-1576724)
            
            For some reason, "=" between RELATED() and BLANK() was removed from measure. You'll need it for it to work.
            
            [Reply](https://chandoo.org/wp/sick-leave-usage-problem/#comment-1576724)
            
2.  ![](https://secure.gravatar.com/avatar/a1f7acf2bbc01a19273378d2791017b7d251be8bfe1b6b93ee46dffa59d85f8d?s=64&d=mm&r=g) Tim Weldon says:
    
    [September 21, 2018 at 6:31 pm](https://chandoo.org/wp/sick-leave-usage-problem/#comment-1576708)
    
    21, 10, 67
    
    [Reply](https://chandoo.org/wp/sick-leave-usage-problem/#comment-1576708)
    
3.  ![](https://secure.gravatar.com/avatar/7fb61c992da223614bc5173e24446a03b43da6fa68b30a9a8eb4533d057bdfcd?s=64&d=mm&r=g) [Taranjit Singh](http://na/)
     says:
    
    [September 21, 2018 at 7:02 pm](https://chandoo.org/wp/sick-leave-usage-problem/#comment-1576712)
    
    How many employees used exactly 100% of their entitled sick leave? = 21.  
    How many employees did not take any sick leaves? = 10.  
    Listing of all employees who used 100% of their entitlement = EMP IDs - 35, 77, 78, 273, 276, 281, 301, 316, 338 & 416.
    
    [Reply](https://chandoo.org/wp/sick-leave-usage-problem/#comment-1576712)
    
4.  ![](https://secure.gravatar.com/avatar/4cdf8c8300564d8c2e85bc91d8d7912cf28f9e2946ab40558aa185f49e577404?s=64&d=mm&r=g) Fowmy says:
    
    [September 21, 2018 at 7:48 pm](https://chandoo.org/wp/sick-leave-usage-problem/#comment-1576719)
    
    I used PQ to solve the problem
    
    File link: [https://1drv.ms/x/s!AmoScH5srsIYvRntB\_Cm\_U53nFh2](https://1drv.ms/x/s!AmoScH5srsIYvRntB_Cm_U53nFh2)
    
    1\. Leave used exactly 100% : 21  
    2\. Didn't take any leave : 10  
    3\. Used 100% of the entitlement : 67
    
    List (5,7,12,30,32,34,43,50,61,79,89,90,91,93,101,103,104,105,119,128,131,139,141,150,157,170,175,176,177,178,179,186,188,191,215,225,231,238,240,249,252,257,259,278,288,295,298,306,312,313,317,318,323,324,327,334,342,344,345,346,370,379,381,387,392,401,415)
    
    [Reply](https://chandoo.org/wp/sick-leave-usage-problem/#comment-1576719)
    
5.  ![](https://secure.gravatar.com/avatar/aee5f5b568c6f3d309e4d5d53b9a98535fd42577d69f12c7476579f35d62842a?s=64&d=mm&r=g) David N says:
    
    [September 21, 2018 at 7:56 pm](https://chandoo.org/wp/sick-leave-usage-problem/#comment-1576721)
    
    Exactly 100% = 21  
    \=SUMPRODUCT(--(SUMIFS(leaves\[Days used\],leaves\[Emp ID\],emps\[Emp ID\])=emps\[Entitlement\]))
    
    At Least 100% = 67  
    \=SUMPRODUCT(--(SUMIFS(leaves\[Days used\],leaves\[Emp ID\],emps\[Emp ID\])>=emps\[Entitlement\]))
    
    None = 10  
    \=SUMPRODUCT(--(SUMIFS(leaves\[Days used\],leaves\[Emp ID\],emps\[Emp ID\])=0))
    
    Getting the list required something more than regular functions. I used a personal VBA function that returns a delimited list of multiple matches and chose to obtain those IDs for the Exactly 100% case.  
    7; 12; 91; 103; 104; 131; 157; 170; 176; 177; 225; 249; 295; 298; 313; 317; 342; 346; 381; 392; 415
    
    [Reply](https://chandoo.org/wp/sick-leave-usage-problem/#comment-1576721)
    
6.  ![](https://secure.gravatar.com/avatar/09a147a72ebae365c1d3d541afd178c0bbb16380c3cb07bebf0eb5d8807f8432?s=64&d=mm&r=g) [Duncan Williamson](https://excelmaster.co/)
     says:
    
    [September 22, 2018 at 2:48 am](https://chandoo.org/wp/sick-leave-usage-problem/#comment-1576766)
    
    Create a query for each table ... I chose Close and Load to the same worksheet in each case  
    Now Append leaves query to emps query to give me a three column query: Emp ID, Entitlement, Spent  
    Use this new query to create a Pivot Table:  
    Emp ID in Rows  
    For demonstration I put Entitlement and Spent in the Values area ... noting that Entitlement will show as Count because there are text entries in that column so you have to make it show Sum  
    I now created a Calculated Field called Entitl less Spent to show the Balance on the Leave Account for each employee  
    From that column, my answers:  
    21 people used all of their entitlement  
    Emloyees who took no leave:  
    35  
    77  
    78  
    273  
    276  
    281  
    301  
    316  
    338  
    416  
    The 21 people who have taken all of their entitlement are:  
    7  
    12  
    91  
    103  
    104  
    131  
    157  
    170  
    176  
    177  
    225  
    249  
    295  
    298  
    313  
    317  
    342  
    346  
    381  
    392  
    415
    
    If I am wrong here, please point out my errors, I would be grateful!
    
    [Reply](https://chandoo.org/wp/sick-leave-usage-problem/#comment-1576766)
    
7.  ![](https://secure.gravatar.com/avatar/16fd50a15922676dcb3511a397c87c2c2fd8e11176d8aa058a3e847bdf7dab2f?s=64&d=mm&r=g) Robert H. Gascon says:
    
    [September 22, 2018 at 8:05 am](https://chandoo.org/wp/sick-leave-usage-problem/#comment-1576811)
    
    1\. Employees who used 100% of their entitlement = 67;  
    \=SUMPRODUCT(--(SUMIF(leaves\[Emp ID\],  
    emps\[Emp ID\],  
    leaves\[Days used\])>=emps\[Entitlement\]))
    
    2\. Employees who took no sick leave = 10;  
    \=SUMPRODUCT(--(SUMIF(leaves\[Emp ID\],  
    emps\[Emp ID\],  
    leaves\[Days used\])=0))
    
    3\. List of 67 employees in Item 1, starting with cell O7 downwards;  
    \=IFERROR(LOOKUP(1,  
    1/(1/ROW(emps\[Emp ID\])=MAX(INDEX(1/ROW(emps\[Emp ID\])\*(SUMIF(leaves\[Emp ID\],emps\[Emp ID\],leaves\[Days used\])>=emps\[Entitlement\])\*(COUNTIF(O$6:O6,emps\[Emp ID\])=0),0))),  
    emps\[Emp ID\]),"")
    
    Note: 1/ROW(emps\[Emp ID\]) is the imaginary helper column and (COUNTIF(O$6:O6,emps\[Emp ID\])=0) filters for employees not yet listed.
    
    [Reply](https://chandoo.org/wp/sick-leave-usage-problem/#comment-1576811)
    
8.  ![](https://secure.gravatar.com/avatar/ce7106cfd406deda8e930395f2500f4f475abf9d52cd3e0b31cc8d7a998ec803?s=64&d=mm&r=g) GraH says:
    
    [September 22, 2018 at 10:10 am](https://chandoo.org/wp/sick-leave-usage-problem/#comment-1576836)
    
    Load both tables as connection only
    
    1) emp  
    let  
    Source = Excel.CurrentWorkbook(){\[Name="emps"\]}\[Content\],  
    #"Changed Type" = Table.TransformColumnTypes(Source,{{"Emp ID", type text}}),  
    FilterOutX = Table.SelectRows(#"Changed Type", each (\[Entitlement\] "x")),  
    ChangeToNumber = Table.TransformColumnTypes(FilterOutX,{{"Entitlement", Int64.Type}})  
    in  
    ChangeToNumber
    
    2) leaves, already grouped to sum the days used  
    let  
    Source = Excel.CurrentWorkbook(){\[Name="leaves"\]}\[Content\],  
    #"Changed Type" = Table.TransformColumnTypes(Source,{{"Days used", Int64.Type}, {"Emp ID", type text}}),  
    SumOfDaysUsed = Table.Group(#"Changed Type", {"Emp ID"}, {{"Days Used", each List.Sum(\[Days used\]), type number}}),  
    SetAsNumber = Table.TransformColumnTypes(SumOfDaysUsed,{{"Days Used", Int64.Type}})  
    in  
    SetAsNumber
    
    3) Analysis: I appended both tables, sorted, grouped to sum, calculated remaining, defined categories, filter the categories and extracted the list of ID's.
    
    let  
    Source = Table.Combine({emps, leaves}),  
    SortOnID = Table.Sort(Source,{{"Emp ID", Order.Ascending}}),  
    SumValues = Table.Group(SortOnID, {"Emp ID"}, {{"Entitlement", each List.Sum(\[Entitlement\]), type anynonnull}, {"Days Used", each List.Sum(\[Days Used\]), type number}}),  
    FilterOutUnlimted = Table.SelectRows(SumValues, each (\[Entitlement\] null)),  
    CalcRemaining = Table.AddColumn(FilterOutUnlimted, "Remaining", each if \[Entitlement\]=null then null else \[Entitlement\]-\[Days Used\]),  
    DefineCategory = Table.AddColumn(CalcRemaining, "Category", each if \[Remaining\] = 0 then "All sick days taken" else if \[Days Used\] = null then "No sick days taken" else if \[Remaining\] < 0 then "More sick days taken then entitled" else "Some days taken"),  
    FilterOnScope = Table.SelectRows(DefineCategory, each (\[Category\] = "All sick days taken" or \[Category\] = "No sick days taken")),  
    GroupCategory = Table.Group(FilterOnScope, {"Category"}, {{"AsTable", each \_, type table}, {"Count Employees", each Table.RowCount(\_), type number}}),  
    ListIDs = Table.AddColumn(GroupCategory, "List IDs", each if \[Category\] "All sick days taken" then null else List.Accumulate(Table.Column(\[AsTable\],"Emp ID") ,"", (state,current) => if state = "" then current else state & ", " & current ))  
    in  
    ListIDs
    
    Analysis loaded to workbook:  
    \- 21 employees took exactly 100% of entitled sickness.  
    \- List is {7, 12, 91, 103, 104, 131, 157, 170, 176, 177, 225, 249, 295, 298, 313, 317, 342, 346, 381, 392, 415}  
    \- 10 have taken no sick leave
    
    [Reply](https://chandoo.org/wp/sick-leave-usage-problem/#comment-1576836)
    
    *   ![](https://secure.gravatar.com/avatar/ce7106cfd406deda8e930395f2500f4f475abf9d52cd3e0b31cc8d7a998ec803?s=64&d=mm&r=g) GraH says:
        
        [September 22, 2018 at 10:38 am](https://chandoo.org/wp/sick-leave-usage-problem/#comment-1576843)
        
        Okay, I misread the assignment
        
        My corrected analysis query  
        let  
        Source = Table.Combine({emps, leaves}),  
        SortOnID = Table.Sort(Source,{{"Emp ID", Order.Ascending}}),  
        SumValues = Table.Group(SortOnID, {"Emp ID"}, {{"Entitlement", each List.Sum(\[Entitlement\]), type anynonnull}, {"Days Used", each List.Sum(\[Days Used\]), type number}}),  
        FilterOutUnlimted = Table.SelectRows(SumValues, each (\[Entitlement\] null)),  
        CalcRemaining = Table.AddColumn(FilterOutUnlimted, "Remaining", each if \[Entitlement\]=null then null else \[Entitlement\]-\[Days Used\]),  
        DefineCategory = Table.AddColumn(CalcRemaining, "Category", each if \[Remaining\] = 0 then "Exactly all sick days taken" else if \[Days Used\] = null then "No sick days taken" else if \[Remaining\] < 0 then "More sick days taken then entitled" else "Some days taken"),  
        FilterOnScope = Table.SelectRows(DefineCategory, each (\[Category\] "Some days taken")),  
        AddCat2 = Table.AddColumn(FilterOnScope, "Category2", each if \[Category\] = "No sick days taken" then \[Category\] else "All entitled sick days taken"),  
        GroupCategory = Table.Group(AddCat2, {"Category2", "Category"}, {{"AsTable", each \_, type table}, {"Count Employees", each Table.RowCount(\_), type number}}),  
        ListIDs = Table.AddColumn(GroupCategory, "List IDs", each if \[Category2\] "All entitled sick days taken" then null else if \[Category\] = "Exactly all sick days taken" then null else List.Accumulate(Table.Column(\[AsTable\],"Emp ID") ,"", (state,current) => if state = "" then current else state & ", " & current )),  
        AddGroupCat = Table.AddColumn(ListIDs, "Group", each if \[Category\] = "Exactly all sick days taken" then \[Category\] else \[Category2\]),  
        RemoveCol = Table.RemoveColumns(AddGroupCat,{"Category2", "Category", "AsTable"}),  
        GroupAsFirstCol = Table.ReorderColumns(RemoveCol,{"Group", "Count Employees", "List IDs"})  
        in  
        GroupAsFirstCol
        
        [Reply](https://chandoo.org/wp/sick-leave-usage-problem/#comment-1576843)
        
9.  ![](https://secure.gravatar.com/avatar/a1f7acf2bbc01a19273378d2791017b7d251be8bfe1b6b93ee46dffa59d85f8d?s=64&d=mm&r=g) Tim says:
    
    [September 22, 2018 at 11:04 am](https://chandoo.org/wp/sick-leave-usage-problem/#comment-1576846)
    
    It took me about ten minutes to sort, sum and count. How long does Power Query take?
    
    [Reply](https://chandoo.org/wp/sick-leave-usage-problem/#comment-1576846)
    
    *   ![](https://secure.gravatar.com/avatar/7c2d6249f7e7aeb5ca458c7326411a64256a9fd754d056c993aa88a6ec6aa138?s=64&d=mm&r=g) Terry W says:
        
        [September 24, 2018 at 3:33 am](https://chandoo.org/wp/sick-leave-usage-problem/#comment-1577197)
        
        Hi Tim,
        
        It took roughly 6~8 minutes to use PQ to work out the answers.
        
        I am new to PQ but I think what is more valuable is that PQ allow you to simply replace the source data to get the result in one click (refresh data). So you do not need to spend another 10 minute next time for a different set of data.
        
        Cheers,
        
        Terry
        
        [Reply](https://chandoo.org/wp/sick-leave-usage-problem/#comment-1577197)
        
10.  ![](https://secure.gravatar.com/avatar/7c2d6249f7e7aeb5ca458c7326411a64256a9fd754d056c993aa88a6ec6aa138?s=64&d=mm&r=g) Terry W says:
    
    [September 24, 2018 at 3:29 am](https://chandoo.org/wp/sick-leave-usage-problem/#comment-1577196)
    
    1) Import both tables (Emps and Leaves) to PQ;  
    2) Group 'Days Used' column in the Leaves table by Emp ID, and then merge the new table with Emps table, then expand the new merged column to show Entitlement;  
    3) Duplicate the new Leaves table, add a new column to calculate the difference between the 'Total Days Used' column and 'Entitlement' column, then filter the difference column by '0'. Remove all columns except the Emp ID column and then use the Count Rows function to find out the total number of employees who used exactly 100% of their leaves;  
    4) Merge the Emps table with Leaves table, expand the new merged column to show Total Days Left. Filter the column by null, Remove all columns except the Emp ID column and then use the Count Rows function to find out the total number of employees who used exactly 100% of their leaves;  
    5) Duplicate the new table from Step 3, alter the filter step to show all employees who have used 100% of their entitlement or more. Remove the step of Count Rows and you will have the list of employees who have no entitlement left.
    
    The answers are 21, 10, and 67 (the answer for Q3 should be a list of employees but for simplicity I just use the total count as the answer)
    
    [Reply](https://chandoo.org/wp/sick-leave-usage-problem/#comment-1577196)
    
11.  ![](https://secure.gravatar.com/avatar/42293d49ba994bb52fa3e6c639ea0013668101d267c74c848e7196058fb40e7b?s=64&d=mm&r=g) Romulo Escobar says:
    
    [September 24, 2018 at 8:07 pm](https://chandoo.org/wp/sick-leave-usage-problem/#comment-1577312)
    
    I used the following formulas:
    
    SUM(IF(SUMIFI(leaves\[Emp ID\],emps\[Emp ID\],leaves\[Days used\])=emps\[Entitlement\],1,0))
    
    SUM(IF(SUMIF(leaves\[Emp ID\],emps\[Emp ID\],leaves\[Days used\])=0,1,0))
    
    TEXTJOIN(", ",1,IF(IF(SUMIF(leaves\[Emp ID\],emps\[Emp ID\],leaves\[Days used\])=emps\[Entitlement\],1,"")=1,emps\[Emp ID\],""))
    
    the results were  
    21  
    10  
    7, 12, 91, 103, 104, 131, 157, 170, 176, 177, 225, 249, 295, 298, 313, 317, 342, 346, 381, 392, 415
    
    [Reply](https://chandoo.org/wp/sick-leave-usage-problem/#comment-1577312)
    
12.  ![](https://secure.gravatar.com/avatar/45bd8f7f61c4df6fef19670ec602202b70e479f5801b01b0b9fcb6ad2bfab2b3?s=64&d=mm&r=g) Shobi Imran says:
    
    [September 29, 2018 at 2:21 pm](https://chandoo.org/wp/sick-leave-usage-problem/#comment-1578295)
    
    Great Article Chandoo, Thanks for sharing, Keep up the good work
    
    [Reply](https://chandoo.org/wp/sick-leave-usage-problem/#comment-1578295)
    
13.  ![](https://secure.gravatar.com/avatar/c7db5b0f3d9a0799a97109f1f51c0416751e3421c7ea6f963e0072ccf811bccd?s=64&d=mm&r=g) Peter Bartholomew says:
    
    [October 10, 2018 at 8:17 pm](https://chandoo.org/wp/sick-leave-usage-problem/#comment-1580323)
    
    Using named formulas. The first step was to sum the number of days leave for each employer, 'used':  
    \= SUMIFS(leaves\[Days used\],leaves\[Emp ID\], ID)  
    where ID is a shorter name to refer to '=emps\[Emp ID\]'.
    
    To avoid the nuisance of CSE or SUMPRODUCT without the product, a couple of further named formulas 'zeroSickLeave?' and 'excessSickLeave?' to act as flags:  
    \= N(used=0)  
    \= N(emps\[Entitlement\] <= used)
    
    That leaves worksheet formulae  
    \= SUM( excessSickLeave? )  
    \= SUM( zeroSickLeave? )  
    giving 67 and 10 respectively.
    
    The list requires the SMALL function  
    \= IFERROR( SMALL( IF(excessSickLeave?, ID ), ID ), "" )
    
    Roll on dynamic arrays and FILTER!
    
    [Reply](https://chandoo.org/wp/sick-leave-usage-problem/#comment-1580323)
    
14.  ![](https://secure.gravatar.com/avatar/d8a7e4ae709e5762a82eab2c1ca5bdb6115df9463e4597fadf18f89fc8ae3c1e?s=64&d=mm&r=g) Gerardo Gomez says:
    
    [January 3, 2019 at 6:38 pm](https://chandoo.org/wp/sick-leave-usage-problem/#comment-1608748)
    
    Hi Chandoo,
    
    Added 2 new columns to "EMPS" table. I used the following formulas:  
    1\. =+SUMAR.SI(leaves;\[@\[Emp ID\]\];leaves\[Days used\])  
    2\. =+SI(\[@Entitlement\]="x";"";\[@\[Days Used\]\]/\[@Entitlement\])
    
    After it, I was able to answer these questions via Pivot Table, Graphics or by simple filtering my columns.  
    1\. How many employees used exactly 100% of their entitlement? 21  
    2\. How many employees did not use take any sick leaves? 10  
    3\. List of employees who used 100% of their entitlement: 67  
    List:  
    5  
    7  
    12  
    30  
    32  
    34  
    43  
    50  
    61  
    79  
    89  
    90  
    91  
    93  
    101  
    103  
    104  
    105  
    119  
    128  
    131  
    139  
    141  
    150  
    157  
    170  
    175  
    176  
    177  
    178  
    179  
    186  
    188  
    191  
    215  
    225  
    231  
    238  
    240  
    249  
    252  
    257  
    259  
    278  
    288  
    295  
    298  
    306  
    312  
    313  
    317  
    318  
    323  
    324  
    327  
    334  
    342  
    344  
    345  
    346  
    370  
    379  
    381  
    387  
    392  
    401  
    415
    
    Cheers Chandoo!  
    And thanks again!
    
    [Reply](https://chandoo.org/wp/sick-leave-usage-problem/#comment-1608748)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/sick-leave-usage-problem/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Lenient lookup \[Advanced Formula Trick\]](https://chandoo.org/wp/lenient-lookup-advanced-trick/) | [Leave entitlement vs. usage analysis with Power Query](https://chandoo.org/wp/entitlement-vs-usage-power-query/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)