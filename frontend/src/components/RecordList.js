import React, { useEffect, useState } from 'react';
import { fetchRecords } from '../services/api';

const RecordList = () => {
    const [records, setRecords] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const loadRecords = async () => {
            try {
                const data = await fetchRecords();
                setRecords(data);
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        };

        loadRecords();
    }, []);

    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>Error: {error}</div>;
    }

    return (
        <div>
            <h2>DNS Records</h2>
            <ul>
                {records.map(record => (
                    <li key={record.name}>
                        {record.name} - {record.type}: {record.value}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default RecordList;