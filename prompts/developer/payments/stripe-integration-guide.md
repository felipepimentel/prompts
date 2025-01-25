---
category: Developer
description: Comprehensive guide for implementing secure payment processing with Stripe
model: GPT-4
path: developer/payments/stripe-integration-guide
prompt_type: Instruction-based prompting
tags:
- stripe
- payments
- security
- api
- integration
- e-commerce
title: Stripe Integration Guide
version: '1.0'
---

# Stripe Integration Guide

## Setup and Configuration

### 1. Initial Setup
```bash
# Install Stripe SDK
npm install stripe @stripe/stripe-js

# Install Stripe CLI (for webhook testing)
brew install stripe/stripe-cli/stripe
```

### 2. Environment Configuration
```typescript
// config/stripe.ts
export const stripeConfig = {
  publishableKey: process.env.NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY!,
  secretKey: process.env.STRIPE_SECRET_KEY!,
  webhookSecret: process.env.STRIPE_WEBHOOK_SECRET!,
  currency: "usd",
  mode: process.env.NODE_ENV === "production" ? "live" : "test",
}
```

## Core Integration

### 1. Client-Side Setup
```typescript
// lib/stripe-client.ts
import { loadStripe } from "@stripe/stripe-js"
import { stripeConfig } from "@/config/stripe"

export const getStripe = async () => {
  const stripe = await loadStripe(stripeConfig.publishableKey)
  if (!stripe) throw new Error("Failed to initialize Stripe")
  return stripe
}
```

### 2. Server-Side Setup
```typescript
// lib/stripe-server.ts
import Stripe from "stripe"
import { stripeConfig } from "@/config/stripe"

export const stripe = new Stripe(stripeConfig.secretKey, {
  apiVersion: "2023-10-16",
  appInfo: {
    name: "YourApp",
    version: "1.0.0",
  },
})
```

## Payment Flows

### 1. One-Time Payment
```typescript
// pages/api/create-payment-intent.ts
import { stripe } from "@/lib/stripe-server"

export async function createPaymentIntent(amount: number) {
  const paymentIntent = await stripe.paymentIntents.create({
    amount: amount * 100, // Convert to cents
    currency: stripeConfig.currency,
    automatic_payment_methods: {
      enabled: true,
    },
  })

  return {
    clientSecret: paymentIntent.client_secret,
  }
}
```

### 2. Subscription Setup
```typescript
// pages/api/create-subscription.ts
export async function createSubscription(
  customerId: string,
  priceId: string
) {
  const subscription = await stripe.subscriptions.create({
    customer: customerId,
    items: [{ price: priceId }],
    payment_behavior: "default_incomplete",
    expand: ["latest_invoice.payment_intent"],
  })

  return {
    subscriptionId: subscription.id,
    clientSecret: (
      subscription.latest_invoice as Stripe.Invoice
    ).payment_intent?.client_secret,
  }
}
```

## Payment UI Components

### 1. Card Element
```tsx
import { CardElement } from "@stripe/stripe-js"
import { useStripe, useElements } from "@stripe/stripe-js"

export function PaymentForm() {
  const stripe = useStripe()
  const elements = useElements()

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault()
    if (!stripe || !elements) return

    const { error, paymentMethod } = await stripe.createPaymentMethod({
      type: "card",
      card: elements.getElement(CardElement)!,
    })

    if (error) {
      console.error(error)
    } else {
      // Handle successful payment method creation
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <CardElement
        options={{
          style: {
            base: {
              fontSize: "16px",
              color: "#424770",
              "::placeholder": {
                color: "#aab7c4",
              },
            },
            invalid: {
              color: "#9e2146",
            },
          },
        }}
      />
      <button type="submit">Pay</button>
    </form>
  )
}
```

### 2. Payment Element
```tsx
import { PaymentElement } from "@stripe/stripe-js"

export function CheckoutForm() {
  return (
    <form>
      <PaymentElement
        options={{
          layout: "tabs",
        }}
      />
      <button>Submit</button>
    </form>
  )
}
```

## Webhook Handling

### 1. Webhook Setup
```typescript
// pages/api/webhooks/stripe.ts
import { buffer } from "micro"
import Stripe from "stripe"

export const config = {
  api: {
    bodyParser: false,
  },
}

export default async function handler(req, res) {
  const buf = await buffer(req)
  const sig = req.headers["stripe-signature"]!

  try {
    const event = stripe.webhooks.constructEvent(
      buf,
      sig,
      stripeConfig.webhookSecret
    )

    switch (event.type) {
      case "payment_intent.succeeded":
        await handlePaymentSuccess(event.data.object)
        break
      case "payment_intent.failed":
        await handlePaymentFailure(event.data.object)
        break
      // Handle other events
    }

    res.status(200).json({ received: true })
  } catch (err) {
    res.status(400).send(`Webhook Error: ${err.message}`)
  }
}
```

### 2. Event Handlers
```typescript
// lib/stripe-webhooks.ts
async function handlePaymentSuccess(paymentIntent: Stripe.PaymentIntent) {
  // Update order status
  // Send confirmation email
  // Update inventory
}

async function handlePaymentFailure(paymentIntent: Stripe.PaymentIntent) {
  // Update order status
  // Send failure notification
  // Handle inventory hold
}
```

## Error Handling

### 1. Client-Side Errors
```typescript
function handleStripeError(error: any) {
  switch (error.type) {
    case "card_error":
      return "Your card was declined."
    case "validation_error":
      return "Please check your payment details."
    default:
      return "An unexpected error occurred."
  }
}
```

### 2. Server-Side Errors
```typescript
function handleStripeAPIError(error: Stripe.StripeError) {
  switch (error.type) {
    case "StripeCardError":
      // Handle card errors
      break
    case "StripeRateLimitError":
      // Handle rate limiting
      break
    case "StripeInvalidRequestError":
      // Handle invalid requests
      break
    case "StripeAPIError":
      // Handle API errors
      break
    case "StripeConnectionError":
      // Handle connection errors
      break
    case "StripeAuthenticationError":
      // Handle authentication errors
      break
    default:
      // Handle unknown errors
      break
  }
}
```

## Security Best Practices

### 1. Data Handling
- Never log card details
- Use HTTPS everywhere
- Implement proper CORS
- Validate all inputs
- Use idempotency keys

### 2. Authentication
- Verify webhook signatures
- Secure API keys
- Implement rate limiting
- Use proper session handling
- Monitor for suspicious activity

### 3. Compliance
- Follow PCI DSS guidelines
- Implement SCA when required
- Handle user data properly
- Keep SDK updated
- Regular security audits

## Testing

### 1. Test Cards
```typescript
const TEST_CARDS = {
  success: "4242424242424242",
  decline: "4000000000000002",
  insufficient_funds: "4000000000009995",
  requires_auth: "4000002500003155",
}
```

### 2. Test Webhooks
```bash
# Start webhook forwarding
stripe listen --forward-to localhost:3000/api/webhooks/stripe

# Trigger test events
stripe trigger payment_intent.succeeded
```

Remember: Always prioritize security and user experience when implementing Stripe payments. Keep your dependencies updated and regularly test your integration with different scenarios and edge cases.