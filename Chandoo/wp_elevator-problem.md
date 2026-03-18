# Elevator problem - Excel homework » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/elevator-problem

---

Elevator problem – Excel homework
=================================

[Excel Challenges](https://chandoo.org/wp/category/excel-challenges/)
 - 192 comments

  

The other day while I was in lift (elevator), it made an alarm like sound and won’t close the doors. Turns out there are one too many people in the lift for it to operate safely. As soon as a couple of people volunteered and stepped out, it started fighting gravity and took us upstairs. That brings us to the problem at hand. **Elevator problem.** 

Let’s say you have a bunch of people and their weights in a spreadsheet like this.

![Elevator problem - excel formula homework](https://chandoo.org/wp/wp-content/uploads/2018/12/elevator-problem.png)

Each row contains some people and their weights. Assume that lift (elevator) can take up to 20 people and total of 1,400 kilos. Your mission, if you choose to accept is this:

*   Write a formula / Power Query thingie / VBA / haiku to figure out if the lift should go or stay.

Go… (or may be stay if the load is too heavy or too many)

**Lift / Elevator conditions explained:**

In order for the lift to move, it needs to satisfy both conditions:

*   Total number of people is under or equal to 20
*   Total weight is under or equal to 1,400

**Download sample data – elevator problem workbook**

[**Click here to download sample data for this problem**](https://chandoo.org/wp/wp-content/uploads/2018/12/elevator-problem-workbook.xlsx)
. Write your formulas / PQ / other solutions in the workbook. Once you crack it, comeback and post your solution in the comments.

Note about using < or > symbols in comments. Our blog commenting system digests angle brackets. So just use LT and GT instead of < or > symbols and you are good to go.

### Want more problems? We got some for you:

No one likes problems. But if you are that rare snowflake who likes challenges, puzzles and problems, then [check out Excel Homework page](https://chandoo.org/wp/tag/homework)
. You will be rewarded handsomely.

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
| Written by Chandoo  <br>Tags: [downloads](https://chandoo.org/wp/tag/downloads/)<br>, [homework](https://chandoo.org/wp/tag/homework/)<br>, [Learn Excel](https://chandoo.org/wp/tag/excel/)<br>, [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 192 Responses to “Elevator problem – Excel homework”

1.  ![](https://secure.gravatar.com/avatar/45bd8f7f61c4df6fef19670ec602202b70e479f5801b01b0b9fcb6ad2bfab2b3?s=64&d=mm&r=g) [Shobi Imran](https://learningkeepsusalive.blogspot.com/)
     says:
    
    [December 13, 2018 at 8:32 am](https://chandoo.org/wp/elevator-problem/#comment-1599384)
    
    Very good post. Keep it up.  
    Thanks for sharing sample data.
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599384)
    
    *   ![](https://secure.gravatar.com/avatar/60e65c6e7030b045b56381cc2c58edc143d49d091476fe1f69d15b8315493e7f?s=64&d=mm&r=g) Josh says:
        
        [January 8, 2019 at 6:04 am](https://chandoo.org/wp/elevator-problem/#comment-1610738)
        
        I guess the simple formula below should do the trick.
        
        \=IF((OR(COUNT(C4:X4)>20,SUM(C4:X4)>1400)),"NO","GO")
        
        Let me know...
        
        Thx.
        
        [Reply](https://chandoo.org/wp/elevator-problem/#comment-1610738)
        
        *   ![](https://secure.gravatar.com/avatar/ea28c1bc04a3d18b9978fecd58f7c23c931824b325cd10168e017b2101f122b4?s=64&d=mm&r=g) Diogo Cuba says:
            
            [January 31, 2019 at 5:11 pm](https://chandoo.org/wp/elevator-problem/#comment-1618572)
            
            +1.
            
            BUT I would change the 1400 to the cell $AA$6 and 20 to $AA$5 for good practice. The same for the other cells.
            
            [Reply](https://chandoo.org/wp/elevator-problem/#comment-1618572)
            
2.  ![](https://secure.gravatar.com/avatar/0a5ea08998c088d59ba3257c1cb772a24a07b030cfacb0fcb6c32c804887fb74?s=64&d=mm&r=g) Art says:
    
    [December 13, 2018 at 8:51 am](https://chandoo.org/wp/elevator-problem/#comment-1599387)
    
    What's the trick?!  
    \=IF(AND(COUNT($C4:$X4) LT= $AA$5;SUM($C4:$X4) LT= $AA$6);"Yes";"No")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599387)
    
3.  ![](https://secure.gravatar.com/avatar/c05318da46bb4ec3144dc41a94da635a2ff47c6fb1b29020537204421052cd3b?s=64&d=mm&r=g) Sumanth says:
    
    [December 13, 2018 at 9:02 am](https://chandoo.org/wp/elevator-problem/#comment-1599390)
    
    \=IF(AND(COUNT(C4:X4)LT 21,SUM(C4:X4) LT 1400),"Go","Stay")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599390)
    
4.  ![](https://secure.gravatar.com/avatar/4429239600f3b245e439f5f00474beccbca92bc5bccc8996ff01242e5b2a2e91?s=64&d=mm&r=g) Rajesh Kumar Singh says:
    
    [December 13, 2018 at 9:14 am](https://chandoo.org/wp/elevator-problem/#comment-1599391)
    
    Formula at cell No. "B4"  
    \=IF(COUNT(C4:X4)>$AA$5,"STOP",IF(SUM(C4:X4)>$AA$6,"STOP","Go"))
    
    Copy this upto "B13".
    
    Regards  
    Rajesh
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599391)
    
5.  ![](https://secure.gravatar.com/avatar/55f76a863f3a799343d8601961e81f2ea88d2863f8c5414cd694956db2cf2223?s=64&d=mm&r=g) Niefer says:
    
    [December 13, 2018 at 10:27 am](https://chandoo.org/wp/elevator-problem/#comment-1599401)
    
    \=IF(AND(COUNT(C4:X4)<=AA$5,SUM(C4:X4)<=AA$6),"Go","Stay")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599401)
    
6.  ![](https://secure.gravatar.com/avatar/bbd148501516bc145cb67f344b5a77d9e599bb626087219d757fb69c94db6a65?s=64&d=mm&r=g) Manoj says:
    
    [December 13, 2018 at 10:31 am](https://chandoo.org/wp/elevator-problem/#comment-1599402)
    
    \=IF(AND(COUNT(C4:X4)<=20,SUM(C4:X4)<=1400),"Go","Stay")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599402)
    
7.  ![](https://secure.gravatar.com/avatar/f9c4b85a0a9b85beec57e34791e14440c631273eed007be1a3beb84d5b6fe0cc?s=64&d=mm&r=g) UWEISS says:
    
    [December 13, 2018 at 10:45 am](https://chandoo.org/wp/elevator-problem/#comment-1599405)
    
    \=IF(COUNT(C4:Y4)<=AA$5\*(SUM(C4:Y4)<=AA$6),"YES","")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599405)
    
8.  ![](https://secure.gravatar.com/avatar/e0868933ff93c375318648cc6e2aaec1c15219073380be11e3552c99ea68c99c?s=64&d=mm&r=g) JoAnn Paules says:
    
    [December 13, 2018 at 11:41 am](https://chandoo.org/wp/elevator-problem/#comment-1599409)
    
    \=IF(AND((COUNT(C4:X4)<=$AA$5),(SUM(C4:X4)<=$AA$6)),"Yes","No")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599409)
    
9.  ![](https://secure.gravatar.com/avatar/aaf7fb59af350a4728bc35024da2334d39b659babb051490fe619d1b671e312f?s=64&d=mm&r=g) Roger Govier says:
    
    [December 13, 2018 at 11:55 am](https://chandoo.org/wp/elevator-problem/#comment-1599412)
    
    \=IF((COUNT(C4:X4)<=$AA$5)\*(SUM(C4:X4)<=$AA$6),"Go","Stop")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599412)
    
10.  ![](https://secure.gravatar.com/avatar/f35ffdd7aaa4fce279235ffee1de2e503bb6fce1f0e24d74537393ed4bed128a?s=64&d=mm&r=g) Hazel McLaren says:
    
    [December 13, 2018 at 3:23 pm](https://chandoo.org/wp/elevator-problem/#comment-1599426)
    
    \=IF(OR(COUNT(C4:X4)RT$AA$5,(SUM(C4:X4)RT$AA$6)),"STOP","GO")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599426)
    
11.  ![](https://secure.gravatar.com/avatar/7f054e5ecf42d0391987b60b0f0a7be863fb6196aa1f102e36571991b752ef07?s=64&d=mm&r=g) Eric says:
    
    [December 13, 2018 at 3:50 pm](https://chandoo.org/wp/elevator-problem/#comment-1599428)
    
    Haiku version:  
    Elevator goes?  
    twenty people and less than  
    1 point 4 kilo
    
    VBA version:  
    Sub CanItGo()  
    Dim rowCount As Integer  
    Dim weightTotal As Integer  
    Dim peopleTotal As Integer  
    For rowCount = 4 To 13  
    weightTotal = WorksheetFunction.Sum(Range("C" & rowCount & ":X" & rowCount))  
    peopleTotal = WorksheetFunction.CountA(Range("C" & rowCount & ":x" & rowCount))  
    If weightTotal GT Range("AA6").Value Then Range("B" & rowCount).Value = "too heavy"  
    If peopleTotal GT Range("AA5").Value Then Range("B" & rowCount).Value = "too many"  
    If weightTotal GT Range("AA6").Value And peopleTotal GT Range("AA5").Value Then Range("B" & rowCount).Value = "too many and too heavy"  
    Next rowCount  
    End Sub
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599428)
    
12.  ![](https://secure.gravatar.com/avatar/00a5349b7c5a4b1984ccc4336028007f308aba6051aa8245d259e6e76b339443?s=64&d=mm&r=g) Dan says:
    
    [December 13, 2018 at 4:14 pm](https://chandoo.org/wp/elevator-problem/#comment-1599437)
    
    I think you can go even simpler -- assuming the data is input/collectect correctly you don't even need to count the columns. Just check if Wx is not empty. Additionally you only need to sum up the first 20 columns as you will get a STOP condition if a 21st element even appears.
    
    \=IF(OR($W3 GT 0,SUM($C3:$V3) GT 1400),"STOP","GO")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599437)
    
13.  ![](https://secure.gravatar.com/avatar/9e68c3a73b772ad35621fcab76f3e150db63003cf52a7f70bfb9b3b0d9f6ef4c?s=64&d=mm&r=g) Wruf says:
    
    [December 13, 2018 at 4:46 pm](https://chandoo.org/wp/elevator-problem/#comment-1599446)
    
    \=IF(NOT($W4)\*(SUM(C4:X4)<=$AA$6),"Go","Stop")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599446)
    
14.  ![](https://secure.gravatar.com/avatar/3ebdb54bed4c8d19284a7f67b664586e3bf707b37c3a3a4b11467d5c1675f7f8?s=64&d=mm&r=g) [Pramod](http://none/)
     says:
    
    [December 13, 2018 at 4:50 pm](https://chandoo.org/wp/elevator-problem/#comment-1599448)
    
    \=IF(AND(SUM(C4:X4)<=1400,COUNT(C4:X4)<=20),"Yes","No")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599448)
    
15.  ![](https://secure.gravatar.com/avatar/7819666548ad64b7804a5867593df3c379027938c61c8b0da15d9e53b0f8d176?s=64&d=mm&r=g) Lorenzo says:
    
    [December 13, 2018 at 4:56 pm](https://chandoo.org/wp/elevator-problem/#comment-1599452)
    
    \=IF(OR(SUM(C5:X5)GT1400,COUNT(C5:X5)GT20),"NO","YES")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599452)
    
16.  ![](https://secure.gravatar.com/avatar/e9d836fd1c285762b9825aeb6a4d0c318d6b680e342a00bfc9548486cb7829f0?s=64&d=mm&r=g) Cesar says:
    
    [December 13, 2018 at 4:58 pm](https://chandoo.org/wp/elevator-problem/#comment-1599454)
    
    \=IF(OR(SUM(C4:X4)>$AA$6;COUNT(C4:X4)>$AA$5);"Stop";"GO")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599454)
    
17.  ![](https://secure.gravatar.com/avatar/1faa850474388d6d3c062660b70fc87e13eb569cd6c70ba4884341be0519ac4b?s=64&d=mm&r=g) Kathy Dawson says:
    
    [December 13, 2018 at 5:00 pm](https://chandoo.org/wp/elevator-problem/#comment-1599455)
    
    \=IF(AND((COUNT(C4:X4)<=$AA$5),(SUM(C4:X4)<=$AA$6)),"Go","Stay")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599455)
    
18.  ![](https://secure.gravatar.com/avatar/588078d70aae8ade403d5f8036a297d108de314b3ae332bf1bbc279038345f18?s=64&d=mm&r=g) Scott says:
    
    [December 13, 2018 at 5:00 pm](https://chandoo.org/wp/elevator-problem/#comment-1599456)
    
    \=IF(OR(COUNT(C4:X4)>$AA$5,SUM(C4:X4)>$AA$6),"Stay","Go")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599456)
    
19.  ![](https://secure.gravatar.com/avatar/e9d836fd1c285762b9825aeb6a4d0c318d6b680e342a00bfc9548486cb7829f0?s=64&d=mm&r=g) Cesar says:
    
    [December 13, 2018 at 5:00 pm](https://chandoo.org/wp/elevator-problem/#comment-1599457)
    
    "=IF(OR(SUM(C4:X4)>$AA$6;COUNT(C4:X4)>$AA$5);"Stop";"GO")"
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599457)
    
20.  ![](https://secure.gravatar.com/avatar/7819666548ad64b7804a5867593df3c379027938c61c8b0da15d9e53b0f8d176?s=64&d=mm&r=g) [Lorenzo](http://none/)
     says:
    
    [December 13, 2018 at 5:00 pm](https://chandoo.org/wp/elevator-problem/#comment-1599458)
    
    \=IF(OR(SUM(C4:X4)GT1400,COUNT(C4:X4)GT20),"NO","YES")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599458)
    
21.  ![](https://secure.gravatar.com/avatar/1faa850474388d6d3c062660b70fc87e13eb569cd6c70ba4884341be0519ac4b?s=64&d=mm&r=g) Kathy Dawson says:
    
    [December 13, 2018 at 5:03 pm](https://chandoo.org/wp/elevator-problem/#comment-1599460)
    
    \=IF(AND((COUNT(C4:X4)<=$AA$5),(SUM(C4:X4)<=$AA$6)),"Go","Stay")
    
    Copy down to remaining rows.
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599460)
    
    *   ![](https://secure.gravatar.com/avatar/348a49572058c15bc4a655a01e4b2dd354073a15af507a8118d74569964a8bb7?s=64&d=mm&r=g) Mohsin Ejaz says:
        
        [December 5, 2019 at 11:30 pm](https://chandoo.org/wp/elevator-problem/#comment-1719098)
        
        Made exact same formula. It's short and sweet.
        
        [Reply](https://chandoo.org/wp/elevator-problem/#comment-1719098)
        
22.  ![](https://secure.gravatar.com/avatar/70cd22acdacc92537aef4e6942f9493c28a58b6d5be3ab15eee305cd2b3f7425?s=64&d=mm&r=g) [Vijayan](http://www.en-spark.com/)
     says:
    
    [December 13, 2018 at 5:16 pm](https://chandoo.org/wp/elevator-problem/#comment-1599465)
    
    Hello  
    Can you help me with a Excel template for financial projections for 5 yearsfor a start up project in India ,showing profit and loss , balance sheet and cash flow  
    Regards  
    Vijayan
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599465)
    
23.  ![](https://secure.gravatar.com/avatar/8f7af946a8fae19829e98a8e7c01c0a4b5789fcfe4215061dffb62a2cc747715?s=64&d=mm&r=g) jim says:
    
    [December 13, 2018 at 5:17 pm](https://chandoo.org/wp/elevator-problem/#comment-1599466)
    
    {=AND(COUNTA(C4:X4)<=AA$5,SUM(--C4:X4)<=AA$6)}
    
    \- entered as an array formula, just in case some people try to sneak their weights in as text!
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599466)
    
24.  ![](https://secure.gravatar.com/avatar/6719e22b4f610ee109ac36e01113ea3385de0e2f7d60f5737502fb8394912b60?s=64&d=mm&r=g) [Mehmet Gunal OLCER](http://www.polimetre.com/)
     says:
    
    [December 13, 2018 at 5:34 pm](https://chandoo.org/wp/elevator-problem/#comment-1599473)
    
    \=IF(AND(COUNTIFS(C4:X4,">0")<=20,SUM(C4:X4)<1400)\*1=1,"GO","NO GO")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599473)
    
25.  ![](https://secure.gravatar.com/avatar/a6d5d6309dc5a94191321f1a2490fe6c514e4bc9ddf71fac1268f96a9823d735?s=64&d=mm&r=g) Don Hopkins says:
    
    [December 13, 2018 at 5:34 pm](https://chandoo.org/wp/elevator-problem/#comment-1599474)
    
    OK I started out by using this formula which seemed to me to be the shortest and most efficient:
    
    \=IF(W4=0,IF(SUM(C4:V4)<1401,"GO","NO GO"),"NO GO")
    
    It was not doing repetitive counting and tested only with LT. The summing does not have to include X4
    
    The following solution has the advantage of being easily adjustable for different capacity elevators.
    
    \=IF(COUNT(C4:X4)<=$AA$5,IF(SUM(C4:X4)<=$AA$6,"GO","NO GO"),"NO GO")
    
    With a small database such as this the processing efficiency comparison would make essentially no difference.
    
    But wait - - - this may be used thousands of times a day. Do we not have to be careful these days and think about efficiency in our coding?
    
    I am 86 years old and remember the old days when we did.
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599474)
    
26.  ![](https://secure.gravatar.com/avatar/b474635bede0a7762c762ac11c9f1feb23856ac452225cdefc465a04165ad051?s=64&d=mm&r=g) [Abbott Katz](http://www.spreadsheetjournalism.com/)
     says:
    
    [December 13, 2018 at 5:39 pm](https://chandoo.org/wp/elevator-problem/#comment-1599476)
    
    I may be missing something, but in B4 I entered:  
    \=IF(AND(COUNT(C4:X4)LT21,SUM(C4:X4)LT1401),"Yes","No")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599476)
    
27.  ![](https://secure.gravatar.com/avatar/e9d836fd1c285762b9825aeb6a4d0c318d6b680e342a00bfc9548486cb7829f0?s=64&d=mm&r=g) Cesar says:
    
    [December 13, 2018 at 5:40 pm](https://chandoo.org/wp/elevator-problem/#comment-1599477)
    
    {=IF(OR(SUM(C4:X4)>$AA$6;COUNT(C4:X4)>$AA$5);"Stop";"Go")}
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599477)
    
28.  ![](https://secure.gravatar.com/avatar/4f62a634981236fc12a334873142985ed225fdd7ee1e2cacf0835c1e2c03c1dd?s=64&d=mm&r=g) Mujibur says:
    
    [December 13, 2018 at 6:10 pm](https://chandoo.org/wp/elevator-problem/#comment-1599493)
    
    \=IF(SUM(C4:X4)<=1400,"Lift can move","")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599493)
    
29.  ![](https://secure.gravatar.com/avatar/9161a414a1a8bcab7eae874e60b172366fb5809f30f0279fab5ac5d2fa880893?s=64&d=mm&r=g) Pablo says:
    
    [December 13, 2018 at 6:12 pm](https://chandoo.org/wp/elevator-problem/#comment-1599494)
    
    I entered this formula:  
    \=IF(AND(SUM($C4:$X4)LT=1400;COUNT($C4:$X4)LT=20);"Can";"Can't")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599494)
    
30.  ![](https://secure.gravatar.com/avatar/30a29dd4ebe4b99664ac8e3180d54c9f212fb5e3debf176b85d2b56b587c5432?s=64&d=mm&r=g) Rajender says:
    
    [December 13, 2018 at 7:15 pm](https://chandoo.org/wp/elevator-problem/#comment-1599521)
    
    I will use this formula =IF(AND(SUM(C4:X4)<=$AA$6,COUNT(C4:X4)<=20),"Go","Not Go")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599521)
    
31.  ![](https://secure.gravatar.com/avatar/2f191246ba19de6891f69d55c1c923580416aaa58f52e9bd01713f5b6c40cf0a?s=64&d=mm&r=g) John says:
    
    [December 13, 2018 at 7:19 pm](https://chandoo.org/wp/elevator-problem/#comment-1599524)
    
    \=IF(AND(COUNT(C4:X4)<=20,SUM(C4:X4)<=1400),"Go","Stay")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599524)
    
32.  ![](https://secure.gravatar.com/avatar/634396c3fb01627b8b70dffb10f454f668c9314d0349fc0c76a1b1d632be66b1?s=64&d=mm&r=g) Jack says:
    
    [December 13, 2018 at 7:21 pm](https://chandoo.org/wp/elevator-problem/#comment-1599526)
    
    Short and sweet:  
    \=IF(OR(COUNT(C4:X4)>20,SUM(C4:X4)>1400),"No","Yes")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599526)
    
33.  ![](https://secure.gravatar.com/avatar/2f191246ba19de6891f69d55c1c923580416aaa58f52e9bd01713f5b6c40cf0a?s=64&d=mm&r=g) John says:
    
    [December 13, 2018 at 7:22 pm](https://chandoo.org/wp/elevator-problem/#comment-1599527)
    
    \=IF(AND(COUNT(C4:X4)<=AA$5,SUM(C4:X4)<=AA$6),"Go","Stay")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599527)
    
34.  ![](https://secure.gravatar.com/avatar/630a3272b5b3c822aa3032f90b43bc08716cbaeb31b6c3aa856885280bed83e1?s=64&d=mm&r=g) Bill Wood says:
    
    [December 13, 2018 at 7:29 pm](https://chandoo.org/wp/elevator-problem/#comment-1599530)
    
    It's not often I read these and feel like I can do them. Thanks for throwing in an easy one. 🙂
    
    Here's my formula:  
    \=IF(AND(COUNT(C4:X4)LT=AA$5,SUM(C4:X4)LTAA$6),"Go","Stay")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599530)
    
35.  ![](https://secure.gravatar.com/avatar/8f01a0099f5f6a4b48553c5ff6861dc0dd217e324f0d5efa2d3ea4c9558289a1?s=64&d=mm&r=g) Nathan says:
    
    [December 13, 2018 at 7:38 pm](https://chandoo.org/wp/elevator-problem/#comment-1599533)
    
    This seems to work:  
    \=IF(AND(COUNTA(C4:X4)<$AA$5+1,SUM(C4:X4)<$AA$6+1),"Good to go","PROBLEM")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599533)
    
36.  ![](https://secure.gravatar.com/avatar/7ff16dc671dced6dd6a62d2b891070a3837eb8c735f62fe75ae9440109d98245?s=64&d=mm&r=g) Pam says:
    
    [December 13, 2018 at 7:41 pm](https://chandoo.org/wp/elevator-problem/#comment-1599534)
    
    \=IF(AND(COUNTA(C4:X4)<=$AC$5,SUM(C4:X4)<=$AC$6),"GO","STAY")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599534)
    
37.  ![](https://secure.gravatar.com/avatar/4fec431773b80779e2495732051661011707e5347580799b01c955d94c2a1ac1?s=64&d=mm&r=g) Jon says:
    
    [December 13, 2018 at 7:51 pm](https://chandoo.org/wp/elevator-problem/#comment-1599538)
    
    \=IF((--(COUNT(C4:X4)<=$AA$5)+--(SUM(C4:X4)=2, "YES", "NO")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599538)
    
38.  ![](https://secure.gravatar.com/avatar/20ba2aa6fe735063514ddc3f90d9b935e3feb8f6acefa6945c912249c8d05871?s=64&d=mm&r=g) Andrew says:
    
    [December 13, 2018 at 8:02 pm](https://chandoo.org/wp/elevator-problem/#comment-1599542)
    
    \=IF(AND(COUNT(C4:X4)<21,SUM(C4:X4)<1401),"YES","NO")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599542)
    
39.  ![](https://secure.gravatar.com/avatar/20ba2aa6fe735063514ddc3f90d9b935e3feb8f6acefa6945c912249c8d05871?s=64&d=mm&r=g) Andrew says:
    
    [December 13, 2018 at 8:04 pm](https://chandoo.org/wp/elevator-problem/#comment-1599544)
    
    ...or this...  
    \=IF(AND(COUNT(C4:X4)<$AA$5,SUM(C4:X4)<$AA$6),"YES","NO")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599544)
    
40.  ![](https://secure.gravatar.com/avatar/ecee021ef5adf04bbec6c34e4113552a03a3330f7496b500a9c80ffcd38769ea?s=64&d=mm&r=g) Alex Ma says:
    
    [December 13, 2018 at 8:09 pm](https://chandoo.org/wp/elevator-problem/#comment-1599547)
    
    \=IF(AND((COUNTA(C4:X4)<=20),(SUM(C4:X4)<=1400)),"Y","N")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599547)
    
41.  ![](https://secure.gravatar.com/avatar/a2ce73364d19179c6ea9c2faafdbc068646d29946dc41fd2fa77a0efe48ea2c6?s=64&d=mm&r=g) Frank McCraw says:
    
    [December 13, 2018 at 8:20 pm](https://chandoo.org/wp/elevator-problem/#comment-1599553)
    
    \=IF(OR(COUNTA(C4:X4)>$AA$5,SUM(C4:X4)>$AA$6),"No","OK")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599553)
    
    *   ![](https://secure.gravatar.com/avatar/a2ce73364d19179c6ea9c2faafdbc068646d29946dc41fd2fa77a0efe48ea2c6?s=64&d=mm&r=g) Frank McCraw says:
        
        [December 14, 2018 at 11:40 am](https://chandoo.org/wp/elevator-problem/#comment-1600013)
        
        \=IF(OR(COUNT(C4:X4)>$AA$5,SUM(C4:X4)>$AA$6),"No","OK")
        
        [Reply](https://chandoo.org/wp/elevator-problem/#comment-1600013)
        
42.  ![](https://secure.gravatar.com/avatar/19091b854a40e09eb1fa7596629b2d75e272c74f6ea62f4f2c308f86ef108cee?s=64&d=mm&r=g) DanO says:
    
    [December 13, 2018 at 8:22 pm](https://chandoo.org/wp/elevator-problem/#comment-1599554)
    
    \=IF(AND((COUNTA(C3:X3)<=20), (SUM(C4:X4)<=1400)),"GO","NO GO")"
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599554)
    
43.  ![](https://secure.gravatar.com/avatar/19091b854a40e09eb1fa7596629b2d75e272c74f6ea62f4f2c308f86ef108cee?s=64&d=mm&r=g) DanO says:
    
    [December 13, 2018 at 8:42 pm](https://chandoo.org/wp/elevator-problem/#comment-1599564)
    
    \=IF(AND((COUNTA(C4:X4)<=20), (SUM(C4:X4)<=1400)),"GO","NO GO")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599564)
    
44.  ![](https://secure.gravatar.com/avatar/553968c1f0ba1c0ef7fcc31bb1ff227856ac0bd91bb39d8a98a284aa2733a1e8?s=64&d=mm&r=g) Alfonso López says:
    
    [December 13, 2018 at 8:46 pm](https://chandoo.org/wp/elevator-problem/#comment-1599569)
    
    It's almost the same formula, I just named the cells to make reading easier:  
    maxPeople -> cell AA5  
    maxWeight -> cell AA6
    
    Formula in B4:  
    \=IF(AND(COUNT(C4:X4)<=maxPeople,SUM(C4:X4)<=maxWeight),"YES","NO")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599569)
    
45.  ![](https://secure.gravatar.com/avatar/758178cec67337aede16d020e34593f395195fb0266ab31edae90b0769261606?s=64&d=mm&r=g) Ravi says:
    
    [December 13, 2018 at 8:49 pm](https://chandoo.org/wp/elevator-problem/#comment-1599570)
    
    \=IF(AND(COUNT(C4:X4)<=20,SUM(C4:X4)<=1400),"go","stay")
    
    please correct if I am wrong
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599570)
    
46.  ![](https://secure.gravatar.com/avatar/4d9a354ccbcee1f5526fa914b576f3ea52f1bb3bbdf13aedae02d9ad98a3bb4d?s=64&d=mm&r=g) Raphael Valente says:
    
    [December 13, 2018 at 9:16 pm](https://chandoo.org/wp/elevator-problem/#comment-1599582)
    
    in portuguese:
    
    \=SE(E(SOMA(E4:Z4)<=$AC$6;CONT.VALORES(E4:Z4)<=$AC$5);"Y";"N")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599582)
    
47.  ![](https://secure.gravatar.com/avatar/c85b5e5c057cbbeb17c39385f0b4181325a16aff675d05dd69857266ae320f2c?s=64&d=mm&r=g) Richard D says:
    
    [December 13, 2018 at 9:20 pm](https://chandoo.org/wp/elevator-problem/#comment-1599584)
    
    \=IF(AND(COUNTA(C4:X4)LT=AA$5,SUM(C4:X4)LT=AA$6),"GO","STAY")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599584)
    
48.  ![](https://secure.gravatar.com/avatar/badcf0a91dcdcb2ca6a7421d73bb477122d6771c408e82930a883ecb5ab6ab55?s=64&d=mm&r=g) Jan Martens says:
    
    [December 13, 2018 at 9:22 pm](https://chandoo.org/wp/elevator-problem/#comment-1599585)
    
    IF((SUM(OFFSET(C4,,,1,COUNTA(C4:Z4)))<1401)\*COUNTA(C4:Z4)<21,"go","no go")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599585)
    
    *   ![](https://secure.gravatar.com/avatar/badcf0a91dcdcb2ca6a7421d73bb477122d6771c408e82930a883ecb5ab6ab55?s=64&d=mm&r=g) jan martens says:
        
        [December 14, 2018 at 12:10 am](https://chandoo.org/wp/elevator-problem/#comment-1599645)
        
        \* counta , should be count.
        
        [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599645)
        
49.  ![](https://secure.gravatar.com/avatar/7f054e5ecf42d0391987b60b0f0a7be863fb6196aa1f102e36571991b752ef07?s=64&d=mm&r=g) Eric says:
    
    [December 13, 2018 at 9:23 pm](https://chandoo.org/wp/elevator-problem/#comment-1599586)
    
    (not sure why my initial response didn't post ... I'm going to assume the Interweb ate it)
    
    Haiku version:  
    Elevator goes?  
    Less than twenty folks and less  
    than one point four k
    
    VBA version:  
    Sub CanItGo()  
    Dim rowCount As Integer  
    Dim peopleCount As Integer  
    Dim weightCount As Integer  
    For rowCount = 4 To 13  
    weightCount = WorksheetFunction.Sum(Range("C" & rowCount & ":x" & rowCount))  
    peopleCount = WorksheetFunction.CountA(Range("C" & rowCount & ":x" & rowCount))  
    If weightCount GT Range("AA6").Value Then Range("B" & rowCount).Value = "Too heavy"  
    If peopleCount GT Range("AA5").Value Then Range("B" & rowCount).Value = "Too Many"  
    If weightCount GT Range("AA6").Value And peopleCount GT Range("AA5").Value Then Range("B" & rowCount).Value = "Too many and too heavy"  
    Next rowCount  
    End Sub
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599586)
    
50.  ![](https://secure.gravatar.com/avatar/b259ea4a3a42f3790584ffa61d762353a0894ddd699b5f0c3d435aad0118991e?s=64&d=mm&r=g) lee hibbert says:
    
    [December 13, 2018 at 9:26 pm](https://chandoo.org/wp/elevator-problem/#comment-1599588)
    
    OK, a bit left field
    
    Select C4:X13, Conditional Formatting, New Rule, Using Formula and enter the following
    
    \=AND(C4"",SUM($C4:C4)<=$AA$6,COUNT($C4:C4)<=$AA$5)  
    then format to your favourite colour OK, OK, OK and BOOM
    
    This will highlight those that can stay so that the lift can go in every event, with those not highlighted having to leave.
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599588)
    
51.  ![](https://secure.gravatar.com/avatar/be42aab533b13aa0f02cf5cf76473fe90e23dacd257123307289e3a7abf8f481?s=64&d=mm&r=g) NeilF says:
    
    [December 13, 2018 at 9:47 pm](https://chandoo.org/wp/elevator-problem/#comment-1599598)
    
    First off, I changed B3 to read "Alarm?"; then used the formula:  
    \=OR(COUNTA(C4:X4)GT$AA$5,SUM(C4:X4)GT$AA$6)
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599598)
    
52.  ![](https://secure.gravatar.com/avatar/dc59fa78c35ecb9a7bd29829bfb87496101325b057da984d1e74b290a30a323e?s=64&d=mm&r=g) Jeff says:
    
    [December 13, 2018 at 9:54 pm](https://chandoo.org/wp/elevator-problem/#comment-1599599)
    
    if there's a prize for the longest, least clever way to do it, this should do the trick:
    
    \=IF(IF(AND(IF(COUNT(C4:X4)<=20,1,0)=1,IF(SUM(C4:X4)<=1400,1,0)=1),1,0)=1,"Go","Stay")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599599)
    
53.  ![](https://secure.gravatar.com/avatar/09a147a72ebae365c1d3d541afd178c0bbb16380c3cb07bebf0eb5d8807f8432?s=64&d=mm&r=g) [Duncan Williamson](http://excelmaster.co/)
     says:
    
    [December 13, 2018 at 10:10 pm](https://chandoo.org/wp/elevator-problem/#comment-1599605)
    
    I offer this ... =IF(AND(COUNT(C4:X4)<=20,SUM(C4:X4)<=1400),"Go","Stay!")&" … "&COUNT(C4:X4)&" People "&SUM(C4:X4)&" Total Weight"
    
    Which tests for No of people <= 20 and combined weight of <=1400
    
    Then I added by concatenation, outside the scope of the exercise, information saying how many people were in the lift and their combined weight.
    
    Finally, I used conditional formatting on the output range to show green text and fill if the answer was Go and red text and fill if the answer was stay.
    
    By the way, I know AI etc is here but how many lifts can count how many people are in it?!
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599605)
    
    *   ![](https://secure.gravatar.com/avatar/09a147a72ebae365c1d3d541afd178c0bbb16380c3cb07bebf0eb5d8807f8432?s=64&d=mm&r=g) Duncan Williamson says:
        
        [December 16, 2018 at 11:13 pm](https://chandoo.org/wp/elevator-problem/#comment-1600582)
        
        Of course, I should have offered this
        
        \=IF(AND(COUNT(C4:X4)<=AA$5,SUM(C4:X4)<=AA$6),"Go","Stay!")&" … "&COUNT(C4:X4)&" People "&SUM(C4:X4)&" Total Weight"
        
        hard coding of the 20 and 1400 is bad practice ... one day, when they strengthen the lift and change 20 to 23 and 1400 to 1500, my formula would have failed.
        
        [Reply](https://chandoo.org/wp/elevator-problem/#comment-1600582)
        
54.  ![](https://secure.gravatar.com/avatar/8cdba8c9ecb80731a2739abc7202604e34a0012d6b17f36784b5bdc5c149d3fe?s=64&d=mm&r=g) Michael Kimber says:
    
    [December 13, 2018 at 11:18 pm](https://chandoo.org/wp/elevator-problem/#comment-1599629)
    
    my solution:
    
    \=IF(AND((COUNT(C4:X4)<21),(SUM(C4:X4)<1401)),"GO","STAY")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599629)
    
55.  ![](https://secure.gravatar.com/avatar/e2137ae94b6a1e113d0eea96654e421e5a1460ced8821aac86d486726674c1e3?s=64&d=mm&r=g) Oscar Rodríguez says:
    
    [December 13, 2018 at 11:38 pm](https://chandoo.org/wp/elevator-problem/#comment-1599634)
    
    \=IF(AND(COUNTIF(C4:X4,">0")<=$AA$5,SUMIF(C4:X4,"<="&$AA$6)),"GO","STAY")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599634)
    
56.  ![](https://secure.gravatar.com/avatar/8ee24008cf895490a38d84ac7dfcd41f40c2b83d0666c95fd598e2a5a51d5e81?s=64&d=mm&r=g) Mehta says:
    
    [December 13, 2018 at 11:41 pm](https://chandoo.org/wp/elevator-problem/#comment-1599636)
    
    \=IF(AND(COUNT(C4:X4)<=$AA$5,SUM(C4:X4)<=$AA$6),"YES","NO")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599636)
    
57.  ![](https://secure.gravatar.com/avatar/7059a9b70265d141a6cb3c29b657d93ffed4a515114d8170af287e60f42cdbfc?s=64&d=mm&r=g) Lily Tran says:
    
    [December 14, 2018 at 12:27 am](https://chandoo.org/wp/elevator-problem/#comment-1599657)
    
    \=IF(AND(SUM(C4:X4)<=$AA$6,COUNTA(C4:X4)<=$AA$5),"CAN GO","CAN'T GO")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599657)
    
58.  ![](https://secure.gravatar.com/avatar/2aec2fb6a8e587da8c0b89a3f6daf8c29c740825916dc658738401631ad62893?s=64&d=mm&r=g) Sagar says:
    
    [December 14, 2018 at 2:43 am](https://chandoo.org/wp/elevator-problem/#comment-1599733)
    
    \=IF(AND(COUNT(C4:X4)<=$AA$5,SUM(C4:X4)<=$AA$6),"Yes","No")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599733)
    
59.  ![](https://secure.gravatar.com/avatar/fc1577c96e8c22a2c0165f15792101802dda1a7dd3115da34c94bba67726f1a3?s=64&d=mm&r=g) Walter W. says:
    
    [December 14, 2018 at 2:55 am](https://chandoo.org/wp/elevator-problem/#comment-1599737)
    
    Here is my Power Query solution with comments above each line.
    
    let  
    Source = Excel.CurrentWorkbook(){\[Name="Table3"\]}\[Content\],  
    // demoted headers  
    #"Demoted Headers" = Table.DemoteHeaders(Source),  
    // removed first row  
    #"Removed Top Rows" = Table.Skip(#"Demoted Headers",1),  
    // removed Can\_Go column; recreate later  
    #"Removed Columns" = Table.RemoveColumns(#"Removed Top Rows",{"Column1"}),  
    // create new column; sum entire row without using column headings  
    #"Inserted Sum" = Table.AddColumn(#"Removed Columns", "Total Weight", each List.Sum(List.Select(Record.ToList(\_), each \_ is number))),  
    // create new column; count columns that have number without using column headings; subtract 1 due to sum column  
    #"Inserted Count" = Table.AddColumn(#"Inserted Sum", "Total People", each List.Count(List.Select(Record.ToList(\_), each \_ is number))-1),  
    // create new column; recreate Can\_Go column  
    #"Added Custom" = Table.AddColumn(#"Inserted Count", "Can Go?", each if \[Total Weight\]<= 1400 and \[Total People\]<= 20 then "Go" else "Stay"),  
    // create new column; group number using index  
    #"Added Index" = Table.AddIndexColumn(#"Added Custom", "Group#", 1, 1),  
    // rearrange and remove columns  
    #"Removed Other Columns" = Table.SelectColumns(#"Added Index",{"Can Go?", "Group#", "Total People", "Total Weight"}),  
    // fix column types  
    #"Changed Type" = Table.TransformColumnTypes(#"Removed Other Columns",{{"Can Go?", type text}, {"Group#", Int64.Type}, {"Total People", Int64.Type}, {"Total Weight", Int64.Type}})  
    in  
    #"Changed Type"
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599737)
    
60.  ![](https://secure.gravatar.com/avatar/4207a40c88f2a3774df9e368510bdfc0712135535837386b63838afd2b25994f?s=64&d=mm&r=g) Sravan K says:
    
    [December 14, 2018 at 3:53 am](https://chandoo.org/wp/elevator-problem/#comment-1599760)
    
    \=IF(AND(COUNTA($C4:$X4)<=20,SUM($C4:$X4)<1400),"Lift is Moving","Pls Volunteer, Lift is Not moving")
    
    used this formula.. as 2 criteria to be matched..  
    Single if statement with AND condition solved the purpose.. Pls let us know even better answer, I like to hear from you Chandoo.
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599760)
    
61.  ![](https://secure.gravatar.com/avatar/2cd886469a29c433f4c1373ff9b65fc62ca2e6502abcec78c1268648b2e2f256?s=64&d=mm&r=g) Hiren says:
    
    [December 14, 2018 at 4:03 am](https://chandoo.org/wp/elevator-problem/#comment-1599764)
    
    \=IF(AND(COUNT(C4:X4)<=20,SUM(C4:X4)<=1400),"Yes","No")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599764)
    
62.  ![](https://secure.gravatar.com/avatar/21dafc4affdfc21bf6c2c7edc3dc8a7489b69f00fc967e11f5bdc8f33dbc0091?s=64&d=mm&r=g) Sushil says:
    
    [December 14, 2018 at 4:14 am](https://chandoo.org/wp/elevator-problem/#comment-1599768)
    
    If((And(Count(C4:X4) <=$AA$5,SUM(C4:X4)<=$AA$6)),"Yes","No")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599768)
    
63.  ![](https://secure.gravatar.com/avatar/5671034704d280c4a557ef7ac78e92a0ae9df0246d7eb707283548ec2c7af157?s=64&d=mm&r=g) [Ghazanfar Abidi](http://www.bookkempt.com/)
     says:
    
    [December 14, 2018 at 4:23 am](https://chandoo.org/wp/elevator-problem/#comment-1599772)
    
    I'll try haiku..
    
    I look around me.  
    "Lady, how much do you weigh?"  
    Slap to the face. Ding!
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599772)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [December 17, 2018 at 7:07 pm](https://chandoo.org/wp/elevator-problem/#comment-1601104)
        
        haha... always a bad idea.
        
        never ask a man's  
        wealth or a woman's weight  
        to save your cheeks
        
        [Reply](https://chandoo.org/wp/elevator-problem/#comment-1601104)
        
64.  ![](https://secure.gravatar.com/avatar/2d2cc9351d173cb3f7e8d8b7fdb611354139879b0932f902fe32b54126a2ddb4?s=64&d=mm&r=g) Orlando Rainey says:
    
    [December 14, 2018 at 4:36 am](https://chandoo.org/wp/elevator-problem/#comment-1599775)
    
    My solution is given below
    
    \=IF(AND(($AA$5-COUNTA($C4:$X4) >=0),($AA$6-SUM($C4:$X4) >=0)),"YES","NO")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599775)
    
65.  ![](https://secure.gravatar.com/avatar/5671034704d280c4a557ef7ac78e92a0ae9df0246d7eb707283548ec2c7af157?s=64&d=mm&r=g) [Ghazanfar Abidi](http://www.bookkempt.com/)
     says:
    
    [December 14, 2018 at 4:41 am](https://chandoo.org/wp/elevator-problem/#comment-1599777)
    
    and I'll take a stab at the M code too:
    
    let  
    Source = Excel.CurrentWorkbook(){\[Name="Table1"\]}\[Content\],  
    #"Removed Columns" = Table.RemoveColumns(Source,{"Can go?"}),  
    #"Added Index" = Table.AddIndexColumn(#"Removed Columns", "Index", 1, 1),  
    #"Unpivoted Other Columns" = Table.UnpivotOtherColumns(#"Added Index", {"Weights", "Index"}, "Attribute", "Value"),  
    #"Grouped Rows" = Table.Group(#"Unpivoted Other Columns", {"Weights", "Index"}, {{"Count of People", each Table.RowCount(\_), type number}, {"Sum of Weight", each List.Sum(\[Weights\]), type number}}),  
    #"Added Custom" = Table.AddColumn(#"Grouped Rows", "Can go?", each if \[Count of People\] <= 20 and \[Weights\] <= 1400 then "Go" else "Stay"),  
    #"Merged Queries" = Table.NestedJoin(#"Added Index",{"Index"},#"Added Custom",{"Index"},"Added Custom",JoinKind.LeftOuter),  
    #"Expanded Added Custom" = Table.ExpandTableColumn(#"Merged Queries", "Added Custom", {"Can go?"}, {"Can go?"}),  
    #"Removed Columns1" = Table.RemoveColumns(#"Expanded Added Custom",{"Index"}),  
    #"Reordered Columns" = Table.ReorderColumns(#"Removed Columns1",{"Can go?"} & List.RemoveItems(Table.ColumnNames(#"Removed Columns1"),{"Can go?"}))  
    in  
    #"Reordered Columns"
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599777)
    
    *   ![](https://secure.gravatar.com/avatar/5671034704d280c4a557ef7ac78e92a0ae9df0246d7eb707283548ec2c7af157?s=64&d=mm&r=g) [Ghazanfar Abidi](http://www.bookkempt.com/)
         says:
        
        [December 14, 2018 at 4:55 am](https://chandoo.org/wp/elevator-problem/#comment-1599785)
        
        oh hang on. I had unpivoted the first weight column as well. fixed:
        
        let  
        Source = Excel.CurrentWorkbook(){\[Name="Table1"\]}\[Content\],  
        #"Removed Columns" = Table.RemoveColumns(Source,{"Can go?"}),  
        #"Added Index" = Table.AddIndexColumn(#"Removed Columns", "Index", 1, 1),  
        #"Unpivoted Other Columns" = Table.UnpivotOtherColumns(#"Added Index", {"Index"}, "Attribute", "Value"),  
        #"Grouped Rows" = Table.Group(#"Unpivoted Other Columns", {"Index"}, {{"Count of People", each Table.RowCount(\_), type number}, {"Sum of Weight", each List.Sum(\[Value\]), type number}}),  
        #"Added Custom" = Table.AddColumn(#"Grouped Rows", "Can go?", each if \[Count of People\] <= 20 and \[Sum of Weight\] <= 1400 then "Go" else "Stay"),  
        #"Merged Queries" = Table.NestedJoin(#"Added Index",{"Index"},#"Added Custom",{"Index"},"Added Custom",JoinKind.LeftOuter),  
        #"Expanded Added Custom" = Table.ExpandTableColumn(#"Merged Queries", "Added Custom", {"Can go?"}, {"Can go?"}),  
        #"Removed Columns1" = Table.RemoveColumns(#"Expanded Added Custom",{"Index"}),  
        #"Reordered Columns" = Table.ReorderColumns(#"Removed Columns1",{"Can go?"} & List.RemoveItems(Table.ColumnNames(#"Removed Columns1"),{"Can go?"}))  
        in  
        #"Reordered Columns"
        
        [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599785)
        
        *   ![](https://secure.gravatar.com/avatar/ac63f8b699a3bcb7d8fe4816a2d467a336f2ef57c50f5cf141d94bf6eed7d68a?s=64&d=mm&r=g) Lalit Kumar (Lucky) says:
            
            [December 14, 2018 at 6:07 am](https://chandoo.org/wp/elevator-problem/#comment-1599826)
            
            Please see the Amswer
            
            \=IF(OR(COUNT(C4:X4)GT20,SUM(C4:X4)GT1400),"Over Weight","No Problem")
            
            [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599826)
            
        *   ![](https://secure.gravatar.com/avatar/09a147a72ebae365c1d3d541afd178c0bbb16380c3cb07bebf0eb5d8807f8432?s=64&d=mm&r=g) Duncan Williamson says:
            
            [December 15, 2018 at 12:09 am](https://chandoo.org/wp/elevator-problem/#comment-1600239)
            
            I liked that Ghazanfar
            
            [Reply](https://chandoo.org/wp/elevator-problem/#comment-1600239)
            
66.  ![](https://secure.gravatar.com/avatar/a98b2418743772cd8664979dd660dcae8e325df575e81e6cfc40a118301df67f?s=64&d=mm&r=g) DOLLAR CHANDE says:
    
    [December 14, 2018 at 5:03 am](https://chandoo.org/wp/elevator-problem/#comment-1599788)
    
    \=IF(+COUNT(C4:X4)>20,"Stay",IF(SUM(C4:X4)<=1400,"Go","Stay"))
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599788)
    
67.  ![](https://secure.gravatar.com/avatar/4c8e9d80bb826d7492ed13ea3c01f591ce9d2dc7abe6ccf912030549bf2b74c0?s=64&d=mm&r=g) Pravin says:
    
    [December 14, 2018 at 5:35 am](https://chandoo.org/wp/elevator-problem/#comment-1599804)
    
    +IF(COUNT(C8:X8)LT21,IF(SUM(C8:X8)LT1400,"Go","Dontgo"),"Dontgo")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599804)
    
68.  ![](https://secure.gravatar.com/avatar/4101e40e4d18de68cab28c2b65ad08b23120aefc69c30d8d0a5c46e2ae0ba364?s=64&d=mm&r=g) Yash Lakhotia says:
    
    [December 14, 2018 at 5:51 am](https://chandoo.org/wp/elevator-problem/#comment-1599810)
    
    \=IF(AND(COUNTA(C4:X4)<$AA$5+1,SUM(C4:X4)<$AA$6+1),"GO","OVERLOAD")
    
    Copy this formula and you are good to go.
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599810)
    
69.  ![](https://secure.gravatar.com/avatar/ac63f8b699a3bcb7d8fe4816a2d467a336f2ef57c50f5cf141d94bf6eed7d68a?s=64&d=mm&r=g) Lalit Kumar (Lucky) says:
    
    [December 14, 2018 at 5:57 am](https://chandoo.org/wp/elevator-problem/#comment-1599814)
    
    Please see the answer in Below
    
    \=IF(OR(COUNT(C4:X4)GT20,SUM(C4:X4)GT1400),"Over Weight","No Problem")
    
    \=IF(OR(COUNT(C4:X4)>20,SUM(C4:X4)>1400),"Over Weight","No Problem")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599814)
    
70.  ![](https://secure.gravatar.com/avatar/4101e40e4d18de68cab28c2b65ad08b23120aefc69c30d8d0a5c46e2ae0ba364?s=64&d=mm&r=g) Yash says:
    
    [December 14, 2018 at 5:57 am](https://chandoo.org/wp/elevator-problem/#comment-1599815)
    
    \=IF(AND(COUNTA(C4:X4)<$AA$5+1,SUM(C4:X4)<$AA$6+1),"GO","OVERLOAD")
    
    Copy this formula then we are good to go.
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599815)
    
71.  ![](https://secure.gravatar.com/avatar/ac63f8b699a3bcb7d8fe4816a2d467a336f2ef57c50f5cf141d94bf6eed7d68a?s=64&d=mm&r=g) Lalit Kumar (Lucky) says:
    
    [December 14, 2018 at 6:01 am](https://chandoo.org/wp/elevator-problem/#comment-1599817)
    
    Please See the Solution.
    
    \=IF(OR(COUNT(C4:X4)GT20,SUM(C4:X4)GT1400),"Over Weight","No Problem")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599817)
    
72.  ![](https://secure.gravatar.com/avatar/bc6486dbec1637f0f58bcd34fa5f389c3a0d96abbf8e23b076b9cc0323b13029?s=64&d=mm&r=g) Barry says:
    
    [December 14, 2018 at 6:12 am](https://chandoo.org/wp/elevator-problem/#comment-1599830)
    
    I think this is the shortest so far  
    \=IF(MAX(W4\*1000,SUM(C4:V4))<1401,"Go","Stop")  
    I can't help thinking there must be some cunning back door solution that we're all missing.  
    I guess, since lifts have no way of knowing the number of people, the simplest solution is just to check the total weight.
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599830)
    
73.  ![](https://secure.gravatar.com/avatar/13421a2fd428b3813e57ab050bb245aaab89c914fd39a340a698e962ba638f41?s=64&d=mm&r=g) Vivek V Phadke says:
    
    [December 14, 2018 at 6:13 am](https://chandoo.org/wp/elevator-problem/#comment-1599834)
    
    \=IF(AND(COUNT(C4:X4)<=$AA$5,SUM(C4:X4)<=$AA$6),"Go","Stop")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599834)
    
74.  ![](https://secure.gravatar.com/avatar/38ddeaf3014737e5825f020d4782c95eade10bc2006ef340dfea800b932e09a2?s=64&d=mm&r=g) Shofiyudin Musthofa says:
    
    [December 14, 2018 at 6:14 am](https://chandoo.org/wp/elevator-problem/#comment-1599835)
    
    I use this formula to solve the Problem  
    \=IF(OR(COUNT(C4:X4)>=20,SUM(C4:X4)>1400),"CAN'T GO","CAN GO")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599835)
    
75.  ![](https://secure.gravatar.com/avatar/ac63f8b699a3bcb7d8fe4816a2d467a336f2ef57c50f5cf141d94bf6eed7d68a?s=64&d=mm&r=g) Lalit Kumar says:
    
    [December 14, 2018 at 6:14 am](https://chandoo.org/wp/elevator-problem/#comment-1599836)
    
    Please See My Answer Below:-
    
    \=IF(OR(COUNT(C4:X4)>20,SUM(C4:X4)>1400),"Over Weight","No Problem")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599836)
    
76.  ![](https://secure.gravatar.com/avatar/ac63f8b699a3bcb7d8fe4816a2d467a336f2ef57c50f5cf141d94bf6eed7d68a?s=64&d=mm&r=g) Lalit says:
    
    [December 14, 2018 at 6:18 am](https://chandoo.org/wp/elevator-problem/#comment-1599837)
    
    \=IF(OR(COUNT(C4:X4)>20,SUM(C4:X4)>1400),"Over Weight","No Problem")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599837)
    
77.  ![](https://secure.gravatar.com/avatar/13421a2fd428b3813e57ab050bb245aaab89c914fd39a340a698e962ba638f41?s=64&d=mm&r=g) Vivek V Phadke says:
    
    [December 14, 2018 at 6:20 am](https://chandoo.org/wp/elevator-problem/#comment-1599838)
    
    Sub Elevator\_Problem()  
    Range("B4:B13").Select  
    Selection.FormulaR1C1 = \_  
    "=IF(AND(COUNT(RC\[1\]:RC\[22\])<=R5C27,SUM(RC\[1\]:RC\[22\])<=R6C27),""GO"",""STOP"")"  
    Range("A1").Select  
    End Sub
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599838)
    
    *   ![](https://secure.gravatar.com/avatar/ac63f8b699a3bcb7d8fe4816a2d467a336f2ef57c50f5cf141d94bf6eed7d68a?s=64&d=mm&r=g) Lalit says:
        
        [December 14, 2018 at 6:26 am](https://chandoo.org/wp/elevator-problem/#comment-1599840)
        
        \=IF(OR(COUNT(C4:X4)>20,SUM(C4:X4)>1400),"Over Weight","No Problem")
        
        [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599840)
        
78.  ![](https://secure.gravatar.com/avatar/ac63f8b699a3bcb7d8fe4816a2d467a336f2ef57c50f5cf141d94bf6eed7d68a?s=64&d=mm&r=g) Lalit Kumar (Lucky) says:
    
    [December 14, 2018 at 6:33 am](https://chandoo.org/wp/elevator-problem/#comment-1599847)
    
    My Answer Is :-
    
    \=IF(OR(COUNT(C4:X4)>20,SUM(C4:X4)>1400),"Over Weight","No Problem")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599847)
    
79.  ![](https://secure.gravatar.com/avatar/9cd1476a8dcd39a3de1500eb90e7cd720d060ff81948ea887dc5f8417ad72a9c?s=64&d=mm&r=g) Lalit Kumar says:
    
    [December 14, 2018 at 6:36 am](https://chandoo.org/wp/elevator-problem/#comment-1599848)
    
    \=IF(OR(COUNT(C4:X4)>20,SUM(C4:X4)>1400),"Over Weight","No Problem")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599848)
    
80.  ![](https://secure.gravatar.com/avatar/ac63f8b699a3bcb7d8fe4816a2d467a336f2ef57c50f5cf141d94bf6eed7d68a?s=64&d=mm&r=g) Lalit Kumar says:
    
    [December 14, 2018 at 6:41 am](https://chandoo.org/wp/elevator-problem/#comment-1599850)
    
    \=IF(OR(COUNT(C4:X4)>20,SUM(C4:X4)>1400),"Over Weight","No Problem")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599850)
    
81.  ![](https://secure.gravatar.com/avatar/0e20a472ed08068b9478da3e178820a2dbca6273885c38d5751463804b5f48c2?s=64&d=mm&r=g) [Mukes Bajaj](http://No%20One)
     says:
    
    [December 14, 2018 at 6:53 am](https://chandoo.org/wp/elevator-problem/#comment-1599856)
    
    \=IF(OR(COUNTA(C4:X4)>$AB$5),"Kidar Vadi Janda ae",IF(COUNTA(C4:X4)=$AB$5,"Massa hi bacheya haan",IF(SUM(C4:X4)>$AB$6,"Marr gya ee oa","ok")))
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599856)
    
82.  ![](https://secure.gravatar.com/avatar/3551b930cfba12d01dd5e65527f1fd19dcb0b29f2e3afcb8044b4ab37d9ef9e5?s=64&d=mm&r=g) satish says:
    
    [December 14, 2018 at 6:56 am](https://chandoo.org/wp/elevator-problem/#comment-1599859)
    
    for easy understood i create Working Note  
    i add  
    total count in Y column  
    total weight in z column  
    and my formula is  
    \=AND(Z4<1400,Y4<20)
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599859)
    
83.  ![](https://secure.gravatar.com/avatar/c964794b86ec530b30c6be1eb728481b05f405ffdacf43fb4c030b5023d3a2d6?s=64&d=mm&r=g) yogi says:
    
    [December 14, 2018 at 6:58 am](https://chandoo.org/wp/elevator-problem/#comment-1599860)
    
    '=+IF(AND(IF(COUNT(F4:AA4)<=AD5,1,0),IF(SUM(F4:AA4)<=AD6,1,0)),1,0)
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599860)
    
84.  ![](https://secure.gravatar.com/avatar/2cd93435a7b0c133ff5dfb79cbd6c85e192ac9ba2b557d63e36b4de72c3cf76d?s=64&d=mm&r=g) Mehar Ali Khatri says:
    
    [December 14, 2018 at 7:00 am](https://chandoo.org/wp/elevator-problem/#comment-1599862)
    
    \=IF(OR(COUNT(C4:X4)>$AA$5,SUM(C4:X4)>$AA$6),"Stop","Go")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599862)
    
85.  ![](https://secure.gravatar.com/avatar/e722f69f28bc8fcb01413f8606ac814ba6b36574e3db7848b1bc3be6c5138458?s=64&d=mm&r=g) Samir Kothari says:
    
    [December 14, 2018 at 7:15 am](https://chandoo.org/wp/elevator-problem/#comment-1599871)
    
    \=IF(COUNT(C4:X4)>$AA$5,"Stay",IF(SUM(C4:X4)>$AA$6,"Stay","Go"))
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599871)
    
86.  ![](https://secure.gravatar.com/avatar/846c312afee6f5c2c5b059a7016990afe90d019a23748836902a8920f81e4e95?s=64&d=mm&r=g) [Ashutosh Pathak](http://www.ashutoshp.in/)
     says:
    
    [December 14, 2018 at 7:41 am](https://chandoo.org/wp/elevator-problem/#comment-1599884)
    
    \=IF(AND(SUM(C4:X4)> 1400,COUNT(C4:X4)<21),"UP","Down")
    
    Looking for a more efficient solution.
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599884)
    
87.  ![](https://secure.gravatar.com/avatar/beddc20ac0fb8fbbbca6a5a93a24d7b93c7cf6a97b003c0a2f0b8eb075cf24e8?s=64&d=mm&r=g) Manoj Aggarwal says:
    
    [December 14, 2018 at 7:59 am](https://chandoo.org/wp/elevator-problem/#comment-1599894)
    
    \=IF(AND(COUNT(C4:X4)<=20,SUM(C4:X4)<=1400),"Go","Stop")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599894)
    
88.  ![](https://secure.gravatar.com/avatar/252b44785658c1d459827c0a2b3bcc4672abd1c82192dd5e5d8736038ef786cc?s=64&d=mm&r=g) Martin says:
    
    [December 14, 2018 at 8:06 am](https://chandoo.org/wp/elevator-problem/#comment-1599897)
    
    \=IF(OR(COUNT(C4:X4) GT 20,SUM(C4:X4) GT 1400),"Don't go","GO")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599897)
    
89.  ![](https://secure.gravatar.com/avatar/20dabe59b014cca95afa7f46c9c18dea6b8b99d5a6294e959e98a9cb0520dd1d?s=64&d=mm&r=g) Gary Skelton says:
    
    [December 14, 2018 at 8:10 am](https://chandoo.org/wp/elevator-problem/#comment-1599899)
    
    Hi,
    
    \=IF(IF(SUM(C4:X4)>$AA$6,1,0)+IF(COUNTA(C4:X4)>$AA$5,1,0)=2,"Stay","Go")
    
    Gaz
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599899)
    
90.  ![](https://secure.gravatar.com/avatar/fc302c0da55d7b843f31257d9b2064ce8c9e66060b1aeeb573b8a8bd6f883ef3?s=64&d=mm&r=g) xaratsarhs says:
    
    [December 14, 2018 at 8:10 am](https://chandoo.org/wp/elevator-problem/#comment-1599900)
    
    \=IF(AND((COUNT(C4:X4)<=$AA$5);(SUM(C4:X4)<=$AA$6));"Yes";"No")
    
    and conditional formatting (Green=Yes, Red=No) more easy to read a large table
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599900)
    
91.  ![](https://secure.gravatar.com/avatar/90d7e7946f17954542b67f21385a26fc807c6766d484e89fbd0c247d5d3d60cc?s=64&d=mm&r=g) pavan says:
    
    [December 14, 2018 at 8:16 am](https://chandoo.org/wp/elevator-problem/#comment-1599901)
    
    \=IF(OR(COUNT(C4:X4)>20,SUM( C4:X4)>1400),"can't go","Can go")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599901)
    
92.  ![](https://secure.gravatar.com/avatar/5727664da35eca4ec97f8ec175e9dad07762ea3e597cb56dd8e1e241902971f4?s=64&d=mm&r=g) [Vitalie Ciobanu](https://systemmanagement.ro/)
     says:
    
    [December 14, 2018 at 8:27 am](https://chandoo.org/wp/elevator-problem/#comment-1599908)
    
    \=IF(OR(\[@SumWeight\]>=MaxWeight,\[@CountPeople\]>=MaxPeople,\[@WeightErrorCheck\]="TRUE"),"Stay","Go")
    
    Where:  
    PeopleWeight is the name of the converted range to Table. This table has 3 additional columns added to avoid having one long IF formula and split the calculations into more smaller steps (useful when there will be a new person checking this in several years).  
    @SumWeight is =SUM(PeopleWeight\[@\[W1\]:\[W22\]\])  
    @CountPeople is =COUNT(PeopleWeight\[@\[W1\]:\[W22\]\])  
    @WeightErrorCheck is =IF(\[@SumWeight\]<0,"TRUE","FALSE")  
    MaxWeight and MaxPeople are cell names of your provided conditions.
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599908)
    
93.  ![](https://secure.gravatar.com/avatar/f6f45d974436b80f49ef8c4c6293a0cfb410050110010041f9b5d64bc43923f8?s=64&d=mm&r=g) Mihail Iadkov says:
    
    [December 14, 2018 at 8:38 am](https://chandoo.org/wp/elevator-problem/#comment-1599915)
    
    \=IF(AND(COUNTA(C4:X4)LT$AA$5;SUM(C4:X4)LT$AA$6);"Yes";"No")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599915)
    
94.  ![](https://secure.gravatar.com/avatar/f6ddcd947a120d4bef47a3ee7540bd5a83c31d96e7f0b94379362b58919c79a4?s=64&d=mm&r=g) Sujan Gurung says:
    
    [December 14, 2018 at 9:02 am](https://chandoo.org/wp/elevator-problem/#comment-1599929)
    
    In conclusion out of 10 elevator trips 6 is a GO and 4 STAY
    
    \=IFERROR(IF(AND(COUNTA(C4:X4)<=$AA$5,SUM(C4:X4)<=$AA$6),"GO","STAY"),"")
    
    Above is the formula I used and this gives me the right criteria
    
    Another is quite a long way where I added the total weight and counted the number of individuals in each trip. I then used the nested IF statement to check the criteria to see if it fitted or not
    
    Any feedbacks is highly appreciated
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599929)
    
95.  ![](https://secure.gravatar.com/avatar/7f14c294e227b7563468db2db4048f5e10fc997779cf209d2a0ce18131e7e9e9?s=64&d=mm&r=g) Ronak says:
    
    [December 14, 2018 at 9:10 am](https://chandoo.org/wp/elevator-problem/#comment-1599935)
    
    \=+IF(OR(COUNT(C4:X4)>$AA$5,SUM(C4:X4)>$AA$6),"Stop","Go")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599935)
    
96.  ![](https://secure.gravatar.com/avatar/ee5967b18f6c3990837b66dec87bc59723e293dec6f6253ceedea30e1e1ebf99?s=64&d=mm&r=g) Deepa R says:
    
    [December 14, 2018 at 9:25 am](https://chandoo.org/wp/elevator-problem/#comment-1599940)
    
    \=IF(OR(SUM(C4:X4)>$AA$6,COUNTA(C4:X4)>$AA$5),"Stop","Go")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599940)
    
97.  ![](https://secure.gravatar.com/avatar/4ab61da8c422b301ff4d4f68e89839551a6c4f55e9915bad29dac480a30288fd?s=64&d=mm&r=g) Ignacio De Bustamante says:
    
    [December 14, 2018 at 9:27 am](https://chandoo.org/wp/elevator-problem/#comment-1599943)
    
    \=SI(Y(SUMA(C4:X4)<=1400;CONTAR(C4;X4)<=20);"YES";"NO")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599943)
    
98.  ![](https://secure.gravatar.com/avatar/14f9c09fb421a06d1b50abd6e262c54e2f6d626ed3a4889a3577ef383bd19202?s=64&d=mm&r=g) Alain Van Holder says:
    
    [December 14, 2018 at 10:23 am](https://chandoo.org/wp/elevator-problem/#comment-1599963)
    
    \=IF(AND(COUNT($C4:$X4)<=$AA$5;SUM($C4:$X4)<=$AA$6);"Go";"Stay")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599963)
    
99.  ![](https://secure.gravatar.com/avatar/ac63f8b699a3bcb7d8fe4816a2d467a336f2ef57c50f5cf141d94bf6eed7d68a?s=64&d=mm&r=g) Lalit Kumar says:
    
    [December 14, 2018 at 10:41 am](https://chandoo.org/wp/elevator-problem/#comment-1599978)
    
    Please see my answer
    
    \=IF(OR(COUNT(C4:X4)>20,SUM(C4:X4)>1400),"Over Weight","No Problem")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599978)
    
100.  ![](https://secure.gravatar.com/avatar/933af19ea2900dc30e8190d61090c8e2ec610d710ee583429c5880bf860ba1b0?s=64&d=mm&r=g) Vijay says:
    
    [December 14, 2018 at 11:18 am](https://chandoo.org/wp/elevator-problem/#comment-1599993)
    
    \=IF(OR(COUNT(C4:X4)>AA$5,SUM(C4:X4)>AA$6),"Can't Go", "Can Go")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1599993)
    
101.  ![](https://secure.gravatar.com/avatar/8f7af946a8fae19829e98a8e7c01c0a4b5789fcfe4215061dffb62a2cc747715?s=64&d=mm&r=g) jim says:
    
    [December 14, 2018 at 12:25 pm](https://chandoo.org/wp/elevator-problem/#comment-1600042)
    
    right, I've got tired of seeing the same solutions here  
    please, if you've nothing original to offer then just read, enjoy and don't feel the need to "metoo"  
    having said that, I've tried to find the shortest solution to the problem as it stands (in terms of typing - it might have various shortcomings, but it's a more interesting challenge):
    
    \=W4+(SUM(C4:V4)%>14)
    
    only 20 characters; if the result's 0, then it's ok to go
    
    loved the haiku
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1600042)
    
    *   ![](https://secure.gravatar.com/avatar/09a147a72ebae365c1d3d541afd178c0bbb16380c3cb07bebf0eb5d8807f8432?s=64&d=mm&r=g) Duncan Williamson says:
        
        [December 15, 2018 at 12:18 am](https://chandoo.org/wp/elevator-problem/#comment-1600242)
        
        This breaks in rows 8 and 13. Don't forget the table extends to column X
        
        [Reply](https://chandoo.org/wp/elevator-problem/#comment-1600242)
        
        *   ![](https://secure.gravatar.com/avatar/8f7af946a8fae19829e98a8e7c01c0a4b5789fcfe4215061dffb62a2cc747715?s=64&d=mm&r=g) jim says:
            
            [December 16, 2018 at 8:58 pm](https://chandoo.org/wp/elevator-problem/#comment-1600522)
            
            How so?  
            if there are entries in column W and X then it has already failed due to too many occupants
            
            [Reply](https://chandoo.org/wp/elevator-problem/#comment-1600522)
            
            *   ![](https://secure.gravatar.com/avatar/09a147a72ebae365c1d3d541afd178c0bbb16380c3cb07bebf0eb5d8807f8432?s=64&d=mm&r=g) Duncan Williamson says:
                
                [December 16, 2018 at 11:07 pm](https://chandoo.org/wp/elevator-problem/#comment-1600574)
                
                Your formula does work but I would expect to see 0 or 1 as outputs rather than 0 and 1 or 62 or 65 as happens in your case. Still, it does work at that level. I know there is no rule in this case to say you did anything wrong but I think modelling best practice is against you.
                
                My point about using columns W and X is that I can see no mechanism in Chandoo's case that says cells cannot be left blank, even by accident. Moreover, whilst you have caught the >20 and >1400 rule breaks, by essentially ignoring everything to the right of column V, you might not be catching all data ... for model review and revision/auditing and so on
                
                [Reply](https://chandoo.org/wp/elevator-problem/#comment-1600574)
                
                *   ![](https://secure.gravatar.com/avatar/8f7af946a8fae19829e98a8e7c01c0a4b5789fcfe4215061dffb62a2cc747715?s=64&d=mm&r=g) jim says:
                    
                    [December 16, 2018 at 11:15 pm](https://chandoo.org/wp/elevator-problem/#comment-1600583)
                    
                    hence my caveat about shortcomings  
                    see my earlier entry for a "better" solution  
                    I was just trying to make this more of a challenge by minimising the formula size/computations
                    
    *   ![](https://secure.gravatar.com/avatar/d1a17d3aca90e081365b9dff8241ee5356ce0958b0580c0c88e2b6289452af6a?s=64&d=mm&r=g) Harold says:
        
        [January 4, 2019 at 4:23 am](https://chandoo.org/wp/elevator-problem/#comment-1608915)
        
        While this works OK  
        You could silence your critics;  
        Wrap it all with NOT()  
        \~~~  
        \=NOT(W4+(SUM(C4:V4)%>14))
        
        [Reply](https://chandoo.org/wp/elevator-problem/#comment-1608915)
        
        *   ![](https://secure.gravatar.com/avatar/8f7af946a8fae19829e98a8e7c01c0a4b5789fcfe4215061dffb62a2cc747715?s=64&d=mm&r=g) jim says:
            
            [January 9, 2019 at 8:31 am](https://chandoo.org/wp/elevator-problem/#comment-1611049)
            
            thanks for your comment  
            I refer you to above  
            re my caveat
            
            [Reply](https://chandoo.org/wp/elevator-problem/#comment-1611049)
            
102.  ![](https://secure.gravatar.com/avatar/e7049505fa672b2be1346f3559f2baf8fa7942cc8dbc89be8fd20d787d5ea1d0?s=64&d=mm&r=g) [Pandurangarao](http://na/)
     says:
    
    [December 14, 2018 at 1:46 pm](https://chandoo.org/wp/elevator-problem/#comment-1600074)
    
    '=IF(AND(COUNT($C4:$X4)<=$AA$5,SUM($C4:$X4)<=$AA$6),"GO","STOP")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1600074)
    
103.  ![](https://secure.gravatar.com/avatar/2d30a81c231885bd119fce196b30f931efe5d99c73136fdcb309ab329f2da3ac?s=64&d=mm&r=g) Marcelo Alencar says:
    
    [December 14, 2018 at 3:56 pm](https://chandoo.org/wp/elevator-problem/#comment-1600139)
    
    \=IF(COUNT(C4:X4)>=$AA$5,"Stop",IF(SUM(C4:X4)>=$AA$6,"STOP","GO"))
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1600139)
    
104.  ![](https://secure.gravatar.com/avatar/aee5f5b568c6f3d309e4d5d53b9a98535fd42577d69f12c7476579f35d62842a?s=64&d=mm&r=g) David N says:
    
    [December 14, 2018 at 4:06 pm](https://chandoo.org/wp/elevator-problem/#comment-1600144)
    
    One note and one suggestion...
    
    My note: None of the sets in your original data resulted in a group that was under on weight but over on people, so I personally reduced some numbers in the last row to create that scenario.
    
    My suggestion: You typically throw in a challenge question when you give a relatively simple homework assignment, so how about something like writing a single formula to return the number of groups that would receive a Yes/Go response?
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1600144)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [December 17, 2018 at 7:10 pm](https://chandoo.org/wp/elevator-problem/#comment-1601105)
        
        Hi David... Good ones. I keep the challenge posts "gettable" to encourage discussion and creativity. For really hard challenges, check out either formula forensics or challenges pages.
        
        [https://chandoo.org/wp/formula-forensics-homepage/](https://chandoo.org/wp/formula-forensics-homepage/)
          
        [https://chandoo.org/wp/category/excel-challenges/](https://chandoo.org/wp/category/excel-challenges/)
        
        And yes, of course, how would you write a single formula to count number of "go"s in the data?
        
        [Reply](https://chandoo.org/wp/elevator-problem/#comment-1601105)
        
        *   ![](https://secure.gravatar.com/avatar/aee5f5b568c6f3d309e4d5d53b9a98535fd42577d69f12c7476579f35d62842a?s=64&d=mm&r=g) David N says:
            
            [December 19, 2018 at 8:10 pm](https://chandoo.org/wp/elevator-problem/#comment-1601849)
            
            Array entered...  
            {=SUMPRODUCT((MMULT(SIGN(C4:X13),TRANSPOSE(SIGN(COLUMN(C3:X3))))<=AA5)\*(MMULT(1\*C4:X13,TRANSPOSE(SIGN(COLUMN(C3:X3))))<=AA6))}
            
            [Reply](https://chandoo.org/wp/elevator-problem/#comment-1601849)
            
            *   ![](https://secure.gravatar.com/avatar/09a147a72ebae365c1d3d541afd178c0bbb16380c3cb07bebf0eb5d8807f8432?s=64&d=mm&r=g) Duncan Williamson says:
                
                [December 20, 2018 at 12:34 am](https://chandoo.org/wp/elevator-problem/#comment-1601923)
                
                David, your formula returns 3 when I say there are 6 go rows! Yes, CSE entered.
                
                [Reply](https://chandoo.org/wp/elevator-problem/#comment-1601923)
                
                *   ![](https://secure.gravatar.com/avatar/aee5f5b568c6f3d309e4d5d53b9a98535fd42577d69f12c7476579f35d62842a?s=64&d=mm&r=g) David N says:
                    
                    [December 21, 2018 at 2:34 pm](https://chandoo.org/wp/elevator-problem/#comment-1602350)
                    
                    I've triple checked, including copying the formula out of my post back into Excel, and it returns 6 for me, which I agree is the correct answer. So I'm not sure what might be happening on your end unless there is some bizarre difference in a regional setting between our computers that could be throwing something off. And I'm using Excel 2013 in case that matters.
                    
105.  ![](https://secure.gravatar.com/avatar/34ef8e6463cdcf1d540c34264f2a43391851f3f2e7802be4ec1bd11c980cf23a?s=64&d=mm&r=g) Xiq says:
    
    [December 14, 2018 at 4:46 pm](https://chandoo.org/wp/elevator-problem/#comment-1600167)
    
    A Boolean version:  
    \=((W4+X4)=0)\*(SUM(C4:V4)0
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1600167)
    
    *   ![](https://secure.gravatar.com/avatar/09a147a72ebae365c1d3d541afd178c0bbb16380c3cb07bebf0eb5d8807f8432?s=64&d=mm&r=g) Duncan Williamson says:
        
        [December 15, 2018 at 12:26 am](https://chandoo.org/wp/elevator-problem/#comment-1600246)
        
        Did you mean
        
        \=((W4+X4)=0)\*(SUM(C4:V4)=0)?
        
        [Reply](https://chandoo.org/wp/elevator-problem/#comment-1600246)
        
        *   ![](https://secure.gravatar.com/avatar/8f7af946a8fae19829e98a8e7c01c0a4b5789fcfe4215061dffb62a2cc747715?s=64&d=mm&r=g) jim says:
            
            [December 16, 2018 at 9:07 pm](https://chandoo.org/wp/elevator-problem/#comment-1600525)
            
            might be what he meant, might not; but neither version would work  
            \=((W4+X4)=0)\*(SUM(C4:V4)<1400) would however
            
            [Reply](https://chandoo.org/wp/elevator-problem/#comment-1600525)
            
            *   ![](https://secure.gravatar.com/avatar/09a147a72ebae365c1d3d541afd178c0bbb16380c3cb07bebf0eb5d8807f8432?s=64&d=mm&r=g) Duncan Williamson says:
                
                [December 16, 2018 at 11:09 pm](https://chandoo.org/wp/elevator-problem/#comment-1600578)
                
                No, it doesn't work but I was asking him if that's what he had intended. Maybe not so smart on my part.  
                In terms of best practice, we really should address AA5 and AA6 rather than hard coding the 20 and the 1400 cut offs. I just checked and I realise I am guilty of the same crime with my effort!
                
                [Reply](https://chandoo.org/wp/elevator-problem/#comment-1600578)
                
        *   ![](https://secure.gravatar.com/avatar/34ef8e6463cdcf1d540c34264f2a43391851f3f2e7802be4ec1bd11c980cf23a?s=64&d=mm&r=g) Xiq says:
            
            [December 27, 2018 at 10:19 am](https://chandoo.org/wp/elevator-problem/#comment-1605415)
            
            My apologies... something went wrong with my copy/paste skills :S
            
            This is the formula I was talking about:  
            \=((W4+X4)=0)\*(SUM(C4:V4)<=1400)
            
            [Reply](https://chandoo.org/wp/elevator-problem/#comment-1605415)
            
106.  ![](https://secure.gravatar.com/avatar/d8c6065d3b1470289dee4efa2fed905eb4dcc39933333cb956af748f39d1c65e?s=64&d=mm&r=g) Garu says:
    
    [December 14, 2018 at 5:05 pm](https://chandoo.org/wp/elevator-problem/#comment-1600176)
    
    \=IF((AND(SUM(C4:X4) LT 1400, COUNTA(C4:X4))), "Go", "Stop")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1600176)
    
107.  ![](https://secure.gravatar.com/avatar/b3bc1ac59881f0ec6844932e136e419fc2f9172f557878c7472b5aafdc7bc073?s=64&d=mm&r=g) Chris Hartnell says:
    
    [December 14, 2018 at 5:07 pm](https://chandoo.org/wp/elevator-problem/#comment-1600177)
    
    \=IF(AND(COUNT(C4:X4)LT=$AA$5,SUM(C4:X4)LT=$AA$6),"Go","Stay")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1600177)
    
108.  ![](https://secure.gravatar.com/avatar/4e552444485da8966fe655a6cfea908aa27522e0b625c7dfcc0ece8ca4284fbe?s=64&d=mm&r=g) Greg says:
    
    [December 14, 2018 at 5:57 pm](https://chandoo.org/wp/elevator-problem/#comment-1600194)
    
    \=IF(AND(COUNT(C4:X4)<21,SUM(C4:X4)<1401),"Go","Stop")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1600194)
    
109.  ![](https://secure.gravatar.com/avatar/4f3d74106b05c999007661cff5d8cf1b6a40541bb0aa9fc65dec4056fa43f720?s=64&d=mm&r=g) Nicholas Voisin says:
    
    [December 14, 2018 at 7:37 pm](https://chandoo.org/wp/elevator-problem/#comment-1600211)
    
    \=IF(OR(COUNT(C4:X4)>=$AA$5,SUM(C4:X4)>=$AA$6)=TRUE,"NO","YES")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1600211)
    
110.  ![](https://secure.gravatar.com/avatar/a369c1237e1d145097ca2fce09caed632bff3fe754d2407ddc06346fbbdf3ebd?s=64&d=mm&r=g) Vane Hugo says:
    
    [December 14, 2018 at 8:50 pm](https://chandoo.org/wp/elevator-problem/#comment-1600220)
    
    formula pasted in column B  
    this example is for row 4  
    \=IF(W4gt0,"Stay",IF(SUM(C4:V4)gt1400,"Stay","Go"))
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1600220)
    
111.  ![](https://secure.gravatar.com/avatar/743a885fe3cb7ca2dbd023ad5e6ee456019017618cd54e3176ede1a9ebbd2368?s=64&d=mm&r=g) Maciej says:
    
    [December 14, 2018 at 9:53 pm](https://chandoo.org/wp/elevator-problem/#comment-1600224)
    
    _  
    \=OR(SUM(C4:INDIRECT("R"&TEXT(ROW(C4),"#")&"C"&TEXT(COLUMN(C4)+$AA$5,"#");FALSE))LT=$AA$6;ISBLANK(INDIRECT("R"&TEXT(ROW(C4),"#")&"C"&TEXT(COLUMN(C4)+$AA$5,"#");FALSE)))_
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1600224)
    
112.  ![](https://secure.gravatar.com/avatar/799fe12f1dfcf8066a1f677fe30d9188533af94ee828d6c5c3e6a6ae29ae5ba8?s=64&d=mm&r=g) Fred says:
    
    [December 14, 2018 at 10:02 pm](https://chandoo.org/wp/elevator-problem/#comment-1600226)
    
    \=IF(OR(SUM(C4:X4)>1400;COUNTA(C4:X4)>20);"no-go"; "GO")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1600226)
    
113.  ![](https://secure.gravatar.com/avatar/13fb8ae02956d31f98b09b87f6bdc61d31fd8468401ddc0145708caeab72f74e?s=64&d=mm&r=g) ALTUG ALTINTAS says:
    
    [December 15, 2018 at 9:42 am](https://chandoo.org/wp/elevator-problem/#comment-1600307)
    
    \=IF(SUM(C4:X4)<$AA$6,IF(COUNT(C4:X4)<$AA$5,"Y","N"),"N")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1600307)
    
114.  ![](https://secure.gravatar.com/avatar/2f996d86d80cf621bd1aea0f994874bdb903b6214e2d47f0bf88159d8003394d?s=64&d=mm&r=g) Khaled Abdel Aziz says:
    
    [December 16, 2018 at 1:47 pm](https://chandoo.org/wp/elevator-problem/#comment-1600461)
    
    \=IF(AND((COUNT(C4:X4)LT=20),(SUM(C4:X4)LT=1400)),"UP", "Down")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1600461)
    
115.  ![](https://secure.gravatar.com/avatar/df1c03e03a5aaebff204c0b4a5ff3e776f363f8e9f11cafe5db70dbb2b92c329?s=64&d=mm&r=g) Avi says:
    
    [December 16, 2018 at 2:08 pm](https://chandoo.org/wp/elevator-problem/#comment-1600464)
    
    \=IF(AND(SUM(C4:X4)<=1400,COUNT(C4:X4)<=20),"YES","NO")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1600464)
    
116.  ![](https://secure.gravatar.com/avatar/918ae1dbc9ae88a17ecd5628e6ec975131080a1a7996a403036b79b8bf95c4ee?s=64&d=mm&r=g) Mariya says:
    
    [December 16, 2018 at 9:04 pm](https://chandoo.org/wp/elevator-problem/#comment-1600523)
    
    Hello,
    
    Thank you for this interesting task.  
    Here is my solution:  
    \=IF(COUNT(C4:X4)>=20;"not allowed"; IF(SUM(C4:X4)>=1400; "not allowed"; "ok"))  
    So far it works. Now I am going to check what are the other's solutions. I wanna more ;-)))
    
    Mariya
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1600523)
    
    *   ![](https://secure.gravatar.com/avatar/dbe5fe9b8ba486819807f258056bac6d4d1a90ced42c914e1ddadf815ff65748?s=64&d=mm&r=g) Giancarlo says:
        
        [December 16, 2018 at 9:28 pm](https://chandoo.org/wp/elevator-problem/#comment-1600530)
        
        \=IF(SUM(C4:X4)/($AA$6/$AA$5)>$AA$5,"Stay","Go")
        
        [Reply](https://chandoo.org/wp/elevator-problem/#comment-1600530)
        
117.  ![](https://secure.gravatar.com/avatar/dbe5fe9b8ba486819807f258056bac6d4d1a90ced42c914e1ddadf815ff65748?s=64&d=mm&r=g) Gian All says:
    
    [December 16, 2018 at 9:30 pm](https://chandoo.org/wp/elevator-problem/#comment-1600531)
    
    \=IF(SUM(C4:X4)/($AA$6/$AA$5)>$AA$5,"Stay","Go")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1600531)
    
118.  ![](https://secure.gravatar.com/avatar/dbe5fe9b8ba486819807f258056bac6d4d1a90ced42c914e1ddadf815ff65748?s=64&d=mm&r=g) Giancarlo says:
    
    [December 16, 2018 at 9:37 pm](https://chandoo.org/wp/elevator-problem/#comment-1600535)
    
    \=IF(SUM(C4:X4)/($AA$6/$AA$5)>$AA$5,"Stay","Go")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1600535)
    
119.  ![](https://secure.gravatar.com/avatar/0ceda4ad2f79f67afb17ede30f4332b1f4d69e7c4136dd0f0d35036f221e2be4?s=64&d=mm&r=g) Giancarlo says:
    
    [December 16, 2018 at 9:39 pm](https://chandoo.org/wp/elevator-problem/#comment-1600536)
    
    \=IF(SUM(C4:X4)/($AA$6/$AA$5)>$AA$5,"Stay","Go")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1600536)
    
120.  ![](https://secure.gravatar.com/avatar/0798d5bfb6f9ba0ac2543ff3a144c66004ae7eb203bd1addc9c0bfbe7c674db0?s=64&d=mm&r=g) Eva says:
    
    [December 17, 2018 at 6:34 am](https://chandoo.org/wp/elevator-problem/#comment-1600802)
    
    \=IF(AND(IF(SUM(C4:X4)>$AA$6,"Too heavy","ok")="ok",IF(COUNT(C4:X4)>$AA$5,"Too many","ok")="ok"),"Go","Stay")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1600802)
    
121.  ![](https://secure.gravatar.com/avatar/c49cdf43394dcf1ce389389fe2f0f66f808dad76fbff5d6fcda1b9f1dc940533?s=64&d=mm&r=g) ALBERTO OLEOTTI says:
    
    [December 17, 2018 at 10:42 am](https://chandoo.org/wp/elevator-problem/#comment-1600916)
    
    My answer is  
    \=IF(OR(AC4>AD3;AD4>20);"Overweight";"In weight")  
    where AD3 is 1400 and AD4 is =COUNTA(C4:X4)
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1600916)
    
122.  ![](https://secure.gravatar.com/avatar/7cd07cb10151004da8833c6e5198de74bd6a9b7428659121b192b2eeae6d99e6?s=64&d=mm&r=g) Suraj Nair says:
    
    [December 17, 2018 at 12:05 pm](https://chandoo.org/wp/elevator-problem/#comment-1600949)
    
    \=IF(AND(COUNTA($C4:$X4)<=$AA$5,SUM($C4:$X4)<=$AA$6),"UP","DOWN")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1600949)
    
123.  ![](https://secure.gravatar.com/avatar/c49cdf43394dcf1ce389389fe2f0f66f808dad76fbff5d6fcda1b9f1dc940533?s=64&d=mm&r=g) ALBERTO says:
    
    [December 17, 2018 at 1:17 pm](https://chandoo.org/wp/elevator-problem/#comment-1600985)
    
    \=SE(E(SOMMA(C4:X4)<=AA6;CONTA.VALORI(C4:X4)<=AA5);"OK";"OVER WEIGHT")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1600985)
    
124.  ![](https://secure.gravatar.com/avatar/7951ed9129b695df383f11a8e799a70cded039b33715f45bd71d2bc8d875d31d?s=64&d=mm&r=g) Chirayu says:
    
    [December 17, 2018 at 1:30 pm](https://chandoo.org/wp/elevator-problem/#comment-1600990)
    
    True = Go, False = No Go
    
    \=AND(SUM(C4:X4)<=$AA$6,COUNT(C4:X4)<=$AA$5)
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1600990)
    
125.  ![](https://secure.gravatar.com/avatar/472306d3913d011b554c0208e8f9f6e5e024f854b420e98f9f0805ca0a337cd6?s=64&d=mm&r=g) Kayak6000 says:
    
    [December 17, 2018 at 1:37 pm](https://chandoo.org/wp/elevator-problem/#comment-1600995)
    
    IF(SUM(C4:S4) LT or equal to $AA$6,IF(COUNT(C4:X4) LT or equal to AA$5,"Lift going up / down", "Burp!!! too heavy or too many people"))
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1600995)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [December 17, 2018 at 7:12 pm](https://chandoo.org/wp/elevator-problem/#comment-1601108)
        
        My friend always said, "a burp is never a good idea in public, unless you are in a lift, then it is better than a fart."
        
        [Reply](https://chandoo.org/wp/elevator-problem/#comment-1601108)
        
126.  ![](https://secure.gravatar.com/avatar/d4a39a29ba251034f960a5e17b104a974f23ec9d9afdf2dc5ae6b92b3081e062?s=64&d=mm&r=g) Chihiro says:
    
    [December 17, 2018 at 8:36 pm](https://chandoo.org/wp/elevator-problem/#comment-1601141)
    
    Set Total\_People and Total\_Weight as named range (vTP & vTW). Pass that onto PQ.  
    Ex: TP = Excel.CurrentWorkbook(){\[Name="vTP"\]}\[Content\]{0}\[Column1\]
    
    Add 0 based index column.
    
    Then add custom column:  
    \=if (List.Sum(Record.ToList(#"Added Index"{\[Index\]}))-\[Index\])<=TW and (List.Count(List.RemoveNulls(Record.ToList(#"Added Index"{\[Index\]}))) - 1) <=TP then "yes" else "no"
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1601141)
    
127.  ![](https://secure.gravatar.com/avatar/a6f1611e3662f47a099a6077e1d139cd2f313290e84ea5bb44350a8768715256?s=64&d=mm&r=g) GC Excel says:
    
    [December 18, 2018 at 2:56 am](https://chandoo.org/wp/elevator-problem/#comment-1601295)
    
    A VBA formula that will return True or False and that will work for any number of cells in the specified range and also if there are blank values (or empty cell between values).
    
    In Excel :  
    \=cango(C4:X4,$AA$5,$AA$6)
    
    VBA Formula =  
    Function CanGo(Weights As Variant, MaxPeople As Integer, MaxWeight As Integer) As Boolean
    
    CanGo = UBound(Split(Replace(Join(Application.Transpose(Application.Transpose(Weights)), "|"), "||", ""), "|")) <= MaxPeople \_  
    And WorksheetFunction.Sum(Weights) <= MaxWeight
    
    End Function
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1601295)
    
128.  ![](https://secure.gravatar.com/avatar/a6f1611e3662f47a099a6077e1d139cd2f313290e84ea5bb44350a8768715256?s=64&d=mm&r=g) GC Excel says:
    
    [December 18, 2018 at 3:02 am](https://chandoo.org/wp/elevator-problem/#comment-1601297)
    
    Hmmm. Forget previous comment...  
    VBA formula can be much much simpler :-O
    
    In Excel:  
    \=CanGo(C4:X4,$AA$5,$AA$6)
    
    In VBA:  
    Function CanGo(Weights As Variant, MaxPeople As Integer, MaxWeight As Integer) As Boolean
    
    With WorksheetFunction  
    CanGo = .CountA(Weights) <= MaxPeople And .Sum(Weights) <= MaxWeight  
    End With
    
    End Function
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1601297)
    
129.  ![](https://secure.gravatar.com/avatar/40cebd813d550efcd70813c0b407fe0022c950fedbbac7f39e5fa23a680a8f4c?s=64&d=mm&r=g) Arvinder Sahni says:
    
    [December 19, 2018 at 12:58 pm](https://chandoo.org/wp/elevator-problem/#comment-1601759)
    
    \=IF(AND(COUNT(C4:X4)<20,SUM(C4:X4)<1400),"UP","Stay")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1601759)
    
130.  ![](https://secure.gravatar.com/avatar/9db0ba26c73be599e26d365e5775c8b253b3b330eafff9ef2dc4089ece6daf73?s=64&d=mm&r=g) Francis says:
    
    [December 20, 2018 at 8:42 am](https://chandoo.org/wp/elevator-problem/#comment-1602006)
    
    \=IF(AND(SUM(C4:X4)<=1400,COUNT(C4:X4)<=20),"Yes","No")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1602006)
    
131.  ![](https://secure.gravatar.com/avatar/ce7106cfd406deda8e930395f2500f4f475abf9d52cd3e0b31cc8d7a998ec803?s=64&d=mm&r=g) GraH says:
    
    [December 20, 2018 at 5:33 pm](https://chandoo.org/wp/elevator-problem/#comment-1602088)
    
    Conditional format using a light green fill  
    \=AND(C4"",COUNTA($C4:D4<=$AA$5),SUM($C4:D4)<=$AA$6)  
    applied to range =$C$4:$X$13
    
    Highlights the range that can go up/down.
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1602088)
    
    *   ![](https://secure.gravatar.com/avatar/ce7106cfd406deda8e930395f2500f4f475abf9d52cd3e0b31cc8d7a998ec803?s=64&d=mm&r=g) GraH says:
        
        [December 20, 2018 at 5:41 pm](https://chandoo.org/wp/elevator-problem/#comment-1602090)
        
        CF messed up my reference, because I started in the wrong cell, clearly it should be  
        \=AND(C4"",COUNTA($C4:C4<=$AA$5),SUM($C4:C4)<=$AA$6)
        
        [Reply](https://chandoo.org/wp/elevator-problem/#comment-1602090)
        
132.  ![](https://secure.gravatar.com/avatar/c012905e123b54c36436352039dca1670632e754e3f5d055be1d0c25539a86d6?s=64&d=mm&r=g) gianfranco pevere says:
    
    [December 23, 2018 at 1:13 am](https://chandoo.org/wp/elevator-problem/#comment-1602946)
    
    \=SE(O(CONTA.SE($C4:$X4;""&"")>$AA$5;SOMMA($C4:$X4)>$AA$6);"no";"si")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1602946)
    
133.  ![](https://secure.gravatar.com/avatar/ecf75ba5d518a210ce02de8d246b882bbcff127c913694768bcd9636fea07ebd?s=64&d=mm&r=g) Bhavani says:
    
    [December 24, 2018 at 12:52 pm](https://chandoo.org/wp/elevator-problem/#comment-1603569)
    
    \=IF(AND(COUNT(C4:X4)<=$AA$5,SUM(C4:X4)<=$AA$6),"UP","DOWN")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1603569)
    
134.  ![](https://secure.gravatar.com/avatar/d095f0a5aed3b6797ca98f8c750da7547376e2aca3b65c8c6cd27aef3c001bd4?s=64&d=mm&r=g) Divvakar says:
    
    [December 27, 2018 at 9:49 am](https://chandoo.org/wp/elevator-problem/#comment-1605390)
    
    \=IF((SUM(C4:X4)>1400),"OVERLOAD",IF(COUNT(C4:X4)>20,"OVERLOAD","A"))
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1605390)
    
135.  ![](https://secure.gravatar.com/avatar/02749853f95afebaaa0b33a6bc03a5bb415c9b414c07d7d0252f6117195ba1a6?s=64&d=mm&r=g) Utkarsh says:
    
    [December 27, 2018 at 4:05 pm](https://chandoo.org/wp/elevator-problem/#comment-1605637)
    
    \=IF(OR(COUNTA(C4:X4)>20,SUM(C4:X4)>1400),"Fail","Pass")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1605637)
    
136.  ![](https://secure.gravatar.com/avatar/42dc58dc543ef4743e8aaa900c2e2edca70b56de247da265ec9a452ee2a3fc4e?s=64&d=mm&r=g) Val says:
    
    [December 27, 2018 at 5:34 pm](https://chandoo.org/wp/elevator-problem/#comment-1605683)
    
    Like many, I used IF/AND/Count & Sum, but then I added a "reason" column in column Y, referencing hidden columns AE (containing the count), AF (containing the weight). AG read the "count" column and used:  
    \=IF(COUNT(C4:X4)>$AC$5,"Too many people","")  
    AH read the Weight column and read:  
    \=IF(SUM(C4:X4)>$AC$6,"Too heavy","")  
    In column Y (displayed reason for no go), read:  
    \=IF(B5="yes","",(CONCAT(AG5&" "&AH5)))
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1605683)
    
137.  ![](https://secure.gravatar.com/avatar/7b90b84b71f1716d259e125613de9f1dd43ebad543e5279d881bb2cff4dfd99f?s=64&d=mm&r=g) MONIKA AGGARWAL says:
    
    [January 2, 2019 at 9:36 am](https://chandoo.org/wp/elevator-problem/#comment-1608190)
    
    \=IF(SUM(C4:X4)<1400,IF(COUNT(C4:X4)<21,"GO","STAY"),"STAY")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1608190)
    
138.  ![](https://secure.gravatar.com/avatar/d8a7e4ae709e5762a82eab2c1ca5bdb6115df9463e4597fadf18f89fc8ae3c1e?s=64&d=mm&r=g) Gerardo Gomez says:
    
    [January 3, 2019 at 6:01 pm](https://chandoo.org/wp/elevator-problem/#comment-1608740)
    
    \=+SI(Y(CONTAR(C4:X4)<=20;SUMA(C4:X4)<=1400);"Go";"Stay")  
    Thank you for Everything Chandoo!  
    Happy New year!
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1608740)
    
139.  ![](https://secure.gravatar.com/avatar/f44694fb536a3633e7a42ad4e09a2e6bfc75392bfb104174d6bcb2e452026722?s=64&d=mm&r=g) Dan says:
    
    [January 4, 2019 at 5:26 am](https://chandoo.org/wp/elevator-problem/#comment-1608936)
    
    Formula: =(SUM(C4:Y4)>1400)+(COUNT(C4:Y4)>20)  
    Number format: "STOP";;"Go"  
    Suggest making 1400 and 20 fixed cell references rather than hard-coding in the formula.
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1608936)
    
140.  ![](https://secure.gravatar.com/avatar/dea7fd5ca0ce0ad2e7c911e3a5df92fa5714ad48bdb62816e4d488e2dc901f54?s=64&d=mm&r=g) Tharun says:
    
    [January 4, 2019 at 12:46 pm](https://chandoo.org/wp/elevator-problem/#comment-1609070)
    
    \=IF(AND(COUNT(C4:X4) <= 20,SUM(C4:X4)<=1400),"go","stop")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1609070)
    
141.  ![](https://secure.gravatar.com/avatar/efd81fb0cfc8551be4f86b2730f5db16bd660f986e5c37abd7985ae25998b05a?s=64&d=mm&r=g) [Abid Hussain](http://n/A)
     says:
    
    [January 4, 2019 at 1:51 pm](https://chandoo.org/wp/elevator-problem/#comment-1609081)
    
    \=IF(AND(COUNT(C4:X4)LT=$AA$5,SUM(C4:X4)LT=$AA$6),"Go","Stay")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1609081)
    
142.  ![](https://secure.gravatar.com/avatar/9d267060d922d98b9e76ed829b971f1290a142ad011edf38070e4fa9611f6640?s=64&d=mm&r=g) Steve says:
    
    [January 5, 2019 at 1:09 pm](https://chandoo.org/wp/elevator-problem/#comment-1609552)
    
    Simple:
    
    \=IF(AND(SUM($C4:$X4)<=$AA$6,COUNT($C4:$X4)<=$AA$5),"YES","NO")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1609552)
    
143.  ![](https://secure.gravatar.com/avatar/ed2987fe2f71c4e8405be08f364632135bbd23f9ece9662f749a7891f298e18b?s=64&d=mm&r=g) MikeO3 says:
    
    [January 6, 2019 at 3:43 am](https://chandoo.org/wp/elevator-problem/#comment-1609849)
    
    \=AND(SUM(C4:X4)<=$AA$6,COUNT(C4:X4)<=$AA$5)
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1609849)
    
144.  ![](https://secure.gravatar.com/avatar/a972411fbb7bcae09634e90f34804551a6cd940079e943fa9aac33972e0531d7?s=64&d=mm&r=g) [Ajay Anand](https://xlncad.blogspot.com/)
     says:
    
    [January 6, 2019 at 4:54 pm](https://chandoo.org/wp/elevator-problem/#comment-1610137)
    
    IF(AND((SUM(C4:X4)<=1400),(COUNT(C4:X4))<=20),"GO","STOP")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1610137)
    
145.  ![](https://secure.gravatar.com/avatar/f22e10eba601046b09e31a27cc8e636aa6b702daa92cdefaad97926763d03a55?s=64&d=mm&r=g) Kirby says:
    
    [January 10, 2019 at 5:47 pm](https://chandoo.org/wp/elevator-problem/#comment-1611714)
    
    Function ElevatorCanGo(MyRange As Range, MaxCount, MaxWeight) As Boolean  
    ' Solves the elevator go/no go problem.  
    ' KJM - 2019-01-10  
    ' Input:  
    ' MyRange - range of weights for each elevator passanger (any units)  
    ' MaxCount - (int) maximum permissible number of people  
    ' MaxWeight - (real) maximum permissible weight  
    ' Returns:  
    ' True if elevator can go!
    
    Dim TotalCount As Long  
    Dim TotalWeight As Single
    
    TotalCount = 0  
    TotalWeight = 0#
    
    Debug.Print ""
    
    For i = 1 To MyRange.Rows.Count  
    For j = 1 To MyRange.Columns.Count  
    If Not (IsEmpty(MyRange.Cells(i, j))) Then
    
    Debug.Print "Cell = "; MyRange.Cells(i, j).Address; " Weight = "; MyRange.Cells(i, j).Value
    
    TotalCount = TotalCount + 1  
    TotalWeight = TotalWeight + MyRange.Cells(i, j).Value  
    End If  
    Next j  
    Next i
    
    Debug.Print "Elevator range: "; MyRange.Address; " Count = "; TotalCount; " Total Weight = "; TotalWeight
    
    If TotalCount > MaxCount Or TotalWeight > MaxWeight Then  
    ElevatorCanGo = False ' no go  
    Else  
    ElevatorCanGo = True ' go!  
    End If
    
    End Function
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1611714)
    
146.  ![](https://secure.gravatar.com/avatar/ca4d8a3ea22361cd6d3a10e3ed1399d86bf334d4137d507b366d2c75eb823ca7?s=64&d=mm&r=g) Bhimarao Naik says:
    
    [January 19, 2019 at 10:57 am](https://chandoo.org/wp/elevator-problem/#comment-1615479)
    
    Hi,
    
    I thick following formula is the simplest one to go for this problem.
    
    \=IF((IF(COUNT(C4:X4)>=20,0,1)\*IF(SUM(C4:X4)>=1400,0,1))=1,"YES","NO")
    
    instead of putting "20" and "1400" we can link cell reference to robust the formula.  
    Let me know your opinion with this
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1615479)
    
147.  ![](https://secure.gravatar.com/avatar/16fb001b749b48d3f8b5ab9ba65322e0df3b08abb184497e699fcb5a59ce7e9f?s=64&d=mm&r=g) Moteb says:
    
    [January 21, 2019 at 6:45 am](https://chandoo.org/wp/elevator-problem/#comment-1615755)
    
    \=IF(AND(SUM(C4:X4)<=1400,COUNT(C4:X4)<=20),"Can go","Can't go")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1615755)
    
148.  ![](https://secure.gravatar.com/avatar/b0e925cbdebe6c31334e44b63510256e16e0dad803bce568d30e4260e18fd419?s=64&d=mm&r=g) Sheshaank Pydikondala says:
    
    [January 23, 2019 at 7:47 am](https://chandoo.org/wp/elevator-problem/#comment-1616175)
    
    \=IF(AND(COUNTA(C4:X4)<=20,SUM(C4:X4)<=1400)," MOVE "," STAY ")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1616175)
    
149.  ![](https://secure.gravatar.com/avatar/dbe5fe9b8ba486819807f258056bac6d4d1a90ced42c914e1ddadf815ff65748?s=64&d=mm&r=g) Gian All says:
    
    [January 23, 2019 at 10:43 pm](https://chandoo.org/wp/elevator-problem/#comment-1616294)
    
    \=SUM(C4:X4)/($AA$6/$AA$5)
    
    Create a custom number format  
    \[>20\]"Stay";;"Go";@
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1616294)
    
150.  ![](https://secure.gravatar.com/avatar/74109386ba52281ab563ea69b958a57e826b12389dee8862aea34f6c363bf0a5?s=64&d=mm&r=g) ari says:
    
    [January 31, 2019 at 8:30 am](https://chandoo.org/wp/elevator-problem/#comment-1618386)
    
    work for me  
    \=IF(COUNT(C4:X4)<=20,IF(SUM(C4:X4)<=1400,"GO","STAY"),"STAY")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1618386)
    
151.  ![](https://secure.gravatar.com/avatar/ea28c1bc04a3d18b9978fecd58f7c23c931824b325cd10168e017b2101f122b4?s=64&d=mm&r=g) Diogo Cuba says:
    
    [January 31, 2019 at 5:08 pm](https://chandoo.org/wp/elevator-problem/#comment-1618571)
    
    \=IF(OR(COUNTA(C4:X4)LT=AA5;SUM(C4:X4)LT=AA6);"YES";"NO")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1618571)
    
152.  ![](https://secure.gravatar.com/avatar/ea28c1bc04a3d18b9978fecd58f7c23c931824b325cd10168e017b2101f122b4?s=64&d=mm&r=g) Diogo Cuba says:
    
    [January 31, 2019 at 5:21 pm](https://chandoo.org/wp/elevator-problem/#comment-1618578)
    
    This one almost nail it but it fails.  
    \=IF(OR(COUNTA(C5:X5)LT=AA5;SUM(C5:X5)LT=AA6);"YES";"NO")
    
    This will do the work:  
    \=IF(AND(COUNTA(C5:X5)LT=AA5;SUM(C5:X5)LT=AA6);"YES";"NO")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1618578)
    
153.  ![](https://secure.gravatar.com/avatar/0612549cfa1bc725c4ab7174da4cbea5283eab3aedc6ff617410854dfb4d59e4?s=64&d=mm&r=g) Syed Mohammad Haris says:
    
    [February 4, 2019 at 8:00 pm](https://chandoo.org/wp/elevator-problem/#comment-1620102)
    
    This one is correctly applied you guys can try  
    \=IF(SUM(C4:X4)>1400,"STAY",IF(COUNTA(C4:X4)>20,"STAY","GO"))
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1620102)
    
154.  ![](https://secure.gravatar.com/avatar/b65398edebb1c43e830a7bbc34c3c9c19a0083017996c3f33216a4c1aaac83d4?s=64&d=mm&r=g) Josh says:
    
    [February 8, 2019 at 8:53 am](https://chandoo.org/wp/elevator-problem/#comment-1621431)
    
    \=IF(AND(COUNT(C4:X4)<$AA$5,SUM(C4:X4)<$AA$6),"GO","NO")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1621431)
    
155.  ![](https://secure.gravatar.com/avatar/6574fae93dd1a9b978d03abd2910b4429caf7f9bdb73bef6f56c3ff2b32b41ad?s=64&d=mm&r=g) PRAMOD DUBEY says:
    
    [February 14, 2019 at 11:05 am](https://chandoo.org/wp/elevator-problem/#comment-1622238)
    
    \=IF(OR(COUNT(C4:X4)<20,AND(SUM(C4:X4)<1400)=TRUE),"Can Go","Can Not Go")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1622238)
    
156.  ![](https://secure.gravatar.com/avatar/0ba6615c7b6c298e88e79ced1e63945d517cdf0f339b5d23ca7f89ed22f57edc?s=64&d=mm&r=g) Gregor says:
    
    [February 20, 2019 at 8:17 am](https://chandoo.org/wp/elevator-problem/#comment-1624346)
    
    \=+IF(COUNT(C4:X4)>20,"No",IF(SUM(C4:X4)>1400,"No","Yes"))
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1624346)
    
157.  ![](https://secure.gravatar.com/avatar/eab8bfc5c05b6d2a6b6abec0374579f1d4369f7b3f00b2ebb44a0d24f0911183?s=64&d=mm&r=g) Sanjeew says:
    
    [February 25, 2019 at 10:43 pm](https://chandoo.org/wp/elevator-problem/#comment-1625283)
    
    \=IF(AND(COUNT(C4:X4)>20,SUM(C4:X4)>1400),"Too Heavy & Too Many","Move Lift")
    
    I used if & and formula jointly to reach solution
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1625283)
    
158.  ![](https://secure.gravatar.com/avatar/515111aa7941929f5f321fa0231c5a54f3ecb97560fe79e59521bfa2e27e3b17?s=64&d=mm&r=g) Malhar Anarse says:
    
    [February 26, 2019 at 10:14 am](https://chandoo.org/wp/elevator-problem/#comment-1625396)
    
    \=IF(SUM(C4:X4)<=1400,IF(COUNT(C4:X4)<=20,"YES","NO"),"NO")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1625396)
    
159.  ![](https://secure.gravatar.com/avatar/2ff2ef29603aa7f80405aa14a95eca00dde332469f7cae667d2e9f8733a5aa8a?s=64&d=mm&r=g) Arshad says:
    
    [March 4, 2019 at 2:54 pm](https://chandoo.org/wp/elevator-problem/#comment-1626679)
    
    I solved this problem by giving this formula .
    
    I use "AND" because in IF condition we need to satisfy two condition same time and "AND" is used to satisfy both condition.
    
    \=IF((AND(COUNT(C4:X4)>20, SUM(C4:X4)>1400)),"CAN NOT GO", "CAN GO")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1626679)
    
160.  ![](https://secure.gravatar.com/avatar/dbe5fe9b8ba486819807f258056bac6d4d1a90ced42c914e1ddadf815ff65748?s=64&d=mm&r=g) Gian All says:
    
    [April 1, 2019 at 8:53 am](https://chandoo.org/wp/elevator-problem/#comment-1634393)
    
    Hi Test  
    \=IF((SUM(C4:X4)>1400)+(COUNT(C4:X4)>20),"STAY","GO")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1634393)
    
161.  ![](https://secure.gravatar.com/avatar/a3061911b88c192013b694f66bd4e2a65dd2aa6efe78d22b1c768eae728b43b0?s=64&d=mm&r=g) Mike says:
    
    [October 11, 2019 at 9:20 pm](https://chandoo.org/wp/elevator-problem/#comment-1694937)
    
    \=IF(COUNT(C4:X4)<=20,IF(SUM(C4:X4)<=1400,"GO","NO GO"),"NO GO")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1694937)
    
162.  ![](https://secure.gravatar.com/avatar/2e6012c305f442cd730c8c1ce23d64785ede19aaebc2865485c59bacad94f975?s=64&d=mm&r=g) Sushmita Bhar says:
    
    [January 17, 2020 at 6:26 am](https://chandoo.org/wp/elevator-problem/#comment-1730193)
    
    \=IF(AND(COUNT(C4:X4)<=$AA$5,SUM(C4:X4)<=$AA$6),"go","stay")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1730193)
    
163.  ![](https://secure.gravatar.com/avatar/5e5dc3c67241034178eea2079b8aa8ffd31cac0204b3d23487efb359dee8966d?s=64&d=mm&r=g) Esakki Rajesh M says:
    
    [March 27, 2020 at 6:27 pm](https://chandoo.org/wp/elevator-problem/#comment-1769015)
    
    \=IF(AVERAGEIFS(C4:X4,C4:X4,"""")\*(IF(COUNTA(C4:X4)>$AA$5,1000,COUNTA(C4:X4)))>$AA$6,"No","Yes")
    
    [Reply](https://chandoo.org/wp/elevator-problem/#comment-1769015)
    
    *   ![](https://secure.gravatar.com/avatar/5e5dc3c67241034178eea2079b8aa8ffd31cac0204b3d23487efb359dee8966d?s=64&d=mm&r=g) Esakki Rajesh M says:
        
        [March 27, 2020 at 6:28 pm](https://chandoo.org/wp/elevator-problem/#comment-1769017)
        
        \=IF(AVERAGEIFS(C4:X4,C4:X4,"""")\*(IF(COUNTA(C4:X4)>$AA$5,1000,COUNTA(C4:X4)))>$AA$6,"No","Yes")
        
        [Reply](https://chandoo.org/wp/elevator-problem/#comment-1769017)
        

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/elevator-problem/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Quick tip: Make a list of numbers (or dates) in Power Query easily](https://chandoo.org/wp/quick-tip-make-a-list-of-numbers-or-dates-in-power-query-easily/) | [Quickly change charts from one to another with this trick](https://chandoo.org/wp/howto-change-excel-chart/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)