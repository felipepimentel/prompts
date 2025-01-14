// Initialize clipboard
new ClipboardJS('.copy-btn').on('success', function(e) {
  const btn = e.trigger;
  const originalText = btn.innerHTML;
  btn.innerHTML = '<span class="btn-icon">✓</span><span class="btn-text">Copied!</span>';
  setTimeout(() => {
    btn.innerHTML = originalText;
  }, 2000);
});

// Search and filter functionality
document.addEventListener('DOMContentLoaded', function() {
  const searchInput = document.querySelector('.prompt-search');
  const filterBtns = document.querySelectorAll('.filter-btn');
  const promptCards = document.querySelectorAll('.prompt-card');
  let currentFilter = 'all';

  // Search functionality
  searchInput.addEventListener('input', filterCards);

  // Filter buttons
  filterBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentFilter = btn.dataset.category;
      filterCards();
    });
  });

  function filterCards() {
    const searchTerm = searchInput.value.toLowerCase();
    let visibleCards = [];

    promptCards.forEach(card => {
      const title = card.querySelector('.prompt-title').textContent.toLowerCase();
      const description = card.querySelector('.prompt-description').textContent.toLowerCase();
      const categories = card.dataset.categories.split(',');
      const template = card.querySelector('.prompt-template').textContent.toLowerCase();
      
      const matchesSearch = title.includes(searchTerm) || 
                           description.includes(searchTerm) || 
                           template.includes(searchTerm);
      
      const matchesFilter = currentFilter === 'all' || categories.includes(currentFilter);

      if (matchesSearch && matchesFilter) {
        card.style.display = 'flex';
        visibleCards.push(card);
      } else {
        card.style.display = 'none';
      }
    });

    // Update pagination
    currentPage = 1;
    totalPages = Math.ceil(visibleCards.length / itemsPerPage);
    showPage(1);
  }

  // Initialize pagination
  const itemsPerPage = 9;
  let currentPage = 1;
  let totalPages = Math.ceil(promptCards.length / itemsPerPage);

  function showPage(page) {
    const start = (page - 1) * itemsPerPage;
    const end = start + itemsPerPage;
    
    Array.from(promptCards).forEach((card, index) => {
      if (card.style.display !== 'none') {
        const shouldShow = index >= start && index < end;
        card.style.display = shouldShow ? 'flex' : 'none';
      }
    });
    
    document.querySelector('.current-page').textContent = page;
    document.querySelector('.total-pages').textContent = totalPages;
    
    // Update button states
    document.querySelector('[data-page="prev"]').disabled = page === 1;
    document.querySelector('[data-page="next"]').disabled = page === totalPages;
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
}); 