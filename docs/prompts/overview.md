# Prompt Gallery

<div class="prompt-filters">
  <input type="text" class="prompt-search" placeholder="Search prompts...">
  
  <div class="filter-buttons">
    <button class="filter-btn active" data-category="all">All</button>
    <button class="filter-btn" data-category="academic">Academic</button>
    <button class="filter-btn" data-category="creative">Creative</button>
    <button class="filter-btn" data-category="technical">Technical</button>
  </div>

  <select class="prompt-sort">
    <option value="popular">Most Popular</option>
    <option value="recent">Most Recent</option>
    <option value="name">Name (A-Z)</option>
  </select>
</div>

<div class="prompt-gallery">
  <!-- Academic Writing Prompt -->
  <div class="prompt-card" 
       data-prompt-id="academic-writing-1"
       data-categories="academic,writing"
       data-popular="95"
       data-recent="2024-01-20"
       data-name="Academic Writing Structure">
    
    <div class="prompt-header">
      <h3 class="prompt-title">📝 Academic Writing Structure</h3>
      <div class="prompt-tags">
        <span class="prompt-tag">Academic</span>
        <span class="prompt-tag">Writing</span>
      </div>
    </div>

    <div class="prompt-actions">
      <button class="prompt-action-btn copy-btn" data-clipboard-target="#academic-writing-1-template">
        📋
        <span class="copy-tooltip">Copied!</span>
      </button>
      <button class="prompt-action-btn favorite-btn">☆</button>
    </div>

    <div class="prompt-content">
      <div class="prompt-description">
        A comprehensive prompt for structuring academic papers and research articles.
      </div>
      
      <div class="prompt-template">
        <pre id="academic-writing-1-template">Please help me structure an academic paper with the following components:

Topic: [Your Research Topic]
Type: [Research Paper/Review Article/Case Study]
Target Journal: [Journal Name]
Word Limit: [Number] words

Please provide:
1. A clear structure for the paper
2. Key sections with brief descriptions
3. Guidelines for content in each section
4. Suggestions for maintaining academic tone
5. Tips for effective argumentation</pre>
      </div>
    </div>

    <div class="prompt-metadata">
      <div class="prompt-stats">👥 Used 2.5k times</div>
      <div class="prompt-rating">⭐ 4.8/5</div>
    </div>
  </div>

  <!-- Creative Writing Prompt -->
  <div class="prompt-card"
       data-prompt-id="creative-writing-1"
       data-categories="creative,writing"
       data-popular="87"
       data-recent="2024-01-19"
       data-name="Creative Story Generator">
    
    <div class="prompt-header">
      <h3 class="prompt-title">✨ Creative Story Generator</h3>
      <div class="prompt-tags">
        <span class="prompt-tag">Creative</span>
        <span class="prompt-tag">Writing</span>
      </div>
    </div>

    <div class="prompt-actions">
      <button class="prompt-action-btn copy-btn" data-clipboard-target="#creative-writing-1-template">
        📋
        <span class="copy-tooltip">Copied!</span>
      </button>
      <button class="prompt-action-btn favorite-btn">☆</button>
    </div>

    <div class="prompt-content">
      <div class="prompt-description">
        Generate creative story ideas with detailed character and plot development.
      </div>
      
      <div class="prompt-template">
        <pre id="creative-writing-1-template">Help me create a story with these elements:

Genre: [Fantasy/Sci-Fi/Mystery/etc.]
Main Character: [Brief description]
Setting: [Time and place]
Theme: [Central theme]
Length: [Short story/Novel/etc.]

Please provide:
1. Story outline
2. Character development arc
3. Key plot points
4. Conflict and resolution ideas
5. Unique story elements</pre>
      </div>
    </div>

    <div class="prompt-metadata">
      <div class="prompt-stats">👥 Used 1.8k times</div>
      <div class="prompt-rating">⭐ 4.7/5</div>
    </div>
  </div>

  <!-- Technical Documentation Prompt -->
  <div class="prompt-card"
       data-prompt-id="technical-doc-1"
       data-categories="technical,documentation"
       data-popular="92"
       data-recent="2024-01-18"
       data-name="API Documentation">
    
    <div class="prompt-header">
      <h3 class="prompt-title">🔧 API Documentation</h3>
      <div class="prompt-tags">
        <span class="prompt-tag">Technical</span>
        <span class="prompt-tag">Documentation</span>
      </div>
    </div>

    <div class="prompt-actions">
      <button class="prompt-action-btn copy-btn" data-clipboard-target="#technical-doc-1-template">
        📋
        <span class="copy-tooltip">Copied!</span>
      </button>
      <button class="prompt-action-btn favorite-btn">☆</button>
    </div>

    <div class="prompt-content">
      <div class="prompt-description">
        Create comprehensive API documentation with examples and best practices.
      </div>
      
      <div class="prompt-template">
        <pre id="technical-doc-1-template">Help me document an API endpoint:

Endpoint: [API endpoint path]
Method: [GET/POST/PUT/DELETE]
Authentication: [Auth method]
Request Format: [JSON/XML/etc.]
Response Format: [JSON/XML/etc.]

Please provide:
1. Endpoint description
2. Request parameters
3. Response structure
4. Example requests/responses
5. Error handling
6. Usage guidelines</pre>
      </div>
    </div>

    <div class="prompt-metadata">
      <div class="prompt-stats">👥 Used 3.2k times</div>
      <div class="prompt-rating">⭐ 4.9/5</div>
    </div>
  </div>
</div>

## Using the Gallery

1. **Search**: Use the search bar to find specific prompts
2. **Filter**: Click on category buttons to filter prompts
3. **Sort**: Use the dropdown to sort prompts by popularity, recency, or name
4. **Copy**: Click the clipboard icon to copy a prompt
5. **Favorite**: Click the star icon to save prompts for later

## Contributing

Have a great prompt to share? Check out our [Contributing Guide](../contributing.md) to learn how to add your prompts to the collection. 