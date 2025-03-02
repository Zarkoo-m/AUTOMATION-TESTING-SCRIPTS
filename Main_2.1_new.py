#SUPPORTING FILES IMPORTS

from SUPPORTING_FILES. A_DRIVERS. A_DRIVER_SETUP import setup_driver
from SUPPORTING_FILES.B_LOGS.B_LOGGIN_CONFIG import logger
#----------------------------------------------------------------
# LOGIN FORM IMPORTS
from A_USER_AUTH.A_1_CUSTOMER_LOGIN import EmailFormPage
#----------------------------------------------------------------
# DASHBOARD IMPORTS
from B_DASHBOARD.B_1_ADD_NEW_APPLIANCE import AddNewAppliance
from B_DASHBOARD.B_2_START_NEW_PURCHASE import StartNewPurchaseButton
#----------------------------------------------------------------
# SHOPPING PROCESS IMPORTS
from C_SHOPPING_PROCESS.C_1_CHOOSE_APPLIANCE_CATEGORY import SelectProductCategory
from C_SHOPPING_PROCESS.C_2_SELECT_BRAND_MODEL import SelectBrandModel
from C_SHOPPING_PROCESS.C_3_QUANTITY_SELECTION import QuantitySelection
#----------------------------------------------------------------
# PRODUCT DETAILS IMPORTS
from D_PRODUCT_DETAILS.A_APPLIANCE_INFO.A_1_SELECT_APPLIANCE_TYPE import SelectApplianceType
from D_PRODUCT_DETAILS.A_APPLIANCE_INFO.A_2_PRODUCT_USAGE_TYPE import ProductUsageType
from D_PRODUCT_DETAILS.A_APPLIANCE_INFO.A_3_MANUAL_ENTRY_OF_DETAILS import ManualEntryOfDetails
from D_PRODUCT_DETAILS.A_APPLIANCE_INFO.A_4_BRAND_SELECTION import BrandSelection
from D_PRODUCT_DETAILS.A_APPLIANCE_INFO.A_5_MODEL_SELECTION import ModelSelection
from D_PRODUCT_DETAILS.A_APPLIANCE_INFO.A_6_POWER_SOURCE import PowerSource
from D_PRODUCT_DETAILS.A_APPLIANCE_INFO.A_7_SERIAL_NUMBER_VALIDATION import SerialNumberValidation
from D_PRODUCT_DETAILS.A_APPLIANCE_INFO.A_8_APPLIANCE_PRICE_DETAILS import AppliancePriceDetails
from D_PRODUCT_DETAILS.A_APPLIANCE_INFO.A_9_RETAIL_STORE_DETAILS import RetailStoreDetails
from D_PRODUCT_DETAILS.A_APPLIANCE_INFO.A_10_YEAR_OF_PRODUCTION import YearOfProduction
from D_PRODUCT_DETAILS.A_APPLIANCE_INFO.A_11_APPLIANCE_CATEGORY import ApplianceCategory
from D_PRODUCT_DETAILS.A_APPLIANCE_INFO.A_12_ENERGY_RATING import EnergyRating
from D_PRODUCT_DETAILS.A_APPLIANCE_INFO.A_13_WAREHOUSE_LOCATION import WarehouseLocation
#----------------------------------------------------------------
# ADDITIONAL DETAILS IMPORTS
from D_PRODUCT_DETAILS.B_ADDITIONAL_DETAILS.B_1_WARRANTY_AND_SUPPORT import WarrantyAndSupport
from D_PRODUCT_DETAILS.B_ADDITIONAL_DETAILS.B_2_INSURANCE_COVERAGE import InsuranceCoverage
from D_PRODUCT_DETAILS.B_ADDITIONAL_DETAILS.B_3_EXTENDED_WARRANTY_OPTIONS import ExtendedWarrantyOptions
#----------------------------------------------------------------
# PAYMENT OPTIONS IMPORTS
from D_PRODUCT_DETAILS.C_PAYMENT_OPTIONS.C_1_INSTALLMENT_PLANS_AVAILABLE import InstallmentPlansAvailable
from D_PRODUCT_DETAILS.C_PAYMENT_OPTIONS.C_2_DISCOUNT_AND_PROMO_CODES import DiscountAndPromoCodes
from D_PRODUCT_DETAILS.C_PAYMENT_OPTIONS.C_3_SECURE_PAYMENT_METHODS import SecurePaymentMethods
#----------------------------------------------------------------
# CUSTOMER DETAILS IMPORTS
from D_PRODUCT_DETAILS.D_CUSTOMER_DETAILS.D_1_CUSTOMER_FULL_NAME import CustomerFullName
from D_PRODUCT_DETAILS.D_CUSTOMER_DETAILS.D_2_CONTACT_PHONE_NUMBER import ContactPhoneNumber
from D_PRODUCT_DETAILS.D_CUSTOMER_DETAILS.D_3_CUSTOMER_EMAIL_ADDRESS import CustomerEmailAddress
#----------------------------------------------------------------
# SHIPPING AND DELIVERY IMPORTS
from D_PRODUCT_DETAILS.E_SHIPPING_AND_DELIVERY.E_1_CUSTOMER_SHIPPING_ADDRESS import CustomerShippingAddress
from D_PRODUCT_DETAILS.E_SHIPPING_AND_DELIVERY.E_2_DELIVERY_DATE_AND_TIME import DeliveryDateAndTime
from D_PRODUCT_DETAILS.E_SHIPPING_AND_DELIVERY.E_3_ORDER_TRACKING_INFORMATION import OrderTrackingInformation
#----------------------------------------------------------------
# ORDER SUMMARY IMPORTS
from D_PRODUCT_DETAILS.F_ORDER_SUMMARY.F_1_ORDER_CONFIRMATION_AND_TOTAL import OrderConfirmationAndTotal
#----------------------------------------------------------------
# NEXT STEP IMPORTS
from D_PRODUCT_DETAILS.G_NEXT_STEP.G_1_SEND_ORDER_CONFIRMATION_EMAIL import SendOrderConfirmationEmail
from D_PRODUCT_DETAILS.G_NEXT_STEP.G_2_CONTINUE_SHOPPING_OR_CHECKOUT import ContinueShoppingOrCheckout
#----------------------------------------------------------------
# PRODUCT OFFERS IMPORTS
from D_PRODUCT_DETAILS.H_PRODUCT_OFFERS.H_1_SELECT_OFFER import SelectOffer
#----------------------------------------------------------------
# CUSTOMER INFO IMPORTS
from D_PRODUCT_DETAILS.I_CUSTOMER_INFO.I_1_PRESON_FOR_DELIVERY import PersonForDelivery
from D_PRODUCT_DETAILS.I_CUSTOMER_INFO.I_2_TITLE import Title
from D_PRODUCT_DETAILS.I_CUSTOMER_INFO.I_3_FIRST_NAME import FirstName
from D_PRODUCT_DETAILS.I_CUSTOMER_INFO.I_4_LAST_NAME import LastName
from D_PRODUCT_DETAILS.I_CUSTOMER_INFO.I_5_PHONE_NUMBER import PhoneNumber
from D_PRODUCT_DETAILS.I_CUSTOMER_INFO.I_6_EMAIL_ADDRESS import Email
#----------------------------------------------------------------
# PURCHASE SUMMARY IMPORTS
from D_PRODUCT_DETAILS.J_PURCHASE_SUMMARY.J_1_FINALIZE_PURCHASE import Finish
#----------------------------------------------------------------
# ORDER PROCESSING IMPORTS
from D_PRODUCT_DETAILS.K_ORDER_PROCESSING.K_1_SEND_TO_CUSTOMER import SendToCustomer
#----------------------------------------------------------------
from SUPPORTING_FILES.C_UTILITIES.A_2_GraphQL import GraphQLResponseChecker
from SUPPORTING_FILES.C_UTILITIES.A_10_Compare_graphql_results_with_data import GraphQLComparer
from SUPPORTING_FILES.C_UTILITIES.A_7_General_statistic import collect_statistics
from SUPPORTING_FILES.C_UTILITIES.A_4_Console_log import ConsoleLogChecker
from SUPPORTING_FILES.C_UTILITIES.A_12_Clear_cache_memory import BrowserCacheCleaner
#----------------------------------------------------------------
import time
#----------------------------------------------------------------

