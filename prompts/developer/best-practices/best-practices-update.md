---
title: "Best Practices Update Guide"
path: "developer/best-practices/best-practices-update"
tags: ["best-practices", "security", "performance", "updates"]
description: "A comprehensive guide for staying current with language and framework best practices, security updates, and performance improvements"
prompt_type: "Update Framework"
---

<purpose>
To provide a structured approach for reviewing and implementing the latest best practices, security updates, and performance improvements for a specific technology stack.
</purpose>

<context>
Use this template when conducting periodic reviews of your technology stack to ensure alignment with current best practices and security standards.
</context>

<instructions>
Provide the following update information:

1. Technology Stack
   - Core Components
     * Language version
     * Framework version
     * Key libraries
     * Runtime environment

   - Update Scope
     * Time period
     * Focus areas
     * Priority levels
     * Impact assessment

2. Security Updates
   - Vulnerabilities
     * New discoveries
     * Patch requirements
     * Mitigation strategies
     * Security advisories

   - Best Practices
     * Authentication updates
     * Authorization patterns
     * Data protection
     * API security

3. Performance Updates
   - Optimization Techniques
     * New methods
     * Improved patterns
     * Deprecated approaches
     * Benchmarking results

   - Tools and Libraries
     * New releases
     * Performance features
     * Migration paths
     * Compatibility notes

4. Implementation Guide
   - Update Strategy
     * Priority order
     * Breaking changes
     * Migration steps
     * Testing approach

   - Maintenance Plan
     * Update frequency
     * Monitoring needs
     * Documentation updates
     * Team training

</instructions>

<variables>
- technology_stack: Language and framework details
- time_period: Update review period
- priority_level: Update importance
- impact_scope: Affected components
</variables>

<examples>
Example 1:
Input: Node.js/Express best practices update
Output:
```markdown
# Node.js/Express Best Practices Update 2024

## Technology Overview
- **Node.js Version:** 20.x LTS
- **Express Version:** 4.18.x
- **Review Period:** Q1 2024
- **Focus:** Security & Performance

## Security Updates

### 1. Authentication Practices
#### JWT Handling Updates
```javascript
// Old approach (deprecated)
const token = jwt.sign(payload, 'secret');

// Current best practice
const token = jwt.sign(payload, process.env.JWT_SECRET, {
  algorithm: 'RS256',
  expiresIn: '1h',
  notBefore: '0s',
  audience: process.env.JWT_AUDIENCE,
  issuer: process.env.JWT_ISSUER,
  jwtid: uuidv4()
});

// Token verification
const verifyToken = async (token) => {
  try {
    const decoded = await jwt.verify(token, process.env.JWT_PUBLIC_KEY, {
      algorithms: ['RS256'],
      audience: process.env.JWT_AUDIENCE,
      issuer: process.env.JWT_ISSUER
    });
    return decoded;
  } catch (error) {
    throw new TokenVerificationError(error.message);
  }
};
```

### 2. Security Headers
```javascript
// Updated security headers configuration
const helmet = require('helmet');

app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      scriptSrc: ["'self'", "'wasm-unsafe-eval'"],
      styleSrc: ["'self'", "'unsafe-inline'"],
      imgSrc: ["'self'", "data:", "https:"],
      connectSrc: ["'self'", "https://api.example.com"],
      frameSrc: ["'none'"],
      objectSrc: ["'none'"]
    }
  },
  crossOriginEmbedderPolicy: true,
  crossOriginOpenerPolicy: true,
  crossOriginResourcePolicy: { policy: "same-site" },
  dnsPrefetchControl: true,
  frameguard: { action: "deny" },
  hsts: {
    maxAge: 31536000,
    includeSubDomains: true,
    preload: true
  },
  referrerPolicy: { policy: "strict-origin-when-cross-origin" }
}));
```

## Performance Improvements

### 1. Async Operations
```javascript
// Old approach
const processItems = async (items) => {
  for (const item of items) {
    await processItem(item);
  }
};

// Current best practice
const processItems = async (items) => {
  const batchSize = 5;
  for (let i = 0; i < items.length; i += batchSize) {
    const batch = items.slice(i, i + batchSize);
    await Promise.all(batch.map(processItem));
  }
};

// With error handling and rate limiting
const processItemsWithRetry = async (items) => {
  const limiter = new RateLimit({
    maxConcurrent: 5,
    minTime: 100
  });

  const results = await Promise.allSettled(
    items.map(item => 
      limiter.schedule(() => processWithRetry(item))
    )
  );

  return results.map((result, index) => ({
    item: items[index],
    status: result.status,
    value: result.value,
    error: result.reason
  }));
};
```

### 2. Memory Management
```javascript
// Stream processing for large datasets
const processLargeFile = async (filePath) => {
  const readable = createReadStream(filePath);
  const parser = csv.parse({
    headers: true,
    skipEmptyLines: true
  });

  const transform = new Transform({
    objectMode: true,
    transform(chunk, encoding, callback) {
      // Process chunk in memory-efficient way
      const processed = processChunk(chunk);
      callback(null, processed);
    }
  });

  return new Promise((resolve, reject) => {
    pipeline(
      readable,
      parser,
      transform,
      createWriteStream('output.csv'),
      (error) => {
        if (error) reject(error);
        else resolve();
      }
    );
  });
};
```

## Deprecated Practices

### Security
1. **Password Hashing**
   ```javascript
   // Deprecated
   const crypto = require('crypto');
   const hash = crypto.createHash('md5').update(password).digest('hex');

   // Current best practice
   const bcrypt = require('bcrypt');
   const hash = await bcrypt.hash(password, 12);
   ```

2. **Session Management**
   ```javascript
   // Deprecated
   app.use(session({
     secret: 'secret',
     resave: true,
     saveUninitialized: true
   }));

   // Current best practice
   app.use(session({
     secret: process.env.SESSION_SECRET,
     resave: false,
     saveUninitialized: false,
     cookie: {
       secure: true,
       httpOnly: true,
       sameSite: 'strict',
       maxAge: 3600000
     },
     store: new RedisStore({
       client: redisClient,
       prefix: 'session:',
       ttl: 3600
     })
   }));
   ```

## Implementation Plan

### Immediate Updates
1. Update security headers
2. Implement new JWT practices
3. Update password hashing
4. Add rate limiting

### Scheduled Updates
1. Migrate session management
2. Implement streaming for large operations
3. Update async patterns
4. Add memory management

### Monitoring
1. Add security logging
2. Implement performance metrics
3. Set up alerting
4. Create dashboards
```

