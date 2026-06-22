import React from 'react';
import './Portal.css';

const Portal = ({ onEnter }) => {
    return (
        <div className="sentinel-portal">
            <div className="animated-bg"></div>
            <div className="portal-content">
                <header className="fade-in">
                    <div className="logo">SENTINEL-X</div>
                    <p className="tagline">National Intelligence & Multimodal AI Safety Platform</p>
                </header>

                <section className="hero-section fade-in-delayed">
                    <h1>Securing Nigeria's Future Through <span>Multimodal Intelligence</span></h1>
                    <p>
                        The unified core for Computer Vision, Remote Sensing, NLP, and Federated Learning.
                        Designed for National Security, Climate Resilience, and Peacebuilding.
                    </p>
                    <button className="enter-button" onClick={onEnter}>
                        ACCESS COMMAND CENTER
                        <div className="button-glow"></div>
                    </button>
                </section>

                <section className="pillars-grid fade-in-delayed">
                    <div className="pillar-card">
                        <h3>👁️ Vision</h3>
                        <p>Real-time threat & crowd analysis</p>
                    </div>
                    <div className="pillar-card">
                        <h3>📡 Satellite</h3>
                        <p>Remote sensing & NDVI monitoring</p>
                    </div>
                    <div className="pillar-card">
                        <h3>🎙️ NLP</h3>
                        <p>Multilingual speech transcription</p>
                    </div>
                    <div className="pillar-card">
                        <h3>🔐 Federated</h3>
                        <p>Privacy-first edge training</p>
                    </div>
                </section>

                <footer className="fade-in-delayed">
                    <p>© 2026 SENTINEL-X | Developed by Uszkido</p>
                </footer>
            </div>
        </div>
    );
};

export default Portal;
