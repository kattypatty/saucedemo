class OrderData:
    # Error messages in case if one of the fields in not filled in
    first_name_error_message = "Error: First Name is required"
    last_name_error_message = "Error: Last Name is required"
    zip_code_error_message = "Error: Postal Code is required"


    # user data for filling checkout fields with invalid credentials
    # Three tests in one to check each line of checkout_info
    user_data_with_invalid_credential = [
        ("", "Smirnova", "125568", first_name_error_message),
        ("Victoria", "", "551248", last_name_error_message),
        ("Victoria", "Smirnova", "", zip_code_error_message),
    ]

    # user data for filling checkout fields with valid credentials
    user_data_with_valid_credential = ["Victoria", "Smirnova", "125568"]

    # The message when an order is succesfully done
    successful_message = "THANK YOU FOR YOUR ORDER"

