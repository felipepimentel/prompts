---
description: Comprehensive guide for integrating Stripe payment solutions securely
  and efficiently into web applications
path: developer/stripe/stripe.md
prompt_type: Instruction-based prompting
tags:
- stripe
- payments
- security
- api
- nodejs
- typescript
- webhooks
title: Stripe Integration Guide
---

# Stripe Integration Guide

## Core Setup

### 1. Installation and Configuration
```bash
# Install Stripe SDK
npm install stripe @stripe/stripe-js

# Install types for TypeScript
npm install -D @types/stripe
```

```typescript
// config/stripe.ts
import Stripe from 'stripe';

export const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!, {
  apiVersion: '2023-10-16',
  typescript: true,
});

export const stripePublicKey = process.env.NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY!;
```

### 2. Environment Setup
```env
# .env.local
STRIPE_SECRET_KEY=sk_test_...
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...
```

## Payment Integration

### 1. Payment Intent Creation
```typescript
// app/api/create-payment-intent/route.ts
import { stripe } from '@/config/stripe';
import { NextResponse } from 'next/server';

export async function POST(req: Request) {
  try {
    const { amount, currency = 'usd' } = await req.json();

    const paymentIntent = await stripe.paymentIntents.create({
      amount,
      currency,
      automatic_payment_methods: {
        enabled: true,
      },
    });

    return NextResponse.json({ clientSecret: paymentIntent.client_secret });
  } catch (error) {
    if (error instanceof Error) {
      return NextResponse.json({ error: error.message }, { status: 400 });
    }
    return NextResponse.json(
      { error: 'Internal Server Error' },
      { status: 500 }
    );
  }
}
```

### 2. Client-Side Implementation
```typescript
// components/PaymentForm.tsx
import { useState } from 'react';
import {
  PaymentElement,
  useStripe,
  useElements,
  Elements,
} from '@stripe/react-stripe-js';
import { loadStripe } from '@stripe/stripe-js';

const stripePromise = loadStripe(process.env.NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY!);

export function PaymentForm() {
  const stripe = useStripe();
  const elements = useElements();
  const [error, setError] = useState<string | null>(null);
  const [processing, setProcessing] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!stripe || !elements) return;

    setProcessing(true);
    setError(null);

    try {
      const { error: submitError } = await stripe.confirmPayment({
        elements,
        confirmParams: {
          return_url: `${window.location.origin}/payment/success`,
        },
      });

      if (submitError) {
        setError(submitError.message ?? 'Payment failed');
      }
    } catch (e) {
      setError('An unexpected error occurred');
    } finally {
      setProcessing(false);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <PaymentElement />
      {error && <div className="text-red-500">{error}</div>}
      <button
        type="submit"
        disabled={!stripe || processing}
        className="mt-4 px-4 py-2 bg-blue-500 text-white rounded"
      >
        {processing ? 'Processing...' : 'Pay Now'}
      </button>
    </form>
  );
}

export function PaymentFormWrapper({ clientSecret }: { clientSecret: string }) {
  return (
    <Elements stripe={stripePromise} options={{ clientSecret }}>
      <PaymentForm />
    </Elements>
  );
}
```

## Webhook Handling

### 1. Webhook Setup
```typescript
// app/api/webhooks/route.ts
import { stripe } from '@/config/stripe';
import { headers } from 'next/headers';
import { NextResponse } from 'next/server';

const webhookSecret = process.env.STRIPE_WEBHOOK_SECRET!;

export async function POST(req: Request) {
  try {
    const body = await req.text();
    const signature = headers().get('stripe-signature')!;

    const event = stripe.webhooks.constructEvent(
      body,
      signature,
      webhookSecret
    );

    switch (event.type) {
      case 'payment_intent.succeeded':
        await handlePaymentSuccess(event.data.object);
        break;
      case 'payment_intent.payment_failed':
        await handlePaymentFailure(event.data.object);
        break;
      // Add other event handlers as needed
    }

    return NextResponse.json({ received: true });
  } catch (error) {
    if (error instanceof Error) {
      return NextResponse.json(
        { error: error.message },
        { status: 400 }
      );
    }
    return NextResponse.json(
      { error: 'Internal Server Error' },
      { status: 500 }
    );
  }
}

async function handlePaymentSuccess(paymentIntent: Stripe.PaymentIntent) {
  // Implement payment success logic
  // e.g., update order status, send confirmation email
}

async function handlePaymentFailure(paymentIntent: Stripe.PaymentIntent) {
  // Implement payment failure logic
  // e.g., update order status, notify customer
}
```

