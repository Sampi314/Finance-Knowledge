# VBA Blogs: Painting with Excel

**Source:** https://sumproduct.com/blog/vba-blogs-painting-with-excel/

---

[Home](https://sumproduct.com/)

\> VBA Blogs: Painting with Excel

*   July 20, 2017

VBA Blogs: Painting with Excel
==============================

VBA Blogs: Painting with Excel
==============================

21 July 2017

One of the things I like to set up in Excel is when you click on a cell and something happens. I once had a great idea that you could actually paint in Excel setting up Worksheet events so that every time you would click a cell, it would change to some predefined colour. Then, of course, I realised it’d already been done.

Today, we’re going to cover the basics of how it would work, using the Worksheet\_SelectionChange event. This event triggers every time you select a new cell range in Excel. Note that this means if you select the range A1:A4, this will trigger an event, but if you then select range A4:A1 (i.e. starting from A4 and dragging upwards), because the same area is selected, it will not trigger the event again.

![](https://sumproduct.com/wp-content/uploads/2025/05/38def046018e936e450ba77db2dcd387.jpg)

The bit at the end says that we can refer to the actual range selected using the variable called “Target”. This means that we can do things to the target area, such as:

*   Target.Address: this will give us the cell range (e.g. “A1:A4”)
*   Target.Item(X): this lets us refer to specific cells within the selected range
*   Target.Interior: this lets us change the cell shading and pattern.

So, if we want to change the cell shading, then we can do so by using the following code:

Private Sub Worksheet\_SelectionChange(ByVal Target As Range)

With Target.Interior

    .Pattern = xlSolid

    .Color = 123456

End With

End Sub

This will take the location that we’ve selected, change the pattern to a Solid background, and set it to be the colour based on colour number 123456 (which in this case, happens to be a bright lime green colour).

![](<Base64-Image-Removed>)

Other useful worksheet commands include:

*   Worksheet\_Activate: an event which triggers whenever this sheet is activated (e.g. by clicking on the sheet tab)
*   Worksheet\_Calculate: an event which triggers every time the sheet (or the entire workbook) calculates
*   Worksheet\_Change: an event which triggers when a cell value is changed

Because there are only four Fridays this month, that wraps up the July VBA Event month blog series. Next week we have the Final Friday Fix, so look out for that! To keep you going until then though, we’ve uploaded a simple Excel Sheet that’s incorporated the rules for the game Tic Tac Toe (or Noughts and Crosses, depending on what you call it in your area). Feel free to download the file [here](https://sumproduct.com/assets/blog-pictures/2017/vba-fridays/tictactoe.xlsm)
 and have a play!

Until next time!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/vba-blogs-painting-with-excel/#0)
    
*   [Register](https://sumproduct.com/blog/vba-blogs-painting-with-excel/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/vba-blogs-painting-with-excel/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/vba-blogs-painting-with-excel/#0)

[](https://sumproduct.com/blog/vba-blogs-painting-with-excel/#0 "close")

top