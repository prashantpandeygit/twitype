/**
 * Functions for displaying and handling personality analysis results
 */

/**
 * Display the personality analysis results
 * @param {Object} results - Personality analysis data from the API
 */
function displayResults(results) {
  document.getElementById('result-username').textContent = `@${results.username}`;
  
  const mbtiType = results.personality_type;
  const typeData = getMbtiTypeData(mbtiType);
  
  document.getElementById('mbti-type').textContent = mbtiType;
  document.getElementById('mbti-title').textContent = typeData.title;
  document.getElementById('personality-description').textContent = typeData.description;
  
  const personalityCard = document.querySelector('.personality-card');
  const classes = Array.from(personalityCard.classList);
  classes.forEach(className => {
    if (className !== 'personality-card') {
      personalityCard.classList.remove(className);
    }
  });
  personalityCard.classList.add(mbtiType);
  
  updateTraitPercentages(results.traits);
  
  displayTweetExamples(results.tweet_evidence);
  
  hideElement('loading-section');
  showElement('results-section');
}

/**
 * Update the trait percentage bars
 * @param {Object} traits - Trait percentages from the API
 */
function updateTraitPercentages(traits) {
  // E-I dimension
  updateTraitPair('E', 'I', traits.extraversion, traits.introversion);
  
  // S-N dimension
  updateTraitPair('S', 'N', traits.sensing, traits.intuition);
  
  // T-F dimension
  updateTraitPair('T', 'F', traits.thinking, traits.feeling);
  
  // J-P dimension
  updateTraitPair('J', 'P', traits.judging, traits.perceiving);
}

/**
 * Update a pair of opposite traits
 * @param {string} trait1 - First trait letter
 * @param {string} trait2 - Second trait letter
 * @param {number} value1 - First trait percentage (0-100)
 * @param {number} value2 - Second trait percentage (0-100)
 */
function updateTraitPair(trait1, trait2, value1, value2) {
  document.getElementById(`${trait1}-progress`).style.width = `${value1}%`;
  document.getElementById(`${trait1}-percentage`).textContent = `${Math.round(value1)}%`;
  
  document.getElementById(`${trait2}-progress`).style.width = `${value2}%`;
  document.getElementById(`${trait2}-percentage`).textContent = `${Math.round(value2)}%`;
}

/**
 * Display tweet examples that evidence personality traits
 * @param {Array} tweetEvidence - Array of tweet examples with trait indicators
 */
function displayTweetExamples(tweetEvidence) {
  const container = document.getElementById('tweet-examples-container');
  container.innerHTML = '';
  
  if (!tweetEvidence || tweetEvidence.length === 0) {
    container.innerHTML = '<p>No specific tweet examples available.</p>';
    return;
  }
  
  tweetEvidence.forEach(tweet => {
    const tweetCard = document.createElement('div');
    tweetCard.className = 'tweet-card';
    
    const tweetText = document.createElement('p');
    tweetText.className = 'tweet-text';
    tweetText.textContent = tweet.text;
    
    const tweetTraits = document.createElement('div');
    tweetTraits.className = 'tweet-traits';
    
    tweet.traits.forEach(trait => {
      const traitSpan = document.createElement('span');
      traitSpan.className = 'tweet-trait';
      traitSpan.textContent = trait;
      tweetTraits.appendChild(traitSpan);
    });
    
    tweetCard.appendChild(tweetText);
    tweetCard.appendChild(tweetTraits);
    container.appendChild(tweetCard);
  });
}

/**
 * Generate a shareable image of the results
 * @returns {Promise<Blob>} - Image blob for download
 */
async function generateResultImage() {
  alert('This feature would generate a shareable image in a production environment.');
  return null;
}

function shareResults() {
  const text = `I just discovered I'm an ${document.getElementById('mbti-type').textContent} (${document.getElementById('mbti-title').textContent}) on TweetPersona!`;
  const url = window.location.href;
  
  const shareUrl = `https://twitter.com/intent/tweet?text=${encodeURIComponent(text)}&url=${encodeURIComponent(url)}`;
  
  window.open(shareUrl, '_blank');
}

function downloadResults() {
  alert('This feature would generate a downloadable report in a production environment.');
}