document.addEventListener('DOMContentLoaded', function() {
    // Função para copiar o conteúdo
    function copyContent(button) {
        const card = button.closest('.prompt-card');
        const promptContent = card.querySelector('.prompt-content');
        
        // Cria um elemento temporário para pegar o conteúdo completo
        const temp = document.createElement('div');
        temp.innerHTML = promptContent.innerHTML;
        
        // Remove qualquer estilo que possa estar truncando o texto
        temp.style.display = 'block';
        temp.style.height = 'auto';
        temp.style.webkitLineClamp = 'none';
        temp.style.overflow = 'visible';
        
        // Pega o texto completo
        const fullPrompt = temp.textContent.trim();
        
        navigator.clipboard.writeText(fullPrompt).then(() => {
            // Feedback visual
            const icon = button.querySelector('.material-icons');
            const originalText = icon.textContent;
            icon.textContent = 'check';
            button.classList.add('copied');
            
            setTimeout(() => {
                icon.textContent = originalText;
                button.classList.remove('copied');
            }, 2000);
        });
    }

    // Função para expandir o card
    function expandCard(card) {
        const modal = document.createElement('div');
        modal.className = 'prompt-modal';
        
        const modalContent = document.createElement('div');
        modalContent.className = 'prompt-modal-content';
        modalContent.innerHTML = card.innerHTML;
        
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
            const content = card.querySelector('.prompt-content').textContent.toLowerCase();
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
    const searchInput = document.querySelector('.search-box input');
    if (searchInput) {
        searchInput.addEventListener('input', (e) => {
            searchQuery = e.target.value;
            filterCards();
        });
    }

    // Configurar filtros de tag
    const filterTags = document.querySelectorAll('.filter-tag');
    filterTags.forEach(tag => {
        tag.addEventListener('click', () => {
            const tagText = tag.textContent.toLowerCase();
            
            if (activeFilters.has(tagText)) {
                activeFilters.delete(tagText);
                tag.classList.remove('active');
            } else {
                activeFilters.add(tagText);
                tag.classList.add('active');
            }
            
            filterCards();
        });
    });

    // Adicionar event listeners aos botões
    document.querySelectorAll('.action-button[data-action="copy"]').forEach(button => {
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
}); 