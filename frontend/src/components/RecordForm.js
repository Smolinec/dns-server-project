import React, { useState } from 'react';
import axios from 'axios';

const RecordForm = ({ onRecordAdded }) => {
    const [name, setName] = useState('');
    const [type, setType] = useState('A');
    const [value, setValue] = useState('');
    const [ttl, setTtl] = useState(3600);
    const [priority, setPriority] = useState(10);
    const [error, setError] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');

        const recordData = {
            name,
            type,
            value,
            ttl: parseInt(ttl),
        };

        if (type === 'MX') {
            recordData.priority = parseInt(priority);
        }

        try {
            const response = await axios.post(`/zones/${name}/records`, recordData);
            onRecordAdded(response.data);
            setName('');
            setValue('');
            setTtl(3600);
            setPriority(10);
        } catch (err) {
            setError('Error adding record: ' + err.response.data.detail);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <h2>Add DNS Record</h2>
            {error && <p className="error">{error}</p>}
            <div>
                <label>Name:</label>
                <input type="text" value={name} onChange={(e) => setName(e.target.value)} required />
            </div>
            <div>
                <label>Type:</label>
                <select value={type} onChange={(e) => setType(e.target.value)}>
                    <option value="A">A</option>
                    <option value="AAAA">AAAA</option>
                    <option value="MX">MX</option>
                    <option value="CNAME">CNAME</option>
                    <option value="TXT">TXT</option>
                    <option value="NS">NS</option>
                </select>
            </div>
            <div>
                <label>Value:</label>
                <input type="text" value={value} onChange={(e) => setValue(e.target.value)} required />
            </div>
            <div>
                <label>TTL:</label>
                <input type="number" value={ttl} onChange={(e) => setTtl(e.target.value)} />
            </div>
            {type === 'MX' && (
                <div>
                    <label>Priority:</label>
                    <input type="number" value={priority} onChange={(e) => setPriority(e.target.value)} />
                </div>
            )}
            <button type="submit">Add Record</button>
        </form>
    );
};

export default RecordForm;