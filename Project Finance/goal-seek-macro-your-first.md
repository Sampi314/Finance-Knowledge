# Goal Seek Macro – Your First and Last

**Source:** https://edbodmer.com/goal-seek-macro-your-first

---

As with the short-cut keys, participants in my classes sometimes say they will not remember how to make a macro, in particular a goal seek macro. This little section is intended to be a reminder as how to make a goal seek macro. You can do really fancy things with macros and functions that I hope are explained at various points in this website. This includes reading data from the internet, creating fancy scenarios, fixing excel to interpolate data, and resolving circular references. If you have not made a macro, however, do not be intimidated.

The first macro I ever made sometime in the early 1990’s was to fix the goal seek in excel so you could repeat it without having to keep going back to the menu and keep changing the target etc. I remember where I was like I rmember where I was when Martin Luther King was shot.

All you have to do is press the macro record button and then make your goal seek and then make absolutely sure to stop the record button once you have finished with the goal seek. This process is described in the video below. The file that I have used to explain this simple macro is associated with my WACC and interest shield stuff and listed below the video.

.

[WACC and Growth with Goal Seek Macro.xls](http://edbodmer.wikispaces.com/file/view/WACC%20and%20Growth%20with%20Goal%20Seek%20Macro.xlsm/606381821/WACC%20and%20Growth%20with%20Goal%20Seek%20Macro.xlsm)

.

More Complex Case
-----------------

If you have an InputC page with multiple scenarios, you may want to perform a goal seek macro, but put the result in each of the scenarios. In the example below, you have different scenarios and you want to compute the capacity charge with a goal seek for each of the scenarios. Note the row with the capacity charge where the capacity charge is the same accross columns in the screenshot below.

.

![](https://edbodmer.com/wp-content/uploads/2023/06/image-22.png)

.

.

The second screenshot shows that the IRR accross the different scenarios is different. So here is what you want. You want to change the CCR so the IRR is the same accross the different scenarios. Currently the IRR’s are different as shown in row 40. The IRR output also comes from a macro that I disuss below.

![](https://edbodmer.com/wp-content/uploads/2023/06/image-23.png)

.

.

To do this stuff where you can compute multiple goal seeks, it is not so difficult. You should know how to use the CELLS statement in vba along with a FOR and NEXT loop. It is also useful to understand the COUNT function. To do this you can follow the following steps.

.

|     |
| --- |
| Step 1: Make the normal goal seek macro |
| Step 2: Range Name for the InputC Row |
| Step 3: Range Name for Scenario |
| Step 4: Make Goal seek with Range(“CCR”).cells(1,Range(“Scenario”)) or \[CCR\].cells(1,\[Scenario\]) |

.

.

![](https://edbodmer.com/wp-content/uploads/2023/06/image-24-768x210.png)

.

The next step with the reset is illustrated below. Note how the count statement is used together with the FOR NEXT loop. Then the CELLS statement is used with the function that goes accross the scenarios in the INPUTC sheet.

.

.

The second function uses the FOR NEXT and calls the goal seek macro each time. As shown above, the goal seek function plops the goal seek result in the range name.

.

![](https://edbodmer.com/wp-content/uploads/2023/06/image-25.png)

.

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=8835&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=0&rand=0.4012965209657269)