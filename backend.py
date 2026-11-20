MEDICINES = {
    "paracetamol": {
        "generic_name": "Paracetamol",
        "strengths": ["500 mg", "650 mg"],
        "category": "Pain reliever and fever reducer",
        "generic_alternative": "Generic paracetamol",
        "affordable_option": "Generic paracetamol is usually available at lower prices than branded versions."
    },

    "amoxicillin": {
        "generic_name": "Amoxicillin",
        "strengths": ["250 mg", "500 mg"],
        "category": "Antibiotic",
        "generic_alternative": "Generic amoxicillin",
        "affordable_option": "Generic amoxicillin may be available at a lower price than branded versions."
    },

    "metformin": {
        "generic_name": "Metformin",
        "strengths": ["500 mg", "850 mg", "1000 mg"],
        "category": "Medicine used to manage blood glucose",
        "generic_alternative": "Generic metformin",
        "affordable_option": "Generic metformin is commonly available at lower prices than branded versions."
    },

    "azithromycin": {
        "generic_name": "Azithromycin",
        "strengths": ["250 mg", "500 mg"],
        "category": "Antibiotic",
        "generic_alternative": "Generic azithromycin",
        "affordable_option": "Generic azithromycin may be available at a lower price than branded versions."
    },

    "cetirizine": {
        "generic_name": "Cetirizine",
        "strengths": ["5 mg", "10 mg"],
        "category": "Antihistamine used for allergy symptoms",
        "generic_alternative": "Generic cetirizine",
        "affordable_option": "Generic cetirizine is commonly available at lower prices."
    },

    "omeprazole": {
        "generic_name": "Omeprazole",
        "strengths": ["20 mg", "40 mg"],
        "category": "Medicine that reduces stomach acid",
        "generic_alternative": "Generic omeprazole",
        "affordable_option": "Generic omeprazole may be available at a lower price than branded versions."
    },

    "pantoprazole": {
        "generic_name": "Pantoprazole",
        "strengths": ["40 mg"],
        "category": "Medicine that reduces stomach acid",
        "generic_alternative": "Generic pantoprazole",
        "affordable_option": "Generic pantoprazole is commonly available as a lower-cost generic."
    },

    "ibuprofen": {
        "generic_name": "Ibuprofen",
        "strengths": ["200 mg", "400 mg"],
        "category": "Pain reliever and anti-inflammatory medicine",
        "generic_alternative": "Generic ibuprofen",
        "affordable_option": "Generic ibuprofen may be available at lower prices."
    },

    "diclofenac": {
        "generic_name": "Diclofenac",
        "strengths": ["50 mg"],
        "category": "Pain reliever and anti-inflammatory medicine",
        "generic_alternative": "Generic diclofenac",
        "affordable_option": "Generic diclofenac may be available at lower prices."
    },

    "atorvastatin": {
        "generic_name": "Atorvastatin",
        "strengths": ["10 mg", "20 mg", "40 mg"],
        "category": "Medicine used to manage cholesterol",
        "generic_alternative": "Generic atorvastatin",
        "affordable_option": "Generic atorvastatin is commonly available at lower prices than branded versions."
    },

    "amlodipine": {
        "generic_name": "Amlodipine",
        "strengths": ["5 mg", "10 mg"],
        "category": "Medicine used to manage high blood pressure",
        "generic_alternative": "Generic amlodipine",
        "affordable_option": "Generic amlodipine is commonly available at lower prices."
    },

    "losartan": {
        "generic_name": "Losartan",
        "strengths": ["25 mg", "50 mg"],
        "category": "Medicine used to manage high blood pressure",
        "generic_alternative": "Generic losartan",
        "affordable_option": "Generic losartan may be available at lower prices."
    },

    "levothyroxine": {
        "generic_name": "Levothyroxine",
        "strengths": ["25 mcg", "50 mcg", "75 mcg", "100 mcg"],
        "category": "Thyroid hormone replacement medicine",
        "generic_alternative": "Generic levothyroxine",
        "affordable_option": "Generic levothyroxine may be available at lower prices."
    },

    "salbutamol": {
        "generic_name": "Salbutamol",
        "strengths": ["2 mg", "4 mg"],
        "category": "Medicine used to relieve breathing difficulty",
        "generic_alternative": "Generic salbutamol",
        "affordable_option": "Generic salbutamol may be available at lower prices."
    },

    "montelukast": {
        "generic_name": "Montelukast",
        "strengths": ["5 mg", "10 mg"],
        "category": "Medicine used for allergy and asthma management",
        "generic_alternative": "Generic montelukast",
        "affordable_option": "Generic montelukast may be available at lower prices."
    },

    "doxycycline": {
        "generic_name": "Doxycycline",
        "strengths": ["100 mg"],
        "category": "Antibiotic",
        "generic_alternative": "Generic doxycycline",
        "affordable_option": "Generic doxycycline may be available at lower prices."
    },

    "ciprofloxacin": {
        "generic_name": "Ciprofloxacin",
        "strengths": ["250 mg", "500 mg"],
        "category": "Antibiotic",
        "generic_alternative": "Generic ciprofloxacin",
        "affordable_option": "Generic ciprofloxacin may be available at lower prices."
    },

    "ondansetron": {
        "generic_name": "Ondansetron",
        "strengths": ["4 mg", "8 mg"],
        "category": "Medicine used to prevent nausea and vomiting",
        "generic_alternative": "Generic ondansetron",
        "affordable_option": "Generic ondansetron may be available at lower prices."
    },

    "vitamin d3": {
        "generic_name": "Vitamin D3",
        "strengths": ["1000 IU", "2000 IU", "60000 IU"],
        "category": "Vitamin supplement",
        "generic_alternative": "Generic vitamin D3",
        "affordable_option": "Generic vitamin D3 may be available at lower prices."
    },

    "calcium": {
        "generic_name": "Calcium",
        "strengths": ["500 mg"],
        "category": "Mineral supplement",
        "generic_alternative": "Generic calcium supplement",
        "affordable_option": "Generic calcium supplements may be available at lower prices."
    }
}

SCHEMES = [
    {
        "name": "Pradhan Mantri Bhartiya Janaushadhi Pariyojana",
        "short_name": "PMBJP",
        "description": "Provides quality generic medicines at affordable prices through Jan Aushadhi Kendras.",
        "relevance": "Useful when a lower-cost generic medicine is available through a Jan Aushadhi Kendra."
    }
]

def find_medicine(medicine_name):
    medicine_name = medicine_name.lower().strip()

    for key, data in MEDICINES.items():
        if key in medicine_name:
            return data

    return None

def find_schemes():
    return SCHEMES
