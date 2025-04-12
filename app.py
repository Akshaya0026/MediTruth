from flask import Flask, render_template, request

app = Flask(__name__)

# Simulated medicine database
medicine_info = {
    "paracetamol": {
        "use": "Used to treat fever and mild to moderate pain.",
        "side_effects": {
            "young": "Liver damage if overdosed. Rare skin rashes.",
            "adult": "Long-term use may affect liver and kidney function.",
            "senior": "May cause blood thinning or organ stress."
        },
        "dosage_per_kg": 15
    },
    "ibuprofen": {
        "use": "Reduces inflammation, pain, and fever.",
        "side_effects": {
            "young": "Stomach upset, dizziness.",
            "adult": "Ulcers, liver/kidney issues if used long-term.",
            "senior": "Heart and stomach risks increase."
        },
        "dosage_per_kg": 10
    },
    "amoxicillin": {
        "use": "Antibiotic used to treat bacterial infections.",
        "side_effects": {
            "young": "Diarrhea, rash, allergic reactions.",
            "adult": "Yeast infections, allergic response.",
            "senior": "Increased risk of colitis and kidney strain."
        },
        "dosage_per_kg": 20
    },
    "azithromycin": {
        "use": "Antibiotic for respiratory and skin infections.",
        "side_effects": {
            "young": "Nausea, stomach upset.",
            "adult": "Heart rhythm issues in high doses.",
            "senior": "Hearing changes or irregular heartbeat."
        },
        "dosage_per_kg": 10
    },
    "cetirizine": {
        "use": "Relieves allergy symptoms like sneezing and itching.",
        "side_effects": {
            "young": "Mild drowsiness or irritability.",
            "adult": "Dry mouth, fatigue.",
            "senior": "Confusion or urinary retention (rare)."
        },
        "dosage_per_kg": 5
    },
    "insulin": {
        "use": "Controls blood sugar in diabetes.",
        "side_effects": {
            "young": "Low blood sugar, dizziness.",
            "adult": "Weight gain, injection site swelling.",
            "senior": "Low glucose confusion, fall risk."
        },
        "dosage_per_kg": 0.5
    },
    "metformin": {
        "use": "Controls blood sugar in type 2 diabetes.",
        "side_effects": {
            "young": "Not usually recommended unless prescribed.",
            "adult": "Stomach upset, lactic acidosis (rare).",
            "senior": "Vitamin B12 deficiency risk."
        },
        "dosage_per_kg": 20
    },
    "tenofovir": {
        "use": "Used in HIV treatment and prevention (PrEP).",
        "side_effects": {
            "young": "Rare use; if used, monitor kidney.",
            "adult": "Kidney issues, bone thinning.",
            "senior": "Higher risk of renal toxicity."
        },
        "dosage_per_kg": 0
    },
    "lamivudine": {
        "use": "HIV and hepatitis B antiviral.",
        "side_effects": {
            "young": "Fatigue, headache.",
            "adult": "Nausea, liver enzyme elevation.",
            "senior": "Peripheral neuropathy (rare)."
        },
        "dosage_per_kg": 0
    },
    "efavirenz": {
        "use": "Antiretroviral drug used to treat HIV.",
        "side_effects": {
            "young": "Not typically used.",
            "adult": "Dizziness, sleep disturbances.",
            "senior": "Confusion, mood changes (rare)."
        },
        "dosage_per_kg": 0
    },
    "artemether": {
        "use": "Antimalarial drug.",
        "side_effects": {
            "young": "Fever, headache, nausea.",
            "adult": "Dizziness, vomiting.",
            "senior": "Liver enzyme elevation."
        },
        "dosage_per_kg": 4
    },
    "hiv vaccine": {
        "use": "Under clinical trials for HIV prevention.",
        "side_effects": {
            "young": "N/A.",
            "adult": "Pain at injection, mild fever.",
            "senior": "Rare mild side effects."
        },
        "dosage_per_kg": 0
    },
    "typhoid": {
        "use": "Protects against typhoid fever.",
        "side_effects": {
            "young": "Fever, headache, nausea.",
            "adult": "Pain at injection site.",
            "senior": "Fatigue, mild reaction."
        },
        "dosage_per_kg": 0
    },
    "hepatitis a": {
        "use": "Protects against hepatitis A infection.",
        "side_effects": {
            "young": "Soreness at site, mild fever.",
            "adult": "Fatigue, headache.",
            "senior": "Usually well tolerated."
        },
        "dosage_per_kg": 0
    },
    "hpv": {
        "use": "Prevents human papillomavirus infections and cervical cancer.",
        "side_effects": {
            "young": "Pain at injection, mild fever.",
            "adult": "Fainting (rare), nausea.",
            "senior": "Not usually administered."
        },
        "dosage_per_kg": 0
    },
    # New Additions: Aspirin, Vitamin C, and More
    "aspirin": {
        "use": "Pain relief, anti-inflammatory, and blood thinner.",
        "side_effects": {
            "young": "Stomach upset, risk of Reye's syndrome in children.",
            "adult": "Stomach ulcers, gastrointestinal bleeding.",
            "senior": "Increased risk of bleeding and ulcers."
        },
        "dosage_per_kg": 10
    },
    "vitamin c": {
        "use": "Supports immune function, antioxidant properties.",
        "side_effects": {
            "young": "Stomach upset in large doses.",
            "adult": "Diarrhea if taken in excess.",
            "senior": "Risk of kidney stones in high doses."
        },
        "dosage_per_kg": 1
    },
    # New Additions: More Common Drugs and Vaccines
    "cholesterol medication": {
        "use": "Lowers cholesterol and triglycerides.",
        "side_effects": {
            "young": "Muscle pain, liver problems.",
            "adult": "Liver enzyme changes, muscle weakness.",
            "senior": "Cognitive issues, increased fall risk."
        },
        "dosage_per_kg": 5
    },
    "penicillin": {
        "use": "Antibiotic used to treat various bacterial infections.",
        "side_effects": {
            "young": "Rash, allergic reactions.",
            "adult": "Diarrhea, allergic reactions.",
            "senior": "Kidney issues with prolonged use."
        },
        "dosage_per_kg": 20
    },
    "calcium supplements": {
        "use": "Supports bone health, treats calcium deficiencies.",
        "side_effects": {
            "young": "Constipation, stomach upset.",
            "adult": "Kidney stones if overused.",
            "senior": "Risk of kidney stones, constipation."
        },
        "dosage_per_kg": 1
    },
    "vitamin d": {
        "use": "Supports bone health and immune function.",
        "side_effects": {
            "young": "High doses may cause nausea.",
            "adult": "Excessive doses may cause kidney damage.",
            "senior": "Risk of hypercalcemia with overdose."
        },
        "dosage_per_kg": 0.5
    },
    "flu vaccine": {
        "use": "Protects against seasonal influenza.",
        "side_effects": {
            "young": "Pain at injection site, mild fever.",
            "adult": "Soreness, low-grade fever.",
            "senior": "Mild side effects, rare allergic reactions."
        },
        "dosage_per_kg": 0
    }
}



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        drug = request.form['drug'].lower()
        age = int(request.form['age'])
        weight = float(request.form['weight'])

        if drug not in medicine_info:
            return render_template('index.html', error="Drug not found. Try another.")

        info = medicine_info[drug]
        use = info["use"]
        dosage = weight * info["dosage_per_kg"]

        # Side effects by age
        if age < 12:
            side_effect = info["side_effects"]["young"]
        elif 12 <= age < 60:
            side_effect = info["side_effects"]["adult"]
        else:
            side_effect = info["side_effects"]["senior"]

        return render_template('index.html', drug=drug, use=use, side_effect=side_effect, dosage=dosage)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
