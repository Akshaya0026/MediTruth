const drugData = {
    'vaccine': {
      uses: 'Protects against specific diseases by boosting immunity.',
      sideEffects: {
        youth: 'Mild fever, fatigue',
        adult: 'Headache, chills',
        senior: 'Joint pain, dizziness'
      },
      dosagePerKg: 0.5 // mg/kg
    },
    'paracetamol': {
      uses: 'Used to treat fever and mild to moderate pain.',
      sideEffects: {
        youth: 'Nausea, rash',
        adult: 'Liver strain, dizziness',
        senior: 'Kidney load, sleepiness'
      },
      dosagePerKg: 10
    }
  };
  
  // Save to localStorage
  function save(key, value) {
    localStorage.setItem(key, value);
  }
  
  // Get from localStorage
  function get(key) {
    return localStorage.getItem(key);
  }
  