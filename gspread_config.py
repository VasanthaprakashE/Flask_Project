try:
    from google.oauth2.service_account import Credentials
    import gspread
except ImportError as e:
    raise ImportError(
        f"{e}\nInstall the required packages:\n"
        "pip install gspread google-auth"
    ) from e


SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]


def cred(cred_path, scopes=SCOPES):
    """
    Authenticate using a Google service account.

    Args:
        cred_path (str): Path to the service account JSON file.
        scopes (list): Google API scopes.

    Returns:
        gspread.Client: Authorized gspread client.
    """
    try:
        credentials = Credentials.from_service_account_file(
            cred_path,
            scopes=scopes
        )
        return gspread.authorize(credentials)

    except FileNotFoundError as e:
        raise FileNotFoundError(
            f"Credentials file not found: {cred_path}"
        ) from e