---
title: "Code Documentation Template"
path: "developer/documentation/code-documentation-template"
tags: ["documentation", "code-comments", "docstrings", "best-practices"]
description: "A comprehensive guide for writing clear and effective code documentation, including comments and docstrings"
prompt_type: "Documentation Framework"
---

<purpose>
To provide a structured approach for writing clear, comprehensive, and maintainable code documentation that follows language-specific conventions.
</purpose>

<context>
Use this template when documenting code to ensure consistency and completeness in documentation across your codebase.
</context>

<instructions>
Provide the following documentation elements:

1. Documentation Overview
   - Basic Information
     * Code element type
     * Language/framework
     * Documentation style
     * Conventions to follow

   - Documentation Scope
     * Files to document
     * Level of detail
     * Target audience
     * Special requirements

2. Documentation Components
   - File Headers
     * Copyright notice
     * File purpose
     * Author information
     * Version history

   - Code Elements
     * Classes
     * Functions
     * Variables
     * Constants

3. Documentation Content
   - Element Description
     * Purpose/behavior
     * Parameters/properties
     * Return values
     * Exceptions

   - Additional Details
     * Usage examples
     * Dependencies
     * Side effects
     * Performance notes

4. Documentation Style
   - Formatting
     * Indentation
     * Line length
     * Section ordering
     * Whitespace rules

   - Best Practices
     * Clarity guidelines
     * Consistency rules
     * Common patterns
     * Anti-patterns

</instructions>

<variables>
- programming_language: Language being documented
- documentation_style: Style guide to follow
- code_element: Type of code being documented
- audience_level: Technical expertise of audience
</variables>

<examples>
Example 1:
Input: Python function documentation
Output:
```python
def process_transaction(
    amount: float,
    currency: str,
    user_id: int,
    *,
    retry_count: int = 3
) -> dict:
    """
    Process a financial transaction for a user with automatic retry capability.

    This function handles the complete transaction flow, including validation,
    processing, and error handling. It will automatically retry failed
    transactions up to the specified number of times.

    Args:
        amount (float): The transaction amount (must be positive)
        currency (str): Three-letter currency code (e.g., 'USD', 'EUR')
        user_id (int): The unique identifier of the user
        retry_count (int, optional): Maximum number of retry attempts. Defaults to 3.

    Returns:
        dict: A dictionary containing transaction details:
            {
                'transaction_id': str,
                'status': str,
                'timestamp': datetime,
                'amount': float,
                'currency': str,
                'user_id': int
            }

    Raises:
        ValueError: If amount is negative or currency code is invalid
        UserNotFoundError: If user_id doesn't exist in the system
        TransactionFailedError: If transaction fails after all retries

    Examples:
        >>> try:
        ...     result = process_transaction(100.50, 'USD', 12345)
        ...     print(f"Transaction completed: {result['transaction_id']}")
        ... except TransactionFailedError as e:
        ...     print(f"Transaction failed: {e}")

    Note:
        - Currency codes must follow ISO 4217 standard
        - Transaction amounts are rounded to 2 decimal places
        - Retry attempts have exponential backoff
    """
    # Function implementation here
    pass


class PaymentProcessor:
    """
    A class to handle various payment processing operations.

    This class provides a comprehensive interface for processing different
    types of payments, managing refunds, and handling payment-related
    operations with proper error handling and logging.

    Attributes:
        gateway (PaymentGateway): The payment gateway instance
        retry_limit (int): Maximum number of retry attempts
        timeout (float): Request timeout in seconds

    Note:
        This class requires proper initialization of payment gateway
        credentials through environment variables or configuration files.
    """

    def __init__(self, gateway: PaymentGateway, retry_limit: int = 3):
        """
        Initialize the PaymentProcessor with a specific gateway.

        Args:
            gateway (PaymentGateway): The payment gateway to use
            retry_limit (int, optional): Maximum retry attempts. Defaults to 3.

        Raises:
            ConfigurationError: If gateway credentials are missing
            ConnectionError: If gateway connection fails
        """
        self.gateway = gateway
        self.retry_limit = retry_limit
        self._initialize_gateway()

    def process_payment(
        self,
        amount: Decimal,
        currency: str,
        payment_method: dict
    ) -> PaymentResult:
        """
        Process a payment using the configured gateway.

        Args:
            amount (Decimal): Payment amount
            currency (str): Three-letter currency code
            payment_method (dict): Payment method details:
                {
                    'type': str,
                    'token': str,
                    'save': bool
                }

        Returns:
            PaymentResult: Object containing:
                - transaction_id: str
                - status: str
                - error: Optional[str]

        Raises:
            PaymentValidationError: If payment details are invalid
            PaymentProcessingError: If payment processing fails
            GatewayTimeoutError: If gateway doesn't respond in time
        """
        # Method implementation here
        pass
```