Example 2:
Input: Python/Django best practices update
Output:
```markdown
# Python/Django Best Practices Update 2024

## Technology Overview
- **Python Version:** 3.12
- **Django Version:** 5.0
- **Review Period:** Q1 2024
- **Focus:** Security & Performance

## Security Updates

### 1. Password Validation
```python
# Updated password validation settings
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        'OPTIONS': {
            'user_attributes': ('username', 'email', 'first_name', 'last_name'),
            'max_similarity': 0.7,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 12,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
    {
        'NAME': 'myapp.validators.PasswordStrengthValidator',
        'OPTIONS': {
            'min_length': 12,
            'min_uppercase': 1,
            'min_lowercase': 1,
            'min_numbers': 1,
            'min_special': 1,
        }
    }
]
```

### 2. Security Middleware
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',
    'django_permissions_policy.PermissionsPolicyMiddleware',
]

# Security settings
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_REFERRER_POLICY = 'strict-origin-when-cross-origin'
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# CSP settings
CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'",)
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'")
CSP_IMG_SRC = ("'self'", "data:", "https:")
CSP_FONT_SRC = ("'self'", "https://fonts.gstatic.com")
```

## Performance Improvements

### 1. Database Optimization
```python
# Model optimization
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, db_index=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['created_at', 'status']),
            models.Index(fields=['author', 'status']),
        ]
        
    def save(self, *args, **kwargs):
        # Optimize save operations
        if not self.pk:
            # Only for new instances
            super().save(*args, **kwargs)
        else:
            # Update specific fields only
            update_fields = kwargs.get('update_fields', None)
            if update_fields is None:
                # Determine changed fields
                changed_fields = []
                for field in self._meta.fields:
                    if field.name != 'updated_at' and \
                       getattr(self, field.name) != getattr(self.__class__.objects.get(pk=self.pk), field.name):
                        changed_fields.append(field.name)
                kwargs['update_fields'] = changed_fields + ['updated_at']
            super().save(*args, **kwargs)

# Query optimization
from django.db.models import Prefetch

def get_articles():
    return Article.objects.select_related('author')\
                         .prefetch_related(
                             Prefetch('comments', 
                                     queryset=Comment.objects.select_related('user'))
                         )\
                         .filter(status='published')\
                         .defer('content')\
                         .only('title', 'author__username', 'created_at')
```

### 2. Caching Implementation
```python
# Cache settings
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PARSER_CLASS': 'redis.connection.HiredisParser',
            'SOCKET_TIMEOUT': 5,
            'SOCKET_CONNECT_TIMEOUT': 5,
            'CONNECTION_POOL_CLASS': 'redis.connection.BlockingConnectionPool',
            'CONNECTION_POOL_CLASS_KWARGS': {
                'max_connections': 50,
                'timeout': 20,
            },
            'MAX_CONNECTIONS': 1000,
            'RETRY_ON_TIMEOUT': True,
        },
        'KEY_PREFIX': 'myapp',
        'TIMEOUT': 300,
    }
}

# View caching
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

@cache_page(60 * 15)  # 15 minutes
@vary_on_cookie
def article_list(request):
    articles = get_articles()
    return render(request, 'articles/list.html', {'articles': articles})

# Template fragment caching
{% load cache %}
{% cache 300 sidebar request.user.id %}
    {# sidebar content #}
{% endcache %}
```

## Deprecated Practices

### Security
1. **User Authentication**
   ```python
   # Deprecated
   from django.contrib.auth.models import User

   # Current best practice
   from django.contrib.auth import get_user_model
   User = get_user_model()
   ```

2. **Form Processing**
   ```python
   # Deprecated
   if request.method == 'POST':
       form = MyForm(request.POST)
       if form.is_valid():
           # process form

   # Current best practice
   from django.views.generic.edit import FormView

   class MyFormView(FormView):
       form_class = MyForm
       template_name = 'form.html'
       success_url = '/success/'

       def form_valid(self, form):
           # Process valid form
           return super().form_valid(form)
   ```

## Implementation Plan

### Immediate Updates
1. Update security middleware
2. Implement new password validation
3. Update authentication practices
4. Add CSP headers

### Scheduled Updates
1. Optimize database queries
2. Implement caching strategy
3. Update form handling
4. Add monitoring

### Monitoring
1. Set up logging
2. Configure error tracking
3. Implement APM
4. Create dashboards
```

</examples>

<notes>
- Review regularly
- Test thoroughly
- Document changes
- Train team members
- Monitor impacts
- Plan migrations
- Consider compatibility
- Update gradually
</notes> 