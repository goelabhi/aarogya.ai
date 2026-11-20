MEDICINES = {
    "paracetamol": {
        "generic_name": "Paracetamol",
        "strengths": ["500 mg", "650 mg"],
        "category": "Pain reliever and fever reducer",
        "generic_alternative": "Generic paracetamol",
        "affordable_option": "Generic paracetamol is usually available at lower prices than branded versions.",
    },
    "amoxicillin": {
        "generic_name": "Amoxicillin",
        "strengths": ["250 mg", "500 mg"],
        "category": "Antibiotic",
        "generic_alternative": "Generic amoxicillin",
        "affordable_option": "Generic amoxicillin may be available at a lower price than branded versions.",
    },
    "metformin": {
        "generic_name": "Metformin",
        "strengths": ["500 mg", "850 mg", "1000 mg"],
        "category": "Medicine used to manage blood glucose",
        "generic_alternative": "Generic metformin",
        "affordable_option": "Generic metformin is commonly available at lower prices than branded versions.",
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