Example 2:
Input: JavaScript/TypeScript class documentation
Output:
```typescript
/**
 * Manages user authentication and session handling.
 * 
 * This class provides comprehensive user authentication functionality,
 * including login, logout, session management, and token refresh operations.
 * It supports both JWT and session-based authentication methods.
 * 
 * @example
 * ```typescript
 * const auth = new AuthManager({
 *   tokenStorage: 'localStorage',
 *   refreshInterval: 5 * 60 * 1000 // 5 minutes
 * });
 * 
 * try {
 *   await auth.login('user@example.com', 'password');
 *   console.log('Login successful');
 * } catch (error) {
 *   console.error('Login failed:', error.message);
 * }
 * ```
 */
class AuthManager {
  private tokenStorage: Storage;
  private refreshInterval: number;
  private refreshTimeout?: NodeJS.Timeout;

  /**
   * Creates an instance of AuthManager.
   * 
   * @param {Object} config - Configuration options
   * @param {string} config.tokenStorage - Storage type ('localStorage' | 'sessionStorage')
   * @param {number} config.refreshInterval - Token refresh interval in milliseconds
   * @throws {ConfigError} If invalid storage type is provided
   */
  constructor(config: AuthConfig) {
    this.validateConfig(config);
    this.initialize(config);
  }

  /**
   * Attempts to log in a user with the provided credentials.
   * 
   * @param {string} email - User's email address
   * @param {string} password - User's password
   * @param {boolean} [remember=false] - Whether to persist the session
   * @returns {Promise<UserSession>} Session information if login successful
   * @throws {AuthError} If login fails
   * @throws {ValidationError} If credentials are invalid
   */
  async login(
    email: string,
    password: string,
    remember: boolean = false
  ): Promise<UserSession> {
    // Method implementation
  }

  /**
   * Refreshes the current authentication token.
   * 
   * This method attempts to obtain a new access token using the refresh token.
   * If successful, it updates the stored tokens and resets the refresh timer.
   * 
   * @returns {Promise<void>}
   * @throws {AuthError} If token refresh fails
   * @throws {TokenExpiredError} If refresh token has expired
   * @private
   */
  private async refreshToken(): Promise<void> {
    // Method implementation
  }
}

/**
 * Middleware to check authentication status.
 * 
 * This middleware verifies the presence and validity of authentication
 * tokens in incoming requests. It can be used to protect routes that
 * require authentication.
 * 
 * @param {Request} req - Express request object
 * @param {Response} res - Express response object
 * @param {NextFunction} next - Express next function
 * @returns {void}
 * @throws {UnauthorizedError} If authentication is invalid
 * 
 * @example
 * ```typescript
 * app.get('/protected', authMiddleware, (req, res) => {
 *   res.json({ message: 'Protected data' });
 * });
 * ```
 */
function authMiddleware(
  req: Request,
  res: Response,
  next: NextFunction
): void {
  // Middleware implementation
}
```
</examples>

<notes>
- Be clear and concise
- Follow language conventions
- Document public interfaces
- Include usage examples
- Explain complex logic
- Keep docs up to date
- Use consistent style
- Document exceptions
</notes> 