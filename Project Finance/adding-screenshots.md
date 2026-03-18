# Adding UserForms

**Source:** https://edbodmer.com/adding-screenshots

---

This page shows how you can easily add forms to your sheet. You may have seen the forms in the generic macros or some of the other files. I use the userforms to keep track of how long something is taking and test the BS that is mentioned in blogs about using a whole line slowing down excel. I use and example where you can use vbModeless and not press a button and then you should I think use the DoEvents. I document how to use the userforms to do this in this page because I often forget how to do this. I use an example where you can send a special card for a birthday or another holiday (please no Valentines day card because this is not a good holiday). For me, a big use of the userforms is to test different ideas about the speed of an excel program. There are a lot of fairy tales about things the slow excel down or make the files big. To test the important issue about speed you can use the methods below. I have attached a few examples to the buttons below with examples of how to use userforms (in the context of the important issue of introducing your child to excel).

.

**[Excel File for with Userforms and Timing Tabulations to Test Speed with Example for Four Year Old](javascript:void(0);)
**

.

.

.

Step 1: Insert Form for Userform and Lay out

I use the example of an excel model that was made for a six year old. I would guess that six year old is about the correct age for starting excel. After inserting a userform, you can put in a label and a picture etc. I use a screenshot and a text input box. After putting things on the userform, use the right-click and go to properties and change the colours and fonts etc. When making a screenshot, save as a JPEG. The screenshot below shows you how to import a picture using properties. Note that when you want to change a property, you can right click and go to properties. This may be too obvious, but I was getting confused by this sort of little thing.

![](https://edbodmer.com/wp-content/uploads/2023/02/image-14.png)

When you use the button to start the program, you should press the button and then hide the userform. This is userform9. You can then compute the time it takes to run the program. This userform.hide is a big deal for userforms that stay on the screen and do not automatically disappear. For userforms that disappear, you use vbModeless after you enter the userform.show (it would have to be userform1.show or userform2.show.

.

.

![](https://edbodmer.com/wp-content/uploads/2023/02/image-13.png)

.

Right click and go to the properties fro changing the colours etc.

![](https://edbodmer.com/wp-content/uploads/2023/01/image-12.png)

.

The code below illustrates how to make a userform that stops until data in entered and a button is pressed. I used to not use CINT and CSTR, but these are really helpful VBA commands.

Finishing with the buttons

.

When you just want to continue, use the userform1.hide

When you want to completely get out of the program use the END statement

![](https://edbodmer.com/wp-content/uploads/2023/01/image-13.png)

.

Modeless
--------

This is how to show the time taken. The trick is to use bot the vbModeless and the DoEvents

        time7 = Time
        time_difference = (time7 - time1) * 60 * 60 * 24
    
        UserForm13.Label1 = " Link Colour - Max Cols " & max_col & " Max Rows " & max_row
        UserForm13.Label2 = " Start Time " & time6 & " End " & time2 & Chr(10) & Chr(10) & _
                            " Time Taken " & Format(time_difference, "##.00")
        DoEvents
        UserForm13.Show vbModeless
    
    

.

The screenshot will remain until you close it.

.

        Unload UserForm13

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=16084&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=11504&rand=0.7976207038673102)