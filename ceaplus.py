import streamlit as st

st.set_page_config(
    page_title="CEA PLus Mejorado - Inicio",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ========= ESTILOS =========
st.markdown("""
<style>
    /* Ocultar elementos por defecto de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        max-width: 100%;
    }

    html, body, [class*="css"] {
        font-family: 'Arial', sans-serif;
    }

    /* Contenedor general */
    .main-wrapper {
        background: linear-gradient(180deg, #f8fbff 0%, #ffffff 35%, #f7fbff 100%);
    }

    /* Navbar */
    .navbar {
        position: sticky;
        top: 0;
        z-index: 999;
        background: rgba(255,255,255,0.94);
        backdrop-filter: blur(10px);
        border-bottom: 1px solid rgba(15, 76, 129, 0.08);
        padding: 16px 60px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    .brand {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .brand-logo {
        width: 48px;
        height: 48px;
        border-radius: 14px;
        background: linear-gradient(135deg, #0d6efd, #00b4d8);
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 22px;
        font-weight: bold;
        box-shadow: 0 10px 25px rgba(13,110,253,0.20);
    }

    .brand-text {
        line-height: 1.1;
    }

    .brand-title {
        font-size: 1.3rem;
        font-weight: 800;
        color: #083b66;
        margin: 0;
    }

    .brand-subtitle {
        font-size: 0.82rem;
        color: #6b7a90;
        margin: 0;
    }

    .nav-links {
        display: flex;
        gap: 28px;
        align-items: center;
    }

    .nav-links a {
        text-decoration: none;
        color: #27496d;
        font-weight: 600;
        font-size: 0.98rem;
    }

    .nav-links a:hover {
        color: #0d6efd;
    }

    .nav-btn {
        background: linear-gradient(135deg, #0d6efd, #1aa7ec);
        color: white !important;
        padding: 10px 18px;
        border-radius: 999px;
        font-weight: 700;
        box-shadow: 0 10px 24px rgba(13,110,253,0.22);
    }

    /* Hero */
    .hero {
        padding: 70px 70px 40px 70px;
    }

    .hero-grid {
        display: grid;
        grid-template-columns: 1.15fr 0.85fr;
        gap: 34px;
        align-items: center;
    }

    .hero-badge {
        display: inline-block;
        background: rgba(13,110,253,0.10);
        color: #0d6efd;
        padding: 8px 16px;
        border-radius: 999px;
        font-weight: 700;
        font-size: 0.9rem;
        margin-bottom: 18px;
    }

    .hero h1 {
        font-size: 3.2rem;
        line-height: 1.05;
        color: #0a2540;
        margin-bottom: 18px;
        font-weight: 900;
    }

    .hero p {
        font-size: 1.08rem;
        color: #607089;
        line-height: 1.75;
        margin-bottom: 28px;
        max-width: 90%;
    }

    .hero-actions {
        display: flex;
        gap: 14px;
        flex-wrap: wrap;
        margin-top: 10px;
    }

    .btn-primary {
        background: linear-gradient(135deg, #0d6efd, #00b4d8);
        color: white;
        text-decoration: none;
        padding: 14px 24px;
        border-radius: 14px;
        font-weight: 800;
        display: inline-block;
        box-shadow: 0 12px 28px rgba(13,110,253,0.20);
    }

    .btn-secondary {
        background: white;
        color: #0d6efd;
        text-decoration: none;
        padding: 14px 24px;
        border-radius: 14px;
        font-weight: 800;
        display: inline-block;
        border: 1px solid rgba(13,110,253,0.18);
    }

    .hero-card {
        background: white;
        border-radius: 28px;
        padding: 30px;
        box-shadow: 0 20px 45px rgba(19, 72, 128, 0.12);
        border: 1px solid rgba(15, 76, 129, 0.06);
        position: relative;
        overflow: hidden;
    }

    .hero-card::before {
        content: "";
        position: absolute;
        top: -50px;
        right: -50px;
        width: 180px;
        height: 180px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(0,180,216,0.18), transparent 70%);
    }

    .hero-doctor {
        width: 100%;
        min-height: 430px;
        border-radius: 24px;
        background:
            linear-gradient(180deg, rgba(13,110,253,0.12), rgba(0,180,216,0.10)),
            url('https://images.unsplash.com/photo-1559839734-2b71ea197ec2?q=80&w=1400&auto=format&fit=crop') center/cover;
        display: flex;
        align-items: end;
        padding: 24px;
        color: white;
        box-shadow: inset 0 -90px 120px rgba(0,0,0,0.18);
    }

    .hero-doctor-text {
        background: rgba(255,255,255,0.14);
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255,255,255,0.20);
        border-radius: 18px;
        padding: 16px 18px;
        width: 100%;
    }

    .hero-doctor-text h3 {
        margin: 0 0 6px 0;
        font-size: 1.2rem;
        font-weight: 800;
    }

    .hero-doctor-text p {
        margin: 0;
        color: rgba(255,255,255,0.92);
        font-size: 0.95rem;
        line-height: 1.5;
    }

    /* Stats */
    .stats-section {
        padding: 12px 70px 50px 70px;
    }

    .stats-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 18px;
    }

    .stat-card {
        background: white;
        border-radius: 22px;
        padding: 26px;
        box-shadow: 0 15px 35px rgba(19, 72, 128, 0.08);
        border: 1px solid rgba(15, 76, 129, 0.06);
        text-align: center;
    }

    .stat-number {
        font-size: 2rem;
        font-weight: 900;
        color: #0d6efd;
        margin-bottom: 8px;
    }

    .stat-label {
        color: #607089;
        font-weight: 600;
        font-size: 0.96rem;
    }

    /* Secciones */
    .section {
        padding: 70px;
    }

    .section-title {
        text-align: center;
        font-size: 2.4rem;
        color: #0a2540;
        font-weight: 900;
        margin-bottom: 14px;
    }

    .section-desc {
        text-align: center;
        font-size: 1.02rem;
        color: #6a778b;
        max-width: 820px;
        margin: 0 auto 38px auto;
        line-height: 1.8;
    }

    .cards-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 24px;
    }

    .info-card {
        background: white;
        border-radius: 24px;
        padding: 28px;
        box-shadow: 0 18px 40px rgba(19, 72, 128, 0.09);
        border: 1px solid rgba(15, 76, 129, 0.06);
        transition: 0.25s ease;
        min-height: 240px;
    }

    .info-card:hover {
        transform: translateY(-6px);
    }

    .icon-box {
        width: 58px;
        height: 58px;
        border-radius: 18px;
        background: linear-gradient(135deg, rgba(13,110,253,0.12), rgba(0,180,216,0.14));
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 26px;
        margin-bottom: 18px;
    }

    .info-card h3 {
        color: #0a2540;
        font-size: 1.2rem;
        font-weight: 800;
        margin-bottom: 10px;
    }

    .info-card p {
        color: #67768a;
        line-height: 1.7;
        font-size: 0.98rem;
    }

    /* Cursos */
    .course-card {
        background: linear-gradient(180deg, #ffffff, #f6fbff);
        border-radius: 24px;
        padding: 26px;
        border: 1px solid rgba(15, 76, 129, 0.08);
        box-shadow: 0 16px 36px rgba(19, 72, 128, 0.08);
        min-height: 280px;
    }

    .course-tag {
        display: inline-block;
        font-size: 0.78rem;
        background: rgba(13,110,253,0.10);
        color: #0d6efd;
        padding: 7px 12px;
        border-radius: 999px;
        font-weight: 800;
        margin-bottom: 14px;
    }

    .course-card h3 {
        color: #0a2540;
        font-size: 1.25rem;
        font-weight: 800;
        margin-bottom: 10px;
    }

    .course-card p {
        color: #657489;
        line-height: 1.7;
        margin-bottom: 18px;
    }

    .course-meta {
        color: #0d6efd;
        font-weight: 700;
        font-size: 0.95rem;
    }

    /* CTA */
    .cta-box {
        margin: 0 70px 70px 70px;
        padding: 44px;
        border-radius: 30px;
        background: linear-gradient(135deg, #0d6efd, #00b4d8);
        color: white;
        text-align: center;
        box-shadow: 0 24px 50px rgba(13,110,253,0.24);
    }

    .cta-box h2 {
        font-size: 2.3rem;
        margin-bottom: 14px;
        font-weight: 900;
    }

    .cta-box p {
        max-width: 760px;
        margin: 0 auto 22px auto;
        font-size: 1rem;
        line-height: 1.7;
        color: rgba(255,255,255,0.92);
    }

    .footer {
        padding: 24px 40px 40px 40px;
        text-align: center;
        color: #748297;
        font-size: 0.95rem;
    }

    /* Responsive */
    @media (max-width: 1100px) {
        .hero-grid, .cards-grid, .stats-grid {
            grid-template-columns: 1fr !important;
        }

        .navbar {
            padding: 16px 24px;
            flex-direction: column;
            gap: 14px;
        }

        .hero, .section, .stats-section {
            padding-left: 24px;
            padding-right: 24px;
        }

        .cta-box {
            margin-left: 24px;
            margin-right: 24px;
        }

        .hero h1 {
            font-size: 2.35rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# ========= NAVBAR =========
st.markdown("""
<div class="main-wrapper">
    <div class="navbar">
        <div class="brand">
            <div class="brand-logo">+</div>
            <div class="brand-text">
                <p class="brand-title">CEA Medicina</p>
                <p class="brand-subtitle">Plataforma de enseñanza</p>
            </div>
        </div>
        <div class="nav-links">
            <a href="#inicio">Inicio</a>
            <a href="#nosotros">Nosotros</a>
            <a href="#cursos">Cursos</a>
            <a href="#contacto" class="nav-btn">Inscribirme</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ========= HERO =========
st.markdown("""
<div id="inicio" class="hero">
    <div class="hero-grid">
        <div>
            <div class="hero-badge">Formación intensiva para futuros profesionales de salud</div>
            <h1>Prepárate para medicina con una experiencia moderna, clara y profesional</h1>
            <p>
                Una landing educativa con apariencia institucional, enfoque médico y una estructura
                pensada para transmitir confianza, calidad académica y alto rendimiento.
                Esta versión replica el estilo general del sitio de referencia para que luego
                podamos mejorarla con tu contenido real.
            </p>
            <div class="hero-actions">
                <a href="#cursos" class="btn-primary">Ver cursos</a>
                <a href="#nosotros" class="btn-secondary">Conocer más</a>
            </div>
        </div>

        <div class="hero-card">
            <div class="hero-doctor">
                <div class="hero-doctor-text">
                    <h3>Formación académica enfocada en resultados</h3>
                    <p>
                        Imagen perrona de un doctor
                    </p>
                </div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ========= STATS =========
st.markdown("""
<div class="stats-section">
    <div class="stats-grid">
        <div class="stat-card">
            <div class="stat-number">10K+</div>
            <div class="stat-label">Estudiantes alcanzados</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">25+</div>
            <div class="stat-label">Cursos especializados</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">95%</div>
            <div class="stat-label">Satisfacción académica</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">24/7</div>
            <div class="stat-label">Acceso al contenido</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ========= NOSOTROS =========
st.markdown("""
<div id="nosotros" class="section">
    <div class="section-title">¿Por qué elegirnos?</div>
    <div class="section-desc">
        Una plataforma con identidad médica, estructura moderna y una comunicación visual
        que transmite confianza, preparación intensiva y orientación al éxito académico.
    </div>

    <div class="cards-grid">
        <div class="info-card">
            <div class="icon-box">🩺</div>
            <h3>Enfoque médico profesional</h3>
            <p>
                Diseño institucional con una imagen seria, moderna y alineada al sector salud,
                ideal para academias, cursos de preparación y plataformas educativas.
            </p>
        </div>

        <div class="info-card">
            <div class="icon-box">📚</div>
            <h3>Contenido estructurado</h3>
            <p>
                Secciones claras para mostrar cursos, metodología, beneficios, testimonios
                o información institucional sin que la página se vea saturada.
            </p>
        </div>

        <div class="info-card">
            <div class="icon-box">🚀</div>
            <h3>Base perfecta para mejorar</h3>
            <p>
                Primero copiamos la estructura visual general y después podemos agregar
                formularios, login, paneles, métricas, IA o conexión a base de datos.
            </p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ========= CURSOS =========
st.markdown("""
<div id="cursos" class="section" style="background: linear-gradient(180deg, #f7fbff 0%, #ffffff 100%);">
    <div class="section-title">Cursos destacados</div>
    <div class="section-desc">
        Ejemplo de cómo mostrar la oferta académica con tarjetas limpias, etiquetas visuales,
        descripciones cortas y llamadas a la acción.
    </div>

    <div class="cards-grid">
        <div class="course-card">
            <div class="course-tag">Curso VIP</div>
            <h3>Residencia Médica</h3>
            <p>
                Preparación intensiva con simulaciones, material organizado y sesiones orientadas
                a reforzar conceptos clave para exámenes de alto nivel.
            </p>
            <div class="course-meta">Modalidad: Online + Recursos descargables</div>
        </div>

        <div class="course-card">
            <div class="course-tag">Preparación</div>
            <h3>Ingreso a Medicina</h3>
            <p>
                Programa dirigido a estudiantes que buscan una formación sólida en las áreas
                más importantes para su admisión a la carrera.
            </p>
            <div class="course-meta">Modalidad: Clases guiadas + Evaluaciones</div>
        </div>

        <div class="course-card">
            <div class="course-tag">Especial</div>
            <h3>Banco de Preguntas</h3>
            <p>
                Sección pensada para práctica intensiva, seguimiento de avance y resolución
                de preguntas con una interfaz moderna y clara.
            </p>
            <div class="course-meta">Modalidad: Práctica continua</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ========= CTA =========
st.markdown("""
<div id="contacto" class="cta-box">
    <h2>La residencia ya no sera un sueño</h2>
    <p>
        Mas info abajo!
    </p>
    <a href="#" class="btn-secondary" style="background:white; color:#0d6efd;">Solicitar información</a>
</div>

<div class="footer">
    © 2026 - Demo inspirada en una plataforma educativa médica.
</div>
""", unsafe_allow_html=True)
