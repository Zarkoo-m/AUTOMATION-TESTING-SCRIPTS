📦 Automated E-Commerce Testing with Selenium

    End-to-End Automation for Appliance Shopping – Featuring Cross-Browser Testing, GraphQL Validation & Console Log Monitoring
_______________________________________________________________________________________________________________________________
📌 MAIN DESCRIPTION
_______________________________________________________________________________________________________________________________
✅ OBJECT-ORIENTED FUNCTIONS
    🔹Each field has a separate object-oriented function, ensuring modularity, code reusability, and maintainability.

✅ MODULAR DESIGN
    🔹The script is modular, making it easy to maintain, structured, and flexible for creating test scenarios.

✅ FOLDER SEPARATION
    🔹Functions and fields are well-organized in separate files, categorized into folders based on software sections for clear navigation.
_______________________________________________________________________________________________________________________________
📚 LIBRARIES & DEPENDENCIES
_______________________________________________________________________________________________________________________________
🔹 Built-in Python Libraries
✔️ os – File and directory operations
✔️ json – Handling JSON data structures
✔️ csv – Working with CSV files
✔️ datetime – Date and time manipulation
✔️ time – Execution time measurement & delays
✔️ inspect – Object and function introspection
✔️ re – Regular expression processing
✔️ string – String manipulation utilities
✔️ random – Random number and data generation
✔️ collections.OrderedDict – Maintaining order of dictionary keys
✔️ ActionChains – Automating complex interactions in Selenium

🔹 Selenium Modules
✔️ By – Element locators (By.ID, By.XPATH, By.CLASS_NAME, etc.)
✔️ WebDriverWait – Explicit waits for better element handling
✔️ EC (Expected Conditions) – Wait conditions like EC.presence_of_element_located()
✔️ Exceptions – Selenium-specific error handling
✔️ Selenium-Wire – Capturing and intercepting network requests
_______________________________________________________________________________________________________________________________
⚙️ MAIN FEATURES
_______________________________________________________________________________________________________________________________
✅ TRY-EXCEPT BLOCKS
    🔹Ensures robust error handling, preventing script crashes and allowing debugging.

✅ PRINT STATEMENTS
    🔹Clearly defined console outputs for better tracking, debugging, and understanding script execution flow.

✅ WAIT DRIVER AND TIME MANAGEMENT
    🔹Explicit and implicit waits ensure elements load before interacting, improving stability and reliability.

✅ CONFIRMATIONS
    🔹Each step is validated with backend confirmations to verify proper execution.

✅ LOGGING SYSTEM
    🔹Captures and logs important events, errors, and execution details for debugging and reporting.

✅ ERROR HANDLING
    🔹Custom exception handling ensures smooth execution and clear debugging messages.
    🔹In case of an error, the system not only logs the error message but also returns the HTML code of the problematic field.

✅ GRAPHQL AND QUERY INTERCEPTION
    🔹Intercepts backend API calls to validate queries, mutations, and data consistency.

✅ POST REQUEST & STATUS CODE VALIDATION
    🔹Verifies server responses for expected status codes after performing actions.

✅ VALUE STORAGE
    🔹Saves input values and HTML elements for comparison with backend data and debugging purposes.

✅ CONSOLE LOG CAPTURING
    🔹Intercepts browser console logs, including errors, warnings, and JavaScript objects.

✅ SCREENSHOT CAPTURE
    🔹Takes screenshots after each step for visual validation and debugging.

✅ TIMER MEASUREMENT
    🔹Tracks execution time per step and calculates the total script execution duration.

✅ GENERAL REPORTING
    🔹Generates a detailed summary of:

    🔹Total number of actions and validations (success/failure).
    🔹Total screenshots captured.
    🔹Logged errors, data, and stored HTML.

✅ BACKEND CHECKER
    🔹Compares input values with GraphQL or API responses for backend validation.

✅ HEADLESS MODE
    🔹Runs the script in a headless browser for improved speed and automation without UI rendering.

✅ CROSS-BROWSER TESTING
    🔹Supports Google Chrome, Mozilla Firefox, and Microsoft Edge for browser compatibility testing.

✅ CACHE CLEANUP
    🔹Cleans stored browser cache and cookies for a fresh test environment on each run.
