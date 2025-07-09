import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime
import random
import json

# Set page configuration
st.set_page_config(
    page_title="Rational Function Quest",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Nintendo-style design
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
    
    .main-title {
        font-family: 'Press Start 2P', cursive;
        color: #E53E3E;
        text-align: center;
        font-size: 24px;
        margin-bottom: 20px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    
    .level-indicator {
        font-family: 'Press Start 2P', cursive;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        margin: 10px 0;
        font-size: 12px;
    }
    
    .level-1 { background-color: #68D391; color: white; }
    .level-2 { background-color: #4FD1C7; color: white; }
    .level-3 { background-color: #F6AD55; color: white; }
    .level-4 { background-color: #B794F6; color: white; }
    .level-5 { background-color: #F56565; color: white; }
    
    .score-display {
        font-family: 'Press Start 2P', cursive;
        background-color: #FFF5B7;
        padding: 15px;
        border-radius: 10px;
        border: 3px solid #F6E05E;
        text-align: center;
        margin: 10px 0;
    }
    
    .function-display {
        font-family: 'Courier New', monospace;
        font-size: 24px;
        text-align: center;
        background-color: #2D3748;
        color: white;
        padding: 20px;
        border-radius: 10px;
        margin: 15px 0;
        border: 3px solid #4A5568;
    }
    
    .nintendo-button {
        font-family: 'Press Start 2P', cursive;
        font-size: 12px;
        padding: 10px 20px;
        border-radius: 8px;
        border: none;
        box-shadow: 0 4px 0 #2D3748;
        transition: all 0.1s ease;
        margin: 5px;
    }
    
    .nintendo-button:active {
        transform: translateY(2px);
        box-shadow: 0 2px 0 #2D3748;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'game_state' not in st.session_state:
    st.session_state.game_state = {
        'player_name': '',
        'current_level': 1,
        'score': 0,
        'correct_answers': 0,
        'total_questions': 0,
        'current_question': None,
        'game_started': False,
        'leaderboard': []
    }

# Rational function definitions for each level
LEVEL_FUNCTIONS = {
    1: [  # Beginner - Basic linear over linear
        {
            'function': 'f(x) = (x + 2) / (x - 1)',
            'vertical_asymptotes': [1],
            'horizontal_asymptote': 1,
            'holes': [],
            'x_intercepts': [-2],
            'y_intercept': -2,
            'correct_answer': 'A'
        },
        {
            'function': 'f(x) = (x - 3) / (x + 1)',
            'vertical_asymptotes': [-1],
            'horizontal_asymptote': 1,
            'holes': [],
            'x_intercepts': [3],
            'y_intercept': -3,
            'correct_answer': 'B'
        }
    ],
    2: [  # Apprentice - Functions with holes
        {
            'function': 'f(x) = (x + 2)(x - 3) / [(x - 1)(x - 3)]',
            'vertical_asymptotes': [1],
            'horizontal_asymptote': 1,
            'holes': [3],
            'x_intercepts': [-2],
            'y_intercept': 2,
            'correct_answer': 'A'
        }
    ],
    3: [  # Skilled - Linear over quadratic
        {
            'function': 'f(x) = (2x + 4) / (x² - 1)',
            'vertical_asymptotes': [-1, 1],
            'horizontal_asymptote': 0,
            'holes': [],
            'x_intercepts': [-2],
            'y_intercept': -4,
            'correct_answer': 'B'
        }
    ],
    4: [  # Expert - Quadratic over quadratic
        {
            'function': 'f(x) = (x² + 2x - 3) / (x² - 1)',
            'vertical_asymptotes': [-1, 1],
            'horizontal_asymptote': 1,
            'holes': [],
            'x_intercepts': [-3, 1],
            'y_intercept': 3,
            'correct_answer': 'A'
        }
    ],
    5: [  # Master - Complex functions
        {
            'function': 'f(x) = (x² - 4)(x + 1) / [(x - 2)(x + 1)(x - 3)]',
            'vertical_asymptotes': [2, 3],
            'horizontal_asymptote': None,
            'holes': [-1],
            'x_intercepts': [-2, 2],
            'y_intercept': 4/3,
            'correct_answer': 'B'
        }
    ]
}

def get_level_name(level):
    level_names = {1: "BEGINNER", 2: "APPRENTICE", 3: "SKILLED", 4: "EXPERT", 5: "MASTER"}
    return level_names.get(level, "UNKNOWN")

def get_level_color(level):
    colors = {1: "level-1", 2: "level-2", 3: "level-3", 4: "level-4", 5: "level-5"}
    return colors.get(level, "level-1")

def create_sample_graph(function_data, option='A'):
    """Create a sample graph for the rational function"""
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Create x values
    x = np.linspace(-10, 10, 1000)
    
    # Simple function evaluation (this would need proper parsing for real functions)
    # For demo purposes, showing basic patterns
    if option == 'A':
        # Correct graph pattern
        y = (x + 2) / (x - 1)  # Example function
        # Handle vertical asymptotes
        y = np.where(np.abs(x - 1) < 0.1, np.nan, y)
    else:
        # Incorrect variations
        y = (x + 2) / (x + 1)  # Different asymptote
        y = np.where(np.abs(x + 1) < 0.1, np.nan, y)
    
    # Plot the function
    ax.plot(x, y, 'b-', linewidth=2, label=f'Option {option}')
    
    # Add vertical asymptotes
    for va in function_data['vertical_asymptotes']:
        ax.axvline(x=va, color='red', linestyle='--', alpha=0.7, label=f'V.A. x={va}')
    
    # Add horizontal asymptote
    if function_data['horizontal_asymptote'] is not None:
        ax.axhline(y=function_data['horizontal_asymptote'], color='blue', linestyle='--', alpha=0.7, 
                  label=f'H.A. y={function_data["horizontal_asymptote"]}')
    
    # Mark holes
    for hole in function_data['holes']:
        ax.plot(hole, 0, 'ro', markersize=8, fillstyle='none', markeredgewidth=2, label=f'Hole at x={hole}')
    
    # Mark intercepts
    for x_int in function_data['x_intercepts']:
        ax.plot(x_int, 0, 'go', markersize=8, label=f'x-int: ({x_int}, 0)')
    
    ax.plot(0, function_data['y_intercept'], 'mo', markersize=8, label=f'y-int: (0, {function_data["y_intercept"]})')
    
    ax.set_xlim(-8, 8)
    ax.set_ylim(-8, 8)
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(f'Graph Option {option}')
    ax.legend()
    
    return fig

def main():
    # Title
    st.markdown('<h1 class="main-title">🎮 RATIONAL FUNCTION QUEST 🎮</h1>', unsafe_allow_html=True)
    
    # Game setup
    if not st.session_state.game_state['game_started']:
        st.markdown("### Enter Your Name to Start the Quest!")
        player_name = st.text_input("Player Name:", max_chars=12)
        
        if st.button("🚀 START QUEST", key="start_game"):
            if player_name:
                st.session_state.game_state['player_name'] = player_name
                st.session_state.game_state['game_started'] = True
                st.rerun()
    
    else:
        # Game header
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f'<div class="score-display">🏆 Score: {st.session_state.game_state["score"]}</div>', unsafe_allow_html=True)
        
        with col2:
            level = st.session_state.game_state['current_level']
            st.markdown(f'<div class="level-indicator {get_level_color(level)}">{get_level_name(level)} - Level {level}</div>', unsafe_allow_html=True)
        
        with col3:
            accuracy = (st.session_state.game_state['correct_answers'] / max(st.session_state.game_state['total_questions'], 1)) * 100
            st.markdown(f'<div class="score-display">🎯 Accuracy: {accuracy:.1f}%</div>', unsafe_allow_html=True)
        
        # Generate question if none exists
        if st.session_state.game_state['current_question'] is None:
            level = st.session_state.game_state['current_level']
            functions = LEVEL_FUNCTIONS[level]
            st.session_state.game_state['current_question'] = random.choice(functions)
        
        current_q = st.session_state.game_state['current_question']
        
        # Display current function
        st.markdown(f'<div class="function-display">{current_q["function"]}</div>', unsafe_allow_html=True)
        
        st.markdown("### 📊 Choose the Correct Graph")
        st.markdown("**Instructions:** Look for vertical asymptotes, horizontal asymptotes, holes, and intercepts.")
        
        # Create graph options
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Option A**")
            fig_a = create_sample_graph(current_q, 'A')
            st.pyplot(fig_a)
            
            st.markdown("**Option C**")
            fig_c = create_sample_graph(current_q, 'C')
            st.pyplot(fig_c)
        
        with col2:
            st.markdown("**Option B**")
            fig_b = create_sample_graph(current_q, 'B')
            st.pyplot(fig_b)
            
            st.markdown("**Option D**")
            fig_d = create_sample_graph(current_q, 'D')
            st.pyplot(fig_d)
        
        # Answer selection
        st.markdown("### Select Your Answer:")
        answer_col1, answer_col2, answer_col3, answer_col4 = st.columns(4)
        
        with answer_col1:
            if st.button("🔴 Option A", key="option_a"):
                check_answer('A')
        
        with answer_col2:
            if st.button("🟢 Option B", key="option_b"):
                check_answer('B')
        
        with answer_col3:
            if st.button("🟠 Option C", key="option_c"):
                check_answer('C')
        
        with answer_col4:
            if st.button("🟣 Option D", key="option_d"):
                check_answer('D')
        
        # Sidebar with hints and progress
        with st.sidebar:
            st.markdown("### 💡 Power-Up Hints")
            if st.session_state.game_state['current_level'] == 1:
                st.info("🎯 Look for where the denominator equals zero to find vertical asymptotes!")
            elif st.session_state.game_state['current_level'] == 2:
                st.info("🕳️ Common factors in numerator and denominator create holes!")
            elif st.session_state.game_state['current_level'] == 3:
                st.info("📊 Linear over quadratic: multiple vertical asymptotes possible")
            elif st.session_state.game_state['current_level'] == 4:
                st.info("🏆 Same degree polynomials: horizontal asymptote = ratio of leading coefficients")
            else:
                st.info("👑 MASTER LEVEL: Analyze complex rational functions step by step")
            
            st.markdown("### 🎮 Player Stats")
            st.write(f"**Player:** {st.session_state.game_state['player_name']}")
            st.write(f"**Correct Answers:** {st.session_state.game_state['correct_answers']}")
            st.write(f"**Total Questions:** {st.session_state.game_state['total_questions']}")
            
            if st.button("🔄 New Game"):
                st.session_state.game_state = {
                    'player_name': '',
                    'current_level': 1,
                    'score': 0,
                    'correct_answers': 0,
                    'total_questions': 0,
                    'current_question': None,
                    'game_started': False,
                    'leaderboard': []
                }
                st.rerun()

def check_answer(selected_option):
    """Check if the selected answer is correct"""
    current_q = st.session_state.game_state['current_question']
    correct = selected_option == current_q['correct_answer']
    
    st.session_state.game_state['total_questions'] += 1
    
    if correct:
        st.session_state.game_state['correct_answers'] += 1
        st.session_state.game_state['score'] += 100 + (st.session_state.game_state['current_level'] * 75)
        st.success("🎉 Correct! Great job!")
        
        # Level up logic
        if st.session_state.game_state['total_questions'] % 3 == 0:
            if st.session_state.game_state['current_level'] < 5:
                st.session_state.game_state['current_level'] += 1
                st.balloons()
                st.success(f"🎊 Level Up! Welcome to {get_level_name(st.session_state.game_state['current_level'])} level!")
    else:
        st.error(f"❌ Incorrect! The correct answer was {current_q['correct_answer']}")
    
    # Generate new question
    st.session_state.game_state['current_question'] = None
    
    # Auto-refresh after a short delay
    st.rerun()

if __name__ == "__main__":
    main()