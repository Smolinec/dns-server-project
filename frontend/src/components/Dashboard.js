import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Dashboard = () => {
    const [zones, setZones] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchZones = async () => {
            try {
                const response = await axios.get('/api/zones');
                setZones(response.data);
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        };

        fetchZones();
    }, []);

    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>Error: {error}</div>;
    }

    return (
        <div>
            <h1>DNS Zones</h1>
            <ul>
                {zones.map(zone => (
                    <li key={zone.domain}>
                        <h2>{zone.domain}</h2>
                        <ul>
                            {zone.records.map(record => (
                                <li key={record.name}>
                                    {record.type}: {record.value}
                                </li>
                            ))}
                        </ul>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Dashboard;