_______________________________________________________________________________________________________________________________
🛠 HOW IT WORKS
_______________________________________________________________________________________________________________________________
🔹 End-to-End Test Flow
1️⃣ User Login – Authenticate with email
2️⃣ Product Selection – Choose category, brand, and model
3️⃣ Order Customization – Configure power source, energy rating, and quantity
4️⃣ Shipping & Delivery – Enter shipping address and schedule delivery
5️⃣ Payment & Discounts – Apply promo codes and choose payment methods
6️⃣ Finalizing Order – Confirm order details and track shipment
7️⃣ Backend Validation – Compare GraphQL API responses with UI data
8️⃣ Console Log Analysis – Capture browser errors for debugging
9️⃣ Reporting & Data Storage – Save execution logs, screenshots, and API comparisons
_______________________________________________________________________________________________________________________________
📂 PROJECT STRUCTURE
_______________________________________________________________________________________________________________________________
📁 APPLIANCE_SHOP
│── 📁 A_USER_AUTH                                                                       # User authentication & login
│   ├── A_1_CUSTOMER_LOGIN.py
│
│── 📁 B_DASHBOARD                                                                        # Dashboard operations
│   ├── B_1_ADD_NEW_APPLIANCE.py
│   ├── B_2_START_NEW_PURCHASE.py
│
│── 📁 C_SHOPPING_PROCESS                                                                 # Shopping process (category, brand, quantity)
│   ├── C_1_CHOOSE_APPLIANCE_CATEGORY.py
│   ├── C_2_SELECT_BRAND_MODEL.py
│   ├── C_3_QUANTITY_SELECTION.py
│
│── 📁 D_PRODUCT_DETAILS                                                                   # Product details & customization
│   ├── 📁 A_APPLIANCE_INFO                                                                # Appliance information
│   │   ├── A_1_SELECT_APPLIANCE_TYPE.py
│   │   ├── A_2_PRODUCT_USAGE_TYPE.py
│   │   ├── A_3_MANUAL_ENTRY_OF_DETAILS.py
│   │   ├── A_4_BRAND_SELECTION.py
│   │   ├── A_5_MODEL_SELECTION.py
│   │   ├── A_6_POWER_SOURCE.py
│   │   ├── A_7_SERIAL_NUMBER_VALIDATION.py
│   │   ├── A_8_APPLIANCE_PRICE_DETAILS.py
│   │   ├── A_9_RETAIL_STORE_DETAILS.py
│   │   ├── A_10_YEAR_OF_PRODUCTION.py
│   │   ├── A_11_APPLIANCE_CATEGORY.py
│   │   ├── A_12_ENERGY_RATING.py
│   │   ├── A_13_WAREHOUSE_LOCATION.py
│   ├── 📁 B_ADDITIONAL_DETAILS                                                              # Extended warranties & support
│   │   ├── B_1_WARRANTY_AND_SUPPORT.py
│   │   ├── B_2_INSURANCE_COVERAGE.py
│   │   ├── B_3_EXTENDED_WARRANTY_OPTIONS.py
│   ├── 📁 C_PAYMENT_OPTIONS                                                                 # Payment methods & discounts
│   │   ├── C_1_INSTALLMENT_PLANS_AVAILABLE.py
│   │   ├── C_2_DISCOUNT_AND_PROMO_CODES.py
│   │   ├── C_3_SECURE_PAYMENT_METHODS.py
│   ├── 📁 D_CUSTOMER_DETAILS                                                                # Customer information
│   │   ├── D_1_CUSTOMER_FULL_NAME.py
│   │   ├── D_2_CONTACT_PHONE_NUMBER.py
│   │   ├── D_3_CUSTOMER_EMAIL_ADDRESS.py
│   ├── 📁 E_SHIPPING_AND_DELIVERY                                                            # Shipping details
│   │   ├── E_1_CUSTOMER_SHIPPING_ADDRESS.py
│   │   ├── E_2_DELIVERY_DATE_AND_TIME.py
│   │   ├── E_3_ORDER_TRACKING_INFORMATION.py
│   ├── 📁 F_ORDER_SUMMARY                                                                    # Order confirmation
│   │   ├── F_1_ORDER_CONFIRMATION_AND_TOTAL.py
│   ├── 📁 G_NEXT_STEP                                                                        # Next steps after order placement
│   │   ├── G_1_SEND_ORDER_CONFIRMATION_EMAIL.py
│   │   ├── G_2_CONTINUE_SHOPPING_OR_CHECKOUT.py
│   ├── 📁 H_PRODUCT_OFFERS                                                                   # Special offers
│   │   ├── H_1_SELECT_OFFER.py
│   ├── 📁 I_CUSTOMER_INFO                                                                    # Personal details
│   │   ├── I_1_PERSON_FOR_DELIVERY.py
│   │   ├── I_2_TITLE.py
│   │   ├── I_3_FIRST_NAME.py
│   │   ├── I_4_LAST_NAME.py
│   │   ├── I_5_PHONE_NUMBER.py
│   │   ├── I_6_EMAIL_ADDRESS.py
│   ├── 📁 J_PURCHASE_SUMMARY                                                                  # Final purchase confirmation
│   │   ├── J_1_FINALIZE_PURCHASE.py
│   ├── 📁 K_ORDER_PROCESSING                                                                  # Order submission & tracking
│       ├── K_1_SEND_TO_CUSTOMER.py
│
│── 📁 SUPPORTING_FILES                                                                        # Utility & helper files
│   ├── 📁 A_DRIVERS                                                                           # WebDriver setup
│   │   ├── A_DRIVER_SETUP.py
│   ├── 📁 B_LOGS                                                                              # Logging system
│   │   ├── B_LOGGING_CONFIG.py
│   ├── 📁 C_UTILITIES                                                                         # General utilities & data processing
│   │   ├── A_1_Status_Code.py
│   │   ├── A_2_GraphQL.py
│   │   ├── A_3_Query.py
│   │   ├── A_4_Console_log.py
│   │   ├── A_5_Data_Collector.py
│   │   ├── A_6_Screenshots.py
│   │   ├── A_7_Statistics.py
│   │   ├── A_8_Input_Validation.py
│   │   ├── A_9_Exception_Handler.py
│   │   ├── A_10_Compare_Data.py
│   │   ├── A_12_Clear_cache_memory.py
│   ├── 📁 D_REUSABLE                                                                           # Reusable functions & components
│       ├── D_1_CONTINUE_TO_CHECKOUT.py
│       ├── D_2_NEXT_STEP_IN_ORDER_PROCESS.py
│
│── 🖥️ Main.py                                                                                   # Execution script

_______________________________________________________________________________________________________________________________

⚠️ Note: This code is an example (Showcase) of automation, and it contains the structure and other elements from the actual project. 
   However, sensitive details have been removed for security reasons and to respect the confidentiality agreement with the client for whom this project was developed. 
   It does not contain real business data or actual API structures. All names, URLs, and data have been modified for security reasons.