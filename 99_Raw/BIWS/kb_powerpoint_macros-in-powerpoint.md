# Macros in PowerPoint: Full Tutorial

**Source:** https://breakingintowallstreet.com/kb/powerpoint/macros-in-powerpoint

---

Macros in PowerPoint: Full Tutorial and How to Write VBA Code for a “Swap Multiple Shapes” Macro
================================================================================================

In this tutorial, you’ll learn how to set up macros in PowerPoint, and you’ll get practice writing VBA code for your first macro.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/powerpoint/macros-in-powerpoint/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/powerpoint/macros-in-powerpoint/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/powerpoint/macros-in-powerpoint/#tab-signup)
    

Macros in PowerPoint: Full Tutorial and How to Write VBA Code for a “Swap Multiple Shapes” Macro

  
**Macros in PowerPoint** are useful for tasks such as performing tricky alignments, fitting shapes within tables, and using Drawing Guides, rather than physical lines, to distribute shapes.

Before you start using macros or writing your own VBA code, you must understand the fundamentals of PowerPoint: features like [the Quick Access Toolbar](https://breakingintowallstreet.com/kb/powerpoint/powerpoint-quick-access-toolbar/)
, [the Slide Master](https://breakingintowallstreet.com/kb/powerpoint/powerpoint-slide-master/)
, [Tables](https://breakingintowallstreet.com/kb/powerpoint/tables-in-powerpoint/)
, and [how to duplicate a shape](https://breakingintowallstreet.com/kb/powerpoint/how-to-duplicate-a-shape-in-powerpoint/)
.

It’s counterproductive to “automate” slides and presentations unless you first understand the key PowerPoint commands and shortcuts.

In this tutorial, we’ll walk you through **how to create your first PowerPoint macro**, which you can use to swap the positions of multiple shapes.

This code is simple, but it is also very useful because it typically takes several keyboard shortcuts and mouse drags to swap shapes manually, so an automated solution is a clear win.

And amazingly, there is no built-in way to do this in the standard version of PowerPoint.

![PowerPoint Pro](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20128%20128'%3E%3C/svg%3E)

### Become a PowerPoint Pro With the **BIWS PowerPoint & VBA Course**

*   #### Become a presentation machine
    
    Master the key shortcuts and commands for “warp speed” slide creation
    
*   #### Acquire the skills with dozens of practice exercises
    
    Learn by doing – and check your work against the solutions
    
*   #### Save hours with our full macro package (25+ macros)
    
    Automate formatting, tables, alignment, drawing guides, and more
    

[Full Details](https://breakingintowallstreet.com/powerpoint-pro/)
 [Short Outline](https://biws-support.s3.us-east-1.amazonaws.com/Course-Outlines/PowerPoint-Pro-Course-Outline.pdf)

### **Video Table of Contents:**

**0:58:** Why Macros Are Useful in PowerPoint

**2:44:** PowerPoint Macro Demo

**6:27:** Lesson Overview

**6:40:** VBA in Excel vs. PowerPoint

**10:09:** Simple “Shape Swap” Macro

**18:29:** Macro to Swap Multiple Shapes

**25:29:** Recap and Summary

### **Files & Resources:**

[Slide Presentation – Macros in PowerPoint and VBA Tutorial (PDF)](https://youtube-breakingintowallstreet-com.s3.amazonaws.com/Macros-in-PowerPoint-VBA-Tutorial-Slides.pdf)

[Reference Slides for Macro Exercise (PPT)](https://youtube-breakingintowallstreet-com.s3.amazonaws.com/Macros-in-PowerPoint-Ref-Slide.pptx)

[“Finished” Version of Macro and Reference Slides (PPTM)](https://youtube-breakingintowallstreet-com.s3.amazonaws.com/Macros-in-PowerPoint-Ref-Slide.pptm)

**PowerPoint Macros and VBA in Excel vs. PowerPoint**
-----------------------------------------------------

Before jumping into the code, it’s worth asking two key questions:

1.  What are the **advantages and disadvantages** of VBA and macros in Excel vs. PowerPoint?
2.  What are **good vs. bad use cases** for macros in PowerPoint? In other words, what is the _most effective_ way to spend your time automating your presentations?

On the first question, [VBA in Excel](https://breakingintowallstreet.com/kb/excel/excel-vba-programming/)
 is **simpler to set up and use for quick macros**.

Excel has a macro recorder, so you can record your actions in a spreadsheet, review them in the VBA Editor, and modify the code to do what you want.

Also, assigning keyboard shortcuts to your macros is easy because you always select a keyboard shortcut when you record actions in the macro recorder.

By contrast, PowerPoint macros are **more difficult to set up but are arguably more powerful**.

Most Excel macros function based on a **selected range of cells** in a single spreadsheet and automate processes like color-coding the cells or changing the decimal places.

That’s nice, but PowerPoint macros often **change the entire presentation**, including on normal slides and templates in [the Slide Master](https://breakingintowallstreet.com/kb/powerpoint/powerpoint-slide-master/)
.

Also, PowerPoint macros **do not break the “Undo” command**, so you can press Ctrl + Z (or ⌘ + Z on Mac) repeatedly, and it will work correctly with all macros.

But in Excel, macros break the Undo and Redo commands unless you build a workaround into your code, which can get very complicated.

Here’s a summary of VBA in Excel vs. PowerPoint:

![VBA in Excel vs. PowerPoint](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201051%20503'%3E%3C/svg%3E "VBA in Excel vs. PowerPoint")

Returning to the second question above – good vs. bad use cases for macros in PowerPoint – **focus on** **macros that are simple to code and that automate actions you repeat _a lot_**.

For example, swapping shapes is quite simple to code (5-10 minutes), and it saves you time because it’s cumbersome to swap shape positions manually. Plus, it’s a common task when editing presentations.

On the other hand, it’s silly to write a macro that “centers” a shape vertically and horizontally on a slide because the “Align Center” and “Align Middle” commands already do this, and it’s not especially common to center single shapes on a slide in corporate presentations.

Something like the Table of Contents macro in our full macro package, which is based on the Slide Master and custom layouts, is in the “maybe” category.

It saves you time, but it’s also complicated to code and test, and it doesn’t work 100% perfectly in all cases.

Plus, you might only add the Table of Contents when you’re finished with a presentation, so this macro may be less useful than simpler shape manipulation commands.

**Your First PowerPoint Macro: “Swap Shapes”**
----------------------------------------------

To start writing your first macro, go to the “Trust Center” in PowerPoint (Alt, T, O in the PC version or ⌘ + , on Mac) and make sure the program will let you run macros:

![PowerPoint Trust Center](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20840%20685'%3E%3C/svg%3E "PowerPoint Trust Center")

![PowerPoint Trust Center - Macro Security Settings](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20840%20685'%3E%3C/svg%3E "PowerPoint Trust Center - Macro Security Settings")

Use one of the settings above (the screens will look slightly different on the Mac) and make sure the “Developer Toolbar” in the ribbon menu is visible by going to “Customize Ribbon” within the Options menu:

![PowerPoint Ribbon Menu and Developer Tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20840%20685'%3E%3C/svg%3E "PowerPoint Ribbon Menu and Developer Tab")

Once you’ve done this, open the VBA Editor with Alt, L, V on the PC (there is no Mac shortcut, so navigate there manually) and insert a “module” and a “subroutine” to write a new macro:

![Macros in PowerPoint - Adding a Module and Subroutine](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20581%20501'%3E%3C/svg%3E "Macros in PowerPoint - Adding a Module and Subroutine")

You can call the new module “SwapShapes” and add a new subroutine with the same name on the right side of the screen:

![Macros in PowerPoint - VBA Subroutine](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20711%20553'%3E%3C/svg%3E "Macros in PowerPoint - VBA Subroutine")

After you type “Sub SwapShapes()” VBA will automatically insert the “End Sub” at the end to indicate that your macro ends there.

With simple macros, you usually want to **work with the shapes, slides, or text the user has selected**.

That’s how this “Swap Shapes” macro will work: it will _assume_ that the user has selected the shapes they want to swap, and then it will change their positions.

First, you need to make sure _the user has selected shapes_, and if so, that they’ve selected _2 shapes_ rather than 1, 10, or 50 shapes:

![PowerPoint VBA - Checking the User's Shape Selection](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20604%20302'%3E%3C/svg%3E "PowerPoint VBA - Checking the User's Shape Selection")

“IF” statements are the building blocks of all programming languages, including VBA.

They let you check conditions, such as the selection consisting of 2 shapes, and they take actions based on whether these conditions are true or false.

The ActiveWindow.Selection object in VBA contains whatever the user has selected (shapes, slides, text, or nothing at all), and it has “properties” for things like the _selection type_ and the _number of objects selected_.

You can use the “IF” statements with ActiveWindow.Selection to check for these conditions.

If you’re unsure of an object’s properties, you can start typing its name followed by a “.” so that VBA displays a list of options.

The “=” operator is used for both **assignments** and **equality checks** in VBA, which is a bit confusing. But if it’s part of an “IF” statement, as it is here, it’s an equality check.

The MsgBox command is useful for **testing the code as you move along** and ensuring the “IF” statements work.

Next, you need to save the first shape’s **Top and Left positions** and put them in “variables” that you can refer to later.

Here’s the code:

![PowerPoint VBA - Saving the Shape Positions in Variables](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20950%20336'%3E%3C/svg%3E "PowerPoint VBA - Saving the Shape Positions in Variables")

The “=” signs in the main part of the code are **assignment operators** because they’re _not_ within “IF” statements.

So, they SET one shape’s Left and Top coordinates to the other shape’s Left and Top coordinates.

Again, it is confusing how “=” can check for equality in VBA _and_ set the value of a variable; there is no easy answer other than “continued practice and exposure.”

The ActiveWindow.ShapeRange(1) part means: “Take the _first_ shape the user has selected on the current slide.”

You can use ActiveWindow.ShapeRange(2) to refer to the second shape, which takes us into the next part: setting the first shape’s Top and Left positions to those of the second shape.

![PowerPoint VBA - Changing the First Shape's Top and Left Positions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20814%20395'%3E%3C/svg%3E "PowerPoint VBA - Changing the First Shape's Top and Left Positions")

If you stopped here, you’d have a problem because you’ve now **lost** the first shape’s original Top and Left positions.

This is why you saved them in the tempLeft and tempTop variables: by saving these original positions in variables, you can now use them to change the second shape’s position.

![Macros in PowerPoint: Swapping the Original Positions of the First Shape with the Second Shape](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20819%20449'%3E%3C/svg%3E "Macros in PowerPoint: Swapping the Original Positions of the First Shape with the Second Shape")

This code properly swaps the positions of two shapes.

However, you can make it more efficient by using a “With” statement, which also exists in Excel VBA, to remove the need to type ActiveWindow.Selection:

![PowerPoint VBA and "With" Statements](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20592%20526'%3E%3C/svg%3E "PowerPoint VBA and "With" Statements")

When you type the “With ActiveWindow.Selection” line, anything that starts with a “.” between that and the “End With” is assumed to be part of ActiveWindow.Selection.

So, VBA “translates” a line like this:

tempLeft = .ShapeRange(1).Left

Into:

tempLeft = ActiveWindow.Selection.ShapeRange(1).Left

You can now go into PowerPoint and test this macro with different shapes on the reference slides.

To do this, use the Alt, L, PM shortcut in the PC version (no Mac equivalent, so navigate to Developer in the ribbon menu and click on Macros), select “SwapShapes” and click “Run”:

!["Shape Swap" Macro Execution on a Normal PowerPoint Slide](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201012%20758'%3E%3C/svg%3E ""Shape Swap" Macro Execution on a Normal PowerPoint Slide")

As a final step, you can save this file as a **macro-enabled presentation** in the .pptm format:

![Saving Macros in a Macro-Enabled PowerPoint File](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20946%20533'%3E%3C/svg%3E "Saving Macros in a Macro-Enabled PowerPoint File")

By doing this, you’ll ensure that whoever opens the file next can still use this macro.

**The Limitations of Macros in PowerPoint**
-------------------------------------------

This simple exercise, while useful, also reveals a few issues with macros in PowerPoint:

**1) Keyboard Shortcuts** – There is no easy way to assign keyboard shortcuts to macros; you must activate them through the “Macros” menu in the Developer Toolbar.

**2) Macro-Enabled Files** – While you _can_ save macros with the above method, it is not ideal for sharing them or making them usable across different presentations.

**3) Code Constraints** – It’s simple to write code that handles _only 2 shapes_, but it’s not immediately obvious how to extend it to manage multiple shapes.

We could fix these issues now or explore other enhancements, but the first two points above are surprisingly complicated to solve.

So, we’ll focus on point #3 and extend this macro to make it swap multiple shapes:

**An Extension to Macros in PowerPoint: “Swap Multiple Shapes”**
----------------------------------------------------------------

You can extend this macro to swap multiple shapes with a few simple changes.

Start by **changing the variable declarations and error checks** at the top.

When the user selects multiple shapes, you need to **save the first shape’s positions**, and you need to create a “counter variable” that tracks the shape # you’re currently on.

For example, if the user has selected 10 shapes, you need to know if you’re currently on shape #1, #2, #3, or #4-10 as you move through the selection and change each shape’s positions.

Also, you need to make sure the user has selected _more than 1 shape_ – not necessarily just 2 shapes:

![PowerPoint VBA - Checking to Ensure That More Than 1 Shape is Selected](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20538%20345'%3E%3C/svg%3E "PowerPoint VBA - Checking to Ensure That More Than 1 Shape is Selected")

Next, you need to “loop” through all the shapes the user has selected with a “For” statement.

So, if the user has selected 10 shapes, you need to move from shape #1 through shape #10 and change the position of each shape.

You can start by typing the syntax for this “For” loop:

![PowerPoint VBA - For/Next Loop for Selected Shapes](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20826%20406'%3E%3C/svg%3E "PowerPoint VBA - For/Next Loop for Selected Shapes")

For an example of how this works, continue assuming that the user has selected 10 shapes.

In this case, you should loop through shapes #1 – #9 and set each shape’s Left and Top positions to the next shape’s Left and Top positions.

So, Shape #1 Top should become Shape #2 Top, and Shape #2 Top should become Shape #3 Top.

When you reach shape #10, you should set its Top and Left positions to those of the _first shape_.

This means you need to save shape #1’s Top and Left positions before starting this loop.

You can start by handling the case for shapes #1 – 9, or “everything before the final shape”:

![PowerPoint VBA - Modifying the "For" Loop for Everything Before the Final Shape](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20941%20379'%3E%3C/svg%3E "PowerPoint VBA - Modifying the "For" Loop for Everything Before the Final Shape")

As the next step, you can add a special case to save the first shape’s position before the “For” loop and set the last shape’s position equal to the first shape’s:

![Macros in PowerPoint: Saving the First Shape's Positions and Swapping Them in for the Last Shape](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20888%20548'%3E%3C/svg%3E "Macros in PowerPoint: Saving the First Shape's Positions and Swapping Them in for the Last Shape")

You can now test these changes on the reference slides and verify that this macro “rotates” multiple shapes:

![Macros in PowerPoint: Testing the Shape Swap Macro with Multiple Shapes on the Reference Slides](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201011%20382'%3E%3C/svg%3E "Macros in PowerPoint: Testing the Shape Swap Macro with Multiple Shapes on the Reference Slides")

Activate the macro enough times, and the shapes will return to their original positions.

**Macros in PowerPoint: Beyond the Surface-Level Detail**
---------------------------------------------------------

If you’ve followed the steps above, you should have a “Multi-Shape Swap” macro you can use to rearrange your slides.

But this tutorial just scratches the surface; it represents ~30 minutes out of the 12-13 hours of VBA training in our [full PowerPoint Pro course](https://breakingintowallstreet.com/powerpoint-pro/)
.

You can do far more with macros and VBA than simple shape manipulation – as shown in the video above, you can manipulate tables, combined table/shape designs, and even the Language properties of entire presentations.

And you can automate the alignment, distribution, and formatting processes in many ways, including the clever use of Drawing Guides.

You can see the full set of macros in the course below:

![Macros in PowerPoint: Full BIWS Macro Package, Part 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20727%20106'%3E%3C/svg%3E "Macros in PowerPoint: Full BIWS Macro Package, Part 1")

![Macros in PowerPoint: Full BIWS Macro Package, Part 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20737%2094'%3E%3C/svg%3E "Macros in PowerPoint: Full BIWS Macro Package, Part 2")

![Macros in PowerPoint: Full BIWS Macro Package, Part 3](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20519%2099'%3E%3C/svg%3E "Macros in PowerPoint: Full BIWS Macro Package, Part 3")

You’ll gain access to the full package and all the detailed tutorials as soon as you sign up for the PowerPoint Pro course:

[See BIWS Powerpoint Pro](https://breakingintowallstreet.com/powerpoint-pro/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Slide Presentation – Macros in PowerPoint and VBA Tutorial (PDF)](https://youtube-breakingintowallstreet-com.s3.amazonaws.com/Macros-in-PowerPoint-VBA-Tutorial-Slides.pdf)
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Reference Slides for Macro Exercise (PPT)](https://youtube-breakingintowallstreet-com.s3.amazonaws.com/Macros-in-PowerPoint-Ref-Slide.pptx)
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) “Finished” Version of Macro and Reference Slides (PPTM)](https://youtube-breakingintowallstreet-com.s3.amazonaws.com/Macros-in-PowerPoint-Ref-Slide.pptm)
    

Premium Courses
---------------

Combined shape 37 Created with Sketch.

Based on the content of this tutorial, our recommended Premium Course Upgrade is...

[PowerPoint Pro](https://breakingintowallstreet.com/powerpoint-pro/)

Master PowerPoint by creating a sell-side M&A and valuation pitch book for Jazz Pharmaceuticals - plus company/deal profiles and more.

[Learn More](https://breakingintowallstreet.com/powerpoint-pro/)

### Other BIWS Courses Include:

Polygon 1 Created with Sketch.

[BIWS Premium](https://breakingintowallstreet.com/biws-premium/)
: Get the Excel & VBA, Core Financial Modeling, and PowerPoint Pro courses together and learn everything from Excel shortcuts up through financial modeling, valuation, M&A and LBO deals, and the key PowerPoint shortcuts and commands. [Learn More![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2019%2020'%3E%3C/svg%3E)](https://breakingintowallstreet.com/biws-premium/)

Polygon 1 Created with Sketch.

[BIWS Platinum](https://breakingintowallstreet.com/platinum/)
: The most comprehensive package on the market today for investment banking, private equity, hedge funds, and other finance roles. Includes ALL the courses on the site at a huge discount, plus updates and new additions over time. [Learn More![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2019%2020'%3E%3C/svg%3E)](https://breakingintowallstreet.com/platinum/)

Share

[X](https://x.com/intent/tweet?text=Macros%20in%20PowerPoint%3A%20Full%20Tutorial%20and%20How%20to%20Write%20VBA%20Code%20for%20a%20%E2%80%9CSwap%20Multiple%20Shapes%E2%80%9D%20Macro&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fpowerpoint%2Fmacros-in-powerpoint%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fpowerpoint%2Fmacros-in-powerpoint%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Macros%20in%20PowerPoint%3A%20Full%20Tutorial%20and%20How%20to%20Write%20VBA%20Code%20for%20a%20%E2%80%9CSwap%20Multiple%20Shapes%E2%80%9D%20Macro&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fpowerpoint%2Fmacros-in-powerpoint%2F&mini=true)
[Email](mailto:?subject=Macros%20in%20PowerPoint%3A%20Full%20Tutorial%20and%20How%20to%20Write%20VBA%20Code%20for%20a%20%E2%80%9CSwap%20Multiple%20Shapes%E2%80%9D%20Macro&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fpowerpoint%2Fmacros-in-powerpoint%2F)

#### Perfect Your PowerPoint Skills

The BIWS PowerPoint Pro course gives you everything you need to complete pitch books and presentations in half the time and move straight to the front of the "top tier bonus" line.

[LEARN MORE](https://breakingintowallstreet.com/powerpoint-pro/)

[](https://x.com/intent/tweet?text=Macros%20in%20PowerPoint%3A%20Full%20Tutorial%20and%20How%20to%20Write%20VBA%20Code%20for%20a%20%E2%80%9CSwap%20Multiple%20Shapes%E2%80%9D%20Macro&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fpowerpoint%2Fmacros-in-powerpoint%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fpowerpoint%2Fmacros-in-powerpoint%2F)
[](https://www.linkedin.com/shareArticle?title=Macros%20in%20PowerPoint%3A%20Full%20Tutorial%20and%20How%20to%20Write%20VBA%20Code%20for%20a%20%E2%80%9CSwap%20Multiple%20Shapes%E2%80%9D%20Macro&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fpowerpoint%2Fmacros-in-powerpoint%2F&mini=true)
[](mailto:?subject=Macros%20in%20PowerPoint%3A%20Full%20Tutorial%20and%20How%20to%20Write%20VBA%20Code%20for%20a%20%E2%80%9CSwap%20Multiple%20Shapes%E2%80%9D%20Macro&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fpowerpoint%2Fmacros-in-powerpoint%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/powerpoint/macros-in-powerpoint/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fpowerpoint%2Fmacros-in-powerpoint%2F&title=Macros%20in%20PowerPoint%3A%20Full%20Tutorial%20and%20How%20to%20Write%20VBA%20Code%20for%20a%20%E2%80%9CSwap%20Multiple%20Shapes%E2%80%9D%20Macro)
[](https://api.whatsapp.com/send?text=Macros%20in%20PowerPoint%3A%20Full%20Tutorial%20and%20How%20to%20Write%20VBA%20Code%20for%20a%20%E2%80%9CSwap%20Multiple%20Shapes%E2%80%9D%20Macro+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fpowerpoint%2Fmacros-in-powerpoint%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=Macros%20in%20PowerPoint%3A%20Full%20Tutorial%20and%20How%20to%20Write%20VBA%20Code%20for%20a%20%E2%80%9CSwap%20Multiple%20Shapes%E2%80%9D%20Macro%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fpowerpoint%2Fmacros-in-powerpoint%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fpowerpoint%2Fmacros-in-powerpoint%2F&text=Macros%20in%20PowerPoint%3A%20Full%20Tutorial%20and%20How%20to%20Write%20VBA%20Code%20for%20a%20%E2%80%9CSwap%20Multiple%20Shapes%E2%80%9D%20Macro)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/powerpoint/macros-in-powerpoint/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/powerpoint/macros-in-powerpoint/)
[Copy](https://breakingintowallstreet.com/kb/powerpoint/macros-in-powerpoint/#)
[Email](mailto:?subject=Macros%20in%20PowerPoint%3A%20Full%20Tutorial%20and%20How%20to%20Write%20VBA%20Code%20for%20a%20%E2%80%9CSwap%20Multiple%20Shapes%E2%80%9D%20Macro&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fpowerpoint%2Fmacros-in-powerpoint%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fpowerpoint%2Fmacros-in-powerpoint%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fpowerpoint%2Fmacros-in-powerpoint%2F&title=Macros%20in%20PowerPoint%3A%20Full%20Tutorial%20and%20How%20to%20Write%20VBA%20Code%20for%20a%20%E2%80%9CSwap%20Multiple%20Shapes%E2%80%9D%20Macro)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/powerpoint/macros-in-powerpoint/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/powerpoint/macros-in-powerpoint/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fpowerpoint%2Fmacros-in-powerpoint%2F&t=Macros%20in%20PowerPoint%3A%20Full%20Tutorial%20and%20How%20to%20Write%20VBA%20Code%20for%20a%20%E2%80%9CSwap%20Multiple%20Shapes%E2%80%9D%20Macro)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fpowerpoint%2Fmacros-in-powerpoint%2F&text=Macros%20in%20PowerPoint%3A%20Full%20Tutorial%20and%20How%20to%20Write%20VBA%20Code%20for%20a%20%E2%80%9CSwap%20Multiple%20Shapes%E2%80%9D%20Macro)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Macros%20in%20PowerPoint%3A%20Full%20Tutorial%20and%20How%20to%20Write%20VBA%20Code%20for%20a%20%E2%80%9CSwap%20Multiple%20Shapes%E2%80%9D%20Macro&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fpowerpoint%2Fmacros-in-powerpoint%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fpowerpoint%2Fmacros-in-powerpoint%2F&title=Macros%20in%20PowerPoint%3A%20Full%20Tutorial%20and%20How%20to%20Write%20VBA%20Code%20for%20a%20%E2%80%9CSwap%20Multiple%20Shapes%E2%80%9D%20Macro)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fpowerpoint%2Fmacros-in-powerpoint%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/powerpoint/macros-in-powerpoint/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fpowerpoint%2Fmacros-in-powerpoint%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=Macros%20in%20PowerPoint%3A%20Full%20Tutorial%20and%20How%20to%20Write%20VBA%20Code%20for%20a%20%E2%80%9CSwap%20Multiple%20Shapes%E2%80%9D%20Macro%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fpowerpoint%2Fmacros-in-powerpoint%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/powerpoint/macros-in-powerpoint/)
[Pinterest](https://breakingintowallstreet.com/kb/powerpoint/macros-in-powerpoint/#)
[Print](https://breakingintowallstreet.com/kb/powerpoint/macros-in-powerpoint/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fpowerpoint%2Fmacros-in-powerpoint%2F&title=Macros%20in%20PowerPoint%3A%20Full%20Tutorial%20and%20How%20to%20Write%20VBA%20Code%20for%20a%20%E2%80%9CSwap%20Multiple%20Shapes%E2%80%9D%20Macro)
[SMS](sms:?&body=Macros%20in%20PowerPoint%3A%20Full%20Tutorial%20and%20How%20to%20Write%20VBA%20Code%20for%20a%20%E2%80%9CSwap%20Multiple%20Shapes%E2%80%9D%20Macro%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fpowerpoint%2Fmacros-in-powerpoint%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fpowerpoint%2Fmacros-in-powerpoint%2F&text=Macros%20in%20PowerPoint%3A%20Full%20Tutorial%20and%20How%20to%20Write%20VBA%20Code%20for%20a%20%E2%80%9CSwap%20Multiple%20Shapes%E2%80%9D%20Macro)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fpowerpoint%2Fmacros-in-powerpoint%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fpowerpoint%2Fmacros-in-powerpoint%2F)
[X](https://x.com/intent/tweet?text=Macros%20in%20PowerPoint%3A%20Full%20Tutorial%20and%20How%20to%20Write%20VBA%20Code%20for%20a%20%E2%80%9CSwap%20Multiple%20Shapes%E2%80%9D%20Macro&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fpowerpoint%2Fmacros-in-powerpoint%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fpowerpoint%2Fmacros-in-powerpoint%2F)
[WhatsApp](https://api.whatsapp.com/send?text=Macros%20in%20PowerPoint%3A%20Full%20Tutorial%20and%20How%20to%20Write%20VBA%20Code%20for%20a%20%E2%80%9CSwap%20Multiple%20Shapes%E2%80%9D%20Macro+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fpowerpoint%2Fmacros-in-powerpoint%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fpowerpoint%2Fmacros-in-powerpoint%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fpowerpoint%2Fmacros-in-powerpoint%2F&title=Macros%20in%20PowerPoint%3A%20Full%20Tutorial%20and%20How%20to%20Write%20VBA%20Code%20for%20a%20%E2%80%9CSwap%20Multiple%20Shapes%E2%80%9D%20Macro&image=&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand