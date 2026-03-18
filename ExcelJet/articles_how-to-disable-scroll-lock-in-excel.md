# How to turn off Scroll Lock in Excel | Exceljet

**Source:** https://exceljet.net/articles/how-to-disable-scroll-lock-in-excel

---

[Skip to main content](https://exceljet.net/articles/how-to-disable-scroll-lock-in-excel#main-content)

[](https://exceljet.net/articles/how-to-disable-scroll-lock-in-excel#)

*   [Previous](https://exceljet.net/articles/20-very-popular-excel-shortcuts)
    
*   [Next](https://exceljet.net/articles/top-10-reasons-to-learn-excel-formulas)
    

How to turn off Scroll Lock in Excel
====================================

by Dave Bruns · Updated 15 May 2024

![The evil scroll lock enabled in Excel 2010](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/evil%20scroll%20lock%20oval.png "The evil scroll lock enabled in Excel 2010")

Summary
-------

_Your report is due in an hour. You're working along in Excel, and suddenly you notice you can no longer move around properly. You press the arrow keys, but instead of the cursor moving to another cell, the entire worksheet seems to be moving about. WTF?!_ 

Before you panic, and call IT to tell them Excel is _broken_, check to see if Scroll Lock is to blame. Read below to learn how.

### What is Scroll Lock?

Usually, the arrow keys will move you one cell at a time in whatever direction you wish. However, when Scroll Lock is enabled, the worksheet is "scrolled" instead. The up and down arrow keys _scroll_ one row up and down, and the right and left arrow keys scroll one column right and left. The active cell never changes.

If you don't understand what's going on, this can be quite distressing :)

![The evil scroll lock, here to ruin your day](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/scroll%20lock%20on%20in%20excel%20status%20bar.png?itok=uqQ3XUpm "The evil scroll lock, here to ruin your day")

Fortunately, the Scroll Lock setting is a toggle, much like Caps Lock. If you have a Scroll Lock key on your keyboard, just press it to toggle Scroll Lock off. Done.

### No key for Scroll Lock?

Unfortunately, it's harder to disable Scroll Lock if your keyboard doesn't have a Scroll Lock key. How can you press a key you don't have?

The "trick" is to figure out how to send the equivalent of the Scroll Lock keystroke to Excel. The rest of this article explains how to do that on both Mac and Windows.

### Is Scroll Lock really on?

First, make sure Scroll Lock is really enabled. You can do this by working with the [status bar](https://exceljet.net/glossary/status-bar)
, the name for the bottom edge of the Excel Window, which displays various information about the state of the current worksheet.

**On Windows**, the status bar will display Scroll Lock if Scroll Lock is toggled on, _and if_ the Scroll Lock status is enabled in the status bar. If Scroll Lock status is not enabled in the status bar, it might be toggled on and you'll never see it.

Right-click the status bar to make sure Scroll Lock status is enabled:

![Scroll lock state enabled in Excel status bar](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/scroll%20lock%20state%20setting%20in%20status%20bar%20arrow.png?itok=ZqqaL0xb "Scroll lock state enabled in Excel status bar")

_The Scroll Lock setting here doesn't control Scroll Lock, it only displays Scroll Lock status._

Once you make sure that the Scroll Lock status is on, look for the Scroll Lock message in the lower left.

![Yes, scroll lock is enabled](https://exceljet.net/sites/default/files/images/articles/inline/scroll%20lock%20enabled%20small.png "Yes, scroll lock is enabled")

_Yes, Scroll Lock is turned on._

**On a Mac**, as far as I know, Scroll Lock status will not appear in the status bar of Excel 2011. (I haven't checked Excel 2016 yet). The only way I know to verify the Scroll Lock state is to use the arrow keys and observe behavior. Try moving around with the arrow keys and watch the address in the name box (directly left of the formula bar). If the address doesn't change, Scroll Lock is probably turned on.

![No scroll lock status on Mac 2011 status bar](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/mac%20excel%202011%20status%20shows%20no%20scroll%20lock.png?itok=SNQobaZH "No scroll lock status on Mac 2011 status bar")

_Mac Excel 2011 doesn't show scroll lock status anywhere._

### How to disable Scroll Lock on Windows

If you're using a full keyboard in Windows – one that has a Scroll Lock key – simply press the key to disable it. You should see the Scroll Lock message disappear from the status bar and then be able to move around normally.

If your keyboard does not have a Scroll Lock key, you can access a virtual keyboard in Windows via Start > All Programs > Accessories > Ease of Access > On-Screen Keyboard.

![Windows virtual keyboard](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/windows%20virtual%20keyboard%20smaller.png?itok=5XVtZ03p "Windows virtual keyboard")

_The On-Screen Keyboard in Windows, Scroll Lock key in white_

Once the keyboard is displayed, make sure Excel is the active application and click the ScrLk key. That should do it. 

### How to disable Scroll Lock on a Mac

The official Microsoft shortcut for Scroll Lock is Shift + F14. If you have an extended keyboard with an F14 key, try that first.

![Mac Extended Keyboard with F14 key highlighted](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/mac%20extended%20keyboard%20f14.png?itok=_RYZ-XLQ "Mac Extended Keyboard with F14 key highlighted")  
  
_A Mac Extended Keyboard has an F14 key (click to enlarge)_

If you have a MacBook Pro, or other machine with a smaller keyboard that does not have extended keys, you'll have to go a little deeper. You'd think that you could go to System Preferences > Keyboard, then enable an extended virtual keyboard, then use that to press F14. But, after an hour or so of fiddling around, I couldn't get it to work, and I'm not sure it can be done.

It seems that the Mac is "aware" of the keyboard currently attached, and uses this information to display the virtual keyboard. If you know a way to enable an extended virtual keyboard (on a Mac that doesn't have one attached), please let me know.

[Virtual Keyboard](http://download.cnet.com/VirtualKeyboard/3000-2094_4-40358.html)
, a commercial freeware utility by Corallo Software (14-day trial) seems to work, but I did very little testing.

### AppleScript to the rescue

On Macs, AppleScript is a built-in scripting language that can be used to automate applications and other general tasks. One of the things you can do with AppleScript is send keystrokes to an application.

While researching this problem, I ran into a nice AppleScript by Damien Clark [here](http://damos.world/2012/06/18/arrow-key-scroll-in-mac-excel/)
. However, I couldn't get the script work like I expected. I could _enable_ Scroll Lock with the script. But when I ran the script again, Scroll Lock wasn't _disabled_.

At least not without checking the "use all F1, F2, etc keys as standard function keys setting" checkbox in the Mac's keyboard preferences...which made the process pretty confusing.

So, after a bit more investigation (read: a few hours flailing about), I adapted the script to send the equivalent of fn + shift + F14, with a small delay. This works on my 2015 MacBook Pro reliably to turn Scroll Lock on and off.

\-- Workaround to enable and disable Scroll Lock in Excel on the Mac
-- For Macs that don't have an F14 key available
-- Tested on 2015 MBP running Mac OS 10.10.5 and Excel 2011 (14.5.8)
-- Dave Bruns, December 10, 2015

activate application "Microsoft Excel"
delay 0.5 -- time to release modifier keys
tell application "System Events"
    key code 63 -- fn key
    key code 107 using {shift down}
end tell

To use this script, run the AppleScript Editor, create a new file, and paste in the code above. Then compile the script (Command + K), and run it (play button, or Command + R).

If Scroll Lock is currently on, it should be disabled.

Caution: if Scroll Lock is _not_ currently enabled, it will be enabled, so you'll need to run the script _again_ to toggle it off again.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Thank you for your very clear explanation on how to test for an existing tab name in a workbook using ISREF and INDIRECT. With your guidance, I am able to build a flexible template that can use variables to test...I really like your site layout and your concise directions. Thank you again!

Thierry

[More Testimonials](https://exceljet.net/feedback)

Get [Training](https://exceljet.net/training)

----------------------------------------------

### Quick, clean, and to the point training

Learn Excel with high quality video training. Our videos are quick, clean, and to the point, so you can learn Excel in less time, and easily review key topics when needed. Each video comes with its own practice worksheet.

[View Paid Training & Bundles](https://exceljet.net/training)

[![Excel foundational video course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_excel.png "Excel foundational video course")](https://exceljet.net/training)

[![Excel Pivot Table video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_pivot.png "Excel Pivot Table video training course")](https://exceljet.net/training)

[![Excel formulas and functions video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_formula_0.png "Excel formulas and functions video training course")](https://exceljet.net/training)

[![Excel Charts video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_charts.png "Excel Charts video training course")](https://exceljet.net/training)

[![Video training for Excel Tables](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_excel_tables.png "Video training for Excel Tables")](https://exceljet.net/training)

[![Dynamic Array Formulas](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_dynamic_array_formulas_0.png "Dynamic Array Formulas")](https://exceljet.net/training)