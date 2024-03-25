from semantic_kernel.functions import kernel_function
from typing import Annotated, Optional

class LicenseOperationsPlugin():
    """
    Description: Activate license and resend activation e-mail to customer.
    """

    @kernel_function(
        description="Activate new license for customer",
        name="ActivateLicenseAndSendActivationEmail",
    )
    def activate_license(self, activation_key: Annotated[str, "the activation key"], full_name: Annotated[str, "the customer full name"], email: Annotated[str, "the customer email"]) -> Annotated[str, "the output is the message to the user"]:
        """
        Description: Activate license
        Args:
            activation_key (str): the activation key
            full_name (str): the customer full name
            email (str): the customer email
        Returns:
            str value
        """
        try:
        
            # TODO: Call API endoint and handle response
            
            return f"""We have sent activation email to customer.\n
We have registered this customer's data:\n
Full Name: {full_name}\n
Email: {email}\n
Activation Key: {activation_key}
"""
        except ValueError as e:
            raise e
    @kernel_function(
        description="Recover existing license for customer",
        name="RecoverLicenseSkill",
    )
    def lost_license(self, email: Annotated[str, "the customer email"]) -> Annotated[str, "the output is the message to the user"]:
        """
        Description: Lost license
        Args:
            email (str): the customer email
            confirmation (str): the customer confirmation
        Returns:
            str value
        """
        try:
            # TODO: Call API endoint and handle response
            
            return f"""We have sent further details to customer's email address {email}"""
        except ValueError as e:
            raise e