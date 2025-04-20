import axios from 'axios';

const API_URL = 'http://localhost:8000'; // Adjust the URL as needed

export const getZones = async () => {
    const response = await axios.get(`${API_URL}/zones`);
    return response.data;
};

export const createZone = async (zone) => {
    const response = await axios.post(`${API_URL}/zones`, zone);
    return response.data;
};

export const getZone = async (domain) => {
    const response = await axios.get(`${API_URL}/zones/${domain}`);
    return response.data;
};

export const deleteZone = async (domain) => {
    await axios.delete(`${API_URL}/zones/${domain}`);
};

export const addRecord = async (domain, record) => {
    const response = await axios.post(`${API_URL}/zones/${domain}/records`, record);
    return response.data;
};

export const deleteRecord = async (domain, name, type) => {
    await axios.delete(`${API_URL}/zones/${domain}/records?name=${name}&type=${type}`);
};