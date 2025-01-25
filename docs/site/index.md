---
title: Galeria de Prompts
description: Uma coleção de prompts otimizados para diferentes modelos de IA
layout: default
---

<div class="gallery-container">
    <div class="filters-section">
        <h2>Filtros</h2>
        <p>Use os filtros abaixo para encontrar o prompt perfeito para sua necessidade.</p>
        
        <div class="search-box">
            <input type="text" placeholder="Pesquisar prompts..." />
        </div>
        
        <div class="filter-groups">
            <div class="filter-group">
                <h3>Categorias</h3>
                <div class="filter-buttons" id="category-filters">
                    <!-- Categorias serão inseridas aqui dinamicamente -->
                </div>
            </div>
            
            <div class="filter-group">
                <h3>Modelos</h3>
                <div class="filter-buttons" id="model-filters">
                    <!-- Modelos serão inseridos aqui dinamicamente -->
                </div>
            </div>
        </div>
        
        <button class="clear-filters">Limpar Filtros</button>
    </div>

    <div class="prompt-gallery" id="prompt-gallery">
        <!-- Cards serão inseridos aqui dinamicamente -->
    </div>
</div>

<script>
    // Função para carregar dados do JSON
    async function loadGalleryData() {
        try {
            // Em desenvolvimento local, usa sample.json
            const isDev = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1';
            const dataUrl = isDev ? '/assets/data/sample.json' : '/assets/data/gallery.json';
            
            const response = await fetch(dataUrl);
            const data = await response.json();
            return data;
        } catch (error) {
            console.error('Error loading gallery data:', error);
            return null;
        }
    }

    // Função para criar um card de prompt
    function createPromptCard(prompt) {
        return `
            <div class="prompt-card" data-category="${prompt.category.toLowerCase()}" data-model="${prompt.model.toLowerCase()}">
                <div class="card-header">
                    <div class="card-badges">
                        <span class="badge model-badge">${prompt.model}</span>
                        <span class="badge category-badge">${prompt.category}</span>
                    </div>
                    <h3>${prompt.title}</h3>
                    <p class="description">${prompt.description}</p>
                </div>
                
                <div class="card-tags">
                    ${prompt.tags.map(tag => `<span class="tag">${tag}</span>`).join(' ')}
                </div>
                
                <div class="card-footer">
                    <div class="metadata">
                        <span class="version">v${prompt.version}</span>
                        <span class="date">${prompt.date}</span>
                    </div>
                    <div class="actions">
                        <button class="copy-btn" title="Copiar">
                            <span class="material-icons">content_copy</span>
                        </button>
                        <button class="expand-btn" title="Expandir">
                            <span class="material-icons">open_in_full</span>
                        </button>
                    </div>
                </div>
            </div>
        `;
    }

    // Função para criar botões de filtro
    function createFilterButtons(items, containerId) {
        const container = document.getElementById(containerId);
        items.forEach((item, index) => {
            const button = document.createElement('button');
            button.className = 'filter-btn' + (index === 0 ? ' active' : '');
            button.textContent = item;
            container.appendChild(button);
        });
    }

    // Inicialização
    document.addEventListener('DOMContentLoaded', async function() {
        const data = await loadGalleryData();
        if (!data) return;

        // Criar filtros
        createFilterButtons(data.categories, 'category-filters');
        createFilterButtons(data.models, 'model-filters');

        // Criar cards
        const gallery = document.getElementById('prompt-gallery');
        data.prompts.forEach(prompt => {
            gallery.insertAdjacentHTML('beforeend', createPromptCard(prompt));
        });

        // Inicializar funcionalidades
        initializeGalleryFunctionality();
    });
</script>