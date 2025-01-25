function initializeGalleryFunctionality() {
    // Elements
    const searchInput = document.querySelector('.search-box input');
    const filterButtons = document.querySelectorAll('.filter-btn');
    const clearFiltersButton = document.querySelector('.clear-filters');
    const promptCards = document.querySelectorAll('.prompt-card');
    
    // Create toast container
    const toastContainer = document.createElement('div');
    toastContainer.className = 'toast-container';
    document.body.appendChild(toastContainer);
    
    // Function to show toast
    function showToast(message, duration = 2000) {
        const toast = document.createElement('div');
        toast.className = 'toast';
        toast.innerHTML = `
            <span class="material-icons">check_circle</span>
            <span>${message}</span>
        `;
        
        toastContainer.appendChild(toast);
        
        // Trigger reflow to enable animation
        toast.offsetHeight;
        
        // Show toast
        requestAnimationFrame(() => {
            toast.classList.add('show');
        });
        
        // Remove toast after duration
        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => {
                toastContainer.removeChild(toast);
            }, 300); // Wait for fade out animation
        }, duration);
    }
    
    // State
    let activeFilters = {
        category: 'all',
        model: 'all'
    };
    
    // Search functionality
    searchInput.addEventListener('input', function(e) {
        const searchTerm = e.target.value.toLowerCase();
        filterCards();
    });
    
    // Filter buttons
    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            const filterGroup = this.closest('.filter-group');
            const filterType = filterGroup.querySelector('h3').textContent.toLowerCase() === 'categorias' ? 'category' : 'model';
            
            // Remove active class from other buttons in the same group
            filterGroup.querySelectorAll('.filter-btn').forEach(btn => {
                btn.classList.remove('active');
            });
            
            // Add active class to clicked button
            this.classList.add('active');
            
            // Update active filters
            activeFilters[filterType] = this.textContent.toLowerCase();
            
            filterCards();
        });
    });
    
    // Clear filters
    clearFiltersButton.addEventListener('click', function() {
        // Reset search
        searchInput.value = '';
        
        // Reset filter buttons
        filterButtons.forEach(button => {
            button.classList.remove('active');
            if (button.parentElement.id === 'category-filters' && button.textContent.toLowerCase() === 'geral') {
                button.classList.add('active');
            }
        });
        
        // Reset active filters
        activeFilters = {
            category: 'geral',
            model: 'all'
        };
        
        filterCards();
    });
    
    // Filter cards based on current state
    function filterCards() {
        const searchTerm = searchInput.value.toLowerCase();
        
        promptCards.forEach(card => {
            const cardCategory = card.dataset.category;
            const cardModel = card.dataset.model;
            const cardTitle = card.querySelector('h3').textContent.toLowerCase();
            const cardDescription = card.querySelector('.description').textContent.toLowerCase();
            const cardTags = Array.from(card.querySelectorAll('.tag')).map(tag => tag.textContent.toLowerCase());
            
            // Check if card matches search term
            const matchesSearch = searchTerm === '' || 
                                cardTitle.includes(searchTerm) || 
                                cardDescription.includes(searchTerm) ||
                                cardTags.some(tag => tag.includes(searchTerm));
            
            // Check if card matches active filters
            const matchesCategory = activeFilters.category === 'all' || cardCategory === activeFilters.category;
            const matchesModel = activeFilters.model === 'all' || cardModel === activeFilters.model;
            
            // Show/hide card
            if (matchesSearch && matchesCategory && matchesModel) {
                card.style.display = '';
            } else {
                card.style.display = 'none';
            }
        });
    }
    
    // Copy button functionality
    document.querySelectorAll('.copy-btn').forEach(button => {
        button.addEventListener('click', function() {
            const card = this.closest('.prompt-card');
            const promptContent = card.querySelector('.prompt-content')?.textContent || '';
            
            navigator.clipboard.writeText(promptContent).then(() => {
                // Visual feedback on button
                const icon = this.querySelector('.material-icons');
                const originalText = icon.textContent;
                icon.textContent = 'check';
                setTimeout(() => {
                    icon.textContent = originalText;
                }, 2000);
                
                // Show toast notification
                showToast('Prompt copiado com sucesso!');
            }).catch(() => {
                showToast('Erro ao copiar o prompt', 3000);
            });
        });
    });
    
    // Expand button functionality
    document.querySelectorAll('.expand-btn').forEach(button => {
        button.addEventListener('click', function() {
            const card = this.closest('.prompt-card');
            card.classList.toggle('expanded');
            
            const icon = this.querySelector('.material-icons');
            icon.textContent = card.classList.contains('expanded') ? 'close_fullscreen' : 'open_in_full';
        });
    });
} 