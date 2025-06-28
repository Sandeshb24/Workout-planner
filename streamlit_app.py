import streamlit as st

# --- workout_plan.py content (copied and adapted for direct use in Streamlit app) ---
# In a real scenario, you would import these from workout_plan.py
def equipment_level(equipment_choice):
    """Maps equipment choice number to a descriptive string."""
    if equipment_choice == 1:
        return "no equipment"
    elif equipment_choice == 2:
        return "basic equipment (dumbbells, resistance bands)"
    elif equipment_choice == 3:
        return "full gym access"
    return "unknown equipment" # Fallback

def weight_loss_plan(workout_plan_dict, workout_type, time_available, experience_level, equipment):
    """Generates a weight loss plan based on user preferences."""
    cardio_options = [
        "moderate running or cycling", "brisk walking on incline", "elliptical or stair climbing", "swimming laps", "dancing or cardio kickboxing"
    ]
    strength_options = [
        f"circuit training with {equipment_level(equipment)} (e.g., squats, lunges, push-ups, planks)",
        f"full-body dumbbell workout focusing on compound movements with {equipment_level(equipment)}",
        f"bodyweight strength exercises (e.g., burpees, mountain climbers, tricep dips)",
        f"resistance band and bodyweight exercises for core and glutes with {equipment_level(equipment)}",
        f"HIIT-style strength intervals using {equipment_level(equipment)}"
    ]
    flexibility_options = [
        "yoga flow for calorie burn and flexibility", "Pilates for core strength and lengthening",
        "dynamic stretching followed by foam rolling", "active recovery with light stretching and mobility drills"
    ]
    hiit_options = [
        "sprint intervals on treadmill or outdoors", "Tabata protocol with bodyweight exercises",
        "plyometric drills and jump squats", "cycling or rowing machine intervals",
        "metabolic conditioning using battle ropes or sled push"
    ]
    mixed_options = [
        f"{time_available // 2} minutes of cardio and {time_available // 2} minutes of strength training",
        f"alternating days of intense cardio and full-body strength with {equipment_level(equipment)}",
        f"cross-training: combine a cardio machine with a strength circuit",
        f"cardio + flexibility: {time_available // 2} mins running, {time_available // 2} mins yoga",
        f"HIIT + strength: {time_available // 2} mins HIIT, {time_available // 2} mins bodyweight strength"
    ]

    day_index = 0
    for day in workout_plan_dict:
        if workout_type == 1:  # Cardio
            workout_plan_dict[day] = [f"{time_available} minutes of {cardio_options[day_index % len(cardio_options)]}"]
        elif workout_type == 2:  # Strength Training
            workout_plan_dict[day] = [f"{time_available} minutes of {strength_options[day_index % len(strength_options)]}"]
        elif workout_type == 3:  # Flexibility
            workout_plan_dict[day] = [f"{time_available} minutes of {flexibility_options[day_index % len(flexibility_options)]}"]
        elif workout_type == 4:  # HIIT
            workout_plan_dict[day] = [f"{time_available} minutes of {hiit_options[day_index % len(hiit_options)]}"]
        elif workout_type == 5:  # Mixed
            workout_plan_dict[day] = [f"{mixed_options[day_index % len(mixed_options)]}"]
        day_index += 1
    return workout_plan_dict

