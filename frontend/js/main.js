
const twitterForm = document.getElementById('twitter-form');
const usernameInput = document.getElementById('twitter-username');
const analyzeBtn = document.getElementById('analyze-btn');
const themeToggle = document.getElementById('theme-toggle');
const downloadBtn = document.getElementById('download-btn');
const shareBtn = document.getElementById('share-btn');

let currentUsername = '';
let currentResults = null;
let isDarkMode = false;


function initApp() {
  twitterForm.addEventListener('submit', handleFormSubmit);
  themeToggle.addEventListener('click', toggleTheme);
  downloadBtn.addEventListener('click', handleDownload);
  shareBtn.addEventListener('click', handleShare);
  
  checkThemePreference();
  
  checkQueryParameters();
}

/**
 * Handle form submission
 * @param {Event} event - Form submit event
 */
async function handleFormSubmit(event) {
  event.preventDefault();
  
  const username = usernameInput.value.trim();
  
  if (!username) {
    showError('Please enter a Twitter username');
    return;
  }
  
  // Remove @ if present
  const cleanUsername = username.startsWith('@') ? username.substring(1) : username;
  
  updateUrlWithUsername(cleanUsername);
  
  await analyzeUsername(cleanUsername);
}

/**
 * Analyze a Twitter username
 * @param {string} username - Twitter username to analyze
 */
async function analyzeUsername(username) {
  showElement('loading-section');
  hideElement('results-section');
  
  updateLoadingStatus('Fetching recent tweets');
  
  try {
    await new Promise(resolve => setTimeout(resolve, 1000));
    
    updateLoadingStatus('Analyzing tweet content');
    
    await new Promise(resolve => setTimeout(resolve, 1500));
    
    updateLoadingStatus('Determining personality traits');
    
    await new Promise(resolve => setTimeout(resolve, 1500));
    
    const results = await api.analyzePersonality(username);
    
    currentUsername = username;
    currentResults = results;
    
    displayResults(results);
  } catch (error) {
    hideElement('loading-section');
    showError(`Error analyzing tweets: ${error.message}`);
  }
}

/**
 * Update loading status message
 * @param {string} message - Status message
 */
function updateLoadingStatus(message) {
  document.querySelector('.loading-status').textContent = message;
}


function toggleTheme() {
  isDarkMode = !isDarkMode;
  
  if (isDarkMode) {
    document.documentElement.setAttribute('data-theme', 'dark');
    localStorage.setItem('theme', 'dark');
  } else {
    document.documentElement.removeAttribute('data-theme');
    localStorage.setItem('theme', 'light');
  }
  
  updateThemeIcon();
}


function checkThemePreference() {
  const savedTheme = localStorage.getItem('theme');
  
  if (savedTheme === 'dark') {
    isDarkMode = true;
    document.documentElement.setAttribute('data-theme', 'dark');
  }
  
  updateThemeIcon();
}

function updateThemeIcon() {
  const icon = themeToggle.querySelector('.icon-moon');
  
  if (isDarkMode) {
    icon.classList.remove('icon-moon');
    icon.classList.add('icon-sun');
  } else {
    icon.classList.remove('icon-sun');
    icon.classList.add('icon-moon');
  }
}

function handleDownload() {
  downloadResults();
}

function handleShare() {
  shareResults();
}


function checkQueryParameters() {
  const urlParams = new URLSearchParams(window.location.search);
  const username = urlParams.get('username');
  
  if (username) {
    usernameInput.value = username;
    analyzeUsername(username);
  }
}

/**
 * Update URL with username parameter
 * @param {string} username - Twitter username
 */
function updateUrlWithUsername(username) {
  const url = new URL(window.location);
  url.searchParams.set('username', username);
  window.history.pushState({}, '', url);
}

/**
 * Show an error message
 * @param {string} message - Error message
 */
function showError(message) {
  alert(message);
}

/**
 * Helper to show an element
 * @param {string} id - Element ID
 */
function showElement(id) {
  document.getElementById(id).classList.remove('hidden');
}

/**
 * Helper to hide an element
 * @param {string} id - Element ID
 */
function hideElement(id) {
  document.getElementById(id).classList.add('hidden');
}

document.addEventListener('DOMContentLoaded', initApp);