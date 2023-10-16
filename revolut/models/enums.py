# Credits to ChatGPT for making a lot of the enums here
from enum import Enum


class Environment(Enum):
    """The API Environments that are available."""
    PRODUCTION = "merchant"
    SANDBOX = "sandbox-merchant"


class OrderType(Enum):
    """The type of order object."""
    PAYMENT = "payment"
    PAYMENT_REQUEST = "payment_request"
    REFUND = "refund"
    CHARGEBACK = "chargeback"
    CHARGEBACK_REVERSAL = "chargeback_reversal"
    CREDIT_REIMBURSEMENT = "credit_reimbursement"


class EnforceChallenge(Enum):
    """The enforce challenge mode."""
    AUTOMATIC = "automatic"
    FORCED = "forced"


class EnvironmentType(Enum):
    """Type of environment where a payment was made."""
    BROWSER = "browser"


class Initiator(Enum):
    """Indicates who is allowed to initiate the payment."""
    CUSTOMER = "customer"
    MERCHANT = "merchant"


class CaptureMode(Enum):
    """The capture mode of an order."""
    AUTOMATIC = "automatic"
    MANUAL = "manual"


class AuthenticationChallengeType(Enum):
    """Type of the authentication challenge the payment triggers."""
    THREE_DS = "three_ds"
    THREE_DS_FINGERPRINT = "three_ds_fingerprint"


class CardBrand(Enum):
    """The credit card brands available."""
    VISA = "visa"
    MASTERCARD = "mastercard"


class Funding(Enum):
    """The type of card funding."""
    CREDIT = "credit"
    DEBIT = "debit"
    PREPAID = "prepaid"


class PaymentType(Enum):
    """The type of payment method used to pay for an order."""
    CARD = "card"
    REVOLUT_PAY_CARD = "revolut_pay_card"
    REVOLUT_PAY_ACCOUNT = "revolut_pay_account"


class VerificationResult(Enum):
    """The result of a verification."""
    MATCH = "match"
    NOT_MATCH = "not_match"
    N_A = "n_a"
    INVALID = "invalid"
    INCORRECT = "incorrect"
    NOT_PROCESSED = "not_processed"


class FeeType(Enum):
    """The type of order fee."""
    FX = "fx"
    ACQUIRING = "acquiring"


class RiskLevel(Enum):
    """The risk level of a card."""
    LOW = "low"
    HIGH = "high"


class State(Enum):
    """The status of a payment or an order."""
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
    """The reason for a failed or declined payment."""
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


