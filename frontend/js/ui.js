// UI Management
const UI = {
    buildModal: null,
    trainModal: null,
    attackModal: null,
    researchModal: null,
    
    init() {
        document.getElementById('build-btn').addEventListener('click', () => this.openBuildMenu());
        document.getElementById('train-btn').addEventListener('click', () => this.openTrainMenu());
        document.getElementById('attack-btn').addEventListener('click', () => this.openAttackMenu());
        document.getElementById('research-btn').addEventListener('click', () => this.openResearchMenu());
    },
    
    openBuildMenu() {
        console.log('Opening build menu');
        const buildingsHTML = Object.entries(GAME_CONFIG.BUILDINGS)
            .map(([key, building]) => `
                <div class="modal-item">
                    <div class="modal-item-info">
                        <h3>${building.name}</h3>
                        <p>Oro: ${building.cost.gold} | Tiempo: ${building.time}s</p>
                    </div>
                    <button class="btn btn-primary" onclick="startBuilding('${key}')">Construir</button>
                </div>
            `).join('');
        
        this.showModal('Construir', buildingsHTML);
    },
    
    openTrainMenu() {
        console.log('Opening train menu');
        const troopsHTML = Object.entries(GAME_CONFIG.TROOPS)
            .map(([key, troop]) => `
                <div class="modal-item">
                    <div class="modal-item-info">
                        <h3>${troop.name}</h3>
                        <p>Oro: ${troop.cost.gold} | Tiempo: ${troop.time}s | Daño: ${troop.damage}</p>
                    </div>
                    <button class="btn btn-primary" onclick="startTraining('${key}')">Entrenar</button>
                </div>
            `).join('');
        
        this.showModal('Entrenar Tropas', troopsHTML);
    },
    
    openAttackMenu() {
        console.log('Opening attack menu');
        const content = `
            <p>Selecciona un enemigo para atacar:</p>
            <div id="enemies-list"></div>
            <button class="btn btn-primary" onclick="loadEnemies()">Cargar enemigos</button>
        `;
        this.showModal('Atacar', content);
    },
    
    openResearchMenu() {
        console.log('Opening research menu');
        const content = `
            <p>Mejoras disponibles en el laboratorio:</p>
            <button class="btn btn-primary" onclick="startResearch('troop_damage')">Daño de tropas</button>
            <button class="btn btn-primary" onclick="startResearch('building_hp')">HP de edificios</button>
        `;
        this.showModal('Investigar', content);
    },
    
    showModal(title, content) {
        const overlay = document.createElement('div');
        overlay.className = 'modal-overlay active';
        overlay.onclick = () => this.closeModal();
        document.body.appendChild(overlay);
        
        const modal = document.createElement('div');
        modal.className = 'modal active';
        modal.innerHTML = `
            <h2>${title}</h2>
            <div>${content}</div>
            <div class="btn-group">
                <button class="btn btn-secondary" onclick="document.querySelector('.modal').parentElement.remove(); document.querySelector('.modal-overlay')?.remove()">Cerrar</button>
            </div>
        `;
        document.body.appendChild(modal);
    },
    
    closeModal() {
        document.querySelector('.modal')?.remove();
        document.querySelector('.modal-overlay')?.remove();
    }
};

// Helper functions
function startBuilding(buildingType) {
    console.log('Starting building:', buildingType);
    const building = GAME_CONFIG.BUILDINGS[buildingType];
    if (gameState.resources.gold >= building.cost.gold) {
        gameState.resources.gold -= building.cost.gold;
        updateResourcesUI();
        UI.closeModal();
        showNotification(`${building.name} en construcción`);
    } else {
        showNotification('Oro insuficiente', 'error');
    }
}

function startTraining(troopType) {
    console.log('Starting training:', troopType);
    const troop = GAME_CONFIG.TROOPS[troopType];
    if (gameState.resources.gold >= troop.cost.gold) {
        gameState.resources.gold -= troop.cost.gold;
        updateResourcesUI();
        UI.closeModal();
        showNotification(`${troop.name} en entrenamiento`);
    } else {
        showNotification('Oro insuficiente', 'error');
    }
}

function startResearch(researchType) {
    console.log('Starting research:', researchType);
    showNotification('Investigación iniciada');
    UI.closeModal();
}

function loadEnemies() {
    console.log('Loading enemies...');
    showNotification('Buscando enemigos...');
}

function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.style.cssText = `
        position: fixed;
        top: 100px;
        right: 20px;
        background: ${type === 'error' ? '#ff4444' : '#44ff44'};
        color: white;
        padding: 15px 20px;
        border-radius: 5px;
        font-weight: bold;
        z-index: 2000;
        animation: slideIn 0.3s ease;
    `;
    notification.textContent = message;
    document.body.appendChild(notification);
    
    setTimeout(() => notification.remove(), 3000);
}

// Initialize UI
UI.init();