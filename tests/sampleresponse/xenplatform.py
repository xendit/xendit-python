def xenplatform_account_response():
    return {
        "account_email": "test-xenplatform@pythonxendit.co",
        "user_id": "5f2132ed172cd67992c402d6",
        "created": "2020-07-29T08:27:25.346Z",
        "status": "SUCCESSFUL",
        "type": "OWNED",
    }


def xenplatform_callback_url_response():
    return {
        "status": "SUCCESSFUL",
        "user_id": "5e6b30d967627b957de8c123",
        "url": "https://test-url-invoice.com",
        "environment": "TEST",
        "callback_token": "66a6680348e1c33ed2b9053a8eb9291b9e2230ff4f4d3057c9f4ac26405d2123",
    }


def xenplatform_transfers_response():
    return {
        "created": "2020-01-01T08:51:44.484Z",
        "transfer_id": "60b9d810-d9a3-456c-abbf-2786ec7a9651",
        "reference": "transfer001",
        "source_user_id": "54afeb170a2b18519b1b8768",
        "destination_user_id": "5cafeb170a2b1851246b8768",
        "status": "SUCCESSFUL",
        "amount": 10000,
    }