class Currency(Enum):
    """ISO 4217 Currencies
    https://en.wikipedia.org/wiki/ISO_4217
    """
    AED = "AED"  # United Arab Emirates Dirham
    AFN = "AFN"  # Afghan Afghani
    ALL = "ALL"  # Albanian Lek
    AMD = "AMD"  # Armenian Dram
    ANG = "ANG"  # Netherlands Antillean Guilder
    AOA = "AOA"  # Angolan Kwanza
    ARS = "ARS"  # Argentine Peso
    AUD = "AUD"  # Australian Dollar
    AWG = "AWG"  # Aruban Florin
    AZN = "AZN"  # Azerbaijani Manat
    BAM = "BAM"  # Bosnia and Herzegovina Convertible Mark
    BBD = "BBD"  # Barbadian Dollar
    BDT = "BDT"  # Bangladeshi Taka
    BGN = "BGN"  # Bulgarian Lev
    BHD = "BHD"  # Bahraini Dinar
    BIF = "BIF"  # Burundian Franc
    BMD = "BMD"  # Bermudian Dollar
    BND = "BND"  # Brunei Dollar
    BOB = "BOB"  # Bolivian Boliviano
    BRL = "BRL"  # Brazilian Real
    BSD = "BSD"  # Bahamian Dollar
    BTN = "BTN"  # Bhutanese Ngultrum
    BWP = "BWP"  # Botswana Pula
    BYN = "BYN"  # Belarusian Ruble
    BZD = "BZD"  # Belize Dollar
    CAD = "CAD"  # Canadian Dollar
    CDF = "CDF"  # Congolese Franc
    CHF = "CHF"  # Swiss Franc
    CLP = "CLP"  # Chilean Peso
    CNY = "CNY"  # Chinese Yuan
    COP = "COP"  # Colombian Peso
    CRC = "CRC"  # Costa Rican Colón
    CUP = "CUP"  # Cuban Peso
    CVE = "CVE"  # Cape Verdean Escudo
    CZK = "CZK"  # Czech Republic Koruna
    DJF = "DJF"  # Djiboutian Franc
    DKK = "DKK"  # Danish Krone
    DOP = "DOP"  # Dominican Peso
    DZD = "DZD"  # Algerian Dinar
    EGP = "EGP"  # Egyptian Pound
    ERN = "ERN"  # Eritrean Nakfa
    ETB = "ETB"  # Ethiopian Birr
    EUR = "EUR"  # Euro
    FJD = "FJD"  # Fijian Dollar
    FKP = "FKP"  # Falkland Islands Pound
    FOK = "FOK"  # Faroese Króna
    GEL = "GEL"  # Georgian Lari
    GGP = "GGP"  # Guernsey Pound
    GHS = "GHS"  # Ghanaian Cedi
    GIP = "GIP"  # Gibraltar Pound
    GMD = "GMD"  # Gambian Dalasi
    GNF = "GNF"  # Guinean Franc
    GTQ = "GTQ"  # Guatemalan Quetzal
    GYD = "GYD"  # Guyanese Dollar
    HKD = "HKD"  # Hong Kong Dollar
    HNL = "HNL"  # Honduran Lempira
    HRK = "HRK"  # Croatian Kuna
    HTG = "HTG"  # Haitian Gourde
    HUF = "HUF"  # Hungarian Forint
    IDR = "IDR"  # Indonesian Rupiah
    ILS = "ILS"  # Israeli New Shekel
    IMP = "IMP"  # Isle of Man Pound
    INR = "INR"  # Indian Rupee
    IQD = "IQD"  # Iraqi Dinar
    IRR = "IRR"  # Iranian Rial
    ISK = "ISK"  # Icelandic Króna
    JEP = "JEP"  # Jersey Pound
    JMD = "JMD"  # Jamaican Dollar
    JOD = "JOD"  # Jordanian Dinar
    JPY = "JPY"  # Japanese Yen
    KES = "KES"  # Kenyan Shilling
    KGS = "KGS"  # Kyrgyzstani Som
    KHR = "KHR"  # Cambodian Riel
    KID = "KID"  # Kiribati Dollar
    KRW = "KRW"  # South Korean Won
    KWD = "KWD"  # Kuwaiti Dinar
    KYD = "KYD"  # Cayman Islands Dollar
    KZT = "KZT"  # Kazakhstani Tenge
    LAK = "LAK"  # Laotian Kip
    LBP = "LBP"  # Lebanese Pound
    LKR = "LKR"  # Sri Lankan Rupee
    LRD = "LRD"  # Liberian Dollar
    LSL = "LSL"  # Lesotho Loti
    LYD = "LYD"  # Libyan Dinar
    MAD = "MAD"  # Moroccan Dirham
    MDL = "MDL"  # Moldovan Leu
    MGA = "MGA"  # Malagasy Ariary
    MKD = "MKD"  # Macedonian Denar
    MMK = "MMK"  # Burmese Kyat
    MNT = "MNT"  # Mongolian Tögrög
    MOP = "MOP"  # Macanese Pataca
    MRU = "MRU"  # Mauritanian Ouguiya
    MUR = "MUR"  # Mauritian Rupee
    MVR = "MVR"  # Maldivian Rufiyaa
    MWK = "MWK"  # Malawian Kwacha
    MXN = "MXN"  # Mexican Peso
    MYR = "MYR"  # Malaysian Ringgit
    MZN = "MZN"  # Mozambican Metical
    NAD = "NAD"  # Namibian Dollar
    NGN = "NGN"  # Nigerian Naira
    NIO = "NIO"  # Nicaraguan Córdoba
    NOK = "NOK"  # Norwegian Krone
    NPR = "NPR"  # Nepalese Rupee
    NZD = "NZD"  # New Zealand Dollar
    OMR = "OMR"  # Omani Rial
    PAB = "PAB"  # Panamanian Balboa
    PEN = "PEN"  # Peruvian Nuevo Sol
    PGK = "PGK"  # Papua New Guinean Kina
    PHP = "PHP"  # Philippine Peso
    PKR = "PKR"  # Pakistani Rupee
    PLN = "PLN"  # Polish Złoty
    PYG = "PYG"  # Paraguayan Guarani
    QAR = "QAR"  # Qatari Riyal
    RON = "RON"  # Romanian Leu
    RSD = "RSD"  # Serbian Dinar
    RUB = "RUB"  # Russian Ruble
    RWF = "RWF"  # Rwandan Franc
    SAR = "SAR"  # Saudi Riyal
    SBD = "SBD"  # Solomon Islands Dollar
    SCR = "SCR"  # Seychellois Rupee
    SDG = "SDG"  # Sudanese Pound
    SEK = "SEK"  # Swedish Krona
    SGD = "SGD"  # Singapore Dollar
    SHP = "SHP"  # Saint Helena Pound
    SLL = "SLL"  # Sierra Leonean Leone
    SOS = "SOS"  # Somali Shilling
    SRD = "SRD"  # Surinamese Dollar
    SSP = "SSP"  # South Sudanese Pound
    STN = "STN"  # São Tomé and Príncipe Dobra
    SVC = "SVC"  # Salvadoran Colón
    SYP = "SYP"  # Syrian Pound
    SZL = "SZL"  # Eswatini Lilangeni
    THB = "THB"  # Thai Baht
    TJS = "TJS"  # Tajikistani Somoni
    TMT = "TMT"  # Turkmenistani Manat
    TND = "TND"  # Tunisian Dinar
    TOP = "TOP"  # Tongan Pa'anga
    TRY = "TRY"  # Turkish Lira
    TTD = "TTD"  # Trinidad and Tobago Dollar
    TWD = "TWD"  # New Taiwan Dollar
    TZS = "TZS"  # Tanzanian Shilling
    UAH = "UAH"  # Ukrainian Hryvnia
    UGX = "UGX"  # Ugandan Shilling
    USD = "USD"  # United States Dollar
    UYU = "UYU"  # Uruguayan Peso
    UZS = "UZS"  # Uzbekistani Soʻm
    VES = "VES"  # Venezuelan Bolívar
    VND = "VND"  # Vietnamese Đồng
    VUV = "VUV"  # Vanuatu Vatu
    WST = "WST"  # Samoan Tala
    XAF = "XAF"  # Central African CFA Franc
    XCD = "XCD"  # Eastern Caribbean Dollar
    XOF = "XOF"  # West African CFA Franc
    XPF = "XPF"  # CFP Franc
    YER = "YER"  # Yemeni Rial
    ZAR = "ZAR"  # South African Rand
    ZMW = "ZMW"  # Zambian Kwacha
    ZWL = "ZWL"  # Zimbabwean Dollar
