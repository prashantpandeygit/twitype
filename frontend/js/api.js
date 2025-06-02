
class ApiClient {
  constructor() {
    this.baseUrl = 'https://twitype.onrender.com';
  }

  async analyzePersonality(username) {
    try {
      const response = await fetch(`${this.baseUrl}/analyze/${username}`);
      
      if (!response.ok) {
        const error = await response.json();
        throw new Error(error.detail || 'Failed to analyze personality');
      }
      
      return await response.json();
    } catch (error) {
      console.error('API Error:', error);
      throw error;
    }
  }


  async getPersonalityTypeDetails(type) {
    try {
      const response = await fetch(`${this.baseUrl}/personality-type/${type}`);
      
      if (!response.ok) {
        const error = await response.json();
        throw new Error(error.detail || 'Failed to get personality details');
      }
      
      return await response.json();
    } catch (error) {
      console.error('API Error:', error);
      throw error;
    }
  }
}

const api = new ApiClient();
