# How to Assign a Macro to a Button in Excel (Easy Guide)

**Source:** https://trumpexcel.com/assign-macro-to-button-in-excel

---

[Skip to content](https://trumpexcel.com/assign-macro-to-button-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/assign-macro-to-button-in-excel/#below-title)

While there are many different ways to run a macro in Excel, none of those methods can be as easy and user-friendly as clicking on a button.

And for that to work, you need to assign a macro to a button first.

In this tutorial, I will show you a couple of ways to insert a button in  Excel and then assign a macro to that button (or shape). Once done, as soon as a user clicks on the button, the macro VBA code would be executed.

For the purpose of this tutorial, I will be using the below VBA macro code (which simply selects cell A1 in the active sheet and enters the text “Good Morning” in it and colors it red).

Sub GoodMorning()
With ActiveSheet.Range("A1")
    .Value = "Good Morning"
    .Interior.Color = vbRed
End With
End Sub

The above VBA code is placed in a regular module in the [VB Editor](https://trumpexcel.com/visual-basic-editor/)

![Adding VBA Macro to a regular module](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20664%20392'%3E%3C/svg%3E)

Now let’s dive right in and see how you can assign this macro to a button or shape in Excel!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/assign-macro-to-button-in-excel/#)

Insert a Shape and Assign Macro to that Shape
---------------------------------------------

While there are dedicated buttons that you can insert in the worksheet and then assign the macro to it, I will first cover **how to assign a macro to a shape**.

I personally love this method and prefer it over the rest two methods covered later. You can easily insert a shape (square or rectangle) and can make it look like a button.

And since it’s a shape, you can easily format it to look perfect with your existing formatting or brand colors.

Below are the steps to insert a shape in Excel:

1.  Click the Insert tab![Click the Insert Tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20380%20199'%3E%3C/svg%3E)
2.  In the illustrations group, click on Shapes![Click on Shapes](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20477%20201'%3E%3C/svg%3E)
3.  In Shapes options, click on the Rectangle option. You will notice that your cursor changes to a plus icon![Click on Rectangle option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20484%20316'%3E%3C/svg%3E)
4.  Click anywhere on the worksheet. This will insert a rectangle shape in the worksheet.![Rectangle Button in the Worksheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20441%20436'%3E%3C/svg%3E)
5.  Resize the rectangle and format it (give it a border, color, shade if you want).

After you have done the above steps, you will have a rectangle shape in the worksheet, and now we will assign a macro to this shape.

Note that I have inserted a rectangle shape in this example, but you can insert whatever shape you want (such as a circle or triangle or arrow). I prefer using a rectangle and it looks like a button and is more intuitive.

Now let’s see how to assign a macro to this shape.

1.  Right-click on the shape on which you want to assign the macro
2.  In the menu options that appear, click on ‘Assign Macro’. This will open the assign macro dialog box![Click on Assign Macro](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20544'%3E%3C/svg%3E)
3.  In the Assign Macro dialog box, you will see a list of all the macros that you have in the workbook
4.  Click the Macro name that you want to assign to this shape. In this example, I will click on the macro named ‘GoodMorning![Select the macro from the list](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20551%20470'%3E%3C/svg%3E)
5.  Click on OK

That’s it!

The selected macro has now been assigned to the shape.

Now when you hover the cursor over the shape, it will show the hand icon. which indicates that now this shape has become clickable.

![The button becomes clickable](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20403%20168'%3E%3C/svg%3E)

And now if you click on the shape, it will [run the assigned macro](https://trumpexcel.com/run-a-macro-excel/)
.

You can type any text within the shape to make it more intuitive (such as ‘Click here to run the macro’). To do this. right-click on the shape and then click on Edit Text. Now you can type within the text box shape.

![Edit Text option to add text to the shape](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20537%20346'%3E%3C/svg%3E)

Note that you won’t be able to click and run the macro when the shape has been selected (i.e., you see a border around the shape that appears when you select it), To make it clickable, hit the Escape key or click anywhere in the worksheet.

Also, when you have assigned the macro to the shape already, you will not be able to select it by using the left mouse key (as it has become clickable and left-click would now execute the macro). In that case, select the shape, hold the control key and then press the left key.

### Keeping Shape Visible When you Hide/Resize Rows/Columns

In Excel. when you insert a shape, it sits over the cells – like a chart/object.

This also has a drawback that when you resize or hide rows/columns that have the shape over it, the shape also follows suit.

In the below example, the shape gets hidden when I hide the column on which it’s placed.

![Shape Gets hidden when the column is hidden](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20452%20428'%3E%3C/svg%3E)

If you don’t want this to happen, follow the below steps:

1.  Right-click on the shape
2.  Click on Format Shape![Right click and then click on Format Shape](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20393%20643'%3E%3C/svg%3E)
3.  In the Format Shape pane (or dialog box in case you’re using Excel 2010 or prior versions), select Size and Properties
4.  In the Properties options, select the option – ‘Don’t move or size with cells’![Click on Don't move or size with cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20356%20438'%3E%3C/svg%3E)
5.  Close the pane (or dialog box)

Now, when you resize rows/columns or hide these, the shape would stay in its place.

Assign a Macro to Form Control Button
-------------------------------------

If you’re not too concerned with the formatting of the button and are ok with regular gray buttons, you can quickly insert it from form control (or ActiveX control as shown next) and then assign a macro to it.

For this to work, you will need to have the Developer tab in your ribbon. If you don’t have it, here is a detailed step-by-step tutorial on [getting the developer tab in the Excel ribbon](https://trumpexcel.com/excel-developer-tab/)
.

Once you have the developer tab visible, you can use the below steps to quickly insert a button and assign a macro to it:

1.  Click on the Developer tab![Click the Developer tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20757%20199'%3E%3C/svg%3E)
2.  In the Control group, click on Insert.![Click on Insert option in the Developer tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20757%20199'%3E%3C/svg%3E)
3.  In the options that appear, in the Form Controls options, click on the Button (Form Control) option.![Click on Form Control button icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20248%20296'%3E%3C/svg%3E)
4.  Click anywhere on the worksheet. This will insert the button wherever you click and automatically open the ‘Assign Macro’ dialog box.
5.  In the Assign Macro dialog box, you will see a list of all the macros that you have in the workbook
6.  Click the Macro name that you want to assign to this button. In this example, I will click on the macro named ‘GoodMorning’![Select the macro from the list](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20551%20470'%3E%3C/svg%3E)
7.  Click on OK

The above steps would insert a button that has the specified macro assigned to it.

By default, it would be a small button with text such as ‘Button’ written on it. You can change the text to whatever you want and can also change the shape of the button (by dragging the edges).

Since this is an object that is placed over the worksheet (just like shapes/charts), you can drag and place it anywhere in the worksheet.

One drawback of using the Form Control button is that you don’t have much control over the formatting. For example, you can not change the color from gray to something else.

Although there is a little bit of formatting that you can do with a Form control button, it’s nowhere close to what you can do with shapes.

You get these button formatting options when you right-click on the button and then click on Format Control.

![Right click on the button and then click on format control](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20374%20336'%3E%3C/svg%3E)

This will open the Format Control dialog box where you can change the font type/color, size, alignment, etc.

![Formatting options for a form control button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20635%20541'%3E%3C/svg%3E)

One good thing about this button is that it doesn’t hide or resize when you hide the rows/columns or resize them. It would, however, move in case you change the height or width or the row/column over which the button is placed.

In case you don’t want the button to stay in its place, you can change the setting by following the below steps:

1.  Right-click on the button
2.  Click on Format Control
3.  Click on the Properties tab
4.  Select the option – ‘Don’t move or size with cells’![Select do not move or size with cells options for the form control button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20635%20541'%3E%3C/svg%3E)
5.  Click Ok

Assign a Macro to an ActiveX Control Button
-------------------------------------------

Apart from the Form Control button, there is also an ActiveX control button to which you can assign a macro.

In most cases, you won’t need to use the ActiveX control button, and I recommend you use it only when you completely understand what it is and you know what you’re doing.

Wondering why we have two different kinds of buttons – Form Control and ActiveX? While Form Controls are in-built in the Excel application, ActiveX is loaded from a separate DLL (Dynamic Link Libraries). This makes Form control buttons a lot more robust and reliable as compared with the ActiveX buttons. You can read more about this difference [here in a post in StackOverflow](https://stackoverflow.com/questions/15455179/what-is-the-difference-between-form-controls-and-activex-control-in-excel-20)
.

This also, sometimes, make ActiveX a bit glitchy and unpredictable. So, while I cover it in this tutorial, I don’t recommend using ActiveX button and assign a macro to it.

To insert an ActiveX button and then assign a macro to it, follow the below steps:

1.  Click on the Developer tab
2.  In the Control group, click on Insert.
3.  In the options that appear, in the ActiveX Controls options, click on the Command Button option.![Click on ActiveX Control Command Button option in the developer tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20290%20295'%3E%3C/svg%3E)
4.  Click anywhere on the worksheet. This will insert the button wherever you click.
5.  Double-click on the button and it will open the VB Editor backend where you can place the code for the ActiveX button

With ActiveX control, you get a lot more flexibility with a single button. For example, you can specify one macro to be run when you simply click on the button once and another macro when you double-click or even another one when you use the up/down arrow key.

Again, not something you need to be using in your regular work.

Another option you can consider (when working with buttons/shapes and assigning macros to it) is to add the macro to the [Quick Access Toolbar](https://trumpexcel.com/excel-quick-access-toolbar-options/)
. That way, you can run the macro with a single click and it’s always visible in the QAT.

Hope you found this tutorial useful. If you’re interested in learning VBA, you can check out [more in-depth Excel VBA tutorials here](https://trumpexcel.com/excel-vba/)
.

**You may also like the following Excel tutorials:**

*   [How to Record a Macro in Excel](https://trumpexcel.com/record-macro-vba/)
    
*   [Creating a User Defined Function (UDF) in Excel VBA](https://trumpexcel.com/user-defined-function-vba/)
    
*   [Excel VBA MsgBox \[Message Box\]](https://trumpexcel.com/vba-msgbox/)
    
*   [Useful Excel Macro Examples for VBA Beginners](https://trumpexcel.com/excel-macro-examples/)
    
*   [How to Remove Macros From an Excel Workbook](https://trumpexcel.com/remove-macros-from-excel/)
    
*   [How to Enable Macros in Excel?](https://trumpexcel.com/enable-macros-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

1 thought on “How to Assign a Macro to a Button in Excel (Easy Guide)”
----------------------------------------------------------------------

1.  Following the procedure here, I cannot assign a Macros from an \*.xlam workbook (addin). Is there a way to do this? thx
    
    [Reply](https://trumpexcel.com/assign-macro-to-button-in-excel/#comment-13853)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/assign-macro-to-button-in-excel/#respond)

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