## Subscription Management

### 1. Creating Subscriptions
```typescript
// app/api/create-subscription/route.ts
import { stripe } from '@/config/stripe';
import { NextResponse } from 'next/server';

export async function POST(req: Request) {
  try {
    const { customerId, priceId } = await req.json();

    const subscription = await stripe.subscriptions.create({
      customer: customerId,
      items: [{ price: priceId }],
      payment_behavior: 'default_incomplete',
      payment_settings: { save_default_payment_method: 'on_subscription' },
      expand: ['latest_invoice.payment_intent'],
    });

    return NextResponse.json({
      subscriptionId: subscription.id,
      clientSecret: (
        subscription.latest_invoice as Stripe.Invoice
      ).payment_intent?.client_secret,
    });
  } catch (error) {
    if (error instanceof Error) {
      return NextResponse.json(
        { error: error.message },
        { status: 400 }
      );
    }
    return NextResponse.json(
      { error: 'Internal Server Error' },
      { status: 500 }
    );
  }
}
```

## Customer Management

### 1. Customer Creation
```typescript
// utils/stripe-customer.ts
import { stripe } from '@/config/stripe';

export async function createOrRetrieveCustomer(
  email: string,
  name?: string
) {
  const customers = await stripe.customers.list({
    email,
    limit: 1,
  });

  if (customers.data.length) {
    return customers.data[0].id;
  }

  const customer = await stripe.customers.create({
    email,
    name,
  });

  return customer.id;
}
```

## Error Handling

### 1. Error Types
```typescript
// types/stripe-error.ts
export type StripeErrorResponse = {
  type: 'card_error' | 'validation_error' | 'api_error';
  code?: string;
  message: string;
};

export function handleStripeError(error: any): StripeErrorResponse {
  if (error.type === 'StripeCardError') {
    return {
      type: 'card_error',
      code: error.code,
      message: error.message,
    };
  }

  if (error.type === 'StripeInvalidRequestError') {
    return {
      type: 'validation_error',
      message: 'Invalid request parameters',
    };
  }

  return {
    type: 'api_error',
    message: 'An unexpected error occurred',
  };
}
```

## Testing

### 1. Test Cards
```typescript
// utils/test-cards.ts
export const TEST_CARDS = {
  success: '4242424242424242',
  decline: '4000000000000002',
  insufficient_funds: '4000000000009995',
  requires_3d_secure: '4000000000003220',
};
```

### 2. Test Helpers
```typescript
// utils/test-helpers.ts
export async function createTestPaymentIntent(
  amount: number,
  currency = 'usd'
) {
  return stripe.paymentIntents.create({
    amount,
    currency,
    payment_method_types: ['card'],
    metadata: { test: 'true' },
  });
}
```

## Security Best Practices

1. **Data Handling**
   - Never log or store raw card data
   - Use Stripe Elements for secure input
   - Implement proper data sanitization

2. **API Security**
   - Use HTTPS for all requests
   - Implement proper authentication
   - Validate webhook signatures
   - Use idempotency keys

3. **Error Handling**
   - Implement proper error logging
   - Display user-friendly messages
   - Handle network failures

4. **Testing**
   - Use test API keys
   - Test all error scenarios
   - Verify webhook handling
   - Test 3D Secure flows

Remember:
- Keep Stripe SDK updated
- Monitor Stripe Dashboard
- Implement proper logging
- Follow PCI compliance
- Use Strong Customer Authentication
- Handle asynchronous events properly 