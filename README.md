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
- Product reviews and ratings
- Real Stripe live payment integration
- Email confirmation for orders and newsletter subscriptions
- Improved mobile navigation menu
- Additional gaming products and product images