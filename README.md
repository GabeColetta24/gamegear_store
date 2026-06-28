# GameGear Store

## Overview

GameGear Store is a full-stack e-commerce web application built using Django. The website allows users to browse gaming accessories, view individual product details, add products to a shopping cart, and complete purchases using Stripe test payments.

The project was developed as part of the Code Institute Portfolio Project 5 assessment for the E-commerce Applications module. The application focuses on creating a responsive and user-friendly online shopping experience while demonstrating full-stack development skills, database management, user authentication, and payment integration.

The site includes features such as:

- Product listings and detail pages
- Shopping cart functionality
- Remove from cart functionality
- Secure checkout process
- Stripe payment integration
- User registration and login system
- Newsletter signup form
- Django admin panel for product, order, newsletter, and user management
- SEO features including sitemap.xml and robots.txt
- Custom 404 error page
- Responsive design for mobile and desktop devices
- Product review functionality with create, read, update and delete options
- Wishlist functionality for logged-in users
- Logged-in user status shown in the navigation bar

### Live Website

[GameGear Store Live Site](https://gamegear-store-gabe-abcc86b4605d.herokuapp.com/)

### Repository

[GitHub Repository](https://github.com/GabeColetta24/gamegear_store)


## Design

### Design Goals

The design goal for GameGear Store was to create a clean, simple, and easy-to-use e-commerce website for users interested in gaming accessories. The site was designed to make the shopping process clear and straightforward, allowing users to browse products, view product details, add items to their cart, and complete checkout without confusion.

The project uses a simple layout with clear navigation, styled product cards, consistent buttons, and readable content. The aim was to keep the design professional without making the interface overly complicated.

### User Experience

The user experience was planned around making the main actions easy to find and complete. Users can access the homepage, cart, newsletter signup, login, and registration pages from the navigation bar. Product cards provide a clear overview of each item, while individual product pages give more detailed information along with an Add to Cart button.

The checkout process was designed to be simple, with an order summary, user details form, Stripe test payment page, and final order success confirmation.

### Colour Scheme

The colour scheme uses a dark navigation bar with a light grey page background and white content cards. Blue buttons are used for key actions such as viewing products, adding items to the cart, continuing shopping, and submitting forms. This creates a clear visual contrast between navigation, content, and user actions.

### Typography

The site uses Arial as the main font. This was chosen because it is simple, readable, and widely supported across browsers and devices.

### Layout

The layout uses a centered main content area with card-style sections. Product listings, cart items, forms, and confirmation pages are displayed using consistent spacing, padding, and shadows to create a clean structure across the website.

### Responsive Design

The site was designed to remain usable on both desktop and mobile screen sizes. The main content area adapts to smaller screens, and the navigation links remain accessible. Product cards stack vertically, making the site easy to browse on mobile devices.


## Agile Development

GitHub Projects was used to manage the planning and development process for the GameGear Store application.

User stories were organised into:
- To Do
- In Progress
- Done

The board was used to track completed functionality and future improvements throughout development.

![Agile Board](static/images/agile-board.png)


## Features

### Navigation Bar

The navigation bar is displayed across all pages of the website and allows users to easily navigate between the homepage, shopping cart, newsletter signup page, login page, and registration page.

Users who are logged in are shown a logout link, while logged out users are shown login and register links.

#### Logged Out Navigation

![Logged Out Navigation](static/images/login-navbar.png)

#### Logged In Navigation

![Logged In Navigation](static/images/logout-navbar.png)

---

### Homepage

The homepage displays all available gaming products using styled product cards. Each product includes an image, description, price, and a link to view more details.

![Homepage](static/images/homepage.png)

---

### Product Detail Pages

Each product has its own detail page containing a larger image, product description, price, add to cart button, and a link back to the homepage.

![Product Detail Page](static/images/product-detail.png)

---

### Shopping Cart

Users can add products to their cart, view selected items, see totals, remove products from the cart, and continue to checkout.

![Cart Page](static/images/cart.png)

---

### Checkout System

The checkout page allows users to enter their details and review their order before completing payment.

![Checkout Page](static/images/checkout.png)

---

### Stripe Payments

Stripe test payments were integrated to simulate a real e-commerce checkout experience.

![Stripe Payment](static/images/stripe-payment.png)

---

### Order Success Page

After a successful payment, users are redirected to an order confirmation page displaying their order details and confirmation message.

![Order Success Page](static/images/order-success.png)

---

### User Authentication

Users can register for an account, log in, and log out securely using Django authentication.

#### Register Page

![Register Page](static/images/register-page.png)

#### Login Page

![Login Page](static/images/login-page.png)

---

### Product Reviews

Logged-in users can leave reviews on products by providing a rating and written feedback. Reviews are displayed on the relevant product page so that other customers can read them before making a purchase.

Users can also edit or delete their own reviews, providing full frontend CRUD (Create, Read, Update and Delete) functionality while preventing users from modifying reviews created by others.

![Product Reviews](static/images/product-reviews.png)

---

### Wishlist

Registered users can save products to a personal wishlist for future viewing. This provides users with a convenient way to keep track of products they are interested in purchasing.

Products can be added directly from the product detail page and removed from the wishlist at any time. Wishlist functionality is only available to authenticated users, providing an additional benefit for creating an account.

![Wishlist](static/images/wishlist.png)

---

### Newsletter Signup

Users can subscribe to the newsletter using a simple signup form. Newsletter signups are stored and manageable through the Django admin panel.

![Newsletter Signup](static/images/newsletter-page.png)

---

### Django Admin Panel

The Django admin panel allows administrators to manage products, customer orders, order items, newsletter signups, and registered users through the built-in Django administration system.

#### Admin Dashboard

![Admin Dashboard](static/images/admin-panel.png)

#### Product Management

![Admin Products](static/images/admin-products.png)

#### Order Management

![Admin Orders](static/images/admin-order.png)

#### Order Item Management

![Admin Order Items](static/images/admin-order-items.png)

#### Newsletter Management

![Admin Newsletter](static/images/admin-newsletter.png)

#### Review Management

Administrators can view and manage all product reviews through the Django admin panel.

![Admin Reviews](static/images/admin-reviews.png)

---

#### Wishlist Management

Administrators can view wishlist entries created by registered users through the Django admin panel.

![Admin Wishlist](static/images/admin-wishlist.png)

---

### Custom 404 Page

A custom 404 page was created to improve user experience when visiting invalid URLs.

![404 Page](static/images/custom-404.png)

---

### SEO Features

The project includes both a `sitemap.xml` file and a `robots.txt` file to improve search engine indexing and SEO structure.

#### sitemap.xml

![Sitemap](static/images/sitemap.png)

#### robots.txt

![Robots](static/images/robots.png)

---

### Responsive Design

The website layout adapts to mobile screen sizes to ensure usability across devices.

![Mobile Responsive Homepage](static/images/mobile-homepage.png)


## Future Features

Several additional features could be added in future development updates:

- Product categories and filtering system
- Product search functionality
- User profile pages with order history
- Quantity update buttons directly inside the cart
- Product stock management system
- Real Stripe live payment integration
- Email confirmation for orders and newsletter subscriptions
- Improved mobile navigation menu
- Additional gaming products and product images


## Marketing Strategy

### Facebook Business Page Mockup

A Facebook business page mockup was created to support the marketing strategy for GameGear Store.

![Facebook Mockup](static/images/facebook-mockup.png)

The Facebook page is designed to:
- Increase brand awareness
- Promote gaming products and special offers
- Drive traffic to the website
- Engage with potential customers
- Support long-term customer growth


## E-commerce Business Model

GameGear Store follows a **Business-to-Consumer (B2C)** e-commerce model. The website is designed to allow customers to browse gaming accessories, add products to a shopping cart, and complete purchases through a secure Stripe payment system.

The application demonstrates the key functionality expected from a modern e-commerce website by allowing users to:

- Browse available products.
- View detailed product information.
- Add products to a shopping cart.
- Complete secure online payments using Stripe.
- Register and log into an account.
- Save products to a personal wishlist.
- Create, edit and delete product reviews.

The site owner manages products, customer orders, newsletter subscriptions, reviews, and wishlist data through the Django administration panel. This allows products and customer data to be managed efficiently while providing customers with a simple and user-friendly shopping experience.

## Database Schema

The GameGear Store application uses a relational database to manage products, customer orders, reviews, wishlist items, newsletter subscriptions, and user accounts.

The main database models are:

- **Product** – Stores product information including name, description, price, image, and availability.
- **Order** – Stores customer order details including delivery information and total cost.
- **OrderItem** – Stores individual products that belong to an order.
- **Review** – Stores product reviews created by registered users.
- **WishlistItem** – Stores products saved to a user's wishlist.
- **NewsletterSignup** – Stores email addresses submitted through the newsletter signup form.
- **User** – Django's built-in authentication model used to manage user accounts and link orders, reviews, and wishlist items.

The Entity Relationship Diagram (ERD) below illustrates the relationships between the application's database models.

![Entity Relationship Diagram](static/images/erd.png)

## Technologies Used

### Languages

- Python
- HTML5
- CSS3

### Frameworks and Libraries

- Django
- Gunicorn
- Psycopg2
- Stripe
- Whitenoise

### Database

- SQLite (development)
- PostgreSQL (production via Heroku)

### Deployment

- Git
- GitHub
- Heroku
- VS Code


## Testing

### Manual Testing

Manual testing was carried out throughout development to ensure that all features worked correctly across the website.

| Feature | Expected Outcome | Testing Performed | Result |
|---|---|---|---|
| Navigation links | Links navigate to correct pages | Clicked all navigation links across the site | Pass |
| Homepage products | Products display correctly with images and details | Loaded homepage and checked all product cards | Pass |
| Product detail pages | Product details display correctly | Opened individual product pages | Pass |
| Add to cart | Products added to shopping cart | Added multiple products to cart | Pass |
| Remove from cart | Products removed from shopping cart | Removed products from cart page | Pass |
| Cart totals | Cart totals calculate correctly | Added and removed products while checking totals | Pass |
| Checkout form | Users can enter checkout details | Submitted checkout form with test details | Pass |
| Stripe payments | Test payment processes successfully | Used Stripe test card payment | Pass |
| Order success page | Confirmation page displays after payment | Completed successful checkout | Pass |
| User registration | Users can create accounts | Registered new user account | Pass |
| User login/logout | Users can log in and out successfully | Tested login and logout functionality | Pass |
| Newsletter signup | Users can subscribe successfully | Submitted newsletter signup form | Pass |
| Admin panel access | Admin users can access Django admin | Logged into admin panel | Pass |
| Product management | Products can be managed through admin panel | Added and viewed products in admin | Pass |
| Order management | Orders display in admin panel | Checked completed orders in admin | Pass |
| Newsletter management | Newsletter signups display in admin | Checked newsletter signups in admin | Pass |
| Custom 404 page | Custom error page displays correctly | Visited invalid URL on deployed site | Pass |
| sitemap.xml | Sitemap loads correctly | Opened sitemap.xml page | Pass |
| robots.txt | robots.txt loads correctly | Opened robots.txt page | Pass |
| Mobile responsiveness | Layout adapts to mobile devices | Tested site using Chrome DevTools mobile view | Pass |
| Product reviews | Logged-in users can create reviews | Created a review on a product page | Pass |
| Edit review | Users can edit their own reviews | Edited an existing review | Pass |
| Delete review | Users can delete their own reviews | Deleted an existing review | Pass |
| Add to wishlist | Logged-in users can save products | Added a product to the wishlist | Pass |
| Remove from wishlist | Users can remove saved products | Removed a product from the wishlist | Pass |
| Logged-in user display | Username displays correctly in the navigation bar | Logged in and confirmed username appeared in the navigation bar | Pass |

---

### Validator Testing

### HTML Validator

HTML pages were tested using the [W3C HTML Validator](https://validator.w3.org/).

No major errors were found during testing.

### CSS Validator

CSS files were tested using the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).

No errors were found during validation.

### Python Validator

Python files were tested using the [Code Institute Python Linter](https://pep8ci.herokuapp.com/).

No functional errors were found. Any remaining warnings relate to code style, such as line length or formatting, and do not affect the operation of the application.

---

### Browser Testing

The website was tested successfully on the following browsers:

- Google Chrome
- Safari

---

### Device Testing

The website was tested on:

- MacBook Pro
- iPhone
- Mobile responsive view using Chrome Developer Tools

---

### Fixed Bugs

| Bug | Fix |
|---|---|
| Cart page styling did not match the rest of the website | Added consistent styling and reusable card/button classes |
| Order success page styling was inconsistent | Updated layout and styling to match the website design |
| Navbar links displayed incorrectly depending on login state | Updated authentication navigation logic |
| Users could not remove products from the cart | Added remove from cart functionality |
| Static files were not displaying correctly on deployment | Updated static file and Heroku configuration |
| Custom 404 page was not displaying correctly | Added and styled a custom 404 template |
| Product reviews were not available | Added full frontend CRUD functionality for authenticated users to create, edit and delete product reviews |
| Wishlist functionality was missing | Implemented a wishlist system allowing authenticated users to save and remove products |
| Search engine optimisation was incomplete | Added a sitemap, robots.txt and improved meta descriptions |
| Logged-in users had no visual account indicator | Added the logged-in username to the navigation bar |
| Logged-in users could access the registration page | Redirected authenticated users away from the registration page |

---

### Remaining Bugs

No known major bugs remain at the time of submission.

## Deployment

### Local Deployment

To clone this project locally:

1. Open GitHub and locate the repository.
2. Click the green **Code** button.
3. Copy the repository URL.
4. Open a terminal and navigate to the desired folder location.
5. Run the following command:

```bash
git clone https://github.com/GabeColetta24/gamegear_store.git
```

6. Open the project in your chosen code editor.
7. Create and activate a virtual environment.
8. Install the required dependencies:

```bash
pip install -r requirements.txt
```

9. Apply migrations:

```bash
python manage.py migrate
```

10. Run the development server:

```bash
python manage.py runserver
```

---

### Heroku Deployment

The project was deployed using Heroku.

Steps used for deployment:

1. Create a Heroku account and log in.
2. Create a new Heroku app.
3. Add the Heroku Postgres add-on.
4. Set the required config variables in Heroku:
   - SECRET_KEY
   - DATABASE_URL
   - STRIPE_PUBLIC_KEY
   - STRIPE_SECRET_KEY
   - DEBUG
5. Add `gunicorn`, `psycopg2`, and `whitenoise` to the project requirements.
6. Create a `Procfile` containing:

```bash
web: gunicorn gamegear_store.wsgi
```

7. Push the project to GitHub.
8. Connect the Heroku app to the GitHub repository.
9. Deploy the main branch through Heroku.
10. Open the deployed application to confirm successful deployment.


## Credits

### Media

- Product images were sourced from Google Images and used for educational purposes only.

### Code

- Django documentation was used throughout development, including authentication, models, forms and views:
  https://docs.djangoproject.com/

- Stripe documentation was used for payment integration:
  https://stripe.com/docs

- Code Institute learning materials and walkthrough content were used for guidance during development.