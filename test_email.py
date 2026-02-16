from exchangelib import Account, Credentials, Configuration

# ====== INPUTS ======
EMAIL = "your_email@domain.com"
PASSWORD = "your_password"
EWS_URL = "https://mail.yourdomain.com/EWS/Exchange.asmx"
# ====================

try:
    # Step 1: Credentials
    creds = Credentials(username=EMAIL, password=PASSWORD)

    # Step 2: Configuration with given EWS URL
    config = Configuration(
        service_endpoint=EWS_URL,
        credentials=creds
    )

    # Step 3: Connect (no autodiscover)
    account = Account(
        primary_smtp_address=EMAIL,
        config=config,
        autodiscover=False
    )

    # Step 4: Simple call to verify access
    inbox_count = account.inbox.total_count

    print("EWS Connection Successful")
    print("Inbox total emails:", inbox_count)

except Exception as e:
    print("Connection Failed")
    print("Error:", str(e))
