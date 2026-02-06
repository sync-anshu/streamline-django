from pyairtable import Api
from django.conf import settings
from pyairtable.api.types import RecordDict

api = Api(settings.AIRTABLE_API_KEY)


def match_airtable_user(username: str) -> tuple[bool, bool]:
    '''
    Match a user in Airtable and return if the user exists and if they have access.

    parameters:
        username: str - the email to match
    returns:
        tuple[bool, bool] - a tuple containing a boolean indicating if the user exists and a boolean indicating if they have access. If the user does not exist, return None.
    '''


    account_found = False
    allow_access = False    

    try:
        accounts_table = api.table('appvOFmpLj8ZNNGPR', 'tbl25IPMcnCR5bOIR')  
        accounts = accounts_table.all()

        for account in accounts:
            #
            fields = account.get('fields',{})
            if fields.get('Email (from Account Owner)')[-1] == username:
                allow_access = fields.get('Allow Access', False)
                account_found = True

                if not allow_access:
                    return account_found, allow_access

                break

        return account_found, allow_access
    except Exception as e:
        return account_found, allow_access


def get_airtable_user(username: str) -> RecordDict | None:
    '''
    Get a user from Airtable and return the user's information.

    parameters:
        username: str - the email to match
    returns:
        RecordDict | None - a dictionary containing the user's information. If the user does not exist, return None.
    '''
    user = None
    
    try:
        accounts_table = api.table('appvOFmpLj8ZNNGPR', 'tbl25IPMcnCR5bOIR')  
        accounts = accounts_table.all()

        for account in accounts:
            fields = account.get('fields',{})
            if fields.get('Email (from Account Owner)')[-1] == username:
                user = account
                break

        return user
    except Exception as e:
        return user