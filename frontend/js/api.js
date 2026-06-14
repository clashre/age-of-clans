// API Client
const API = {
    async request(endpoint, method = 'GET', data = null) {
        try {
            const options = {
                method: method,
                headers: {
                    'Content-Type': 'application/json',
                }
            };
            
            if (data) {
                options.body = JSON.stringify(data);
            }
            
            const response = await fetch(`${GAME_CONFIG.API_BASE_URL}${endpoint}`, options);
            
            if (!response.ok) {
                throw new Error(`API error: ${response.status}`);
            }
            
            return await response.json();
        } catch (error) {
            console.error('API request failed:', error);
            throw error;
        }
    },
    
    async getVillage(playerId) {
        return this.request(`/villages/${playerId}`);
    },
    
    async getBuildings(villageId) {
        return this.request(`/villages/${villageId}/buildings`);
    },
    
    async getTroops(villageId) {
        return this.request(`/villages/${villageId}/troops`);
    },
    
    async startBuilding(villageId, buildingType, x, y) {
        return this.request(`/villages/${villageId}/buildings`, 'POST', {
            type: buildingType,
            x: x,
            y: y
        });
    },
    
    async startTraining(villageId, troopType, quantity) {
        return this.request(`/villages/${villageId}/troops`, 'POST', {
            type: troopType,
            quantity: quantity
        });
    },
    
    async startAttack(villageId, enemyId, troops) {
        return this.request(`/villages/${villageId}/attack`, 'POST', {
            enemy_id: enemyId,
            troops: troops
        });
    },
    
    async startResearch(villageId, researchType) {
        return this.request(`/villages/${villageId}/research`, 'POST', {
            type: researchType
        });
    }
};