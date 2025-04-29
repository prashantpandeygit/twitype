const mbtiData = {
  INTJ: {
    title: 'The Architect',
    description: 'INTJs are analytical problem-solvers, innovative and independent. They drive to implement their ideas and achieve their goals. They quickly see patterns and generate long-range explanatory perspectives. INTJs are skeptical, critical, independent, determined, often stubborn. They have high standards of competence and performance, for themselves and others.',
    traits: ['Analytical', 'Logical', 'Strategic', 'Independent', 'Perfectionist'],
  },
  INTP: {
    title: 'The Logician',
    description: 'INTPs are logical, original, creative thinkers. They seek to develop logical explanations for everything that interests them. They excel at analyzing complex theoretical problems and grasp subtle logical distinctions. INTPs are skeptical, sometimes critical, analytical, and often seek precision in expression.',
    traits: ['Inventive', 'Logical', 'Contemplative', 'Theoretical', 'Objective'],
  },
  ENTJ: {
    title: 'The Commander',
    description: 'ENTJs are strategic leaders, motivated to organize change. They conceptualize and theorize, then create plans to implement their vision. They value knowledge, competence, and structure. ENTJs are natural leaders who can make tough decisions and are driven to achieve their goals.',
    traits: ['Assertive', 'Strategic', 'Efficient', 'Decisive', 'Confident'],
  },
  ENTP: {
    title: 'The Debater',
    description: 'ENTPs are creative, resourceful problem-solvers. They excel at generating conceptual possibilities and analyzing them strategically. They are quick, witty, and outspoken with a clever solution for any complex problem. ENTPs value knowledge and competence and enjoy intellectual challenges.',
    traits: ['Innovative', 'Debative', 'Assertive', 'Quick-witted', 'Resourceful'],
  },
  INFJ: {
    title: 'The Advocate',
    description: 'INFJs are insightful, creative nurturers with a strong sense of personal integrity and a drive to help others. They seek meaning and connection and want to understand what motivates people. INFJs are organized and decisive in implementing their vision and are deeply concerned with the welfare of others.',
    traits: ['Insightful', 'Principled', 'Creative', 'Altruistic', 'Reserved'],
  },
  INFP: {
    title: 'The Mediator',
    description: 'INFPs are idealistic, loyal to their values and to people who are important to them. They seek to live a life in accordance with their values and want to be authentic. INFPs are curious about possibilities, see potential for good in others, and enjoy helping others fulfill their potential.',
    traits: ['Idealistic', 'Empathetic', 'Creative', 'Curious', 'Adaptable'],
  },
  ENFJ: {
    title: 'The Protagonist',
    description: 'ENFJs are people-focused organizers. They strive to develop potential in others and build communities. They are charismatic and inspiring leaders who bring out the best in others. ENFJs are typically exuberant, idealistic, focused on possibilities, and attuned to others\' needs.',
    traits: ['Charismatic', 'Empathetic', 'Reliable', 'Persuasive', 'Altruistic'],
  },
  ENFP: {
    title: 'The Campaigner',
    description: 'ENFPs are enthusiastic, creative, and sociable free spirits who can always find a reason to smile. They see possibilities for improvement everywhere and can be inspiring, motivating, and persuasive. ENFPs value authentic connections with others and enjoy helping people explore their creative potential.',
    traits: ['Enthusiastic', 'Creative', 'Sociable', 'Perceptive', 'Spontaneous'],
  },
  ISTJ: {
    title: 'The Logistician',
    description: 'ISTJs are practical, fact-minded, and reliable, with a strong sense of responsibility. They are thorough, dependable, and work steadily toward identified goals. They can be counted on to honor their commitments. ISTJs tend to be private, reserved, and thoughtful.',
    traits: ['Practical', 'Dependable', 'Organized', 'Logical', 'Traditional'],
  },
  ISFJ: {
    title: 'The Defender',
    description: 'ISFJs are conscientious and dedicated. They are committed to kindness and consideration, and their excellent organizational skills allow them to create order and security in their environments. ISFJs are caring, loyal, and often focused on the needs of others.',
    traits: ['Observant', 'Supportive', 'Reliable', 'Patient', 'Detailed'],
  },
  ESTJ: {
    title: 'The Executive',
    description: 'ESTJs are practical, realistic, and matter-of-fact, with a natural head for business or mechanics. They organize projects and people to get things done efficiently and systematically. ESTJs take responsibility and are dedicated to traditional values and institutions.',
    traits: ['Organized', 'Practical', 'Honest', 'Dedicated', 'Traditional'],
  },
  ESFJ: {
    title: 'The Consul',
    description: 'ESFJs are warmhearted, conscientious, and cooperative. They want to be appreciated for who they are and for what they contribute. They excel at creating harmony in their environment and are adept at building consensus. ESFJs value tradition, security, and peaceful living.',
    traits: ['Caring', 'Supportive', 'Reliable', 'Conscientious', 'Traditional'],
  },
  ISTP: {
    title: 'The Virtuoso',
    description: 'ISTPs are observant and incisive troubleshooters. They excel at practical problem-solving and are independent, adaptable, and often athletic. ISTPs enjoy adventure and variety and often have mechanical or artistic skills. They can be detached and analytical.',
    traits: ['Practical', 'Adaptable', 'Technical', 'Spontaneous', 'Independent'],
  },
  ISFP: {
    title: 'The Adventurer',
    description: 'ISFPs are gentle, sensitive, and compassionate. They enjoy the present moment and seek autonomy and personal space. ISFPs are often artistic and design-oriented, with an affinity for aesthetics and nature. They are adaptable, accepting, and realistic.',
    traits: ['Artistic', 'Sensitive', 'Loyal', 'Imaginative', 'Spontaneous'],
  },
  ESTP: {
    title: 'The Entrepreneur',
    description: 'ESTPs are energetic, spontaneous problem-solvers. They enjoy life and new experiences. ESTPs are realists who easily adapt to new situations, enjoy physical activities, and excel at solving immediate problems. They can be charming, persuasive, and resourceful.',
    traits: ['Energetic', 'Adaptable', 'Practical', 'Spontaneous', 'Persuasive'],
  },
  ESFP: {
    title: 'The Entertainer',
    description: 'ESFPs are outgoing, friendly, and accepting. They enjoy people, experiences, and making things fun. ESFPs are observant of others and responsive to their practical needs. They are generous with their time and resources and love to be the center of attention.',
    traits: ['Enthusiastic', 'Social', 'Spontaneous', 'Practical', 'Observant'],
  }
};

function getMbtiTypeData(type) {
  return mbtiData[type.toUpperCase()] || {
    title: 'Unknown Type',
    description: 'Information about this personality type is not available.',
    traits: []
  };
}