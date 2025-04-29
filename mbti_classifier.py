from typing import Dict, Tuple, List
import random

def classify_personality(trait_counts: Dict[str, int]) -> Tuple[str, Dict[str, float]]:
    """
    Classify MBTI personality type based on trait indicators
    
    Args:
        trait_counts: Dictionary with counts for each trait
        
    Returns:
        Tuple containing:
            - MBTI personality type (e.g., "INTJ")
            - Dictionary with percentage scores for each trait
    """
    e_i_percentages = get_trait_percentages(trait_counts, "E", "I")
    s_n_percentages = get_trait_percentages(trait_counts, "S", "N")
    t_f_percentages = get_trait_percentages(trait_counts, "T", "F")
    j_p_percentages = get_trait_percentages(trait_counts, "J", "P")
    
    e_or_i = "E" if e_i_percentages["E"] >= e_i_percentages["I"] else "I"
    s_or_n = "S" if s_n_percentages["S"] >= s_n_percentages["N"] else "N"
    t_or_f = "T" if t_f_percentages["T"] >= t_f_percentages["F"] else "F"
    j_or_p = "J" if j_p_percentages["J"] >= j_p_percentages["P"] else "P"
    
    mbti_type = e_or_i + s_or_n + t_or_f + j_or_p
    
    all_percentages = {
        **e_i_percentages,
        **s_n_percentages,
        **t_f_percentages,
        **j_p_percentages
    }
    
    return mbti_type, all_percentages

def get_trait_percentages(trait_counts: Dict[str, int], trait1: str, trait2: str) -> Dict[str, float]:
    """
    Calculate percentage distribution between opposing traits
    
    Args:
        trait_counts: Trait count dictionary
        trait1: First trait in the pair (E, S, T, or J)
        trait2: Second trait in the pair (I, N, F, or P)
        
    Returns:
        Dictionary with percentage values for both traits
    """
    total = trait_counts[trait1] + trait_counts[trait2]
    
    if total == 0:
        base = random.uniform(45, 55)
        return {trait1: base, trait2: 100 - base}
    
    percent1 = (trait_counts[trait1] / total) * 100
    percent2 = (trait_counts[trait2] / total) * 100
    
    noise = random.uniform(-10, 10)
    percent1 = max(min(percent1 + noise, 90), 10)  
    percent2 = 100 - percent1
    
    return {trait1: percent1, trait2: percent2}

def get_personality_description(mbti_type: str) -> str:
    """
    Get a description of the MBTI personality type
    
    Args:
        mbti_type: MBTI type code (e.g., "INTJ")
        
    Returns:
        Description of the personality type
    """
    descriptions = {
        "INTJ": "INTJs are analytical problem-solvers, innovative and independent. They drive to implement their ideas and achieve their goals.",
        "INTP": "INTPs are logical, original, creative thinkers. They seek to develop logical explanations for everything that interests them.",
        "ENTJ": "ENTJs are strategic leaders, motivated to organize change. They conceptualize and theorize, then create plans to implement their vision.",
        "ENTP": "ENTPs are creative, resourceful problem-solvers. They excel at generating conceptual possibilities and analyzing them strategically.",
        "INFJ": "INFJs are insightful, creative nurturers with a strong sense of personal integrity and a drive to help others realize their potential.",
        "INFP": "INFPs are idealistic, loyal to their values and to people who are important to them. They want to live a life in accordance with their values.",
        "ENFJ": "ENFJs are people-focused organizers. They are extraverted, idealistic, charismatic, outspoken, highly principled and ethical.",
        "ENFP": "ENFPs are enthusiastic, creative, and sociable free spirits who can always find a reason to smile. They are warm, passionate and charismatic.",
        "ISTJ": "ISTJs are practical, fact-minded, and reliable, with a strong sense of responsibility. They are thorough, dependable, and work steadily.",
        "ISFJ": "ISFJs are conscientious, responsible, and committed to their obligations. They are compassionate, caring, and focused on others' needs.",
        "ESTJ": "ESTJs are practical, realistic, and matter-of-fact, with a natural head for business or mechanics. They organize projects and people.",
        "ESFJ": "ESFJs are warmhearted, conscientious, and cooperative. They value harmony and work determinedly to establish it.",
        "ISTP": "ISTPs are practical troubleshooters. They are quiet observers until a problem appears, then they act quickly to find workable solutions.",
        "ISFP": "ISFPs are quiet, sensitive, kind, and loyal. They enjoy the present moment, what's going on around them, and are keen observers of the practical.",
        "ESTP": "ESTPs are energetic, active problem-solvers. They are spontaneous, adaptable, and resourceful. They enjoy new experiences and sensations.",
        "ESFP": "ESFPs are outgoing, friendly, and accepting. They enjoy working with others and are energized by social interaction. They are spontaneous."
    }
    
    return descriptions.get(mbti_type, "Personality type description not available.")

def get_trait_strength(percentages: Dict[str, float], trait: str) -> str:
    """
    Determine the strength of a trait based on its percentage
    
    Args:
        percentages: Dictionary with trait percentages
        trait: The trait to evaluate
        
    Returns:
        String description of trait strength
    """
    percentage = percentages[trait]
    
    if percentage >= 80:
        return "very strong"
    elif percentage >= 65:
        return "strong"
    elif percentage >= 55:
        return "moderate"
    elif percentage > 50:
        return "slight"
    else:
        return "not preferred"