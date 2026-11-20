MEDICINES = {
    "paracetamol": {
        "generic_name": "Paracetamol",
        "strengths": ["500 mg", "650 mg"],
        "category": "Pain reliever and fever reducer",
        "affordable_option": "Generic paracetamol is usually available at lower prices than branded versions.",
    },
    "amoxicillin": {
        "generic_name": "Amoxicillin",
        "strengths": ["250 mg", "500 mg"],
        "category": "Antibiotic",
        "affordable_option": "Generic amoxicillin may be available at a lower price than branded versions.",
    },
    "metformin": {
        "generic_name": "Metformin",
        "strengths": ["500 mg", "850 mg", "1000 mg"],
        "category": "Medicine used to manage blood glucose",
        "affordable_option": "Generic metformin is commonly available at lower prices than branded versions.",
    }
}


def find_medicine(medicine_name):
    medicine_name = medicine_name.lower().strip()

    for key, data in MEDICINES.items():
        if key in medicine_name:
            return data

    return None
