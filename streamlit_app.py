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
    for day in workout_plan_dict:
        if workout_type == 1:  # Cardio
            workout_plan_dict[day] = [f"{time_available} minutes of moderate running or cycling"]
        elif workout_type == 2:  # Strength Training
            workout_plan_dict[day] = [f"{time_available} minutes of circuit training with {equipment_level(equipment)}"]
        elif workout_type == 3:  # Flexibility
            workout_plan_dict[day] = [f"{time_available} minutes of yoga or Pilates"]
        elif workout_type == 4:  # HIIT
            workout_plan_dict[day] = [f"{time_available} minutes of high-intensity interval training"]
        elif workout_type == 5:  # Mixed
            workout_plan_dict[day] = [f"{time_available // 2} minutes of cardio and {time_available // 2} minutes of strength training"]
    return workout_plan_dict

def muscle_gain_plan(workout_plan_dict, workout_type, time_available, experience_level, equipment):
    """Generates a muscle gain plan based on user preferences."""
    for day in workout_plan_dict:
        if workout_type == 1:  # Cardio
            workout_plan_dict[day] = [f"{time_available // 3} minutes of light cardio and {time_available * 2 // 3} minutes of focused strength training with {equipment_level(equipment)}"]
        elif workout_type == 2:  # Strength Training
            workout_plan_dict[day] = [f"{time_available} minutes of heavy lifting with {equipment_level(equipment)} (e.g., compound exercises)"]
        elif workout_type == 3:  # Flexibility
            workout_plan_dict[day] = [f"{time_available} minutes of dynamic stretching and light resistance training"]
        elif workout_type == 4:  # HIIT
            workout_plan_dict[day] = [f"{time_available // 2} minutes of strength-focused HIIT and {time_available // 2} minutes of accessory work"]
        elif workout_type == 5:  # Mixed
            workout_plan_dict[day] = [f"{time_available // 2} minutes of strength training and {time_available // 2} minutes of hypertrophy-focused exercises"]
    return workout_plan_dict

def maintenance_plan(workout_plan_dict, workout_type, time_available, experience_level, equipment):
    """Generates a maintenance plan based on user preferences."""
    for day in workout_plan_dict:
        if workout_type == 1:  # Cardio
            workout_plan_dict[day] = [f"{time_available // 2} minutes of moderate cardio and {time_available // 2} minutes of strength maintenance with {equipment_level(equipment)}"]
        elif workout_type == 2:  # Strength Training
            workout_plan_dict[day] = [f"{time_available} minutes of balanced strength and endurance training with {equipment_level(equipment)}"]
        elif workout_type == 3:  # Flexibility
            workout_plan_dict[day] = [f"{time_available} minutes of mixed stretching and light cardio for mobility"]
        elif workout_type == 4:  # HIIT
            workout_plan_dict[day] = [f"{time_available // 2} minutes of HIIT and {time_available // 2} minutes of endurance training or active recovery"]
        elif workout_type == 5:  # Mixed
            workout_plan_dict[day] = [f"{time_available // 2} minutes of cardio and {time_available // 2} minutes of strength maintenance"]
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
