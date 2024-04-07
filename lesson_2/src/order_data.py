class OrderData:
    # Error messages in case if one of the fields in not filled in
    first_name_error_message = "Error: First Name is required"
    last_name_error_message = "Error: Last Name is required"
    zip_code_error_message = "Error: Postal Code is required"


    # user data for filling fields
    user_data = [
        ("", "Smirnova", "125568", first_name_error_message),
        ("Victoria", "", "551248", last_name_error_message),
        ("Victoria", "Smirnova", "", zip_code_error_message),
    ]


