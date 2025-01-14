# Prompt Gallery

<div class="gallery-header">
  <div class="search-container">
    <input type="text" class="prompt-search" placeholder="🔍 Search prompts...">
    <div class="search-filters">
      <select class="prompt-sort">
        <option value="category">Category</option>
        <option value="name">Name</option>
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
  <div class="prompt-card" 
       data-prompt-id="midjourney-1"
       data-categories="ai,creative">
    <div class="prompt-header">
      <h3 class="prompt-title">🎨 Midjourney V5 Style</h3>
    </div>

    <div class="prompt-tags">
      <span class="prompt-tag">AI Art</span>
      <span class="prompt-tag">Midjourney</span>
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
        <span class="btn-text">Copy</span>
      </button>
    </div>
  </div>
</div>

<div class="pagination">
  <button class="page-btn" data-page="prev">← Previous</button>
  <span class="page-info">Page <span class="current-page">1</span> of <span class="total-pages">10</span></span>
  <button class="page-btn" data-page="next">Next →</button>
</div>

<script>
// Initialize pagination
const itemsPerPage = 9;
const promptCards = document.querySelectorAll('.prompt-card');
const totalPages = Math.ceil(promptCards.length / itemsPerPage);
let currentPage = 1;

function showPage(page) {
  const start = (page - 1) * itemsPerPage;
  const end = start + itemsPerPage;
  
  promptCards.forEach((card, index) => {
    card.style.display = (index >= start && index < end) ? 'flex' : 'none';
  });
  
  document.querySelector('.current-page').textContent = page;
  document.querySelector('.total-pages').textContent = totalPages;
}

document.querySelectorAll('.page-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    if (btn.dataset.page === 'prev' && currentPage > 1) {
      currentPage--;
    } else if (btn.dataset.page === 'next' && currentPage < totalPages) {
      currentPage++;
    }
    showPage(currentPage);
  });
});

// Initialize first page
showPage(1);
</script> 