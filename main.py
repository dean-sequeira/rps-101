import streamlit as st
from st_api_conn import APIConnection
import random
import time

# session state for player score
if 'player_score' not in st.session_state:
    st.session_state['player_score'] = 0

# session state for computer score
if 'computer_score' not in st.session_state:
    st.session_state['computer_score'] = 0

# create connection
conn = st.experimental_connection(name="rps101", type=APIConnection)


@st.cache_data
def get_response(endpoint: str):
    """Get response from API
    :param endpoint: The API endpoint
    :return: The response
    """
    response = conn.get(endpoint)
    return response


# streamlit app
st.title('Rock Paper Scissors 101')
st.write('Rock, paper, scissors? Something else? Take on the battle bot and see who survives.')

# get all objects
objects = get_response("objects/all")
st.write('Make your choice 🤔:')
co1, co2 = st.columns(2)
with co1:
    object1 = st.selectbox('Make your choice', objects, key='object1', label_visibility='collapsed')
with co2:
    battle = st.button('Battle 🤺', type='primary', key='battle')

col1, col2 = st.columns(2, gap='large')

if battle:
    with col1:
        st.write("Player's Choice :")
        st.info(object1)
        st.image(f'images/{object1.lower().replace(".", "")}.png', width=200)

    with col2:
        object2 = random.choice(objects)
        st.write("Bot's Choice :")

        with st.spinner('Processing...'):
            time.sleep(3)
        st.info(object2)
        st.image(f'images/{object2.lower().replace(".", "")}.png', width=200)

    # get result of match
    result = get_response(f"match?object_one={object1}&object_two={object2}")
    if result["winner"] == object1:
        st.header("You Win 🏆")
        st.success(f"{result['winner']} {result['outcome']} {result['loser']}.")
        st.session_state['player_score'] += 1
    elif result["winner"] == object2:
        st.header("You Lose 😵")
        st.error(f"{result['winner']} {result['outcome']} {result['loser']}.")
        st.session_state['computer_score'] += 1
    else:
        st.header("It's a Draw 🤝")
        st.warning(f"{object1} meets {object2}. Nothing to see here.")
        st.balloons()

with st.sidebar:
    st.text('Rock Paper Scissors 101')
    st.write('## Rules')
    st.write('Choose an object, click the :red[**Battle**] button, see who wins. Repeat.')

    st.write('## Score')
    st.write('Player 🧑‍🚀:')
    st.info(st.session_state['player_score'])
    st.write('Bot 🤖:')
    st.info(st.session_state['computer_score'])

    st.write('## About')
    st.write('This app is intended to demo the use of the Streamlit `experimental_connection` feature, using an API'
             ' `ExperimentalBaseConnection`.')
    st.write('The API used for the object list and battle outcomes are from'
             ' [RPS101 API](https://rps101.pythonanywhere.com/api). ')
    st.write('Original idea, and all hand symbol artwork from [UMOP.COM](https://www.umop.com/rps101.htm)')
    st.write('The source code for this app can be found on [GitHub](https://github.com/dean-sequeira/rps-101)')
