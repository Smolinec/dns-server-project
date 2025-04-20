import React, { useEffect, useState } from 'react';
import { fetchZones, createZone, deleteZone } from '../services/api';

const ZoneManager = () => {
    const [zones, setZones] = useState([]);
    const [newZone, setNewZone] = useState('');

    useEffect(() => {
        loadZones();
    }, []);

    const loadZones = async () => {
        const fetchedZones = await fetchZones();
        setZones(fetchedZones);
    };

    const handleCreateZone = async () => {
        if (newZone) {
            await createZone({ domain: newZone, records: [] });
            setNewZone('');
            loadZones();
        }
    };

    const handleDeleteZone = async (domain) => {
        await deleteZone(domain);
        loadZones();
    };

    return (
        <div>
            <h2>Manage DNS Zones</h2>
            <input
                type="text"
                value={newZone}
                onChange={(e) => setNewZone(e.target.value)}
                placeholder="Enter new zone domain"
            />
            <button onClick={handleCreateZone}>Create Zone</button>
            <ul>
                {zones.map((zone) => (
                    <li key={zone.domain}>
                        {zone.domain}
                        <button onClick={() => handleDeleteZone(zone.domain)}>Delete</button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ZoneManager;