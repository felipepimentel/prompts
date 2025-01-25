document.addEventListener('DOMContentLoaded', async function() {
    try {
        // Carregar dados da galeria
        const response = await fetch('/assets/data/gallery.json');
        const galleryData = await response.json();
        
        // Adicionar filtros dinamicamente
        const filterContainer = document.getElementById('categoryFilters');
        galleryData.categories.forEach(category => {
            const button = document.createElement('button');
            button.className = 'filter-btn';
            button.setAttribute('data-filter', category.toLowerCase());
            button.textContent = category;
            filterContainer.appendChild(button);
        });

        // Renderizar cards
        const gallery = document.querySelector('.prompt-gallery');
        
        function createCard(prompt) {
            return `
                <div class="prompt-card" data-category="${prompt.category.toLowerCase()}" data-model="${prompt.model}">
                    <div class="prompt-header">
                        <div class="prompt-meta">
                            <span class="prompt-category">${prompt.category}</span>
                            <span class="prompt-model">${prompt.model}</span>
                        </div>
                        <h3 class="prompt-title">${prompt.title}</h3>
                        <p class="prompt-description">${prompt.description}</p>
                        <div class="prompt-tags">
                            ${prompt.tags.map(tag => `<span class="prompt-tag">${tag}</span>`).join('')}
                        </div>
                    </div>
                    <div class="prompt-content">
                        <pre class="prompt-text">${prompt.content}</pre>
                        <button class="copy-button" title="Copiar prompt">
                            <span class="material-icons">content_copy</span>
                        </button>
                    </div>
                    <div class="prompt-footer">
                        <span class="prompt-version">v${prompt.version}</span>
                        <span class="prompt-date">${prompt.date}</span>
                    </div>
                </div>
            `;
        }

        function renderCards(prompts) {
            gallery.innerHTML = prompts.map(createCard).join('');
            setupCopyButtons();
        }

        // Renderizar cards iniciais
        renderCards(galleryData.prompts);

        // Configurar filtros
        const filterButtons = document.querySelectorAll('.filter-btn');
        filterButtons.forEach(button => {
            button.addEventListener('click', () => {
                const filter = button.getAttribute('data-filter');
                
                // Atualizar estado ativo dos botões
                filterButtons.forEach(btn => btn.classList.remove('active'));
                button.classList.add('active');
                
                // Filtrar cards
                const filteredPrompts = filter === 'all' 
                    ? galleryData.prompts 
                    : galleryData.prompts.filter(p => p.category.toLowerCase() === filter);
                
                renderCards(filteredPrompts);
            });
        });

        // Configurar busca
        const searchInput = document.querySelector('.prompt-search');
        searchInput.addEventListener('input', (e) => {
            const searchTerm = e.target.value.toLowerCase();
            const filteredPrompts = galleryData.prompts.filter(prompt => {
                const activeFilter = document.querySelector('.filter-btn.active').getAttribute('data-filter');
                const matchesCategory = activeFilter === 'all' || prompt.category.toLowerCase() === activeFilter;
                
                return matchesCategory && (
                    prompt.title.toLowerCase().includes(searchTerm) ||
                    prompt.description.toLowerCase().includes(searchTerm) ||
                    prompt.tags.some(tag => tag.toLowerCase().includes(searchTerm)) ||
                    prompt.content.toLowerCase().includes(searchTerm)
                );
            });
            
            renderCards(filteredPrompts);
        });

    } catch (error) {
        console.error('Erro ao carregar dados da galeria:', error);
    }
});

