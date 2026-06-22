import React, { useState, useEffect } from 'react';
import { MapContainer, TileLayer, Marker, Popup, Circle } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import './App.css';
import Portal from './components/Portal';
import './components/Portal.css';

const SentinelDashboard = () => {
    const [view, setView] = useState('portal'); // 'portal' or 'dashboard'
    const [reports, setReports] = useState([]);
    const [selectedReport, setSelectedReport] = useState(null);

    // Mock data for Nigeria locations
    const initialReports = [
        { id: 1, lat: 12.0022, lng: 8.5920, title: "Kano Node", threat: "Low", explanation: "Clear vision, normal NDVI" },
        { id: 2, lat: 6.5244, lng: 3.3792, title: "Lagos Node", threat: "Medium", explanation: "High crowd density detected" },
        { id: 3, lat: 9.0765, lng: 7.3986, title: "Abuja Core", threat: "Safe", explanation: "All systems operational" }
    ];

    useEffect(() => {
        setReports(initialReports);
    }, []);

    if (view === 'portal') {
        return <Portal onEnter={() => setView('dashboard')} />;
    }

    return (
        <div className="sentinel-dashboard dark-mode">
            <header className="glass-panel">
                <h1>SENTINEL-X | Intelligence Dashboard</h1>
                <div className="status-badge pulse">SYSTEM OPERATIONAL</div>
            </header>

            <main>
                <div className="map-container">
                    <MapContainer center={[9.0820, 8.6753]} zoom={6} scrollWheelZoom={false}>
                        <TileLayer
                            url="https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png"
                            attribution='&copy; OpenStreetMap &copy; CARTO'
                        />
                        {reports.map(report => (
                            <Circle
                                key={report.id}
                                center={[report.lat, report.lng]}
                                pathOptions={{ color: report.threat === 'Medium' ? 'red' : 'cyan' }}
                                radius={50000}
                                eventHandlers={{ click: () => setSelectedReport(report) }}
                            />
                        ))}
                    </MapContainer>
                </div>

                <aside className="glass-panel sidebar">
                    <h2>Intelligence Feed</h2>
                    {selectedReport ? (
                        <div className="report-detail">
                            <h3>{selectedReport.title}</h3>
                            <div className="threat-level" data-level={selectedReport.threat}>
                                Threat: {selectedReport.threat}
                            </div>
                            <p><strong>XAI Explanation:</strong></p>
                            <p className="explanation-text">{selectedReport.explanation}</p>
                            <div className="multimodal-view">
                                <div className="view-slot">Vision Feed</div>
                                <div className="view-slot">Audio Waveform</div>
                            </div>
                        </div>
                    ) : (
                        <div className="empty-state">Select a hotspot on the map to analyze</div>
                    )}
                </aside>
            </main>
        </div>
    );
};

export default SentinelDashboard;
