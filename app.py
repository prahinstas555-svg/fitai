import streamlit as st
from groq import Groq

# СЮДА ВСТАВЬ СВОЙ КЛЮЧ
api_key = st.secrets["GROQ_API_KEY"]

st.set_page_config(
    page_title="FitAI",
    page_icon="💪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===== ЛЮКС ДИЗАЙН =====
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Montserrat:wght@300;400;600&display=swap');

    .stApp {
        background:
            radial-gradient(circle at 20% 20%, rgba(212,175,55,0.08) 0%, transparent 40%),
            radial-gradient(circle at 80% 80%, rgba(212,175,55,0.06) 0%, transparent 40%),
            linear-gradient(180deg, #0a0a0a 0%, #141414 100%);
        background-attachment: fixed;
    }
    #MainMenu, footer {visibility: hidden;}
    .block-container { max-width: 800px; padding-top: 2rem; }

    /* Боковое меню */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0a0a0a 0%, #1a1a1a 100%);
        border-right: 1px solid rgba(212,175,55,0.2);
    }

    .hero {
        position: relative;
        background:
            linear-gradient(180deg, rgba(0,0,0,0.55) 0%, rgba(0,0,0,0.85) 100%),
            url('https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=1400');
        background-size: cover; background-position: center;
        padding: 80px 40px; border-radius: 28px; text-align: center;
        margin-bottom: 50px; border: 1px solid rgba(212,175,55,0.3);
        box-shadow: 0 25px 70px rgba(0,0,0,0.7), inset 0 0 60px rgba(212,175,55,0.05);
    }
    .hero h1 {
        font-family: 'Playfair Display', serif; font-size: 64px; font-weight: 900; margin: 0;
        background: linear-gradient(135deg, #f9d976 0%, #d4af37 50%, #b8860b 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent; letter-spacing: 2px;
    }
    .hero .line { width: 80px; height: 2px; background: linear-gradient(90deg, transparent, #d4af37, transparent); margin: 20px auto; }
    .hero p {
        font-family: 'Montserrat', sans-serif; color: rgba(255,255,255,0.85);
        font-size: 16px; font-weight: 300; letter-spacing: 3px; text-transform: uppercase; margin: 0;
    }
    .section-title {
        font-family: 'Montserrat', sans-serif; color: #d4af37 !important;
        font-size: 15px; font-weight: 600; letter-spacing: 2px; text-transform: uppercase;
        margin: 28px 0 10px 0;
    }
    .stApp, .stApp p, .stApp label, .stApp span { color: #f0f0f0 !important; font-family: 'Montserrat', sans-serif; }
    .stSelectbox > div > div, .stNumberInput > div > div input {
        background: rgba(255,255,255,0.04) !important; border: 1px solid rgba(212,175,55,0.25) !important;
        border-radius: 14px !important; color: #fff !important; height: 52px !important; padding: 0 16px !important;
    }
    .stNumberInput > div { background: transparent !important; }
    .stSlider [data-baseweb="slider"] div[role="slider"] { background: #d4af37 !important; }
    .stButton > button {
        background: linear-gradient(135deg, #f9d976 0%, #d4af37 50%, #b8860b 100%);
        color: #0a0a0a; font-family: 'Montserrat', sans-serif; font-size: 16px; font-weight: 600;
        letter-spacing: 2px; text-transform: uppercase; padding: 20px 40px; border-radius: 16px;
        border: none; width: 100%; margin-top: 30px; box-shadow: 0 10px 40px rgba(212,175,55,0.4);
        transition: all 0.4s ease;
    }
    .stButton > button:hover { transform: translateY(-3px); box-shadow: 0 18px 50px rgba(212,175,55,0.6); filter: brightness(1.1); }
    .result-card {
        background: rgba(255,255,255,0.03); border: 1px solid rgba(212,175,55,0.3);
        border-radius: 20px; padding: 40px; margin-top: 30px; line-height: 1.9; box-shadow: 0 15px 50px rgba(0,0,0,0.5)    [data-testid="stSidebarCollapseButton"] span,
        [data-testid="stSidebarCollapseButton"] span,
    [data-testid="stSidebarCollapseButton"] p,
    [data-testid="baseButton-headerNoPadding"] span {
        font-size: 0 !important;
    }
    .result-title {
        font-family: 'Playfair Display', serif; color: #d4af37 !important; font-size: 32px;
        font-weight: 700; text-align: center; margin: 40px 0 0 0;
    }
</style>
""", unsafe_allow_html=True)

# ===== МЕНЮ СЛЕВА =====
st.sidebar.markdown("## 💪 FitAI")
st.sidebar.markdown("---")
page = st.sidebar.radio(
    "Меню",
    ["🏠 Главная", "💬 Чат с тренером", "🍎 Калькулятор калорий", "📊 Дневник прогресса"],
    label_visibility="collapsed"
)

# ========== СТРАНИЦА: ГЛАВНАЯ ==========
if page == "🏠 Главная":
    st.markdown("""
    <div class="hero">
        <h1>FitAI</h1>
        <div class="line"></div>
        <p>Персональный ИИ-тренер премиум класса</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">🎯 Твоя цель</div>', unsafe_allow_html=True)
    goal = st.selectbox("g", ["Похудеть", "Набрать мышцы", "Поддерживать форму", "Стать выносливее"], label_visibility="collapsed")

    st.markdown('<div class="section-title">👤 Пол</div>', unsafe_allow_html=True)
    gender = st.radio("ge", ["Мужской", "Женский"], horizontal=True, label_visibility="collapsed")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="section-title">🎂 Возраст</div>', unsafe_allow_html=True)
        age = st.number_input("a", 14, 90, 25, label_visibility="collapsed")
    with col2:
        st.markdown('<div class="section-title">⚖️ Вес</div>', unsafe_allow_html=True)
        weight = st.number_input("w", 30, 200, 70, label_visibility="collapsed")
    with col3:
        st.markdown('<div class="section-title">📏 Рост</div>', unsafe_allow_html=True)
        height = st.number_input("h", 120, 220, 170, label_visibility="collapsed")

    st.markdown('<div class="section-title">💪 Уровень подготовки</div>', unsafe_allow_html=True)
    level = st.select_slider("l", ["Новичок", "Средний", "Продвинутый"], label_visibility="collapsed")

    st.markdown('<div class="section-title">🏠 Где тренируешься</div>', unsafe_allow_html=True)
    place = st.radio("p", ["Дома", "В зале"], horizontal=True, label_visibility="collapsed")

    if st.button("✦ Получить персональный план ✦"):
        with st.spinner("🤖 Создаём твой эксклюзивный план..."):
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])
            prompt = f"""Ты элитный персональный тренер премиум-класса.
Составь план для клиента:
- Цель: {goal}
- Пол: {gender}
- Возраст: {age}
- Вес: {weight} кг
- Рост: {height} см
- Уровень: {level}
- Место: {place}

Дай: 1) план тренировок на неделю, 2) питание, 3) мотивацию.
Пиши стильно, премиально, с эмодзи."""
            response = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama-3.3-70b-versatile"
            )
            plan = response.choices[0].message.content
            st.markdown('<div class="result-title">✦ Твой персональный план ✦</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="result-card">{plan}</div>', unsafe_allow_html=True)

# ========== СТРАНИЦА: ЧАТ ==========
elif page == "💬 Чат с тренером":
    st.markdown('<div class="result-title">💬 Чат с тренером</div>', unsafe_allow_html=True)
    st.write("")

    # Создаём память для переписки (один раз)
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "👋 Привет! Я твой персональный ИИ-тренер. Спрашивай что угодно про тренировки, питание и мотивацию! 💪"}
        ]

    # Показываем всю переписку
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.chat_message("user", avatar="🧑").write(msg["content"])
        else:
            st.chat_message("assistant", avatar="💪").write(msg["content"])

    # Поле ввода вопроса
    user_question = st.chat_input("Напиши свой вопрос...")

    if user_question:
        # Сохраняем вопрос пользователя
        st.session_state.messages.append({"role": "user", "content": user_question})
        st.chat_message("user", avatar="🧑").write(user_question)

        # ИИ отвечает
        with st.chat_message("assistant", avatar="💪"):
            with st.spinner("Думаю..."):
                client = Groq(api_key=st.secrets["GROQ_API_KEY"])
                response = client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": "Ты опытный персональный фитнес-тренер. Отвечай дружелюбно, по делу, с эмодзи. Давай практичные советы про тренировки, питание и мотивацию."},
                        *st.session_state.messages
                    ],
                    model="llama-3.3-70b-versatile"
                )
                answer = response.choices[0].message.content
                st.write(answer)

        # Сохраняем ответ ИИ
        st.session_state.messages.append({"role": "assistant", "content": answer})

# ========== СТРАНИЦА: КАЛЬКУЛЯТОР ==========
elif page == "🍎 Калькулятор калорий":
    st.markdown('<div class="result-title">🍎 Калькулятор калорий</div>', unsafe_allow_html=True)
    st.write("")

    st.markdown('<div class="section-title">👤 Пол</div>', unsafe_allow_html=True)
    c_gender = st.radio("cg", ["Мужской", "Женский"], horizontal=True, label_visibility="collapsed")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="section-title">🎂 Возраст</div>', unsafe_allow_html=True)
        c_age = st.number_input("ca", 14, 90, 25, label_visibility="collapsed")
    with col2:
        st.markdown('<div class="section-title">⚖️ Вес (кг)</div>', unsafe_allow_html=True)
        c_weight = st.number_input("cw", 30, 200, 70, label_visibility="collapsed")
    with col3:
        st.markdown('<div class="section-title">📏 Рост (см)</div>', unsafe_allow_html=True)
        c_height = st.number_input("ch", 120, 220, 170, label_visibility="collapsed")

    st.markdown('<div class="section-title">🏃 Активность</div>', unsafe_allow_html=True)
    activity = st.selectbox("act", [
        "Минимальная (сидячий образ жизни)",
        "Лёгкая (1-2 тренировки в неделю)",
        "Средняя (3-4 тренировки)",
        "Высокая (5-6 тренировок)",
        "Очень высокая (каждый день)"
    ], label_visibility="collapsed")

    st.markdown('<div class="section-title">🎯 Цель</div>', unsafe_allow_html=True)
    c_goal = st.radio("cgo", ["Похудеть", "Поддерживать", "Набрать массу"], horizontal=True, label_visibility="collapsed")

    if st.button("🍎 Рассчитать норму"):
        # Формула Миффлина-Сан Жеора
        if c_gender == "Мужской":
            bmr = 10 * c_weight + 6.25 * c_height - 5 * c_age + 5
        else:
            bmr = 10 * c_weight + 6.25 * c_height - 5 * c_age - 161

        # Коэффициент активности
        coef = {
            "Минимальная (сидячий образ жизни)": 1.2,
            "Лёгкая (1-2 тренировки в неделю)": 1.375,
            "Средняя (3-4 тренировки)": 1.55,
            "Высокая (5-6 тренировок)": 1.725,
            "Очень высокая (каждый день)": 1.9
        }[activity]

        calories = bmr * coef

        # Корректировка под цель
        if c_goal == "Похудеть":
            calories -= 400
        elif c_goal == "Набрать массу":
            calories += 400

        calories = int(calories)

        # БЖУ
        protein = int(c_weight * 2)        # 2г белка на кг
        fat = int(c_weight * 1)            # 1г жира на кг
        carbs = int((calories - protein*4 - fat*9) / 4)

        st.markdown(f"""
        <div class="result-card">
            <div style="text-align:center; font-family:'Playfair Display',serif; font-size:48px; color:#d4af37; font-weight:900;">
                {calories} ккал
            </div>
            <div style="text-align:center; color:rgba(255,255,255,0.7); margin-bottom:30px;">
                твоя дневная норма для цели «{c_goal}»
            </div>
            <div style="display:flex; justify-content:space-around; text-align:center;">
                <div>
                    <div style="font-size:32px; color:#f9d976; font-weight:700;">{protein}г</div>
                    <div style="color:rgba(255,255,255,0.6);">🥩 Белки</div>
                </div>
                <div>
                    <div style="font-size:32px; color:#f9d976; font-weight:700;">{fat}г</div>
                    <div style="color:rgba(255,255,255,0.6);">🥑 Жиры</div>
                </div>
                <div>
                    <div style="font-size:32px; color:#f9d976; font-weight:700;">{carbs}г</div>
                    <div style="color:rgba(255,255,255,0.6);">🍚 Углеводы</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ========== СТРАНИЦА: ДНЕВНИК ==========
elif page == "📊 Дневник прогресса":
    st.markdown('<div class="result-title">📊 Дневник прогресса</div>', unsafe_allow_html=True)
    st.write("")

    # Создаём память для записей (один раз)
    if "progress" not in st.session_state:
        st.session_state.progress = []

    # Поле ввода веса
    st.markdown('<div class="section-title">⚖️ Запиши свой вес сегодня</div>', unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    with col1:
        new_weight = st.number_input("nw", 30.0, 200.0, 70.0, step=0.1, label_visibility="collapsed")
    with col2:
        add = st.button("➕ Добавить")

    if add:
        from datetime import datetime
        st.session_state.progress.append({
            "Дата": datetime.now().strftime("%d.%m %H:%M"),
            "Вес": new_weight
        })
        st.success(f"✅ Записано: {new_weight} кг")

    # Показываем график и таблицу
    if len(st.session_state.progress) > 0:
        import pandas as pd
        df = pd.DataFrame(st.session_state.progress)

        st.markdown('<div class="section-title">📈 График веса</div>', unsafe_allow_html=True)
        st.line_chart(df.set_index("Дата")["Вес"], color="#d4af37")

        # Статистика
        first = st.session_state.progress[0]["Вес"]
        last = st.session_state.progress[-1]["Вес"]
        diff = round(last - first, 1)

        if diff < 0:
            status = f"📉 Минус {abs(diff)} кг — отличный прогресс!"
        elif diff > 0:
            status = f"📈 Плюс {diff} кг"
        else:
            status = "➖ Вес без изменений"

        st.markdown(f"""
        <div class="result-card" style="text-align:center;">
            <div style="font-family:'Playfair Display',serif; font-size:42px; color:#d4af37; font-weight:900;">
                {last} кг
            </div>
            <div style="color:rgba(255,255,255,0.7);">текущий вес</div>
            <div style="font-size:20px; color:#f9d976; margin-top:15px;">{status}</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="section-title">📋 Все записи</div>', unsafe_allow_html=True)
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        st.info("📝 Пока нет записей. Введи свой вес и нажми «Добавить»!")