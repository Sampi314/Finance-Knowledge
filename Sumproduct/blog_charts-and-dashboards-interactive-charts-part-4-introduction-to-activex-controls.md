# Charts and Dashboards: Interactive Charts – Part 4: Introduction to ActiveX Controls

**Source:** https://sumproduct.com/blog/charts-and-dashboards-interactive-charts-part-4-introduction-to-activex-controls/

---

[Home](https://sumproduct.com/)

\> Charts and Dashboards: Interactive Charts – Part 4: Introduction to ActiveX Controls

*   August 20, 2020

Charts and Dashboards: Interactive Charts – Part 4: Introduction to ActiveX Controls
====================================================================================

Charts and Dashboards: Interactive Charts – Part 4: Introduction to ActiveX Controls
====================================================================================

21 August 2020

_Welcome back to this week’s Charts and Dashboards blog series. This week, we will briefly talk about ActiveX Controls in Excel._

In addition to the various Form Controls, ActiveX Controls may be included in Excel or other programs. An ActiveX Control is a component program object that can be re-used by many application programs within a computer or among computers in a network. Whilst Form Controls are built into Excel, ActiveX Controls are loaded separately. Generally, Form Controls are used based on their simple nature, while ActiveX Controls allow for more flexible design and should be used when the task is not able to be done with the more basic Form Controls.

When installing new ActiveX Controls, the setup program for the controls usually register each control on the computer, which makes it available to use from Excel. If the control does not appear in the list, we must register it manually. It is also worth noting that, not all ActiveX Controls can be used directly on worksheets; some can be used only on Microsoft Visual Basic for Applications (VBA) UserForms. When working with these controls, Excel displays the message ‘Cannot insert object’ if we try to add them to a worksheet incorrectly.

From the Developer tab on the Ribbon, in the Controls group, click Insert, and then under ‘ActiveX Controls’, select a control, or click ‘More Controls’ to view all the available ActiveX controls. Then:

![](<Base64-Image-Removed>)

*   click the worksheet location where you want the ActiveX control to appear
*   to edit the control, make sure that you are in the Design mode by going to the Developer tab, and in the Controls group, turn on ‘Design Mode’
*   to specify the control properties, on the Developer tab, in the Controls group, click Properties (or right-click on the control then choose Properties). In the Properties dialog, for detailed information about each property, select the property, and then press **F1** to display a ‘Visual Basic Help’ topic, or type the property name in the ‘Visual Basic Help’ search box.

To register an ActiveX Control, first click the ActiveX Control that you want to register, making sure you do this in the Design Mode (**Developer -> Controls -> Design Mode**). Next, choose the ‘More Controls’ under ‘ActiveX Control’, similar to when selecting a control (above). Then, at the bottom of the ‘More Controls’ dialog, click ‘Register Custom’. In here, locate the folder containing the control file (with **.ocx** file name extension) or dynamically link the library file (with **.dll** file name extension) for the control you wish to register. Finally, select the file for the control, click ‘Open’.

That’s it for this week, check back next week for more Charts and Dashboards tips.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/charts-and-dashboards-interactive-charts-part-4-introduction-to-activex-controls/#0)
    
*   [Register](https://sumproduct.com/blog/charts-and-dashboards-interactive-charts-part-4-introduction-to-activex-controls/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/charts-and-dashboards-interactive-charts-part-4-introduction-to-activex-controls/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/charts-and-dashboards-interactive-charts-part-4-introduction-to-activex-controls/#0)

[](https://sumproduct.com/blog/charts-and-dashboards-interactive-charts-part-4-introduction-to-activex-controls/#0 "close")

top