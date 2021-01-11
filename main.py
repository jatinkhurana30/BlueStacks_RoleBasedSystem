from CommandInterface import CommandInterface
from RABCSystem import RABCSystem
from Resource import Resource
from Role import Role
from User import User
from ActionType import ActionType

if __name__ == '__main__':

    """
    *******************
    Creating Resources
    *******************  
    """
    emails = Resource("Emails")
    text_messages = Resource("Text Messages")
    account_details = Resource("Account Details")

    """
    *******************
    Creating Roles
    *******************  
    """
    role_read_emails = Role("Role Read Emails").add_resource_privileges(emails, [ActionType.READ])
    role_emails = Role("Role Emails").add_resource_privileges(emails,
                                                              [ActionType.READ, ActionType.WRITE, ActionType.DELETE])

    role_read_messages = Role("Role Read Messages").add_resource_privileges(text_messages, [ActionType.READ])
    role_messages = Role("Role Messages").add_resource_privileges(text_messages,
                                                                  [ActionType.READ, ActionType.WRITE,
                                                                   ActionType.DELETE])

    role_read_account_details = Role("Role Read Account Details").add_resource_privileges(account_details,
                                                                                          [ActionType.READ,
                                                                                           ])
    role_account_details = Role("Role Account Details").add_resource_privileges(account_details,
                                                                                [ActionType.READ, ActionType.WRITE])

    """
    *******************
    Creating Users
    *******************  
    """
    admin_user = User("Admin User").add_role(role_emails).add_role(role_messages).add_role(role_read_account_details)
    super_admin_user = User("SuperAdmin User").add_role(role_emails).add_role(role_messages).add_role(
        role_account_details)
    user = User("NormalUser").add_role(role_read_emails).add_role(role_read_account_details).add_role(
        role_read_messages)

    """
    ******************* 
    Initializing RABC Systems and CLI Interface
    *******************
    """
    users = [admin_user, super_admin_user, user]
    roles = [role_read_messages, role_messages, role_read_emails, role_emails, role_read_account_details,
             role_account_details]
    resources = [emails, text_messages, account_details]

    rabc_system = RABCSystem(users=users, roles=roles, resources=resources)

    cli = CommandInterface(rabc_system)
    cli.execute_cli()
