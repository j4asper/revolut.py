# THIS PACKAGE IS NOT READY FOR RELEASE YET - NO ETA

---

[![GitHub](https://img.shields.io/github/license/j4asper/revolut.py?style=for-the-badge)](https://github.com/j4asper/revolut.py/blob/main/LICENSE)

# Revolut Merchant API Wrapper
Simple Revolut Merchant API Wrapper written in Python 3. This API Wrapper will make it easier to interact with the [Merchant API](https://developer.revolut.com/docs/accept-payments), provided by [Revolut](https://www.revolut.com/business/). It's highly recommended to read through [Revoluts Merchant API docs](https://developer.revolut.com/docs/merchant/merchant-api), as this API wrapper uses the same names for almost everything.

## Table of Contents

- [Installation](#installation)
  - [Install with PIP](#install-with-pip)
  - [Install from source](#install-from-source)
- [Initial Setup](#initial-setup)
- [Sandbox Environment](#sandbox-environment)
- [Current Goal](#current-goal)
  - [Checklist](#checklist)

## Installation

### Install with PIP

```console
python -m pip install revolut.py
```

### Install from source

This installation may or may not work all the time. If it doesn't, use the pip installation as a fallback.

```console
python -m pip install git+https://github.com/j4asper/revolut.py
```

## Initial Setup

To use the Revolut Merchant API, you will need a Revolut Merchant account, to do thi,s you can follow [Revoluts own guide here](https://developer.revolut.com/docs/guides/accept-payments/get-started/apply-for-a-merchant-account).

When you have got the Merchant Account, you can now see the API keys needed to interact with the API. Follow [this guide](https://developer.revolut.com/docs/guides/accept-payments/get-started/generate-the-api-key) to locate them.

## Sandbox Environment

It's highly recommended to use Revoluts Sandbox environment when testing your implementation of the API. To use the sandbox environment, you need to make a new account on the sandbox version of the revolut site, which can be [found here](https://sandbox-business.revolut.com/signup). When you have done that, get your API keys, and then you should be good to go.

The testing cards can be [found here](https://developer.revolut.com/docs/guides/accept-payments/get-started/test-in-the-sandbox-environment/test-cards), they will come in handy when testing different payment outcomes.

## Current Goal

The goal of this API wrapper is to cover [Revoluts Merchant API Implementation Checklist](https://developer.revolut.com/docs/guides/accept-payments/get-started/implementation-checklists).

### Checklist

**Customer management:**

- [ ] [Create a customer](https://github.com/j4asper/revolut.py/issues/15)
- [ ] [Update customer details](https://github.com/j4asper/revolut.py/issues/2)
- [ ] [Delete customer](https://github.com/j4asper/revolut.py/issues/3)

**Order management:**

- [x] [Create and pay for order](https://github.com/j4asper/revolut.py/issues/4)
- [ ] [Capture order later](https://github.com/j4asper/revolut.py/issues/5)
- [ ] [Cancel order (without capture later)](https://github.com/j4asper/revolut.py/issues/6)
- [ ] [Cancel uncaptured order](https://github.com/j4asper/revolut.py/issues/7)
- [ ] [Manage billing and delivery information](https://github.com/j4asper/revolut.py/issues/8)

**Refunds:**

- [ ] [Refund order](https://github.com/j4asper/revolut.py/issues/9)
- [ ] [Manage partial refund](https://github.com/j4asper/revolut.py/issues/10)
- [ ] [Manage multiple partial refunds](https://github.com/j4asper/revolut.py/issues/11)
- [ ] [Refund order fully by partial refunds](https://github.com/j4asper/revolut.py/issues/12)

**Webhooks:**

- [ ] [Set and listen to Revolut webhooks](https://github.com/j4asper/revolut.py/issues/13)
