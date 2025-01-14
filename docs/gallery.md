# Prompt Gallery

<div class="gallery-header">
  <div class="search-container">
    <input type="text" class="prompt-search" placeholder="🔍 Search prompts...">
    <div class="search-filters">
      <select class="prompt-sort">
        <option value="popular">Most Used</option>
        <option value="recent">Recently Added</option>
        <option value="rating">Highest Rated</option>
      </select>
    </div>
  </div>
  
  <div class="category-filters">
    <button class="filter-btn active" data-category="all">All Prompts</button>
    <button class="filter-btn" data-category="ai">AI/ML</button>
    <button class="filter-btn" data-category="creative">Creative</button>
    <button class="filter-btn" data-category="technical">Technical</button>
    <button class="filter-btn" data-category="business">Business</button>
    <button class="filter-btn" data-category="academic">Academic</button>
  </div>
</div>

<div class="prompt-gallery">
  <!-- AI Image Generation Prompt -->
  <div class="prompt-card" 
       data-prompt-id="midjourney-1"
       data-categories="ai,creative"
       data-uses="2642837"
       data-rating="4.9"
       data-date="2024-01-15">
    
    <div class="prompt-header">
      <div class="prompt-title-section">
        <h3 class="prompt-title">🎨 Midjourney V5 Style</h3>
        <div class="prompt-author">by @promptmaster</div>
      </div>
      <div class="prompt-stats">
        <span class="stat-item">👁️ 2.6M</span>
        <span class="stat-item">⭐ 4.9</span>
      </div>
    </div>

    <div class="prompt-tags">
      <span class="prompt-tag">AI Art</span>
      <span class="prompt-tag">Midjourney</span>
      <span class="prompt-tag">V5</span>
    </div>

    <div class="prompt-content">
      <div class="prompt-description">
        Generate stunning Midjourney V5 prompts with enhanced photorealistic quality and artistic style.
      </div>
      
      <div class="prompt-template">
        <pre id="midjourney-1-template">A [subject] in the style of [artist/style], [lighting], [composition], [camera settings], [additional details], --ar 16:9 --v 5 --q 2 --style raw</pre>
      </div>
    </div>

    <div class="prompt-actions">
      <button class="action-btn copy-btn" data-clipboard-target="#midjourney-1-template">
        <span class="btn-icon">📋</span>
        <span class="btn-text">Copy Prompt</span>
      </button>
      <button class="action-btn favorite-btn">
        <span class="btn-icon">☆</span>
        <span class="btn-text">Save</span>
      </button>
    </div>
  </div>

  <!-- ChatGPT Code Review Prompt -->
  <div class="prompt-card"
       data-prompt-id="code-review-1"
       data-categories="technical,development"
       data-uses="1688619"
       data-rating="4.8"
       data-date="2024-01-18">
    
    <div class="prompt-header">
      <div class="prompt-title-section">
        <h3 class="prompt-title">💻 Advanced Code Review</h3>
        <div class="prompt-author">by @techexpert</div>
      </div>
      <div class="prompt-stats">
        <span class="stat-item">👁️ 1.6M</span>
        <span class="stat-item">⭐ 4.8</span>
      </div>
    </div>

    <div class="prompt-tags">
      <span class="prompt-tag">Development</span>
      <span class="prompt-tag">Code Review</span>
      <span class="prompt-tag">Best Practices</span>
    </div>

    <div class="prompt-content">
      <div class="prompt-description">
        Get comprehensive code reviews with security analysis, performance optimization, and best practices.
      </div>
      
      <div class="prompt-template">
        <pre id="code-review-1-template">Please review this code with focus on:
1. Security vulnerabilities
2. Performance optimization
3. Code organization
4. Best practices
5. Potential bugs

Code:
```[language]
[paste your code here]
```

Provide specific recommendations for improvement in each category.</pre>
      </div>
    </div>

    <div class="prompt-actions">
      <button class="action-btn copy-btn" data-clipboard-target="#code-review-1-template">
        <span class="btn-icon">📋</span>
        <span class="btn-text">Copy Prompt</span>
      </button>
      <button class="action-btn favorite-btn">
        <span class="btn-icon">☆</span>
        <span class="btn-text">Save</span>
      </button>
    </div>
  </div>

  <!-- Business Analysis Prompt -->
  <div class="prompt-card"
       data-prompt-id="business-analysis-1"
       data-categories="business,analysis"
       data-uses="987654"
       data-rating="4.7"
       data-date="2024-01-20">
    
    <div class="prompt-header">
      <div class="prompt-title-section">
        <h3 class="prompt-title">📊 Market Analysis Framework</h3>
        <div class="prompt-author">by @bizanalyst</div>
      </div>
      <div class="prompt-stats">
        <span class="stat-item">👁️ 987K</span>
        <span class="stat-item">⭐ 4.7</span>
      </div>
    </div>

    <div class="prompt-tags">
      <span class="prompt-tag">Business</span>
      <span class="prompt-tag">Analysis</span>
      <span class="prompt-tag">Strategy</span>
    </div>

    <div class="prompt-content">
      <div class="prompt-description">
        Comprehensive market analysis framework using PESTLE, Porter's Five Forces, and SWOT analysis.
      </div>
      
      <div class="prompt-template">
        <pre id="business-analysis-1-template">Conduct a comprehensive market analysis for [Company/Industry] covering:

1. PESTLE Analysis:
   - Political factors
   - Economic factors
   - Social factors
   - Technological factors
   - Legal factors
   - Environmental factors

2. Porter's Five Forces:
   - Competitive rivalry
   - Supplier power
   - Buyer power
   - Threat of substitution
   - Threat of new entry

3. SWOT Analysis:
   - Strengths
   - Weaknesses
   - Opportunities
   - Threats

Provide actionable insights and strategic recommendations based on the analysis.</pre>
      </div>
    </div>

    <div class="prompt-actions">
      <button class="action-btn copy-btn" data-clipboard-target="#business-analysis-1-template">
        <span class="btn-icon">📋</span>
        <span class="btn-text">Copy Prompt</span>
      </button>
      <button class="action-btn favorite-btn">
        <span class="btn-icon">☆</span>
        <span class="btn-text">Save</span>
      </button>
    </div>
  </div>
</div>

<script>
// Initialize view count formatting
document.querySelectorAll('.stat-item').forEach(stat => {
  if (stat.textContent.includes('M')) {
    const num = parseFloat(stat.textContent.replace(/[^0-9.]/g, ''));
    stat.setAttribute('title', `${(num * 1000000).toLocaleString()} views`);
  } else if (stat.textContent.includes('K')) {
    const num = parseFloat(stat.textContent.replace(/[^0-9.]/g, ''));
    stat.setAttribute('title', `${(num * 1000).toLocaleString()} views`);
  }
});
</script> 