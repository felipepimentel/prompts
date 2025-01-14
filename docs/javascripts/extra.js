document.addEventListener('DOMContentLoaded', function() {
  // Initialize clipboard.js
  const clipboard = new ClipboardJS('.copy-btn');
  
  clipboard.on('success', function(e) {
    const tooltip = e.trigger.querySelector('.copy-tooltip');
    tooltip.classList.add('visible');
    setTimeout(() => {
      tooltip.classList.remove('visible');
    }, 2000);
    e.clearSelection();
  });

  // Initialize favorites system
  const favorites = JSON.parse(localStorage.getItem('prompt-favorites') || '{}');
  
  document.querySelectorAll('.favorite-btn').forEach(btn => {
    const promptId = btn.closest('.prompt-card').dataset.promptId;
    if (favorites[promptId]) {
      btn.classList.add('active');
      btn.innerHTML = '★';
    }
    
    btn.addEventListener('click', () => {
      btn.classList.toggle('active');
      btn.innerHTML = btn.classList.contains('active') ? '★' : '☆';
      favorites[promptId] = btn.classList.contains('active');
      localStorage.setItem('prompt-favorites', JSON.stringify(favorites));
    });
  });

  // Initialize filters
  const filterButtons = document.querySelectorAll('.filter-btn');
  filterButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      filterButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      
      const category = btn.dataset.category;
      document.querySelectorAll('.prompt-card').forEach(card => {
        if (category === 'all' || card.dataset.categories.includes(category)) {
          card.style.display = 'block';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });

  // Initialize search
  const searchInput = document.querySelector('.prompt-search');
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      const searchTerm = e.target.value.toLowerCase();
      document.querySelectorAll('.prompt-card').forEach(card => {
        const content = card.textContent.toLowerCase();
        const shouldShow = content.includes(searchTerm);
        card.style.display = shouldShow ? 'block' : 'none';
      });
    });
  }

  // Initialize sorting
  const sortSelect = document.querySelector('.prompt-sort');
  if (sortSelect) {
    sortSelect.addEventListener('change', (e) => {
      const cards = Array.from(document.querySelectorAll('.prompt-card'));
      const sortedCards = cards.sort((a, b) => {
        const valueA = a.dataset[e.target.value];
        const valueB = b.dataset[e.target.value];
        
        if (e.target.value === 'name') {
          return valueA.localeCompare(valueB);
        }
        return Number(valueB) - Number(valueA);
      });
      
      const container = document.querySelector('.prompt-gallery');
      sortedCards.forEach(card => container.appendChild(card));
    });
  }
}); 