print("---------------------------------------------------------------------------------------------------")
browsers = ["chrome", "firefox", "edge"]

#---------------------------------------------------------------------------------------------------------
# RUN DRIVER

for browser in browsers:
    print(f"-------------------------------- Running tests on {browser.upper()} -------------------------------")
    #---------------------------------------------------------------------------------------------------------
    driver = setup_driver(browser)
    #---------------------------------------------------------------------------------------------------------
    #CELAN CACHE MEMORY
    BrowserCacheCleaner.clear_cache(driver)
    #---------------------------------------------------------------------------------------------------------
    # OPEN PAGE
    driver.get("https://app.one.com")
    #---------------------------------------------------------------------------------------------------------
    #INTERCEPTION - IMPORTANT!
    driver.scopes = ['.*']
    #---------------------------------------------------------------------------------------------------------
    #EMAIL
    email_form = EmailFormPage(driver)  
    email_form.enter_email_and_click_next("test.email@gmail.com")  
    print("--------------------------------------------------------------------------------------------------")
    #---------------------------------------------------------------------------------------------------------
    # ADD NEW APPLIANCE
    add_new_appliance = AddNewAppliance(driver)
    add_new_appliance.add_new_appliance()
    print("--------------------------------------------------------------------------------------------------")
    #---------------------------------------------------------------------------------------------------------
    # START PURCHASE PROCESS
    start_new_purchase = StartNewPurchaseButton(driver)
    start_new_purchase.click_start_new_purchase()
    print("--------------------------------------------------------------------------------------------------")

    #---------------------------------------------------------------------------------------------------------
    # SELECT PRODUCT CATEGORY
    product_category = SelectProductCategory(driver)
    product_category.select_product_category("Refrigerators")
    print("--------------------------------------------------------------------------------------------------")

    #---------------------------------------------------------------------------------------------------------
    # SELECT BRAND & MODEL
    brand_model = SelectBrandModel(driver)
    brand_model.select_brand_model("Samsung RF28R7201SR")
    print("--------------------------------------------------------------------------------------------------")

    #---------------------------------------------------------------------------------------------------------
    # SELECT QUANTITY
    quantity_selection = QuantitySelection(driver)
    quantity_selection.select_quantity("2")
    print("--------------------------------------------------------------------------------------------------")

    #---------------------------------------------------------------------------------------------------------
    # APPLIANCE TYPE
    appliance_type = SelectApplianceType(driver)
    appliance_type.select_appliance_type("Side-by-Side Refrigerator")
    print("--------------------------------------------------------------------------------------------------")

    #---------------------------------------------------------------------------------------------------------
    # PRODUCT USAGE TYPE
    product_usage = ProductUsageType(driver)
    product_usage.select_product_usage_type("Home Use")
    print("--------------------------------------------------------------------------------------------------")

    #---------------------------------------------------------------------------------------------------------
    # MANUAL ENTRY OF DETAILS
    manual_entry = ManualEntryOfDetails(driver)
    manual_entry.select_manual_entry_of_details("Cooling Technology: Twin Cooling Plus")
    print("--------------------------------------------------------------------------------------------------")

    #---------------------------------------------------------------------------------------------------------
    # BRAND SELECTION
    brand_selection = BrandSelection(driver)
    brand_selection.enter_brand_selection("Samsung")
    print("--------------------------------------------------------------------------------------------------")

    #---------------------------------------------------------------------------------------------------------
    # MODEL SELECTION
    model_selection = ModelSelection(driver)
    model_selection.enter_model_selection("RF28R7201SR")
    print("--------------------------------------------------------------------------------------------------")

    #---------------------------------------------------------------------------------------------------------
    # POWER SOURCE
    power_source = PowerSource(driver)
    power_source.enter_power_source("Electric")
    print("--------------------------------------------------------------------------------------------------")

    #---------------------------------------------------------------------------------------------------------
    # SERIAL NUMBER VALIDATION
    serial_number = SerialNumberValidation(driver)
    serial_number.enter_serial_number("SN123456789")
    print("--------------------------------------------------------------------------------------------------")

    #---------------------------------------------------------------------------------------------------------
    # APPLIANCE PRICE DETAILS
    appliance_price = AppliancePriceDetails(driver)
    appliance_price.enter_appliance_price_details("1200")
    print("--------------------------------------------------------------------------------------------------")

    #---------------------------------------------------------------------------------------------------------
    # RETAIL STORE DETAILS
    retail_store = RetailStoreDetails(driver)
    retail_store.enter_retail_store_details("BestBuy, NY")
    print("--------------------------------------------------------------------------------------------------")

    #---------------------------------------------------------------------------------------------------------
    # YEAR OF PRODUCTION
    year_of_production = YearOfProduction(driver)
    year_of_production.select_year_of_production("2023")
    print("--------------------------------------------------------------------------------------------------")

    #---------------------------------------------------------------------------------------------------------
    # APPLIANCE CATEGORY
    appliance_category = ApplianceCategory(driver)
    appliance_category.select_appliance_category("Kitchen Appliances")
    print("--------------------------------------------------------------------------------------------------")

    #---------------------------------------------------------------------------------------------------------
    # ENERGY RATING
    energy_rating = EnergyRating(driver)
    energy_rating.enter_energy_rating("5 Stars")
    print("--------------------------------------------------------------------------------------------------")

    #---------------------------------------------------------------------------------------------------------
    # WAREHOUSE LOCATION
    warehouse_location = WarehouseLocation(driver)
    warehouse_location.enter_warehouse_location("New Jersey Warehouse")
    print("--------------------------------------------------------------------------------------------------")

    #---------------------------------------------------------------------------------------------------------
    # WARRANTY AND SUPPORT
    warranty_support = WarrantyAndSupport(driver)
    warranty_support.select_warranty_and_support("2 Years Extended")
    print("--------------------------------------------------------------------------------------------------")

    #---------------------------------------------------------------------------------------------------------
    # INSURANCE COVERAGE
    insurance_coverage = InsuranceCoverage(driver)
    insurance_coverage.select_insurance_coverage("Yes")
    print("--------------------------------------------------------------------------------------------------")

    #---------------------------------------------------------------------------------------------------------
    # EXTENDED WARRANTY OPTIONS
    extended_warranty = ExtendedWarrantyOptions(driver)
    extended_warranty.select_extended_warranty_options("5 Years")
    print("--------------------------------------------------------------------------------------------------")

    #---------------------------------------------------------------------------------------------------------
    # INSTALLMENT PLANS AVAILABLE
    installment_plans = InstallmentPlansAvailable(driver)
    installment_plans.select_installment_plan("12 months")
    print("--------------------------------------------------------------------------------------------------")

    #---------------------------------------------------------------------------------------------------------
    # DISCOUNT AND PROMO CODES
    discount_promo = DiscountAndPromoCodes(driver)
    discount_promo.select_discount_or_promo_code("SUMMER50")
    print("--------------------------------------------------------------------------------------------------")

    #---------------------------------------------------------------------------------------------------------
    # SECURE PAYMENT METHODS
    payment_methods = SecurePaymentMethods(driver)
    payment_methods.select_payment_method("Credit Card")
    print("--------------------------------------------------------------------------------------------------")

    #---------------------------------------------------------------------------------------------------------
    # CUSTOMER FULL NAME
    customer_full_name = CustomerFullName(driver)
    customer_full_name.enter_customer_name("John Doe")
    print("--------------------------------------------------------------------------------------------------")

    #---------------------------------------------------------------------------------------------------------
    # CONTACT PHONE NUMBER
    contact_phone = ContactPhoneNumber(driver)
    contact_phone.enter_contact_phone_number("+1234567890")
    print("--------------------------------------------------------------------------------------------------")

    #---------------------------------------------------------------------------------------------------------
    # CUSTOMER EMAIL ADDRESS
    customer_email = CustomerEmailAddress(driver)
    customer_email.enter_customer_email_address("johndoe@example.com")
    print("--------------------------------------------------------------------------------------------------")

    #---------------------------------------------------------------------------------------------------------
    # CUSTOMER SHIPPING ADDRESS
    shipping_address = CustomerShippingAddress(driver)
    shipping_address.enter_customer_shipping_address("123 Main St, Los Angeles, CA")
    print("--------------------------------------------------------------------------------------------------")

    #---------------------------------------------------------------------------------------------------------
    # DELIVERY DATE AND TIME
    delivery_date_time = DeliveryDateAndTime(driver)
    delivery_date_time.enter_delivery_date_and_time("2024-03-10")
    print("--------------------------------------------------------------------------------------------------")

    #---------------------------------------------------------------------------------------------------------
    # ORDER TRACKING INFORMATION
    tracking_info = OrderTrackingInformation(driver)
    tracking_info.enter_order_tracking_information("FedEx Tracking: 1234567890")
    print("--------------------------------------------------------------------------------------------------")

    #---------------------------------------------------------------------------------------------------------
    # ORDER CONFIRMATION AND TOTAL
    order_confirmation = OrderConfirmationAndTotal(driver)
    order_confirmation.select_order_confirmation_and_total()
    print("--------------------------------------------------------------------------------------------------")

    #---------------------------------------------------------------------------------------------------------
    # SEND ORDER CONFIRMATION EMAIL
    send_order_email = SendOrderConfirmationEmail(driver)
    send_order_email.select_send_order_confirmation_email()
    print("--------------------------------------------------------------------------------------------------")

    #---------------------------------------------------------------------------------------------------------
    # CONTINUE SHOPPING OR CHECKOUT
    continue_checkout = ContinueShoppingOrCheckout(driver)
    continue_checkout.select_continue_shopping_or_checkout("Proceed to Checkout")
    print("--------------------------------------------------------------------------------------------------")

    #---------------------------------------------------------------------------------------------------------
    # SELECT PRODUCT OFFER
    select_offer = SelectOffer(driver)
    select_offer.click_select("Limited Time Offer - Free Installation")
    print("--------------------------------------------------------------------------------------------------")

    #---------------------------------------------------------------------------------------------------------
    # PERSON FOR DELIVERY
    person_delivery = PersonForDelivery(driver)
    person_delivery.enter_person_for_delivery("John Doe")
    print("--------------------------------------------------------------------------------------------------")

    #---------------------------------------------------------------------------------------------------------
    # TITLE
    title = Title(driver)
    title.select_title("Mr.")
    print("--------------------------------------------------------------------------------------------------")

    #---------------------------------------------------------------------------------------------------------
    # FIRST NAME
    first_name = FirstName(driver)
    first_name.enter_first_name("John")
    print("--------------------------------------------------------------------------------------------------")

    #---------------------------------------------------------------------------------------------------------
    # LAST NAME
    last_name = LastName(driver)
    last_name.enter_last_name()
    print("--------------------------------------------------------------------------------------------------")

    #---------------------------------------------------------------------------------------------------------
    # PHONE NUMBER
    phone_number = PhoneNumber(driver)
    phone_number.enter_phone_number("+1234567890")
    print("--------------------------------------------------------------------------------------------------")

    #---------------------------------------------------------------------------------------------------------
    # EMAIL
    email = Email(driver)
    email.enter_email("johndoe@example.com")
    print("--------------------------------------------------------------------------------------------------")

    #---------------------------------------------------------------------------------------------------------
    # FINALIZE PURCHASE
    finalize_purchase = Finish(driver)
    finalize_purchase.click_finish()
    print("--------------------------------------------------------------------------------------------------")

    #---------------------------------------------------------------------------------------------------------
    # SEND ORDER TO CUSTOMER
    send_order = SendToCustomer(driver)
    send_order.send_to_customer()
    print("--------------------------------------------------------------------------------------------------")
    #---------------------------------------------------------------------------------------------------------
    time.sleep(10)
    #---------------------------------------------------------------------------------------------------------
    # GRAPHQL CHECKER
    graphql_checker = GraphQLResponseChecker(driver)
    graphql_checker.fetch_second_last_graphql_request()
    print("--------------------------------------------------------------------------------------------------")
    #---------------------------------------------------------------------------------------------------------
    # GRAPHQL COMPARE WITH VALUES
    graphql_comparer = GraphQLComparer()
    graphql_comparer.compare_graphql_values()
    print("--------------------------------------------------------------------------------------------------")
    #---------------------------------------------------------------------------------------------------------
    #CONSOL CHECKER
    console_log_checker = ConsoleLogChecker(driver)
    console_logs = console_log_checker.fetch_console_logs()
    print("--------------------------------------------------------------------------------------------------")
    #---------------------------------------------------------------------------------------------------------
    #FILE LOGGER PATH
    log_file_path = r"C:\Users\PC\Desktop\app.log"
    collect_statistics(log_file_path, console_logs)
    print("--------------------------------------------------------------------------------------------------")
    #---------------------------------------------------------------------------------------------------------


    driver.quit()
    print(f"{browser.upper()} - Browser closed")
    print("--------------------------------------------------------------------------------------------------\n")