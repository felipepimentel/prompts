// Initialize clipboard.js
document.addEventListener('DOMContentLoaded', function() {
  // Initialize clipboard
  const clipboard = new ClipboardJS('.copy-button', {
    text: function(trigger) {
      return trigger.closest('.prompt-content').querySelector('.prompt-text').textContent;
    }
  });
  
  clipboard.on('success', function(e) {
    const button = e.trigger;
    const originalHTML = button.innerHTML;
    button.classList.add('copy-success');
    button.innerHTML = '<span class="material-icons">check</span>';
    
    setTimeout(() => {
      button.classList.remove('copy-success');
      button.innerHTML = originalHTML;
    }, 2000);
    
    e.clearSelection();
  });
  
  // Search and filter functionality
  const searchInput = document.querySelector('.prompt-search');
  const filterButtons = document.querySelectorAll('.filter-btn');
  const promptCards = document.querySelectorAll('.prompt-card');
  let currentFilter = 'all';
  
  function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
      const later = () => {
        clearTimeout(timeout);
        func(...args);
      };
      clearTimeout(timeout);
      timeout = setTimeout(later, wait);
    };
  }
  
  function filterPrompts() {
    const searchTerm = searchInput.value.toLowerCase();
    
    promptCards.forEach(card => {
      const title = card.querySelector('.prompt-title').textContent.toLowerCase();
      const description = card.querySelector('.prompt-description').textContent.toLowerCase();
      const tags = Array.from(card.querySelectorAll('.prompt-tag')).map(tag => tag.textContent.toLowerCase());
      const category = card.dataset.category;
      const model = card.dataset.model;
      
      const matchesSearch = !searchTerm || 
                          title.includes(searchTerm) || 
                          description.includes(searchTerm) || 
                          tags.some(tag => tag.includes(searchTerm));
                          
      const matchesFilter = currentFilter === 'all' || 
                           (currentFilter.startsWith('category-') && category === currentFilter.replace('category-', '')) ||
                           (currentFilter.startsWith('model-') && model === currentFilter.replace('model-', ''));
      
      const shouldShow = matchesSearch && matchesFilter;
      
      card.style.display = shouldShow ? 'block' : 'none';
      card.style.opacity = shouldShow ? '1' : '0';
      card.style.transform = shouldShow ? 'translateY(0)' : 'translateY(20px)';
    });
    
    // Update category sections visibility
    document.querySelectorAll('.category-section').forEach(section => {
      const hasVisibleCards = Array.from(section.querySelectorAll('.prompt-card'))
        .some(card => card.style.display !== 'none');
      section.style.display = hasVisibleCards ? 'block' : 'none';
    });
  }
  
  const debouncedFilter = debounce(filterPrompts, 300);
  
  if (searchInput) {
    searchInput.addEventListener('input', debouncedFilter);
  }
  
  filterButtons.forEach(button => {
    button.addEventListener('click', () => {
      filterButtons.forEach(btn => btn.classList.remove('active'));
      button.classList.add('active');
      currentFilter = button.dataset.filter;
      filterPrompts();
    });
  });
  
  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });
  
  // Lazy loading for prompt cards
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, {
      rootMargin: '50px',
      threshold: 0.1
    });
    
    promptCards.forEach(card => {
      observer.observe(card);
    });
  } else {
    promptCards.forEach(card => {
      card.classList.add('visible');
    });
  }

  // Handle prompt section tabs
  document.querySelectorAll('.prompt-section-tab').forEach(tab => {
    tab.addEventListener('click', function() {
      const content = this.closest('.prompt-content');
      const allTabs = content.querySelectorAll('.prompt-section-tab');
      const allSections = content.querySelectorAll('.section-content');
      const targetSection = content.querySelector(`.section-${this.dataset.section}`);
      
      // Update active states
      allTabs.forEach(t => t.classList.remove('active'));
      allSections.forEach(s => s.style.display = 'none');
      
      this.classList.add('active');
      if (targetSection) {
        targetSection.style.display = 'block';
      }
    });
  });
});

