# Excel VBA - Information, Tutorials, Examples & Resources » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/excel-vba

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

Excel VBA – Information, Tutorials, Examples & Resources
========================================================

**Excel VBA allows you to automate various activities you do in Excel**. We use Excel to analyze data, create reports, prepare charts & presentations, do calculations and understand information. When we are doing all these, we spend quite some time, repeating same steps.

For example, we prepare and email same type of report every week with different data.

By using Excel VBA, we can cut down the time we spend repeating these steps and improve our productivity.

In this section of our site, you will find information, tutorials, examples, tips & resources on Excel VBA & Macros.

|     |     |
| --- | --- |
| **In this page**<br><br>*   [What is VBA?](https://chandoo.org/wp/excel-vba/#what_is_vba)<br>    <br>*   [What is a Macro?](https://chandoo.org/wp/excel-vba/#what_is_macro)<br>    <br>*   [Basics of VBA & Macros](https://chandoo.org/wp/excel-vba/#basics_of_vba)<br>    <br>*   [Enabling Developer Toolbar in Excel](https://chandoo.org/wp/excel-vba/#developer_toolbar)<br>      <br>    [Using Excel’s built-in recorder](https://chandoo.org/wp/excel-vba/#macro_recorder)<br>      <br>    [Writing our first Excel Macro](https://chandoo.org/wp/excel-vba/#first_macro)<br>      <br>    [Important Shortcuts for Excel VBA](https://chandoo.org/wp/excel-vba/#shortcuts) | **More on Excel VBA**<br><br>[Excel VBA Examples](http://chandoo.org/wp/excel-vba/examples/)<br>  <br>[Video Tutorials on Excel VBA, Macros](http://chandoo.org/wp/excel-vba/videos/)<br>  <br>[Excel VBA Tips](http://chandoo.org/wp/excel-vba/vba-tips/)<br>  <br>[User Forms & Controls in VBA](http://chandoo.org/wp/excel-vba/user-forms/)<br>  <br>[Books on Excel VBA](http://chandoo.org/wp/excel-vba/books/)<br>  <br>[References on Excel VBA](http://chandoo.org/wp/excel-vba/references/)<br>  <br>[Training on Excel VBA](http://chandoo.org/wp/excel-vba/training/)<br>  <br>[Join our Excel Newsletter](http://chandoo.org/wp/excel-vba/newsletter/) |

### Resources for you...

[Example file](https://files.chandoo.org/vba/getting-started-with-vba-demo.xlsm)

[Video Tutorial](https://youtu.be/5k-KpSkrROw)

[Online VBA Class](https://chandoo.org/wp/vba-classes/)

What is VBA?
------------

**VBA stands for Visual Basic for Applications.** Just like you and I have a language, computer programs too have their own language. VBA happens to be the language in which Excel speaks. For that matter, VBA is also the language of MS Word, PowerPoint, Access and other MS Office applications. The prospect of learning new languages scares us a lot. But worry not, VBA is much easier to learn than French, Spanish, German or Chinese. The main reason why VBA is easy to learn is because it almost looks like plain English. For example the following line says hello to you:

MsgBox "hello"

Just like any language, VBA too has its own rules, grammatical structures & nuances. Once you understand these, speaking VBA with Excel becomes as easy as chatting with your friend over a drink.

What is a Macro?
----------------

While VBA is the language which Excel speaks (and understands), Macro is like a paragraph. In other words, **a Macro is a set of instructions given to Excel to accomplish something.** For example, this is a macro for generating a report (written in plain English, not VBA)

1.  Open data.xlsx
2.  Take last 30 days of data
3.  Prepare a bar chart
4.  Copy the chart to a new workbook
5.  Save the workbook as a PDF
6.  Email it to boss

When we **execute or run** this macro, we end up **_generating the report & mailing it_**.

Basics of VBA & Macros – Writing our First Macro
------------------------------------------------

In this section, lets build our first macro. We will write a FillYellowColor() macro, that paints yellow color in any selected cell(s). Like this, ![Fill yellow color - VBA macro - demo](https://chandoo.org/wp/wp-content/uploads/2021/07/fill-yellow-color-vba-macro-demo.gif)

### Enabling Developer Ribbon in Excel

In order to record and use macros (and other developer features), the first step is to activate Developer Ribbon (or Developer Toolbar). This is done by, **Excel 365 / 2016 etc:** 1. Right click on any ribbon 3. Select “Customize Ribbon” 4. Make sure “Developer tab” is checked in right side area 5. Click ok.

### Using Excel’s Built-in Macro Recorder

In order to write your first VBA program (or Macro), you need to know the language first. This is where Excel’s tape recorder will help us. _**Tape Recorder?!?**_ Yes. Excel has a built-in tape recorder, that listens and records everything you do, in Excel’s own language, _ie_ VBA. Since we don’t know any VBA, we will use this recorder to record our actions and then we will see recorded instructions (called as _code_ in computer lingo) to understand how VBA looks like. **Step 1: Select any cell & start macro recorder** This is the easiest part. Just select any cell and go to Developer Ribbon & click on Record Macro button. ![](https://chandoo.org/wp/wp-content/uploads/2021/07/record-macro-button-excel.png) **Step 2: Give a name to your Macro** Specify a name for your macro. I called mine FillYellowColor. You can choose whatever you want. Just make sure there are no spaces or special characters in the name (except underscore) Click OK when done. **Step 3: Fill the current cell with yellow color** This is easy as eating pie. Just go to Home ribbon and fill color in the current cell. **Step 4: Stop Recording** Now that you have done the only step in our macro, its time to stop Excel’s tape recorder. Go to Developer ribbon and hit “stop recording” button. ![](https://chandoo.org/wp/wp-content/uploads/2021/07/stop-recording-button-excel.png) **Step 5: Assign your Macro to a button** Now go to Insert ribbon and draw a nice rectangle. Then, put some text like “fill color” in it. Then right click on the rectangle shape and go to Assign Macro. And select the FillYellowColor macro from the list shown. Click ok. ![](https://chandoo.org/wp/wp-content/uploads/2021/07/how-to-add-macro-to-a-screen-button-in-excel.png) **Step 6: Go ahead and play with your first macro** That is all. Now, we have linked the rectangle shape to your macro. Whenever you click it, Excel would drop a bucket of yellow paint in the selected cell(s). Go ahead and play with this little macro of ours.

Download This Excel VBA Example
-------------------------------

**[Click here to download sample file with this and two other macros](https://files.chandoo.org/vba/getting-started-with-vba-demo.xlsm)
 (todo list, data extractor).** Play with the code & understand this better.

Excel VBA - Getting Started Video
---------------------------------

Please watch my video on **how to get started with VBA.** In this video, you will learn how to:

✅ Set up FillYellowColor macro with recorder  
✅ How to view & edit the recorded macros  
✅ Create a simple to-do list app in Excel  
✅ Make a data extractor with VBA

Watch it below or [on my Youtube channel](https://youtu.be/5k-KpSkrROw)
.

Learn more about Excel VBA
--------------------------

Please visit these pages for more on Excel VBA,

1.  [What is VBA & Writing your First VBA Macro in Excel](https://chandoo.org/wp/introduction-to-vba-macros/)
    
2.  [Understanding Variables, Conditions & Loops in VBA](https://chandoo.org/wp/variables-conditions-loops-in-vba/)
    
3.  [Using Cells, Ranges & Other Objects in your Macros](https://chandoo.org/wp/using-objects-in-vba-howto/)
    
4.  [Putting it all together – Your First VBA Application using Excel](https://chandoo.org/wp/excel-vba-demo-application/)
    
5.  [My Top 10 Tips for Mastering VBA & Excel Macros](https://chandoo.org/wp/top-10-tips-for-excel-vba/)
    

Important Shortcuts for Excel VBA
---------------------------------

Please remember these shortcuts & use them to be productive while using Excel VBA.

*   ALT+F11: To view VBA Editor (or to switch back to Excel)
*   ALT+F8: To display all macros

**These shortcuts will work only in VBA Editor (also known as VBE):**

*   ALT+Q: To close VBA Editor and return to Excel
*   F5: To run a Macro
*   F2: Display Object Browser
*   F7: Display code editor
*   CTRL+G: Open immediate window
*   F1: Display help

More on Excel VBA
-----------------

Please go thru these pages for more on Excel VBA

*   [Excel VBA Examples](http://chandoo.org/wp/excel-vba/examples/)
    
*   [Video Tutorials on Excel VBA, Macros](http://chandoo.org/wp/excel-vba/videos/)
    
*   [Excel VBA Tips](http://chandoo.org/wp/excel-vba/vba-tips/)
    
*   [User Forms & Controls in VBA](http://chandoo.org/wp/excel-vba/user-forms/)
    
*   [Books on Excel VBA](http://chandoo.org/wp/excel-vba/books/)
    
*   [References on Excel VBA](http://chandoo.org/wp/excel-vba/references/)
    
*   [Training on Excel VBA](http://chandoo.org/wp/excel-vba/training/)
    
*   [Join our Excel Newsletter](http://chandoo.org/wp/excel-vba/newsletter/)
    

### Resources for you...

[Example file](https://files.chandoo.org/vba/getting-started-with-vba-demo.xlsm)

[Video Tutorial](https://youtu.be/5k-KpSkrROw)

[Online VBA Class](https://chandoo.org/wp/vba-classes/)

[^ Go to Top](https://chandoo.org/wp/excel-vba/#top)
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