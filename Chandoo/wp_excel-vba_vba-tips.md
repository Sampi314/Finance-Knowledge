# Excel VBA Tips & Tricks » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/excel-vba/vba-tips

---

[![Excel VBA - Tutorials, Examples, Information & Resources](https://cache.chandoo.org/logos/excel-vba.png "Excel VBA - Tutorials, Examples, Information & Resources")](https://chandoo.org/wp/excel-vba/)

[**Excel VBA**](https://chandoo.org/wp/excel-vba/)
 > [Examples](https://chandoo.org/wp/excel-vba/examples/)
 [Videos](https://chandoo.org/wp/excel-vba/videos/)
 [VBA Tips](https://chandoo.org/wp/excel-vba/vba-tips/)
 [User Forms & Controls](https://chandoo.org/wp/excel-vba/user-forms/)
 [Books](https://chandoo.org/wp/excel-vba/books/)
 [References](https://chandoo.org/wp/excel-vba/references/)
 [Training](https://chandoo.org/wp/excel-vba/training/)
 [FREE Newsletter](https://chandoo.org/wp/excel-vba/newsletter/)

Tips & Tricks for Excel VBA, Macros
===================================

In this section, learn some interesting tips & ideas to improve your VBA proficiency.

My Top 10 Tips for Excel VBA
----------------------------

### #1 Think Thru before Coding

The best way to solve even a very complex problem is to think thru. Next time, when you are about to automate that report or clean some imported data using VBA, just write the logic down on a paper. See and understand various aspects of the problem. The solution becomes clear to you. It has worked for me and it works for you too.

Related: [Building your First VBA Application using Excel](http://chandoo.org/wp/2011/09/02/excel-vba-demo-application/ "Putting It All Together – Our First VBA Application [Part 4 of 5 - Excel VBA Crash Course]")

### #2 Use the Recorder

Excel’s built in Macro recorder is a great way to learn about new objects and ways to deal with them. I use it all the time to record parts of my code and then customize the output. Just keep in mind that macro recorder does not produce the best or complete code all the time. But it gives you a damn good idea about how to write code for a set of actions.

Related: [Introduction to Excel VBA & Writing your First Macro](http://chandoo.org/wp/2011/08/29/introduction-to-vba-macros/ "What is VBA & Writing your First VBA Macro in Excel [VBA Crash Course Part 1 of 5]")

### #3 Use Immediate Window

Excel VBE has a powerful feature called as Immediate window. Think of this like a sandbox. You can write almost any VBA statements here and get quick results. For example, Open VBE (ALT+F11 in Excel) and go to Immediate window.

1.  Type ?Activecell.Value
2.  Press Enter
3.  And you will see the current cell’s value printed in immediate window

**Here is a quick demo of immediate window.**

![Demo of Immediate Window - Excel VBA Crash Course](https://img.chandoo.org/vba/crash-course/demo-of-immediate-window-excel-vba.gif)

### #4 Debug.Print is your Friend

There are 3 things you cannot avoid in life

1.  your 2 year old daughter thinking it would be fun to throw a stone on your car
2.  your baby boy running and sitting in your lap suddenly making the hot coffee spill on you
3.  and of course bugs in your code

_Bug is a fancy name given to the situation when your code is not doing what it is supposed to do._

But why?!? Well, we don’t know why unless we examine. And this is where Debug.Print can come handy. In below example, you would see the values of all tasks in the immediate window as your program runs.

![Example on Debug.Print in VBA](https://chandoo.org/img/vba/crash-course/debug-print-example-vba-macros.png)

### #5 There is a method for that!

Just like Apple says [_There is an App for that!_](http://www.youtube.com/watch?v=szrsfeyLzyg)
, may be Microsoft should say **_There is a Method for that!_** about VBA. I say this because VBA comes with a lot of methods and functions to do lots of things. If you are thinking of writing your own code to reverse some text, split something based on a delimiter, find the intersection of 2 ranges or run something after 10 seconds, may be you should before writing your code. _**Because, my dear, there is a method for that**_.

Whenever you feel like you are writing code for a problem that is already solved several times, chances are there is some built-in method or object for that. So just search.

### Tips for Using & Mastering VBA in Long-term

While the above tips are good for solving your immediate problems, we should always aim for continuous improvement. Here are my top tips for keeping your VBA in shape.

### #6 Break Your Work in to Smaller Chunks

No matter how complex your work situation or problem might be, chances are, it is made up of several smaller problems. So break things in to smaller chunks. This coding technique is called as **_modularization_**. Modularization has several advantages:

*   Reuse: Once you break a big program to smaller parts, you can reuse a smaller part in several places or in other projects.
*   Testable: Smaller code fragments are easy to test and debug.
*   Maintainable: You can maintain smaller parts easily. You can upgrade them once you get a better version of Excel without breaking much.

### #7 Build Iteratively

_Rome is not built in one day, so is your buildRome() macro._ Whenever you are attempting to automate a whole department’s work, take a step back and see what is the smallest (but most useful) feature you can have. Implement it and then add new features iteratively. That way, your turn-around time is improved, you look pretty in front of your boss and you feel in control of things.

Iterative development also lets you stop whenever you want and you would still have some working piece of code.

### #8 Keep a Good Reference Handy

If you are going to use VBA quite often, then invest in a good reference. I suggest [John Walkenbach’s Excel 2010 Power Programming](http://www.amazon.com/gp/product/0470475358/ref=as_li_ss_tl?ie=UTF8&tag=poinhairdilb-20&linkCode=as2&camp=217145&creative=399369&creativeASIN=0470475358)
 if you are looking for one. Good reference books have lots of information and tips buried in them. For example, I keep Excel 2010 Power Programming book on my desk all the time and refer to it whenever I feel like not doing any work. I always learn something new.

### #9 Take up Challenges

_“Computers are like bicycles for our mind”_ [said Steve Jobs](http://www.youtube.com/watch?v=ob_GX50Za6c)
. I am not sure if hours I put on facebook, twitter and gmail are keeping my mind fit. But any time I invest on programming is worth every second. I feel very sharp, excited and stoked when I solve a tricky problem using a computer program (be it VBA, an Excel Formula or php or anything else).

I think if you want to be good in VBA or Excel, then take up challenging work. Try to automate a report that you (or your team) produce using VBA, Try to simplify a formula or improve a chart.

If you are looking for fresh challenges, then [**look at our forums**](http://chandoo.org/forums/)
. We get dozens of interesting questions everyday.

### #10 Use VBA only when you need it

Once you start learning VBA, it is natural to feel excited about the possibilities you have. But keep in mind that overusing it can complicate your work.

My suggestion: Use Excel’s native features as much as possible. Excel has several built in features to solve various day to day problems (conditional formatting, pivot tables, formulas, data validation, form controls to name a few). Only when you feel that there is no easy way to use Excel alone to solve a problem, go for VBA.

More Tips & Tricks for Excel VBA
--------------------------------

**Please go thru these tips as well:**  
[Introduction to VBA & Excel Macros](http://chandoo.org/wp/2011/08/29/introduction-to-vba-macros/)
  
[Understanding variables, conditions & loops in VBA](http://chandoo.org/wp/2011/08/30/variables-conditions-loops-in-vba/)
  
[Using Objects in VBA](http://chandoo.org/wp/2011/08/31/using-objects-in-vba-howto/)
  
[Debugging VBA Macros by Selecting them](http://chandoo.org/wp/2010/07/19/select-expressions-to-find-values-macro-debugging-tip/)
  
[Adding Macros to Excel Toolbars](http://chandoo.org/wp/2010/06/08/add-macros-to-excel-toolbars/)
  
[Enabling Relative References while Recording Macros](http://chandoo.org/wp/2008/11/18/excel-vba-macros-relative-references-help/)
  
[Making Case In-sensitive String Comparison in VBA](http://chandoo.org/wp/2011/12/01/case-in-sensitive-string-compare-vba/)

More on Excel VBA
-----------------

Please go thru these pages for more on Excel VBA

*   [Excel VBA Homepage](http://chandoo.org/wp/excel-vba/)
    
*   [Excel VBA Examples](http://chandoo.org/wp/excel-vba/examples/)
    
*   [Video Tutorials on Excel VBA, Macros](http://chandoo.org/wp/excel-vba/videos/)
    
*   **Excel VBA Tips**
*   [User Forms & Controls in VBA](http://chandoo.org/wp/excel-vba/user-forms/)
    
*   [Books on Excel VBA](http://chandoo.org/wp/excel-vba/books/)
    
*   [References on Excel VBA](http://chandoo.org/wp/excel-vba/references/)
    
*   [Training on Excel VBA](http://chandoo.org/wp/excel-vba/training/)
    
*   [Join our Excel Newsletter](http://chandoo.org/wp/excel-vba/newsletter/)
    

[^ Go to Top](https://chandoo.org/wp/excel-vba/vba-tips/#top)
 [**Excel VBA**](https://chandoo.org/wp/excel-vba/)
 [Examples](https://chandoo.org/wp/excel-vba/examples/)
 [Videos](https://chandoo.org/wp/excel-vba/videos/)
 [VBA Tips](https://chandoo.org/wp/excel-vba/vba-tips/)
 [User Forms & Controls](https://chandoo.org/wp/excel-vba/user-forms/)
 [Books](https://chandoo.org/wp/excel-vba/books/)
 [References](https://chandoo.org/wp/excel-vba/references/)
 [Training](https://chandoo.org/wp/excel-vba/training/)
 [FREE Newsletter](https://chandoo.org/wp/excel-vba/newsletter/)

[![Excel VBA - Tutorials, Examples, Information & Resources](https://cache.chandoo.org/logos/excel-vba.png "Excel VBA - Tutorials, Examples, Information & Resources")](https://chandoo.org/wp/excel-vba/)