// Função para copiar o conteúdo do prompt
function setupCopyButtons() {
    document.querySelectorAll('.copy-button').forEach(button => {
        button.addEventListener('click', async () => {
            const card = button.closest('.prompt-card');
            const promptText = card.querySelector('.prompt-text').textContent;
            
            try {
                await navigator.clipboard.writeText(promptText);
                const icon = button.querySelector('.material-icons');
                const originalText = icon.textContent;
                
                // Feedback visual
                button.classList.add('copied');
                icon.textContent = 'check';
                
                // Reverter após 2 segundos
                setTimeout(() => {
                    button.classList.remove('copied');
                    icon.textContent = originalText;
                }, 2000);
            } catch (err) {
                console.error('Erro ao copiar:', err);
            }
        });
    });
}

// Função para expandir o card
function expandCard(card) {
    const modal = document.createElement('div');
    modal.className = 'prompt-modal';
    
    const modalContent = document.createElement('div');
    modalContent.className = 'prompt-modal-content';
    
    // Copiar apenas o conteúdo relevante para o modal
    const title = card.querySelector('.prompt-title').cloneNode(true);
    const description = card.querySelector('.prompt-description').cloneNode(true);
    const tags = card.querySelector('.prompt-tags').cloneNode(true);
    const content = card.querySelector('.prompt-content').cloneNode(true);
    
    modalContent.appendChild(title);
    modalContent.appendChild(description);
    modalContent.appendChild(tags);
    modalContent.appendChild(content);
    
    const closeButton = document.createElement('button');
    closeButton.className = 'modal-close';
    closeButton.innerHTML = '<span class="material-icons">close</span>';
    modalContent.appendChild(closeButton);
    
    modal.appendChild(modalContent);
    document.body.appendChild(modal);
    
    setTimeout(() => modal.classList.add('active'), 10);
    
    closeButton.onclick = () => {
        modal.classList.remove('active');
        setTimeout(() => modal.remove(), 300);
    };
    
    modal.onclick = (e) => {
        if (e.target === modal) {
            modal.classList.remove('active');
            setTimeout(() => modal.remove(), 300);
        }
    };
}

// Estado dos filtros
let activeFilters = new Set();
let searchQuery = '';

// Função para filtrar cards
function filterCards() {
    const cards = document.querySelectorAll('.prompt-card');
    const query = searchQuery.toLowerCase();

    cards.forEach(card => {
        const title = card.querySelector('.prompt-title').textContent.toLowerCase();
        const description = card.querySelector('.prompt-description').textContent.toLowerCase();
        const content = card.querySelector('.prompt-text').textContent.toLowerCase();
        const tags = Array.from(card.querySelectorAll('.prompt-tag')).map(tag => tag.textContent.toLowerCase());
        
        const matchesSearch = query === '' || 
            title.includes(query) || 
            description.includes(query) || 
            content.includes(query);

        const matchesFilters = activeFilters.size === 0 || 
            tags.some(tag => activeFilters.has(tag));

        card.style.display = (matchesSearch && matchesFilters) ? 'flex' : 'none';
    });
}

// Configurar busca
const searchInput = document.querySelector('.prompt-search');
if (searchInput) {
    searchInput.addEventListener('input', (e) => {
        searchQuery = e.target.value;
        filterCards();
    });
}

// Configurar filtros de tag
const filterButtons = document.querySelectorAll('.filter-btn');
filterButtons.forEach(button => {
    button.addEventListener('click', () => {
        const filter = button.dataset.filter;
        
        if (filter === 'all') {
            activeFilters.clear();
            filterButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
        } else {
            const isActive = button.classList.contains('active');
            if (isActive) {
                activeFilters.delete(filter);
                button.classList.remove('active');
            } else {
                activeFilters.add(filter);
                button.classList.add('active');
            }
            document.querySelector('[data-filter="all"]').classList.remove('active');
        }
        
        filterCards();
    });
});

// Adicionar event listeners aos botões de copiar
document.querySelectorAll('.copy-button').forEach(button => {
    button.onclick = () => {
        copyContent(button);
    };
});

document.querySelectorAll('.action-button[data-action="expand"]').forEach(button => {
    button.onclick = () => {
        const card = button.closest('.prompt-card');
        expandCard(card);
    };
}); 