def muscle_gain_plan(workout_plan_dict, workout_type, time_available, experience_level, equipment):
    """Generates a muscle gain plan based on user preferences."""
    cardio_options = [
        "light cardio (e.g., incline walking, cycling) paired with focused strength training",
        "post-workout cardio for active recovery (15-20 mins)",
        "warm-up cardio before heavy lifting", "steady-state cardio on rest days"
    ]
    strength_options = [
        f"heavy lifting for chest & triceps with {equipment_level(equipment)} (e.g., bench press, overhead press, tricep extensions)",
        f"heavy lifting for back & biceps with {equipment_level(equipment)} (e.g., pull-ups, rows, bicep curls)",
        f"heavy lifting for legs & shoulders with {equipment_level(equipment)} (e.g., squats, deadlifts, lunges, shoulder press)",
        f"full-body compound movements focusing on progressive overload with {equipment_level(equipment)}",
        f"strength circuit emphasizing hypertrophy for major muscle groups with {equipment_level(equipment)}"
    ]
    flexibility_options = [
        "dynamic stretching before workout, static stretching after", "foam rolling and mobility work for recovery",
        "PNF stretching for muscle lengthening", "active recovery with light stretching and joint rotations"
    ]
    hiit_options = [
        "strength-focused HIIT with compound lifts and short rests",
        "plyometric HIIT drills for explosive power (e.g., box jumps, broad jumps)",
        "kettlebell swings and other power movements in HIIT format",
        "sprint intervals followed by bodyweight strength work"
    ]
    mixed_options = [
        f"{time_available // 2} minutes of strength training and {time_available // 2} minutes of hypertrophy-focused exercises",
        f"strength training split with short, intense cardio bursts",
        f"focus on one major muscle group (e.g., legs) with {equipment_level(equipment)}, followed by light cardio",
        f"upper/lower split days with specific compound and isolation exercises with {equipment_level(equipment)}",
        f"powerlifting-style workout with accessory exercises"
    ]

    day_index = 0
    for day in workout_plan_dict:
        if workout_type == 1:  # Cardio
            workout_plan_dict[day] = [f"{time_available // 3} minutes of {cardio_options[day_index % len(cardio_options)]}"]
        elif workout_type == 2:  # Strength Training
            workout_plan_dict[day] = [f"{time_available} minutes of {strength_options[day_index % len(strength_options)]}"]
        elif workout_type == 3:  # Flexibility
            workout_plan_dict[day] = [f"{time_available} minutes of {flexibility_options[day_index % len(flexibility_options)]}"]
        elif workout_type == 4:  # HIIT
            workout_plan_dict[day] = [f"{time_available // 2} minutes of {hiit_options[day_index % len(hiit_options)]}"]
        elif workout_type == 5:  # Mixed
            workout_plan_dict[day] = [f"{mixed_options[day_index % len(mixed_options)]}"]
        day_index += 1
    return workout_plan_dict


def maintenance_plan(workout_plan_dict, workout_type, time_available, experience_level, equipment):
    """Generates a maintenance plan based on user preferences."""
    cardio_options = [
        "moderate cardio (e.g., jogging, cycling, brisk walking)", "recreational sports (e.g., basketball, tennis)",
        "hiking or trail walking", "dancing or active games", "swimming or water aerobics"
    ]
    strength_options = [
        f"balanced strength and endurance training with {equipment_level(equipment)} (e.g., compound lifts with moderate weight)",
        f"full-body resistance training with {equipment_level(equipment)} for muscle tone",
        f"functional strength exercises to improve daily movement with {equipment_level(equipment)}",
        f"circuit workout blending strength and cardio with {equipment_level(equipment)}",
        f"core and stability training with {equipment_level(equipment)}"
    ]
    flexibility_options = [
        "mixed stretching and light cardio for overall mobility", "Pilates or Barre for core and flexibility",
        "restorative yoga or deep stretching for recovery", "active recovery walks with light stretching"
    ]
    hiit_options = [
        "short HIIT session for cardiovascular health and metabolism boost",
        "sprint intervals or jump rope drills", "bodyweight HIIT with active rest",
        "circuit of cardio and bodyweight strength intervals"
    ]
    mixed_options = [
        f"{time_available // 2} minutes of cardio and {time_available // 2} minutes of strength maintenance",
        f"balanced workout with a mix of endurance and light resistance",
        f"active recovery day with light cardio and stretching",
        f"cross-training session (e.g., swim + bodyweight strength)",
        f"light gym session with focus on form and controlled movements"
    ]

    day_index = 0
    for day in workout_plan_dict:
        if workout_type == 1:  # Cardio
            workout_plan_dict[day] = [f"{time_available} minutes of {cardio_options[day_index % len(cardio_options)]}"]
        elif workout_type == 2:  # Strength Training
            workout_plan_dict[day] = [f"{time_available} minutes of {strength_options[day_index % len(strength_options)]}"]
        elif workout_type == 3:  # Flexibility
            workout_plan_dict[day] = [f"{time_available} minutes of {flexibility_options[day_index % len(flexibility_options)]}"]
        elif workout_type == 4:  # HIIT
            workout_plan_dict[day] = [f"{time_available // 2} minutes of {hiit_options[day_index % len(hiit_options)]} and {time_available // 2} minutes of endurance training or active recovery"]
        elif workout_type == 5:  # Mixed
            workout_plan_dict[day] = [f"{mixed_options[day_index % len(mixed_options)]}"]
        day_index += 1
    return workout_plan_dict

def generate_workout_plan(user_data):
    """
    Generates a personalized weekly workout plan based on user data.
    """
    goal = user_data['goal']
    workout_type = user_data['workout_type']
    experience_level = user_data['experience_level'] # Not directly used in current plan logic but kept for future expansion
    equipment = user_data['equipment']
    time_available = user_data['time_available']
    
    workout_plan = {
        'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [],
        'Friday': [], 'Saturday': [], 'Sunday': []
    }
    
    if goal == 1:  # Weight Loss
        workout_plan = weight_loss_plan(workout_plan, workout_type, time_available, experience_level, equipment)
    elif goal == 2:  # Muscle Gain
        workout_plan = muscle_gain_plan(workout_plan, workout_type, time_available, experience_level, equipment)
    elif goal == 3:  # Maintenance
        workout_plan = maintenance_plan(workout_plan, workout_type, time_available, experience_level, equipment)
    
    return workout_plan

