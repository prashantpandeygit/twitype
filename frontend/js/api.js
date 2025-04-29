
class ApiClient {
  constructor() {
    this.baseUrl = 'https://xpersonalitypredictor.onrender.com/';
  }

  /**
   * Analyze a Twitter user's personality
   * @param {string} username - Twitter username without @
   * @returns {Promise<Object>} - Personality analysis results
   */
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

  /**
   * Get a specific MBTI personality type description
   * @param {string} type - MBTI type code (e.g., 'INFJ')
   * @returns {Promise<Object>} - Personality type details
   */
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