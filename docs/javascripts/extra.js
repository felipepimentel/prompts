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
  const sortSelect = document.querySelector('.prompt-sort');
  const filterBtns = document.querySelectorAll('.filter-btn');
  const promptCards = document.querySelectorAll('.prompt-card');
  let currentFilter = 'all';

  // Search functionality
  searchInput.addEventListener('input', filterCards);

  // Sort functionality
  sortSelect.addEventListener('change', filterCards);

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
    const sortBy = sortSelect.value;
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

    // Sort visible cards
    if (sortBy === 'name') {
      visibleCards.sort((a, b) => {
        const titleA = a.querySelector('.prompt-title').textContent;
        const titleB = b.querySelector('.prompt-title').textContent;
        return titleA.localeCompare(titleB);
      });
    } else if (sortBy === 'category') {
      visibleCards.sort((a, b) => {
        const catA = a.dataset.categories.split(',')[0];
        const catB = b.dataset.categories.split(',')[0];
        return catA.localeCompare(catB);
      });
    }

    // Reorder cards in DOM
    const gallery = document.querySelector('.prompt-gallery');
    visibleCards.forEach(card => gallery.appendChild(card));

    // Update pagination
    currentPage = 1;
    totalPages = Math.ceil(visibleCards.length / itemsPerPage);
    showPage(1);
  }
}); 