# --- Streamlit App ---

st.set_page_config(page_title="Gym AI Workout Planner", layout="centered")

st.title("🏋️‍♀️ Gym AI Workout Planner")
st.markdown("Enter your details to get a personalized weekly workout plan!")

with st.form("workout_form"):
    st.header("Your Personal Information")
    name = st.text_input("Your Name", placeholder="John Doe")
    age = st.number_input("Your Age", min_value=12, max_value=100, value=25)
    gender = st.selectbox("Your Gender", ["Male", "Female", "Other"])
    height = st.number_input("Your Height (cm)", min_value=100.0, max_value=250.0, value=170.0, step=0.1)
    weight = st.number_input("Your Weight (kg)", min_value=30.0, max_value=300.0, value=70.0, step=0.1)

    st.header("Your Fitness Preferences")
    goal = st.selectbox(
        "Your Fitness Goal",
        options=[
            (1, "Weight Loss"),
            (2, "Muscle Gain"),
            (3, "Maintenance")
        ],
        format_func=lambda x: x[1] # Display the string part of the tuple
    )
    # Extract the integer value for the goal
    goal_value = goal[0]

    activity_level = st.selectbox(
        "Your Activity Level",
        options=[
            (1, "Sedentary (little or no exercise)"),
            (2, "Light Activity (light exercise/sports 1-3 days a week)"),
            (3, "Moderate Activity (moderate exercise/sports 3-5 days a week)"),
            (4, "Active (intense exercise/sports 6-7 days a week)"),
            (5, "Very Active (very intense exercise, physical job, or training)")
        ],
        format_func=lambda x: x[1]
    )
    activity_level_value = activity_level[0]

    workout_type = st.selectbox(
        "Your Preferred Workout Type",
        options=[
            (1, "Cardio"),
            (2, "Strength Training"),
            (3, "Flexibility"),
            (4, "HIIT (High-Intensity Interval Training)"),
            (5, "Mixed (Cardio and Strength)")
        ],
        format_func=lambda x: x[1]
    )
    workout_type_value = workout_type[0]

    experience_level = st.selectbox(
        "Your Experience Level",
        options=[
            (1, "Beginner"),
            (2, "Intermediate"),
            (3, "Advanced")
        ],
        format_func=lambda x: x[1]
    )
    experience_level_value = experience_level[0]

    equipment = st.selectbox(
        "Available Equipment",
        options=[
            (1, "No Equipment"),
            (2, "Basic Equipment (dumbbells, resistance bands)"),
            (3, "Full Gym Access")
        ],
        format_func=lambda x: x[1]
    )
    equipment_value = equipment[0]

    time_available = st.number_input("Time Available for Workout Each Day (in minutes)", min_value=15, max_value=240, value=60, step=5)

    submitted = st.form_submit_button("Generate Workout Plan")

    if submitted:
        if not name:
            st.error("Please enter your name.")
        else:
            user_data = {
                'name': name,
                'age': age,
                'gender': gender,
                'height': height,
                'weight': weight,
                'goal': goal_value,
                'activity_level': activity_level_value,
                'workout_type': workout_type_value,
                'experience_level': experience_level_value,
                'equipment': equipment_value,
                'time_available': time_available
            }
            
            st.subheader(f"Hello, {name}! Here is your personalized weekly workout plan:")
            
            workout_plan = generate_workout_plan(user_data)
            
            for day, exercises in workout_plan.items():
                if exercises: # Only display days with planned exercises
                    st.markdown(f"**{day}:**")
                    for exercise in exercises:
                        st.write(f"- {exercise}")
                else:
                    st.markdown(f"**{day}:** Rest or active recovery.")

st.markdown("""
<style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        padding: 0.75rem 1.5rem;
        border-radius: 0.5rem;
        border: none;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #45a049;
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
    }
    .stTextInput>div>div>input, .stNumberInput>div>div>input, .stSelectbox>div>div>div {
        border-radius: 0.5rem;
        border: 1px solid #ddd;
        padding: 0.5rem;
    }
    .stForm {
        background-color: #f9f9f9;
        padding: 2rem;
        border-radius: 1rem;
        box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
    }
    h1, h2, h3 {
        color: #333;
        font-family: 'Inter', sans-serif;
    }
    p, li {
        font-family: 'Inter', sans-serif;
        color: #555;
    }
</style>
""", unsafe_allow_html=True)
