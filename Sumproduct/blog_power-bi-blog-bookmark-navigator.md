# Power BI Blog: Bookmark Navigator

**Source:** https://sumproduct.com/blog/power-bi-blog-bookmark-navigator/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Bookmark Navigator

*   May 4, 2022

Power BI Blog: Bookmark Navigator
=================================

Power BI Blog: Bookmark Navigator
=================================

5 May 2022

To better support interaction between multiple navigators, bookmark groups and interaction with elements on the report, Power BI now ensures that once a bookmark is clicked on the navigator, it will continue to stay selected, regardless of changes in the report state. The “active” bookmark in any navigator will continue to stay active until another bookmark contained within the navigator is selected, either from the navigator or the Bookmarks pane. Before, selecting any other bookmark, including those not in the bookmark group represented by a navigator, would clear the selections in the bookmark navigator. This small behaviour change enables the use of multiple navigators targeting separate bookmark groups to operate and have independent “active” bookmarks.

For example, imagine you have two bookmark navigators, one which reflects the bookmark group you’ve made to filter a report page by country, and one which reflects the bookmark group you’ve made to filter by decade. Before, selecting a decade would clear the country selection, and vice versa, even if the filter being applied from the country selection is still active:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-33-1.jpg)

Now, however, both bookmarks (selected country and selected decade) will remain selected:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-45-1.jpg)

Note that you can still change the report state without selecting another bookmark to leave the state captured by that bookmark (_e.g._ by manually changing a filter away from Europe trends to US trends). Your bookmark navigators will still maintain their selection state.

Check back next week for more Power BI tips and tricks!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-bookmark-navigator/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-bookmark-navigator/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-bookmark-navigator/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-bookmark-navigator/#0)

[](https://sumproduct.com/blog/power-bi-blog-bookmark-navigator/#0 "close")

top