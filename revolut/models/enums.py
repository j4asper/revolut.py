from enum import Enum


class Environment(Enum):
    PRODUCTION = "merchant"
    SANDBOX = "sandbox-merchant"


class OrderType(Enum):
    PAYMENT = "payment"
    PAYMENT_REQUEST = "payment_request"
    REFUND = "refund"
    CHARGEBACK = "chargeback"
    CHARGEBACK_REVERSAL = "chargeback_reversal"
    CREDIT_REIMBURSEMENT = "credit_reimbursement"


class CaptureMode(Enum):
    AUTOMATIC = "automatic"
    MANUAL = "manual"


class AuthenticationChallengeType(Enum):
    THREE_DS = "three_ds"
    THREE_DS_FINGERPRINT = "three_ds_fingerprint"


class CardBrand(Enum):
    VISA = "visa"
    MASTERCARD = "mastercard"


class Funding(Enum):
    CREDIT = "credit"
    DEBIT = "debit"
    PREPAID = "prepaid"


class PaymentType(Enum):
    CARD = "card"
    REVOLUT_PAY_CARD = "revolut_pay_card"
    REVOLUT_PAY_ACCOUNT = "revolut_pay_account"


class VerificationResult(Enum):
    MATCH = "match"
    NOT_MATCH = "not_match"
    N_A = "n_a"
    INVALID = "invalid"
    INCORRECT = "incorrect"
    NOT_PROCESSED = "not_processed"


class FeeType(Enum):
    FX = "fx"
    ACQUIRING = "acquiring"


class RiskLevel(Enum):
    LOW = "low"
    HIGH = "high"


class State(Enum):
    PENDING = "pending"
    AUTHENTICATION_CHALLENGE = "authentication_challenge"
    AUTHENTICATION_VERIFIED = "authentication_verified"
    AUTHORISATION_STARTED = "authorisation_started"
    AUTHORISATION_PASSED = "authorisation_passed"
    AUTHORISED = "authorised"
    CAPTURE_STARTED = "capture_started"
    CAPTURED = "captured"
    REFUND_VALIDATED = "refund_validated"
    REFUND_STARTED = "refund_started"
    CANCELLATION_STARTED = "cancellation_started"
    DECLINING = "declining"
    COMPLETING = "completing"
    CANCELLING = "cancelling"
    FAILING = "failing"
    COMPLETED = "completed"
    DECLINED = "declined"
    SOFT_DECLINED = "soft_declined"
    CANCELLED = "cancelled"
    FAILED = "failed"
    PROCESSING = "processing"
    VERIFIED = "verified"
    CHALLENGE = "challenge"


class DeclineReason(Enum):
    HIGH_RISK = "high_risk"
    CARDHOLDER_NAME_MISSING = "cardholder_name_missing"
    UNKNOWN_CARD = "unknown_card"
    PICK_UP_CARD = "pick_up_card"
    INVALID_CARD = "invalid_card"
    EXPIRED_CARD = "expired_card"
    DO_NOT_HONOUR = "do_not_honour"
    INVALID_EMAIL = "invalid_email"
    INVALID_AMOUNT = "invalid_amount"
    RESTRICTED_CARD = "restricted_card"
    INSUFFICIENT_FUNDS = "insufficient_funds"
    REJECTED_BY_CUSTOMER = "rejected_by_customer"
    WITHDRAWAL_LIMIT_EXCEEDED = "withdrawal_limit_exceeded"
    ThreeDS_CHALLENGE_FAILED_MANUALLY = "3ds_challenge_failed_manually"
    TRANSACTION_NOT_ALLOWED_FOR_CARDHOLDER = "transaction_not_allowed_for_cardholder"
    ISSUER_NOT_AVAILABLE = "issuer_not_available"
    INVALID_EXPIRY = "invalid_expiry"
    INVALID_CVV = "invalid_cvv"
    INVALID_PIN = "invalid_pin"
    INVALID_PHONE = "invalid_phone"
    INVALID_ADDRESS = "invalid_address"
    INVALID_COUNTRY = "invalid_country"
    INVALID_MERCHANT = "invalid_merchant"
    CUSTOMER_CHALLENGE_FAILED = "customer_challenge_failed"
    CUSTOMER_CHALLENGE_ABANDONED = "customer_challenge_abandoned"
    CUSTOMER_NAME_MISMATCH = "customer_name_mismatch"
    TECHNICAL_ERROR = "technical_error"
