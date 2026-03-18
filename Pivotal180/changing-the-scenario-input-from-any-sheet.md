# How to Change the Scenario Input From Any Spreadsheet

**Source:** https://pivotal180.com/changing-the-scenario-input-from-any-sheet

---

[Skip to content](https://pivotal180.com/changing-the-scenario-input-from-any-sheet/#fl-main-content)

Changing the Scenario Input From Any Sheet
==========================================

By Haydn Palliser | September 19, 2024

**Changing the Scenario Input From Any Sheet** 

### Overview

This video is a new lesson from our online financial modeling courses

This lesson provides instructions to create a combo box which will allow you to  change scenarios from any sheet. This will make models much easier to present and to review.

### Video

**Video Transcript** 

**Haydn:** This lesson, we’ll introduce a concept called a combo box that will significantly improve your ability to assess different scenarios. A combo box is a scenario selection dropdown box that allows you to change the scenario from any sheet. And here is what we mean. Notice here how I can change the active scenario on the Dashboard sheet. This enables me to review how inputs vary when the inputs change without having to return to the input sheet each time I wish to select a new scenario. In this example, I also have a scenario input box called a combo box on the Calculation sheet of this demo model. It is so much easier seeing how the model calculations and outputs change when you can directly change the scenario on the relevant sheet. Before we get into how to create a combo box, we encourage you to download the model attached to this lesson. Alternatively, you can use any model with a scenario input already included, perhaps your course model to date. So over to you, Bastian.

**Bastian:** We must first set up the model by adding the Developer tab to the Excel ribbon if you don’t already have it. This is because the function we will use called a combo box is on the Developer tab in Excel. For Windows users, click File, Options, or by shortcut, Alt + F + T, and then click on Customize Ribbon. For Mac users go to Preferences, Ribbon and then to Toolbar. With either operating system, tick off Developer and click OK. Once you have Developer ticked off, it will be on your ribbon for all future Excel sessions.

**Haydn:** Next, we must store the scenario inputs we wish to select from. We will do that on our N sheet. We can add a title here in F20 called Scenario Inputs. In cell F21, we hard code a value as 1 and we style this as a technical input. In cell F22, we type = F21 + 1. We will have four scenarios in this model, so we copy down to F24. These are the four scenario inputs that we wish to select from. Now you may think this is duplicative work as we already have the case numbers stored in our Input sheet in cells E5 to H5. However, for this combo box to work, the scenario inputs must be vertically laid out. Now we are ready to add the dropdown box. Critically the combo box must be created on a different sheet to the scenario inputs list. We will create our dropdown box on the Calculation sheet.

**Bastian:** To add the box, go to Developer tab under Controls and Insert. Here you can go to Form Controls and click on the second top-left button called Combo Box Form Control. When you do that, your cursor has changed to a plus sign signifying you can click and drag to create your box. Start in the upper-left corner of cell D2 and click and hold your mouse button and keep holding down the mouse button until the bottom-right corner of cell D2, or until the box is the size you want it to be. Release your mouse button to finalize the box. You can now see the dropdown box. You can modify the size and the position of the box by clicking and dragging, or if you already clicked off the box, right-clicking the combo box first and then dragging to change the size. If you put your cursor on the box, you will see a hands meaning this is a clickable cell. If you click the dropdown list, you will see there are no options to select from. We must populate the combo box with the scenario inputs and tell Excel which cell these inputs should change. To do so, right-click the box and select Format Control. A dialogue box appears. We need to populate the Input range and the Cell link. The Input range refers to the scenario input cases on the N sheet. Click in the Input range box, or on the up arrow on the right-hand side of the box, and then navigate to the N sheets and select cells F21 to F24 and press Enter. This means that the inputs we may select will be from one through four. Next, we need to add the Cell link. The cell link is a cell that the scenario inputs need to change. To do this, click in the Cell link box or on the up arrow on the right-hand side of the box. Then navigate to the Input sheets and select sell C2. With these inputs, we are asking the combo box to input one of these values from the input range into cell C2 on the Input sheets. Press OK. Don’t worry about the value errors you’re getting. Simply select 1 from the new dropdown box, the value errors go away. Just to be clear, whatever value is selected in the combo box is inserted into C2 on the Input sheets. For example, select 2 in the combo box. Now on the Input sheets, we can see that in C2, Case 2 is active. And if we want to change the scenario to Case 1 again, from the Input sheets, we can. We are not overriding the existing case selector in C2.

**Haydn:** So why did we get a value error then? The value error was the result of the input value not having been selected when we first created the box. The input value was thus zero, which would now result in my index function in column C of the input sheet not working. What is cool is that now we have one combo box, we can copy it to the other sheets. To do that, we first need to navigate to the combo box. on the Calculation sheet. You can hover over the cell and right-click, then click Copy. Go to the Dashboard sheet, click on D2 and press Control + V. We can move it into place and now we have a combo box here as well. Now we can change scenarios from any sheet. This will make models much easier to present and to review. Feel free to also download the PDF attached as a reminder for how to create these.

Note The PDF is only available in the online courses  not as part of this article.

#### Share This Resource

[](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fpivotal180.com%2Fchanging-the-scenario-input-from-any-sheet%2F)

[](https://twitter.com/share?url=https%3A%2F%2Fpivotal180.com%2Fchanging-the-scenario-input-from-any-sheet%2F)

[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fpivotal180.com%2Fchanging-the-scenario-input-from-any-sheet%2F)

[](https://pivotal180.com/cdn-cgi/l/email-protection#0d326f626974306579797d7e283e4c283f4b283f4b7d647b62796c613c353d236e6260283f4b6e656c636a64636a20796568207e6e68636c7f64622064637d7879206b7f6260206c6374207e65686879283f4b)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%20200'%3E%3C/svg%3E)

### Haydn Palliser

[https://www.linkedin.com/in/haydnpalliser/](https://www.linkedin.com/in/haydnpalliser/)

Complexity simplified.
----------------------

Advisory, financial modeling, and training courses within climate change, sustainable finance, renewable energy, and infrastructure.  
We don’t just teach you how to build models. We teach you how to do deals.

[VIEW ALL OF OUR COURSES](https://pivotal180.com/all-courses/)

[ENQUIRE ABOUT OUR SERVICES](https://pivotal180.com/contact-us/#form)

[Scroll To Top](https://pivotal180.com/changing-the-scenario-input-from-any-sheet/#)

### Download Free Brochure

Fill out the form to download your brochure now.

"\*" indicates required fields

First Name\*

Last Name\*

Email\*

CAPTCHA