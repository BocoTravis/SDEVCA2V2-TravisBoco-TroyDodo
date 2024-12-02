# Project Name: CA2 Django E commerce: Numero Uno
# Members
Name: Troy Dodo
ID: X00212938
Name: Travis Boco
ID: x00209463

# Overview
This is an e-commerce web application built using Django, featuring user authentication, product management, use of UUID, static images and assets, image uploads, search functionality, Django session framework, and a shopping cart that can create orders, finalize payment, and also empty the cart.

# Features
-User Registration, Login, Logout
-Product Listings
-Making orders
-Shopping Cart and Checkout (Stripe Functionality)
-Voucher Codes
-Search Functionality
-CSS Styling
-Use of UUID
-Static image uploads and assets
-E commerce features such as sales

# Contributions
-Travis
--Set up the Django project structure and configured settings.py, including static and media file handling.
--Created models for accounts (e.g., CustomUser) Order(e.g.,OrderItem) and Cart (e.g., Cart, CartItem).
--Developed views for user authentication (e.g., login, signup) and cart-related logic.
--Designed and implemented templates for the accounts and cart apps, including dynamic navbar and footer elements.
--Tested functionality for accounts ,order and cart, ensuring smooth operations.
--Prepared the requirements.txt file.

-Troy
--Configured urls.py for the main project and apps, ensuring proper routing.
Created models for the shop app (e.g., Product, Category) and implemented voucher-related models and logic.
--Devloped Search app
--Developed views for product listing, product detail pages, and voucher application.
--Designed and implemented templates for the shop and voucher pages, including product styling and checkout layouts.
--Tested functionality for shop and voucher apps, including the application of voucher codes.
--Designed the logo for the Website

We both made sure to add products that we thought were appropriate for the shop.
We both peer-reviewed each other’s code to ensure quality and fix bugs.
Prepared and presented the project collaboratively.


# References
Throughout this project, we extensively utilised the labs to help us get our site running. Specifically:

Lab 10: Used as a base template to kickstart the project structure and logic.
Lab 6: Adapted for the custom user model and custom user authentication.
Lab 5: Referenced for CRUD functionality.
Additionally, for product sales features, we used the following external resource:

[ https://www.youtube.com/watch?v=w7pnR408jVU&list=PLCC34OHNcOtpRfBYk-8y0GMO4i1p1zn50&index=5]
: The sale_price and _on_sale model logic and the sales badge implementation were adapted from this resource.

For CSS, we borrowed ideas from our client-side labs, particularly:

Styling for product cards, hover effects, and consistent sizing.
Implementing a .product-card:hover effect to visually indicate when an item is hovered.

##External Libraries Used
--Django: Python web framework.
--Bootstrap: Front-end framework for styling.
--Pillow: For image handling.
--Stripe:Handeling the payements
