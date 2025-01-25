---
title: Prompt Engineering Collection
description: A curated collection of high-quality prompts for various use cases, organized by category and optimized for different AI models.
---

<head>
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
</head>

# Catálogo de Prompts

Explore nossa coleção curada de prompts de IA para diferentes casos de uso e modelos de linguagem.

<div class="search-box">
    <input type="text" class="prompt-search" placeholder="Pesquisar prompts...">
</div>

<div class="filter-section" id="categoryFilters">
    <button class="filter-btn active" data-filter="all">Todos</button>
    <!-- Filtros serão adicionados dinamicamente via JavaScript -->
</div>

<div class="prompt-gallery">
    <!-- Cards serão adicionados dinamicamente via JavaScript -->
</div>

<script>
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
        galleryData.prompts.forEach(prompt => {
            // ... (manter o código existente de renderização dos cards)
        });

    } catch (error) {
        console.error('Erro ao carregar dados da galeria:', error);
    }
});
</script>