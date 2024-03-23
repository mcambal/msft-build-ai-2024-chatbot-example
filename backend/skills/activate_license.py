from semantic_kernel.functions import kernel_function
from typing import Annotated, Optional

class ActivateLicenseSkillPlugin():
    """
    Description: Activate license and resend activation e-mail to customer.
    """

    @kernel_function(
        description="Activate license and send activation e-mail to customer.",
        name="ActivateLicenseAndSendActivationEmail",
    )
    
    def activate_license(self, activation_key: Annotated[Optional[str], "the activation key"] = None, full_name: Annotated[Optional[str], "the customer full name"] = None, email: Annotated[Optional[str], "the customer email"] = None, confirmation: Annotated[Optional[str], "the customer confirmation"] = None) -> Annotated[str, "the output is the message to the user"]:
        """
        Description: Activate license and resend activation e-mail to customer.
        Args:
            activation_key (str): the activation key
            full_name (str): the customer full name
            email (str): the customer email
            confirmation (str): the customer confirmation
        Returns:
            str value
        """
        try:
            if(activation_key == ""):
                return """To activate your license we need to know your activation key, full name and contact email address.\n\nWhat is your activation key, please?"""
            
            if(full_name == ""):
                return "What is your full name, please?"
            
            if(email == ""):
                return f"What is your contact email address, please?"
            
            if(confirmation == ""):
                return f"We will send an activation email to { email }. Do you want to proceed?"

            if(confirmation.lower() == 'false'):
                return "Sure. How can I help you?"
            else:
                print(f"Activating user email {email} with license key {activation_key} and full name {full_name}")
                return f"Thank you { full_name }. We have sent you an email with further details"
        except ValueError as e:
            print(f"Invalid input {email}")
            raise e