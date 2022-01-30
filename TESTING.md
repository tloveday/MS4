# Teifi Taekwondo

- [Teifi Taekwondo](#teifitkd)
  * [Testing](#testing)
    + [Manual Testing](#manual-testing)
    + [Compatibility and Responsiveness](#compatibility-and-responsiveness)
    + [Open Issues](#open-issues)

## Testing

I carried our substantial testing on all of my sites pages and links.

http://ami.responsivedesign.is/ has been used to see how the site performs on different Apple devices and their viewports, all links, icons performed as expected on all devices.
I also used it to create the AppleDevicesView.png at the top of this Readme.

### Manual Testing

- Google Chrome Browser; all feature links and icons perform well on all viewport sizes. Developer tools were also used on browser for the various viewport sizes. 
The webpages are responsive as are the images, info windows and forms, whilst retaining user friendly design aspects.
The images did not appear stretched or pixilated and remained sharp and clear throughout the site.


- Safari Browser; all feature links and icons perform well on all viewport sizes. Developer tools were also used on browser for the various viewport sizes. 
The webpages are responsive as are the images, info windows and forms, whilst retaining user friendly design aspects.
The images did not appear stretched or pixilated and remained sharp and clear throughout the site.


- Various browsers and devices; the project was shared with friends and associates, owners of independent shops with their own website, alongside those who practice and have children who practice martial arts 

> Note: The developer used dev tools to check the responsiveness of all the apps pages, using the dropdown burger menu, to click every page link. The 'Top' button was pressed on every page to test for the required action on smaller screen sizes, with the correct response given. 
        The images were viewed and buttons all pressed on various browser sizes in dev tools to check responsiveness, along with forms and the search bar. 
        All pages and their contents were fully responsive whilst maintaining user friendly design aspects.

* This is in direct relation to the 'Goals' and 'User Stories' from the 'UX' Section.

    The results of this were -

    1. Users can choose their own username and password.

    2. Users can find what they're looking for quickly and easily, using the navbar, search bar, categories and sort by dropdown.

    3. Links in the navbar are labelled clearly.
    
    4. Users can view a list of products and select some to purchase.

    5. Users can view a specific item details in a separate window.

    6. The app is easy to use and has easy to follow instructions, with user feedback when an action has been carried out using toasts messages.

    7. Users are notified if their inputs are successful and have been denied.

    8. Users can add, edit and delete inputs easily

    9. Users payment information is handled securely via stripe.

    10. Having the forms within the 'Edit' buttons autofill, saves user time and repetition.

    12. Some parts of the site are only accessible to super users.

    13. Users can purchase items quickly.

    14. Unregistered users can still purchase items.

    15. It's colourful and engaging.

    16. The site has been designed to be fluid and never to entrap the user.
    
    17. The 'Top' button takes users back to the top of the page ensuring they always have somewhere to go and don't feel trapped as they get to the bottom of the page.
    
* A super user and regular user were created to test the elements only accessible to superusers stays hidden to regular users.
* All buttons, forms and links were clicked and tested for responses, all form fields were filled out and responded as expected, all features were used and tested with appropriate responses given as a logged in user, superuser and unregistered user.
* All buttons were tested by the developer to check that they responded correctly and displayed the correct information.
* All links were tested by the developer to check they lead to the correct endpoints and gave the correct responses.
* All product categories were tested by the developer to check that it responded correctly and displayed the correct information.
* All forms were tested by the developer by filling them out using the wrong inputs to test validation and user feedback, which worked as expected. A red underline and text box appear alerting the user to the mistake.
* Edit forms were tested by changing the information and viewing those changes on their respective pages. Edit forms were also pre-filled with the current information as programmed.
* All 'Delete' buttons delete the appropriate information and take users back to the all products. 
* The back to top button takes the user to the top of the current page and has been tested and responded as expected on every page.
* Toasts give the user real time feedback on thier inputs and are visible with bold, clean text to grab the users attention. They show at the appropriate time and with the correct text in all circumstances.

_Landing Page_ -
* Clicking the links within the jumbotron on the image take users to the pages specified.
* Clicking the links within the shop dropdown take users to the product categories specified or the all products page if requested.

_Search Bar_ -
* The search bar was tested by entering information completely irrelevent to the site which showed the programmed message 'No Results Found!', and the item count read 0.
* The search bar in the header generates results based on user input. Results are listed underneath. Words relevent to the site were searched all returning the correct information.

_Login Page_ -
* The form fields have validation and were tested using correct and incorrect information with the expected responses given.
* Clicking the home button takes users to the main landing page.
* Clicking the login button takes the user to the sites main landing page, which has links to all other areas of the site, upon correct entry of their personal username and password, and the link to the 'Register' page transports the user to that page as expected.
* Clicking the forgot password button takes users through the process of setting a new password.

_Register Page_ -
* The form fields have validation and were tested using correct and incorrect information with the expected responses given.
* Clicking the back to login and sign in links take users back to the login page as stated and expected.
* Clicking the register button registers that user’s username and email address and sends the user an email asking them to validate their email address before directing them back to the login page.

_Products Pages - Via Shop Dropdown_ -
* All the links in the shop dropdown list take the user to the products within that category.
* The result of the user’s input is shown below with only the products in that category visible.
* The page has a header to remind users of the category they're searching in and an item count so they can see how many items are in that category, next to a link that directs them to the all products page.
The item count was tested by entering and removing products from the DB and updates accordingly.
* The sort by dropdown is available for users to sort the products within the chosen category, it was tested by clicking all the available sorting methods and observing the results, which were as expected.
* Both the product image and product name take the user to that specific items details page.


_Product Details_ -
* Show all the details with regards to the specific item.
* A category link takes users to that products category, where they will find other items to purchase within that category if there are any within the DB. It was tested by clicking on every available method and observing the results visible underneath.
* Users can use the amount - and + icons to select the amount of that product to add to the basket. This has been tested with every product and the amount specified here will be added to the users shopping basket.
* On selected items Users can use dropdown menu to select the size of that particular product to add to the basket, adding multiples of the same size if required by using the - and + icons mentioned previously. This has been tested with every product and the amount specified here will be added to the users shopping basket. 
* Superusers will find the Edit and Delete buttons here. They are not visible to non-superusers and were tested by creating a regular user.
* A continue shopping link directs users to the all products page whilst saving their current shopping basket.
* The add to basket button adds the specified amount of the specified product and it’s size (if applicable) to the users shopping basket. Users are notified of the success of this or if there's been an error.

_Edit Product Button_ -
* Only super users have access to this button (found on Product Details page), and it was tested by creating a regular user.
* Clicking the 'Edit' buttons take the user to a form with the fields filled out with the current information and the 'Edit' button within the forms changes the information within the DB, before taking the user back to that products’ details page.
* The form fields have validation and were tested using correct and incorrect information with the expected responses given.
* The current image section shows a thumbnail of the current image with the option to remove it (checkbox), select a new image from the computer’s files (select button) or add an image using the image url field.
All 3 methods were tested and gave appropriate responses.
* Clicking the 'Cancel' buttons take the user back to their respective details page without making changes as expected.
* Users are notified of the success of this or if there's been an error.

_Product Management_ -
* Only super users have access to this page (found in My Account dropdown), and it was tested by creating a regular user.
* Clicking the 'Add' buttons add the entered information to the DB before taking the user back to the product’s details page.
* The form fields have validation and were tested using correct and incorrect information with the expected responses given.
* Users can select a new image from the computers files via the select button or add an image using the image url field.
Both methods were tested and gave appropriate responses.
* Clicking the 'Cancel' buttons take the user back to thier respective details page without making changes as expected.
* Users are notified of the success of this or if there's been an error.

_My Account Dropdown_ -
* The 'My Account' dropdown, when logged in, shows relevant information dependant on if you're a non-superuser or superuser, with superusers getting the added management pages, alongside the profile and logout links.
This was tested using superuser and non-superuser credentials.
* Using the 'My Account' dropdown users will be taken to the pages stated, with a confirmation of input required before logging them out via the logout button. Pressing cancel at this point takes users to the main landing page.
* Unregistered users and users who aren't logged in will see login and register links. This was also tested using superuser and non-superuser credentials.

_Profile Page_ -
* The users username appears at the top as programmed with their email displayed underneath. This was tested using 3 users’ credentials with the correct information displayed every time.
* The profile page displays the user’s username and email address with a table of all their previous orders and current delivery information.
* Clicking the order numbers, within the order history table, directs users to a page with all the information relative to that order displayed. A reminder that the user is viewing an old order 
is also displayed, with a link which takes users back to the profile page.
* The current billing information section has fields that can be edited with updated information and saved using the update information button.
The information stored in this form will be automatically generated within the checkout form when a user is logged in and has been tested by changing the user’s information.
The form has validation with explicit instructions when it's incorrect and was tested with both correct and incorrect information with the expected results.
* This page is only accessible to a logged in user and was tested using a username that wasn't logged in.

_Basket Icon_ -
* The Basket icon in the navbar takes users to their shopping baskets, where they will find a list of all the items they've added to it alongside some important information. If the basket is empty
users will be faced with a comment expressing that and a link which directs them to the all products page. This was tested by clicking the empty basket and clicking the basket with items inside and viewing the results, which were as stated.
* Users who have items in their baskets will be faced with the option to update item amounts and remove items from their baskets. Both the + and - buttons update the number within the box field, and the update and delete buttons update the subtotal, basket total, delivery and grand total to reflect the changes.
If all the items are removed from the basket, users will be directed to a page stating that their basket is empty and a link which takes them to the all products page.
* Clicking the continue shopping link directs users to the all products page.
* Clicking the checkout button takes users to the checkout page where they find an order summary alongside an order form. 

_Checkout Page_ -
* All form fields work as intended and have validation that tells users if it's not been filled out correctly.
The form was tested using correct and incorrect information, and gave the expected results and validation instructions.
* Clicking the 'Save info to profile' box, saves just the main form sections users details to their profile page, which can be accessed via the 'My Account' dropdown. If the user has information saved to their profile, the delivery form fields will
be automatically generated with the stored info. Any information changes made on this form update the info on the profile page when the save info box is checked.
This was tested by changing the information and observing the results on both pages.
* Clicking the basket link takes users back to their basket.
* Clicking the checkout button generates the payment through stripe, adding the order to the admin section of the site and the users profile page. This was tested using multiple users and making orders then viewing the results, which were as expected. 
* The 'warning card is about to be debited' message updates with the basket user entries such as updating the quantity of items and was tested by doing so.
*Users are informed that their items will be available for collection from the instructor at their next class. 


_Thankyou_ -
* When users have checked out and paid, they are directed to a thankyou page with a copy of their order and a link which directs the to the all recipes page.
Users are also sent a copy of their order to the email they supplied in the form on the checkout page. This has been tested multiple times, giving correct responses every time.
Users are notified of the email on the thankyou page alongside the email address.
*Users are informed that their items will be available for collection from the instructor at their next class. 

### Compatibility and Responsiveness

The device emulator by Google Chrome's developer tool was used to check the responsiveness across all the different screen sizes and devices to ensure compatibility and responsiveness to a screen minimum of 300. 
The images were viewed and buttons all pressed on various browser sizes to check responsiveness, along with forms and the search bar. The 'Top' button was pressed on every page to test for the required action on smaller screen sizes, with the correct response given
and the dropdown burger menu was used, to click every page link. 
All pages and their contents were fully responsive whilst maintaining user friendly design aspects.
This website has been tested on multiple browsers (Chrome, Safari, Firefox).
IPhone 12 (iOS 15.3) was used to test for mobile testing.
Ipad mini 5th Generation (iOS 15.3) and Ipad Pro (iOS 15.3) are used for medium screen testing.

### Open Issues

* When logging in users are taken back to the home page.

* When editing, adding and deleting products in some views the shopping basket appears in the success message toast if the basket isn't empty.

* Occasionally the webhook will duplicate orders if there's a time delay on my order form. This is a time sensitive issue and unfortunately, I didn't have the time to implement other features from stripe to overcome this.

** Back to [README.md](./README.md) **